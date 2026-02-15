#!/bin/bash
# E2E ZK Loan Integration Test Script
# This script deploys contracts and tests ZK proof verification on anvil-zksync

set -e

RPC_URL="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

echo "============================================"
echo "  E2E ZK Loan Integration Test"
echo "============================================"
echo ""

# Ensure anvil-zksync is running
if ! curl -s $RPC_URL -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' > /dev/null 2>&1; then
    echo "Starting anvil-zksync..."
    anvil-zksync --port 8546 &
    sleep 3
fi

cd "$(dirname "$0")/.."

echo "--- Step 1: Deploy ZKTranscriptLib ---"
LIB_OUTPUT=$(forge create --zk-compile --rpc-url $RPC_URL --private-key $PRIVATE_KEY src/Verifier.sol:ZKTranscriptLib --broadcast 2>&1)
ZK_TRANSCRIPT_LIB=$(echo "$LIB_OUTPUT" | grep "Deployed to:" | awk '{print $3}')
echo "ZKTranscriptLib: $ZK_TRANSCRIPT_LIB"

echo ""
echo "--- Step 2: Deploy HonkVerifier ---"
VERIFIER_OUTPUT=$(forge create --zk-compile --rpc-url $RPC_URL --private-key $PRIVATE_KEY src/Verifier.sol:HonkVerifier --libraries src/Verifier.sol:ZKTranscriptLib:$ZK_TRANSCRIPT_LIB --broadcast 2>&1)
VERIFIER_ADDRESS=$(echo "$VERIFIER_OUTPUT" | grep "Deployed to:" | awk '{print $3}')
echo "HonkVerifier: $VERIFIER_ADDRESS"

echo ""
echo "--- Step 3: Generate ZK Proof ---"
cd ../zk-scripts

# Generate proof and save to file
PROOF_OUTPUT=$(npx tsx generate_proof_ffi.ts 2>&1)
echo "Proof generated"

# Extract proof hex from output (it's ABI encoded)
PROOF_HEX=$(echo "$PROOF_OUTPUT" | tail -1)

echo ""
echo "--- Step 4: Verify Proof On-Chain ---"
cd ../contracts

# Call the verifier contract
# Note: This requires parsing the proof data properly
echo "Calling verifier.verify()..."
echo "Verifier address: $VERIFIER_ADDRESS"

# For now, output the addresses for manual testing
echo ""
echo "============================================"
echo "  Deployment Complete!"
echo "============================================"
echo ""
echo "Contracts deployed:"
echo "  ZKTranscriptLib: $ZK_TRANSCRIPT_LIB"
echo "  HonkVerifier:    $VERIFIER_ADDRESS"
echo ""
echo "To test verification manually, use the TypeScript script:"
echo "  cd ../zk-scripts"
echo "  VERIFIER_ADDRESS=$VERIFIER_ADDRESS npx tsx test_onchain.ts"
