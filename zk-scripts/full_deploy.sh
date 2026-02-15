#!/bin/bash
# Complete deployment and setup for ZK loan creation
set -e

RPC_URL="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
DEPLOYER="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
CONTRACTS_DIR="/Users/admin/Desktop/credit_rail/contracts"

cd "$CONTRACTS_DIR"

echo "============================================================"
echo "Deploying all contracts to anvil-zksync"
echo "============================================================"

# Deploy contracts
echo "1. Deploying ZKTranscriptLib..."
TRANSCRIPT=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/Verifier.sol:ZKTranscriptLib 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   ZKTranscriptLib: $TRANSCRIPT"

echo "2. Deploying HonkVerifier..."
VERIFIER=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" --libraries "src/Verifier.sol:ZKTranscriptLib:$TRANSCRIPT" src/Verifier.sol:HonkVerifier 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   HonkVerifier: $VERIFIER"

echo "3. Deploying MockPoseidon2..."
POSEIDON=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" test/mocks/MockPoseidon2.sol:MockPoseidon2 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   MockPoseidon2: $POSEIDON"

echo "4. Deploying CreditPolicy..."
POLICY=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/CreditPolicy.sol:CreditPolicy --constructor-args "$DEPLOYER" 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   CreditPolicy: $POLICY"

echo "5. Deploying ERC20Mock (USDC)..."
USDC=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   USDC: $USDC"

echo "6. Deploying TranchePool..."
POOL=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/TranchePool.sol:TranchePool --constructor-args "$USDC" "$DEPLOYER" 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   TranchePool: $POOL"

echo "7. Deploying LoanEngine..."
ENGINE=$(forge create --zk-compile --broadcast --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/LoanEngine.sol:LoanEngine --constructor-args "$POLICY" "$VERIFIER" "500" "$POOL" "$USDC" "$POSEIDON" 2>&1 | grep "Deployed to:" | awk '{print $3}')
echo "   LoanEngine: $ENGINE"

echo ""
echo "============================================================"
echo "Setting up CreditPolicy..."
echo "============================================================"

# Create policy version 1
cast send "$POLICY" "createPolicy(uint256)" 1 --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Created policy version 1"

# Update eligibility
cast send "$POLICY" "updateEligibility(uint256,(uint256,uint256,uint256,uint256,uint256,bool))" 1 "(1000000,100000,250000,730,0,true)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set eligibility"

# Update ratios
cast send "$POLICY" "updateRatios(uint256,(uint256,uint256,uint256,uint256))" 1 "(40000,15000,12000,1000)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set ratios"

# Update concentration
cast send "$POLICY" "updateConcentration(uint256,(uint256,uint256))" 1 "(1000,2500)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set concentration"

# Update attestation
cast send "$POLICY" "updateAttestation(uint256,(uint256,uint256,bool))" 1 "(90,365,false)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set attestation"

# Update covenants
cast send "$POLICY" "updateCovenants(uint256,(uint256,uint256,uint256,bool,uint256))" 1 "(50000,10000,50000,true,90)" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set covenants"

# Set loan tier
cast send "$POLICY" "setLoanTier(uint256,uint8,(string,uint256,uint256,uint256,uint256,uint256,uint256,uint256,uint256,bool))" 1 1 '("Standard",1000000,10000000,100000,40000,1000000000000000000,1200,100,365,true)' --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set loan tier"

# Set policy document
DOC_HASH=$(cast keccak "policy_document_v1")
cast send "$POLICY" "setPolicyDocument(uint256,bytes32,string)" 1 "$DOC_HASH" "ipfs://test" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set policy document"

# Set policy scope hash
SCOPE_HASH=$(cast keccak "policy_scope_v1")
cast send "$POLICY" "setPolicyScopeHash(uint256,bytes32)" 1 "$SCOPE_HASH" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Set policy scope hash"

# Freeze policy
cast send "$POLICY" "freezePolicy(uint256)" 1 --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   ✅ Policy frozen!"

echo ""
echo "============================================================"
echo "Setting up TranchePool..."
echo "============================================================"

# Whitelist LoanEngine
cast send "$POOL" "whitelistAddress(address)" "$ENGINE" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Whitelisted LoanEngine"

# Mint USDC
cast send "$USDC" "mint(address,uint256)" "$DEPLOYER" "10000000000000000000000000" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Minted USDC"

# Transfer USDC to pool
cast send "$USDC" "transfer(address,uint256)" "$POOL" "5000000000000000000000000" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Transferred USDC to pool"

# Commit pool
cast send "$POOL" "commit()" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Committed pool"

# Deploy pool
cast send "$POOL" "deploy()" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   Deployed pool"

# Allocate capital
cast send "$POOL" "allocateCapital(address,uint256)" "$ENGINE" "1000000000000000000000000" --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" > /dev/null
echo "   ✅ Allocated capital to LoanEngine"

echo ""
echo "============================================================"
echo "DEPLOYMENT COMPLETE!"
echo "============================================================"
echo ""
echo "export LOAN_ENGINE=$ENGINE"
echo "export CREDIT_POLICY=$POLICY"
echo "export TRANCHE_POOL=$POOL"
echo "export USDC=$USDC"
echo "export VERIFIER=$VERIFIER"
echo "export POSEIDON=$POSEIDON"
echo "export RPC_URL=$RPC_URL"
echo ""

# Save to env file
cat > /Users/admin/Desktop/credit_rail/zk-scripts/.env.deployed <<EOF
LOAN_ENGINE=$ENGINE
CREDIT_POLICY=$POLICY
TRANCHE_POOL=$POOL
USDC=$USDC
VERIFIER=$VERIFIER
POSEIDON=$POSEIDON
RPC_URL=$RPC_URL
EOF

echo "Environment saved to: zk-scripts/.env.deployed"
