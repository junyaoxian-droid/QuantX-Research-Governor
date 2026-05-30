# QuantX Research Governor

[中文说明](README.zh-CN.md)

QuantX Research Governor is a compact protocol and template library for
AI-assisted quantitative research.

It does **not** contain trading signals, private data, positions, or a public
strategy. It contains the research discipline around strategy work:

- hypothesis-first design,
- Train / Validation / Test selection,
- rolling walk-forward validation,
- cost and cadence stress,
- compute-scale gates before broad grids,
- standard metrics such as Sharpe, Calmar, max drawdown, and win rate,
- failure logs,
- report hygiene,
- source replay handoff,
- and clear separation between model evidence and manual judgment.

If [QuantX GoalForge](https://github.com/junyaoxian-droid/QuantX-GoalForge) is
the general Codex goal governance layer, this repository is the quant-specific
research protocol layer.

## Who This Is For

- independent quant researchers,
- AI-assisted research workflows,
- people running many backtests and needing report discipline,
- teams that want reproducible source replay before trusting a result,
- and anyone who wants to avoid OOS-only traps.

## What This Is Not

- Not financial advice.
- Not a trading strategy.
- Not a signal service.
- Not a broker integration.
- Not a performance claim.

## Core Protocol

| Layer | Requirement |
|---|---|
| Hypothesis | State the market hypothesis before testing |
| Data | Record source, coverage, and point-in-time caveats |
| Label | Align label horizon with execution timing |
| Selection | Train creates candidates, Validation selects |
| Test | Test is opened once after selection |
| Rolling | Use walk-forward windows when claiming time robustness |
| Metrics | Report annualized return, DD, Sharpe, Calmar, win rate, turnover |
| Stress | Include cost, cadence, and perturbation checks |
| Compute | Estimate replay scale; use finalist funnels before exhaustive stress |
| Failure | Log rejected rows and why they failed |
| Handoff | Provide a replay prompt for another environment |

## Layout

```text
.
├── README.md
├── README.zh-CN.md
├── protocol/
│   ├── protocol-v2.md
│   └── data-leakage-checklist.md
├── templates/
│   ├── strategy-research-report.md
│   ├── source-replay-handoff.md
│   └── research-index.md
└── examples/
    └── sanitized-experiment-readout.md
```

## Relationship to QuantX

This repository is inspired by a private QuantX research workflow, but it is
not the QuantX strategy repository. Strategy formulas, current candidates,
private trade journals, and real account information are intentionally excluded.

## Community

Contributions are welcome from quant researchers, Codex users, backtest
engineers, data-science practitioners, and anyone who cares about reproducible
AI-assisted research.

Useful contributions include better validation checklists, walk-forward
templates, leakage-audit examples, source-replay workflows, metric definitions,
and sanitized failure cases. The aim is not to chase prettier backtests, but to
make research protocols more reliable and easier to review.

## License

MIT.
