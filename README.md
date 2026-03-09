# Credit Rail

Private credit on-chain. Borrower financials stay off-chain.
Policy compliance is ZK-proven, not trusted.

Built on Foundry + Noir, tested with three fuzz frameworks, deployed on zkSync Era.

---

## The Hard Problems This Solves

**1. On-chain privacy for institutional underwriting**

Institutional borrowers cannot expose revenue, EBITDA, debt ratios, or banking relationships on a public chain. The standard solution — off-chain underwriting with on-chain IOUs — removes any trustless guarantee of policy compliance.

Credit Rail solves this with a Noir ZK circuit that the Fund Manager runs off-chain. The borrower's private financial data is fed in as private inputs. The circuit proves all policy constraints are satisfied (eligibility, financial ratios, tier bounds) and outputs only three values to the chain: a policy version hash, a loan parameter hash, and a nullifier. The borrower never interacts with the chain at all.

**2. Cryptographic binding of proof to policy**

A proof must be tied to a *specific, immutable* version of the credit policy — otherwise an underwriter could generate a valid proof against a loose policy and then tighten the policy post-origination to mask the violation.

The solution: the `policyScopeHash` — a Poseidon2 hash of all 21 policy parameters — is computed off-chain and set on-chain via `setPolicyScopeHash()` before the policy is frozen. The Noir circuit embeds this hash as a public input. `LoanEngine.createLoan()` independently recomputes the loan hash from on-chain state and rejects any proof where the hashes don't match. The policy and the proof are cryptographically bound.

**3. Underwriter signature scheme: Schnorr over Grumpkin**

The underwriter attests to the borrower's private data with a cryptographic signature. ECDSA over secp256k1 was rejected — verifying it inside a ZK circuit requires ~250k constraints. Schnorr over Grumpkin (BN254's embedded curve) reduces this to ~25k constraints because Grumpkin arithmetic is native to the BN254 proving backend. The signature scheme: `R = s·G + e·PK`, verified via `multi_scalar_mul` as a blackbox opcode.

**4. Structured finance waterfall with lazy interest accrual**

Interest accrues on-demand (no keepers, no oracles). When capital is deployed, the `TranchePool` tracks per-tranche target interest using each tranche's configured APR and deployed principal. On repayment, interest flows Senior → Junior → Equity (residual). On write-off, principal loss is absorbed Equity → Junior → Senior. On recovery, shortfalls are restored Senior → Junior → Equity with any excess flowing to equity upside.

LP claims use a global interest index pattern (`interestIndex += Δ / totalShares`) for O(1) per-user accounting regardless of pool size.

---

## Architecture

```
Off-chain                              On-chain
─────────────────────────────────      ──────────────────────────────────────
Borrower → Underwriter                 LoanEngine.createLoan()
           (Schnorr sign)   →  proof      → CreditPolicy.policyScopeHash()
           ↓                               → Poseidon2.hash() [recompute loan hash]
           Noir Circuit                    → HonkVerifier.verify()
           (Barretenberg)              LoanEngine.activateLoan()
                                           → TranchePool.allocateCapital()
                                       LoanEngine.repayLoan()
                                           → TranchePool.onRepayment()
                                       LoanEngine.writeOffLoan()
                                           → TranchePool.onLoss()
                                       LoanEngine.recoverLoan()
                                           → TranchePool.onRecovery()
```

**Loan state machine:** `CREATED → ACTIVE → REPAID` or `ACTIVE → DEFAULTED → WRITTEN_OFF`

**Pool state machine:** `OPEN → COMMITTED → DEPLOYED → CLOSED`

Every function is role-gated — there are no public entry points. Role separation:

| Role | Functions |
|---|---|
| `FUND_MANAGER_ROLE` | `createLoan()` — submits ZK proof, originates loan |
| `SERVICER_ROLE` | `activateLoan()`, `repayLoan()`, `recoverLoan()` |
| `RISK_ADMIN_ROLE` | `declareDefault()`, `writeOffLoan()` |
| `CONFIG_ADMIN_ROLE` | Whitelists, fee parameters |
| `EMERGENCY_ADMIN_ROLE` | `pause()`, `unpause()` |

All contracts are UUPS upgradeable. In production, `DEFAULT_ADMIN_ROLE` is held by a `TimelockController`.

---

## ZK Circuit

**Location:** `circuits/src/main.nr`

**Proving system:** UltraHonk (Barretenberg WASM)

**Public inputs (3):**
| Input | Purpose |
|---|---|
| `policy_version_hash` | Binds proof to exact frozen policy version |
| `loan_hash` | Poseidon2 hash of all loan parameters (recomputed on-chain) |
| `nullifier_hash` | Prevents proof reuse across loans |

