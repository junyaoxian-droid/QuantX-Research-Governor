# Sanitized Experiment Readout

This is a fictional example showing how to report a result without exposing a
private strategy.

## Executive Verdict

No source replay candidate was promoted.

## Why

The best Test row was attractive, but it was not selected by Validation. It is
therefore labeled `test_best_not_selected`.

## Summary

| Candidate | Train Ann. | Train DD | Val Ann. | Val DD | Test Ann. | Test DD | Sharpe | Calmar | Win Rate | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| candidate_a | 14% | -12% | 11% | -15% | 9% | -16% | 0.7 | 0.6 | 56% | shadow |
| candidate_b | 3% | -24% | 2% | -18% | 60% | -5% | 1.8 | 12.0 | 72% | test_best_not_selected |

## Rolling Walk-Forward

| Window | Selected Candidate | Test Ann. | Test DD | Pass / Fail | Reason |
|---|---|---:|---:|---|---|
| 1 | candidate_a | 10% | -14% | pass | modest but stable |
| 2 | candidate_a | -3% | -20% | fail | regime mismatch |

## Do Not Do

- Do not promote candidate_b.
- Do not retune on Test.
- Do not hide the failure.
- Do not merge manual context into training features.
