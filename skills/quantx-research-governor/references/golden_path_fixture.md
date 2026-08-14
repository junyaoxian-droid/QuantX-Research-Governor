# QuantX Governor Golden-Path Fixture

Use this synthetic fixture to verify lifecycle wiring before adapting a large,
promotion-affecting QuantX experiment. It contains no strategy identity,
performance metric, data access, or real native-goal authorization.

## Files

```text
assets/golden_path_fixture/lifecycle.json
assets/golden_path_fixture/INTAKE.md
assets/golden_path_fixture/GOAL.md
assets/golden_path_fixture/ITERATION_LEDGER.md
assets/golden_path_fixture/CONTRACT_PREFLIGHT.md
assets/golden_path_fixture/TEST_ACCESS_ENTRY.md
assets/golden_path_fixture/INDEPENDENT_REVIEW.md
assets/golden_path_fixture/CLOSEOUT.md
scripts/validate_golden_path.py
```

The fixture encodes:

```text
intake
-> goal_contract
-> contract_preflight
-> candidate_freeze
-> test_access
-> independent_review
-> recommendation
-> closeout
```

`contract_preflight`, `candidate_freeze`, and `recommendation` are explicit
because semantic gate review, Test access, and adoption boundaries cannot be
validated without them.

## Validate

From the repository root:

```bash
.venv/bin/python 00_RESEARCH_HUB/skills/quantx-research-governor/scripts/validate_golden_path.py
```

The validator uses only the Python standard library. It checks artifact
presence, stage order, simulated authorization, freeze-before-Test, canonical
Test-ledger routing, independent-review separation, recommendation-versus-
adoption separation, and completion-audit closure.

## Adaptation Rules

1. Read `goal_templates.md`, `research_protocol.md`, `subagent_policy.md`, and
   the canonical workspace owners before adapting the fixture.
2. Copy the structure into the governed experiment report pack; do not edit the
   fixture with current strategy facts.
3. Run instrument feasibility, gate reachability, terminal exclusivity, and
   contract-runner conformance before formal output.
4. Replace every synthetic value with evidence from the actual experiment.
5. Obtain real user authorization before `create_goal`; the fixture's simulated
   state is never authorization.
6. Append the canonical `00_RESEARCH_HUB/TEST_ACCESS_LEDGER.md` only when real
   Test computation occurs. The fixture entry is illustrative and is not a
   canonical access event.
7. Use the real workspace closeout and exact-path staging rules after work.

This fixture proves governance consistency only. It does not prove a strategy,
authorize compute, satisfy independent reproduction, recommend adoption, or
permit trading.
