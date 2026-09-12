# QuantX Goal Templates

## Contents

- Goal minimality and vague-goal intake
- QuantX Plan-to-GOAL bridge
- Large iterative strategy goal
- Iteration ledger template
- Pre-goal scout
- Single-hypothesis, signal-review, and governance templates
- Contract readiness
- Adaptive iteration and candidate freeze
- User stop / pause handling
- Research closure audit

This file governs experiment contracts and research iteration. Optional Codex
native goal controls are governed only by [native_goal_control.md](native_goal_control.md).
GOAL.md, experiment execution authorization, and native tracking authorization
are separate. An authorized experiment may run without native tracking; do not
ask the user to opt out of a feature they did not request.

## -1. Goal Minimality

Most QuantX tasks should not use GOAL.md or native Codex goal tracking.

```text
No GOAL.md by default for:
- signal/trade status review
- one bounded hypothesis or one replay
- small/medium validation or exploration with fewer than 5 effective iterations
- pre-goal scout
- governance cleanup, cache hygiene, report/code review
- bug fix, smoke test, compile check, command QA

Use instead:
- final answer
- short report note
- SCOUT_PLAN.md / README.md for isolated scouts
- commands_used.md / existing report section

Upgrade only when:
- the work becomes a large iterative experiment, normally 5 or more effective iterations
- results may affect active strategy governance
- the user explicitly asks for a durable experiment contract

If a small task grows beyond its authorized scope into a broad search, obtain
approval for the expanded contract. Preserve sufficient existing authorization.
```

## 0. Vague Goal Intake

Use before any large experiment when the user gives a fuzzy direction.

```text
Resolve from existing context first; ask only for consequential missing choices:
- 目标类型: 验证 / 优化 / 诊断 / 治理
- 成功标准:
- 迭代强度: one-shot / 3 independent failures / 4 effective iterations / >=5 large goal / evening run / user-defined
- 停止条件: success gates / failure budget / wall-clock or token cap / suspected data bug / user interrupt
- 预算: one-shot / N independent failures / time / result gate / hybrid
- 因子/候选范围: local factors only / current or referenced families / external data / mixed
- practical replay: use current workspace execution replay contract? overrides?
- subagent / parallel permission:
- commit / push policy:

Then write:
- docs/reports/<experiment_family>_vN/GOAL.md
- docs/reports/<experiment_family>_vN/ITERATION_LEDGER.md
- question-to-goal trace
- stop rules
- output contract

Do not run broad search until the contract and ledger are materialized,
verified, and covered by explicit execution authorization. Show the contract
and obtain confirmation when that authorization is missing. A recorded
`contract_then_execute_if_faithful` choice permits execution after faithful
verification; do not repeat a confirmation already supplied. Native tracking
is optional and follows native_goal_control.md independently.
```

## 0A. QuantX Plan-To-GOAL Bridge

Use only for private QuantX large iterative experiments. Do not use for
quick monitor, one replay, governance cleanup, public-repo stewardship, or
ordinary non-QuantX Plan/goal work.

Trigger only when the user has already opened Plan mode in the Codex UI and
the request is classified as `large_iterative_experiment` or
`heavy_experiment`, normally because it requests 5 or more effective
iterations, may affect strategy governance, or needs broad/high-resource
compute. If the user discusses or edits this bridge from normal chat, treat it
as governance cleanup, not as a live Plan-to-GOAL handoff.

Plan mode boundary:

```text
If the user asks Codex to open/switch Plan mode but the current runtime is not
actually Plan mode, do not imitate Plan mode in normal chat. Tell the user to
switch the UI to Plan mode and resend the goal, or ask them to explicitly choose
plain-chat intake.
```

If the user manually opened Plan mode but the request is quick monitor, one
bounded replay, small/medium validation with fewer than 5 effective iterations,
governance cleanup, or pre-goal scout, use the lightest workflow by default.
Plan mode alone does not require GOAL.md or authorize native tracking.

When the execution handoff is unresolved, offer this bridge choice:

```text
执行 Plan 后的衔接方式：
1. 先落 GOAL.md + ITERATION_LEDGER.md，展示后等我确认。（推荐）
2. 先落文件；若它们忠实反映本 Plan，则直接执行实验。
3. 只落文件，暂不执行。
```

Map the answer to:

