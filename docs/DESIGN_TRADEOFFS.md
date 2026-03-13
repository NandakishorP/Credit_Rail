# Design Trade-Offs

> **Last Updated:** March 2, 2026  
> **Scope:** Full system — Noir ZK Circuit, Solidity Smart Contracts, Off-Chain Infrastructure  
> **Related Docs:** [architecture.md](./architecture.md) · [THREAT_MODEL.md](./THREAT_MODEL.md) · [security/zk-circuit-review.md](./security/zk-circuit-review.md)

---

## Overview

Every engineering decision in Credit Rail involves a trade-off between competing goals: security vs. gas cost, privacy vs. auditability, trustlessness vs. operational simplicity. This document explicitly catalogues those trade-offs so that LPs, auditors, and future contributors understand *why* the system works the way it does — not just *how*.

---

## 1. Permissioned vs. Trustless Architecture

| Dimension | V1 Choice | Alternative | Why V1 Wins For Now |
|---|---|---|---|
| Loan origination | `FUND_MANAGER_ROLE` submits proofs | Borrower self-serves | Institutional funds require KYC/AML gatekeeping; self-service origination would require on-chain identity binding (EIP-4337 wallets, DID integrations) that adds months of complexity |
| Repayment reporting | `SERVICER_ROLE` calls `repayLoan()` | Oracle / Chainlink Functions | Off-chain fiat repayments have no on-chain signal; an oracle would need bank API integrations and introduce additional trust assumptions |
| Default declaration | `RISK_ADMIN_ROLE` calls `declareDefault()` | Automated maturity-based default | Real-world private credit includes grace periods, restructuring, and partial recoveries that cannot be encoded in a smart contract rule |
| Policy authoring | `POLICY_ADMIN_ROLE` sets all parameters | DAO governance | Institutional credit policies are written by credit committees, not token holders; DAO governance would be a regulatory liability |

**The Implication:**  
Credit Rail V1 is not a DeFi protocol in the "permissionless, anyone can participate" sense. It is a **structured finance vehicle** that uses blockchain for transparency, immutability, and ZK-verified compliance. The permissioned roles mirror the legal structure of a real regulated fund: Fund Manager, Servicer, Risk Officer, Policy Committee.

**What This Means for LPs:**  
LPs trust the *smart contract invariants* (18 invariant tests, see [invariants.md](./security/invariants.md)), not the *operators*. Even a rogue Servicer cannot inflate shares, steal idle capital, or invert the loss waterfall. They can only affect *timing* (delay repayments, prematurely default) — which is mitigated by the Timelock governance delay and LP withdrawal windows.

---

## 2. ZK Proof Architecture Trade-Offs

### 2.1 Grumpkin Schnorr vs. ECDSA secp256k1

| | Grumpkin Schnorr | ECDSA secp256k1 |
|---|---|---|
| Constraint cost | ~2,000 constraints | ~20,000+ constraints |
| Proving time | ~2s | ~15-20s |
| On-chain key format | Two BN254 Field elements | Standard Ethereum address |
| Key reuse with EOA wallets | ❌ Separate key management | ✅ Same key as MetaMask |

