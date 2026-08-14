# Source Replay Handoff

Use this template when handing a candidate to another machine or reviewer.

## Objective

Reproduce the selected candidate under the source-of-truth environment.

## Scope

- Research-only.
- No broker connection.
- No automatic trading.
- No private account modification.

## Read First

- `REPORT.md`
- frozen experiment contract and shared-clause identity
- `contract_runner_conformance.json`
- `summary_metrics.csv`
- `failed_candidates.csv` or the experiment's failure log
- immutable generation path and runner hash

## Candidate To Replay

| Field | Value |
|---|---|
| Candidate ID | |
| Selection stage | |
| Data range | |
| Cost assumptions | |
| Execution assumptions | |
| Contract identity | |
| Shared-clause identity | |
| Input identities | |
| Runner identity | |
| Original builder | |
| Contract drafter | |
| Searcher, if applicable | |
| Assigned reviewer | |

## Required Checks

1. Reproduce Train / Validation / Test.
2. Reproduce cost stress.
3. Reproduce cadence stress.
4. Confirm no Test selection.
5. Confirm no private data dependency.
6. Recompute at least one headline from source inputs; vary the seed when
   sampling is involved.
7. Preserve adverse findings and report mismatches.

## Output

- replay report,
- mismatch table,
- final replay verdict.
