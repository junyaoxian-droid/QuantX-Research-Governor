# QuantX Goal Templates

## Contents

- Goal minimality and vague-goal intake
- QuantX Plan-to-GOAL bridge
- Large iterative strategy goal
- Iteration ledger template
- Pre-goal scout
- Single-hypothesis, signal-review, and governance templates
- Native goal authorization and integrity
- Adaptive iteration and candidate freeze
- User stop / pause handling
- Native goal completion audit

## -1. Goal Minimality

Most QuantX tasks should not use GOAL.md or native Codex goal tracking.

```text
No GOAL.md / no create_goal for:
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

If a small task grows into a broad search, pause and ask whether to upgrade to
a GOAL.md-backed large experiment.
```

## 0. Vague Goal Intake

Use before any large experiment when the user gives a fuzzy direction.

```text
Ask first:
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

Do not call create_goal and do not run broad search until these are captured,
shown to the user, and explicitly confirmed. The only exception is a QuantX
Plan-to-GOAL bridge where the user explicitly chose
`contract_then_execute_if_faithful`; even then, GOAL.md and
ITERATION_LEDGER.md must be written and verified before create_goal or compute.

After the user confirms a large iterative GOAL.md contract with "确认",
"同意", "确认，执行", "确认，都同意", or equivalent wording, open native
Codex goal tracking by default before compute unless the user explicitly opts
out. The native goal objective must include:
Experiment contract: docs/reports/<experiment_family>_vN/GOAL.md
Iteration ledger: docs/reports/<experiment_family>_vN/ITERATION_LEDGER.md

If an active native goal exists but does not include both the GOAL.md path and
the ITERATION_LEDGER.md path, pause and ask the user to close/recreate/edit it
before running the large experiment.
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
governance cleanup, or pre-goal scout, do not create GOAL.md or native goal.
Use the lightest workflow for that task.

Plan intake should end with this bridge choice:

```text
执行 Plan 后的衔接方式：
1. 先落 GOAL.md + ITERATION_LEDGER.md，展示后等我确认。（推荐）
2. 先落文件；若它们忠实反映本 Plan，则直接开启 native goal 并执行。
3. 只落文件，不开启 native goal。
```

Map the answer to:

```text
contract_only:
  write GOAL.md and ITERATION_LEDGER.md first, show them, wait for confirmation.

contract_then_execute_if_faithful:
  write GOAL.md and ITERATION_LEDGER.md first; if verification passes, open
  native goal with both paths in the objective and then execute.

no_native_goal:
  write GOAL.md and ITERATION_LEDGER.md first; execute without native goal only
  after the user explicitly opted out.
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
permits skipping GOAL.md, the ledger, question-to-goal trace, or native-goal
integrity checks.

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
- Respect static top1500 caveat.
- 2026-05+ real operations are monitor-only unless explicitly scoped.

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
- One iteration means: hypothesis -> complete the agreed experiment evidence
  path -> read outputs -> verdict -> next direction.
- The following do not count as iterations: intake/GOAL/ledger writing,
  environment or data checks, compile/smoke, guard/preflight, baseline
  reproduction/source replay used to verify setup, bug fixes, report cleanup,
  and reruns after fixes.
- Record prep/audit/reproduction work in ITERATION_LEDGER.md with
  `iteration_counted=no`.
- Do not pre-schedule all <N> iterations as lightweight probes unless this GOAL explicitly says so.
- Continue after one failed run, but choose the next direction from the observed evidence.
- Stop once the declared success criteria are met and verified.
- Pause after <N> independent failures or a suspected data/label bug.
- Stop/pause immediately if the user asks to stop, pause, or terminate the goal.
- Do not claim the goal is stopped while the native goal remains active; pause
  it with the native control or complete it when the user explicitly terminates it.

Outputs:
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
- Native goal objective includes GOAL.md and this ledger: yes/no
- Status: draft / active / user_paused / user_terminated / success / failed_budget / blocked_by_bug
- Native goal state: not_opened / active / paused / completed / needs_user_ui_pause
- Native goal close reason: none / user_pause / user_terminated / success / failure_budget / data_bug

