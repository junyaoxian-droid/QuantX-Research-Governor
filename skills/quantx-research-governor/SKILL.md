---
name: quantx-research-governor
description: Govern strategy research, backtests, source replay, data/cache work, and research-workspace maintenance in private QuantX. Route to canonical evidence, preserve held-out samples, and separate recommendations from adoption. Exclude unrelated finance/coding and external governance repositories unless explicitly in scope.
---

# QuantX Research Governor

Use the lightest workflow that preserves the research question, evidence, and
user's authority. The current task owns scope and synthesis; bounded helpers
may verify fixed work, but may not expand scope or decide adoption.

## Sources And Paths

Start with `STATE.md` and `00_RESEARCH_HUB/README.md`, then classify the lane in
`00_RESEARCH_HUB/STRATEGY_WORK_INTAKE.md` before creating scripts or artifacts.
Repository paths below are relative to the QuantX repository root, including
when this skill is installed elsewhere. `references/`, `assets/`, and
`scripts/` links in this skill are relative to the skill directory.

| Need | Canonical repository source |
|---|---|
| Collaboration, ownership, Git authority, closeout | `AGENTS.md` |
| Current core and strategy roles | `00_RESEARCH_HUB/CURRENT_SHELL_REGISTRY.md`, `00_RESEARCH_HUB/ACTIVE_STRATEGY_LINES.md` |
| New baseline / replacement base | `00_RESEARCH_HUB/NEW_BASELINE_RESEARCH.md` |
| Research status and adoption | `00_RESEARCH_HUB/CURRENT_RESEARCH_MAP.md`, `00_RESEARCH_HUB/STRATEGY_GOVERNANCE.md` |
| Data/cache facts and commands | `DATASETS.md`, `00_RESEARCH_HUB/COMMANDS_AND_CACHE.md`, the named canonical monitors |
| Execution assumptions | `00_RESEARCH_HUB/EXECUTION_REPLAY_CONTRACT.md`, `00_RESEARCH_HUB/EXECUTION_DISCIPLINE.md` |
| Reproduction | `00_RESEARCH_HUB/REPRODUCTION_POLICY.md` |
| Current / historical reports | `docs/reports/CURRENT_REPORTS.md`, `docs/reports/RESEARCH_INDEX.md` |
| Test access and blind state | `00_RESEARCH_HUB/TEST_ACCESS_LEDGER.md` |
| Shared contract clauses | `00_RESEARCH_HUB/CONTRACT_BOILERPLATE.md` |
| Research-method policy | `docs/reports/quantx_research_protocol_v2/REPORT.md` |
| Artifact placement and retention | `docs/REPOSITORY_MAP.md`, `docs/reports/ARTIFACT_HYGIENE.md`, `docs/reports/PROVENANCE_RETENTION.md` |
| Script and lifecycle mechanics | `code/scripts/SCRIPT_LIFECYCLE.md`, `code/scripts/quantx_git_guard_v1.py`, `.codex/hooks.json` |

Moving strategy identities, metrics, dates, and conclusions belong to these
owners, not this skill. Historical report names never establish current status.

## Choose The Route

| Route | Scope and boundary | Read when needed |
|---|---|---|
| `standard_check` | Freeze one question, baseline, inputs, split, and output; no broad grid | report or research reference relevant to the check |
| `pre_goal_scout` | Small diagnostic or skeleton; do not spend a future experiment budget | goal templates only when planning an upgrade |
| `plan_stress_test` | Explicit challenge of a plan; return `decided`, `open_risk`, `deferred`, `next_route`; no edits, compute, or helpers | the proposed plan and its canonical constraints |
| `governance_patch` | Only the requested docs, skill, or infrastructure layer; no strategy computation | governance and closeout |
| `cache_refresh` | Governed updater and exact allowlist; no strategy signal | repository commands/cache page and target monitor |
| `heavy_experiment` | Contract, ledger, resource gate, adaptive evidence, completion audit | goal, contract, research, and runtime references |
| `independent_review` | Frozen candidate and decision question; no tuning or rescue | contract design and subagent policy |
| `signal_or_trade_review` | Registry first; no adopted core means no current strategy plan | current registry, roles, and governed runbook |
| `open_source_stewardship` | Explicitly scoped external mirror; sanitize before sync | governance and closeout plus target repository rules |

A future goal mentioned during exploration does not turn a scout into a large
experiment. Fewer than five effective iterations usually stay lightweight;
sustained adaptive search, material compute, or broad promotion-affecting work
requires a contract and ledger. Even a short held-out-sample opening needs the
appropriate frozen contract and independent review. Classify by consequence,
not runtime alone.

## Conditional References

Read the relevant reference before the action it governs. Load only the
sections needed for the selected route; do not load every reference for context.

| When | Skill reference |
|---|---|
| Large-experiment intake, Plan bridge, contract/ledger, iteration accounting | [goal templates](references/goal_templates.md) |
| Explicit native goal request or an already active native goal | [native goal control](references/native_goal_control.md) |
| Frozen/promotion-affecting contract, semantic preflight, runner conformance | [contract design](references/contract_design.md) |
| Sample selection, cost/cadence stress, failure and multiplicity controls | [research protocol](references/research_protocol.md) |
| Heavy computation, memory, heartbeat, resume | [runtime and resources](references/runtime_and_resources.md) |
| Creating a report or review pack | [report contract](references/report_contract.md) |
| Delegating a fixed task or conducting independent review | [subagent policy](references/subagent_policy.md) |
| Changing or verifying lifecycle wiring and its synthetic example | [golden-path fixture](references/golden_path_fixture.md) |
| Governance edits, Git closeout, installation or external mirror sync | [governance and closeout](references/governance_and_closeout.md) |

The research and contract references are operational guides. Canonical policy
and the content identity bound by an already frozen contract retain ownership.

