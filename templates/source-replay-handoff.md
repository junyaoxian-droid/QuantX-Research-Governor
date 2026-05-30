# Source Replay Handoff

Use this template when handing a candidate to another machine or reviewer.

## Objective

Reproduce the selected candidate under the source-of-truth environment.

## Scope

- Research-only.
- No broker connection.
- No automatic trading.
- No private account modification.

## Read First

- `REPORT.md`
- `summary.csv`
- `failure_log.csv`
- script path

## Candidate To Replay

| Field | Value |
|---|---|
| Candidate ID | |
| Selection stage | |
| Data range | |
| Cost assumptions | |
| Execution assumptions | |

## Required Checks

1. Reproduce Train / Validation / Test.
2. Reproduce cost stress.
3. Reproduce cadence stress.
4. Confirm no Test selection.
5. Confirm no private data dependency.
6. Report mismatches.

## Output

- replay report,
- mismatch table,
- final replay verdict.
