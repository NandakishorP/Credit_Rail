# Economic Modeling & Capital Waterfall

Credit Rail employs an institutional structured-finance waterfall model. Instead of peer-to-peer matching, capital is pooled into three risk-tiered tranches: **Senior**, **Junior**, and **Equity**. 

This document breaks down the mathematical flow of funds from LP deposit, through the capital allocation (origination), interest distribution, loss absorption, and recovery phases. All formulas are rigorously tested off-chain within the Python engine (`economic-modelling/`).

---

## 1. Capital Origination (Allocation)

When an authorized Servicer calls `activateLoan` on the `LoanEngine`, the smart contracts draw `X` principal from the `TranchePool`.

By default, the protocol is configured to draw matching ratios. `S`% from Senior, `J`% from Junior, and `(100 - S - J)`% from Equity. The ratios are configurable.

```text
Let TotalDisbursement D = Principal
Let Configured Allocations S% = 80%, J% = 15%, E% = 5%

If all tranches have sufficient idle capital:
SeniorContribution = D * S
JuniorContribution = D * J
EquityContribution = D * E
```

### The "Bottom-Up Override"
In an automated vault, a strict ratio draw could fail a loan if the `Senior` tranche hits high utilization but `Junior` and `Equity` sit dormant. Therefore, the system incorporates **Bottom-Up Capacity Absorption**.

If `SeniorContribution` exceeds `Senior Idle Capital` (liquidity shortage), the missing capacity drops back into the remaining allocation flow:

1. `EquityCapacityRemaining`: Equity absorbs up to its `Idle Capital` limit.
2. `JuniorCapacityRemaining`: Junior absorbs the overflow of the equity layer up to its `Idle Capital`.
3. If, after all available `Idle Capital` is pooled, the required `D` isn't met: *The transaction completely reverts with InsufficientLiquidity*.

---

## 2. Interest Accrual and Payment Waterfall

Interest is calculated linearly (`SIMPLE` not compounding) on a continuous basis per-second to mirror off-chain time horizons efficiently. The base constant is `1e18` representing a 100% factor over `365 Days`.

Each `TrancheState` tracks a variable `targetInterest`. Equity **does not** have a target APR. It serves as the residual claimant.

```solidity
uint256 accrueTime = currentTime - lastAccrualTime;
SeniorTargetIncrease = (SeniorDeployed * SeniorAPR * accrueTime) / (365 days * 10000);
JuniorTargetIncrease = (JuniorDeployed * JuniorAPR * accrueTime) / (365 days * 10000);
```

When a repayment batch contains interest (`onRepayment(principal, interest)`), it trickles strictly down the Capital Stack.

### The Flow:
1. **Senior Distribution:** `TranchePool` allocates up to `SeniorTargetInterest` if the repayment amount covers it.
2. **Junior Distribution:** Remaining interest flows down, fulfilling the `JuniorTargetInterest`.
3. **Equity Upside:** Anything left over spills into the `Equity` index.

*Edge Case Handling:* If Equity LP pool has zero depositors and is earning residual interest, it acts globally and spills over into `Junior`. If `Junior` also has zero deposits, it's flagged as `Protocol Revenue` to prevent permanently locking value.

---

## 3. Loss Absorption & Principal Waterfall

Private credit fundamentally relies on robust loss mitigations (e.g., defaulted SME loans, unpaid invoices). The risk system protects Senior LPs at all costs, acting in a **Reverse Waterfall**. 

When a loan enters the `DEFAULTED` or unrecoverable `WRITTEN_OFF` sequence, a strict loss is recorded:

```text
Let Loss L = PrincipalWrittenOff

If L > 0:
  If Equity_Deployed > 0:
     Absorb L from Equity_Deployed. Update Shortfalls.
  If L > Equity_Deployed:
     Absorb remaining L from Junior_Deployed.
  If L > (Equity_Deployed + Junior_Deployed):
     Absorb remaining L from Senior_Deployed.
```

The protocol implements "ghost interest" cancellation alongside this. If a loan defaults after accruing `Y` unpaid interest, that simulated ghost value is subtracted from the tranche targets (Senior first) to correct the global ledger.

---

## 4. Default Recovery

If off-chain collection mechanisms partially recover the defaulted capital (through liquidation of underlying assets or corporate recovery actions), the recovery is injected directly back into the `TranchePool`. 

This follows a **Top-Down Restoration** to make LPs whole again:

1. **Senior Shortfall:** If Senior was impacted by severe losses, the recovered value fully replaces their `PrincipalShortfall`, returning it to `Idle Capital`.
2. **Junior Shortfall:** Flow reaches Junior to heal the remaining deficit.
3. **Equity Shortfall:** The risk-tolerant capital gets its initial investment back.
4. **Equity Upside (Excess):** Any extraordinary recovery yielding more than the initial loss drops entirely into `Equity Idle Capital` as a reward.

---

## LP Global Share Index Pattern
Rather than iterating over thousands of arrays per transaction, the `TranchePool` relies on a `userIndex` paradigm for LP withdrawals of interest, similar to Staking Yield algorithms. This maintains an explicit `O(1)` gas cost regardless of the number of users interacting with the protocol.
