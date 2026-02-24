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

# Timelock (set after ProtocolController deployment)
TIMELOCK_DELAY=172800                   # 48 hours in seconds (for production)
# TIMELOCK_DELAY=600                    # 10 minutes (for testing)

# Roles (set these to multisig addresses for production)
UNDERWRITER_ADDRESS=0x...               # Will receive UNDERWRITER_ROLE
SERVICER_ADDRESS=0x...                  # Will receive SERVICER_ROLE
RISK_ADMIN_ADDRESS=0x...                # Will receive RISK_ADMIN_ROLE
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

Constructor args:
```
TranchePool(
    address _usdcToken,         // ERC20 token address
    uint256 _seniorAprBps,      // e.g. 800 (8% APR)
    uint256 _juniorAprBps,      // e.g. 1200 (12% APR)
    uint256 _equityAprBps       // e.g. 1500 (15% APR)
)
```

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

Constructor args:
```
LoanEngine(
    address _creditPolicy,      // CreditPolicy address from Step 1
    address _tranchePool,       // TranchePool address from Step 2
    address _verifier,          // HonkVerifier address from Step 3
    address _poseidon2,         // Poseidon2 address from Step 4
    uint256 _maxOriginationFeeBps  // e.g. 500 (5% max fee cap)
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

Transfer all admin rights to `ProtocolController`:

```bash
# 1. CreditPolicy (policyAdmin)
cast send $CREDIT_POLICY_ADDRESS "transferAdmin(address)" $PROTOCOL_CONTROLLER_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# 2. TranchePool (owner)
cast send $TRANCHE_POOL_ADDRESS "transferOwnership(address)" $PROTOCOL_CONTROLLER_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# 3. LoanEngine (DEFAULT_ADMIN_ROLE)
cast send $LOAN_ENGINE_ADDRESS \
  "grantRole(bytes32,address)" \
  $(cast keccak "DEFAULT_ADMIN_ROLE") \
  $PROTOCOL_CONTROLLER_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# (Optional: revoke DEFAULT_ADMIN_ROLE from deployer)
```

> ⚠️ This is the critical step. After this, all core protocol changes require a timelock proposal. Do not skip this in production.

---

### Step 8: Grant Roles on `LoanEngine`

```bash
# UNDERWRITER_ROLE
cast send $LOAN_ENGINE_ADDRESS \
  "grantRole(bytes32,address)" \
  $(cast keccak "UNDERWRITER_ROLE") \
  $UNDERWRITER_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# SERVICER_ROLE
cast send $LOAN_ENGINE_ADDRESS \
  "grantRole(bytes32,address)" \
  $(cast keccak "SERVICER_ROLE") \
  $SERVICER_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL

# RISK_ADMIN_ROLE
cast send $LOAN_ENGINE_ADDRESS \
  "grantRole(bytes32,address)" \
  $(cast keccak "RISK_ADMIN_ROLE") \
  $RISK_ADMIN_ADDRESS \
  --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

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
| Policy admin | Deployer | Deployer | ProtocolController |
| Roles | All on deployer | Separate addresses | Separate multisigs |

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
