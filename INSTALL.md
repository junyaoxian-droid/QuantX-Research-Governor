# Installing The Research Governor Skill

The skill lives at `skills/quantx-research-governor/`. Installing it is a
directory copy plus one required edit. Inspect the files before enabling them —
`SKILL.md` grants and withholds permissions, and you should know which.

## Claude Code

```bash
git clone https://github.com/junyaoxian-droid/QuantX-Research-Governor.git
cd QuantX-Research-Governor
mkdir -p ~/.claude/skills
cp -R skills/quantx-research-governor ~/.claude/skills/
```

Project-local instead of global:

```bash
mkdir -p .claude/skills
cp -R skills/quantx-research-governor .claude/skills/
```

## Codex

```bash
mkdir -p ~/.codex/skills
cp -R skills/quantx-research-governor ~/.codex/skills/
```

## Required Edit After Copying

`SKILL.md` routes to canonical truth files by name. Those names come from one
specific private workspace and will not exist in yours:

```text
STATE.md
CURRENT_SHELL_REGISTRY.md
ACTIVE_STRATEGY_LINES.md
TEST_ACCESS_LEDGER.md
REPRODUCTION_POLICY.md
EXECUTION_REPLAY_CONTRACT.md
DATASETS.md
COMMANDS_AND_CACHE.md
```

Open the `Read Current Truth First` table in `SKILL.md` and replace the right
column with your own files. Delete rows you have no equivalent for rather than
leaving them pointing at nothing — a skill that sends the agent hunting for
missing files is worse than one that says less.

Do the same for `references/report_contract.md`, which assumes an output layout
of `docs/reports/<experiment>_vN/` and an ignored `outputs/<experiment>_vN/`.

Read `references/contract_design.md` and adapt
`templates/experiment-contract.md` before the first formal experiment. In
particular, map the generic Test ledger, canonical governance owners, artifact
paths, and review-role identifiers to your repository.

## Verify

The bundled fixture is an end-to-end lifecycle you can validate:

```bash
python skills/quantx-research-governor/scripts/validate_golden_path.py
```

It defaults to the bundled `assets/golden_path_fixture/lifecycle.json` and
prints `golden-path fixture passed: quantx_governor_golden_path_v2`. Pass a
different `lifecycle.json` path as the one positional argument to validate your
own.

## Customization

Worth changing for your own project:

- request types in the routing table, replaced with your workflow categories,
- the forbidden-action list, which currently encodes research-only safety
  (no broker connection, no live config, no auto-trade),
- evaluation gates and standard metrics,
- failure budget and stop rules,
- the report contract's section list and output file pack.
- the workspace ownership map described in `docs/workspace-governance.md`.

The parts worth keeping as-is: the selection order, the one-shot Test rule, the
test access ledger, and the separation between recommendation and adoption.
Those are the reason the skill exists.

## Uninstall

```bash
rm -rf ~/.claude/skills/quantx-research-governor
```

## Caveats

- Skill trigger behavior depends on your agent environment.
- Keep project-sensitive details out of any copy you share onward.
- This repository is downstream of a private workspace. If you fork it, expect
  upstream edits to arrive as squashed syncs rather than granular commits.
