#!/bin/bash
# Full deploy + policy setup + create loan test
set -e

cd /Users/admin/Desktop/credit_rail/zk-scripts

echo "Step 1: Deploy all contracts..."
bash full_deploy.sh

echo ""
echo "Step 2: Set up policy version 2 with Poseidon2 scope hash..."

# Load the deployed addresses
source /Users/admin/Desktop/credit_rail/zk-scripts/.env.deployed

RPC_URL="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
POLICY="$CREDIT_POLICY"
SCOPE_HASH="0x1cf25e17e3e03cd06259fb4eca69a2317651ec700354473fed420a8a6a399a66"

cd /Users/admin/Desktop/credit_rail/contracts

echo "  Creating policy 2..."
cast send "$POLICY" "createPolicy(uint256)" 2 --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting eligibility..."
cast send "$POLICY" "updateEligibility(uint256,(uint256,uint256,uint256,uint256,uint256,bool))" 2 "(1000000,100000,250000,730,0,true)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting ratios..."
cast send "$POLICY" "updateRatios(uint256,(uint256,uint256,uint256,uint256))" 2 "(40000,15000,12000,1000)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting concentration..."
cast send "$POLICY" "updateConcentration(uint256,(uint256,uint256))" 2 "(1000,2500)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting attestation..."
cast send "$POLICY" "updateAttestation(uint256,(uint256,uint256,bool))" 2 "(90,365,false)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting covenants..."
cast send "$POLICY" "updateCovenants(uint256,(uint256,uint256,uint256,bool,uint256))" 2 "(50000,10000,50000,true,90)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting loan tier..."
cast send "$POLICY" 'setLoanTier(uint256,uint8,(string,uint256,uint256,uint256,uint256,uint256,uint256,uint256,uint256,bool))' 2 1 '("Standard",1000000,10000000,100000,40000,1000000000000000000,1200,100,365,true)' --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting policy document..."
DOC_HASH=$(cast keccak "policy_document_v2")
cast send "$POLICY" "setPolicyDocument(uint256,bytes32,string)" 2 "$DOC_HASH" "ipfs://test" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Setting scope hash (Poseidon2)..."
cast send "$POLICY" "setPolicyScopeHash(uint256,bytes32)" 2 "$SCOPE_HASH" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  Freezing policy..."
cast send "$POLICY" "freezePolicy(uint256)" 2 --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null 2>&1

echo "  ✅ Policy 2 frozen with Poseidon2 scope hash!"

echo ""
echo "Step 3: Run create_loan.ts to create loan with ZK proof..."
cd /Users/admin/Desktop/credit_rail/zk-scripts

# Export the environment variables for create_loan.ts
export LOAN_ENGINE
export CREDIT_POLICY
export TRANCHE_POOL
export USDC
export VERIFIER
export RPC_URL

# Sleep briefly to let the nonce sync
sleep 2

npx tsx create_loan.ts 2>&1
