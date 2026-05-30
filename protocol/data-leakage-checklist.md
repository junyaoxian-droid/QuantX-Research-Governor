# Data Leakage Checklist

Use this before trusting a backtest or model result.

## Time Alignment

- Was the signal computed using only information available at signal time?
- Is the trade price after the signal timestamp?
- Are close-based features traded at next open or later?
- Are future returns shifted correctly?

## Point-in-Time Data

- Are financial reports aligned to publication date, not report period?
- Are index constituents point-in-time?
- Is universe construction point-in-time?
- Are delisted names included if relevant?

## Execution Realism

- Are suspended stocks handled?
- Are limit-up buys and limit-down sells handled?
- Are board lots handled?
- Are costs and slippage included?
- Are high-price names feasible for the account size?

## Research Process

- Did Validation select parameters before Test?
- Was Test opened only once?
- Are OOS-only winners labeled?
- Are failed attempts logged?
- Are manual decisions excluded from historical training features?
