# QuantX Subagent Policy

Use subagents only when they reduce risk or wall time.

Default bounded helpers to `medium` reasoning effort; honor an explicit user
override. Give a fresh helper the minimum context for its fixed task. A helper
is not a separate user-owned Codex task.

## Allowed

```text
data and label audit
fixed-configuration replay
independent report QA
parallel line comparison with frozen specs
reproduction handoff drafting
checking whether outputs match protocol
frozen independent falsification / red-team review
```

## Not Allowed

```text
final promotion decision
scope expansion
inventing new strategy families without user approval
changing safety boundaries
editing positions or live config
using Test results to tune candidates
```

## How To Delegate

Give the subagent:

```text
exact file paths
frozen parameters
expected outputs
what not to touch
how to report failures
```

Do not give the intended answer unless the task is pure QA.

## Independent Review Contract

Give the reviewer a frozen packet:

```text
candidate and claim
builder, contract drafter, searcher (when applicable), and reviewer task ids
decision question
input and artifact paths
parameters and sample splits
primary evidence and declared caveats
forbidden scope changes
```

The reviewer must not tune, substitute candidates, add a rescue hypothesis, or
change the evaluation scope. No scope changes are allowed during this pass.
Return a verdict, counterevidence, protocol deviations, remaining uncertainty,
the actual review relation and confirmation level, and the adoption boundary.
Use the role/level mapping in
[contract design](contract_design.md#review-relations-and-handoff); the private
workspace's `AGENTS.md`, `00_RESEARCH_HUB/CONTRACT_BOILERPLATE.md`, and
`code/scripts/quantx_research_contract_gate_v1.py` own the record contract.
Do not treat a distinct task id alone as proof of substantive independence.

Persist each formal review, including a disclosed non-independent review, in the experiment's append-only
`review_history.jsonl`. A later synthesis may supersede an earlier verdict, but
must retain the earlier counterevidence and protocol deviations rather than
overwriting them.

If the searching agent also reviews the finding, record the actual entanglement
under that mapping. Do not identify a searcher as the contract drafter unless
it drafted the contract. A non-independent review is a valid record but cannot
satisfy a promotion-affecting independent-review gate.

## Integration

The main thread must:

```text
check subagent outputs
merge only verified findings
label disagreements
make the final recommendation
decide whether to continue or stop
```
