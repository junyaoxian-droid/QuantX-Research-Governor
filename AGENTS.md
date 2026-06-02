# AGENTS.md

Guidance for Codex, GPT reviewers, and other agents working in this public repository.

## Role

`QuantX-Research-Governor` is a public quant-research protocol and template
library. It is not the private QuantX strategy repository, not a trading
strategy, and not a signal service.

Use this repo for reusable quant-research discipline:

```text
Train / Validation / Test protocol
rolling walk-forward rules
cost and cadence stress checklists
data-leakage audits
failure logs
source replay handoff templates
sanitized examples
```

## Read First

```text
README.md
README.zh-CN.md
protocol/protocol-v2.md
protocol/data-leakage-checklist.md
templates/strategy-research-report.md
templates/source-replay-handoff.md
templates/research-index.md
examples/sanitized-experiment-readout.md
```

## Editing Rules

- Keep all content public, generic, and protocol-focused.
- Do not include private QuantX signals, positions, current candidates, raw datasets, vendor data, full outputs, or real account context.
- Strategy examples must be sanitized and should illustrate process discipline rather than performance claims.
- If protocol behavior changes, update the matching README, checklist, and template references when relevant.
- Use conservative wording: this repo may describe research validation, not financial advice or executable trading recommendations.
- Prefer small, reviewable patches over broad rewrites.

## Verification

For documentation-only changes, run at least:

```bash
git diff --check
```

If scripts or generated examples are added later, add or run the repo-native
lint/test/smoke command and document it in the final response.

## GitHub Sync

This is a public open-source repository. After useful verified changes, commit
and push the lightweight artifacts to GitHub unless the user asks otherwise.
Stage only intended files and keep commits separate from other QuantX
repositories.
