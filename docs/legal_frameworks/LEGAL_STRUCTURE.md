# Legal Structure & Bankruptcy Remoteness

This document outlines the off-chain legal framework required to operate the CreditRail protocol as a bankruptcy-remote structured credit facility. The smart contracts handle economics and access control — this document covers the legal and operational layer that wraps around them.

---

## Securities Analysis (Howey Test)

All four Howey prongs are triggered when outside capital enters the protocol:

| Prong | Analysis |
|-------|----------|
| Investment of money | LPs deposit stablecoins into tranches |
| Common enterprise | Pooled capital, shared waterfall, shared loan portfolio |
| Expectation of profits | Senior and Junior have explicit `aprBps` targets; Equity receives residual |
| Efforts of others | Admin roles control lifecycle, LPs are passive |

**Per-tranche nuance:**

- **Senior / Junior** — Fixed yield targets, passive holders. Strongest securities classification.
- **Equity** — No fixed APR, absorbs first loss. If held by the fund manager as skin-in-the-game, Howey prongs 2 and 4 weaken because the holder *is* the operator, not a passive investor.
- **Key principle**: Classification depends on the **holder's relationship to the enterprise**, not the tranche itself. The same tranche can be a security for an outside LP and not a security for the fund manager.

**Implication**: Any outside capital requires securities registration or an exemption (Reg D, Reg S, etc.).

---

## Entity Structure

```
┌─────────────────────────────────────┐
│         Fund Manager (LLC)          │
│  Originates loans, services them    │
│  Holds: FUND_MANAGER_ROLE           │
│         SERVICER_ROLE               │
│         RISK_ADMIN_ROLE             │
│  On: LoanEngine                    │
└──────────────┬──────────────────────┘
               │ Servicing Agreement
               ▼
┌─────────────────────────────────────┐
│       SPV / Trust (Separate LLC)    │
│  Holds investor capital             │
│  No employees, no other business    │
│  Holds: POOL_ADMIN_ROLE             │
│         CONFIG_ADMIN_ROLE           │
│         WHITELIST_ADMIN_ROLE        │
│         EMERGENCY_ADMIN_ROLE        │
│         TREASURY_ROLE               │
│  On: TranchePool                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│       Investors (LPs)               │
│  Deposit into Senior / Junior       │
│  Whitelisted after KYC / accreditation │
└─────────────────────────────────────┘
```

The Fund Manager holds equity as skin-in-the-game (GP commitment). This position is documented in the operating agreement, not offered as a security.

---

## Role Assignment Map

### TranchePool (Owned by SPV/Trust)

| Role | Assigned To | Wallet Type | Purpose |
|------|-------------|-------------|---------|
| `DEFAULT_ADMIN_ROLE` | SPV/Trust | Multisig (2-of-3 min) | Grant/revoke all other roles |
| `POOL_ADMIN_ROLE` | SPV/Trust | Multisig | Pool lifecycle transitions (OPEN → COMMITTED → DEPLOYED → CLOSED) |
| `CONFIG_ADMIN_ROLE` | SPV/Trust | Multisig | Set tranche parameters, allocation ratios |
| `WHITELIST_ADMIN_ROLE` | SPV/Trust (may delegate to servicer) | Multisig | Gate LP access after KYC/accreditation |
| `EMERGENCY_ADMIN_ROLE` | SPV/Trust | Multisig | Pause/unpause |
| `TREASURY_ROLE` | SPV/Trust | Multisig | Treasury operations |

### LoanEngine (Serviced by Fund Manager)

| Role | Assigned To | Wallet Type | Purpose |
|------|-------------|-------------|---------|
| `DEFAULT_ADMIN_ROLE` | SPV/Trust | Multisig (2-of-3 min) | Grant/revoke all other roles, replace servicer |
| `FUND_MANAGER_ROLE` | Fund Manager | Multisig | Create loans (submit ZK proofs) |
| `SERVICER_ROLE` | Fund Manager | Multisig | Activate, repay, recover loans |
| `RISK_ADMIN_ROLE` | Fund Manager | Multisig | Declare defaults, write off loans |
| `CONFIG_ADMIN_ROLE` | Fund Manager (or SPV) | Multisig | Update whitelists, fee parameters |
| `EMERGENCY_ADMIN_ROLE` | SPV/Trust | Multisig | Pause/unpause |

