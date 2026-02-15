# ZK Proof Integration for Credit Rail

## Overview

This document details the implementation of Zero-Knowledge (ZK) proof verification for the Credit Rail private credit platform. The system enables privacy-preserving loan origination where borrowers can prove they meet credit policy requirements without revealing sensitive financial data.

## What Was Accomplished

### 1. ZK Circuit Development (Noir)

A comprehensive ZK circuit was developed in **Noir** (version 1.0.0-beta.16) that proves:

- **Borrower Eligibility**: Revenue, EBITDA, net worth, company age, default history
- **Financial Ratios**: Debt-to-EBITDA, interest coverage, current ratio, margin
- **Loan Terms Compliance**: Principal, APR, origination fees, term length against policy tiers
- **Industry Exclusions**: Verification that borrower's industry is not excluded
- **Underwriter Attestation**: Schnorr signature verification of borrower data
- **Privacy Commitments**: Borrower commitment binding private data to the proof

**Circuit Location**: `/circuits/src/main.nr`

**Public Inputs** (visible on-chain):
1. `policy_version_hash` - Poseidon hash of frozen policy parameters
2. `loan_hash` - Poseidon hash of loan details
3. `nullifier_hash` - Prevents double-spending of proofs

**Private Inputs** (hidden in proof):
- Borrower financial data (revenue, EBITDA, etc.)
- Borrower secret
- Policy constraints
- Underwriter signature

### 2. On-Chain Verifier Deployment

The **UltraHonk** proving system was used to generate a Solidity verifier contract:

```bash
# Generate verifier from compiled circuit
bb write_vk_ultra_honk -b ./target/circuits.json -o ./target/vk
bb contract_ultra_honk -k ./target/vk -o ../contracts/src/Verifier.sol
```

**Verifier Contract**: `HonkVerifier.sol` - Auto-generated from the Noir circuit

### 3. Poseidon2 Hash Integration

A critical challenge was ensuring the **Poseidon2 hash function** used off-chain in the ZK circuit matches the on-chain computation.

**Problem Identified**: The initial `MockPoseidon2.sol` contract used `keccak256` instead of real Poseidon2, causing hash mismatches.

**Solution**: Deployed the real Poseidon2 implementation from `@poseidon2-evm` library:

```solidity
// Real Poseidon2 deployed at: 0x1B69c60F3ac12BC305C96D927573102f6617eb16
import {Poseidon2} from "@poseidon2-evm/Poseidon2.sol";
```

### 4. Policy Scope Hash Computation

The `policyScopeHash` is a Poseidon hash of 21 policy parameters that creates a binding commitment to the frozen policy version:

```typescript
// Parameters hashed (in order):
const policyInputs = [
  policy.min_revenue,
  policy.min_ebitda,
  policy.min_net_worth,
  policy.min_age,
  policy.max_defaults,
  policy.bankruptcy_excluded ? 1 : 0,
  policy.max_debt_to_ebitda,
  policy.min_interest_coverage,
  policy.min_current_ratio,
  policy.max_leverage,
  policy.min_margin_bps,
  tier.min_principal,
  tier.max_principal,
  tier.min_apr_bps,
  tier.max_apr_bps,
  tier.min_term_days,
  tier.max_term_days,
  tier.max_fee_bps,
  tierId,
  policyId,
  attestation_timestamp
];
```

**Computed Hash**: `0x1cf25e17e3e03cd06259fb4eca69a2317651ec700354473fed420a8a6a399a66`

### 5. Smart Contract Integration

The `LoanEngine.sol` contract was updated to:

1. **Verify ZK Proofs**: Calls `HonkVerifier.verify(proof, publicInputs)`
2. **Validate Policy Hash**: Compares proof's `policy_version_hash` with on-chain `policyScopeHash`
3. **Check Loan Hash**: Recomputes loan hash using Poseidon2 and verifies match
4. **Validate Timestamps**: Ensures proof is not expired or from the future
5. **Register Underwriters**: Manages authorized underwriter public keys

### 6. End-to-End Testing Scripts

Multiple TypeScript scripts were created for testing:

