# QuantX Subagent Policy

Use subagents only when they reduce risk or wall time.

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
builder/search task id and distinct reviewer task id
decision question
input and artifact paths
parameters and sample splits
primary evidence and declared caveats
forbidden scope changes
```

The reviewer must not tune, substitute candidates, add a rescue hypothesis, or
change the evaluation scope. No scope changes are allowed during this pass.
Require this output:

```text
verdict = confirmed | partially_confirmed | not_confirmed | invalidated
confirmation_level = independent_reproduction | independent_analysis | self_review_only
builder_task_id != reviewer_task_id for an independent claim
counterevidence
protocol_deviations
remaining_uncertainty
adoption_ready = yes | no
```

Persist each independent review in the experiment's append-only
`review_history.jsonl`. A later synthesis may supersede an earlier verdict, but
must retain the earlier counterevidence and protocol deviations rather than
overwriting them.

Use a bounded helper when a genuinely separate pass is practical. If the
searching agent also performs the review, label it `self_review_only`; it does
not satisfy the independent-review gate for a promotion-affecting adoption
proposal.

## Integration

The main thread must:

```text
check subagent outputs
merge only verified findings
label disagreements
make the final recommendation
decide whether to continue or stop
```