**Critical**: The SPV/Trust holds `DEFAULT_ADMIN_ROLE` on **both** contracts. This ensures the SPV can revoke the Fund Manager's roles and appoint a replacement servicer without needing the Fund's keys.

---

## Bankruptcy Remoteness

### What Makes the SPV Bankruptcy-Remote

1. **Separate legal entity** — The SPV/Trust is a distinct LLC or statutory trust, not a subsidiary of the Fund
2. **No other business** — The SPV exists solely to hold the TranchePool assets
3. **No other creditors** — The SPV does not borrow money or enter other contracts
4. **Independent governance** — At least one multisig signer on the SPV is independent of the Fund
5. **True sale** — Capital flows from investors to the SPV, not through the Fund

### What Happens If the Fund Goes Bankrupt

1. Fund bankruptcy triggers a **servicer event of default** under the servicing agreement
2. The SPV/Trust (holding `DEFAULT_ADMIN_ROLE` on LoanEngine) **revokes** the Fund's `SERVICER_ROLE`, `FUND_MANAGER_ROLE`, and `RISK_ADMIN_ROLE`
3. The SPV **grants** these roles to the backup servicer
4. The backup servicer takes over loan management
5. Investor capital in TranchePool is **not** part of the Fund's bankruptcy estate

### On-Chain Enforceability

The contracts already support servicer replacement via `AccessControl`:

- SPV calls `revokeRole(SERVICER_ROLE, fundAddress)` on LoanEngine
- SPV calls `grantRole(SERVICER_ROLE, backupServicerAddress)` on LoanEngine
- No cooperation from the Fund is required
- This works because the SPV holds `DEFAULT_ADMIN_ROLE`, not the Fund

---

## Required Legal Documents

### 1. SPV Operating Agreement
- Establishes the SPV as a single-purpose entity
- Restricts the SPV from taking on debt or other business
- Names the trustee(s) who control the SPV's multisig keys
- Documents the GP/equity commitment as a non-securities position

### 2. Servicing Agreement
- Defines the Fund's role as loan servicer
- Specifies servicing fee (percentage of interest collected)
- Lists servicer obligations (loan origination, collection, reporting)
- Defines termination triggers:
  - Fund bankruptcy or insolvency
  - Failure to perform servicing duties for N days
  - Material breach of agreement
- Designates a **backup servicer** by name
- Includes key transfer / access transfer obligations

### 3. Subscription Agreements (per LP)
- Accredited investor verification
- Risk disclosures specific to the tranche
- Acknowledgment of the smart contract mechanics
- Maps the LP's wallet address to their legal identity (KYC)

### 4. Backup Servicer Agreement
- Pre-negotiated terms with a backup servicer
- Defines the trigger conditions for stepping in
- Specifies the backup servicer's multisig address (to be granted roles)
- Covers compensation and operational handover

### 5. Trustee Agreement (if using a statutory trust)
- Appoints an independent trustee for the SPV
- Trustee holds one key in the SPV multisig
- Trustee's fiduciary duty is to the investors, not the Fund

---

## Deployment Checklist

Before going live, verify:

- [ ] SPV/Trust is legally formed as a separate entity
- [ ] Multisig wallets are created for SPV and Fund Manager
- [ ] At least one SPV multisig signer is independent of the Fund
- [ ] `DEFAULT_ADMIN_ROLE` on **both** TranchePool and LoanEngine is assigned to the SPV multisig
- [ ] Fund Manager roles on LoanEngine are assigned to the Fund's multisig (not an EOA)
- [ ] Backup servicer is designated and their multisig address is recorded
- [ ] Servicing agreement is signed
- [ ] Subscription agreements are signed by all LPs before whitelisting
- [ ] Role assignments on-chain match the role assignment map in this document
- [ ] Off-ramping entities on LoanEngine are whitelisted by the SPV/Fund as per the servicing agreement

---

## Multisig Recommendations

| Entity | Minimum Signers | Recommended Composition |
|--------|----------------|------------------------|
| SPV/Trust | 2-of-3 | Independent trustee + 2 SPV directors |
| Fund Manager | 2-of-3 | Fund GP + Fund COO + Fund legal counsel |
| Backup Servicer | 2-of-3 | Per backup servicer's internal policy |

**Why multisig matters**: If any single keyholder disappears, becomes incapacitated, or is part of a bankrupt entity, the remaining signers can still operate. This is the on-chain equivalent of corporate continuity.