| Script | Purpose |
|--------|---------|
| `create_loan_simple.ts` | Main loan creation with ZK proof |
| `compute_policy_hash.ts` | Compute Poseidon policy hash |
| `setup_policy_v2.ts` | Set up CreditPolicy version 2 |
| `test_onchain.ts` | Test on-chain verification |
| `test_integration.ts` | Full integration test |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Off-Chain                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────┐ │
│  │  Borrower   │───▶│ Underwriter │───▶│  ZK Proof Generator │ │
│  │  Data       │    │  Signature  │    │  (Noir + bb.js)     │ │
│  └─────────────┘    └─────────────┘    └──────────┬──────────┘ │
│                                                    │            │
│  ┌─────────────────────────────────────────────────▼──────────┐ │
│  │  Proof Generation (UltraHonk)                              │ │
│  │  - Witness computation                                     │ │
│  │  - Constraint satisfaction                                 │ │
│  │  - Proof serialization                                     │ │
│  └─────────────────────────────────────────────────┬──────────┘ │
└────────────────────────────────────────────────────┼────────────┘
                                                     │
                                                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                         On-Chain (zkSync)                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────┐ │
│  │   Proof     │───▶│ HonkVerifier│───▶│    LoanEngine       │ │
│  │   + Inputs  │    │  Contract   │    │    createLoan()     │ │
│  └─────────────┘    └─────────────┘    └──────────┬──────────┘ │
│                                                    │            │
│  ┌─────────────┐    ┌─────────────┐    ┌──────────▼──────────┐ │
│  │ Poseidon2   │◀───│CreditPolicy │◀───│   Loan Created      │ │
│  │  (Hash)     │    │ (Frozen)    │    │   State: ACTIVE     │ │
│  └─────────────┘    └─────────────┘    └─────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## Deployed Contracts (Local anvil-zksync)

| Contract | Address | Description |
|----------|---------|-------------|
| **LoanEngine** | `0x46F2Dc79c3D6E9DDb3F263FF3B6331d4938f198b` | Main loan engine with ZK verification |
| **CreditPolicy** | `0x22D151A1313d9B517Fa437F1F5B3744E636D8790` | Policy management |
| **TranchePool** | `0xd7385ba726A7b72933E63FCb0Dfee8Bcae63478c` | Liquidity pool |
| **HonkVerifier** | `0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe` | ZK proof verifier |
| **Poseidon2** | `0x1B69c60F3ac12BC305C96D927573102f6617eb16` | Real Poseidon2 hasher |
| **USDC (Mock)** | `0x82778c3185fD0666d3f34F8930B4287405D9fBe4` | Stablecoin |

---

## Technical Challenges & Solutions

### Challenge 1: Poseidon2 Hash Mismatch

**Problem**: The `MockPoseidon2.sol` used `keccak256(abi.encode(input))` instead of the actual Poseidon2 algorithm.

**Solution**: Deployed the real Poseidon2 implementation from `lib/poseidon2-evm/src/Poseidon2.sol` and redeployed LoanEngine with the correct hasher address.

### Challenge 2: Policy Scope Hash Computation

**Problem**: The on-chain `policyScopeHash` was being computed with `keccak256` but the circuit expected Poseidon2.

**Solution**: Created `compute_policy_hash.ts` to compute the correct Poseidon hash off-chain, then stored it via `setPolicyScopeHash()`.

### Challenge 3: Proof Timestamp Validation

**Problem**: The script used `Date.now() / 1000` (real Unix timestamp ~1.7 billion) but `anvil-zksync` starts with timestamp ~1000.

**Error**: `LoanEngine__ProofFromFuture(proofTimestamp, blockTimestamp)`

**Solution**: Fetch the actual chain timestamp via `provider.getBlock('latest')` and use that in the proof.

### Challenge 4: zkSync Contract Deployment

**Problem**: Standard Ethereum deployment via `ethers.ContractFactory` doesn't work on zkSync (error: `toAddressIsNull`).

**Solution**: Use `forge create` with `--zksync` flag for contract deployment:

```bash
forge create src/LoanEngine.sol:LoanEngine \
  --constructor-args <args> \
  --private-key $PK \
  --rpc-url http://127.0.0.1:8546 \
  --zksync --broadcast
```

---

## How to Run

### Prerequisites

1. **Install Dependencies**:
   ```bash
   # Contracts
   cd contracts && forge install

   # ZK Scripts
   cd zk-scripts && npm install

   # Noir (using noirup)
   noirup -v 1.0.0-beta.16
   ```

2. **Start Local zkSync Node**:
   ```bash
   anvil-zksync --port 8546
   ```

