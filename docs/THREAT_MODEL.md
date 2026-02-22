# Credit Rail Threat Model

This document outlines the systematic security and threat model for the Credit Rail protocol. Given the institutional nature of this private credit rail, the security posture assumes a permissioned environment with zero-knowledge verification, specifically focusing on economic attack surfaces, trust boundaries, and actor-driven exploits.

---

## 1. System Actors & Trust Assumptions

Credit Rail operates under a delegated trust model where certain actions require whitelisted roles, but economic invariants must be enforced trustlessly by the smart contracts.

| Actor | Role / Capabilities | Trust Assumption |
| :--- | :--- | :--- |
| **Protocol Admin** | Upgrades contracts, manages roles, sets global fees, parameters, and pauses the protocol. | **Highly Trusted:** Expected to be governed by a `TimelockController` and a heavily distributed Multi-Sig (e.g., a Gnosis Safe). |
| **Underwriter** | Cryptographically signs off-chain loan structures that the ZK circuit hashes. | **Semi-Trusted:** Capable of originating loans, heavily restricted by the mathematically immutable `CreditPolicy` limits. |
| **Servicer** | Activates loans, reports off-chain repayments, and triggers default/write-off sequences. | **Semi-Trusted:** Can affect the state of outstanding loans and capital allocation. Cannot artificially print LP shares or steal idle capital. |
| **LPs (Liquidity Providers)** | Deposit stablecoins (e.g., USDC) into the TranchePool. | **Untrusted:** Subject to strict KYC/AML whitelisting before depositing, but economically assumed to be rational and potentially malicious. |
| **Borrower** | Off-chain entity receiving capital. | **Untrusted:** Submits zero-knowledge cryptographic proofs. Cannot access smart contracts directly. |

---

## 2. Trust Boundaries

- **On-chain vs. Off-chain (The ZK Boundary):** The most critical boundary. Borrowers generate proofs locally (or via an off-chain secure enclave) using their private financial data. The blockchain *only* sees the cryptographic proof and public inputs. The primary mitigation against "Garbage In, Garbage Out" is the underwriter signature checked against `policyScopeHash`.
- **Tranche Segregation:** The boundaries between the Senior, Junior, and Equity capital pools must remain impenetrable. A sudden loss in the Junior pool must strictly isolate the Senior pool from realizing any shortfall until the Junior pool is completely zeroed out.
- **Handler / Oracle Independence:** The protocol currently relies heavily on the `Servicer` role as the ultimate source of truth for fiat-leg repayments. The boundary here is strict: the Servicer cannot claim capital directly, they can only trigger `onRepayment` mapping funds into the TranchePool.

---

## 3. Threat Vectors & Mitigations

### 3.1 Economic & Logical Vectors

#### **T1: Share Inflation / Vault Manipulation**
- **Threat:** An LP or Servicer manipulates the `idleValue` or `deployedValue` of a tranche to artificially inflate the underlying value of their shares, similar to a classic ERC-4626 inflation attack.
- **Mitigation:** The protocol separates state into explicit `totalShares` and `idleValue`. The global interest index (`interestIndex`) pattern correctly calculates pro-rata distributions at O(1) efficiency without altering the strict 1:1 ratio of principal upon deposit. Rounding favors the protocol (downward division) preventing extraction of wei.

#### **T2: Waterfall Inversion (Senior Loss Extraction)**
- **Threat:** A catastrophic loan default is improperly accounted for, draining the Senior tranche while leaving the Equity tranche intact, destroying the foundational premise of structured finance.
- **Mitigation:** Fuzz testing specifically targets `invariant_waterfallSymmetry` and the `onLoss` sequence. The contracts execute a rigid reverse-for-loop: Equity → Junior → Senior, forcefully reverting via `TranchePool__LossExceededCapital` if the math breaks.

#### **T3: Ghost Interest Accrual**
- **Threat:** A defaulted loan artificially drives up the `targetInterest` of LPs, leading to a permanent shortfall where LPs cannot withdraw because the protocol thinks it has capital that doesn't exist.
- **Mitigation:** `onLoss` inherently triggers a ghost interest cancellation sequence, retroactively slashing the accrued targets (Senior first) to reset the system's economic state to reality.

### 3.2 Access Control & Cryptographic Vectors

#### **T4: Malicious or Compromised Underwriter**
- **Threat:** An attacker compromises an Underwriter's off-chain key and attempts to sign malicious loan parameters (e.g., 0% APR, 100-year term).
- **Mitigation:** The active `CreditPolicy.sol` uses `policyScopeHash` to construct a tight mathematical bounding box. The Noir zero-knowledge circuit guarantees that even with a valid Underwriter signature, if the parameters violate the frozen policy (e.g., `APR < MIN_APR`), the proof generation or on-chain verification will categorically fail.

#### **T5: ZK Proof Replay Attacks**
- **Threat:** An attacker captures a valid `createLoan` transaction from the mempool and replays the ZK proof to originate a duplicate loan.
- **Mitigation:** The protocol implements a rigid Nullifier Hash mechanism alongside a standard increasing `loanId` nonce. The `borrowerCommitment` and unique initialization vectors ensure `LoanProofVerifier.verify` is strictly a one-time operation per unique loan artifact.

#### **T6: Malicious Protocol Admin (Rug Pull)**
- **Threat:** The admin alters the `CreditPolicy` post-deposit to originate extremely risky loans, or directly alters the `LoanEngine` pointer in `TranchePool` to mint infinite loss limits.
- **Mitigation:** The active mitigation is the deployment of a heavily parameter-restricted Timelock delay for any state-altering `CreditPolicy` mutations, allowing LPs to withdraw if they disagree with the new parameters. The `CreditPolicy` also implements a `policyFrozen` boolean—once a policy generates a `policyScopeHash` that is actively referenced by live proofs, those parameters are immutable for the life of those loans.

---

## 4. Unmitigated Risks / Future Work

* **Off-Ramp Counterparty Risk:** The `LoanEngine` pays disbursements directly to a whitelisted off-ramping entity (e.g., a regulated custodian). If this custodian fails to wire fiat to the borrower, the protocol mathematically believes a loan is active when it is essentially void.
* **Servicer Centralization:** Currently, the `SERVICER_ROLE` is the sole oracle for off-chain repayment events. A compromised servicer could indefinitely pause repayments or prematurely mark loans as `DEFAULTED`. Future iterations should explore decentralized dispute resolution or multi-party computation (MPC) for servicer actions.
