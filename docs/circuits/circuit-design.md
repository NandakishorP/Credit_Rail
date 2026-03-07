# Circuit Design

The Credit Rail ZK circuit is implemented in Noir and compiled using the UltraHonk proving system. It is approximately 3,400 lines including a comprehensive test suite. The circuit serves as the cryptographic bridge between off-chain underwriting and on-chain loan origination — it proves that a borrower meets a frozen credit policy without revealing any of the underlying financial data on-chain.

---

## Public vs Private Inputs

The circuit has exactly **3 public inputs** (visible on-chain) and **47 private inputs** (never leave the prover's machine).

### Public Inputs

| Input | Description |
|---|---|
| `policy_version_hash` | Poseidon2 hash of all 21 policy parameters. Binds the proof to an exact frozen policy version. |
| `loan_hash` | Poseidon2 hash of loan terms + borrower commitment + underwriter key + loanId. Binds proof to a specific loan. |
| `nullifierHash` | Poseidon2 hash of (loanId, borrower_secret, principal, attestation_timestamp). Prevents proof replay. |

### Private Inputs (selected)

| Input | Category |
|---|---|
| `borrower_secret` | Commitment randomness |
| `borrower_annual_revenue`, `borrower_ebitda`, `borrower_tangible_net_worth`, `borrower_business_age_days` | Eligibility data |
| `borrower_debt_to_ebitda`, `borrower_interest_coverage`, `borrower_current_ratio`, `borrower_ebitda_margin_bps` | Financial ratios |
| `underwriter_sig_s_low`, `underwriter_sig_s_high`, `underwriter_sig_e` | Schnorr signature components |
| `attestation_timestamp` | When the underwriter signed |
| All 21 policy parameters | Policy constraints |

The private inputs are provided by the fund admin at proof generation time. The Noir circuit verifies them against each other and the public inputs — the prover must know the raw values to generate a valid proof, but the verifier (on-chain `HonkVerifier`) only ever sees the 3 public inputs and the proof bytes.

---

## Constraint Taxonomy

The circuit enforces six categories of constraints in sequence:

| Step | Name | What It Proves |
|---|---|---|
| 1 | Borrower Commitment | The private financial data matches the public `borrower_commitment` hash |
| 2 | Attestation Freshness | The attestation is not expired relative to `current_timestamp` |
| 3 | Underwriter Signature | The Schnorr/Grumpkin signature over the borrower data is valid for the underwriter's public key |
| 4 | Policy Version Integrity | The 21 private policy parameters hash to the public `policy_version_hash` |
| 5 | Policy Compliance | All eligibility, ratio, and tier constraints hold against the private borrower data |
| 6 | Loan Term Matching | The loan's APR, fee, and term exactly match the selected pricing tier |

A proof is only valid if all six steps pass simultaneously. The circuit cannot selectively skip any step.

---

## Borrower Commitment Scheme

The borrower commitment binds a subset of the borrower's financial data to the proof, without revealing it:

```
borrower_commitment = Poseidon2(
    borrower_secret,
    borrower_annual_revenue,
    borrower_ebitda,
    borrower_tangible_net_worth,
    borrower_business_age_days
)
```

**Why only 4 financial fields?**
The commitment captures the borrower's core eligibility data — the fields that define whether they qualify at all. The ratio fields (`debt_to_ebitda`, `interest_coverage`, etc.) are also verified inside the circuit but are not included in the commitment because they are derived metrics rather than identity-level facts. The commitment is a succinct, stable fingerprint of the borrower's financial standing.

**Why a secret?**
Without the `borrower_secret`, an attacker who knows the policy thresholds could brute-force the commitment by iterating through plausible revenue/EBITDA values and checking which combination produces the observed commitment hash. The secret is a 32-byte random field element that makes this infeasible.

---

## Nullifier Construction

```
nullifierHash = Poseidon2(loanId, borrower_secret, loan_principal, attestation_timestamp)
```

**Why these four fields?**

| Field | Why It's Needed |
|---|---|
| `loanId` | Binds the nullifier to a specific on-chain loan. Different loanIds produce different nullifiers. |
| `borrower_secret` | Cryptographically binds the nullifier to the borrower's private commitment entropy, making the nullifier un-forgeable and collision-resistant. |
| `loan_principal` | Binds the nullifier to the specific loan amount. Prevents reusing a proof for a different principal. |
| `attestation_timestamp` | Binds to the time of the underwriter attestation. Prevents using an old attestation for a new loan. |

**Important Architecture Note:**
In public ZK systems (like Tornado Cash), nullifier secrets prevent random mempool observers from computing the nullifier and frontrunning a transaction to grief the user. However, because Credit Rail's `createLoan` is heavily permissioned (`onlyRole(FUND_MANAGER_ROLE)`), public frontrunning is structurally impossible. 

Here, `borrower_secret` is included in the nullifier to prevent theoretical collision attacks and to ensure that the un-spendable tag (`s_nullifierHashes`) is inextricably linked to the borrower's 32-byte private entropy, not just public transaction parameters.

The `nullifierHash` is stored permanently on-chain in `LoanEngine.s_nullifierHashes` after first use.

---

## Schnorr Signature over Grumpkin

**Why Grumpkin instead of secp256k1?**

Grumpkin is the BN254 embedded curve — its scalar field matches the BN254 base field that Noir's backend (UltraHonk / Barretenberg) operates over. This means scalar multiplications on Grumpkin are native field operations inside the circuit.

secp256k1 (Ethereum's curve) has a different scalar field, requiring expensive non-native arithmetic inside the circuit — approximately 10x more constraints for the same signature verification. For a circuit with 40+ private inputs and 6 constraint categories, choosing Grumpkin over secp256k1 for the underwriter signature is a significant efficiency gain.

**How Schnorr verification works in the circuit:**

The Schnorr scheme used is the Fiat-Shamir transformed version:

```
Given: public key PK, message hash m, signature (s, e)

1. Decompose s into (s_low, s_high) — two 128-bit limbs forming one 256-bit scalar
2. Reconstruct R' = s·G + e·PK  via multi_scalar_mul
3. Recompute challenge: e' = Poseidon2(R'.x, R'.y, m)
4. Assert: e' == e
```

The off-chain signing in `grumpkin.ts` produces the `(s, e)` pair. The circuit reconstructs `R'` from the public key and verifies the challenge matches.

**Signature message:**
The underwriter signs a Poseidon2 hash of 12 fields:
- 4 eligibility values (`annual_revenue`, `ebitda`, `tangible_net_worth`, `business_age_days`)
- 4 ratio values (`defaults_last_36_months`, `has_bankruptcy`, `debt_to_ebitda`, `interest_coverage`)
- 2 additional metrics (`current_ratio`, `ebitda_margin_bps`)
- `industry_hash` (binding the attestation to a specific industry)
- `attestation_timestamp` (preventing replay of stale attestations)

The `borrower_secret` is deliberately **not** included in the signed message — the underwriter does not know the borrower's secret (it is the borrower's private randomness). The underwriter signs only the verifiable financial facts.

---

## Policy Hash Construction

The `policy_version_hash` is computed inside the circuit as:

```
Poseidon2([
    policy_min_annual_revenue,
    policy_min_ebitda,
    policy_min_tangible_net_worth,
    policy_min_business_age_days,
    policy_max_defaults_36_months,
    policy_bankruptcy_excluded,
    policy_max_debt_to_ebitda,
    policy_min_interest_coverage,
    policy_min_current_ratio,
    policy_min_ebitda_margin_bps,
    policy_max_attestation_age_days,
    tier_id,
    tier_min_revenue,
    tier_max_revenue,
    tier_min_ebitda,
    tier_max_debt_to_ebitda,
    tier_max_loan_to_ebitda,
    tier_interest_rate_bps,
    tier_origination_fee_bps,
    tier_term_days,
    tier_active
], 21)
```

This must match the `policyScopeHash` stored on-chain for the referenced policy version. If any single parameter differs, the hash will not match and the proof will be invalid.

---

## The On-chain / Off-chain Split for Industry Exclusion

The excluded industry list is checked on-chain in `LoanEngine.createLoan()` rather than inside the Noir circuit.

**Why?**

The primary reason is how the data is structured. The 21 standard policy parameters are singular values that can be easily combined into a single, unified `policy_version_hash`. 

However, a policy can have multiple excluded industries. In `CreditPolicy.sol`, these are stored in a mapping: `mapping(uint256 => mapping(bytes32 => bool))`. 

Because different excluded industries have different distinct hashes, there is no clean way to combine a dynamic number of industry hashes into the single `policy_version_hash` without changing the fundamental design of the hash (e.g., you can't just hash a dynamic Solidity mapping inside a fixed-length Noir Poseidon array). 

If you tried to include them, you would either need to artificially limit the number of excluded industries (to fit a fixed-size array) or store multiple different policy hashes on-chain for the same policy version.

Instead, the simplest and most elegant solution is to have the circuit take the borrower's `industry_hash` as a public input, binding it cryptographically to the underwriter's signature. Then, the on-chain verifier (`LoanEngine.sol`) simply checks if that specific `industry_hash` is marked as `true` in the `CreditPolicy`'s exclusion mapping.

---

## Fixed-Point Arithmetic Conventions

Because ZK circuits (and Solidity) have no floating-point numbers, all fractional values use fixed-point integer scaling. The circuit uses two different scaling conventions depending on the variable's role:

| Convention | Scale Factor | Example | Used For |
|---|---|---|---|
| **Basis Points (1e4)** | 10,000 | 3.5x → `35,000` | Static comparison ratios (`debt_to_ebitda`, `interest_coverage`, `current_ratio`, `ebitda_margin_bps`, APR, fees) |
| **1e3 Fixed-Point** | 1,000 | 3.5x → `3,500` | Generative multiplier (`tier_max_loan_to_ebitda`) |

**Why two conventions?**

Basis point ratios (1e4) are only ever used for direct comparisons inside the circuit (e.g., `assert(borrower_debt_to_ebitda <= tier_max_debt_to_ebitda)`). They never participate in multiplication against monetary values, so 4 decimal places of precision is sufficient and matches TradFi conventions.

`tier_max_loan_to_ebitda` is different — it is multiplied against `borrower_ebitda` to compute the maximum allowed loan amount. Its scaling must be chosen so that the cross-multiplication fits within `u64` bounds:

```
loan_principal * 1,000 <= borrower_ebitda * tier_max_loan_to_ebitda
```

**Overflow analysis** (all monetary inputs capped at < 1e15 by `MAX_MONETARY_VALUE`):
- Left side max: `1e15 * 1,000 = 1e18` (fits `u64`, max ~1.84e19)
- Right side max: `1e15 * 10,000 = 1e19` (fits `u64`, max ~1.84e19)

The 1e3 convention provides 3 decimal places of ratio precision (e.g., 3.567x = `3,567`), which is more than sufficient for institutional loan-to-EBITDA limits. The values never interact with ERC20 token math in Solidity — the `CreditPolicy.sol` contract only stores and hashes them — so the standard DeFi WAD (1e18) precision is unnecessary.

---

## Test Coverage

The circuit ships with 78 test functions (~2,400 lines) in `src/main.nr`. Test categories:

| Category | Examples |
|---|---|
| Valid compliance | Happy path with all parameters in bounds |
| Eligibility failures | Revenue below minimum, EBITDA below minimum, bankruptcy excluded |
| Ratio failures | Debt-to-EBITDA too high, interest coverage too low |
| Tier failures | Revenue outside tier bounds, wrong APR, wrong term |
| Signature failures | Invalid signature, zero public key |
| Commitment failures | Mismatched borrower data vs commitment hash |
| Attestation expiry | Timestamp outside maximum age window |

All failure tests use `#[test(should_fail_with = "exact error message")]` assertions.

---

## How to Run

**Compile:**
```bash
cd circuits
nargo compile
```

**Run tests:**
```bash
nargo test
```

**Generate a proof (requires a populated Prover.toml):**
```bash
nargo prove
```

**Verify a proof locally:**
```bash
nargo verify
```

The compiled circuit artifact is output to `circuits/target/circuits.json`. This file is consumed by the TypeScript proof generation scripts in `zk-scripts/`.

For the full proof generation pipeline including on-chain submission, see [`ZK_PROOF_INTEGRATION.md`](../ZK_PROOF_INTEGRATION.md).