3. **Compile Circuit**:
   ```bash
   cd circuits && nargo compile
   ```

### Running the Test

```bash
# Navigate to zk-scripts
cd zk-scripts

# Run loan creation with ZK proof
npx tsx create_loan_simple.ts
```

### Expected Output

```
============================================================
Create Loan with ZK Proof
============================================================
LoanEngine: 0x46F2Dc79c3D6E9DDb3F263FF3B6331d4938f198b
RPC URL: http://127.0.0.1:8546

Initializing Barretenberg...
Chain timestamp: 1106 (block 106)
Creating loan ID: 2
Generating underwriter key...
  Key found after 4 iterations
Computing hashes...
Signing attestation data...

Generating ZK Proof...
Generated proof for circuit with 3 public inputs and 282 fields.
  Proof size: 9024 bytes
  Public inputs: 3

Verifying off-chain...
✅ Off-chain verification PASSED

--- Creating Loan ---
...
Transaction confirmed in block 107

✅ LOAN CREATED SUCCESSFULLY!
  Loan ID: 2
  State: 2 (ACTIVE)
  Principal: 500000

============================================================
🎉 SUCCESS: ZK-proven loan created on-chain!
============================================================
```

---

## File Structure

```
credit_rail/
├── circuits/
│   ├── Nargo.toml              # Noir project config
│   ├── src/
│   │   └── main.nr             # ZK circuit (2448 lines)
│   └── target/
│       ├── circuits.json       # Compiled circuit
│       └── vk                  # Verification key
│
├── contracts/
│   ├── src/
│   │   ├── LoanEngine.sol      # Main loan contract
│   │   ├── CreditPolicy.sol    # Policy management
│   │   ├── TranchePool.sol     # Liquidity pool
│   │   ├── Verifier.sol        # Auto-generated HonkVerifier
│   │   └── interfaces/
│   │       └── IPoseidon2.sol  # Poseidon2 interface
│   ├── lib/
│   │   └── poseidon2-evm/      # Real Poseidon2 implementation
│   └── script/
│       ├── DeployAndSetup.s.sol
│       └── DeployLoanEngine.s.sol
│
├── zk-scripts/
│   ├── package.json            # Node.js dependencies
│   ├── create_loan_simple.ts   # Main test script
│   ├── compute_policy_hash.ts  # Policy hash computation
│   ├── setup_policy_v2.ts      # Policy setup
│   └── test_onchain.ts         # On-chain verification test
│
└── docs/
    └── ZK_PROOF_INTEGRATION.md # This document
```

---

## Dependencies

### Noir / ZK
- **Noir**: 1.0.0-beta.16
- **@aztec/bb.js**: ^0.82.2 (Barretenberg WASM)
- **@noir-lang/noir_js**: ^1.0.0-beta.3

### Solidity
- **Solidity**: 0.8.30
- **zksolc**: 1.5.15
- **OpenZeppelin**: ^5.0.0
- **poseidon2-evm**: (submodule)

### Tools
- **Foundry**: forge, cast, anvil
- **anvil-zksync**: v0.6.11

---

## Security Considerations

1. **Proof Replay Prevention**: Each proof contains a unique `nullifier_hash` that is tracked on-chain to prevent reuse.

2. **Timestamp Bounds**: Proofs must be within `PROOF_MAX_AGE` seconds of the current block timestamp.

3. **Policy Immutability**: Once a policy version is frozen, its `policyScopeHash` cannot be changed.

4. **Underwriter Authorization**: Only registered underwriter public keys can sign valid attestations.

5. **Privacy**: Borrower financial data never appears on-chain—only commitments and ZK proofs.

---

## Future Improvements

1. **Mainnet Deployment**: Deploy to zkSync Era mainnet with production parameters
2. **Multiple Tiers**: Support multiple loan tiers in a single proof
3. **Recursive Proofs**: Batch multiple loan proofs for gas efficiency
4. **Auditing**: Formal verification of the Noir circuit
5. **Key Management**: HSM integration for underwriter key storage

---

## References

- [Noir Documentation](https://noir-lang.org/docs)
- [Barretenberg](https://github.com/AztecProtocol/barretenberg)
- [zkSync Era Documentation](https://era.zksync.io/docs)
- [Poseidon Hash Function](https://www.poseidon-hash.info/)

---

*Document created: February 15, 2026*
*Last updated: February 15, 2026*
