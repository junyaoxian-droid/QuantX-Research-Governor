# Synthetic GOAL Contract

Fixture-only contract; never use as native-goal authorization.

## Objective

Validate the governor lifecycle from intake through closeout without strategy
compute or private strategy facts.

## Question-To-GOAL Trace

| Intake choice | Contract encoding |
|---|---|
| Promotion-affecting synthetic path | `heavy_experiment` route |
| No real execution | synthetic artifacts and standard-library validator only |
| Test integrity | freeze before Test and record a synthetic ledger entry |
| Adoption integrity | independent review precedes recommendation; user decision remains required |

## Success And Stop Rules

- Success: every lifecycle state and negative-path test passes.
- Stop: any missing artifact, invalid transition, Test-selection leak,
  non-independent review, or open completion item.
- Native goal: `not_created_fixture_only`.

## Outputs

- `GOAL.md`
- `ITERATION_LEDGER.md`
- `CONTRACT_PREFLIGHT.md`
- `TEST_ACCESS_ENTRY.md`
- `INDEPENDENT_REVIEW.md`
- `CLOSEOUT.md`
- `lifecycle.json`
