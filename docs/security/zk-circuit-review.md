# ZK Circuit Review — Findings & Limitations

> **Version:** 1.0 (V1 — Permissioned Architecture)  
> **Last Updated:** March 2, 2026  
> **Scope:** Noir ZK Circuit (`circuits/src/main.nr`) ↔ Solidity Smart Contracts (`contracts/src/LoanEngine.sol`, `contracts/src/CreditPolicy.sol`)  
> **Related Docs:** [assumptions.md](./assumptions.md) · [invariants.md](./invariants.md) · [THREAT_MODEL.md](../THREAT_MODEL.md)

---

## Overview

This document records the findings from a manual security review of the Noir ZK circuit and its interaction with the on-chain `LoanEngine` and `CreditPolicy` contracts. It covers circuit-specific attack vectors, cryptographic edge cases, and cross-boundary (ZK ↔ EVM) integration risks that are outside the scope of the broader [Threat Model](../THREAT_MODEL.md) and [Assumptions](./assumptions.md) documents.

**V1 Trust Model:** The current architecture is designed for a **permissioned, internally operated** system where the `FUND_MANAGER_ROLE` (Admin) and `POLICY_ADMIN_ROLE` are trusted entities. Several design decisions optimize for operational simplicity under this trust model, with clear upgrade paths for a more trustless V2.

---

## Table of Contents

