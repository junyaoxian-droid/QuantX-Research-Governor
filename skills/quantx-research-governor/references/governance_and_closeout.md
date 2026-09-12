# QuantX Governance And Closeout

## Contents

- Governance patch discipline
- Workspace closeout
- Exact staging and commits
- Lifecycle hooks are defense-in-depth
- Push decision
- Installation and external repository stewardship

## Governance Patch Discipline

Before editing:

```bash
git status --short --branch
```

Then:

1. Identify the canonical owner.
2. Separate current-task paths from user or other-thread changes.
3. Prefer pointers and compact summaries over copied facts.
4. Keep root and Hub entry pages navigational.
5. Do not run strategy compute.
6. Do not touch `data_cache/`, `data_v3*/`, `outputs/`, `positions/`,
   `local_trade_journal/`, live config, secrets, or raw vendor data.
7. Report ignored local noise separately from durable changes.

Do not use a governance patch to change current strategy identity, adopt a
candidate, reopen a closed line, or reinterpret an experiment conclusion.

## Workspace Closeout

Repository `AGENTS.md` owns closeout scope and Git authority. For a read-only
audit, report findings and the checks actually performed; do not create a
report, run compilation, or stage files solely to satisfy a write-task checklist.
For edits or generated artifacts, run the relevant validation and:

```bash
.venv/bin/python code/scripts/quantx_workspace_closeout_v1.py
```

Classify every dirty path:

| Class | Action |
|---|---|
| `owned_current_task` | Validate and consider exact staging |
| `regenerable_current_task_noise` | Clean only when ownership is certain |
| `pre_existing_or_other_thread` | Preserve and exclude |
| `ambiguous_ownership` | Preserve and exclude; request an owner decision only if required to finish the scoped work |

Retain durable lightweight evidence:

```text
REPORT.md
commands_used.md
GOAL.md / ITERATION_LEDGER.md when required
small scorecards and readouts
reproduction handoffs
scripts needed to recreate the result
```

Keep heavy artifacts local under ignored `outputs/`. Do not clean, stage, move,
or summarize protected data contents during closeout.

## Exact Staging And Commits

Before `git add`, state:

```text
intended exact paths
semantic reason they belong together
excluded dirty paths
validation completed
commit and push decision
```

Rules:

- Never use `git add .`.
- Stage exact owned lightweight paths only.
- Keep governance docs, one experiment pack, report indexes, cache monitors,
  and public-repo changes in separate semantic commits.
- Do not commit failed validation, ambiguous ownership, secrets, raw data, or
  protected local-heavy paths.
- Make a local commit by default only when scope is coherent, ownership is
  clear, and relevant validation passes.
- Ask before committing when a file contains mixed user/current-task edits or
  when the report-index meaning is ambiguous.

Choose validation by the changed surface:

- Documentation: check local references and `git diff --check`; use the
  entrypoint/report gates when those surfaces are affected.
- Skill changes: validate skill structure and its synthetic lifecycle; assess
  representative behavior for substantial rule changes.
- Governance rules or entrypoints: compile the current script manifest and run
  relevant existing gates/tests. Shared behavior changes require the tests for
  that behavior. Do not run a strategy search as a hygiene check.

Relevant repository commands:

```bash
git diff --check
.venv/bin/python code/scripts/quantx_entrypoint_drift_gate_v1.py
.venv/bin/python code/scripts/quantx_report_pack_gate_v1.py --base <base>
```

In a mixed worktree, distinguish pre-existing failures from the proposed exact
change. Validate the intended index or committed range without staging unrelated
work; report any remaining workspace-level failure.

## Lifecycle Hooks Are Defense-In-Depth

Read current mechanics from `.codex/hooks.json`, `code/scripts/SCRIPT_LIFECYCLE.md`,
and `code/scripts/quantx_git_guard_v1.py`.

- `SessionStart` and `Stop` are fail-open advisories. They record or compare
  workspace baselines and never mutate the worktree.
- `pre-commit` and `pre-push` are fail-closed mechanical gates over the proposed
  index and outgoing committed range.
- Hooks do not replace owner classification, relevant tests, workspace closeout,
  exact-path staging, semantic commit scope, or the separate push decision.
- Never claim that a Stop hook automatically stages or commits work.

## Push Decision

Push lightweight verified work only when repository scope is clean and the
branch does not contain unrelated ahead commits requiring a separate decision.

Do not push automatically when:

```text
ahead commits span unrelated research/data/governance lines
worktree ownership is mixed
privacy or destination is unclear
validation failed
the user requested local-only work
```

Never rewrite history, reset, rebase, clean, or perform destructive Git cleanup
without explicit authorization.

## Installation And External Repository Stewardship

The private workspace owns this skill. The installed local copy and the
separate `QuantX-Research-Governor` repository are downstream copies; neither
silently overrides the canonical source. External repository visibility and
archive status are moving facts: inspect the explicitly scoped target when
syncing rather than copying dated status into stable rules.

First resolve the installed skill path. If it is a symlink to the canonical
directory, verify that target and its hashes; changes are already active, so
preserve the link and do not copy files onto themselves.
For a separate installed copy, compare it against the known pre-edit version
before copying exact changed skill files after an authorized update. Preserve
unexpected local differences; do not replace the whole skills directory or
copy bytecode/cache files. Verify the resulting source/installation hashes.

Before editing an external repository:

1. Read its README, local-only AGENTS.md, and relevant skill/protocol.
2. Check its Git status independently.
3. Convert private lessons into generic process language; preserve target-only
   documentation and established sanitization of structural paths.
4. Validate and commit each repository separately.
5. Keep external-repo AGENTS.md local-only when its repository contract says so.

An explicit skill-mirror push does not authorize pushing unrelated commits
from the private strategy repository. Check each outgoing range separately.

Never copy into external repositories:

```text
current private strategy identities or candidates
daily signals
real positions or account records
raw datasets or vendor data
full outputs
private report tables
tokens, cookies, keys, or credentials
```

Use this safe direction:

```text
private workflow lesson
-> private workspace process rule
-> sanitized generic public update when reusable
-> optional backport if the public framework improves the private workflow
```
