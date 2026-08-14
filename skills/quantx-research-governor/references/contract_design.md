# QuantX Contract Design Reference

## Contents

- Canonical ownership and contract weight
- Instrument feasibility
- Pre-freeze semantic review
- Frozen identity and shared clauses
- Contract-runner conformance
- Immutable publication
- Review relations and handoff

Canonical ownership in the private QuantX workspace:

```text
00_RESEARCH_HUB/CONTRACT_BOILERPLATE.md
```

That file owns the current shared clauses. This reference is a portable
operational checklist. If wording conflicts, use the canonical boilerplate in
the private workspace and preserve the exact version bound by each already
frozen contract.

## Weight The Contract By Consequence

Use the lightest contract that can safely govern the outcome:

| Tier | Typical scope | Maximum consequence |
|---|---|---|
| `light` | outcome-free feasibility or Train-only diagnostic | may authorize only another contract or diagnostic |
| `full` | Validation, Test, blind/post-sample data, promotion-affecting work, or a favourable revision of a failed object | may support a frozen review candidate, never automatic adoption |

Classify by what the result could authorize, not by runtime. A three-minute
Test opening needs more governance than a three-hour outcome-free data audit.

## Instrument Feasibility Comes First

Before drafting a long contract, verify that the available instrument can
answer the question:

```text
timestamp resolution is finer than the effect being measured
cross-sectional resolution can distinguish the proposed comparison
sample supply can support the planned uncertainty or power statement
execution observations match the action surface being claimed
```

If the data cannot resolve the effect, stop at `instrument_infeasible`. A
perfectly frozen contract cannot repair an incapable instrument.

## Pre-Freeze Semantic Review

Hashes and mechanical gates detect execution drift. They do not detect a
wrong specification. Before freeze, answer all eight questions:

1. For every gate, what exact observation makes it fail? Is that failure
   physically reachable under the data range and mechanism?
2. Does the primary statistic contain a component fixed by construction rather
   than learned from observations? If so, isolate or cap it.
3. Are terminal labels mutually exclusive and reachable? If one terminal
   implies another, define an explicit priority or repair the conditions.
4. Does every cross-subset comparison have a size- and opportunity-matched
   control? Subset size alone is not a control.
5. For dependent resampling, is effective independent sample size estimated
   from the relevant statistic rather than equated with raw repetitions?
6. Was the null chosen after measuring the dependence structure of the exact
   statistic being tested, rather than from a generic market assumption?
7. Does the gate measure the decision question? Distinguish predictive
   discrimination from the value of choosing one feasible action over another.
8. Can the record schema state the true relationship, failure, and uncertainty
   without forcing a false attestation?

Label gates by function:

```text
evidence_structure
role_fit
personal_execution
```

Only `evidence_structure` gates support a claim about source structure. A role
or execution failure may reject the object for that use, but it must not be
rewritten as evidence that the source contains no structure.

## Frozen Identity And Shared Clauses

A frozen contract should identify at least:

```text
experiment and candidate identity
question, allowed scope, and forbidden actions
input paths plus content hashes
sample splits and Test-access mode
metrics and their exact definitions
gates, gate classes, and failure conditions
terminal labels and their precedence
selection order and search breadth
cost, cadence, and execution assumptions
output paths and no-overwrite policy
review roles and adoption boundary
```

When contracts share boilerplate, bind the shared clauses to a retrievable
content identity. In Git, prefer a blob object id:

```bash
git rev-parse HEAD:path/to/CONTRACT_BOILERPLATE.md
git cat-file -p <blob-id>
```

A bare file checksum proves that bytes changed but cannot recover the frozen
version after the source moves. If the artifact must stand alone without Git
history, copy the frozen boilerplate bytes into the lightweight review pack.

## Contract-Runner Conformance

Before a formal run, produce `contract_runner_conformance.json` mapping each
frozen requirement to executable evidence:

```text
requirement_id
contract_clause
runner_location
fixture_or_assertion
status: pass / fail / not_applicable
evidence_path
```

The receipt must cover inputs, splits, metrics, gates, terminal precedence,
forbidden data, output paths, and publication semantics. Every required row
must pass before formal output is trusted.

Conformance is necessary but not sufficient. It proves that the runner matches
the frozen text; it does not prove that the frozen text asks the right question.
That is why semantic pre-freeze review is separate.

## Immutable Publication

Use a no-overwrite publication sequence for durable experiment outputs:

```text
write to a run-specific staging directory
-> verify the complete manifest and hashes
-> atomically rename to an immutable generation directory
-> atomically update a small current pointer last
```

Keep raw grids, event tables, full paths, vendor data, and debug traces outside
Git. Track only compact reports, scorecards, contracts, conformance receipts,
review history, and the code required to reproduce them.

## Review Relations And Handoff

Record the roles separately:

```text
builder_task_id
contract_drafter_task_id
searcher_task_id when applicable
reviewer_task_id
```

Use these relations:

| Relation | Meaning | Governance consequence |
|---|---|---|
| `independent` | reviewer differs from drafter and, when recorded, searcher | may support governance only if the substantive review passes |
| `drafter_self_review` | reviewer drafted the contract | valid record; `adoption_ready=false`, `governance_eligible=false` |
| `non_independent` | another disclosed entanglement, such as searcher-reviewer | valid record with reason; same fail-closed consequence |

For a numerical postformal review, recompute at least one headline figure from
source inputs rather than from the builder's summary. Vary the seed when
sampling is involved. A preformal design review has no headline result to
recompute; it instead runs the semantic checklist and tests gate/terminal
reachability.

The builder hands over pointers and hashes, not a persuasive narrative:

```text
immutable generation path
contract and shared-clause identities
terminal label and gate scorecard path
input and runner hashes
conformance receipt
known deviations and adverse findings
```

No recommendation or review verdict is adoption. Adoption remains an explicit
human decision followed by a separate update to canonical governance.
