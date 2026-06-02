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
- adaptive staged funnels before expensive full stress,
- explicit iteration-strength definitions so "N iterations" means N independent
  research attempts, not N commands or report sections,
- tiered research checklists so quick reviews stay light while heavy experiments
  cannot start without a `GOAL.md`, compute gate, and adoption gate,
- efficiency modes so lightweight checks stay lightweight,
- standard metrics such as Sharpe, Calmar, max drawdown, and win rate,
- failure logs,
- report hygiene,
- adoption gates that separate agent recommendations from human-confirmed
  strategy governance,
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

## Heavy Goal Contract

For heavy quant research goals, do not rely on a short native goal summary.
Before execution, create a local `GOAL.md` contract that captures:

- the user's answers and assumptions,
- the exact iteration strength or failure budget,
- Train / Validation / Test and rolling requirements,
- compute funnel and full-run conditions,
- success, partial-success, and stop rules,
- output/report paths,
- and forbidden actions.

If the user asks for "5 iterations", count five independent research
hypotheses or repair mechanisms, not five commands, charts, reruns, or report
cleanup steps.

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
| Compute | Estimate replay scale; use adaptive finalist funnels before exhaustive stress |
| Checklist | Use light / standard / heavy checklists according to task risk |
| Iteration | Count only independent hypotheses/repair mechanisms as iterations |
| Efficiency | Keep quick signal/review tasks lightweight; reserve full protocol for promotion-impacting work |
| Run discipline | Use long-running job time to prepare expectations, failure branches, and next iterations |
| Parallelism | Use subagents/parallel jobs only for bounded independent audit/replay/QA with resource headroom |
| Failure | Log rejected rows and why they failed |
| Adoption | Recommendations do not become active lines until the user confirms them |
| Handoff | Provide a replay prompt for another environment |

## Adoption Gate

A research report may recommend an upgrade, but it must not silently rewrite the
current strategy hierarchy.

Use a clear post-experiment adoption table:

| Bucket | Meaning |
|---|---|
| `recommended_upgrade` | Strong enough to recommend, pending human confirmation |
| `source_replay_candidate` | Worth replaying in the source environment |
| `paper_shadow_candidate` | Track, but do not use as the main line |
| `manual_review_candidate` | Human review aid only |
| `diagnostic_only` | Useful clue, not an executable rule |
| `stop_as_rule` | Do not continue as a rule |

Only after the user or research owner confirms which lines are adopted should
the research map, README, or other project source-of-truth files be updated.
Skills describe process behavior, not current strategy facts; update a skill
only when the user explicitly asks to change the research workflow itself.
This prevents many good-looking experiments from accumulating as competing
"main" strategies.

## Efficiency Modes

Research governance should scale with task risk.

| Mode | Use When | Process |
|---|---|---|
| `quick_monitor` | latest signal, current-holding review, one table | read the current hub and relevant latest report only |
| `standard_check` | one hypothesis or bounded replay | fixed scope, minimal report, minimal verification |
| `governance_patch` | memory/hub/index cleanup | edit intended governance files only |
| `heavy_experiment` | broad search, rolling validation, promotion evidence | full protocol, staged compute funnel, adoption gate |

Do not launch full TVT/rolling/cost/cadence machinery for a simple monitor
question. Do not skip it when a result may change active research governance.

## Checklist Levels

Use the smallest checklist that protects the research.

| Level | Use When | Required Checks |
|---|---|---|
| `light` | latest signal, holding review, monitor note | no training; no broad grid; separate model signal from manual judgment |
| `standard` | one factor, one replay, one bounded hypothesis | inputs, date range, TVT applicability, outputs, no forbidden files staged |
| `heavy` | rolling validation, broad search, source-replay candidate | `GOAL.md`, question-to-goal trace, compute funnel, failure budget, adoption gate |

Heavy quant experiments should not start until:

- Train / Validation / Test roles are explicit;
- Validation selects and Test evaluates once;
- rolling is specified as fixed rolling stress or true dynamic retraining;
- standard metrics include annualized return, DD, Sharpe, Calmar, win rate, and turnover where relevant;
- cost / cadence / rolling / concentration checks are declared;
- output reports, handoff, and failure logs are named;
- source replay and adoption language stay conservative.

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
