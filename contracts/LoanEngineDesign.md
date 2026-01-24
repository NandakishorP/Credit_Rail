# 🏦 Loan Engine — System Specification

> **Canonical source of truth for institutional private credit obligations**

---

## 📋 Overview

The **Loan Engine** is the canonical source of truth for all loan obligations within the private credit system. It is responsible for managing loan lifecycles, interest accrual, cashflow accounting, and enforcement of credit policy constraints, including zero-knowledge underwriting verification.

> 💡 **Note:** The Loan Engine does not handle liquidity pooling or investor accounting. Those responsibilities are delegated to the `TranchePool`.

---

## 🎯 Responsibilities

The Loan Engine is responsible for:

1. **Loan lifecycle state management**
2. **Time-based interest accrual**
3. **Cashflow accounting** (repayments and losses)
4. **Enforcement of credit policy and ZK underwriting constraints**

---

## 👥 Actors

### 1. 🔑 Fund Manager (Admin / Multisig)
- Originates loans
- Deploys capital
- Declares defaults and write-offs

### 2. 🛡️ ZK Verifier
- Verifies underwriting proofs against the active credit policy

### 3. 💰 TranchePool
- Receives repayments
- Applies loss waterfall accounting

> 💡 **Note:** Borrowers do not interact directly with the Loan Engine.

---

## 🔄 Loan States

A loan progresses through the following states:

| State | Description |
|-------|-------------|
| `NONE` | Initial state (not yet created) |
| `CREATED` | Loan approved, awaiting capital deployment |
| `ACTIVE` | Capital deployed, interest accruing |
| `REPAID` | Fully repaid |
| `DEFAULTED` | Declared in default |
| `WRITTEN_OFF` | Terminal state, accounting closed |

---

## ⚡ State Transitions

```
NONE → CREATED → ACTIVE
         ↓
      REPAID

ACTIVE → DEFAULTED → WRITTEN_OFF
```

### Transition Rules

- ✅ Transitions are strictly enforced
- ❌ No reverse or skipped transitions are allowed
- 🔒 `WRITTEN_OFF` is terminal

---

## 📊 Loan Data Model

```solidity
struct Loan {
    // Identity
    uint256 loanId;
    bytes32 borrowerCommitment;
    uint256 policyVersion;
    uint8 tierId;

    // Economics
    uint256 principalIssued;
    uint256 principalOutstanding;
    uint256 aprBps;
    uint256 originationFeeBps;

    // Interest accounting
    uint256 interestAccrued;
    uint256 interestPaid;
    uint256 lastAccrualTimestamp;

    // Timing
    uint256 startTimestamp;
    uint256 maturityTimestamp;

    // State
    LoanState state;
}
```

### 🔐 Invariants

- `principalOutstanding ≤ principalIssued` must always hold
- A loan's `policyVersion` is **immutable** after creation

---

## 📜 Credit Policy Binding

Each loan is **permanently bound** to the policy version used at origination.

- Policy updates do **not** retroactively affect existing loans
- This ensures legal, accounting, and risk-model consistency

---

## 🔍 ZK-Based Loan Origination

Underwriting occurs **off-chain**. A zero-knowledge proof is generated attesting that:

- ✓ Borrower satisfies eligibility criteria
- ✓ Financial ratios meet policy thresholds
- ✓ Loan parameters fall within the selected tier
- ✓ Borrower is not part of an excluded category

**Upon successful verification:**

1. Loan is created
2. State transitions to `CREATED`
3. **No capital is deployed at this stage**

---

## 💸 Capital Deployment

To activate a loan:

1. Verify loan state is `CREATED`
2. Call `TranchePool.allocateCapital()`
3. Record issued principal
4. Initialize interest accrual variables
5. Transition loan state to `ACTIVE`
6. Funds are off-ramped to the borrower/SPV entity

---

## 📈 Interest Accrual Model

Interest accrues **continuously** based on time and outstanding principal.

```solidity
accruedInterest += principalOutstanding × aprBps × timeElapsed / (365 days × 10_000)
```

### Accrual Characteristics

- **Lazy:** Accrual is calculated on-demand
- **Deterministic:** No reliance on external oracles
- **Event-driven:** Interest is accrued on any state-changing interaction
- **No scheduled jobs or keepers required**

---

## 💳 Repayment Model

Repayments occur **off-chain** and are recorded on-chain.

### On repayment:

1. Accrue interest up to the repayment timestamp
2. Apply payment to accrued interest
3. Apply remaining amount to outstanding principal
4. Forward repayment to the `TranchePool` via `onRepayment()`

### Loan Closure

When:
- `principalOutstanding == 0`
- `interestAccrued == 0`

The loan transitions to `REPAID`.

---

## ⚠️ Default Handling

> **⚠️ WARNING:** Defaults are not algorithmic.

When a default occurs:

1. Admin/multisig **declares default** on-chain
2. Interest is accrued up to the default timestamp
3. Loss amount is determined
4. `TranchePool.onLoss()` is called
5. Loan transitions to `DEFAULTED`

---

## 📝 Write-Off

A defaulted loan may later be **written off**.

- Loan transitions from `DEFAULTED` → `WRITTEN_OFF`
- Accrual permanently stops
- Obligation is closed from an accounting perspective

---

## 🎨 Design Philosophy

> **The Loan Engine models legal credit obligations, not DeFi liquidation mechanics.**

### Key Principles

- **Discretionary risk management:** Risk decisions are governance-controlled
- **Privacy-preserving:** Zero-knowledge is used to enforce constraints without leaking borrower data
- **Accounting-first:** Correctness and auditability take precedence over automation
- **Modular architecture:** Clear separation between capital allocation, loan accounting, and investor exposure

---

## ✨ Summary

The Loan Engine provides a **deterministic, auditable, and policy-constrained** foundation for institutional private credit. It separates capital allocation, loan accounting, and investor exposure into clearly defined modules while supporting confidential underwriting and discretionary default management.

---