Plan-To-GOAL Bridge:
- Came from Plan mode: yes/no
- Bridge authorization: contract_only / contract_then_execute_if_faithful / no_native_goal / not_applicable
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
| H1 |  |  |  |  |  |
```

## A0. Pre-Goal Scout

Use when the user asks for a new isolated strategy line or exploratory probe,
and says the large goal should happen only if the scout looks promising.

```text
Classification:
- pre_goal_scout, not large_iterative_experiment.

Native Goal:
- Do not call create_goal.
- Do not create a large GOAL.md contract yet unless the user explicitly asks.
- Treat "可以规划一个 goal" or "迭代强度可设为 N 次" as future planning hints.

Scope:
- Folder: <user-requested isolated scout folder, e.g. <new_family_scout>/>.
- Read shared workspace context and current cache contracts.
- Keep early work small: data inspection, hypothesis sketch, small sample,
  reproducible skeleton, or scout note.
- Do not disturb adopted governance or other research lines.

Output:
- <folder>/SCOUT_PLAN.md or <folder>/README.md when useful.
- What evidence would justify promotion to GOAL.md.
- Open questions before a large experiment.

Promotion:
- If the scout is promising, draft docs/reports/<experiment>_vN/GOAL.md.
- Show the contract path and wait for explicit confirmation.
- After confirmation, open native Codex goal tracking by default unless the
  user explicitly says not to, and include both GOAL.md and ITERATION_LEDGER.md
  paths in the objective.
```

## B. Single Hypothesis Check

Use when the user wants to test one idea.

```text
Native Goal:
- Do not call create_goal.
- Do not create GOAL.md unless the user explicitly upgrades this to a large iterative experiment.

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
Native Goal:
- Do not call create_goal.
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
Native Goal:
- Do not call create_goal.
- Do not create GOAL.md unless the user explicitly asks for a long-running governance goal.

Read current source-of-truth files.
Patch only minimal divergence.
Prefer pointers and short summaries over duplicated long facts.
Update repository map / artifact hygiene when file roles change.
Do not delete important reports.
Do not touch data_cache, outputs, positions, live config.
Report remaining divergences and commit scope.
```

## E. Native Goal Authorization And Integrity

Treat “goal” as planning language until the user has seen the GOAL.md path and
a concise contract summary.

Do not interpret these as `create_goal` authorization before contract review:

```text
可以规划一个 goal
可以考虑开 goal
先探索，有可能后再大规模实验
我希望你想一个 goal
先帮我确认 / 先问我问题
```

After the large contract has been shown, treat clear execution confirmation as
authorization to open native goal tracking unless the user opts out:

```text
确认，执行
确认，都同意
按这份 GOAL.md 跑
确认，开启 native goal
```

Before compute, verify:

```text
GOAL.md exists and matches confirmed requirements
ITERATION_LEDGER.md exists and matches GOAL.md
question-to-goal trace is complete
native goal is authorized or the user explicitly opted out
native objective includes both contract paths
resource gate is recorded for heavy work
```

If an active native goal lacks either path, pause and ask the user to repair or
recreate it. Do not continue a large experiment under an unlinked native goal.

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
3. Update the ledger with `user_paused`, `user_terminated`, or the actual
   available native state.
4. Use the native pause control when available. If it is unavailable, explain
   that UI pause or termination is still required.
5. Do not claim the goal is paused or stopped while native state remains active
   without explicitly saying what user action remains.
6. Preserve completed iterations, artifacts, and the exact resume command.

## H. Native Goal Completion Audit

Before `update_goal(status="complete")`, read:

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

Do not complete while any required item is `still_open` unless the user accepts
early closure after seeing the remaining work.

Complete only when one of these closes the whole goal:

```text
verified success gate
effective-iteration or independent-failure budget exhausted
user termination or accepted early closure
fatal whole-goal data/PIT/baseline issue
declared whole-goal stop rule
```

Failure of one branch, mapping gate, or replay path is not whole-goal
completion while budget remains. Record `needs_next_iteration`,
`needs_reproduction`, or a real paused state instead.

Final closeout must state the close reason, counted iterations versus budget,
open risks, adoption boundary, and the next useful plan.
