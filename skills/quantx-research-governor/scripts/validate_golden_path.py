#!/usr/bin/env python3
"""Validate the synthetic QuantX governor lifecycle fixture."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = SKILL_DIR / "assets/golden_path_fixture/lifecycle.json"
STAGE_ORDER = (
    "intake",
    "goal_contract",
    "candidate_freeze",
    "test_access",
    "independent_review",
    "recommendation",
    "closeout",
)
REQUIRED_ARTIFACTS = {
    "intake": ("INTAKE.md", "synthetic_governance_only"),
    "goal": ("GOAL.md", "Question-To-GOAL Trace"),
    "iteration_ledger": ("ITERATION_LEDGER.md", "Iteration counted?"),
    "test_access_entry": ("TEST_ACCESS_ENTRY.md", "first_blind"),
    "independent_review": ("INDEPENDENT_REVIEW.md", "independent_analysis"),
    "closeout": ("CLOSEOUT.md", "still_open"),
}


def load_fixture(path: Path = DEFAULT_FIXTURE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _stage_map(data: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    stages = data.get("stages")
    if not isinstance(stages, list):
        errors.append("stages must be a list")
        return {}
    names = [stage.get("stage") for stage in stages if isinstance(stage, dict)]
    if tuple(names) != STAGE_ORDER:
        errors.append(f"stage order must be {STAGE_ORDER!r}")
    if len(names) != len(stages):
        errors.append("every stage must be an object")
    return {
        stage["stage"]: stage
        for stage in stages
        if isinstance(stage, dict) and isinstance(stage.get("stage"), str)
    }


def validate_fixture(
    data: dict[str, Any], fixture_dir: Path | None = None
) -> list[str]:
    errors: list[str] = []
    if data.get("fixture_scope") != "synthetic_governance_only":
        errors.append("fixture must remain synthetic_governance_only")
    if data.get("private_strategy_facts") is not False:
        errors.append("fixture must not contain private strategy facts")
    if data.get("native_goal_created") is not False:
        errors.append("fixture must not create a native goal")

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
    else:
        for key, (expected_name, token) in REQUIRED_ARTIFACTS.items():
            relative = artifacts.get(key)
            if relative != expected_name:
                errors.append(f"artifact {key} must be {expected_name}")
                continue
            if fixture_dir is not None:
                path = fixture_dir / relative
                if not path.is_file():
                    errors.append(f"missing artifact: {relative}")
                elif token not in path.read_text(encoding="utf-8"):
                    errors.append(f"artifact {relative} missing token: {token}")

    stages = _stage_map(data, errors)
    if set(stages) != set(STAGE_ORDER):
        return errors
    for name, stage in stages.items():
        if stage.get("status") != "complete":
            errors.append(f"stage {name} must be complete")

    intake = stages["intake"]
    if intake.get("route") != "heavy_experiment":
        errors.append("promotion-affecting fixture must route to heavy_experiment")
    if (
        intake.get("promotion_affecting") is not True
        or intake.get("scope_frozen") is not True
    ):
        errors.append("intake must freeze a promotion-affecting scope")

    goal = stages["goal_contract"]
    if goal.get("question_to_goal_trace") != "complete":
        errors.append("question-to-goal trace must be complete")
    if goal.get("authorization_state") != "fixture_simulated_confirmed":
        errors.append("fixture authorization must be explicitly simulated")
    if goal.get("native_goal_action") != "not_created_fixture_only":
        errors.append("fixture must not open a native goal")
    if (
        goal.get("goal_path") != "GOAL.md"
        or goal.get("iteration_ledger_path") != "ITERATION_LEDGER.md"
    ):
        errors.append("goal contract must link GOAL.md and ITERATION_LEDGER.md")

    freeze = stages["candidate_freeze"]
    if (
        freeze.get("candidate_frozen") is not True
        or freeze.get("frozen_before_test") is not True
    ):
        errors.append("candidate must be frozen before Test")
    for field in (
        "matched_placebo_predeclared",
        "search_breadth_disclosed",
        "selection_deflation_recorded",
    ):
        if freeze.get(field) is not True:
            errors.append(f"candidate freeze missing promotion control: {field}")

    test = stages["test_access"]
    if test.get("candidate_id") != freeze.get("candidate_id"):
        errors.append("Test access candidate must match frozen candidate")
    access_seq = test.get("access_seq")
    if not isinstance(access_seq, int) or isinstance(access_seq, bool) or access_seq < 1:
        errors.append("Test access_seq must be a positive integer")
    if test.get("access_mode") not in {
        "first_blind",
        "repeat_display_only",
        "independent_reproduction",
        "legacy_baseline",
    }:
        errors.append("Test access_mode is invalid")
    if test.get("canonical_ledger_path") != data.get("canonical_test_ledger"):
        errors.append("Test access must route to the canonical ledger")
    if test.get("ledger_recorded") is not True:
        errors.append("every Test computation must be ledger-recorded")
    if test.get("used_for_selection") is not False:
        errors.append("Test must not be used for selection")

    review = stages["independent_review"]
    if review.get("candidate_id") != freeze.get("candidate_id"):
        errors.append("review candidate must match frozen candidate")
    independent = (
        review.get("reviewer_relation") == "independent"
        and review.get("scope_changed") is False
        and review.get("confirmation_level")
        in {"independent_analysis", "independent_reproduction"}
    )
    if not independent:
        errors.append("promotion review must be independent with no scope changes")
    if review.get("adoption_ready") is True and not independent:
        errors.append("self review cannot mark adoption_ready")
    if review.get("verdict") != "confirmed":
        errors.append("golden-path independent review must be confirmed")

    recommendation = stages["recommendation"]
    if recommendation.get("candidate_id") != freeze.get("candidate_id"):
        errors.append("recommendation candidate must match frozen candidate")
    if recommendation.get("bucket") != "recommended_upgrade":
        errors.append("golden-path recommendation must be recommended_upgrade")
    else:
        if review.get("adoption_ready") is not True or not independent:
            errors.append("recommended_upgrade requires adoption-ready independent review")
        if recommendation.get("user_decision_required") is not True:
            errors.append("recommended_upgrade must require an explicit user decision")
        if recommendation.get("adopted") is not False:
            errors.append("fixture recommendation must remain non-adopted")

    closeout = stages["closeout"]
    if closeout.get("completion_audit") != "satisfied":
        errors.append("closeout completion audit must be satisfied")
    if closeout.get("still_open") != []:
        errors.append("closeout cannot complete with still_open items")
    checks = closeout.get("checks")
    if (
        not isinstance(checks, dict)
        or not checks
        or any(value is not True for value in checks.values())
    ):
        errors.append("all closeout checks must pass")
    if closeout.get("exact_paths_only") is not True:
        errors.append("closeout must use exact-path staging")
    if closeout.get("push_decision") != "separate_scope_check":
        errors.append("closeout must keep push as a separate scope decision")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    args = parser.parse_args(argv)
    try:
        data = load_fixture(args.fixture)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"golden-path fixture load failed: {exc}", file=sys.stderr)
        return 2
    errors = validate_fixture(data, args.fixture.parent)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"golden-path fixture passed: {data['fixture_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
