# QuantX Governance And Closeout

## Contents

- Governance patch discipline
- Workspace closeout
- Exact staging and commits
- Lifecycle hooks are defense-in-depth
- Push decision
- Public repository stewardship

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

Run:

```bash
.venv/bin/python code/scripts/quantx_workspace_closeout_v1.py
```

Classify every dirty path:

| Class | Action |
|---|---|
| `owned_current_task` | Validate and consider exact staging |
| `regenerable_current_task_noise` | Clean only when ownership is certain |
| `pre_existing_or_other_thread` | Preserve and exclude |
| `ambiguous_ownership` | Stop and request an owner decision |

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

Minimum validation:

```bash
git diff --check
.venv/bin/python code/scripts/quantx_entrypoint_drift_gate_v1.py
.venv/bin/python code/scripts/quantx_report_pack_gate_v1.py --base <base>
```

Run relevant tests and manifest compilation when shared behavior, entrypoints,
or governance rules change.

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

## Public Repository Stewardship

Treat these as separate repositories:

```text
QuantX-Mac-Research: private strategy workspace, canonical owner of this skill
QuantX-Research-Governor: private portable mirror of this skill plus reusable
  protocol, templates, and sanitized examples
QuantX-GoalForge: archived 2026-08-05; superseded by the mirror above
```

The mirror is downstream, never upstream. Edit the skill here first, then sync.
No repository is public as of 2026-08-05, but keep the sanitization rules below
in force anyway so the mirror stays publishable without a rewrite.

Before editing an external repository:

1. Read its README, local-only AGENTS.md, and relevant skill/protocol.
2. Check its Git status independently.
3. Convert private lessons into generic process language.
4. Validate and commit each repository separately.
5. Keep external-repo AGENTS.md local-only when its repository contract says so.

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
