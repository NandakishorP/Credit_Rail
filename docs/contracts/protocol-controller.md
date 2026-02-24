# ProtocolController

The `ProtocolController` is a governance wrapper around OpenZeppelin's `TimelockController`. It acts as the `policyAdmin` of `CreditPolicy` in production, enforcing a mandatory time delay on all parameter changes so that liquidity providers have a window to review and exit before any risk changes take effect.

---

## Why a Timelock

Without a timelock, the fund administrator can:
- Create a new policy version with arbitrary parameters
- Freeze it immediately
- Begin originating loans under the new rules

LPs would have no window to react. A timelock forces any governance action to be publicly visible on-chain for a fixed delay period before it executes. During that window, LPs can withdraw if they disagree with the proposed change.

---

## How It Works

The `TimelockController` lifecycle has three steps:

### 1. Schedule
The proposer submits a scheduled operation — a call to `CreditPolicy` — with a specific delay:

```solidity
timelockController.schedule(
    target,       // CreditPolicy address
    value,        // 0 ETH
    data,         // encoded function call (e.g. freezePolicy(version))
    predecessor,  // 0x0 (no dependency)
    salt,         // unique salt
    delay         // minimum delay in seconds
);
```

This emits a `CallScheduled` event on-chain. Anyone watching the contract can see what operation is pending and when it will execute.

### 2. Delay Period
The operation sits in a pending state for the full delay duration. During this window:
- The `Guardian` role can cancel the operation if it is deemed harmful
- LPs can observe the pending change and decide whether to withdraw
- No execution is possible until the delay has elapsed

### 3. Execute
After the delay, the proposer (or any executor role holder) calls:

```solidity
timelockController.execute(
    target,
    value,
    data,
    predecessor,
    salt
);
```

The underlying call to `CreditPolicy` is executed. If the operation was cancelled, execution reverts.

---

## Roles

| Role | Who Holds It | Authority |
|---|---|---|
| `PROPOSER_ROLE` | Multisig / governance | Schedule operations |
| `EXECUTOR_ROLE` | Multisig / governance | Execute operations after delay |
| `CANCELLER_ROLE` (Guardian) | Security council / multisig | Cancel any pending operation |
| `TIMELOCK_ADMIN_ROLE` | TimelockController itself | Manage role assignments |

In a minimal setup, the same multisig holds both `PROPOSER_ROLE` and `EXECUTOR_ROLE`. The `CANCELLER_ROLE` should be held by a separate smaller guardian committee for emergency use.

---

## Deployment Sequence

The correct order for a production deployment:

```
1. Deploy CreditPolicy
2. Deploy TranchePool
3. Deploy LoanEngine (references CreditPolicy + TranchePool)
4. Deploy ProtocolController (TimelockController)
5. Call CreditPolicy.transferAdmin(address(protocolController))
6. Call TranchePool.setLoanEngine(address(loanEngine))
7. Grant LoanEngine roles to appropriate operator addresses
8. Fund the TranchePool (LP deposits)
9. Create and freeze a policy version via the timelock
10. Activate the pool (set state to COMMITTED)
```

Step 5 is critical. Until ownership is transferred, the deployer retains full admin control with no timelock. This should happen before any real capital enters the system.

---

## Recommended Delay

The minimum delay before an operation can execute. For production:

| Change Type | Recommended Delay |
|---|---|
| Policy parameter update | 48 hours minimum |
| New policy version + freeze | 48 hours minimum |
| Emergency pause | Immediate (via `EMERGENCY_ADMIN_ROLE` on LoanEngine — bypasses timelock) |

The emergency pause in `LoanEngine` is intentionally outside the timelock. If the protocol needs to be stopped immediately (active exploit, critical bug), the `EMERGENCY_ADMIN_ROLE` holder can pause without waiting 48 hours.

---

## What the Timelock Does NOT Govern

The `ProtocolController` only governs `CreditPolicy`. The following are **not** gated by the timelock:

- `LoanEngine` configuration (whitelists, max fee) — controlled by `CONFIG_ADMIN_ROLE`
- Emergency pause/unpause — controlled by `EMERGENCY_ADMIN_ROLE`
- TranchePool pool state transitions — controlled by the pool admin
- LP deposits and withdrawals — open to whitelisted LPs

In a more hardened production setup, all admin functions on `LoanEngine` and `TranchePool` would also pass through the timelock. The current architecture gates the most critical parameter (the credit policy governing all new loan origination) while keeping operational controls (pausing, whitelist updates) fast-response.
