# QuantX Research Governor

[中文说明](README.zh-CN.md)

A portable copy of the research-governance skill used in a private quantitative
research workspace, plus the reusable protocol, templates, and sanitized
examples that go with it.

This repository is **downstream**. The canonical owner of `SKILL.md` and its
references is the private `QuantX-Mac-Research` workspace; this is the version
that can be installed elsewhere or read without workspace access. Edit upstream
first, then sync here.

It contains no strategy logic, no signals, no positions, no datasets, and no
performance claims. It is not financial advice and not a trading system.

## What This Is For

Agentic research drifts. It widens scope mid-run, quietly reuses the test set,
reports the best window instead of the selected one, and loses the record of
what failed. The skill in this repo is a set of brakes for that:

```text
scope, budget, and stop rules fixed before execution
Train / Validation / Test with a one-shot Test opening
a selection order that cannot be reordered after the fact
cadence, cost, and rolling stress as defaults rather than extras
compute-scale gates before broad grids
iteration strength defined so "N iterations" means N research attempts,
  not N commands or N report sections
failure logging as a first-class output
recommendation and adoption kept strictly separate
```

The last one matters most: the agent may recommend a promotion, but a human
confirms before anything becomes the active line of work.

## Layout

```text
skills/quantx-research-governor/   the skill itself
  SKILL.md                         entry point: routing, lifecycle, safety
  references/                      loaded conditionally, not all at once
    goal_templates.md              goal intake, plan-to-GOAL bridge, ledgers
    research_protocol.md           selection order, test ledger, placebo, stress
    report_contract.md             report sections and output file contract
    runtime_and_resources.md       compute gate, heavy-run launch, resume
    subagent_policy.md             delegation limits, independent review
    governance_and_closeout.md     git closeout, mirror stewardship
    golden_path_fixture.md         end-to-end lifecycle skeleton
  assets/golden_path_fixture/      a complete worked lifecycle, placeholder data
  scripts/validate_golden_path.py  fixture validator

protocol/data-leakage-checklist.md        pre-trust audit, A-share aware
templates/strategy-research-report.md     strategy design spec
templates/research-index.md               portfolio-level research index
templates/source-replay-handoff.md        independent replay handoff
examples/sanitized-experiment-readout.md  worked readout, invented numbers
docs/case-study.md                        what the private workspace taught
```

## Install

See [INSTALL.md](INSTALL.md). Short version: copy
`skills/quantx-research-governor/` into your agent's skills directory, then
rewrite the canonical-source table in `SKILL.md` to point at your own
repository's truth files.

## Adapting It

`SKILL.md` routes to canonical files by name — `STATE.md`,
`CURRENT_SHELL_REGISTRY.md`, `TEST_ACCESS_LEDGER.md`, and so on. Those names
belong to one specific workspace. The routing discipline is the reusable part;
the filenames are not. Substitute your own before using the skill, or it will
send the agent looking for files you do not have.

The same applies to `references/report_contract.md`, which names an output file
pack that assumes a particular directory layout.

## Who This Is For

Independent quant researchers, AI-assisted research workflows, anyone running
many backtests who needs report discipline, and anyone who wants reproducible
source replay before trusting a result.

## What This Is Not

Not financial advice. Not a trading strategy. Not a signal service. Not a
backtest engine.

## History

`QuantX-GoalForge` was archived on 2026-08-05 and folded into this repository.
Its goal-governance docs, prompt templates, and two `goal-governor` skills were
superseded by `references/goal_templates.md`, which is a strict superset. The
one piece worth keeping — its case study — is now `docs/case-study.md`.
`protocol/protocol-v2.md` was likewise superseded by
`references/research_protocol.md` and removed. Both repositories' full histories
are preserved in local git bundles.

## License

MIT. See [LICENSE](LICENSE).