```text
contract_only:
  write GOAL.md and ITERATION_LEDGER.md first, show them, wait for confirmation.

contract_then_execute_if_faithful:
  write GOAL.md and ITERATION_LEDGER.md first; execute after faithful verification.

files_only:
  write and verify GOAL.md and ITERATION_LEDGER.md; no compute authorized.

no_native_goal:
  legacy choice: preserve the user's actual execution scope; native tracking
  is excluded, but this label alone does not authorize compute.
```

When the user selects Plan mode "Execute plan", the first actions are:

```text
1. write/update GOAL.md
2. write/update ITERATION_LEDGER.md
3. verify question-to-goal trace
4. show paths and summary, unless bridge_authorization explicitly allows direct execution after faithful verification
```

Never treat Plan mode "Execute plan" as permission to skip GOAL.md, skip the
ledger, call create_goal first, or run compute first.

When a user-approved line-specific pre-goal protocol already selected
`contract_then_execute_if_faithful`, preserve that recorded choice unless the
user overrides it. Record the authorization in `ITERATION_LEDGER.md`; it never
permits skipping GOAL.md, the ledger, or question-to-goal trace. Separately
record whether the approved wording explicitly included native creation;
the bridge label alone is not native authorization. Honor an existing explicit
approval of a displayed plan that included native creation under its own rules.

## A. Large Iterative Strategy Goal

Use when the user asks for a major QuantX experiment, continuous iteration, or broad but disciplined search.

```text
Objective:
- Find robust candidates for <line/family> under strict QuantX Protocol v2.

Scope:
- Lines: <current, candidate, reference, or cross-line scope>.
- Allowed: <feature work, model class, overlay, replay, cadence stress>.
- Forbidden: positions, live config, auto-trading, info/news as historical features.

Budget:
- Type: wall-clock time / iteration count / token budget / result gate / hybrid.
- Iteration strength: one-shot / 3 independent failures / 4 effective iterations / >=5 effective iterations / evening run / user-defined.
- Stop on success: yes.
- Failure budget: <N> independent failures before pausing.
- If near time limit while a run is active: finish current run unless user asked for immediate stop.

Resource Budget:
- Max workers / parallel jobs:
- Expected peak RSS: low (<10G) / normal (10-25G) / warning (25-30G) / unsafe (>30G).
- Intervention threshold:
- Process-stop authorization: user-confirmed now / pre-approved in GOAL.md / not approved.
- Allowed high-memory condition:
- Non-chunkable justification if peak RSS may exceed 30G:
- Chunking key: score_id / hypothesis / date window / candidate family.
- Cache/materialization plan:
- Resume policy for partial chunks:
- Guard command: `.venv/bin/python code/scripts/quantx_heavy_run_guard_v1.py ... -- .venv/bin/python ...`
- If a single Python process exceeds 30G RSS, first classify whether this is a planned bounded phase or unsafe growth; stop the process only with explicit user approval or a pre-approved GOAL.md stop rule.

Data:
- Use current DuckDB/Parquet.
- Record the current dataset's universe-selection and survivorship caveats.
- Recent real operations and post-sample evidence are monitor-only unless
  explicitly scoped; obtain boundaries from the current data/replay contract.

Selection:
- Train first.
- Validation selects parameters.
- Test opens once after selection.
- Label Test-best-but-not-selected rows accordingly.

Evaluation:
- Train / Validation / Test annualized, DD, Calmar, win rate.
- Monthly / semimonthly / weekly / day10 / day20 cadence.
- 20 / 50 / 100 bps cost stress.
- Practical account replay: follow the workspace execution replay contract when execution-relevant.
- Contribution concentration and failure log.

Iteration:
- Try up to <N> effective adaptive iterations.
- Apply section F's complete evidence-loop counting rule; record preparation
  and audit work with `iteration_counted=no`.
- Do not pre-schedule all <N> iterations as lightweight probes unless this GOAL explicitly says so.
- Continue after one failed run, but choose the next direction from the observed evidence.
- Stop once the declared success criteria are met and verified.
- Pause after <N> independent failures or a suspected data/label bug.
- Stop/pause immediately if the user asks to stop, pause, or terminate the goal.
- Record research stop reasons independently of any native state (section G).

Outputs:
- code/scripts/experiments/<experiment_family>_vN/ for one-off code
- docs/reports/<experiment_family>_vN/
- outputs/<experiment_family>_vN/ ignored
- Plan-to-GOAL bridge choice when the experiment came from Plan mode.
- ITERATION_LEDGER.md with current budget, completed effective iterations, last verdict, and next allowed action.
- REPORT.md, commands_used.md, summary CSVs, REPRODUCTION_HANDOFF_PROMPT.md when useful.
- practical_account_replay_summary.csv when execution relevance is claimed.
- resource note if memory was high, user-approved stop was used, or the script was refactored.
```

