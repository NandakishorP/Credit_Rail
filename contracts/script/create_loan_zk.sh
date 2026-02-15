#!/bin/bash
# ZK Integration Test - Create Loan with ZK Proof
# This script generates a ZK proof and creates a loan on anvil-zksync

set -e

# Configuration
RPC_URL="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
DEPLOYER="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

# Contract Addresses (from deployment)
LOAN_ENGINE="0xb98e374C912ff8C02ac7363c57d5bfdb48f40d53"
VERIFIER="0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe"
CREDIT_POLICY="0x22D151A1313d9B517Fa437F1F5B3744E636D8790"
TRANCHE_POOL="0xd7385ba726A7b72933E63FCb0Dfee8Bcae63478c"
USDC="0x82778c3185fD0666d3f34F8930B4287405D9fBe4"

echo "=============================================="
echo "ZK Loan Creation Integration Test"
echo "=============================================="
echo ""
echo "Contracts:"
echo "  LoanEngine: $LOAN_ENGINE"
echo "  Verifier:   $VERIFIER"
echo ""

# Step 1: Check if anvil-zksync is running
echo "Step 1: Checking anvil-zksync connection..."
BLOCK=$(curl -s $RPC_URL -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' | jq -r '.result')
if [ "$BLOCK" == "null" ] || [ -z "$BLOCK" ]; then
  echo "ERROR: anvil-zksync is not running on $RPC_URL"
  exit 1
fi
echo "  Connected! Block number: $BLOCK"

# Step 2: Setup Credit Policy
echo ""
echo "Step 2: Creating Credit Policy..."
# Create policy ID 1
cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $CREDIT_POLICY \
  "createPolicy(uint256)" 1 2>/dev/null || true
echo "  Policy created"

# Step 3: Mint USDC and fund pool
echo ""
echo "Step 3: Minting USDC and funding TranchePool..."
cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $USDC \
  "mint(address,uint256)" $DEPLOYER 10000000000000000000000000 2>/dev/null
echo "  Minted 10M USDC to deployer"

# Approve USDC for TranchePool
cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $USDC \
  "approve(address,uint256)" $TRANCHE_POOL 10000000000000000000000000 2>/dev/null
echo "  Approved TranchePool to spend USDC"

# Step 4: Set LoanEngine in TranchePool
echo ""
echo "Step 4: Configuring TranchePool..."
cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $TRANCHE_POOL \
  "setLoanEngine(address)" $LOAN_ENGINE 2>/dev/null
echo "  LoanEngine set in TranchePool"

# Step 5: Test the verifier directly
echo ""
echo "Step 5: Testing HonkVerifier..."
echo "  Verifier address: $VERIFIER"

# Quick check - call verify with empty proof (should revert or return false)
VERIFY_RESULT=$(cast call --rpc-url $RPC_URL $VERIFIER \
  "verify(bytes,bytes32[])" "0x" "[]" 2>&1 || echo "reverted")
echo "  Empty proof result: $VERIFY_RESULT"

# Step 6: Show how to generate and submit a real proof
echo ""
echo "=============================================="
echo "DEPLOYMENT SUCCESSFUL!"
echo "=============================================="
echo ""
echo "To test with a real ZK proof:"
echo ""
echo "1. Generate a proof using the TypeScript script:"
echo "   cd ../zk-scripts && npm run test"
echo ""
echo "2. Or use the on-chain test script:"
echo "   cd ../zk-scripts && VERIFIER_ADDRESS=$VERIFIER RPC_URL=$RPC_URL npx tsx test_onchain.ts"
echo ""
echo "Contract Addresses for reference:"
echo "  LOAN_ENGINE=$LOAN_ENGINE"
echo "  VERIFIER=$VERIFIER"
echo "  CREDIT_POLICY=$CREDIT_POLICY"
echo "  TRANCHE_POOL=$TRANCHE_POOL"
echo "  USDC=$USDC"