## Research And Execution Boundaries

- Keep research separate from broker connections, auto-trading, live config,
  and real account records. Update a private execution journal only when the
  user requests a scoped journal change.
- Read the registry before any strategy card or runner. If `current_core=None`,
  return `no_current_core`; retired, candidate, reference, or sidecar artifacts
  do not authorize current signals or a next-day strategy plan.
- Historical replay requires the user's explicit scope and governed opt-in.
  Label it `retired_historical_replay`. For an adopted core, use its current
  runner/runbook, confirm freshness, and separate model output from manual
  execution facts. Do not stitch legacy reports into a current signal.
- Use PIT-safe inputs and labels. Do not use news, manual tape-reading, or
  future information as historical features.
- Train generates candidates; Validation selects; Test opens once after freeze.
  Every new computation or report generation reading held-out Test observations
  or metrics appends `00_RESEARCH_HUB/TEST_ACCESS_LEDGER.md` in the same closeout.
  Reading an existing tracked report is not a new Test access.
- Unopened splits stay `not_opened`. Do not access Test to fill a report template.
  Post-sample/latest data is monitoring evidence, never selection or rescue.
- Distinguish rolling stress from true dynamic rolling reselection. Apply
  matched controls, search-breadth/multiplicity disclosure, cadence and cost
  stress when relevant; do not present Test-best or OOS-only results as proof.
- Separate `evidence_structure`, `role_fit`, and `personal_execution` gates.
  Verify candidate quality before account-path promotion; execution-relevant
  claims must use the governed practical replay assumptions.
- Preserve negative findings and failure logs. Closed lines stay closed unless
  the user explicitly reopens them.

## Contract And Review Discipline

Before formal output, check instrument resolution, sample supply, reachable
failure conditions, mutually exclusive terminals, matched controls, and
statistic-appropriate uncertainty. Bind shared clauses to a retrievable content
identity and map frozen requirements to runner evidence in
`contract_runner_conformance.json`. Hash agreement does not establish that the
contract asks a valid question.

For large work, materialize and verify `GOAL.md` and `ITERATION_LEDGER.md`
before compute. Preserve already granted execution authority; ask only for
material unresolved constraints. Native goal tracking is separate and requires
explicit authorization under [native goal control](references/native_goal_control.md).

Choose iteration N+1 from iteration N's evidence, not a pre-spent queue.
Preparation, environment repair, reproduction used for setup, bug fixes, and
report cleanup are not counted research iterations. Freeze promising candidates
before review; a failed branch does not close a broader authorized search.

Promotion-affecting evidence needs a reviewer independent of the search and
contract drafting. Record builder, drafter, searcher, and reviewer roles
truthfully using the canonical relation schema; a self-review cannot drive
governance. A numerical postformal review recomputes at least one headline
figure from source, varying seeds for sampling. Preformal review checks design
and gate reachability instead. Hand over pointers, hashes, and adverse findings.

Research contracts, user stop rules, and native tool states are distinct.
Honor a user stop immediately; never mark a native goal complete merely because
the research budget ended or the user terminated the work.

## Artifacts And Adoption

Continue an existing `_vN` family when the hypothesis and evaluation object
are continuous. Use a new family only for a materially different object.

```text
code/scripts/experiments/<experiment_id>/   one-off code
docs/reports/<experiment_id>/               lightweight review pack
outputs/<experiment_id>/                    ignored full local evidence
```

Top-level `code/scripts/` additions need a reusable/current or governed-reference
role and an entry in `code/scripts/CURRENT_SCRIPT_MANIFEST.txt`. Do not create
new root experiment directories or use a cleanup to relocate historical code.

Keep full grids, raw events, daily paths, vendor data, and debug traces local.
Retain lightweight reports, commands, contracts, ledgers, scorecards, conformance
receipts, and reproduction handoffs. Ignored does not mean disposable; apply
the provenance registry before pruning any pre-existing evidence.

| Result label | Permitted interpretation |
|---|---|
| `recommended_upgrade` | proposal awaiting independent review and user adoption |
| `source_replay_candidate` | frozen candidate needing reproduction |
| `paper_shadow_candidate` | monitor only |
| `manual_review_candidate` | human-review evidence only |
| `diagnostic_only` | clue, not a strategy rule |
| `stop_as_rule` | closed unless explicitly reopened |

Evidence and independent review may support a recommendation. Only explicit
user adoption authorizes updating current-core governance; a report verdict or
skill edit never adopts a strategy.

## Route-Specific Operations And Closeout

Cache work uses the existing updater's atomic/staging path, timeouts, retry
caps, locks, and circuit breaker. Keep one updater per target; stop at a
recoverable failure rather than retrying indefinitely. Use `Asia/Shanghai`
for data-day interpretation. Keep app automation identifiers and schedules
outside repository docs. The cache helper's `AUTO_ALLOWED_EXACT` owns staging.

Heavy runs use `code/scripts/quantx_heavy_run_guard_v1.py` and the runtime
reference; estimate scale and use a staged funnel before broad grids. Stop an
active process only under current user authorization or its approved stop rule.

Use bounded helpers under the subagent reference; create a separate Codex task
only on an explicit user request. The current task remains responsible for
scope, synthesis, and verifying the helper's output.

Follow `AGENTS.md` for write-task closeout, ownership, and Git authority.
A read-only audit reports checks and findings without manufacturing artifacts
or a commit. For edits, run relevant checks and workspace closeout, retain other
threads' changes, and stage only owned exact paths. The detailed governance
reference supplies commands, not additional authorization.

Match the user's language, explain unfamiliar abbreviations briefly, and lead
with the result and evidence limits. Report what changed, validation, excluded
dirty paths, and whether local commits or remote sync actually succeeded.
