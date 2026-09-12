# Optional Native Codex Goal Control

This reference owns native goal authorization, tool state, and integrity rules.
[goal_templates.md](goal_templates.md) owns experiment contracts and research
iteration. Follow the current runtime tool schema if it changes; never invent
capabilities from a template or historical workflow.

## Authorization And Creation

- Call `create_goal` only when the user or system/developer instructions explicitly
  request a native goal. Ordinary research requests, GOAL.md creation, an
  experiment contract, or “确认，执行实验” alone do not authorize native tracking.
- “可以规划一个 goal”, “先探索，有可能后再大规模实验”, and a prospective iteration
  budget are planning language. Do not infer native authorization from them.
- Explicit confirmation of a displayed proposal that clearly includes native
  goal creation is authorization. Preserve that approval rather than asking
  again; record the approved wording and scope. A Plan bridge label by itself
  is insufficient: check what the user actually approved.
- Native tracking is optional. When it was not requested, continue authorized
  research without it; do not require an opt-out or ask solely to enable it.
- Set `token_budget` only when the user explicitly requests a token budget.
  Do not convert time, iteration, failure, or qualitative effort budgets into
  tokens. Omit the field otherwise.

For a large experiment, materialize and verify GOAL.md and ITERATION_LEDGER.md
before native creation or compute. Include both actual paths in the new
objective, alongside the concrete requested outcome:

```text
Experiment contract: docs/reports/<experiment_id>/GOAL.md
Iteration ledger: docs/reports/<experiment_id>/ITERATION_LEDGER.md
```

`get_goal` is read-only and may inspect existing state. `create_goal` fails if
an unfinished native goal exists; do not close it artificially to make room.
If existing tracking lacks contract links, record the actual objective and
both paths in the ledger and verify scope before associating it with this
experiment. The current tools cannot edit an objective. Do not claim it has
been repaired or recreate it automatically. An unrelated or unclear active
objective must not be silently repurposed; resolve the scope conflict before
work that could be attributed to it.

## Status Contract

The current `update_goal` tool accepts only `complete` and `blocked`:

- `complete`: the concrete native objective has actually been achieved and no
  required work remains. Read the contract, ledger, and latest evidence first.
  For a budgeted goal, report final token usage from the tool result.
- Budget exhaustion, failure, infeasibility, a fatal data issue, a declared
  stopping rule, user termination, or early research closure do not establish
  completion by themselves. They may leave the native objective unmet.
  A fully delivered, bounded evaluation can legitimately conclude negatively;
  assess its original objective and required deliverables, not whether a
  candidate succeeded. Do not rewrite success criteria after the fact.
- `blocked`: the same blocking condition has recurred for at least three
  consecutive goal turns (including the original user-triggered turn and
  automatic continuations), and no meaningful progress remains possible
  without user input or an external-state change. Do not use it merely for
  difficult, slow, uncertain, incomplete, or budget-limited work.
- After a previously blocked goal resumes, restart the consecutive-turn audit.
  Once the threshold is met at a genuine impasse, mark blocked rather than
  indefinitely reporting the same blocker with the goal active.

The tool cannot pause, resume, terminate, or change budgets/usage limits.
Never use `complete` or `blocked` to simulate those operations. Research
iteration counts and consecutive native goal turns are different quantities.

## User Stop And Control Limits

Immediately stop launching new work when the user asks to stop or pause.
Handle already-running processes under the user's instruction and the
contract's process-stop authorization; preserve outputs and resume information.

Use a supported native control only if it is actually available and permitted
by its current schema. Otherwise explain the UI action needed and preserve the
actual tool state. Do not continue research simply because native state still
reads active, and do not claim a native pause or termination that did not occur.

## Ledger Audit Fields

Keep these optional fields alongside the research ledger, without treating
research stop reasons as native state values:

```text
Native tracking: not_requested / requested / existing
Creation authorization source and exact approved scope:
Token budget explicitly requested by user: yes/no; amount if any:
Native objective and contract/ledger linkage:
Actual native state (verbatim from tool/UI, or unknown):
Last observed state and observation time:
Requested control action and available control:
Action result / remaining user UI action:
Research stop or close reason (separate from native state):
Blocking condition and evidence of no meaningful next action:
Consecutive goal turns with this blocker:
Resume audit reset point:
Required work still open:
```
