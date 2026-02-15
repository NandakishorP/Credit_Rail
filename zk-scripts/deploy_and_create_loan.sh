#!/bin/bash
# Deploy all contracts to anvil-zksync and prepare for loan creation

set -e

CONTRACTS_DIR="/Users/admin/Desktop/credit_rail/contracts"
RPC_URL="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
DEPLOYER="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

cd "$CONTRACTS_DIR"

echo "============================================================"
echo "Deploying contracts to anvil-zksync"
echo "============================================================"

# 1. Deploy ZKTranscriptLib
echo -e "\n1. Deploying ZKTranscriptLib..."
TRANSCRIPT_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/Verifier.sol:ZKTranscriptLib 2>&1)
TRANSCRIPT_LIB=$(echo "$TRANSCRIPT_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   ZKTranscriptLib: $TRANSCRIPT_LIB"

# 2. Deploy HonkVerifier with library linking
echo -e "\n2. Deploying HonkVerifier..."
VERIFIER_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" \
  --libraries "src/Verifier.sol:ZKTranscriptLib:$TRANSCRIPT_LIB" \
  src/Verifier.sol:HonkVerifier 2>&1)
VERIFIER=$(echo "$VERIFIER_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   HonkVerifier: $VERIFIER"

# 3. Deploy MockPoseidon2
echo -e "\n3. Deploying MockPoseidon2..."
POSEIDON_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" test/mocks/MockPoseidon2.sol:MockPoseidon2 2>&1)
POSEIDON=$(echo "$POSEIDON_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   MockPoseidon2: $POSEIDON"

# 4. Deploy CreditPolicy
echo -e "\n4. Deploying CreditPolicy..."
POLICY_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/CreditPolicy.sol:CreditPolicy --constructor-args "$DEPLOYER" 2>&1)
POLICY=$(echo "$POLICY_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   CreditPolicy: $POLICY"

# 5. Deploy ERC20Mock (USDC)
echo -e "\n5. Deploying USDC Mock..."
USDC_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" test/mocks/ERC20Mock.sol:ERC20Mock --constructor-args "USD Coin" "USDC" 2>&1)
USDC=$(echo "$USDC_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   USDC: $USDC"

# 6. Deploy TranchePool
echo -e "\n6. Deploying TranchePool..."
POOL_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" src/TranchePool.sol:TranchePool --constructor-args "$USDC" "$DEPLOYER" 2>&1)
POOL=$(echo "$POOL_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   TranchePool: $POOL"

# 7. Deploy LoanEngine
echo -e "\n7. Deploying LoanEngine..."
ENGINE_OUT=$(forge create --zk-compile --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" \
  src/LoanEngine.sol:LoanEngine \
  --constructor-args "$POLICY" "$POOL" "$VERIFIER" "$POSEIDON" 2>&1)
ENGINE=$(echo "$ENGINE_OUT" | grep "Deployed to:" | awk '{print $3}')
echo "   LoanEngine: $ENGINE"

# Output environment variables
echo ""
echo "============================================================"
echo "Deployment Complete! Export these environment variables:"
echo "============================================================"
echo "export LOAN_ENGINE=$ENGINE"
echo "export CREDIT_POLICY=$POLICY"
echo "export TRANCHE_POOL=$POOL"
echo "export USDC=$USDC"
echo "export VERIFIER=$VERIFIER"
echo "export POSEIDON=$POSEIDON"
echo "export RPC_URL=$RPC_URL"

# Write to a file for easy sourcing
cat > /Users/admin/Desktop/credit_rail/zk-scripts/.env.deployed <<EOF
LOAN_ENGINE=$ENGINE
CREDIT_POLICY=$POLICY
TRANCHE_POOL=$POOL
USDC=$USDC
VERIFIER=$VERIFIER
POSEIDON=$POSEIDON
RPC_URL=$RPC_URL
EOF

echo ""
echo "Environment saved to: zk-scripts/.env.deployed"
echo ""
echo "Now run: cd /Users/admin/Desktop/credit_rail/zk-scripts && source .env.deployed && npx tsx create_loan.ts"
