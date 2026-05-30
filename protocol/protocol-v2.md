# Quant Research Protocol v2

## 1. Hypothesis First

Do not start with a parameter grid. Start with a market hypothesis.

Bad:

```text
Search for a better strategy.
```

Better:

```text
Test whether lower-noise pullback candidates outperform over the next 20
trading days after transaction costs.
```

## 2. Data Contract

Record:

- data source,
- coverage range,
- update timestamp,
- point-in-time status,
- known survivorship or liquidity caveats,
- missingness,
- and whether the data may be used for backtest or monitor only.

## 3. Label Contract

A label must define:

- prediction horizon,
- benchmark or absolute return,
- entry timing,
- exit timing,
- open-case handling,
- and whether the sample is closed.

## 4. Selection Discipline

Use:

```text
Train -> Validation -> Test
```

Train creates candidates. Validation selects. Test evaluates once.

Do not select by Test.

## 5. Rolling Walk-Forward

When a strategy claims robustness over time, fixed Train / Validation / Test is
not enough. Add rolling walk-forward windows:

```text
Train A -> Validation A -> Test A
Train B -> Validation B -> Test B
Train C -> Validation C -> Test C
```

Report:

- window dates,
- selected candidate,
- Test performance,
- pass / fail,
- failure reason,
- and whether the selection process is stable across windows.

Do not tune future windows after seeing their Test results.

## 6. Standard Metrics

Report standard performance metrics before custom scores:

| Metric | Purpose |
|---|---|
| Annualized return | Normalizes return across different horizons |
| Max DD | Measures worst peak-to-trough loss |
| Sharpe | Return per unit of volatility |
| Sortino | Return per downside volatility |
| Calmar | Annualized return divided by absolute max DD |
| Win rate | Share of profitable trades or periods |
| Turnover | Trading intensity and cost sensitivity |
| Cost-adjusted return | Return after explicit transaction costs |
| Benchmark-relative return | Excess return versus the benchmark |

Custom metrics may be added, but they should not replace these fields.

## 7. Stress Tests

At minimum, consider:

- cost stress,
- cadence or anchor stress,
- market regime splits,
- industry exclusion,
- single-name contribution,
- rolling windows,
- and execution feasibility.

## 8. Compute-Scale Gate

Before launching a broad search, estimate the replay scale:

```text
replay units = candidates * cadences * costs * overlays * rolling windows
```

If the full Cartesian product is large, use a staged design. The stage count is
not fixed; use the smallest sequence that still answers the research question:

```text
Early stage: select candidates under the native execution cadence and baseline cost.
Later stages: add cadence, cost, industry, execution, and rolling stress only where needed.
```

This is not a shortcut around rigor. It prevents obviously failed candidates
from consuming expensive robustness checks. Full grids are allowed only when the
estimated runtime and memory are acceptable, or when exhaustive coverage is the
explicit research question.

## 9. Failure Logging

Every major rejected candidate should have a failure reason.

Examples:

- `train_fail`,
- `validation_fail`,
- `test_best_not_selected`,
- `oos_only_trap`,
- `cadence_fragile`,
- `cost_reversal`,
- `execution_infeasible`,
- `data_alignment_bug`.

## 10. Promotion Language

Use conservative labels:

- `source_replay_candidate`,
- `paper_shadow_candidate`,
- `manual_review_candidate`,
- `diagnostic_only`,
- `stop_as_rule`.

Avoid:

- "deploy",
- "live base",
- "proven",
- "guaranteed",
- "safe",
- unless the governance process explicitly supports that status.
