# Case Study: What QuantX Taught Me About Agentic Research Governance

This case study summarizes lessons from a private quantitative research
workspace. It intentionally removes strategy details, private data, positions,
signals, and performance claims.

The point is not "how to trade." The point is how long-running AI-assisted
research can go wrong, and what governance patterns helped.

## Context

QuantX is a private research project for China A-share strategy experiments.
It uses local data caches, reproducible scripts, research-only reports, and
human review. The project is not a public strategy service.

The workspace became a useful stress test for Codex because it had:

- many experiment families,
- frequent strategy hypotheses,
- rolling data updates,
- multiple machines reproducing results,
- thousands of local artifacts,
- and a real need to separate research evidence from manual execution.

## Problems Encountered

| Problem | What Happened | Risk |
|---|---|---|
| Goal drift | A prompt started as one experiment but slowly became a broader search | The agent could optimize the wrong objective |
| Prompt burden | Good Codex goal prompts became long and hard to write manually | The user had to draft prompts elsewhere, losing local project context |
| Plan-to-goal gap | Planning discussions did not automatically become executable goal specs | Decisions made during planning were easy to lose |
| Version sprawl | Many disconnected `v1` reports appeared across related ideas | Later review became hard and continuity was lost |
| OOS temptation | Attractive out-of-sample paths looked convincing before training evidence was solid | Overfitting and false confidence |
| Report explosion | Thousands of reports and CSVs accumulated | Important conclusions became hard to find |
| Mixed evidence | Model output, manual judgment, current holdings, and news context could blur together | Historical conclusions could become contaminated |
| Cadence fragility | Some strategies looked good on one review schedule and weak on another | Timing dependency was mistaken for robustness |
| Single-split fragility | Some candidates looked acceptable under one fixed split but failed when the window moved | The selection process was less stable than the headline result |
| Cost blindness | Some candidate paths depended on unrealistic friction assumptions | Backtest quality was overstated |
| Agent over-persistence | A broad search could continue after weak evidence instead of pausing for hypothesis review | Time was spent tuning noise |
| Agent under-persistence | A promising line could be abandoned after one failed run | Useful ideas were not developed deeply enough |
| Cross-machine mismatch | Mac and Windows research environments needed to reproduce each other | Local-only conclusions could become misleading |
| Specification passed mechanical gates | Hashes and assertions matched a frozen contract whose gate did not answer the intended question | Clean artifacts could still support a false claim |
| Review-role entanglement | Builder, contract drafter, searcher, and reviewer were treated as one coarse identity | A review could be labeled independent when it was not |
| Partial publication | A run could expose a current pointer before every artifact was complete | Reviewers could inspect a mixed or incomplete generation |

## Governance Patterns That Helped

| Pattern | Description | Effect |
|---|---|---|
| Read-first hub | A small set of current-state files replaced scattered memory | New sessions could orient quickly |
| Goal brief | Each major run had objective, scope, forbidden actions, gates, budget, and outputs | Reduced drift |
| Prompt intake | Codex helped convert partial intent into a goal brief using local context | Reduced dependence on external prompt drafting |
| Plan-to-goal bridge | Planning conclusions were rewritten as executable goal specs before running | Reduced lost decisions between modes |
| Experiment family versioning | Related work continued as v2/v3 instead of unrelated v1 folders | Improved continuity |
| Train / Validation / Test | Validation selected; Test evaluated only after selection | Reduced OOS chasing |
| Failure budget | Large searches had allowed attempts and stop rules | Balanced persistence and discipline |
| Failure log | Rejected candidates were recorded with reasons | Prevented repeated dead ends |
| Cadence stress | Monthly, semi-monthly, weekly, and anchor variants were shown side by side when relevant | Exposed schedule dependence |
| Rolling validation | Walk-forward windows checked whether the selection process survived different periods | Exposed candidates that depended on one favorable split |
| Cost stress | 20 / 50 / 100 bps friction checks were included when relevant | Exposed fragile paths |
| Monitor-only layer | News, manual tape-reading, and post-sample observations were separated from historical training | Reduced contamination |
| Lightweight GitHub sync | Only scripts, reports, and small summaries were pushed; full outputs and data stayed local | Enabled review without leaking large/private artifacts |
| Windows/source replay | A second environment replayed important findings | Reduced single-machine error |
| Instrument-first contract preflight | Resolution, sample supply, gate reachability, and terminal logic were checked before freeze | Prevented expensive contracts for questions the data could not answer |
| Contract-runner conformance | Every frozen clause was mapped to code, fixtures, and evidence | Exposed implementation drift without claiming semantic correctness |
| Explicit review relations | Searcher, drafter, builder, and reviewer identities were recorded separately | Made self-review truthful and promotion gates fail closed |
| Immutable generation publication | Staging, manifest verification, atomic rename, and last-pointer update replaced overwrite-in-place | Made partial and silent reruns visible |

