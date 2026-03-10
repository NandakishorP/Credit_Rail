# V2 Proposal — Credit Rail Evolution Roadmap

> **Last Updated:** March 2, 2026  
> **Status:** Proposal (Not Implemented)  
> **Prerequisites:** All V1 contracts audited and deployed; operational feedback from at least one full loan lifecycle  
> **Related Docs:** [DESIGN_TRADEOFFS.md](./DESIGN_TRADEOFFS.md) · [security/zk-circuit-review.md](./security/zk-circuit-review.md) · [THREAT_MODEL.md](./THREAT_MODEL.md)

---

## Overview

This document proposes the architectural upgrades for Credit Rail V2. Each proposal directly addresses a known V1 limitation identified during the [ZK circuit review](./security/zk-circuit-review.md) and [design trade-off analysis](./DESIGN_TRADEOFFS.md). Proposals are ordered by priority: critical infrastructure first, then operational improvements, then feature expansions.

---

## Priority 1 — Critical Infrastructure

### P1.1 Stateless Loan Origination (Remove `loanId` from Circuit)

**V1 Problem:** The ZK circuit binds the proof to a sequential `loanId` fetched from on-chain state (`s_nextLoanId`). This creates a race condition when multiple Admins generate proofs concurrently — the second proof will fail because the `loanId` has already been consumed.

**V2 Solution:**

1. **Remove `loanId` from `compute_loan_hash` and `nullifierHash`** in the Noir circuit.
2. **Replace with a random `nonce`** generated client-side during proof generation.
3. **Assign `loanId` dynamically** in `LoanEngine.createLoan()` at transaction time.

```noir
// V2 Circuit Changes
fn compute_loan_hash(..., nonce: Field) -> Field {
    poseidon2::Poseidon2::hash([
        borrower_commitment,
        underwriter_public_key_x,
        underwriter_public_key_y,
        tier_id as Field,
        loan_principal as Field,
        loan_apr_bps as Field,
        loan_origination_fee_bps as Field,
        loan_term_days as Field,
        industry_hash,
        current_timestamp as Field,
        nonce,  // Random nonce instead of sequential loanId
    ], 11)
}

// V2 Nullifier
let nullifier = poseidon2::Poseidon2::hash(
    [nonce, borrower_secret, loan_principal as Field, attestation_timestamp as Field],
    4,
);
```

**Solidity Changes:**
```solidity
// LoanEngine.createLoan() — V2
// No longer uses s_nextLoanId for loan hash verification
// The nonce is embedded in the proof's loan_hash
// loanId is assigned at storage time:
uint256 loanId = s_nextLoanId++;
s_loans[loanId] = newLoan;
```

**Impact:** Enables fully parallel, stateless proof generation. Multiple Admins can generate proofs simultaneously without coordinating on-chain state. The nullifier hash still prevents double-spend because the random nonce makes each proof unique.

**Migration Risk:** Low. This is a circuit-level change that requires redeploying the Noir circuit and updating the `HonkVerifier` contract. Existing loans are unaffected.

---

### P1.2 Cross-Chain Domain Separator

**V1 Problem:** The `loan_hash` does not include a domain separator (`chainId`, contract address). A valid proof could theoretically be replayed across different chain deployments.

**V2 Solution:**

Add `chain_id` and `loan_engine_address` as private inputs to the circuit, hashed into the `loan_hash`:

```noir
fn compute_loan_hash(
    ...,
    chain_id: u64,           // NEW
    contract_address: Field,  // NEW
) -> Field {
    poseidon2::Poseidon2::hash([
        borrower_commitment,
        ...,
        chain_id as Field,
        contract_address,
    ], 13)
}
```

**Solidity Changes:**
```solidity
// LoanEngine.createLoan() — V2
inputs[11] = Field.toField(block.chainid);
inputs[12] = Field.toField(uint256(uint160(address(this))));
```

**Impact:** Proofs become deployment-specific. A proof generated for Arbitrum deployment A cannot be replayed on Base deployment B, even if both deployments share the same policy and loan parameters.

---

### P1.3 Borrower Identity Binding via UUID

**V1 Problem:** The Underwriter's Schnorr signature does not cover the `borrower_secret` or `borrower_commitment`. A trusted Admin can pair any valid financial attestation with any borrower identity.

**V2 Solution:**

Introduce a `borrower_uuid` (a standard Web2 identifier from the internal CRM) into the Underwriter's signature payload:

```noir
// V2: Underwriter signs the UUID alongside financial data
let data_to_sign_hash = poseidon2::Poseidon2::hash([
    borrower_uuid,                    // NEW — Web2 identifier
    borrower_annual_revenue as Field,
    borrower_ebitda as Field,
    ...,
    attestation_timestamp as Field,
], 13);

// V2: Commitment includes UUID
let computed_commitment = poseidon2::Poseidon2::hash([
    borrower_uuid,      // NEW
    borrower_secret,
    borrower_annual_revenue as Field,
    ...,
], 6);
```

