# Portable Quant Research Workspace Governance

This document describes a repository architecture for agent-assisted
quantitative research. It governs evidence and artifacts; it does not define a
trading strategy or authorize execution.

## 1. Keep One Owner Per Moving Fact

Do not make every README a partial database. Assign one canonical owner for
each moving fact and let entry pages link to it.

| Fact | Suggested owner |
|---|---|
| current adopted research object and vacancy state | current registry |
| active, candidate, reference, monitor, and archived roles | active-lines map |
| research status and adoption decisions | governance map |
| data freshness, coverage, and provenance | dataset registry |
| held-out Test access | append-only Test ledger |
| current report navigation | current-reports index |
| historical and negative evidence | research index |
| artifact placement and retention | repository map and artifact policy |

An entry page is a router, not an alternate truth source. Historical report
wording never overrides the current registry.

## 2. Route The Task Before Creating Artifacts

Use explicit lanes so an exploratory result cannot acquire authority by folder
placement alone:

```text
daily or monitor review
current-object optimization
new baseline or replacement candidate
sidecar or paper shadow
reference or comparator
archive or closed
governance, data, cache, or CI
```

The route determines the first files to read, allowed outputs, evidence burden,
and whether a durable experiment contract is required.

## 3. Separate Code, Heavy Outputs, And Review Evidence

Use a three-layer experiment layout:

```text
code/experiments/<experiment_id>/    code that recreates the experiment
outputs/<experiment_id>/             full local artifacts, ignored by Git
docs/reports/<experiment_id>/        compact review pack, tracked
```

A compact review pack normally contains:

```text
REPORT.md
commands_used.md
experiment contract or GOAL.md when required
small scorecards and summary tables
contract_runner_conformance.json for formal contracts
independent_review.md and append-only review history when reviewed
reproduction handoff when another environment must replay it
```

Raw grids, vendor data, event-level paths, full daily portfolios, debug traces,
and machine-specific caches stay outside Git.

## 4. Classify Dirty Paths By Ownership

At task start, record `git status --short --branch`. At closeout, classify every
dirty path:

| Class | Action |
|---|---|
| current-task durable change | validate and stage by exact path |
| current-task regenerable noise | remove only when ownership is certain |
| pre-existing or another task's work | preserve and exclude |
| ambiguous ownership | stop and request an owner decision |

Never use broad staging to make a mixed workspace appear clean. Hooks cannot
infer human ownership.

## 5. Use Gates As Defense In Depth

Different layers catch different failures:

| Layer | Catches | Does not catch |
|---|---|---|
| semantic pre-freeze review | wrong question, unreachable gate, incapable instrument | runner drift after freeze |
| contract-runner conformance | frozen clause missing from code or fixtures | bad frozen specification |
| experiment tests | implementation and data-alignment errors | undisclosed search or adoption drift |
| pre-commit / pre-push gate | forbidden paths, oversized packs, malformed records | ownership and economic meaning |
| independent review | counterevidence, reproduction mismatch, claim overreach | explicit human adoption |

No single gate replaces the others. A clean checksum is not evidence that the
contract asked the right question.

## 6. Preserve Review Relationships Truthfully

Record builder, contract drafter, searcher, and reviewer identities separately.
An independent review requires the reviewer to differ from the drafter and,
when a searcher is recorded, from the searcher. Self-review is a legitimate
record but must fail closed for adoption and governance eligibility.

For numerical claims, the reviewer should recompute at least one headline from
source inputs, varying the seed when sampling is involved. For preformal design
review, test instrument feasibility, gate reachability, and terminal semantics
instead.

## 7. Make Publication Immutable

Formal outputs should use a no-overwrite sequence:

```text
run-specific staging directory
-> complete manifest and hash verification
-> immutable generation directory
-> small current pointer updated last
```

This makes partial publication and silent reruns visible. Retain the contract,
runner identity, input identities, conformance receipt, and known adverse
findings with the generation or its compact review pack.

## 8. Keep Recommendation Separate From Adoption

Use an explicit transition:

```text
experiment evidence
-> recommendation
-> independent review when promotion-affecting
-> explicit human decision
-> canonical governance update
```

A strong Test result, a confirmed review, or a `recommended_upgrade` label is
not adoption. The active registry changes only after the human decision.

## 9. Close Out Exactly

Before commit:

1. Run the smallest relevant tests and `git diff --check`.
2. Run workspace-specific artifact and privacy gates.
3. Reclassify all dirty paths by ownership.
4. State intended paths, semantic reason, excluded paths, and validation.
5. Stage exact lightweight paths only.
6. Keep governance, one experiment pack, data monitors, and public-mirror work
   in separate commits.
7. Treat push as a separate scope and privacy decision.

The desired outcome is not a clean-looking tree. It is an auditable boundary
between owned evidence, protected local data, and unrelated work in progress.
