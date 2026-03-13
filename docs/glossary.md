# Glossary

Terms used throughout the Credit Rail codebase and documentation.

---

### Accrued Interest
The cumulative interest that has been earned by a loan but not yet paid by the borrower. Stored per loan in `LoanEngine.interestAccrued`. Increases continuously with time; decreases when a repayment is applied.

---

### APR (Annual Percentage Rate)
The annualised interest rate on a loan. Expressed in **basis points** in all contract storage. 1200 bps = 12% APR.

---

### Attestation
A cryptographic statement made by an underwriter about a borrower's financial data. In Credit Rail, the attestation is a Schnorr signature over the borrower's financial facts, produced using the underwriter's Grumpkin private key. The attestation has a maximum age (`maxAttestationAgeDays`) after which it expires and cannot be used to originate a loan.

---

### Basis Point (bps)
One hundredth of one percentage point. 100 bps = 1%. Used to express APR, origination fees, and policy ratio constraints. The protocol uses `BPS_DENOMINATOR = 10,000`.

---

### Borrower Commitment
A Poseidon2 hash that binds the borrower's private financial data to the ZK proof without revealing it on-chain.

```
borrowerCommitment = Poseidon2(secret, revenue, EBITDA, netWorth, ageDays)
```

The commitment is a public input to the circuit and is stored on-chain as part of the loan record. It can be used later to verify that a specific borrower was the one linked to a given loan, without revealing the underlying data.

---

### Deployed Value
Capital that has been sent to active loans and is currently outstanding. Tracked per tranche (`TrancheState.deployed`) and globally (`totalDeployedValue`). Deployed capital is not held in the `TranchePool` contract — it has been transferred to the borrower's off-ramping entity.

---

### Equity (Tranche)
The highest-risk, highest-return tranche. Equity LPs earn residual interest after Senior and Junior targets are met. In a loss event, Equity absorbs losses first. In a recovery event, Equity benefits from any upside beyond full shortfall restoration.

---

### Ghost Interest
Interest that was theoretically accruing on a loan that subsequently defaulted. When a loan is written off, this ghost interest — interest the pool "expected" to receive but will not — is cancelled from the Senior and Junior target interest buckets. Cancelling ghost interest prevents the pool from indefinitely expecting interest from a loan that no longer exists.

---

### Grumpkin Curve
The BN254 embedded curve. Its scalar field matches the BN254 base field used by the Noir proving backend (Barretenberg). This makes scalar multiplications on Grumpkin native field operations inside a Noir circuit — approximately 10x fewer constraints than performing the equivalent secp256k1 operations (which require non-native arithmetic). Credit Rail uses Grumpkin for the underwriter's Schnorr signature scheme.

---

### Idle Value
Capital held in the `TranchePool` that is not currently backing any active loan. Available for new loan activation. Tracked per tranche (`TrancheState.idle`) and globally (`totalIdleValue`). Idle capital is physically present in the pool contract as ERC20 token balance.

---

### Interest Index
A global per-tranche accumulator used to distribute interest to LPs in O(1) time. When interest is paid to a tranche, the index is incremented by `interestPaid × INDEX_PRECISION / totalShares`. An LP's claimable interest is `userShares × (currentIndex - userLastClaimedIndex) / INDEX_PRECISION`. This pattern allows any number of LPs without iterating over them on every payment.

---

### Junior (Tranche)
The middle-risk tranche. Junior LPs receive interest after Senior and before Equity. In a loss event, Junior absorbs losses after Equity is exhausted and before Senior is touched.

---

### Loan Hash
A Poseidon2 hash that binds the loan terms and borrower identity to a specific on-chain loan record.

```
loanHash = Poseidon2(borrowerCommitment, underwriterKeyX, underwriterKeyY,
                     tierId, principal, aprBps, feeBps, termDays,
                     industryHash, timestamp, loanId)
```

The `loanHash` is a public input to the ZK circuit and is recomputed on-chain during `createLoan()` to verify the proof references the exact loan being submitted.

---

### Nullifier
A one-time hash used to prevent a ZK proof from being submitted more than once. Once used, the nullifier is permanently recorded on-chain.

```
nullifierHash = Poseidon2(loanId, borrowerSecret, loanPrincipal, attestationTimestamp)
```

If the same proof were submitted a second time, the nullifier check in `LoanEngine` would revert the transaction.

---

### Policy Scope Hash (`policyScopeHash`)
A Poseidon2 hash of all 21 frozen policy parameters, computed automatically on-chain during `freezePolicy()` for each tier. Every ZK proof must embed this hash as a public input, binding the proof permanently to a specific policy version and tier. Once the policy is frozen, the hash (and all underlying parameters) become permanently immutable.

---

### Poseidon2
A ZK-friendly hash function operating over the BN254 scalar field. Used in Credit Rail for: the borrower commitment, the nullifier hash, the loan hash, and the policy scope hash. Unlike keccak256 (which is expensive in ZK circuits), Poseidon2 is designed to minimise constraint count when used inside a ZK circuit. The same implementation is used both in the Noir circuit and on-chain (`poseidon2-evm` library), ensuring the hashes match between off-chain proof generation and on-chain verification.

---

### Principal Shortfall
The amount by which a tranche's `deployed` capital fell short due to a loss event. Tracked per tranche. During recovery, shortfalls are filled in order of seniority (Senior first). A tranche with a non-zero shortfall has not yet been fully made whole from its loss exposure.

---

### Protocol Revenue
A pool-level accumulator that captures interest that flows to the Equity tranche when Equity has zero LP shares outstanding. Rather than being stranded in the contract, this residual interest is collected in `protocolRevenue` and can be swept to a treasury address via `sweepProtocolRevenue()`.

---

### Schnorr Signature
The digital signature scheme used by underwriters in Credit Rail. A Schnorr signature over the Grumpkin curve produces a compact `(s, e)` pair where `s` is a 256-bit scalar and `e` is a field element challenge. The circuit verifies the signature using the underwriter's public key without revealing the private key or the signed data.

---

### Senior (Tranche)
The lowest-risk tranche. Senior LPs receive interest first (until their target is met) and are last to absorb losses. In a recovery event, Senior shortfalls are restored first.

---

### Target Interest
The theoretical interest a tranche is owed based on its `APR × deployed capital × time`. Distinguished from *accrued interest* (what has actually been paid). When repayments fall short of full interest due, Senior target is satisfied first before Junior and Equity targets are addressed.

---

### Tranche
A risk-stratified pool of capital. Credit Rail has three tranches (Senior, Junior, Equity) with different risk/return profiles. The tranche structure is the mechanism by which a single pool can simultaneously serve risk-averse LPs (Senior) and yield-seeking LPs (Equity).

---

### UltraHonk
The proving system used by Credit Rail's Noir circuit. UltraHonk is an instantiation of the PLONK-based proof system implemented in the Barretenberg backend. It supports the custom gates and lookup tables that make Noir's built-in functions (including the Schnorr verification and Poseidon2 hash) efficient within the circuit.

---

### Waterfall
The ordered application of payments (or losses) across tranches, with priority given to the most senior tranche. Credit Rail has four waterfalls: interest payment, principal repayment, loss absorption, and recovery. Each follows a defined seniority ordering.
