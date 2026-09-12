# QuantX Report Contract

## Contents

- Stage-appropriate summary
- Conditional report sections
- Output files and conformance
- Table style

## User-Facing Summary

Prefer compact tables, written in the user's input language.

Use a result table appropriate to the authorized research stage. For example:

| Line | Candidate | Train | Validation | Test | Cadence | DD | Verdict |
|---|---|---:|---:|---:|---|---:|---|

Omit inapplicable columns or mark unopened splits `not_opened`. A report
template never authorizes opening Validation, Test, or blind/post-sample data.

Explain:

```text
why selected
why rejected
what is monitor-only
what needs independent reproduction / source replay
what should not be used for trading
```

## Markdown Report Sections

For `docs/reports/<experiment>_vN/REPORT.md`, select sections by stage:

| Stage | Required focus | Conditional evidence |
|---|---|---|
| Outcome-free feasibility / Train-only scout | question, permitted inputs, diagnostic result, limitations, next gate | held-out splits remain `not_opened` |
| Formal research | frozen scope, authorized split results, gate verdict, failure cases | cadence, cost, robustness as specified in the contract |
| Execution-relevant research | the above plus practical replay assumptions and evidence | current monitoring only when separately authorized and meaningful |
| Governance-only | changes, reasons, validation, remaining divergence | no strategy metrics or signal generation |

The following is a menu for a full report, not a mandatory outline:

```text
# <Experiment Name>

## 1. Executive Verdict
## 2. Hypothesis And Scope
## 3. Data / Label / Execution Assumptions
## 4. Authorized Split Results
## 5. Cadence Stress
## 6. Cost And Execution Stress
## 7. Practical Account Replay
## 8. Failure Cases
## 9. Monitoring Evidence (only if in scope)
## 10. Decision And Next Step
## 11. Do-Not-Do
```

Do not generate a latest signal merely to fill a section. Read the registry
first; no adopted current core means no current strategy signal. Historical
replay and candidate monitoring must retain their explicit non-adopted labels.

For governance-only reports, use:

```text
what changed
why changed
remaining divergence
commit / push recommendation
```

## Standard Output Files

Use only what fits the experiment:

```text
REPORT.md
commands_used.md
experiment_contract.json or GOAL.md when contract-backed
CONTRACT_PREFLIGHT.md or preformal_checklist.json when formal
REPRODUCTION_HANDOFF_PROMPT.md
summary_metrics.csv
train_validation_test_summary.csv
cadence_stress_summary.csv
cost_stress_summary.csv
practical_account_replay_summary.csv
failed_candidates.csv
latest_signal_monitor.csv
contract_runner_conformance.json
independent_review.md
review_history.jsonl
```

The conformance receipt is required for a new or modified experiment contract.
It maps frozen requirements to runner evidence and fixtures, but is not a
substitute for independent semantic review. The review history is required
when `independent_review.md` is added or changed and must preserve earlier
adverse findings.

Practical account replay should follow
`00_RESEARCH_HUB/EXECUTION_REPLAY_CONTRACT.md` unless the report states why it
is not applicable. Any user override must be recorded in the report.

Full artifacts stay under ignored `outputs/<experiment>_vN/`.

Commit only lightweight scripts, docs, figures, and small CSVs.

Historical reports may still contain `WINDOWS_HANDOFF_PROMPT.md` when they were
written for a Windows/MateBook replay. New reports should use reproduction
handoff wording unless the user explicitly asks for a Windows/MateBook check.

## Table Style

Keep first columns short to avoid ugly wrapping in VS Code preview.

Prefer:

```text
Line | Candidate | Train Ann | Val Ann | Test Ann | DD | Verdict
```

Avoid overly long first-column labels. Put long explanations below the table.
