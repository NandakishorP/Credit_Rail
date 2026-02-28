# LoanEngine

The `LoanEngine` is the canonical source of truth for all loan obligations within the Credit Rail protocol. It manages loan lifecycle state, lazy interest accrual, repayment accounting, and ZK proof verification. It does not handle LP accounting — that is delegated entirely to `TranchePool`.

The contract is deployed behind an `ERC1967Proxy` using the UUPS (Universal Upgradeable Proxy Standard) pattern. Access control is managed via `AccessControlUpgradeable` with six granular roles (see [Role Architecture](#role-architecture) below).

---

## Responsibilities

1. **Loan lifecycle state management** — enforcing strict, one-directional state transitions
2. **ZK proof verification** — verifying Noir UltraHonk proofs against the `HonkVerifier` contract
3. **Interest accrual** — lazy computation on any state-changing event
4. **Repayment and loss accounting** — forwarding correct amounts to `TranchePool`
5. **Access control** — role-based and whitelist-based permission enforcement

---

## Loan State Machine

```
NONE → CREATED → ACTIVE → REPAID
                   ↓
               DEFAULTED → WRITTEN_OFF
```

| State | Description |
|---|---|
| `NONE` | Loan does not yet exist |
| `CREATED` | ZK proof verified, loan recorded, capital not yet deployed |
| `ACTIVE` | Capital deployed to borrower, interest accruing |
| `REPAID` | Principal and interest fully settled |
| `DEFAULTED` | Declared in default by servicer; interest frozen |
| `WRITTEN_OFF` | Terminal. Accounting closed, loss forwarded to TranchePool |

All transitions are strictly enforced. No reversal. No skipping. `WRITTEN_OFF` is terminal.

---

## Loan Data Model

```solidity
struct Loan {
    LoanState state;
    bytes32 borrowerCommitment;     // Hash binding private borrower data
    uint256 policyVersion;          // Frozen policy version used at origination
    uint8 tierId;                   // Pricing tier within the policy
    uint256 principalIssued;        // Original principal amount
    uint256 principalOutstanding;   // Remaining principal
    uint256 aprBps;                 // Annual interest rate in basis points
    uint256 originationFeeBps;      // One-time fee in basis points
    uint256 termDays;               // Loan term in days
    uint256 interestAccrued;        // Cumulative interest not yet paid
    uint256 interestPaid;           // Total interest paid to date
    uint256 lastAccrualTimestamp;   // Timestamp of last interest accrual
    uint256 startTimestamp;         // When the loan was activated
    bytes32 nullifierHash;          // Anti-replay hash
    bytes32 underwriterKeyX;        // Underwriter Grumpkin public key X
    bytes32 underwriterKeyY;        // Underwriter Grumpkin public key Y
}
```

**Key invariants on the struct:**
- `principalOutstanding ≤ principalIssued` — always
- `policyVersion` is immutable after `CREATED`
- `nullifierHash` is unique globally (enforced on-chain)

---

## Interest Accrual Model

Interest is **lazy** — it is not accrued on a schedule but computed on-demand whenever a state-changing function is called.

```
accruedInterest += principalOutstanding × aprBps × timeElapsed
                   ──────────────────────────────────────────────
                              365 days × 10,000
```

**Characteristics:**
- No keepers or external triggers required
- Deterministic — same inputs always produce the same result
- Event-driven — accrual fires on `repayLoan()`, `declareDefault()`, and `writeOffLoan()`
- Accrual stops permanently when a loan enters `DEFAULTED` or `WRITTEN_OFF`

---

## ZK Proof Verification

`createLoan()` performs three independent on-chain checks before accepting a loan:

1. **Policy hash check** — `CreditPolicy.policyScopeHash(policyVersion)` must match the proof's `policy_version_hash` public input
2. **Loan hash check** — `Poseidon2.hash(params)` recomputed on-chain must match the proof's `loan_hash` public input
3. **Proof verification** — `HonkVerifier.verify(proofData, publicInputs)` must return `true`

If any check fails, the transaction reverts. The nullifier is then stored to prevent replay:

```solidity
s_nullifierHashes[nullifierHash] = true;
```

---

## Role Architecture

`LoanEngine` uses OpenZeppelin `AccessControlUpgradeable` with five operational roles (plus `DEFAULT_ADMIN_ROLE` for upgrade authorization and role management):

| Role | Who Holds It | What They Can Do |
|---|---|---|
| `UNDERWRITER_ROLE` | Fund admin | `createLoan()` — submit ZK proof to originate a loan |
| `SERVICER_ROLE` | Servicer | `activateLoan()`, `repayLoan()`, `declareDefault()` |
| `RISK_ADMIN_ROLE` | Risk team | `writeOffLoan()`, `declareDefault()` |
| `CONFIG_ADMIN_ROLE` | Governance / multisig | Manage whitelists, update `maxOriginationFeeBps`, set underwriter authorizations |
| `EMERGENCY_ADMIN_ROLE` | Multisig | `pause()`, `unpause()` |

> Note: `UNDERWRITER_ROLE` in the contract refers to the **fund admin** who submits the on-chain transaction. The off-chain underwriter is a separate entity whose authority is captured by the Schnorr signature verified inside the ZK circuit.

---

## Whitelist Architecture

Four independent whitelists gate operational interactions:

| Whitelist | Checked In | Purpose |
|---|---|---|
| `whitelistedOffRampingEntities` | `activateLoan()` | Who can receive principal disbursals |
| `whitelistedRepaymentAgents` | `repayLoan()` | Who can be the source of repayment funds |
| `whitelistedRecoveryAgents` | `recoverLoan()` | Who can submit post-default recovery amounts |
| `whitelistedFeeManagers` | `activateLoan()` | Who handles origination fee routing |

Any call with a non-whitelisted address reverts immediately. Whitelists are managed by `CONFIG_ADMIN_ROLE`.

---

## Repayment Model

On `repayLoan(loanId, amount, repaymentAgent, feeManager)`:

1. Accrue interest up to `block.timestamp`
2. Split `amount` into `interestPortion` and `principalPortion`
3. Pull funds via `IERC20.safeTransferFrom(repaymentAgent, ...)`
4. Forward to `TranchePool.onRepayment(principalPortion, interestPortion)`
5. If `principalOutstanding == 0`, transition to `REPAID`

Excess payments above total outstanding (principal + accrued interest) are not accepted. Repayments must be exact or less than the total due.

---

## Default and Write-Off

`declareDefault(loanId)` (callable by `SERVICER_ROLE` or `RISK_ADMIN_ROLE`):
1. Accrues interest up to the default timestamp
2. Transitions state to `DEFAULTED`
3. Interest accrual stops permanently

`writeOffLoan(loanId, principalLoss, ghostInterestLoss)` (callable by `RISK_ADMIN_ROLE`):
1. Transitions state to `WRITTEN_OFF`
2. Calls `TranchePool.onLoss(principalLoss, ghostInterestLoss)`
3. Loss is absorbed by tranches in reverse seniority (Equity → Junior → Senior)

---

## Design Philosophy

> The Loan Engine models legal credit obligations, not DeFi liquidation mechanics.

- **Discretionary risk management** — defaults are declared by humans, not triggered algorithmically by price feeds
- **Privacy-preserving** — ZK proofs enforce credit policy compliance without on-chain exposure of borrower financials
- **Accounting-first** — correctness and auditability take precedence over automation
- **Modular** — loan accounting is fully separated from capital allocation (`TranchePool`) and from credit parameterisation (`CreditPolicy`)

---

See [`architecture.md`](../architecture.md) for the full call graph and [`contracts/tranche-pool.md`](./tranche-pool.md) for waterfall details.
