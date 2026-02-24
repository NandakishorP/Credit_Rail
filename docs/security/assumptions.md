# Assumptions

These are the explicit trust and design assumptions that the Credit Rail protocol is built on. Violating any of these assumptions does not necessarily mean the contracts have a bug — it means the protocol is being used outside its intended operating context.

---

## Protocol-Wide Assumptions

1. **Borrowers are legally identifiable off-chain.** The underwriter is responsible for KYC/KYB before issuing any attestation. The protocol does not verify identity on-chain.

2. **The underwriter is trusted.** The Schnorr signature inside the ZK circuit proves that the underwriter signed the borrower data, but it does not prove that the underwriter performed diligent KYC or that the financial data is accurate. Trust in the underwriter is a protocol assumption, not a cryptographic guarantee.

3. **Borrowers have signed a legal credit agreement off-chain.** The smart contracts enforce accounting incentives; they do not enforce legal obligations. Repayment is expected to be driven by legal and reputational pressure, not by on-chain mechanics.

4. **Smart contracts cannot seize assets or force repayments.** This is an intentional, non-collateralised credit system. There is no liquidation mechanism. Default is declared manually by the servicer.

5. **Defaults are expected outcomes, not bugs.** The loss waterfall exists precisely because defaults are anticipated. A defaulted loan does not indicate a smart contract failure.

6. **Liquidity providers accept loss risk according to their tranche position.** Senior LPs accept lower yield in exchange for loss protection. Equity LPs accept higher risk in exchange for residual upside. This risk allocation is transparent at the time of deposit and does not change retroactively.

7. **Governance is trusted for emergency action but cannot arbitrarily seize funds.** The `EMERGENCY_ADMIN_ROLE` can pause the protocol. It cannot redirect funds, modify loan terms, or drain the pool.

8. **ZK proofs verify eligibility and authorisation, not economic correctness.** The circuit proves that the borrower met the policy criteria at the time of underwriting. It does not guarantee future repayment, business performance, or that the borrower's financial statements are audited.

9. **The protocol only enforces accounting, incentives, and loss allocation.** All legal enforcement, debt collection, and asset seizure are the responsibility of off-chain legal agreements between the fund, borrowers, and LPs.

10. **Loan terms are immutable once issued.** The APR, principal, origination fee, and term are recorded at origination and cannot be modified by any party, including governance.

11. **No grace periods or partial repayments below accrued interest.** Repayments must satisfy accrued interest before reducing principal. There is no on-chain mechanism for renegotiating payment schedules.

12. **No loan refinancing.** A loan cannot be restructured or extended on-chain. If a borrower needs different terms, the existing loan must be repaid and a new loan originated.

13. **The underwriter's Schnorr signature is non-repudiable.** Once a signature is incorporated into a valid ZK proof submitted on-chain, the underwriter cannot deny having signed the underlying borrower data.

---

## CreditPolicy Design Assumptions

### 1. Data Trust Model

The `CreditPolicy` contract does not validate, sanity-check, or verify the correctness of any parameters supplied to it. All data written to the contract is assumed to be correct by construction.

Responsibility for correctness lies entirely with the `policyAdmin` (and, in production, the `ProtocolController` timelock that governs it). This is an explicit architectural decision: the contract is a registry, not a validator.

### 2. Policy Lifecycle Semantics

- **Active:** The policy is mutable. It is being configured.
- **Frozen:** The policy is permanently immutable. It is the canonical definition used by loan origination.
- **Inactive:** The policy is deprecated. No new loans can reference it.

Allowed transitions: `Active → Frozen → Inactive` or `Active → Inactive`. Once frozen, a policy can never be modified. Once inactive, it can never be reactivated.

### 3. Usage Guarantees

External contracts (specifically `LoanEngine`) are expected to reference only **frozen** policies. The `CreditPolicy` contract enforces immutability of frozen policies but does not prevent an external contract from attempting to reference an active or inactive policy version. It is `LoanEngine`'s responsibility to validate the policy state at origination time.

### 4. Versioning Model

Policy versions are arbitrary identifiers. They do not imply ordering, chronological release, or semantic versioning. The meaning of version numbers is the sole responsibility of governance and off-chain coordination. Version `5` is not necessarily newer or stricter than version `3`.