1. [Trust Assumptions](#1-trust-assumptions)
2. [Known Limitations & V2 Roadmap](#2-known-limitations--v2-roadmap)
3. [Verified Security Properties](#3-verified-security-properties)
4. [Off-Chain Operational Risks](#4-off-chain-operational-risks)

---

## 1. Trust Assumptions

The following trust assumptions are **intentional design decisions** for the V1 permissioned architecture. They are not vulnerabilities — they are the boundaries of the system's threat model.

### 1.1 Admin (FUND_MANAGER_ROLE) Trust

The Admin is trusted to:

- Honestly pair the correct `borrower_secret` with the correct Underwriter attestation during proof generation.
- Not generate multiple proofs from a single Underwriter approval beyond what is operationally intended.
- Correctly fetch the sequential `loanId` before generating a ZK proof.

**Rationale:** The Admin is an internal operator (or a multisig) within the fund management entity. Rogue Admin behavior is an HR/legal issue, not a cryptographic one. The ZK proof still guarantees that every loan issued is backed by a verified financial profile adhering to the frozen Credit Policy, regardless of Admin behavior.

### 1.2 Policy Admin Trust

The `policyScopeHash` stored on-chain is **computed automatically on-chain** during `freezePolicy()` using the `Poseidon2` contract for each tier. The EVM independently verifies that this hash matches the actual on-chain policy parameters.

**Why:** This mathematically guarantees that the ZK proof is checking exactly the parameters stored on-chain.

**Mitigation:** 
- The `policyScopeHash` is computed inside `freezePolicy()`. Once frozen, it is permanently immutable.
- Any external party (LPs, auditors) can independently recompute the Poseidon2 hash from the on-chain policy storage values and verify it matches the stored `_policyScopeHashes[version][tier]`.

---

## 2. Known Limitations & V2 Roadmap

### 2.1 Sequential `loanId` Race Condition

| | |
|---|---|
| **Severity** | Medium (Operational) |
| **Component** | Circuit (`main.nr`) ↔ `LoanEngine.sol` |
| **Impact** | Transaction failure, not fund loss |

**Description:** The ZK circuit binds the proof to a sequential `loanId` (via `compute_loan_hash` and `nullifierHash`). Because proof generation takes several seconds off-chain, if two Admins generate proofs concurrently, the second transaction will revert because the on-chain `s_nextLoanId` has already incremented.

**Current Behavior:** The first proof to land on-chain succeeds; the second reverts with `LoanEngine__InvalidPublicInputs`. The Admin must regenerate the proof with the updated `loanId`.

**V2 Mitigation:** Remove `loanId` from the circuit entirely. Replace it with a private, randomly generated `nonce` in the `nullifierHash` calculation. This decouples proof generation from on-chain state, enabling stateless, parallel loan origination. The smart contract would assign `loanId` dynamically at mint time.

```
// V2 Nullifier (proposed)
nullifierHash = Poseidon2(nonce, borrower_secret, loan_principal, attestation_timestamp)
```

### 2.2 Cross-Chain / Cross-Deployment Replay

| | |
|---|---|
| **Severity** | Medium (Multi-Chain) |
| **Component** | Circuit (`compute_loan_hash`) |
| **Impact** | Proof replay across deployments |

**Description:** The `loan_hash` does not include a domain separator (`chainId` or `LoanEngine` contract address). If the same contracts are deployed on multiple chains (e.g., Arbitrum and Base), a valid proof generated for one chain could be replayed on another chain if both contracts happen to share the same `s_nextLoanId` state.

**Current Behavior:** Not exploitable in V1 (single-chain deployment).

**V2 Mitigation:** Add `chainId` and the `LoanEngine` contract address as private inputs to the circuit, hashed into the `loan_hash`. This follows the EIP-712 domain separator pattern adapted for ZK circuits.

```
// V2 Loan Hash (proposed)
loan_hash = Poseidon2(borrower_commitment, ..., chain_id, contract_address, loanId)
```

### 2.3 Borrower Identity Binding (Underwriter ↔ Borrower Decoupling)

| | |
|---|---|
| **Severity** | Low (Admin Trust) |
| **Component** | Circuit (`data_to_sign_hash`) |
| **Impact** | Identity mismatch under rogue Admin |

**Description:** The Underwriter's Schnorr signature covers the borrower's financial data but does **not** cover the `borrower_secret` or `borrower_commitment`. This means the Underwriter attests to the financial health of a borrower without cryptographically binding that attestation to a specific on-chain identity.

A trusted Admin is responsible for pairing the correct `borrower_secret` with the correct Underwriter attestation. A rogue Admin could theoretically use Borrower A's financial attestation to issue a loan under Borrower B's commitment.

**Why This Design Was Chosen:** 
- It decouples the traditional Web2 underwriting process from Web3 cryptographic identity management.
- The Underwriter's backend only needs to sign plain-text financial metrics — no knowledge of Poseidon2, BN254 fields, or ZK identity schemes is required.
- This enables integration with traditional institutional underwriting firms who should not be required to manage cryptographic secrets.

**V2 Mitigation:** Introduce a `Borrower_UUID` (a standard Web2 identifier from the internal CRM) into the Underwriter's signature payload. The circuit would then enforce that the `borrower_commitment` is derived from this UUID, eliminating the Admin's ability to swap identities without forcing the Underwriter to manage cryptographic keys.

### 2.4 Soft Commitment (Liquidity Over-Allocation)

| | |
|---|---|
| **Severity** | Low (Operational) |
| **Component** | `LoanEngine.sol` (`createLoan` → `activateLoan`) |
| **Impact** | Activation failure, not fund loss |

**Description:** `createLoan()` checks available pool liquidity but does not lock or reserve capital. Multiple loans can be created against the same idle liquidity. If total `CREATED` loan principals exceed available liquidity, subsequent `activateLoan()` calls will revert with `LoanEngine__InsufficientPoolLiquidity`.

**Why This Design Was Chosen:**
- Avoids gas-expensive capital locking mechanisms at creation time.
- Prevents liquidity fragmentation from abandoned `CREATED` loans that are never activated.
- The Admin controls the activation pipeline and can sequence activations appropriately.

**V2 Mitigation:** Implement a soft-reserve mechanism that tracks committed (but not yet deployed) capital, with automatic expiry for stale `CREATED` loans.

---

## 3. Verified Security Properties

The following properties have been verified through circuit analysis and unit testing (78 tests passing):

### 3.1 Input Aliasing Protection ✅

All `uint256` values passed to Poseidon2 hashing in `LoanEngine.sol` go through `Field.toField()`, which enforces `input < BN254_PRIME` via a `require` check. This makes field wrap-around / input aliasing attacks mathematically impossible.

**Verified in:** `contracts/lib/poseidon2-evm/src/Field.sol` — `checkField()` (line 12).

### 3.2 Schnorr Signature Soundness ✅

The Schnorr verification over Grumpkin (`verify_schnorr_signature`) is cryptographically sound:

- **Zero-point guard:** The circuit rejects `PK = (0, 0)` to prevent trivial forgery.
- **Curve membership:** Noir's `multi_scalar_mul` blackbox internally validates that points are on the Grumpkin curve.
- **Self-checking loop:** The verification recomputes `e' = Poseidon2(R'.x, R'.y, msg)` and asserts `e' == e`, making forgery equivalent to solving the Discrete Logarithm Problem.
- **Deterministic nonce:** The off-chain signing implementation (`zk-scripts/grumpkin.ts`) uses `k = sha256(sk || msg) mod n`, preventing nonce reuse.

**Test coverage:** 9 tests including valid signatures, wrong message, wrong PK, tampered `s`, tampered `e`, swapped components, and zero-point PK.

### 3.3 Proof Freshness (Timestamp Binding) ✅

The circuit's `current_timestamp` is hashed into the `loan_hash` (public input). On-chain, `LoanEngine.sol` enforces:

```solidity
if (block.timestamp - params.proofTimestamp > PROOF_MAX_AGE) revert;
```

This creates a tight 1-hour window between proof generation and on-chain submission, preventing the replay of stale proofs with forged timestamps.

### 3.4 Attestation Expiry ✅

`verify_attestation_age()` enforces that the Underwriter's attestation is within the policy's `max_attestation_age_days`. Overflow guards prevent:
- `u64` overflow in `max_age_seconds = days * 86400` (capped at `< 10,000` days).
- `u64` overflow in `attestation_timestamp + max_age_seconds` (explicit bound check).

### 3.5 Policy Immutability ✅

Once a policy version is frozen via `CreditPolicy.freezePolicy()`, all parameters (eligibility, ratios, tiers, document hash, scope hash) are permanently immutable. The `policyEditable` modifier prevents any writes to frozen versions. The ZK circuit's `policy_version_hash` (public input) binds the proof to the exact frozen policy state.

### 3.6 Nullifier Double-Spend Protection ✅

The `s_nullifierHashes` mapping in `LoanEngine.sol` prevents any proof from being processed more than once. Each unique combination of `[loanId, borrower_secret, loan_principal, attestation_timestamp]` produces a unique nullifier. Resubmitting the same proof reverts with `LoanEngine__ProofAlreadyUsed`.

### 3.7 Loan Term Enforcement ✅

The circuit enforces strict equality between loan terms and tier parameters:

```noir
assert(loan_apr_bps == tier_interest_rate_bps);
assert(loan_origination_fee_bps == tier_origination_fee_bps);
assert(loan_term_days == tier_term_days);
```

Combined with the `loan_hash` binding, this guarantees that no loan can be originated with terms that deviate from the frozen policy's tier definition.

### 3.8 Overflow Protection ✅

All arithmetic in the circuit uses `u64` types with explicit overflow guards:
- `loan_principal < 1e15` and `borrower_ebitda < 1e15` (prevents `loan_principal * 1000` from overflowing `u64`).
- `tier_max_loan_to_ebitda < 10e18` (prevents ratio calculation overflow).
- Noir's `u64` type enforces implicit range constraints — values ≥ 2^64 cause proof generation failure.

---

## 4. Off-Chain Operational Risks

### 4.1 Schnorr Nonce Reuse

If the Underwriter's signing backend uses the same random nonce `k` for two different messages, the private key `sk` can be trivially extracted:

```
sk = (s1 - s2) / (e2 - e1)
```

**Mitigation:** The `schnorrSign()` function in `zk-scripts/grumpkin.ts` uses a deterministic nonce derived from `sha256(sk || msg)`, ensuring the same `(sk, msg)` pair always produces the same `k`. Different messages always produce different nonces.

### 4.2 Underwriter Key Compromise

If the Underwriter's Grumpkin private key is compromised, an attacker with `FUND_MANAGER_ROLE` could generate unlimited valid proofs with arbitrary (but policy-compliant) financial data.

**Mitigation:**
- The `authorizedUnderwriters` mapping in `LoanEngine.sol` allows immediate revocation of compromised keys via `setUnderwriterAuthorization(keyX, keyY, false)`.
- In production, the Underwriter's private key should be stored in an HSM (Hardware Security Module).

### 4.3 Proof Generation Infrastructure

ZK proof generation requires access to the borrower's private financial data and the `borrower_secret`. The machine performing proof generation must be secured against data exfiltration.

**Mitigation:** In production, proof generation should occur in a Trusted Execution Environment (TEE) or an air-gapped secure enclave.

---

## Conclusion

Credit Rail V1 is designed as a permissioned, internally operated protocol where the Admin and Policy Admin are trusted entities. The ZK circuit provides cryptographic guarantees to external Liquidity Providers that every loan originated through the system adheres to the frozen Credit Policy, without revealing borrower identity or financial details.

The known limitations documented above are intentional design trade-offs that optimize for operational simplicity in a V1 deployment. Each has a clear architectural upgrade path for a future V2 trustless deployment.

For questions or to report a security concern, please open a GitHub issue or contact the maintainers directly.