**Workflow Change:**
1. KYC/KYB process assigns a `Borrower_UUID` (e.g., internal CRM ID, LEI).
2. The Underwriter's signing payload now includes this UUID alongside the financial metrics.
3. The circuit enforces that the `borrower_commitment` is derived from the same UUID.
4. The Admin can no longer swap identities because changing the `borrower_secret` would break the commitment, and changing the UUID would break the Underwriter's signature.

**Impact:** Eliminates the Admin identity-swapping attack vector without requiring the Underwriter to manage any cryptographic secrets. The UUID is a plain-text identifier they already use in their traditional workflow.

---

## Priority 2 — Operational Improvements

### P2.1 On-Chain Policy Hash Verification

**V1 Problem:** The `policyScopeHash` is computed off-chain and manually set by the `POLICY_ADMIN_ROLE`. There is no on-chain verification that it matches the actual policy storage.

**V2 Solution:**

Deploy a lightweight Poseidon2 verification contract that spot-checks policy integrity:

```solidity
// PolicyHashVerifier.sol — V2
function verifyPolicyScopeHash(uint256 version) external view returns (bool) {
    ICreditPolicy cp = ICreditPolicy(creditPolicy);
    
    // Sample 3 fields and verify they match their positions in the hash
    // Full 21-field verification is too expensive (~2M gas)
    // Probabilistic check catches accidental mismatches
    
    EligibilityCriteria memory e = cp.eligibility(version);
    FinancialRatios memory r = cp.ratios(version);
    
    // Verify the hash was computed with the correct min_revenue in position 0
    // and correct max_debt_to_ebitda in position 6
    // If any field is wrong, the hash will not match
    
    Field.Type[] memory inputs = new Field.Type[](21);
    inputs[0] = Field.toField(e.minAnnualRevenue);
    // ... populate all 21 fields ...
    
    bytes32 computed = bytes32(Field.toUint256(poseidon2.hash(inputs)));
    return computed == cp.policyScopeHash(version);
}
```

**Alternative V2 Approach:** If gas costs for full 21-field Poseidon2 hashing become acceptable (through EIP precompiles or L2 gas reductions), compute the hash automatically in `freezePolicy()` instead of requiring manual `setPolicyScopeHash()`.

---

### P2.2 Capital Reservation with Expiry

**V1 Problem:** `createLoan()` does not reserve capital. Multiple `CREATED` loans can over-commit the pool.

**V2 Solution:**

```solidity
// LoanEngine.createLoan() — V2
s_reservedCapital += params.principalIssued;
s_loanReservationExpiry[loanId] = block.timestamp + RESERVATION_WINDOW;

// Effective idle = totalIdle - reservedCapital
if (params.principalIssued > i_tranchePool.getTotalIdleValue() - s_reservedCapital) {
    revert InsufficientLiquidity();
}

// Cleanup function (callable by anyone)
function expireReservation(uint256 loanId) external {
    if (block.timestamp > s_loanReservationExpiry[loanId]) {
        s_reservedCapital -= s_loans[loanId].principalIssued;
        s_loans[loanId].state = LoanState.EXPIRED; // New terminal state
    }
}
```

**Impact:** Prevents liquidity over-allocation. Stale reservations automatically expire after a configurable window (e.g., 48 hours), preventing liquidity fragmentation from abandoned loans.

---

### P2.3 Multi-Servicer with Dispute Resolution

**V1 Problem:** A single `SERVICER_ROLE` is the sole oracle for repayment events. A compromised Servicer can delay or fabricate repayments.

**V2 Solution:**

Introduce a 2-of-3 multi-sig pattern for critical Servicer actions:

```solidity
// V2: Repayment requires confirmation from 2 of 3 authorized servicers
mapping(uint256 => mapping(address => bool)) public repaymentConfirmations;
uint256 public constant REQUIRED_CONFIRMATIONS = 2;

function confirmRepayment(
    uint256 loanId,
    uint256 principalAmount,
    uint256 interestAmount,
    address repaymentAgent
) external onlyRole(SERVICER_ROLE) {
    bytes32 repaymentHash = keccak256(abi.encode(loanId, principalAmount, interestAmount));
    repaymentConfirmations[repaymentHash][msg.sender] = true;
    
    if (confirmationCount(repaymentHash) >= REQUIRED_CONFIRMATIONS) {
        _executeRepayment(loanId, principalAmount, interestAmount, repaymentAgent);
    }
}
```

**Impact:** No single compromised Servicer can fabricate repayment events. Requires collusion between multiple independent entities.

