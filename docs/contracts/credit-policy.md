# CreditPolicy

The `CreditPolicy` contract is an immutable-by-version registry of fund risk parameters. It defines the criteria a borrower must meet, the pricing tiers available, and the industries excluded from lending — all versioned and frozen before any loan can be originated against them.

---

## Policy Lifecycle

Every policy version follows a strictly one-directional state machine:

```
ACTIVE → FROZEN → INACTIVE
ACTIVE → INACTIVE
```

| State | Mutable | Can Originate Loans | Can Be Reactivated |
|---|---|---|---|
| `ACTIVE` | ✅ | ❌ | N/A |
| `FROZEN` | ❌ | ✅ | ❌ |
| `INACTIVE` | ❌ | ❌ | ❌ |

- **ACTIVE:** The policy is being configured. Parameters can be added or updated by the `policyAdmin`.
- **FROZEN:** All parameters are locked permanently. `LoanEngine` can only accept ZK proofs that reference a frozen policy's `policyScopeHash`. This is the canonical state for loan origination.
- **INACTIVE:** The policy is deprecated. No proofs referencing it will be accepted. Cannot be reversed.

Once a policy is frozen, it can never be modified — not even by the `policyAdmin`. This is an intentional, hard constraint: the rules a loan was underwritten under are permanently on-chain.

---

## Struct Taxonomy

A policy version is composed of six independent structs, each updated via a separate function:

### `EligibilityCriteria`
Minimum thresholds a borrower must meet to qualify for any loan under this policy.

| Field | Type | Description |
|---|---|---|
| `minAnnualRevenue` | `uint256` | Minimum annual revenue (in stablecoin units) |
| `minEBITDA` | `uint256` | Minimum EBITDA |
| `minTangibleNetWorth` | `uint256` | Minimum tangible net worth |
| `minBusinessAgeDays` | `uint256` | Minimum age of the business in days |
| `maxDefaultsLast36Months` | `uint256` | Maximum number of credit defaults in the past 36 months |
| `bankruptcyExcluded` | `bool` | Whether borrowers with any bankruptcy history are excluded |

### `FinancialRatios`
Ratio-based underwriting constraints, scaled by `1e4` for precision.

| Field | Type | Description |
|---|---|---|
| `maxTotalDebtToEBITDA` | `uint256` | Maximum debt/EBITDA ratio (e.g., 40000 = 4.0x) |
| `minInterestCoverageRatio` | `uint256` | Minimum EBIT/interest expense (e.g., 15000 = 1.5x) |
| `minCurrentRatio` | `uint256` | Minimum current assets/current liabilities (e.g., 12000 = 1.2x) |
| `minEBITDAMarginBps` | `uint256` | Minimum EBITDA margin in basis points (e.g., 1000 = 10%) |

### `LoanTier`
A pricing band that defines loan terms for a specific segment of borrowers. A policy can have multiple active tiers.

| Field | Type | Description |
|---|---|---|
| `name` | `string` | Human-readable tier name |
| `minRevenue` | `uint256` | Minimum annual revenue to qualify |
| `maxRevenue` | `uint256` | Maximum annual revenue ceiling |
| `minEBITDA` | `uint256` | Minimum EBITDA for this tier |
| `maxDebtToEBITDA` | `uint256` | Tier-specific max leverage (may be tighter than policy-wide) |
| `maxLoanToEBITDA` | `uint256` | Maximum loan principal as a multiple of EBITDA (1e18 scale) |
| `interestRateBps` | `uint256` | Fixed APR for this tier in basis points |
| `originationFeeBps` | `uint256` | One-time origination fee in basis points |
| `termDays` | `uint256` | Loan term in days |
| `active` | `bool` | Whether this tier is currently accepting new loans |

### `ConcentrationLimits`
Portfolio-level risk limits.

| Field | Type | Description |
|---|---|---|
| `maxSingleBorrowerBps` | `uint256` | Maximum exposure to any single borrower (basis points of pool) |
| `maxIndustryConcentrationBps` | `uint256` | Maximum exposure to any single industry (basis points of pool) |

