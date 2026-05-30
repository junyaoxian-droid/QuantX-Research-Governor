# Sanitized Experiment Readout

This is a fictional example showing how to report a result without exposing a
private strategy.

## Executive Verdict

No source replay candidate was promoted.

## Why

The best Test row was attractive, but it was not selected by Validation. It is
therefore labeled `test_best_not_selected`.

## Summary

| Candidate | Train Ann. | Train DD | Validation Ann. | Validation DD | Test Ann. | Test DD | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| candidate_a | 14% | -12% | 11% | -15% | 9% | -16% | shadow |
| candidate_b | 3% | -24% | 2% | -18% | 60% | -5% | test_best_not_selected |

## Do Not Do

- Do not promote candidate_b.
- Do not retune on Test.
- Do not hide the failure.
- Do not merge manual context into training features.
