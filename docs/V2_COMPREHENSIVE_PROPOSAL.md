# Credit Rail V2 — Comprehensive Architecture Proposal

> **Last Updated:** March 13, 2026
> **Status:** Proposal (Not Implemented)
> **Scope:** Full system — Noir ZK Circuit, Solidity Smart Contracts, Off-Chain Infrastructure, Protocol Positioning
> **Prerequisites:** V1 contracts audited and deployed; operational feedback from at least one full loan lifecycle
> **Related Docs:** [V2_PROPOSAL.md](./V2_PROPOSAL.md) · [DESIGN_TRADEOFFS.md](./DESIGN_TRADEOFFS.md) · [THREAT_MODEL.md](./THREAT_MODEL.md) · [ARCHITECTURE.md](./ARCHITECTURE.md) · [security/zk-circuit-review.md](./security/zk-circuit-review.md)

---

## Preamble

The existing [V2 Proposal](./V2_PROPOSAL.md) (P1.1–P3.5) focuses on fixing known V1 limitations: the sequential `loanId` race condition, cross-chain replay, borrower identity binding, capital reservation, multi-servicer confirmation, and feature expansions like tradable tranche shares and recursive proof aggregation.

This document goes deeper. It provides a critical architectural assessment of V1's structural constraints, proposes ten new features (P4.1–P4.10), maps the competitive landscape, defines the V2 contract topology, charts the ZK circuit evolution path, and lays out a prioritized 12-month roadmap. The goal is to transform Credit Rail from a single-fund prototype into **private credit infrastructure** — a platform for launching, managing, and composing institutional credit funds on-chain.

---

## Table of Contents

