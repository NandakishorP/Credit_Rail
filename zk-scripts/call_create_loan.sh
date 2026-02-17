#!/bin/bash
set -e

# Contract addresses
LOAN_ENGINE="0xb98e374C912ff8C02ac7363c57d5bfdb48f40d53"
RPC="http://127.0.0.1:8546"
PRIVATE_KEY="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

# Encode the createLoan call - we need the calldata from the last failed transaction
# The tx input data starts with function selector 0x1230a365

# First, let's check the next loan ID
NEXT_ID=$(cast call $LOAN_ENGINE "getNextLoanId()" --rpc-url $RPC)
echo "Next loan ID: $NEXT_ID"

# Actually, let's just call create_loan.ts but with the transaction via cast
# Extract proof and params...

# The simplest approach is to restart anvil to reset nonces
echo "The nonce desync issue requires restarting anvil-zksync"
echo "Or we can try a signed raw transaction approach"