> Note: Concentration limits are informational constraints enforced off-chain by the fund administrator. They are stored on-chain for auditability but are not checked programmatically in `LoanEngine`.

### `AttestationRequirements`
Requirements for how fresh and frequent underwriter attestations must be.

| Field | Type | Description |
|---|---|---|
| `maxAttestationAgeDays` | `uint256` | Maximum age of an underwriter attestation before it expires |
| `reAttestationFrequencyDays` | `uint256` | How frequently re-attestation is required for ongoing loans |
| `requiresCPAAttestation` | `bool` | Whether a CPA-audited financial statement is required |

### `MaintenanceCovenants`
Ongoing obligations for borrowers during the loan term.

| Field | Type | Description |
|---|---|---|
| `maxLeverageRatio` | `uint256` | Maximum ongoing leverage ratio |
| `minCoverageRatio` | `uint256` | Minimum ongoing coverage ratio |
| `minLiquidityAmount` | `uint256` | Minimum cash/liquid assets to maintain |
| `allowsDividends` | `bool` | Whether borrower is permitted to pay dividends during the loan |
| `reportingFrequencyDays` | `uint256` | How often the borrower must submit financial reports |

> Note: Maintenance covenants are enforced off-chain by the servicer. Breach triggers a discretionary `declareDefault()` call.

---

## `policyScopeHash`

When a policy is frozen, the contract computes a Poseidon2 hash of **21 policy parameters** and stores it as `policyScopeHash[version]`.

The 21 parameters hashed are:
1. `policy_min_annual_revenue`
2. `policy_min_ebitda`
3. `policy_min_tangible_net_worth`
4. `policy_min_business_age_days`
5. `policy_max_defaults_36_months`
6. `policy_bankruptcy_excluded`
7. `policy_max_debt_to_ebitda`
8. `policy_min_interest_coverage`
9. `policy_min_current_ratio`
10. `policy_min_ebitda_margin_bps`
11. `policy_max_attestation_age_days`
12. `tier_id`
13. `tier_min_revenue`
14. `tier_max_revenue`
15. `tier_min_ebitda`
16. `tier_max_debt_to_ebitda`
17. `tier_max_loan_to_ebitda`
18. `tier_interest_rate_bps`
19. `tier_origination_fee_bps`
20. `tier_term_days`
21. `tier_active`

This hash is the public input `policy_version_hash` embedded in every ZK proof. During `createLoan()`, the `LoanEngine` calls `CreditPolicy.policyScopeHash(policyVersion)` and checks that it matches the proof's public input. If the policy parameters were ever changed after the proof was generated, the hash would not match and the transaction would revert.

This binding makes it impossible to accept a proof generated against one set of risk parameters while a different set is now active.

---

## Industry Exclusion

Specific industry codes can be excluded from a policy version. Excluded industries are stored as a mapping from an industry hash to a boolean:

```solidity
mapping(uint256 version => mapping(bytes32 industryHash => bool)) public excludedIndustries;
```

Industry exclusion is **checked on-chain in `LoanEngine`**, not inside the ZK circuit. This is an intentional architectural decision: the exclusion list can change dynamically (new industries can be excluded without requiring a new frozen policy), but the ZK proof is locked to a specific static policy hash. Checking exclusions on-chain separates the static (frozen) underwriting parameters from the dynamic (operational) exclusion list.

---

## `policyAdmin` and Production Setup

`CreditPolicy` has a single `policyAdmin` address that can create, configure, and freeze policy versions.

In development, `policyAdmin` is the deployer. In production, it should be set to the `ProtocolController` address:

```bash
creditPolicy.transferAdmin(address(protocolController));
```

This means every policy update — even creating a new version — passes through the `ProtocolController`'s timelock delay, giving LPs a window to review and exit before new risk parameters take effect.

See [`protocol-controller.md`](./protocol-controller.md) for the governance setup.