## A1. Iteration Ledger Template

Write this as `docs/reports/<experiment_family>_vN/ITERATION_LEDGER.md` for
large iterative experiments.

```text
# Iteration Ledger

Goal:
- GOAL.md:
- Status: draft / active / user_paused / user_terminated / success / failed_budget / blocked_by_bug
- Research stop/close reason:
- Native tracking (optional): use the audit fields in native_goal_control.md;
  record not_requested when absent, never infer state from research status.

Plan-To-GOAL Bridge:
- Came from Plan mode: yes/no
- Bridge authorization: contract_only / contract_then_execute_if_faithful / files_only / no_native_goal (legacy) / not_applicable
- Execution authorization source and exact scope:
- Native creation explicitly included in approval: yes/no; source wording:
- Plan answers encoded in GOAL.md: yes/no
- Verified faithful to Plan before execution: yes/no
- Next confirmation required: yes/no

Budget:
- Max effective iterations:
- Completed effective iterations:
- Iteration counting rule: only complete experiment loops count; prep/checks/smoke/guard/reproduction/reruns after fixes use `iteration_counted=no`.
- Failure budget:
- Current stop rules:

Resource Gate:
- Guard command:
- Expected peak RSS:
- Intervention threshold:
- Memory observability: Codex best-effort only; guard RSS may be unavailable.
  Use design estimates first, and treat user/Activity Monitor reports as valid
  evidence.

Current State:
- Current hypothesis:
- Last completed run:
- Last verdict:
- Next allowed action:
- Do not continue if:

Iteration Log:
| Iteration | Type | Iteration counted? | Hypothesis / prep purpose | Run/artifact | Evidence read | Verdict | Next direction |
|---|---|---|---|---|---|---|---|

Use `Type=experiment` and `Iteration counted?=yes` only for complete
experiment loops. Use `Type=prep/audit/reproduction/fix/report` and
`Iteration counted?=no` for setup, checks, source replay, bug fixes, and
report cleanup.
| H1 |  |  |  |  |  |  |  |
```

## A0. Pre-Goal Scout

Use when the user asks for a new isolated strategy line or exploratory probe,
and says the large goal should happen only if the scout looks promising.

```text
Classification:
- pre_goal_scout, not large_iterative_experiment.

Contract:
- Do not create a large GOAL.md contract yet unless the user explicitly asks.
- Treat "可以规划一个 goal" or "迭代强度可设为 N 次" as future planning hints.

Scope:
- Code: code/scripts/experiments/<scout_id>/.
- Full artifacts: outputs/<scout_id>/ (ignored).
- Review pack: docs/reports/<scout_id>/.
- Read shared workspace context and current cache contracts.
- Keep early work small: data inspection, hypothesis sketch, small sample,
  reproducible skeleton, or scout note.
- Do not disturb adopted governance or other research lines.

Output:
- docs/reports/<scout_id>/SCOUT_PLAN.md or README.md when useful.
- What evidence would justify promotion to GOAL.md.
- Open questions before a large experiment.

Promotion:
- If the scout is promising, draft docs/reports/<experiment>_vN/GOAL.md.
- Materialize and verify the matching ITERATION_LEDGER.md before compute.
- Show the contract and obtain execution authorization if not already given.
- Apply section 0's intake and readiness gates; native tracking stays optional.
```

## B. Single Hypothesis Check

Use when the user wants to test one idea.

```text
Contract:
- Do not create GOAL.md unless the user explicitly requests a durable contract
  or upgrades this to a large iterative experiment.

Objective:
- Test whether <hypothesis> improves <line> under fixed evaluation.

Keep small:
- No broad grid.
- No new model family unless required.
- Compare against the current baseline and one obvious control.

Report:
- Main table, failure cases, whether it deserves v2.
```

## C. Signal / Trade Review

Use for strategy status, an adopted-core signal, or execution discipline.

```text
Contract:
- Do not create GOAL.md.

Read CURRENT_SHELL_REGISTRY.md before any strategy artifact or runner.
If current_core=None:
- Return no_current_core.
- Do not derive a strategy plan from retired, candidate, reference, or sidecar lines.

If an adopted core exists:
- Do not train or rerank.
- Read its current signal artifact and confirm freshness.
- Separate model signal from manual holdings.
- Produce an if/then plan only within the adopted execution contract.

For explicit retired replay:
- Require its governed opt-in.
- Label retired_historical_replay.
- Do not imply current execution authority.

Record discretionary facts only when the user asks for a journal update.
```

