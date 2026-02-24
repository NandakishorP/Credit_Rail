# ProtocolController

The `ProtocolController` is a governance wrapper around OpenZeppelin's `TimelockController`. It acts as the ultimate administrator across the **entire Credit Rail protocol**. It governs not only the `CreditPolicy`, but also the `LoanEngine` (via `DEFAULT_ADMIN_ROLE`) and the `TranchePool` (via `Ownable`).

It enforces a mandatory time delay on all critical protocol changes (like policy updates, whitelist modifications, and role grants) so that liquidity providers have a window to review and exit before any changes take effect.

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
    target, // Could be CreditPolicy, LoanEngine, or TranchePool
    value,
    data,
    predecessor,
    salt
);
```

The underlying call is executed. If the operation was cancelled, execution reverts.

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
5. Transfer admin rights to ProtocolController:
   - CreditPolicy.transferAdmin(address(protocolController))
   - TranchePool.transferOwnership(address(protocolController))
   - LoanEngine.grantRole(DEFAULT_ADMIN_ROLE, address(protocolController))
   - LoanEngine.revokeRole(DEFAULT_ADMIN_ROLE, deployer)
6. Call TranchePool.setLoanEngine(address(loanEngine)) (via Timelock if transferred first)
7. Grant operational roles (UNDERWRITER, SERVICER) via Timelock to operators
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

## What the Timelock Governs

In a full production setup, the `ProtocolController` governs:
1. **CreditPolicy**: All policy creation and freezing (`policyAdmin`)
2. **LoanEngine**: All configuration and role assignments (`DEFAULT_ADMIN_ROLE`, `CONFIG_ADMIN_ROLE`)
3. **TranchePool**: All pool-level configuration and state transitions (`owner`)

Operational roles (creating loans, activating them, or processing repayments) are generally assigned to dedicated bots or servicers without a timelock to ensure fast execution, but the ProtocolController retains ultimate authority to revoke those roles if a servicer misbehaves.
