#!/bin/bash
# ZK Proof Integration Test Script
# Tests that Noir circuit proofs can be verified by HonkVerifier on Anvil

set -e

CONTRACTS_DIR="/Users/admin/Desktop/credit_rail/contracts"
ZK_SCRIPTS_DIR="/Users/admin/Desktop/credit_rail/zk-scripts"
ANVIL_RPC="http://127.0.0.1:8545"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

echo "============================================"
echo "   ZK Proof Integration Test"
echo "============================================"

# Step 1: Build with zksolc
echo ""
echo "Step 1: Building contracts with zksolc..."
cd "$CONTRACTS_DIR"
forge build --zksync

# Step 2: Deploy the HonkVerifier
echo ""
echo "Step 2: Deploying HonkVerifier to Anvil..."

# Deploy and capture the address
DEPLOY_OUTPUT=$(forge script script/DeployVerifier.s.sol \
    --rpc-url "$ANVIL_RPC" \
    --private-key "$PRIVATE_KEY" \
    --broadcast \
    --skip-simulation \
    2>&1)

echo "$DEPLOY_OUTPUT"

# Extract verifier address from output
VERIFIER_ADDRESS=$(echo "$DEPLOY_OUTPUT" | grep -oE "0x[a-fA-F0-9]{40}" | tail -1)

if [ -z "$VERIFIER_ADDRESS" ]; then
    echo "ERROR: Failed to extract verifier address"
    exit 1
fi

echo ""
echo "Verifier deployed at: $VERIFIER_ADDRESS"

# Step 3: Generate a ZK proof using the TypeScript script
echo ""
echo "Step 3: Generating ZK proof..."
cd "$ZK_SCRIPTS_DIR"

# Generate proof and get hex output
PROOF_OUTPUT=$(npx ts-node generate_proof_ffi.ts 2>&1)
echo "$PROOF_OUTPUT" | head -5

# Step 4: Call the verifier with the proof
echo ""
echo "Step 4: Verifying proof on-chain..."
cd "$CONTRACTS_DIR"

# Use cast to call the verifier
# First, let's create a simple verification call
VERIFIER_ADDRESS="$VERIFIER_ADDRESS" \
PRIVATE_KEY="$PRIVATE_KEY" \
forge script script/TestZkProof.s.sol \
    --rpc-url "$ANVIL_RPC" \
    --broadcast \
    --ffi \
    -vvv

echo ""
echo "============================================"
echo "   Integration Test Complete!"
echo "============================================"