## D. Governance Cleanup

Use for project memory and workspace organization.

```text
Contract:
- Do not create GOAL.md unless the user explicitly asks for a long-running governance goal.

Read current source-of-truth files.
Patch only minimal divergence.
Prefer pointers and short summaries over duplicated long facts.
Update repository map / artifact hygiene when file roles change.
Do not delete important reports.
Do not touch data_cache, outputs, positions, live config.
Report remaining divergences and commit scope.
```

## E. Contract Readiness

Before compute, verify:

```text
GOAL.md exists and matches confirmed requirements
ITERATION_LEDGER.md exists and matches GOAL.md
question-to-goal trace is complete
execution authorization covers this scope
resource gate is recorded for heavy work
```

If native tracking was explicitly requested, also apply
[native_goal_control.md](native_goal_control.md). Its absence does not block
an otherwise authorized experiment.

## F. Adaptive Iteration And Candidate Freeze

Count an effective iteration only when it completes:

```text
hypothesis
-> full agreed evidence path
-> output readout
-> attribution
-> verdict
-> next decision
```

Do not count:

```text
intake or GOAL/ledger writing
environment and data checks
compile, smoke, guard, or preflight
baseline reproduction used to verify setup
source replay used only for reproduction
bug or data-alignment fixes
report cleanup
reruns after fixes
extra charts or narrow sensitivity rows for the same hypothesis
```

Record each counted iteration with:

```text
iteration_id
status
hypothesis
prior_evidence_or_pivot_reason
experiment_design
expected_result
commands_and_artifacts
result_readout
analysis_attribution
verdict
next_decision
iteration_counted=yes
```

Choose iteration N+1 only after reading iteration N. Deepen a concrete clue,
pivot from an identified failure mode, or stop under a declared rule. Do not
select the next experiment from a prewritten queue when evidence points
elsewhere.

When a candidate clears a gate:

1. Freeze its features, thresholds, permissions, action surface, sample split,
   costs, replay contract, and output paths.
2. Run required PIT, provenance, practical replay, cadence, cost, rolling,
   concentration, and reproduction checks.
3. Classify it as recommendation, source replay, paper shadow, manual review,
   diagnostic, or stop-as-rule.
4. Continue in a materially different direction while budget remains unless
   the whole-goal success or stop rule is satisfied.

Do not squeeze adjacent thresholds after freeze to make a candidate look
better. Adjacent work must be a declared audit or a materially different
representation, source, action surface, or portfolio-construction hypothesis.

## G. User Stop / Pause Handling

Treat these as immediate control instructions:

```text
可以终止 goal 了
目标暂停 / 先暂停 / 先停
不要继续 / 不用继续
做到这里 / 等我回来再继续
```

Then:

1. Do not launch more compute.
2. Do not kill an active process unless the user explicitly requests it or a
   confirmed GOAL.md stop rule authorizes it.
3. Record the research status `user_paused` or `user_terminated`, the reason,
   completed iterations, artifacts, active-process status, and exact resume command.
4. If native tracking exists, record its actual state separately and apply
   native_goal_control.md. Report accurately that new research work has stopped
   even if native state is still active; do not imply a native transition occurred.

## H. Research Closure Audit

Before closing or handing off the research, read:

```text
GOAL.md
ITERATION_LEDGER.md
latest REPORT.md or iteration report
```

Classify every required objective, gate, output, replay, and budget item as:

```text
satisfied
exhausted_by_declared_stop_rule
explicitly_waived_by_user
blocked_by_fatal_data_or_baseline_issue
still_open
```

Keep unresolved items visible. User acceptance of early research closure does
not turn unmet objectives into satisfied ones or complete a native goal.

Record the actual whole-research close reason:

```text
verified success gate
effective-iteration or independent-failure budget exhausted
user termination or accepted early closure
fatal whole-goal data/PIT/baseline issue
declared whole-goal stop rule
```

These are research outcomes, not native status mappings. Apply
native_goal_control.md before any native state update. Failure of one branch,
mapping gate, or replay path is not whole-research closure while budget remains
and no whole-goal stop rule applies. Record `needs_next_iteration`,
`needs_reproduction`, or the actual research pause reason instead.

Final closeout must state the close reason, counted iterations versus budget,
open risks, adoption boundary, and the next useful plan.
