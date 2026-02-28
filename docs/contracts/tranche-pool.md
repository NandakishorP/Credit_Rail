# TranchePool

The `TranchePool` is the capital vault of the Credit Rail protocol. It manages liquidity provider deposits, tracks capital across three risk tranches, and enforces the interest, loss, and recovery waterfalls mechanically — without administrator discretion.

The contract is deployed behind an `ERC1967Proxy` using the UUPS (Universal Upgradeable Proxy Standard) pattern. Access control is managed via `AccessControlUpgradeable` with granular roles:

| Role | Purpose |
|---|---|
| `DEFAULT_ADMIN_ROLE` | Manages role assignments, authorizes upgrades |
| `POOL_ADMIN_ROLE` | Pool state transitions, loan engine wiring |
| `CONFIG_ADMIN_ROLE` | Allocation factors, APR targets, tranche caps |
| `WHITELIST_ADMIN_ROLE` | LP whitelist management |
| `EMERGENCY_ADMIN_ROLE` | Pause/unpause |
| `TREASURY_ROLE` | Sweep protocol revenue |

In production, `DEFAULT_ADMIN_ROLE` is held by the `ProtocolController` (timelock + multisig).

---

## Tranche Structure

Capital is split across three tranches, each modelled as a `TrancheState` struct:

```solidity
struct TrancheState {
    uint256 idle;       // Capital waiting to be deployed
    uint256 deployed;   // Capital currently backing active loans
    uint256 aprBps;     // Target yield for this tranche (basis points)
}
```

| Tranche | Index | Risk Level | Priority |
|---|---|---|---|
| Senior | 0 | Lowest | First paid, last to absorb losses |
| Junior | 1 | Medium | Second paid, middle loss buffer |
| Equity | 2 | Highest | Residual yield, first-loss absorber |

---

## LP Share Model

When a liquidity provider deposits USDC, the pool mints shares at a **1:1 ratio** to the deposit amount. Shares track ownership within a specific tranche — they are not transferable between tranches.

```
shares_minted = deposit_amount  // always 1:1 at deposit time
```

Interest is distributed using a **global interest index** per tranche. Rather than iterating over all LPs on every payment, the pool maintains a running `interestIndex` value. Each LP's claimable interest is computed on-demand from the delta between the current index and the index at their last claim.

```
claimable = userShares × (currentIndex - userLastIndex) / INDEX_PRECISION
```

`INDEX_PRECISION` is `1e18`. This pattern scales to any number of LPs with O(1) computation per user.

---

## Pool State Machine

The pool transitions through four states, strictly one-directional:

```
OPEN → COMMITTED → DEPLOYED → CLOSED
```

| State | Deposits | Withdrawals | Loan Activation |
|---|---|---|---|
| `OPEN` | ✅ | ✅ | ❌ |
| `COMMITTED` | ❌ | ❌ | ✅ |
| `DEPLOYED` | ❌ | ❌ | ✅ |
| `CLOSED` | ❌ | ✅ | ❌ |

The pool moves to `COMMITTED` when the fund admin decides capital is ready to deploy. From that point forward, deposits and withdrawals are locked until the pool reaches `CLOSED`.

---

## Capital Allocation Algorithm

When a loan is activated, `allocateCapital(principal)` splits the principal across tranches using fixed allocation ratios:

| Tranche | Default Ratio |
|---|---|
| Senior | 80% |
| Junior | 15% |
| Equity | 5% |

**Overflow handling:** If a tranche does not have enough idle capital to cover its share, the shortfall cascades upward to Senior. Senior is the final absorber — if Senior also lacks funds, the call reverts with `InsufficientPoolLiquidity`.

For each tranche, `idle` decreases and `deployed` increases by the amount allocated. The global `totalDeployedValue` increases by `principal`.

---

## Interest Waterfall

Interest payments are routed through the pool via `onRepayment(principalPaid, interestPaid)` called by `LoanEngine`.

Each tranche has:
- **Target interest:** what the tranche is theoretically owed based on its APR and deployed capital
- **Accrued interest:** what has actually been paid into it

When interest arrives:
1. Senior receives interest until its accumulated target is fully met
2. Junior receives interest until its accumulated target is fully met
3. Equity receives all remaining residual

If the interest payment is insufficient to meet Senior's target, Senior gets everything available and Junior and Equity receive nothing. This strict priority order is what makes the Senior tranche lower risk.

The `interestIndex` for each tranche is updated via `InterestMath.computeIndexDelta`:

```
indexDelta = interestPaid × INDEX_PRECISION / totalShares
newIndex = oldIndex + indexDelta
```

---

## Loss Waterfall

When `LoanEngine` calls `onLoss(principalLoss, ghostInterest)` after a write-off:

**Step 1 — Ghost interest cancellation:**
Interest that was theoretically accrued on the now-defaulted loan is cancelled. This "ghost interest" is removed from Senior's target first, then Junior's if Senior's allocation is exhausted.

**Step 2 — Principal loss absorption:**
Principal loss is absorbed starting from the riskiest tranche:
1. Equity `deployed` is reduced first
2. Any remainder reduces Junior `deployed`
3. Any remainder reduces Senior `deployed`

If a tranche's `deployed` goes to zero but loss remains, a `principalShortfall` is recorded for that tranche. This shortfall is tracked for recovery targeting.

---

## Recovery Waterfall

When `LoanEngine` calls `onRecovery(amount)` after a post-default recovery:

Recovery funds are applied in seniority order (Senior first, riskiest last):
1. Senior `principalShortfall` is filled first
2. Junior `principalShortfall` is filled next
3. Equity `principalShortfall` is filled next
4. Any remaining funds beyond total shortfall flow to Equity as **upside** — Equity earns the excess because it bore the first-loss risk

Recovery funds increase the pool's `totalIdleValue` as capital is returned.

---

## Protocol Revenue

When interest payments arrive but the Equity tranche has zero shares outstanding (no LPs), the Equity residual has no one to attribute it to. Instead of being locked in the contract, it flows into the `protocolRevenue` bucket.

```solidity
uint256 public s_protocolRevenue;
```

A holder of the `TREASURY_ROLE` can sweep this to a treasury address via `sweepProtocolRevenue(address treasury)`. This ensures no yield is permanently stranded in the contract.

---

## Key Invariants

The pool is designed to maintain these conservation laws at all times:

```
TotalIdle + TotalDeployed = TotalDeposited - TotalLoss + TotalRecovered
TokenBalance = TotalIdle + TotalUnclaimedInterest + ProtocolRevenue
TotalDeployed = SeniorDeployed + JuniorDeployed + EquityDeployed
```

See [`security/invariants.md`](../security/invariants.md) for formal proofs and Solidity implementations.
