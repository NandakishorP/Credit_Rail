# Credit Rail

**Credit Rail** is an institutional-grade, zero-knowledge powered private credit protocol. It provides a secure, fully on-chain accounting rail for managing credit funds, structured with multi-tranche capital pools (Senior, Junior, Equity) and programmatic credit policies enforced via ZK proofs.

Built for the exact needs of real-world asset (RWA) and private credit originators, the system separates the *public* verification of loan criteria from the *private* borrower data (like PII, bank statements, and business relationships) using Noir-based zero-knowledge circuits.

## Core Features

- **Privacy-Preserving Origination**: Uses ZK-SNARKs (via [Noir](https://noir-lang.org/)) to mathematically prove that a borrower meets a fund’s strict `CreditPolicy` (e.g., Debt-Service Coverage Ratio limits, excluded industries) without leaking sensitive, plaintext financials on-chain.
- **Structured Finance Tranching**: The `TranchePool` manages LP capital in a standard structured finance methodology:
  - **Senior Tranche**: Lowest risk, first to be paid interest, last to take losses.
  - **Junior Tranche**: Medium level of risk and returns.
  - **Equity Tranche**: High upside, but absorbs the first wave of defaults and losses.
- **Immutable Credit Policies**: Underwriters construct versioned `CreditPolicy` contracts. A snapshot (hash) of this policy is baked into the Noir circuit. If the fund manager attempts to originate a loan that violates the active policy, the ZK proof simply fails.
- **Robust Economic Engine**: A standalone Python-based economic model (`economic-modelling`) mirrors the smart contract flow. This enables 10-year Monte Carlo simulations of the exact interest math, waterfall distribution, and insolvency thresholds utilized on-chain.

## Repository Structure

The repository is structured to separate concerns between business logic, zero-knowledge proving, and off-chain modeling:

- `contracts/`: The Solidity smart contract suite (Foundry) governing the fund accounting and loan state machine.
- `circuits/`: The Noir circuits for generating and verifying zero-knowledge proofs of credit policy adherence.
- `economic-modelling/`: Python engine to test the mathematical safety of the waterfall, loss distributions, and yield targets.
- `zk-scripts/`: TypeScript wrappers to tie the Noir circuits to the Solidity engine.

## Documentation

For a deeper technical understanding of the protocol internals, refer to the `docs/` folder:

- [**System Architecture**](./docs/ARCHITECTURE.md): An overview of how the smart contracts interact with the ZK verifier and off-chain clients.
- [**Economic Model**](./docs/ECONOMIC_MODEL.md): A detailed breakdown of the math governing the interest and loss waterfalls across tranches.
- [**ZK Proof Integration**](./docs/ZK_PROOF_INTEGRATION.md): How borrower data is blinded, hashed, and verified on-chain.

## Quick Start

### 1. Smart Contracts
The `contracts/` directory uses Foundry and builds for evm as well as ZKsync.
```bash
cd contracts
forge install
forge build --zksync
forge test --zksync
```

### 2. ZK Proofs
The circuits are written in Noir. Make sure you have Nargo installed.
```bash
cd circuits
nargo check
```

### 3. Economic Modeling
Run the Python simulations to verify mathematical invariants.
```bash
cd economic-modelling
source venv/bin/activate
pip install -r requirements.txt
python3 -m pytest tests/
```
