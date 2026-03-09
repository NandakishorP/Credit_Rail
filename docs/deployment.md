# Deployment Guide

This document describes the complete deployment sequence for the Credit Rail protocol, including constructor arguments, ownership transfer, and environment configuration.

---

## Prerequisites

- Foundry installed (`forge`, `cast`)
- `anvil-zksync` running for local deployment (or target network RPC)
- Node.js + `ts-node` for ZK proof scripts
- Noir toolchain (`nargo`) for circuit compilation
- `.env` file configured (see template below)

---

## Environment Variables

Create a `.env` file in `contracts/`:

```bash
# Network
RPC_URL=http://127.0.0.1:8546          # anvil-zksync local
# RPC_URL=https://sepolia.era.zksync.dev  # zkSync Sepolia testnet

# Deployer
PRIVATE_KEY=0x...                       # Deployer private key (holds all admin roles initially)

# Token
USDC_ADDRESS=0x...                      # ERC20 token used as pool currency
                                        # For local: deploy ERC20Mock via script

# Governance (ProtocolController — 48h timelock)
MULTISIG_ADDRESS=0x...                  # Gnosis Safe: proposer + executor on timelock
GUARDIAN_ADDRESS=0x...                  # Can cancel pending ops + pause instantly
TIMELOCK_DELAY=172800                   # 48 hours in seconds (production)
# TIMELOCK_DELAY=600                    # 10 minutes (testing)

# Operations (direct, no timelock — daily loan/pool ops)
OPERATIONS_MULTISIG=0x...              # Receives FUND_MANAGER, SERVICER, RISK_ADMIN,
                                        # CONFIG_ADMIN, WHITELIST_ADMIN, POLICY_EDITOR,
                                        # INDUSTRY_ADMIN, TREASURY roles
```

---

## Deployment Sequence

The contracts must be deployed in this exact order due to constructor dependencies.

### Step 1: Deploy `CreditPolicy`

```bash
forge script script/DeployFullSystem.s.sol --zksync --rpc-url $RPC_URL \
  --broadcast --private-key $PRIVATE_KEY
```

Constructor args: none. The deployer becomes `policyAdmin`.

---

### Step 2: Deploy `TranchePool`

Initialized via proxy with:
```
TranchePool.initialize(
    address stableCoin_,        // ERC20 token address (e.g. USDC)
    address initialAdmin        // Receives all admin roles
)
```

Senior/Junior APR targets and allocation ratios are configured separately via `CONFIG_ADMIN_ROLE` setters after initialization.

At this point, the pool is in `OPEN` state. No `loanEngine` is set yet — it will be set in Step 5.

---

### Step 3: Deploy `HonkVerifier`

The verifier is auto-generated from the compiled Noir circuit:

```bash
# Compile the circuit first
cd circuits && nargo compile

# Generate the Solidity verifier
bb write_vk --scheme ultra_honk -b target/circuits.json -o target/vk
bb contract --scheme ultra_honk -k target/vk -o ../contracts/src-zk/Verifier.sol
```

The `HonkVerifier` contract has no constructor args. It is a pure verification contract.

```bash
forge script script/DeployVerifier.s.sol --zksync --rpc-url $RPC_URL \
  --broadcast --private-key $PRIVATE_KEY
```

---

### Step 4: Deploy `Poseidon2`

The on-chain Poseidon2 hasher is used by `LoanEngine` to recompute the `loan_hash` during `createLoan()`.

```bash
# Deployed via @poseidon2-evm package
# Address is fixed per network — check package docs
```

For local anvil-zksync, deploy via `DeployFullSystem.s.sol` which handles this automatically.

---

### Step 5: Deploy `LoanEngine`

Initialized via proxy with:
```
LoanEngine.initialize(
    address _creditPolicy,         // CreditPolicy proxy address from Step 1
    address _loanProofVerifier,    // HonkVerifier address from Step 3
    uint256 _maxOriginationFeeBps, // e.g. 500 (5% max fee cap)
    address _tranchePool,          // TranchePool proxy address from Step 2
    address _stableCoin,           // USDC token address
    address _poseidon2,            // Poseidon2 address from Step 4
    address _initialAdmin          // Receives all admin roles
)
```

After deployment, register the `LoanEngine` with `TranchePool`:

```bash
cast send $TRANCHE_POOL_ADDRESS "setLoanEngine(address)" $LOAN_ENGINE_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

---

### Step 6: Deploy `ProtocolController`

Constructor args (TimelockController):
```
ProtocolController(
    uint256 minDelay,           // e.g. 172800 (48 hours)
    address[] proposers,        // [multisig_address]
    address[] executors,        // [multisig_address]
    address admin               // address(0) for self-administration
)
```

---

### Step 7: Transfer Administration to ProtocolController

Grant **governance roles only** to the `ProtocolController` (timelock). These are rare, high-impact operations that must be delayed:

```bash
# DEFAULT_ADMIN_ROLE on all contracts (upgrades + role management)
cast send $CREDIT_POLICY_ADDRESS "grantRole(bytes32,address)" 0x00 $PROTOCOL_CONTROLLER \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $TRANCHE_POOL_ADDRESS "grantRole(bytes32,address)" 0x00 $PROTOCOL_CONTROLLER \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $LOAN_ENGINE_ADDRESS "grantRole(bytes32,address)" 0x00 $PROTOCOL_CONTROLLER \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# POOL_ADMIN_ROLE (pool state transitions — rare, high-impact)
cast send $TRANCHE_POOL_ADDRESS "grantPoolAdminRole(address)" $PROTOCOL_CONTROLLER \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# POLICY_ADMIN_ROLE (create/freeze/deactivate policies — rare, high-impact)
cast send $CREDIT_POLICY_ADDRESS "grantPolicyAdminRole(address)" $PROTOCOL_CONTROLLER \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

