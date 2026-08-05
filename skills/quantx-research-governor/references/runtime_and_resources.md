# QuantX Runtime And Resource Discipline

## Contents

- Applicability
- Compute scale gate
- Heavy-run launch gate
- Memory plan
- Monitoring and intervention
- Long-run decision discipline
- Resume after compaction or interruption

## Applicability

Read this file before any QuantX command expected to run longer than about
15 minutes, exceed 10 GB estimated RSS, materialize broad candidate grids, or
use parallel heavy workers.

Do not apply heavy-run ceremony to cache checks, report QA, compile checks,
single small replays, or workspace governance.

## Compute Scale Gate

Estimate:

```text
total replay units = candidates * variants * cadences * costs * windows
```

Record for heavy work:

```text
candidate and variant counts
cadence / cost / rolling multipliers
runtime class: small / medium / heavy
memory pressure: low / medium / high
expected peak RSS and intervention threshold
funnel: one-stage / staged / exhaustive
chunking and resume plan
```

Prefer a staged funnel:

```text
factor or label gate
-> native-cadence finalist screen
-> practical account path
-> cadence, cost, rolling, concentration stress
-> reproduction / source replay
```

Do not run the full Cartesian product by default. Pick one native cadence and
one cost point as the primary selection funnel, then apply the remaining
cadences and cost stress to finalists only.

## Heavy-Run Launch Gate

Launch heavy commands through:

```bash
.venv/bin/python code/scripts/quantx_heavy_run_guard_v1.py \
  --name <experiment_stage> \
  --estimated-peak-gb <N> \
  --scale-summary "<configs * windows * costs * variants>" \
  --chunking-plan "<score_id / hypothesis / date-window / none + why>" \
  --materialization-plan "<fully loaded vs streamed/projected>" \
  --stop-authorization not-approved \
  -- .venv/bin/python code/scripts/<experiment>.py <args>
```

For estimated peak RSS of 30 GB or more, require `--allow-high-memory` plus a
`--nonchunkable-justification`. The guard is a launch and heartbeat record, not
a reliable memory oracle.

## Memory Plan

Record before launch:

```text
max workers
expected peak RSS
intervention threshold
process-stop authorization
chunking key
cache/materialization policy
partial-output and resume policy
```

Use these planning bands:

```text
low: under 10 GB
normal heavy: 10-25 GB
warning: 25-30 GB
unsafe unless explicitly approved: above 30 GB
```

Prefer:

```text
score_id / hypothesis batching
DuckDB or Parquet projection instead of full pandas materialization
date-window or candidate-family chunks
partial summaries per chunk
release large frames before the next chunk
merge lightweight summaries after completion
```

A smoke run must exercise the same memory shape as the formal run. If the smoke
already approaches the intervention threshold, refactor before launching more
work.

## Monitoring And Intervention

- Treat memory observability as best-effort. Do not claim exact RSS without an
  actual measurement.
- Accept user Activity Monitor reports as valid evidence.
- Use guard heartbeats and progress logs when RSS is unavailable.
- Pause new heavy launches when memory crosses the declared threshold.
- Distinguish a planned, bounded high-memory phase from monotonic growth without
  progress or checkpointing.
- Do not stop or kill the active process without current user approval or a
  clear pre-approved GOAL.md stop rule.
- If stopping is authorized, preserve partial outputs, the exact resume command,
  and the unchanged research objective.

Classify high-memory runs:

```text
acceptable:
  approved budget; visible progress; bounded phase; known checkpoint/resume;
  no competing heavy jobs.

unsafe:
  unplanned 30GB+; monotonic growth; all-at-once materialization that can be
  chunked; competing jobs; no checkpoint or resume path.
```

## Long-Run Decision Discipline

While a command runs, prepare:

```text
expected result
success / partial-success / failure interpretation
first output checks
data/label bug indicators
next hypothesis if the branch fails
```

After completion, read outputs before launching the next iteration. Attribute
whether failure came from Train, Validation, Test, cost, cadence, rolling,
concentration, execution, source quality, or data integrity.

## Resume After Compaction Or Interruption

Before resuming a large experiment, read completely:

```text
docs/reports/<experiment>/GOAL.md
docs/reports/<experiment>/ITERATION_LEDGER.md
```

The ledger must contain the native goal state, completed effective iterations,
last verdict, next allowed action, resource budget, guard command, completion
audit state, and any user stop/pause instruction. Rebuild stale ledger state
from artifacts before more compute.
