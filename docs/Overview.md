 
# Institutional Private Credit Rail
Credit Rail is an on-chain accounting and risk allocation engine for institutional private credit. It connects off-chain underwriting decisions to on-chain capital allocation, using zero-knowledge proofs to verify loan compliance without exposing any sensitive borrower data.

It's not a liquidation-based lending protocol, not a KYC provider, and not a legal enforcement system. It is a strict accounting ledger — one that enforces capital allocation, interest waterfalls, and loss absorption with mathematical certainty.

## The Problem & The Solution

Institutional borrowers — companies seeking credit from private funds — have detailed financial records: revenue, EBITDA, debt ratios, industry classifications. These records are the basis of any credit underwriting decision, but they are fundamentally private. Posting them on a public blockchain is a non-starter for any serious institutional counterparty.

At the same time, liquidity providers deploying capital into private credit funds want guarantees. They want to know that the loans being originated actually meet the fund's stated risk criteria, and that the capital waterfall will protect them in the event of a default — without having to trust a central administrator to do the right thing.

The core tension is: **how do you enforce a credit policy on-chain when the underlying borrower data cannot be public?**

## The Solution

Credit Rail solves this with three components working together:

**1. Zero-Knowledge Origination**
Each loan originates through a Noir ZK circuit. The borrower's financial data — revenue, EBITDA, debt ratios, business age — is never posted on-chain. Off-chain, an underwriter reviews the borrower's financials through traditional due diligence and cryptographically signs the data using a Schnorr signature over the Grumpkin curve (BN254 embedded curve, ~10x cheaper in constraints than secp256k1 ECDSA). The fund admin then takes this signed data, feeds it as private inputs into the Noir circuit, and generates a ZK proof using the UltraHonk proving system. The proof attests that: the borrower's data meets every threshold in the frozen credit policy, the underwriter's signature over the raw data is valid, and the loan parameters match the selected pricing tier exactly. The on-chain `LoanEngine` verifies this proof against the `HonkVerifier` contract without ever seeing the underlying borrower financials. The off-chain underwriter and the on-chain transaction submitter are intentionally separate roles — the circuit enforces that a real underwriter signed off on the data, while the fund admin is responsible for executing the on-chain commitment.

**2. Immutable Credit Policy**
The risk parameters of the fund — minimum revenue, maximum debt-to-EBITDA, allowed industries, pricing tiers — are stored in the `CreditPolicy` contract. Before a policy version can be used to originate loans, it must be frozen. Freezing computes a Poseidon2 hash of all 21 parameters, the `policyScopeHash`. This hash is embedded in every ZK proof that references that policy. There is no way to retroactively change the rules a loan was written under — not even for an admin.

**3. Tranched Capital Pool**
Liquidity is organized into three tranches in the `TranchePool`:
- **Senior**: Fixed APR, highest priority in payment and recovery, last to absorb losses.
- **Junior**: Slightly higher risk and return, buffer between Senior and Equity.
- **Equity**: Residual yield claimant and first-loss absorber. Earns surplus; bears default losses first.

When a repayment arrives, interest flows to Senior until its target is met, then to Junior, then the residual goes to Equity. When a default is written off, losses are absorbed in reverse: Equity first, Junior second, Senior last. This waterfall is enforced mechanically by the smart contracts — not by an administrator's discretion.

---

## What It Is / What It Isn't

**It is:**
- An accounting and incentive enforcement layer for institutional credit
- A risk allocation engine using structured tranching
- A cryptographic verification bridge between off-chain underwriting and on-chain capital
- A protocol primitive that a private credit fund could plug into

**It is not:**
- A legal enforcement system (defaults are declared by the servicer, not triggered algorithmically)
- A KYC provider (whitelisting and identity are handled entirely off-chain)
- A trustless system (it operates in a permissioned environment with whitelisted servicers and underwriters)
- A liquidation engine (there are no collateral seizures or price oracles)

---

## A Loan's Lifecycle

To make the system concrete, here is what happens when a single loan moves through the protocol end-to-end:

1. **Deposit**: Liquidity providers deposit USDC into the Senior, Junior, or Equity tranche of the `TranchePool`, receiving shares proportional to their contribution. Withdrawals are permitted when the pool is in the `OPEN` or `CLOSED` state.

   > The pool state is strictly one-directional: `OPEN → COMMITTED → DEPLOYED → CLOSED`.

2. **Policy Setup**: The fund administrator configures a `CreditPolicy` version — setting eligibility criteria, financial ratio thresholds, pricing tiers, and industry exclusions — then freezes it. Freezing generates the `policyScopeHash` that all future proofs for this policy must reference.

3. **Underwriting**: Off-chain, an authorized underwriter reviews the borrower's financials and signs the data using their Grumpkin private key. The signed attestation is timestamped and bounded by the policy's `maxAttestationAgeDays` to prevent stale underwriting.

4. **ZK Proof Generation**: The fund admin generates a ZK proof using the Noir circuit. The proof encodes: a borrower commitment (binding the private financial data to the proof without revealing it), a unique nullifier hash (preventing proof replay), and verification of the underwriter's Schnorr signature over the borrower data.

5. **Loan Creation**: The fund manager submits `createLoan()` to the `LoanEngine` with the proof and three public inputs: the `policy_version_hash`, the `loan_hash`, and the `nullifierHash`. The contract verifies the proof, checks the nullifier hasn't been used, and confirms the loan hash matches the on-chain recomputed value using Poseidon2.

6. **Capital Deployment**: The servicer calls `activateLoan()`, deploying USDC from the `TranchePool` to the borrower's nominated off-ramping address. Capital is split across tranches according to the pool's current allocation ratios (default: 80% Senior, 15% Junior, 5% Equity).

7. **Repayment**: The servicer reports repayments on-chain via `repayLoan()`. Interest is applied first (routed through the tranche waterfall), then principal (returned to idle capital in the pool, available for redeployment).

8. **Default & Recovery**: If a loan defaults, the servicer declares it via `declareDefault()`. After write-off, any recovered funds flow through `recoverLoan()` back into the pool, restoring Senior first, then Junior, then Equity — with any excess beyond total shortfall flowing to Equity as upside.

---

## Technical Stack

| Layer | Technology |
|---|---|
| Smart Contracts | Solidity 0.8.30, deployed on zkSync Era |
| ZK Circuit | Noir (v1.0.0-beta.16), UltraHonk proving system |
| On-chain Verifier | Auto-generated `HonkVerifier.sol` from Noir circuit |
| Hash Function | Poseidon2 (BN254 field), matching between circuit and on-chain |
| Signature Scheme | Schnorr over Grumpkin (BN254 embedded curve) |
| Governance | OpenZeppelin `TimelockController` wrapped in `ProtocolController` |
| Proof Scripts | TypeScript + `@aztec/bb.js` (Barretenberg WASM) |
| Economic Model | Python simulation (`model/flows.py`, `model/state.py`) |
| Testing | Foundry unit tests, Foundry invariant fuzzing, Echidna, Medusa, Wake (Python) |

---

## Repository Structure

```
credit_rail/
├── circuits/            # Noir ZK circuit + test cases
├── contracts/           # Solidity contracts, tests, deployment scripts
│   ├── src/             # Core: LoanEngine, TranchePool, CreditPolicy, ProtocolController
│   ├── test/            # Unit tests, invariant fuzzing, Echidna, Medusa
│   └── script/          # Foundry deploy + E2E test scripts
├── zk-scripts/          # TypeScript: proof generation, policy setup, on-chain integration
├── economic-modelling/  # Python: capital flow simulation and conservation law validation
└── docs/                # This documentation
```
