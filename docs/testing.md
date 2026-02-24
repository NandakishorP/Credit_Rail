# Testing

Credit Rail uses a layered testing strategy across five frameworks. Each layer covers a different failure class. No single layer is sufficient on its own.

---

## Testing Pyramid

```
                      ┌─────────────┐
                      │   E2E / ZK  │   ← zk-scripts/ + Python model
                      └──────┬──────┘
                   ┌─────────┴─────────┐
                   │   Property-Based   │   ← Echidna, Medusa
                   └────────┬──────────┘
              ┌─────────────┴─────────────┐
              │     Invariant / Stateful   │   ← Foundry invariant + Handler
              └──────────────┬────────────┘
         ┌────────────────────┴────────────────────┐
         │              Unit Tests                  │   ← Foundry unit tests
         └──────────────────────────────────────────┘
```

The higher the layer, the fewer tests there are, but the higher the confidence in system-level correctness.

---

## Unit Tests

Located in `contracts/test/unit/`. Eight files targeting each contract and feature area:

| File | What It Tests |
|---|---|
| `TestTranchePool.t.sol` | Core deposit, withdrawal, share minting, pool state transitions |
| `TestTranchePool_Deposits.t.sol` | Deposit edge cases: zero amounts, wrong state, whitelist enforcement |
| `TestTranchePool_Withdrawals.t.sol` | Withdrawal edge cases: insufficient shares, wrong state |
| `TestTranchePool_Allocation.t.sol` | Capital allocation algorithm, overflow absorption, tranche split ratios |
| `TestTranchePool_Lifecycle.t.sol` | Repayment waterfall, loss waterfall, recovery waterfall, admin setters |
| `TestTranchePoolBase.t.sol` | Shared test harness and helpers used by all TranchePool tests |
| `TestCreditPolicy.t.sol` | Policy CRUD, freeze mechanics, tier management, industry exclusion |
| `TestLoanEngineComplete.t.sol` | Full loan lifecycle using mock verifier and mock Poseidon2 |

**What unit tests catch:** Incorrect state transitions, wrong arithmetic in individual functions, access control violations, wrong events emitted.

**What unit tests miss:** Interaction bugs between contracts, emergent behaviour from unexpected operation ordering, conservation law violations under adversarial sequencing.

**How to run:**
```bash
cd contracts
forge test --match-path "test/unit/**" -v
```

---

## Invariant / Stateful Fuzzing (Foundry)

Located in `contracts/test/fuzz/invariant/`.

| File | Role |
|---|---|
| `Handler.t.sol` | Drives all state transitions against real contracts; maintains ghost variables |
| `CreditRailStateFullFuzzTest.t.sol` | Declares all invariants; Foundry calls them after every random handler action |
| `EchidnaCreditRailTest.sol` | Lightweight Echidna adapter over the same invariants |

**How the handler works:**

The handler holds all required roles (`UNDERWRITER_ROLE`, `SERVICER_ROLE`, etc.) and calls every protocol function in bounded-random order. It maintains ghost variables (e.g., `outstandingPrincipal`, `totalDeposited`) that track expected system state. Invariants compare real on-chain storage against ghost expectations.

**What invariant tests catch:** Conservation law violations, accounting drift between contracts, edge cases at zero liquidity, interactions that unit tests cannot predict.

**How to run:**
```bash
forge test --match-path "test/fuzz/invariant/**" --fuzz-runs 10000 -v
```

For the full invariant list, see [`security/invariants.md`](./security/invariants.md).

---

## Echidna (Property-Based Fuzzing)

Located in `contracts/test/fuzz/echidna/`.

| File | Role |
|---|---|
| `EchidnaTest.sol` | Echidna-compatible property declarations |
| `EchidnaHandler.sol` | State-driving handler for Echidna corpus |
| `echidna.yaml` | Echidna configuration (runs, timeout, corpus directory) |

Echidna uses corpus-based mutation to explore the state space. It is particularly effective at finding violations that require a specific sequence of operations to trigger.

**How to run:**
```bash
cd contracts/test/fuzz/echidna
echidna EchidnaTest.sol --config echidna.yaml --contract EchidnaTest
```

---

## Medusa (Coverage-Guided Stateful Fuzzing)

Located in `contracts/test/medusa/`.

| File | Role |
|---|---|
| `MedusaTest.sol` | Medusa-compatible stateful property harness (27K bytes) |

Medusa uses coverage-guided mutation — it tracks which new code paths each mutation exercises and prioritises mutations that discover new paths. More effective than random fuzzing for deeply nested state machines.

**How to run:**
```bash
medusa fuzz --target contracts/test/medusa/MedusaTest.sol
```

---

## Python Economic Model

Located in `economic-modelling/`.

The Python model is a **conservation law validator** — it implements the same waterfall logic as the Solidity contracts in pure Python and mathematically verifies that all conservation laws hold across thousands of simulation paths before the invariants were encoded in Solidity.

| File | Role |
|---|---|
| `model/state.py` | `SystemState`, `TrancheState`, `LoanState` dataclasses |
| `model/flows.py` | `allocate_capital`, `repay_loan`, `apply_loss`, `on_recovery` |
| `model/time.py` | `accrue_loan_interest` |
| `verify_inferences.py` | Runs conservation law assertions across simulation paths |
| `simulate_scenario.py` | Multi-scenario Monte Carlo stress testing |
| `visualize_stress_test.py` | Matplotlib visualisation of stress test results |

**What it validates:**
- `Idle + Deployed = Deposited - Loss + Recovered` holds after every operation
- Interest waterfall distributes correctly in all ordering combinations
- Recovery exactly undoes loss when full recovery occurs

**How to run:**
```bash
cd economic-modelling
python verify_inferences.py
python simulate_scenario.py
```

---

## ZK Circuit Tests

Located in `circuits/src/main.nr` (approximately 2,400 lines of test code).

The Noir circuit ships with tests covering:
- Valid compliance (happy path with all parameters in bounds)
- Every eligibility failure (revenue, EBITDA, net worth, age, defaults, bankruptcy)
- Every ratio failure (debt-to-EBITDA, interest coverage, current ratio, margin)
- Every tier failure (revenue outside bounds, wrong APR, wrong term, wrong fee)
- Signature failures (invalid signature, mismatched public key)
- Commitment failures (tampered private data does not match commitment hash)
- Attestation expiry (timestamp outside maximum age window)

All failure tests use `#[test(should_fail_with = "exact error message")]`.

**How to run:**
```bash
cd circuits
nargo test
```

---

## CI Pipeline

`.github/workflows/tests.yml` runs on every push to `main`:

```yaml
- forge build --zksync          # Compile all contracts
- forge test --match-path "test/unit/**"   # Run unit tests
```

**What CI does not currently run:**
- Invariant fuzzing (too slow for CI; run manually)
- Echidna / Medusa (requires separate installation)
- Noir circuit tests (requires Noir toolchain in CI environment)
- ZK proof generation E2E (requires anvil-zksync)

For a complete test run before production deployment, all layers should be executed locally.

---

## Mocks

Two mock contracts are used exclusively in unit tests to avoid ZK and Poseidon2 dependencies:

| Mock | What It Replaces | Behaviour |
|---|---|---|
| `MockLoanProofVerifier` | `HonkVerifier` | Always returns `true` — assumes proof validity |
| `MockPoseidon2` | `Poseidon2` | `keccak256`-based hash — deterministic but not ZK-compatible |

These mocks are never deployed in integration or production environments.
