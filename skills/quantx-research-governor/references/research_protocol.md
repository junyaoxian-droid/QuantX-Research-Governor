# QuantX Research Protocol Reference

## Contents

- Canonical ownership
- Strict selection order
- Test access ledger
- Required tables
- Placebo and selection deflation
- Experiment versioning
- Cadence stress
- Cost and execution
- Failure handling

Canonical ownership:

```text
docs/reports/quantx_research_protocol_v2/REPORT.md
```

That versioned report owns QuantX research-method policy. This skill reference
is only a compact operational checklist for agents. If wording conflicts, use
the canonical report for policy and current Hub files for current project facts.

## Strict Selection Order

For new strategy candidates:

```text
1. Build labels and features using only point-in-time information.
2. Train period: generate candidates and estimate parameters.
3. Validation period: select candidates and parameters.
4. Freeze selected rows.
5. Test period: open once and report honestly.
6. Do not tune on Test.
```

Before any computation or report generation reads held-out Test observations or
Test metrics, check and then update:

```text
00_RESEARCH_HUB/TEST_ACCESS_LEDGER.md
```

If a Test result is excellent but was not selected by Validation, mark:

```text
test_best_not_selected
```

If a row only looks good in OOS while Train fails, mark:

```text
oos_only_trap
```

## Test Access Ledger

Record every new Test evaluation in the ledger as part of the same experiment
closeout. Include frozen-display reruns and independent reproduction; do not
count opening or quoting an already-generated tracked report.

Use the next integer `access_seq` for that strategy line. If old reports prove
Test was already opened but the historical count is unknown, preserve a single
`legacy` baseline instead of inventing a number. A repeated Test access cannot
restore blindness and must not tune, select, or rescue the candidate.

## Required Tables

Core tables:

```text
strategy / candidate_id / line
Train annualized / DD / Calmar / win rate
Validation annualized / DD / Calmar / win rate
Test annualized / DD / Calmar / win rate
monthly / semimonthly / weekly / day10 / day20
20bps / 50bps / 100bps
verdict
```

## Placebo And Selection Deflation

For any layer delta that could affect promotion, predeclare and run a matched
placebo, null, or negative-control calibration. Match the placebo to the claim's
sample opportunity, holding/cadence structure, cost assumptions, and search
budget closely enough that the comparison measures the proposed delta rather
than an easier benchmark.

Report at least:

```text
layer delta and frozen primary claim
placebo / null construction and why it is matched
number of candidates, variants, anchors, and hypotheses searched
raw effect versus placebo distribution
multiplicity or selection-deflation method
deflated conclusion and failure threshold
```

If a valid matched placebo is impossible, label the result diagnostic or
exploratory and state the limitation; do not promote from the raw delta alone.

## Gate Classes And Preformal Reachability

Every fresh contract must label each gate as one of:

```text
evidence_structure
role_fit
personal_execution
```

Only `evidence_structure` gates may support a source/structure terminal.
Minimum desired trading frequency, invested share, cash preference, and other
standalone-base preferences belong to `role_fit`; lot, cost, turnover burden,
and operational constraints belong to `personal_execution`. A role or
execution failure may reject the object for that use, but must not be rewritten
as evidence that the information source lacks structure.

Before formal, establish that the gate conjunction is reachable and that
expected supply is sufficient for the planned uncertainty or power statement.
Derive activity bounds from the mechanism and intended role. Do not copy
minimum-frequency or cash constants from another experiment as workspace-wide
defaults.

## Experiment Versioning Checklist

Before creating an experiment name:

```text
rg "<keywords>" code docs/reports 00_RESEARCH_HUB
```

Continue an existing family when:

```text
same strategy line
same market hypothesis
same output audience
same core evaluation object
```

Start a new family only when:

```text
new label family
new model family
new execution architecture
new governance layer
new data source or PIT audit
```

Use:

```text
<family>_v1
<family>_v2
<family>_v3
```

Avoid scattering unrelated one-off `v1` folders.

## Cadence Stress

When relevant, show:

```text
month_end
semimonth
weekly
day10 monthly anchor
day20 monthly anchor
```

Do not promote a strategy that only works on one convenient anchor unless the report clearly labels it as an anchor-specific clue.

For promotion work on any future current core, weight continuous account-path
evidence and true reset/random-start robustness as primary evidence. Treat
fixed calendar anchors as pressure and survival checks, not as a single deciding
judge. If fixed-anchor and random-start evidence conflict, report the conflict
and shape the stress plan around it; do not silently flip governance.

## Cost And Execution

Use the current repo assumptions unless user overrides:

```text
practical account replay follows `00_RESEARCH_HUB/EXECUTION_REPLAY_CONTRACT.md`
when output could inform real review
any capital / lot / timing / blocked-buy / replacement override is recorded
20 / 50 / 100 bps cost stress
single-name cap according to current governance
limit-up / limit-down / suspension / missing open handling logged explicitly
```

If a strategy only passes with fractional shares, same-close fills, or unlogged
replacement assumptions, label it `execution_infeasible` or `paper_shadow_candidate`.

## Failure Handling

A failed run is useful if it identifies:

```text
bad label
wrong direction
weak factor IC
cadence fragility
cost fragility
industry or single-name concentration
turnover problem
execution infeasibility
```

After repeated independent failures, stop parameter search and return to market hypothesis.