---

## Priority 3 — Feature Expansions

### P3.1 Borrower Self-Service Portal

Allow borrowers to generate their own ZK proofs through a web interface, eliminating the `FUND_MANAGER` as a proof-generation bottleneck.

**Requirements:**
- Client-side WASM proof generation (Barretenberg already supports this)
- EIP-4337 account abstraction for gas-sponsored submissions
- The UUID binding (P1.3) must be implemented first to prevent borrower impersonation

### P3.2 Automated Maturity Monitoring

Deploy a Chainlink Automation keeper that automatically calls `declareDefault()` when a loan exceeds its maturity date plus a configurable grace period, reducing dependence on the `RISK_ADMIN_ROLE` for routine defaults.

### P3.3 LP Governance Module

Introduce a lightweight governance system where Senior LPs (above a minimum deposit threshold) can vote on:
- Policy version activation/deactivation
- Maximum fund-level concentration limits
- Servicer role changes

This does not replace the `ProtocolController` timelock but adds an LP consent layer for material changes.

### P3.4 Proof Aggregation (Batch Loan Creation)

Use Noir's recursive proof composition to batch multiple loan proofs into a single aggregated proof, reducing on-chain verification gas by ~80% when originating multiple loans in the same block.

```noir
// V2: Recursive proof aggregation
fn verify_batch(
    proof_1: Proof,
    proof_2: Proof,
    // ... up to N proofs
) {
    // Verify each sub-proof recursively
    // Output a single aggregated proof that covers all N loans
}
```

### P3.5 Tradable Tranche Shares & Secondary Liquidity

**V1 Problem:** LPs are completely locked into their positions while the pool is `DEPLOYED`. Additionally, if a pool transitions to `CLOSED` and LPs fully withdraw by burning their shares, any delayed loan recovery (e.g., from long-term bankruptcy proceedings) becomes permanently locked in the contract because there are no shares left to claim it.

**V2 Solution:** Tokenize Tranche Shares as standard transferrable ERC-20 tokens and implement snapshot-based capital claims.

1. **ERC-20 Tranche Tokens:** Convert the internal `mapping(address => uint256) shares` into compliant ERC-20 tokens (e.g., `crSENIOR`, `crJUNIOR`). This enables a secondary market, allowing LPs to sell their risk positions and exit early without the underlying loans needing to be liquidated.
2. **Snapshot-Based Closed Pool Recoveries:** When a pool transitions to `CLOSED`, the protocol takes a snapshot of final token balances. LPs can claim their pro-rata share of `idleValue` *without* burning their tokens. If a late `onRecovery()` event brings new funds into the closed pool months later, the LPs holding the snapshot balances can return and claim their pro-rata share of the newly recovered funds.

**Impact:** Dramatically improves LP liquidity via secondary markets while elegantly solving the "Zero-Share Recovery" lockup edge case by decoupling capital withdrawal from share destruction.

---

## Migration Strategy

### Phase 1: Circuit Upgrade (P1.1, P1.2, P1.3)
1. Deploy updated Noir circuit with nonce, domain separator, and UUID.
2. Generate new verification key and deploy updated `HonkVerifier`.
3. Update `LoanEngine` via UUPS upgrade to support the new public input format.
4. All existing loans (created under V1 circuit) remain valid and unaffected.

### Phase 2: Contract Upgrades (P2.1, P2.2, P2.3)
1. Deploy `PolicyHashVerifier` as a standalone view contract.
2. Upgrade `LoanEngine` to support capital reservation and multi-servicer confirmation.
3. Add `EXPIRED` loan state to the state machine.

### Phase 3: Feature Rollout (P3.1 — P3.4)
1. Deploy borrower self-service frontend.
2. Register Chainlink Automation keeper for maturity monitoring.
3. Deploy LP governance module as an independent contract.
4. Implement recursive proof aggregation (requires Noir stdlib support for recursive verification).

---

## Timeline Estimate

| Phase | Scope | Estimated Effort |
|---|---|---|
| Phase 1 | Circuit + Verifier upgrade | 4-6 weeks |
| Phase 2 | Contract upgrades | 3-4 weeks |
| Phase 3 | Feature rollout | 6-8 weeks |
| Audit | Full re-audit of V2 changes | 4-6 weeks |

**Total V2 Timeline:** ~4-6 months from V1 stabilization.

---

## Conclusion

V2 transforms Credit Rail from a permissioned institutional prototype into a production-grade, multi-party lending infrastructure. The three Priority 1 changes (stateless origination, domain separator, UUID binding) eliminate the core trust assumptions identified during the V1 circuit review. The Priority 2 and 3 changes progressively reduce operational centralization while maintaining the institutional compliance framework that differentiates Credit Rail from consumer DeFi lending protocols.