## Before / After

| Before GoalForge Discipline | After GoalForge Discipline |
|---|---|
| "Try improving this strategy" | "Run v3 of this family, with 5 independent attempts, Train-first selection, and Test opened once" |
| Many unrelated reports | Indexed report families with explicit current read |
| Pretty OOS path looked exciting | Labeled as `oos_only_trap` if Train/Validation failed |
| Agent kept searching | Stop after success, repeated failures, or suspected data bug |
| Manual decisions mixed into strategy evidence | Manual overlay logged separately |
| Hard to know what mattered | Current research map and active-line documents summarized status |

## Practical Design Lessons

### 1. The Goal Must Be Smaller Than the Ambition

The long-term ambition can be broad, but each executable goal must be bounded.

Bad:

```text
Find a better strategy.
```

Better:

```text
Test whether a holding-buffer rule improves the existing daily-review family
under fixed Train / Validation / Test splits, with 20/50/100 bps stress and a
maximum of five independent attempts.
```

### 2. Reports Need a Current Read, Not Just History

Chronological logs are useful, but a working project also needs a current map:

- active lines,
- rejected lines,
- source replay candidates,
- shadow candidates,
- open risks,
- and "do not promote" warnings.

Without this, the agent can keep rediscovering old conclusions.

### 3. Negative Results Are Assets

A failed experiment is valuable if it prevents repeated work.

The failure log should say:

- what failed,
- why it failed,
- whether it invalidates the hypothesis or only one wrapper,
- and what should not be tried again without new evidence.

### 4. Agent Goals Need Both Persistence and Brakes

For hard research, stopping after one weak run is too shallow. But endless
search is dangerous.

GoalForge uses failure budgets:

```text
Try up to 5 independent directions.
Stop earlier on success.
Stop immediately on suspected data bug.
After 5 failures, summarize and return to hypothesis design.
```

### 5. Human Judgment Must Be Labeled

Human review is useful, especially in live or post-sample contexts. But it must
not be silently mixed into historical model evidence.

Use labels like:

- `model_signal`,
- `manual_overlay`,
- `monitor_only`,
- `post_sample`,
- `not_training_feature`.

### 6. Mechanical Correctness Is Not Semantic Correctness

A runner can match a frozen contract perfectly while the contract measures the
wrong thing. Before freeze, ask what observation makes each gate fail, whether
terminal labels are mutually exclusive, and whether the available data can
resolve the claimed effect. After freeze, use a separate conformance receipt to
prove that the runner implements those clauses. Neither review replaces the
other.

## What Did This Improve?

The biggest improvement was not a single metric. It was research quality:

- fewer duplicated experiments,
- faster session handoff,
- clearer rejection of overfit candidates,
- better separation between evidence and judgment,
- safer collaboration between machines,
- and more disciplined use of Codex for long-running work.

In short: the agent became less like a clever assistant chasing the next shiny
result, and more like a research operator working inside a protocol.

## What Still Requires Human Judgment?

Goal governance does not remove the need for judgment.

Humans still decide:

- which hypotheses are worth testing,
- whether a result is economically meaningful,
- whether a risk is acceptable,
- when to stop a line,
- and how much real-world trust to assign to a research candidate.

GoalForge is the guardrail, not the driver.