> ⚠️ After this, upgrades, role changes, pool state transitions, and policy freezing all require a timelock proposal. Do not skip this in production.

---

### Step 8: Grant Operational Roles to Operations Multisig

Grant **operational roles** to a separate operations multisig (or hot wallet). These are daily operations that must execute immediately — no timelock delay:

```bash
# LoanEngine operational roles
cast send $LOAN_ENGINE_ADDRESS "grantFundManagerRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $LOAN_ENGINE_ADDRESS "grantServicerRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $LOAN_ENGINE_ADDRESS "grantRiskAdminRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $LOAN_ENGINE_ADDRESS "grantConfigAdminRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# TranchePool operational roles
cast send $TRANCHE_POOL_ADDRESS "grantConfigAdminRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $TRANCHE_POOL_ADDRESS "grantWhitelistAdminRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $TRANCHE_POOL_ADDRESS "grantTreasuryRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# CreditPolicy operational roles
cast send $CREDIT_POLICY_ADDRESS "grantPolicyEditorRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $CREDIT_POLICY_ADDRESS "grantIndustryAdminRole(address)" $OPS_MULTISIG \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

---

### Step 8b: Grant Emergency Roles to Guardian

The guardian needs instant pause/unpause — no timelock:

```bash
cast send $LOAN_ENGINE_ADDRESS "grantEmergencyAdminRole(address)" $GUARDIAN \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
cast send $TRANCHE_POOL_ADDRESS "grantEmergencyAdminRole(address)" $GUARDIAN \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

---

### Step 8c: Deployer Renounces ALL Roles

```bash
# Renounce all roles on CreditPolicy
cast send $CREDIT_POLICY_ADDRESS "renounceRole(bytes32,address)" 0x00 $DEPLOYER ...
# (repeat for every role on every contract — see DeployWithGovernance.s.sol Phase 7)
```

> After this, the deployer holds **zero** roles. Only the ProtocolController, operations multisig, and guardian have access.

---

### Step 9: Configure Whitelists

```bash
# Whitelist off-ramping entity
cast send $LOAN_ENGINE_ADDRESS \
  "setWhitelistedOffRampingEntity(address,bool)" \
  $OFF_RAMP_ADDRESS true \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# Whitelist repayment agent
cast send $LOAN_ENGINE_ADDRESS \
  "setWhitelistedRepaymentAgent(address,bool)" \
  $REPAYMENT_AGENT true \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

---

### Step 10: Authorize Underwriter Key

The fund admin's Grumpkin public key must be registered before any proofs can be submitted:

```bash
# Run the TypeScript script to get the key from the deterministic seed
cd zk-scripts && ts-node setup_policy_v2.ts
```

Or directly via `cast`:
```bash
cast send $LOAN_ENGINE_ADDRESS \
  "setUnderwriterAuthorization(bytes32,bytes32,bool)" \
  $KEY_X $KEY_Y true \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

---

### Step 11: Create and Freeze a Policy

```bash
# Via the timelock (production) or directly (development)
cd zk-scripts && ts-node setup_policy_v2.ts
```

This creates policy version 1, sets all parameters, and freezes it. The resulting `policyScopeHash` is stored on-chain.

---

### Step 12: Commit the Pool

Move the pool from `OPEN` → `COMMITTED` to enable loan activation:

```bash
cast send $TRANCHE_POOL_ADDRESS "commitPool()" \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

The system is now ready for loan origination.

---

## Local vs Testnet vs Production

| Consideration | Local (anvil-zksync) | zkSync Sepolia | Production (zkSync Era) |
|---|---|---|---|
| Poseidon2 | Deploy via script | Fixed address | Fixed address |
| USDC | ERC20Mock | Test USDC | Real USDC |
| Timelock delay | 0 or 60s | 600s | 48h+ |
| Private key | Anvil default key | Test wallet | Hardware wallet / HSM |
| Governance (DEFAULT_ADMIN) | Deployer | ProtocolController | ProtocolController (multisig) |
| Operations multisig | Deployer | Separate address | Gnosis Safe (2-of-3+) |
| Guardian | address(0) | Separate address | Security team wallet |
| Role separation | All on deployer | Partial | Full (see DeployWithGovernance) |

---

## Running the Full Local Setup

The `DeployFullSystem.s.sol` script handles Steps 1–5 in a single transaction for local development. After running it:

```bash
forge script script/DeployFullSystem.s.sol --zksync --rpc-url http://127.0.0.1:8546 \
  --broadcast --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

# Then run the TypeScript setup scripts
cd zk-scripts
ts-node setup_policy_v2.ts
ts-node create_loan_simple.ts
```

See `zk-scripts/full_deploy.sh` for a complete shell orchestration of the full local setup.