1. [Part 1 — Critical Architecture Assessment](#part-1--critical-architecture-assessment)
2. [Part 2 — Novel V2 Proposals (P4.1–P4.10)](#part-2--novel-v2-proposals-p41p410)
3. [Part 3 — Competitive Differentiation Strategy](#part-3--competitive-differentiation-strategy)
4. [Part 4 — V2 Contract Architecture](#part-4--v2-contract-architecture)
5. [Part 5 — ZK Circuit Evolution](#part-5--zk-circuit-evolution)
6. [Part 6 — Prioritized Implementation Roadmap](#part-6--prioritized-implementation-roadmap)

---

## Part 1 — Critical Architecture Assessment

The existing V2 proposal addresses circuit-level bugs (P1.1–P1.3) and operational improvements (P2.1–P2.3). These are necessary but insufficient. The deeper structural issues below constrain Credit Rail's ability to scale, attract institutional capital, and differentiate from competitors.

### 1.1 Monolithic Pool Architecture

**The Problem:** The entire protocol is 1:1:1 — one `LoanEngine`, one `TranchePool`, one `CreditPolicy` per deployment. The `loanEngine` address is hardcoded in `TranchePool` (set once via `setLoanEngine()`), the `i_tranchePool` is an immutable reference in `LoanEngine`, and the stablecoin address is fixed at initialization.

**The Consequence:** A fund manager who wants to run two strategies — say, an SME working capital fund at 12% target APR and a Special Situations distressed fund at 20% — must deploy the entire contract stack twice. No shared infrastructure: no shared LP whitelists, no shared underwriter keys, no shared CreditPolicy registry, no shared ProtocolController. The operational complexity scales linearly with the number of strategies, and there is no unified view of total AUM or cross-fund risk.

**Why This Matters:** Institutional asset managers typically run multiple strategies under a single platform. BlackRock doesn't deploy separate infrastructure for each fund. The monolithic deployment model limits Credit Rail to single-strategy operators, excluding the multi-strategy funds that represent the largest pool of institutional capital.

### 1.2 Static Tranche Ratios

**The Problem:** The capital allocation factors (`s_capital_allocation_factor_senior` and `s_capital_allocation_factor_junior`) are global parameters on `TranchePool`. Every loan, regardless of risk tier, draws the same ratio from each tranche — by default 80% from Senior, 15% from Junior, and 5% from Equity.

**The Consequence:** A Tier 0 loan (low-risk, low-APR borrower with strong financials) gets the same 80/15/5 split as a Tier 3 loan (higher-risk, higher-APR borrower at the policy's outer bounds). This contradicts how real structured credit works. In a traditional CLO, riskier loan tranches draw proportionally more from junior and equity capital to maintain the senior tranche's credit enhancement. A uniform ratio either over-protects seniors on safe loans (reducing their yield) or under-protects them on risky loans (increasing their loss exposure).

**Why This Matters:** Sophisticated LPs — the kind who invest in structured credit — will immediately notice that the overcollateralization ratio doesn't vary by credit quality. This is a red flag for any institutional allocator familiar with real CLO structures.

### 1.3 Dead Capital Problem

**The Problem:** Once the pool transitions from `OPEN` to `COMMITTED`, all idle capital is frozen. LPs cannot deposit, withdraw, or rebalance. If the fund manager only deploys 60% of pool capital to loans, the remaining 40% sits idle earning exactly zero yield, with no mechanism for LPs to reclaim it until the pool transitions to `CLOSED`.

**The Consequence:** Capital efficiency depends entirely on the fund manager's ability to originate loans that fill the pool. In a real market with uneven deal flow, pools will routinely have 20-40% idle capital for extended periods. This capital earns nothing and is completely illiquid — a devastating proposition for institutional LPs who have alternatives earning 5%+ risk-free in traditional money markets.

**Why This Matters:** Capital efficiency is the single most important metric for institutional LP adoption. A protocol that locks capital without guaranteed deployment will lose to competitors that offer flexible entry/exit.

### 1.4 All-or-Nothing Pool Lifecycle

**The Problem:** The linear state machine (`OPEN → COMMITTED → DEPLOYED → CLOSED`) treats the pool as a monolithic unit. You cannot add new LPs to a `DEPLOYED` pool even if it has idle capacity. You cannot close one segment while keeping another active. You cannot process partial withdrawals during deployment.

**The Consequence:** This models a closed-end fund with a fixed commitment period. While valid for some strategies, the institutional market has moved heavily toward open-ended and evergreen fund structures. An LP who wants to invest in Credit Rail 6 months after the pool commits must wait for the next vintage. This limits the total addressable capital to what can be raised in a single commitment window.

**Why This Matters:** Open-ended fund structures represent over 60% of institutional private credit AUM globally. A closed-end-only model excludes the majority of the market.

### 1.5 Interest Model Coupling Risk

**The Problem:** Two independent interest accrual mechanisms run in parallel. `LoanEngine._accrueInterest()` computes per-loan interest at the loan's APR. `TranchePool._accrueTrancheTargets()` independently computes tranche-level target interest at the tranche's configured APR. These are loosely coupled — the tranche targets accrue based on deployed capital and time, while loan interest accrues based on outstanding principal and time.

**The Consequence:** If the portfolio's weighted average loan APR is lower than the senior tranche's target APR (e.g., the fund originates mostly Tier 0 loans at 8% but promises seniors 10%), the tranche targets will grow faster than actual interest income. This creates a phantom yield obligation that can only be resolved by equity absorbing the shortfall — but this shortfall is not explicitly tracked or surfaced anywhere.

**Why This Matters:** Silent yield gaps erode equity returns and create accounting discrepancies that would be caught in any institutional audit. The system should either enforce that tranche target APRs are always achievable given the loan book, or explicitly track and report the yield gap.

### 1.6 No On-Chain Portfolio Analytics

**The Problem:** Loans are stored in a flat `mapping(uint256 => Loan)` with a sequential counter (`s_nextLoanId`). There are no aggregate tracking structures — no count of active loans by tier, no exposure tracking per `borrowerCommitment`, no weighted average APR, no average maturity, no distribution of loan states.

**The Consequence:** Any portfolio-level query requires iterating all loans off-chain by replaying events. The `invariant__systemLevel_PrincipalIntegrity` test in the fuzzing suite already demonstrates this by looping through every loan ID. At 1,000 loans, this becomes expensive; at 10,000, impractical. More critically, there is no on-chain mechanism for LPs to verify portfolio composition without trusting off-chain reporting.

**Why This Matters:** Institutional LPs require regular portfolio reporting — NAV calculations, concentration analysis, duration profiles, default rates. Without on-chain analytics, all reporting becomes an off-chain trust assumption, undermining the transparency guarantees that blockchain-based lending is supposed to provide.

### 1.7 Origination Fee Leakage

**The Problem:** When `activateLoan()` is called, the origination fee is transferred directly to a `feeManager` address via `IERC20.safeTransfer()` inside `TranchePool.allocateCapital()`. This fee leaves the system entirely — it is not tracked as pool revenue, not distributed to LPs, and not recorded in any internal accounting variable.

**The Consequence:** LPs have no share in origination fee income. The only revenue that accrues to the pool is interest payments and the overflow that becomes `s_protocolRevenue` (which only occurs when there are zero equity holders). For a fund charging 2% origination fees on a $10M pool, that's $200K of revenue that bypasses the waterfall entirely.

**Why This Matters:** In traditional structured credit, origination fees are typically split between the manager (as an incentive) and the fund (as enhanced return to investors). A 100% extraction by the manager is unusual and makes the LP economics less attractive.

### 1.8 No Reinvestment Mechanism

**The Problem:** When a loan is repaid, principal returns to the pool's `idleValue`. But there is no mechanism to automatically redeploy that capital into new loans. The fund manager must manually generate a new ZK proof (5-15 seconds), submit `createLoan()`, and then call `activateLoan()` — a minimum of two transactions and significant off-chain coordination.

**The Consequence:** Between loan repayment and redeployment, capital sits idle earning nothing. For a fund with 40 loans on 90-day terms, approximately one loan repays every 2-3 days. If redeployment takes 24-48 hours of operational lag, the fund has a perpetual drag of 1-3% idle capital even in steady state.

**Why This Matters:** Every day of idle capital reduces the fund's net yield. At institutional scale, a 1% drag on a $50M pool is $500K/year of missed return.

### 1.9 Unenforced Policy Sections

**The Problem:** `CreditPolicy.sol` defines two struct categories that are never enforced anywhere:

1. **`ConcentrationLimits`** — `maxSingleBorrowerBps` and `maxIndustryConcentrationBps` are stored on-chain but never checked in `LoanEngine.createLoan()` or `activateLoan()`. There is no tracking of cumulative exposure per borrower or industry.

2. **`MaintenanceCovenants`** — `maxLeverageRatio`, `minCoverageRatio`, `minLiquidityAmount`, `allowsDividends`, and `reportingFrequencyDays` are stored but never referenced by any contract logic.

**The Consequence:** These policy sections create a false sense of security. An LP reviewing the `CreditPolicy` might believe that concentration limits and covenants are enforced, when in reality they are purely informational. The ZK circuit proves that borrower financials meet eligibility criteria at origination time, but there is no ongoing enforcement or monitoring.

**Why This Matters:** Concentration risk is the number one killer in private credit. A single borrower taking 80% of the pool and defaulting would wipe out even the senior tranche. Without enforcement, the policy's concentration limits are aspirational documentation, not hard constraints.

---

## Part 2 — Novel V2 Proposals (P4.1–P4.10)

These proposals address the structural gaps identified in Part 1 and introduce new capabilities that extend Credit Rail beyond a single-fund lending tool into a composable private credit platform.

> **Numbering Convention:** P1.x–P3.x refer to the [existing V2 proposals](./V2_PROPOSAL.md). P4.x are new proposals introduced in this document.

---

### P4.1 Pool Factory & Multi-Pool Architecture

**Problem:** Deploying a new fund strategy requires deploying and configuring 5+ contracts from scratch with no shared infrastructure.

**Solution:** Introduce a `PoolFactory` contract that deploys pre-configured `(LoanEngine, TranchePool)` pairs using the EIP-1167 minimal clone pattern. The factory:

1. **Maintains a pool registry** — every deployed pool is tracked with its configuration (stablecoin, policy version, creation date, current state).
2. **Shares stateless singletons** — `CreditPolicy`, `HonkVerifier`, and `Poseidon2` are deployed once and referenced by all pool instances. These contracts are pure verification functions with no per-pool state.
3. **Unifies governance** — a single `ProtocolController` can govern all pools through the factory's role management.
4. **Provides aggregate views** — total AUM, total deployed, total idle across all pools via `PoolRegistry.getAggregateStats()`.

```
PoolFactory.createPool(
    stableCoin: USDC,
    policyVersion: 3,
    seniorAPR: 800,      // 8%
    juniorAPR: 1200,     // 12%
    allocationRatios: [80, 15, 5],
    poolLabel: "SME Working Capital Fund I"
) → returns (loanEngineProxy, tranchePoolProxy, poolId)
```

**Architectural Impact:**
- New contracts: `PoolFactory.sol`, `PoolRegistry.sol`
- `CreditPolicy` becomes a shared singleton referenced by multiple LoanEngines
- `LoanEngine.initialize()` takes a `poolId` parameter for registry tracking
- Each pool clone gets its own storage but shares implementation bytecode

**Differentiation:** No competitor in the RWA lending space offers a multi-strategy factory pattern. Goldfinch has a single pool type. Maple has siloed pools with no shared policy infrastructure. This positions Credit Rail as **infrastructure for launching credit funds**, not just a single fund.

---

### P4.2 Epoch-Based Rolling Pool (Open-Ended Fund Model)

**Problem:** The `OPEN → COMMITTED → DEPLOYED → CLOSED` lifecycle models a closed-end fund. Institutional private credit has moved heavily toward open-ended and evergreen fund structures where LPs can enter and exit on a rolling basis.

**Solution:** Replace the linear lifecycle with an epoch-based system:

1. The pool operates in rolling epochs (configurable: monthly, quarterly, or custom).
2. During a **request window** (e.g., the last 7 days of each epoch), LPs submit deposit and withdrawal requests.
3. At the epoch boundary, the pool manager calls `processEpoch()`, which:
   - Fills deposit requests pro-rata if oversubscribed against the pool's remaining capacity.
   - Fills withdrawal requests pro-rata against available idle capital.
   - Queues unfilled withdrawal requests for the next epoch.
4. Between epochs, the pool operates normally — loans are created, activated, repaid, defaulted.

```
Pool States (V2):
  SETUP → ACTIVE → PROCESSING_EPOCH → ACTIVE → ... → WINDING_DOWN → CLOSED

Within ACTIVE:
  - Loan operations proceed normally
  - LPs submit deposit/withdrawal requests (queued, not immediate)

During PROCESSING_EPOCH:
  - Fund manager processes all queued requests
  - Net capital flow is computed and applied
  - New shares minted / burned accordingly
```

**Architectural Impact:**
- New internal state: `EpochState` struct with request queues, epoch boundaries, fill ratios
- `deposit()` and `withdraw()` become request-based (returns a request ID, not immediate settlement)
- New functions: `submitDepositRequest()`, `submitWithdrawalRequest()`, `processEpoch()`, `claimProcessedRequest()`
- Pool state machine evolves from linear to cyclic

**Differentiation:** This mirrors the redemption mechanics of real institutional fund structures (Luxembourg SICAVs, Cayman Master Funds, UK ACS structures). Centrifuge's Tinlake pools had a similar epoch model but predate modern ZK and lack the privacy-preserving underwriting layer.

---

### P4.3 Dynamic Tranche Allocation per Risk Tier

**Problem:** A Tier 0 loan (low risk) and a Tier 3 loan (high risk) both draw 80/15/5 from Senior/Junior/Equity. This under-prices risk for high-tier loans and over-protects seniors on low-tier loans.

**Solution:** Extend `CreditPolicy.LoanTier` with per-tier allocation overrides:

```solidity
struct LoanTier {
    // ... existing fields ...
    uint256 seniorAllocationBps;    // e.g., 8500 for Tier 0, 6000 for Tier 3
    uint256 juniorAllocationBps;    // e.g., 1000 for Tier 0, 2500 for Tier 3
    // equity = 10000 - senior - junior
}
```

When `LoanEngine.activateLoan()` calls `TranchePool.allocateCapital()`, it passes the tier-specific ratios:

```solidity
// LoanEngine.activateLoan() — V2
ICreditPolicy.LoanTier memory tier = i_creditPolicy.getLoanTier(loan.policyVersion, loan.tierId);
i_tranchePool.allocateCapital(
    totalDisbursement,
    fees,
    receivingEntity,
    feeManager,
    tier.seniorAllocationBps,   // NEW: per-tier ratio
    tier.juniorAllocationBps    // NEW: per-tier ratio
);
```

**Example Configuration:**

| Tier | Risk Level | Senior | Junior | Equity | Loan APR |
|------|-----------|--------|--------|--------|----------|
| 0 | Low | 85% | 10% | 5% | 8% |
| 1 | Medium-Low | 80% | 15% | 5% | 10% |
| 2 | Medium-High | 70% | 20% | 10% | 14% |
| 3 | High | 60% | 25% | 15% | 18% |

**Architectural Impact:**
- `ICreditPolicy.LoanTier` gains two new fields (added to `policyScopeHash`)
- `TranchePool.allocateCapital()` accepts ratio parameters instead of using internal state
- `CreditPolicy.freezePolicy()` includes the new fields in the Poseidon2 hash (23 parameters instead of 21)
- Circuit update: Two additional private inputs for the allocation ratios in the policy hash computation
- **Backward compatible:** if the new fields are zero, fall back to pool-wide defaults

**Differentiation:** This is how real CLO managers work — overcollateralization tests and subordination levels vary by credit quality bucket. No on-chain protocol implements per-tier capital allocation.

---

### P4.4 Revolving Credit Lines

**Problem:** V1 supports only term loans. A borrower who repays a 90-day loan and wants another must go through the entire origination cycle again — new ZK proof, new `createLoan()`, new `activateLoan()`. Revolving credit facilities, where a borrower can draw, repay, and redraw up to a limit, are a cornerstone of commercial lending and represent the majority of working capital financing.

**Solution:** Introduce a `CreditLine` concept alongside the existing term loan:

1. A credit line is **created** with a ZK proof (same circuit, proves borrower eligibility), establishing:
   - Maximum principal limit (approved amount)
   - Revolving term (e.g., 12 months)
   - APR and fee schedule (from the policy tier)
2. The credit line is **activated** once. Capital is reserved (not deployed) up to the approved limit.
3. The borrower (via the Servicer) **draws** against the line without a new ZK proof, up to the limit minus outstanding balance.
4. **Repayments** reduce the outstanding balance and free capacity for redraw.
5. Interest accrues only on the **drawn balance**, not the full limit.
6. The line **expires** at maturity. Any outstanding balance must be repaid. Undrawn capacity is released.

```
Credit Line State Machine:
  CREATED → ACTIVE_REVOLVING → EXPIRED → REPAID
                ↓                  ↓
           DEFAULTED → WRITTEN_OFF

Within ACTIVE_REVOLVING:
  draw() → increases outstandingBalance, deploys capital from pool
  repay() → decreases outstandingBalance, returns capital to pool
  redraw() → draw again after repayment
```

**Architectural Impact:**
- New loan type flag: `isRevolving` in the `Loan` struct
- New fields: `maxPrincipal`, `drawnBalance`, `availableBalance`, `revolvingExpiryTimestamp`
- New functions: `drawFromCreditLine(loanId, amount)`, `repayToCreditLine(loanId, amount)`
- The ZK proof at origination proves eligibility for the max limit. Subsequent draws are authorized by `SERVICER_ROLE` without new proofs
- Interest accrual modified: `_accrueInterest()` uses `drawnBalance` instead of `principalOutstanding` for revolving lines

**Differentiation:** No on-chain private credit protocol supports revolving credit. Goldfinch, Maple, TrueFi, Centrifuge, and Clearpool all do term loans exclusively. This would be a **genuine first-mover advantage** for the institutional working capital market.

---

### P4.5 Loan Restructuring & Workout Module

**Problem:** V1 has a binary default path: `ACTIVE → DEFAULTED → WRITTEN_OFF`. Real private credit involves extensive workout negotiations — extending terms, reducing principal, lowering rates, granting payment holidays. Currently, the only option for a struggling borrower is full default and write-off, which triggers the loss waterfall and permanently destroys LP capital.

**Solution:** Introduce a `restructureLoan()` function that allows `RISK_ADMIN_ROLE` to modify the terms of an `ACTIVE` or `DEFAULTED` loan:

1. **Term Extension** — push the maturity date forward (e.g., +90 days).
2. **APR Reduction** — lower the interest burden (e.g., from 12% to 8%).
3. **Principal Reduction** — write down a portion while keeping the loan active for the remainder. The written-down portion flows through `TranchePool.onPartialLoss()`.
4. **Payment Holiday** — freeze interest accrual for a specified period.

```solidity
function restructureLoan(
    uint256 loanId,
    uint256 newTermDays,            // 0 = no change
    uint256 newAprBps,              // 0 = no change
    uint256 principalReduction,     // 0 = no reduction
    uint256 paymentHolidayDays      // 0 = no holiday
) external onlyRole(RISK_ADMIN_ROLE) {
    // Requires ProtocolController timelock approval
    // Accrues interest up to restructuring date
    // Applies modifications
    // If principalReduction > 0: calls TranchePool.onPartialLoss()
    // Emits LoanRestructured event with full audit trail
}
```

**New Loan State (optional):**
A `RESTRUCTURED` flag (or a counter `restructureCount`) on the loan struct tracks how many times a loan has been modified. This is standard in institutional credit reporting.

**Architectural Impact:**
- New function on `LoanEngine`: `restructureLoan()`
- New function on `TranchePool`: `onPartialLoss(principalReduction, interestCancellation)` — absorbs a partial loss through the waterfall without zeroing the loan
- New event: `LoanRestructured(loanId, oldTermDays, newTermDays, oldAprBps, newAprBps, principalReduction, paymentHolidayDays)`
- All restructuring actions require `ProtocolController` timelock approval (material LP-impacting changes)

**Differentiation:** Maple Finance has basic loan modification, but no structured workout process with partial write-downs flowing through a waterfall. No protocol handles the combination of restructuring + tranched loss absorption.

---

### P4.6 Loan Position NFTs (ERC-721)

**Problem:** Loan positions exist as internal structs in a mapping. They cannot be traded, transferred, or used as collateral in other protocols. The fund manager holds all economic exposure with no mechanism for risk distribution or secondary market liquidity.

**Solution:** Mint an ERC-721 token for each loan at creation time. The NFT represents economic rights to the loan's repayment stream (principal + interest). This enables:

1. **Secondary Market Trading** — fund managers can sell individual loan exposures to other institutional buyers.
2. **DeFi Composability** — loan NFTs can be used as collateral in lending protocols (borrow against a portfolio of loan positions).
3. **Portfolio Construction** — aggregate loan NFTs from different Credit Rail pools into structured products.
4. **Regulatory Reporting** — each loan has a unique, transferable, auditable on-chain instrument.

```solidity
// LoanPositionNFT.sol
contract LoanPositionNFT is ERC721, ERC721URIStorage {
    function mint(uint256 loanId, address owner) external onlyLoanEngine;

    // Metadata includes:
    // - Loan terms (principal, APR, term, origination date)
    // - Current state (ACTIVE, DEFAULTED, etc.)
    // - Borrower commitment hash (pseudonymous)
    // - Policy version and tier
    // - Outstanding balance and accrued interest
}
```

**Important Design Constraint:** Transfer of the NFT does **not** affect the underlying loan accounting. Interest and principal still flow through the pool waterfall. The NFT represents a *claim* on the loan economics, not operational control over the loan. Only the `SERVICER_ROLE` and `RISK_ADMIN_ROLE` can perform loan operations regardless of NFT ownership.

**Architectural Impact:**
- New contract: `LoanPositionNFT.sol` (ERC-721 with dynamic metadata)
- `LoanEngine.createLoan()` mints an NFT alongside the loan struct
- Need to define what NFT ownership entitles: claim on recovery proceeds, information rights, potential governance voice over default/restructuring decisions
- ERC-721 enables integration with NFT marketplaces and lending protocols

**Differentiation:** Centrifuge tokenizes asset pools (via DROP/TIN tokens) but not individual loan positions. Individual loan NFTs enable granular risk trading — a fundamentally new primitive for on-chain structured credit.

---

### P4.7 Privacy-Preserving Portfolio Analytics via Aggregate ZK Proofs

**Problem:** LPs need portfolio-level risk metrics — average credit quality, concentration by borrower, weighted average maturity, industry diversification, default rate — but individual loan data is private. Currently, there is no mechanism to provide aggregate analytics without either revealing individual loan details or trusting off-chain reporting.

**Solution:** Introduce aggregate proof circuits that prove portfolio-level statements without revealing per-loan data:

1. **Concentration Proof** — proves "no single `borrowerCommitment` exceeds X% of total deployed capital" without revealing which borrower has what exposure or how many loans they have.

2. **Portfolio Quality Proof** — proves "the weighted average risk tier of the active portfolio is ≤ T" without revealing individual tier assignments or loan sizes.

3. **Diversification Proof** — proves "the portfolio has at least N distinct `borrowerCommitment` values" without listing them.

4. **Covenant Compliance Proof** — proves "all active borrowers' latest re-attestation data still meets the frozen policy requirements" without revealing the underlying financials.

These proofs would be generated periodically (e.g., monthly) by the fund manager using a recursive circuit that takes individual loan commitments as inputs. The aggregated proof is submitted on-chain and stored in a `PortfolioAttestation` contract:

```solidity
// PortfolioAttestation.sol
contract PortfolioAttestation {
    struct Attestation {
        uint256 poolId;
        uint256 epoch;
        bytes32 proofType;          // CONCENTRATION, QUALITY, DIVERSIFICATION, COVENANT
        bytes32 statement;          // The proven statement (e.g., "maxConcentration <= 1500 bps")
        uint256 timestamp;
        bool verified;
    }

    mapping(uint256 => Attestation[]) public attestations; // poolId → attestations

    function submitAttestation(
        uint256 poolId,
        bytes32 proofType,
        bytes32 statement,
        bytes calldata proof,
        bytes32[] calldata publicInputs
    ) external onlyRole(FUND_MANAGER_ROLE);
}
```

**Architectural Impact:**
- New recursive circuit: `portfolio_analytics.nr` (takes N loan commitments as inputs, proves aggregate properties)
- New contract: `PortfolioAttestation.sol` (stores and verifies aggregate proofs)
- New verifier contract: `PortfolioVerifier.sol` (auto-generated from the recursive circuit)
- LP-facing: LPs can verify that portfolio risk constraints are actively maintained, not just promised

**Differentiation:** This is **genuinely novel**. No protocol — DeFi or traditional — offers ZK-verified portfolio analytics. This would be a research-grade differentiator that could attract academic attention, institutional trust, and regulatory goodwill. It turns Credit Rail's privacy model from a limitation ("LPs can't see the loans") into an advantage ("LPs can verify portfolio properties without needing to see the loans").

---

### P4.8 Concentration Limit Enforcement

**Problem:** `CreditPolicy.sol` defines `ConcentrationLimits` with `maxSingleBorrowerBps` and `maxIndustryConcentrationBps`, but these are never enforced anywhere. There is no tracking of cumulative exposure per borrower or industry in `LoanEngine`.

**Solution:** Enforce concentration limits on-chain during loan creation and activation:

```solidity
// LoanEngine.sol — V2 additions
mapping(bytes32 => uint256) public s_borrowerExposure;    // borrowerCommitment → total active principal
mapping(bytes32 => uint256) public s_industryExposure;    // industryHash → total active principal

function createLoan(...) external {
    // ... existing validation ...

    // V2: Concentration check
    ICreditPolicy.ConcentrationLimits memory limits = i_creditPolicy.getConcentrationLimits(params.policyVersion);
    uint256 totalDeployed = i_tranchePool.getTotalDeployedValue();

    uint256 newBorrowerExposure = s_borrowerExposure[params.borrowerCommitment] + params.principalIssued;
    if (totalDeployed > 0 && newBorrowerExposure * 10000 / (totalDeployed + params.principalIssued) > limits.maxSingleBorrowerBps) {
        revert LoanEngine__ConcentrationLimitExceeded();
    }

    uint256 newIndustryExposure = s_industryExposure[params.industryHash] + params.principalIssued;
    if (totalDeployed > 0 && newIndustryExposure * 10000 / (totalDeployed + params.principalIssued) > limits.maxIndustryConcentrationBps) {
        revert LoanEngine__IndustryConcentrationExceeded();
    }
}

function activateLoan(...) external {
    // Update exposure tracking
    s_borrowerExposure[loan.borrowerCommitment] += loan.principalIssued;
    s_industryExposure[loan.industryHash] += loan.principalIssued;
}

function _onLoanClosed(uint256 loanId) internal {
    // Decrease exposure on repayment, write-off, or recovery
    s_borrowerExposure[loan.borrowerCommitment] -= closedPrincipal;
    s_industryExposure[loan.industryHash] -= closedPrincipal;
}
```

**Note on Privacy:** Tracking exposure per `borrowerCommitment` reveals concentration patterns (how many loans per commitment, total exposure per commitment) but does not reveal the borrower's identity. This is consistent with the existing design decision of "linkable pseudonymity" (see [DESIGN_TRADEOFFS.md §5.1](./DESIGN_TRADEOFFS.md)).

**Architectural Impact:**
- Two new storage mappings in `LoanEngine`
- Exposure updates on activation, repayment, write-off, and recovery
- New error types: `LoanEngine__ConcentrationLimitExceeded`, `LoanEngine__IndustryConcentrationExceeded`
- The `industryHash` is already available from the loan creation parameters

**Differentiation:** Bridges the gap between policy definition and enforcement. Makes the `ConcentrationLimits` struct meaningful rather than decorative.

---

### P4.9 Multi-Currency Support

**Problem:** V1 is initialized with a single `i_stableCoin` address. Institutional private credit operates across multiple currencies — USD, EUR, GBP, SGD. A UK-based fund lending in GBP or an EU fund lending in EUR cannot use a USD-only protocol.

**Solution:** This requires minimal smart contract changes because the stablecoin is already a configurable initialization parameter. The real enablement comes from the factory pattern (P4.1):

1. `PoolFactory.createPool()` accepts any ERC-20 token address as the denomination currency.
2. Pool A uses USDC (USD), Pool B uses EURC (EUR), Pool C uses a regulated GBP stablecoin.
3. Cross-currency pools are explicitly out of scope — each pool is single-currency.
4. `InterestMath.sol` is already currency-agnostic (it works in basis points, not absolute amounts).
5. The `PoolRegistry` tracks each pool's denomination for aggregate reporting (TVL by currency).

**Architectural Impact:** Minimal — the factory pattern naturally enables this. The main work is ensuring documentation, UI, and reporting correctly handle multiple denominations.

**Differentiation:** Positions Credit Rail for non-USD markets where most RWA protocols have zero presence.

---

### P4.10 Automated Pool Operations via Keepers

**Problem:** All pool state transitions and time-sensitive operations are manual. `declareDefault()` for overdue loans requires `RISK_ADMIN_ROLE` intervention. Pool state transitions require admin action. Interest accrual numbers go stale between state-changing calls. There is no mechanism for automated loan expiry (ties to existing [P2.2](./V2_PROPOSAL.md)).

**Solution:** Deploy a `CreditRailKeeper` contract implementing Chainlink's `AutomationCompatibleInterface`:

1. **Maturity Monitoring** — automatically calls `declareDefault()` when a loan exceeds `maturityTimestamp + gracePeriod`. Configurable grace period per pool.
2. **Reservation Expiry** — calls `expireReservation()` for stale `CREATED` loans that exceed the reservation window (ties to P2.2).
3. **Pool State Transitions** — auto-transitions to `CLOSED` when `totalDeployedValue == 0` and a closure trigger is met.
4. **Interest Refresh** — periodically calls a `refreshAccrual()` function that forces tranche target accrual, keeping on-chain state fresh for LP queries.
5. **Epoch Processing Reminder** — emits alerts when an epoch boundary approaches and `processEpoch()` hasn't been called (ties to P4.2).

```solidity
// CreditRailKeeper.sol
contract CreditRailKeeper is AutomationCompatibleInterface {
    function checkUpkeep(bytes calldata) external view override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        // Scan registered pools for:
        // 1. Loans past maturity + grace period
        // 2. Expired reservations
        // 3. Pools eligible for closure
        // 4. Stale accrual timestamps
    }

    function performUpkeep(bytes calldata performData) external override {
        // Decode performData and execute the appropriate action
        // The keeper contract holds RISK_ADMIN_ROLE and POOL_ADMIN_ROLE
    }
}
```

**Architectural Impact:**
- New contract: `CreditRailKeeper.sol`
- The keeper needs appropriate roles on each pool it monitors
- `LoanEngine` may need a `refreshAccrual(loanId)` function that accrues interest without requiring a repayment
- Compatible with Chainlink Automation, Gelato, or OpenZeppelin Defender

**Differentiation:** Reduces the operational burden on fund managers and creates more predictable, timely lifecycle management for LPs.

---

## Part 3 — Competitive Differentiation Strategy

### 3.1 Competitive Landscape

| Protocol | Model | Privacy | ZK Proofs | Structured Finance | Immutable Policy | Open-Ended Pools |
|---|---|---|---|---|---|---|
| **Credit Rail** | Institutional, permissioned | Full (ZK-hidden borrower data) | Noir/UltraHonk | 3-tranche waterfall | Frozen + Poseidon2 hash | Proposed (P4.2) |
| **Goldfinch** | Community-audited | None (public borrower) | None | 2-tranche (Senior/Junior) | None | No |
| **Maple Finance** | Institutional pools | None | None | None (single pool per strategy) | None | Partial (withdrawal queues) |
| **Centrifuge** | RWA tokenization | None | None | 2-tranche (DROP/TIN) | None | Yes (Tinlake epochs) |
| **TrueFi** | Institutional unsecured | None | None | None | None | No |
| **Clearpool** | Permissioned single-borrower | None | None | None | None | Yes (instant liquidity) |

### 3.2 Credit Rail's Unique Advantages

**1. Privacy as Regulatory Compliance (not just a feature)**

Credit Rail is the *only* protocol where borrower financial data never touches the blockchain. This is not a nice-to-have — it's a legal requirement in many jurisdictions:
- **GDPR (EU):** Processing financial data on a public blockchain without consent violates Article 5(1)(c) (data minimization). ZK proofs satisfy the requirement by proving compliance without processing personal data on-chain.
- **Banking Secrecy Laws (Switzerland, Singapore, Cayman Islands):** Disclosing borrower financials on a public ledger could violate bank secrecy obligations. ZK proofs eliminate this exposure.
- **CCPA (California):** Borrowers have the right to deletion of personal information. On-chain data is permanent; ZK commitments are not personal information.

**Positioning:** Credit Rail is not "DeFi that happens to have privacy." It is the only lending protocol that can operate legally in jurisdictions with strict financial data protection requirements.

**2. Verifiable Compliance Without Disclosure**

The combination of:
- Private policy thresholds (protecting the fund's IP)
- Private borrower data (protecting the borrower's privacy)
- Public `policyScopeHash` (proving which policy governs each loan)
- On-chain hash verification (proving the hash matches frozen policy storage)

...creates a unique property: **any external party can verify that every loan was originated in compliance with a specific, immutable set of credit criteria, without knowing what those criteria are or what the borrower's numbers were.**

No competitor offers this. Goldfinch's community auditors see all borrower data. Maple's pool delegates see all borrower data. Centrifuge's asset originators publish borrower details. TrueFi publishes detailed loan terms.

**3. Structured Finance Depth**

The 3-tranche waterfall with proper loss absorption (Equity → Junior → Senior), ghost interest cancellation, recovery restoration (Senior → Junior → Equity), and 19 invariants tested across 4 fuzzing frameworks is the most sophisticated on-chain structured credit model. Combined with per-tier dynamic allocation (P4.3), this approaches the complexity of real CLO structures.

**4. Immutable Underwriting Standards**

Once a `CreditPolicy` is frozen, the `policyScopeHash` is permanently immutable and cryptographically binds every ZK proof to that exact policy version. Even the fund administrator cannot retroactively weaken the underwriting criteria for existing loans. No competitor offers this guarantee — in every other protocol, the pool delegate or originator can change lending criteria at any time.

### 3.3 Recommended Positioning Directions

**Direction 1: "Regulatory-Grade DeFi"**

Position Credit Rail as the only lending protocol that satisfies institutional compliance requirements out of the box. Target regulated fund managers (FCA-authorized, MAS-licensed, SEC-registered) who cannot use existing DeFi lending protocols due to data protection requirements. Marketing message: *"The only on-chain lending infrastructure where borrower data stays off-chain by mathematical guarantee."*

**Direction 2: "Private Credit Infrastructure"**

Via the factory pattern (P4.1) and multi-pool architecture, position Credit Rail not as a single fund but as **infrastructure for launching credit funds**. Multiple fund managers deploy their own pools with custom strategies, shared compliance infrastructure, and unified governance. Marketing message: *"Launch an institutional credit fund in one transaction."*

**Direction 3: "ZK-Verified Portfolio Analytics"**

The aggregate proof capability (P4.7) would be genuinely novel — no protocol, DeFi or traditional, offers ZK-verified portfolio analytics. This could attract academic attention, institutional trust, and regulatory engagement. Marketing message: *"Verify portfolio risk without seeing the loans."*

**Direction 4: "Composable Structured Credit"**

Via loan position NFTs (P4.6), tradable tranche shares ([P3.5](./V2_PROPOSAL.md)), and the factory pattern, enable Credit Rail assets to participate in the broader DeFi ecosystem. Senior tranche tokens used as collateral in Aave. Loan NFTs traded on specialized marketplaces. Cross-pool portfolio construction. Marketing message: *"Structured credit that composes with DeFi."*

---

## Part 4 — V2 Contract Architecture

### 4.1 Target Topology

```
┌─────────────────────────────────────────────────────────┐
│                    ProtocolController                     │
│              (TimelockController, governs all)            │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────┴──────────────────────────────┐
│                       PoolFactory                        │
│         (deploys pool pairs, manages registry)           │
└──┬────────────────┬──────────────────┬──────────────────┘
   │                │                  │
   ▼                ▼                  ▼
┌──────────┐  ┌──────────┐  ┌─────────────────────────────┐
│ Shared   │  │ Shared   │  │  Pool Instance 1             │
│ Credit   │  │ Honk     │  │  ├── LoanEngine (proxy)      │
│ Policy   │  │ Verifier │  │  ├── TranchePool (proxy)      │
│          │  │ +        │  │  ├── LoanPositionNFT          │
│ (multi-  │  │ Poseidon2│  │  └── ERC-20 Tranche Tokens   │
│  version)│  │ (pure)   │  │       (crSENIOR, crJUNIOR)   │
└──────────┘  └──────────┘  └─────────────────────────────┘
                                      │
┌─────────────────────────────────────┴───────────────────┐
│  Pool Instance 2                                         │
│  ├── LoanEngine (proxy)                                  │
│  ├── TranchePool (proxy)                                 │
│  └── (same shared CreditPolicy, Verifier, Poseidon2)    │
└─────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────┴──────────────────────────────┐
│                    Support Contracts                      │
│  ├── PoolRegistry (aggregate TVL, pool metadata)         │
│  ├── CreditRailKeeper (Chainlink Automation)             │
│  └── PortfolioAttestation (aggregate ZK proof store)     │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Key Design Decisions

**Shared vs. Per-Pool Contracts:**

| Contract | Deployment | Why |
|---|---|---|
| `CreditPolicy` | Shared singleton | Policies are stateless verification rules. No reason to duplicate per pool. Multiple pools can reference the same frozen policy version. |
| `HonkVerifier` | Shared singleton | Pure function — takes proof bytes, returns bool. No state. |
| `Poseidon2` | Shared singleton | Pure hash function. No state. |
| `LoanEngine` | Per-pool clone | Stateful — stores loans, nullifiers, whitelists specific to each pool. |
| `TranchePool` | Per-pool clone | Stateful — stores tranche balances, shares, indices specific to each pool. |
| `LoanPositionNFT` | Per-pool (optional) | Token collection per pool for clear attribution. |
| `ProtocolController` | Shared singleton | Single governance entity across all pools. |

**Clone Pattern (EIP-1167):**

Each pool's `LoanEngine` and `TranchePool` are deployed as minimal proxy clones pointing to a shared implementation. This reduces deployment gas from ~5M (full deploy) to ~100K (clone deploy) per pool. The factory stores the current implementation addresses, enabling batch upgrades.

**Upgrade Management:**

1. **Shared Implementation Upgrades** — when a new `LoanEngine` implementation is approved via `ProtocolController`, the factory updates its stored implementation address. New pools use the new implementation automatically.
2. **Existing Pool Upgrades** — existing pools use UUPS proxy upgrade. The `ProtocolController` calls `upgradeToAndCall()` on each pool's proxy. This can be batched.
3. **Version Registry** — the `PoolRegistry` tracks which implementation version each pool is running. Alerts operators when pools fall behind.

### 4.3 On-Chain vs. Off-Chain Balance

**Keep On-Chain (trust anchor):**
- All accounting (idle, deployed, shares, interest indices)
- All state transitions (loan states, pool states)
- ZK proof verification
- Policy hash verification
- Concentration limit enforcement
- Waterfall execution

**Move Off-Chain (with on-chain anchoring):**
- Portfolio analytics (computed off-chain, attested on-chain via aggregate ZK proofs per P4.7)
- Loan maturity monitoring (off-chain keepers trigger on-chain actions per P4.10)
- Proof generation pipeline (already off-chain, scale to parallel infrastructure)
- LP reporting and dashboards (read from events and state, compute off-chain)
- NAV calculations (off-chain computation, on-chain attestation)

---

## Part 5 — ZK Circuit Evolution

### 5.1 V2 Origination Circuit Changes

The V2 origination circuit incorporates the existing proposals (P1.1–P1.3) plus support for dynamic allocation:

| Change | Gate Impact | Source |
|---|---|---|
| Replace `loanId` with `nonce` in `compute_loan_hash` and `nullifierHash` | ~0 (same number of hash inputs) | P1.1 |
| Add `chain_id` and `contract_address` to `compute_loan_hash` | +200 gates (2 extra Poseidon2 inputs) | P1.2 |
| Add `borrower_uuid` to signature payload and commitment | +400 gates (1 extra hash input + 1 extra signature field) | P1.3 |
| Add `seniorAllocationBps` and `juniorAllocationBps` to `compute_policy_hash` | +200 gates (2 extra Poseidon2 inputs) | P4.3 |
| **Total V2 origination circuit** | **~7,050 gates** (up from 6,248) | |

**Gate budget:** The target maximum for the V2 origination circuit is 20,000 gates. At ~7,050 gates, there is ample headroom for future additions. For reference, Tornado Cash Nova's circuit is ~30,000 gates.

### 5.2 New Circuits

**A. Borrower Re-Attestation Circuit (~3,000 gates)**

A lighter-weight circuit that proves "the borrower's financials still meet the policy requirements" without originating a new loan. Used for ongoing covenant monitoring of active credit lines (P4.4) and maintenance covenant enforcement (addressing §1.9).

- Inputs: Updated borrower financials, existing borrower commitment, frozen policy parameters
- Proves: Current financials still satisfy eligibility and ratio requirements
- Does not include: Schnorr signature (reuses existing underwriter attestation), loan hash computation
- Output: Re-attestation hash submitted on-chain as a covenant compliance proof

**B. Portfolio Concentration Circuit (~10,000–20,000 gates)**

A recursive circuit proving portfolio-level concentration properties (P4.7):

- Inputs: Merkle tree of `(borrowerCommitment, activePrincipal)` pairs
- Proves: No single leaf exceeds X% of the tree's total value
- Uses: Poseidon2 Merkle tree (ZK-efficient), recursive sub-proof verification
- Output: Concentration attestation hash

**C. Credit Line Draw Circuit (~2,000 gates)**

A minimal circuit proving that a credit line draw is within the approved limit (P4.4):

- Inputs: Original credit line proof commitment, current drawn balance, draw amount, max limit
- Proves: `drawnBalance + drawAmount <= maxPrincipal`
- Does not include: Full eligibility re-check (already done at origination)
- Output: Draw authorization hash

**D. Multi-Loan Batch Circuit (~50,000–100,000 gates)**

A recursive circuit aggregating N individual loan proofs into a single proof ([P3.4](./V2_PROPOSAL.md)):

- Inputs: N individual proof commitments (not the full proofs — just their public outputs)
- Proves: All N sub-proofs are valid
- Uses: Noir's `std::verify_proof` recursive verification capability
- Output: Single aggregated proof covering all N loans
- Gas savings: From N × 500K (N verifications) to ~600K (one verification) + N × 200K (storage). For 10 loans: saves ~4.5M gas.

### 5.3 Circuit Growth Management Strategy

1. **Modular Sub-Circuit Design** — split `main.nr` into composable modules:
   - `eligibility_check.nr` — borrower eligibility verification
   - `signature_verification.nr` — Schnorr signature verification
   - `policy_hash.nr` — policy hash computation
   - `loan_hash.nr` — loan hash computation
   - `nullifier.nr` — nullifier computation
   - These are composed via function calls within a single proof, not separate proofs.

2. **Separate Circuits for Separate Purposes** — the origination circuit, re-attestation circuit, portfolio analytics circuit, and batch circuit should be independent Noir projects with independent verifiers. Do not bloat the origination circuit with every new feature.

3. **Client-Side Proving Architecture** — for borrower self-service (P3.1), the WASM-compiled Barretenberg backend enables in-browser proof generation. The circuit must be small enough for client-side proving (~30 second budget on a mid-range laptop). At ~7,050 gates, the V2 origination circuit should prove in under 5 seconds client-side.

---

## Part 6 — Prioritized Implementation Roadmap

### Tier 1: Foundation (Months 1–3)

**Goal:** Fix critical V1 limitations and lay the groundwork for multi-pool.

| Item | Scope | Effort |
|---|---|---|
| P1.1 Stateless loan origination | Circuit + LoanEngine | 2 weeks |
| P1.2 Cross-chain domain separator | Circuit + LoanEngine | 1 week |
| P1.3 Borrower UUID binding | Circuit + LoanEngine | 2 weeks |
| P2.2 Capital reservation with expiry | LoanEngine | 2 weeks |
| P4.3 Dynamic tranche allocation | CreditPolicy + TranchePool + LoanEngine | 2 weeks |
| P4.8 Concentration limit enforcement | LoanEngine | 1 week |
| Circuit re-audit | Noir circuit | 2 weeks |

**Deliverable:** Updated circuit + verifier, upgraded LoanEngine and TranchePool with per-tier allocation and concentration enforcement.

### Tier 2: Multi-Pool Infrastructure (Months 3–5)

**Goal:** Enable multi-strategy deployment and LP liquidity.

| Item | Scope | Effort |
|---|---|---|
| P4.1 Pool Factory + Registry | New contracts | 3 weeks |
| P3.5 Tradable tranche shares (ERC-20) | TranchePool | 2 weeks |
| P4.10 Automated keepers | New contract + Chainlink | 2 weeks |
| P2.3 Multi-servicer confirmation | LoanEngine | 1 week |

**Deliverable:** Factory-deployable pools with ERC-20 tranche tokens and automated lifecycle management.

### Tier 3: Advanced Credit Products (Months 5–8)

**Goal:** Expand the product offering beyond term loans.

| Item | Scope | Effort |
|---|---|---|
| P4.4 Revolving credit lines | LoanEngine + new circuit | 4 weeks |
| P4.5 Loan restructuring/workout | LoanEngine + TranchePool | 3 weeks |
| P4.2 Epoch-based rolling pool | TranchePool | 4 weeks |

**Deliverable:** Revolving credit facilities, loan workout capabilities, and open-ended fund structures.

### Tier 4: DeFi Composability & ZK Innovation (Months 8–12)

**Goal:** Enable ecosystem integration and novel ZK capabilities.

| Item | Scope | Effort |
|---|---|---|
| P4.6 Loan position NFTs | New contract + LoanEngine | 3 weeks |
| P4.7 Portfolio analytics proofs | New circuit + new contract | 6 weeks |
| P3.4 Recursive batch proofs | New circuit + new contract | 4 weeks |
| P3.1 Borrower self-service portal | Frontend + EIP-4337 | 4 weeks |

**Deliverable:** Composable loan NFTs, ZK-verified portfolio analytics, batch origination, and borrower self-service.

### Full V2 Audit (Month 12+)

| Item | Scope | Effort |
|---|---|---|
| Full system re-audit | All contracts + circuits | 6–8 weeks |
| Invariant expansion | 19 → ~35 invariants for new features | 2 weeks |
| Economic model validation | Python simulations for new products | 2 weeks |

---

## Conclusion

Credit Rail V1 is a well-architected permissioned private credit protocol with a genuine technological moat: ZK-verified compliance, immutable frozen policies, and a 3-tranche waterfall tested to institutional standards. The existing V2 proposal (P1.1–P3.5) addresses critical circuit-level bugs and adds valuable operational features.

This comprehensive proposal goes further by identifying the structural constraints that would limit Credit Rail's growth — the monolithic deployment model, static tranche ratios, capital inefficiency in the pool lifecycle, and unenforced policy sections — and proposing concrete solutions that transform the protocol from a single-fund tool into **private credit infrastructure**.

The four strategic directions — Regulatory-Grade DeFi, Private Credit Infrastructure, ZK-Verified Portfolio Analytics, and Composable Structured Credit — are not mutually exclusive. They compound: a factory-deployed, multi-currency pool with dynamic tranching, revolving credit, ZK-verified portfolio analytics, and tradable loan NFTs would be a genuinely unique product in the institutional credit market, on-chain or off.

The 12-month roadmap is deliberately sequenced: fix foundations first (Tier 1), enable scale (Tier 2), expand the product (Tier 3), then innovate at the frontier (Tier 4). Each tier delivers standalone value while building toward the full vision.

---

> *This document is a living proposal. Each section should be refined based on operational experience from V1 deployment, LP feedback, and evolving regulatory requirements.*