**What the circuit proves (private inputs stay off-chain):**
1. Borrower commitment: `Hash(secret ‖ revenue ‖ EBITDA ‖ net_worth ‖ age)` binds private data to proof
2. Attestation freshness: timestamp within `policy_max_attestation_age_days`
3. Underwriter Schnorr/Grumpkin signature over borrower data hash is valid
4. Policy scope hash matches all 21 policy parameter constraints
5. All eligibility, ratio, and tier constraints satisfied by private borrower data

Industry exclusion is verified on-chain in `LoanEngine` (dynamic list, cannot be embedded in a static circuit hash).

---

## Testing

Tested across four fuzz frameworks with 17 protocol-level invariants:

| Framework | Type | Coverage |
|---|---|---|
| Foundry (`forge test`) | Unit + Fuzz | Full lifecycle: create, activate, repay, default, write-off, recovery |
| Foundry Invariants | Stateful fuzz | 17 invariants, 18 handler actions |
| Echidna | Property-based fuzz | Economic invariants (value conservation, waterfall ordering) |
| Medusa | Stateful fuzz | Concurrent with Echidna for differential coverage |

**Key invariants tested:**
- Token balance == idle value + unclaimed interest (no value leak)
- Sum of loan outstanding principals == pool deployed value
- If senior shortfall > 0 → equity deployed value must be 0 (waterfall ordering)
- Interest index is monotonically non-decreasing
- REPAID and WRITTEN_OFF loans have zero outstanding principal and accrued interest

---

## Repository Structure

```
credit_rail/
├── circuits/                # Noir ZK circuit (UltraHonk, Barretenberg)
│   └── src/main.nr          # 3000+ line circuit with full test suite
├── contracts/               # Solidity (Foundry, zkSync-compatible)
│   ├── src/
│   │   ├── LoanEngine.sol       # Loan lifecycle, ZK proof verification
│   │   ├── TranchePool.sol      # Capital pool, waterfall accounting
│   │   ├── CreditPolicy.sol     # Versioned, immutable credit policies
│   │   └── interfaces/          # ILoanEngine, ITranchePool, ICreditPolicy
│   └── test/
│       ├── unit/                # Unit tests for all contracts
│       └── fuzz/
│           ├── invariant/       # Foundry stateful invariant tests + Handler
│           ├── echidna/         # Echidna configuration
│           └── medusa/          # Medusa configuration
├── economic-modelling/      # Python economic model + Monte Carlo simulations
│   └── model/               # state.py, flows.py, time.py
├── zk-scripts/              # TypeScript: proof generation, deployment, E2E tests
└── docs/                    # Architecture, threat model, ZK integration guide
```

---

## Quick Start

### Smart Contracts
```bash
cd contracts
forge install
forge build
forge test
```

### ZK Circuit
```bash
cd circuits
nargo check
nargo test       # Runs circuit unit tests
nargo compile    # Compiles to target/circuits.json
```

### Economic Model
```bash
cd economic-modelling
python3 -m venv venv && source venv/bin/activate
pip install numpy matplotlib
python3 scripts/simulate_scenario.py
```

### End-to-End (ZK proof → on-chain loan creation)
```bash
# Requires: anvil-zksync running on :8546
cd zk-scripts
npm install
npx tsx create_loan_simple.ts
```

---

## Documentation

| Doc | Contents |
|---|---|
| [`docs/overview.md`](./docs/overview.md) | High-level introduction, core components, tech stack |
| [`docs/architecture.md`](./docs/architecture.md) | System topology, call graph, role architecture |
| [`docs/circuits/circuit-design.md`](./docs/circuits/circuit-design.md) | ZK circuit internals, constraint taxonomy, Schnorr scheme |
| [`docs/ZK_PROOF_INTEGRATION.md`](./docs/ZK_PROOF_INTEGRATION.md) | E2E proof pipeline, Poseidon2 integration, deployment |
| [`docs/contracts/`](./docs/contracts/) | Per-contract deep dives (LoanEngine, TranchePool, CreditPolicy, ProtocolController, InterestMath) |
| [`docs/ECONOMIC_MODEL.md`](./docs/ECONOMIC_MODEL.md) | Waterfall math, interest accrual, stress test results |
| [`docs/testing.md`](./docs/testing.md) | Testing pyramid, all frameworks, invariant list, CI pipeline |
| [`docs/deployment.md`](./docs/deployment.md) | Step-by-step deployment guide, environment variables |
| [`docs/THREAT_MODEL.md`](./docs/THREAT_MODEL.md) | Trust boundaries, attack vectors, mitigations |
| [`docs/security/`](./docs/security/) | ZK circuit review, trust assumptions, invariant definitions |
| [`docs/DESIGN_TRADEOFFS.md`](./docs/DESIGN_TRADEOFFS.md) | 10 major architectural trade-offs with rationale |
| [`docs/V2_PROPOSAL.md`](./docs/V2_PROPOSAL.md) | V2 roadmap with code-level specs and migration strategy |
| [`docs/glossary.md`](./docs/glossary.md) | Term definitions for all stakeholders |
