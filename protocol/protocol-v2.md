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

## 8. Pre-Run Workflow Check

Before a heavy experiment starts, confirm that the workflow is appropriate:

- hypothesis is defined,
- Train / Validation / Test roles are clear,
- Validation selects and Test only evaluates,
- the compute plan is sized,
- success and failure rules are explicit,
- and expected outputs are known.

If these are unclear, do not launch a full search.

## 9. Compute-Scale Gate

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

## 10. Long-Run Thinking

While a long experiment is running, the agent should prepare a pre-mortem:

- expected result,
- success / partial-success / failure interpretation,
- next iteration if the run fails,
- likely data or label bug triggers,
- output files to inspect first.

If the result differs from expectation, analyze why before launching another
run.

## 11. Iteration Strength

An iteration budget should count independent research attempts, not commands,
script phases, chart generation, or report cleanup.

Not an effective iteration:

- bug fixes,
- data / label / time-alignment corrections,
- rerunning the same script after a patch,
- adding a figure or narrow sensitivity row to the same idea,
- renaming or re-rating report outputs.

Effective iteration:

- a new hypothesis,
- a materially different factor, rule, overlay, model, or portfolio
  construction mechanism,
- a complete evaluation path through the agreed gates,
- and a verdict: pass, fail, downgrade, or deepen.

If the owner asks for `N` iterations or `N` failures, treat `N` as independent
research attempts. A staged funnel for one hypothesis usually counts as one
iteration, unless the later stage introduces a new hypothesis.

## 12. Subagents and Parallelism

Subagents are useful for fixed replay, label audit, report QA, and source-replay
handoff drafts. They should not choose final promotion or invent new strategy
lines.

Parallel execution is allowed only when tasks are independent, write to separate
outputs, and CPU/memory headroom is healthy. If memory pressure is high, prefer
staged sequential execution.

## 13. Failure Logging

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

## 14. Promotion Language

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

## 15. Adoption Gate

Promotion language is still only a recommendation. A report must separate:

```text
agent recommendation -> human adoption decision -> source-of-truth update
```

Use an adoption table after major experiments:

| Bucket | Meaning |
|---|---|
| `recommended_upgrade` | Recommend promotion, pending owner confirmation |
| `source_replay_candidate` | Replay in the source environment before adoption |
| `paper_shadow_candidate` | Track but do not use as the active line |
| `manual_review_candidate` | Human review aid only |
| `diagnostic_only` | Explanation, not a rule |
| `stop_as_rule` | Stop promoting as a rule |

Do not update the active strategy map, README, or governance documents until
the research owner confirms which recommendation is adopted. Skills should not
store current strategy facts; update a skill only when the owner explicitly
asks to change the research process itself. This keeps multiple experiments
from becoming competing source-of-truth lines.
