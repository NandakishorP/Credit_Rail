## Credit Rail Smart Contracts

This directory contains the core smart contract suite for the Credit Rail protocol, built using [Foundry](https://book.getfoundry.sh/). 

The architecture is deliberately segmented to maintain strict boundaries between identity checks, risk management, and capital allocation.

### Core Contracts (`src/`)

1. **`LoanEngine.sol`**: The primary entry point. Orchestrates the creation, activation, repayment, and write-off of loans. It handles zero-knowledge proof verification natively using the imported Noir `LoanProofVerifier`.
2. **`TranchePool.sol`**: The capital vault. Manages LP deposits across three risk tiers (Senior, Junior, Equity) and runs the complex arithmetic for interest distribution and loss absorption waterfalls. Contains the core logic for the share-based `Global Claim Index` (so it handles mass distribution at O(1) gas).
3. **`CreditPolicy.sol`**: A registry of active and historical lending criteria (e.g., maximum concentrations, specific banned industries, coverage ratios). Its defining role is supplying the unalterable `policyScopeHash` against which the zero-knowledge circuits restrict borrower proofs.

### Helper Math Library 
- **`InterestMath.sol`**: Centralized library avoiding re-computation across the stack. Calculations include `accrueTargetInterest`, `calculateClaimable`, and `computeIndexDelta`.

---

## Setup & Testing

Foundry handles the EVM testing suite, compiling both standard deterministic logic and fuzzing/invariant checking. We leverage an embedded ZKSync compiler due to the ultimate deployment target requiring native account abstraction and high-throughput zero-knowledge environments.

### 1. Build

You must install dependencies (`forge install`) before building. We execute builds using the `--zksync` flag to ensure compatibility with EraVM:

```shell
$ forge build --zksync
```

### 2. State-Based Invariant Fuzzing

Due to the complexity of the Senior/Junior/Equity capital waterfall and math rounding, simple static unit tests are insufficient. The suite heavily relies on stateful invariant tests (`test/fuzz/invariant/CreditRailStateFullFuzzTest.t.sol`).

Run the standard test suite:
```shell
$ forge test --zksync
```

*Note: The `Echidna` and `Medusa` test contracts are designed exclusively for their respective offline analysis engines and may fail gracefully in the standard Foundry runner.*

### 3. Formatting

Enforce style using the built-in formatter:

```shell
$ forge fmt
```