**Why Grumpkin:** Grumpkin is the embedded curve of BN254 (the curve underlying `alt_bn128` and Noir's proving backend). Its arithmetic is native to the SNARK backend, making signature verification ~10x cheaper in constraints. This directly translates to faster proof generation and smaller proof sizes.

**The Cost:** The Underwriter needs a separate Grumpkin keypair managed by the backend infrastructure, rather than reusing an Ethereum EOA. For an institutional system with dedicated signing infrastructure, this is a non-issue. For a consumer-facing product, it would be a UX barrier.

### 2.2 Poseidon2 vs. Keccak256 for Circuit Hashing

| | Poseidon2 | Keccak256 |
|---|---|---|
| ZK constraint cost | ~300 constraints per hash | ~150,000 constraints per hash |
| EVM gas cost | ~100,000 gas (external precompile) | ~30 gas (native opcode) |
| Standardization | Emerging (Aztec, Polygon) | Universal |

**Why Poseidon2:** Keccak256 inside a ZK circuit is catastrophically expensive (~500x more constraints). Since the circuit hashes 12+ fields per proof, using Keccak would make the circuit impractically large. The trade-off is that on-chain hash verification requires calling an external Poseidon2 precompile contract, adding gas overhead and a deployment dependency.

### 2.3 Public vs. Private Inputs

| Input | Visibility | Why |
|---|---|---|
| `policy_version_hash` | **Public** | LPs must verify which policy governs each loan |
| `loan_hash` | **Public** | On-chain reconstruction ensures loan terms match the proof |
| `nullifierHash` | **Public** | On-chain nullifier registry prevents double-spend |
| `borrower_commitment` | **Private** (hashed into `loan_hash`) | Borrower pseudonymity — the raw commitment is never exposed as a standalone public input |
| All financial data | **Private** | Core privacy guarantee — revenue, EBITDA, ratios never touch the blockchain |
| Policy constraints | **Private** | Prevents competitors from reverse-engineering the fund's exact underwriting criteria |

**The Trade-Off:** Making the policy constraints private means LPs cannot independently verify *what* the eligibility thresholds are — only that the proof was generated against the correct frozen `policy_version_hash`. However, the `policyScopeHash` is now automatically computed from the on-chain policy parameters during policy freezing, eliminating the trust assumption.

---

## 3. Smart Contract Architecture Trade-Offs

### 3.1 Two-Phase Loan Creation (Create → Activate)

| | Single-Step (Create + Deploy) | Two-Step (V1 Design) |
|---|---|---|
| Atomicity | Capital locked at proof time | Capital reserved at activation |
| Operational flexibility | None — proof must match exact liquidity | Admin can batch, reorder, or abandon created loans |
| Liquidity risk | No over-commitment possible | Soft commitment risk (see §3.2) |
| Gas cost | One transaction | Two transactions |

**Why Two-Step:** In institutional lending, the underwriting decision and the capital deployment are separate events. A loan may be approved (created with a valid ZK proof) but not funded for days while legal documents are finalized off-chain. The two-step model mirrors this real-world workflow.

### 3.2 Soft Commitment (No Capital Reservation)

`createLoan()` validates available liquidity (`params.principalIssued > totalIdleValue` reverts) but does **not** lock or escrow funds. Multiple `CREATED` loans can potentially exceed total idle capital.

**Why No Reservation:**  
- Avoids gas-expensive storage writes for capital locking at creation time
- Prevents liquidity fragmentation from abandoned `CREATED` loans that are never activated
- In practice, the Admin controls both creation and activation, so the sequencing is deterministic

**The Cost:** If the Admin creates 5 loans worth $500K each against a pool with $2M idle, and then activates all 5, the 5th `activateLoan()` will revert with `InsufficientPoolLiquidity`. This is an operational inconvenience, not a security vulnerability.

### 3.3 Simple Interest vs. Compound Interest

Credit Rail uses **simple interest** accrual:
```
interest = principal × APR × timeElapsed / (365 days × 10,000)
```

**Why Simple:** 
- Matches the legal documentation of institutional private credit facilities, which universally use simple interest
- Eliminates compounding rounding errors that accumulate over long-dated loans (1-3 years)
- Reduces gas cost — no exponential math or iteration required

**The Cost:** For very short-term, frequently-rolled facilities, compound interest would generate slightly higher yields for LPs. This is not relevant for Credit Rail's target loan durations (90-365 days).

### 3.4 O(1) Interest Distribution (Global Index Pattern)

Interest is distributed to LPs using a global `interestIndex` per tranche, rather than iterating over all LP addresses.

**Why:** A naive loop over N LPs would cost O(N) gas per repayment, making the protocol unusable beyond ~50 LPs. The index pattern enables O(1) distributions regardless of LP count.

**The Cost:** LPs must explicitly call `claimInterest()` to collect accrued yield. Interest is not automatically pushed to their wallets. This is standard in DeFi (Compound, Aave, MorphoBlue all use this pattern).

### 3.5 UUPS Upgradeability

All three core contracts are upgradeable via the UUPS proxy pattern.

**Why:** Institutional deployments require the ability to patch bugs, add features, and adapt to regulatory changes without migrating all state to new contracts.

**The Cost:** Upgradeability introduces a trust vector — the `DEFAULT_ADMIN_ROLE` (held by `ProtocolController`, a `TimelockController`) can deploy a malicious implementation. This is mitigated by the timelock delay (LPs can exit before the upgrade executes) and the `__gap` storage slots for safe storage layout evolution.

### 3.6 Zero-Share Recovery in Closed Pools

A pool can only transition to the `CLOSED` state once `totalDeployedValue == 0` (all loans are either fully repaid or written-off). Once closed, LPs can withdraw their remaining capital and burn their shares. 

However, if all LPs fully withdraw and their `totalShares` drop to `0`, any subsequent `onRecovery()` events for previously written-off loans will lock the recovered funds in the contract. The funds are added back to the tranche's `idleValue`, but with zero shares remaining and deposits disabled in a `CLOSED` pool, no one can claim them, and the Admin cannot sweep them since they are not tracked as `s_protocolRevenue`.

**Why Not Prevent This:** 
- Retaining "redeemable value" for burned shares, or automatically classifying zero-share recoveries as sweepable protocol revenue, requires complex storage overhead and edge-case accounting that bloats the core waterfall logic.

**The Cost:** Counterparty recoveries that take years (e.g., protracted bankruptcy court proceedings) cannot be permissionlessly recovered by LPs if they empty the pool too soon. This is mitigated operationally: the Admin can simply wait to distribute out-of-band fiat recoveries directly to LPs off-chain if the on-chain pool is already empty.

---

## 4. Off-Chain Infrastructure Trade-Offs

### 4.1 Servicer as the Sole Repayment Oracle

The `SERVICER_ROLE` is the only entity that can call `repayLoan()`. There is no on-chain mechanism to independently verify that a fiat repayment actually occurred.

**Why:** Private credit repayments happen via bank wire. There is no existing on-chain oracle for bank wire confirmations. Building one would require banking API integrations (Plaid, Stripe Treasury) and regulatory approval — a multi-year effort outside the scope of a lending protocol.

**The Cost:** A compromised Servicer could indefinitely delay reporting repayments (causing phantom defaults) or report phantom repayments (temporarily inflating LP yields until the real default surfaces). Both are detectable by off-chain audits.

### 4.2 Off-Ramp Entity as Disbursement Target

Loan principal is not sent to the borrower's wallet. It is sent to a whitelisted `receivingEntity` (typically a regulated custodian or payment processor that converts USDC → fiat).

**Why:** Institutional borrowers (SMEs, logistics companies) need fiat, not stablecoins. The off-ramp entity bridges the on-chain/fiat boundary.

**The Cost:** If the off-ramp entity fails to wire fiat to the borrower, the protocol records an active loan against a borrower who never received funds. This is a counterparty risk mitigated by legal agreements and regulated custodian selection, not by smart contract logic.

### 4.3 Deterministic Schnorr Nonces

The Underwriter's signing function uses `k = sha256(sk || msg)` instead of a random nonce.

**Why:** Random nonces from a CSPRNG are safe if the entropy source is trustworthy. But if the signing backend ever has a faulty RNG (a real-world vulnerability — see the PlayStation 3 ECDSA key extraction), nonce reuse would expose the Underwriter's private key. Deterministic nonces (RFC 6979 style) eliminate this entire class of vulnerability.

**The Cost:** The same `(sk, msg)` pair always produces the same signature. This is not a problem because the `attestation_timestamp` in the signed payload ensures every signing event produces a unique message hash.

---

## 5. Privacy vs. Auditability Trade-Offs

### 5.1 Borrower Pseudonymity

On-chain, a borrower is identified only by their `borrower_commitment` hash. The same borrower using the same secret across multiple loans will produce the same commitment, making all their loans **linkable** to each other on-chain.

**Why Not Full Anonymity:** Institutional LPs and regulators need the ability to assess concentration risk ("Is one borrower taking 80% of the pool?"). Linkable pseudonymity enables this without revealing the borrower's real identity.

**The Cost:** An observer can count how many loans belong to the same `borrower_commitment` and calculate total exposure. They cannot determine *who* the borrower is, but they can detect concentration patterns.

### 5.2 Policy Privacy

The actual policy thresholds (min revenue, max debt ratio, etc.) are private inputs to the ZK circuit. Only the `policy_version_hash` is public.

**Why:** The fund's underwriting criteria are proprietary intellectual property. Publishing them would allow competitors to precisely replicate the fund's investment strategy.

**The Cost:** LPs cannot independently verify the policy thresholds. They can verify that the policy hash matches the on-chain frozen version, which is now automatically computed on-chain to remove the trust assumption.

---

## Summary

| Trade-Off | V1 Chose | Over |
|---|---|---|
| Permissioned roles | Operational simplicity | Trustless access |
| Grumpkin Schnorr | 10x fewer constraints | Ethereum EOA key reuse |
| Poseidon2 hashing | ZK-native efficiency | EVM-native convenience |
| Two-phase loan creation | Real-world workflow match | Atomic capital locking |
| Soft commitment | No liquidity fragmentation | Deterministic capital reservation |
| Simple interest | Legal compliance | Compound yield optimization |
| UUPS upgradeability | Institutional adaptability | Immutability guarantees |
| Zero-share recovery | Accounting simplicity | Orphaned recovered funds |
| Servicer oracle | Practical fiat integration | Decentralized verification |
| Linkable pseudonymity | Concentration risk monitoring | Full anonymity |
| Private policy thresholds | IP protection | LP transparency |

Each of these decisions can be revisited in future versions. See [V2_PROPOSAL.md](./V2_PROPOSAL.md) for the planned evolution.
