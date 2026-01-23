## Assumptions

1. Borrower is legally identifiable off chain via the kyc performed by the underwriter
2. Underwriter is trusted
3. Borrower has signed a legal contract for credit.
4. Smart contracts cannot enforce repayments or seize assets.
5. Legal enforcment is handled on-chain.
6. Defaults are expected outcome, not bugs.
7. Liquidity providers accepts loss risk according to their tranche position.
8. Governance is trusted for emergency action but cannot aribtarly engage in seizing funds.
9. ZK Proof verifies eligibility and authorization not economic correctness.
10. The protocol only enforces accounting, incentives and loss allocation.
11. Loan terms are immutable once issued.
12. No extention of grace period and partial repayments are allowed.
13. Underwriting signature is non repuidable.
14. No Loan refinancig.


*** CREDIT POLICY DEFINITION DESIGN ASSUMPTIONS ***

1. Data Trust Model
The CreditPolicy contract does not validate, sanity-check, or verify the correctness of any numerical or semantic data supplied to it.
All data written to the contract is assumed to be correct by construction.

Responsibility for data correctness, verification, and attestation lies entirely with governance and the data-feeding mechanism (e.g. off-chain underwriting, attestations, oracles, or ZK proofs).
This is an explicit architectural decision, not a tradeoff.

⸻

2. Policy Lifecycle Semantics
A policy version may exist in one of three logical states:
	•	Active:
The policy is mutable and intended to be configured or updated by governance.
	•	Frozen:
The policy is immutable and represents a finalized, canonical definition.
Only frozen policies are intended to be referenced by external contracts.
	•	Inactive:
The policy is deprecated and must not be referenced by any contract.

A policy may transition:
	•	Active → Frozen → Inactive
	•	Active → Inactive

Once a policy is frozen, it can never be modified again.
Once a policy is inactive, it can never be reactivated.

⸻

3. Usage Guarantees
External contracts are expected to:
	•	Reference only frozen policies
	•	Never reference active or inactive policies

The CreditPolicy contract enforces immutability but does not enforce usage correctness across external consumers.

⸻

4. Versioning Model
Policy versions are arbitrary identifiers and do not imply ordering, sequencing, or chronological releases.

Semantic meaning, ordering, or categorization of policy versions is the sole responsibility of governance and off-chain coordination mechanisms.
