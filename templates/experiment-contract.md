# Experiment Contract

Freeze this file before formal execution. Replace every placeholder and bind
the final bytes to a content identity.

## 1. Identity And Consequence

| Field | Value |
|---|---|
| Experiment ID | `<family>_vN` |
| Contract tier | `light` / `full` |
| Route | `standard_check` / `heavy_experiment` / other |
| Promotion-affecting | `yes` / `no` |
| Contract content identity | `<git blob id or immutable artifact hash>` |
| Shared clauses path | `<path or not_applicable>` |
| Shared clauses retrievable identity | `<git blob id or embedded copy>` |

Maximum consequence this contract may authorize:

```text
<diagnostic only / another contract / frozen review candidate>
```

It never authorizes adoption or live execution.

## 2. Question And Scope

- Frozen question:
- Baseline or comparator:
- Allowed changes:
- Forbidden changes:
- Date range and market/universe boundary:
- Output audience:

## 3. Instrument Feasibility

| Check | Evidence | Verdict |
|---|---|---|
| Time resolution can measure the effect | | pass / fail |
| Cross-sectional resolution supports the comparison | | pass / fail |
| Expected sample supply supports the uncertainty statement | | pass / fail |
| Available execution observations match the claimed action | | pass / fail / not_applicable |

Stop at `instrument_infeasible` if a required row fails.

## 4. Roles

| Role | Task or actor ID |
|---|---|
| Builder | |
| Contract drafter | |
| Searcher, when applicable | |
| Assigned reviewer | |

Allowed review relations: `independent`, `drafter_self_review`, or
`non_independent`. The last two force `adoption_ready=false` and
`governance_eligible=false`.

## 5. Inputs And Provenance

| Input | Point-in-time rule | Content identity | Required |
|---|---|---|---|
| | | | yes / no |

- Missing-data policy:
- Universe membership policy:
- Vendor/cache provenance:
- Forbidden inputs:

## 6. Splits And Test Access

| Split | Range or rule | Permitted use |
|---|---|---|
| Train | | generate and estimate |
| Validation | | select and freeze |
| Test | | one-shot evaluation after freeze |
| Post-sample monitor | | monitoring only |

- Canonical Test ledger:
- Expected access mode: `first_blind` / `repeat_display_only` /
  `independent_reproduction` / `not_applicable`
- Candidate freeze artifact:

## 7. Metrics And Selection

| Metric ID | Exact definition | Split used | Decision role |
|---|---|---|---|
| | | | primary / secondary / diagnostic |

- Candidate and variant search breadth:
- Selection order:
- Multiplicity or selection-deflation method:
- Matched placebo, null, or negative control:
- Why the control matches sample opportunity, cadence, costs, and search budget:

## 8. Gate Register

| Gate ID | Class | Statistic | Pass condition | Reachable failure example | Evidence path |
|---|---|---|---|---|---|
| | `evidence_structure` / `role_fit` / `personal_execution` | | | | |

Every required gate must have a physically reachable failure condition. Only
`evidence_structure` gates may support a source-structure terminal.

## 9. Terminal Register

| Terminal label | Exact Boolean condition | Priority | Maximum consequence |
|---|---|---:|---|
| | | | |

- Terminal labels mutually exclusive: `yes` / `no`
- If no, explicit precedence and proof that every lower-priority terminal is
  still reachable:

## 10. Resampling And Null Design

- Statistic whose dependence matters:
- Measured dependence evidence:
- Null or resampling method:
- Independent draws or dependent sequence:
- Effective independent sample-size method when dependent:
- Frozen seeds and repetition count:

## 11. Contract-Runner Conformance

Write `contract_runner_conformance.json` before formal execution.

| Requirement ID | Contract clause | Runner location | Fixture/assertion | Status | Evidence |
|---|---|---|---|---|---|
| | | | | pass / fail / not_applicable | |

Required coverage: inputs, splits, metrics, gates, terminal precedence,
forbidden data, output paths, and publication semantics.

## 12. Outputs And Publication

- Code path:
- Ignored full-output path:
- Tracked review-pack path:
- Staging path pattern:
- Immutable generation path pattern:
- Current pointer updated last:
- No-overwrite enforcement:
- Required manifest and hashes:

## 13. Stop Rules And Failure Handling

- Success terminal:
- Honest failure terminals:
- Failure budget:
- Suspected data/label bug action:
- User stop action:
- Rescue reruns forbidden after outcome:

A failed gate is an honest result, not a reason to change the frozen contract.

## 14. Review And Adoption Boundary

- Preformal semantic reviewer and verdict:
- Postformal reviewer:
- Numerical headline to recompute from source:
- Seed variation required:
- Known non-independence, if any:
- Adoption requires a separate explicit human decision: `yes`

## 15. Freeze Receipt

- All placeholders removed:
- Instrument feasibility passed:
- Gate failures reachable:
- Terminal logic reviewed:
- Shared clauses recoverable:
- Inputs and runner identities recorded:
- Contract-runner conformance passed:
- Test ledger ready:
- Reviewer assigned:
- Frozen timestamp:
- Frozen content identity:
