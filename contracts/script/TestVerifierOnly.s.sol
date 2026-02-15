// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {HonkVerifier} from "../src-zk/Verifier.sol";
import {IVerifier} from "../src/interfaces/IVerifier.sol";

/**
 * @title TestVerifierOnly
 * @notice Simple test: Deploy verifier and verify a proof
 *
 * Usage:
 * forge script script/TestVerifierOnly.s.sol:TestVerifierOnly \
 *   --zk-compile --rpc-url http://127.0.0.1:8546 \
 *   --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 \
 *   --broadcast --ffi -vvv
 */
contract TestVerifierOnly is Script {
    function run() external {
        uint256 deployerPrivateKey = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80;
        address deployer = vm.addr(deployerPrivateKey);

        console2.log("============================================");
        console2.log("  ZK Proof Verification Test");
        console2.log("============================================");
        console2.log("");
        console2.log("Deployer:", deployer);

        vm.startBroadcast(deployerPrivateKey);

        // Deploy verifier
        console2.log("");
        console2.log("--- Deploying HonkVerifier ---");
        HonkVerifier verifier = new HonkVerifier();
        console2.log("Verifier deployed at:", address(verifier));

        vm.stopBroadcast();

        // Generate proof via FFI
        console2.log("");
        console2.log("--- Generating ZK Proof via FFI ---");

        string[] memory ffiCmd = new string[](3);
        ffiCmd[0] = "npx";
        ffiCmd[1] = "tsx";
        ffiCmd[2] = "../zk-scripts/generate_proof_ffi.ts";

        bytes memory ffiResult = vm.ffi(ffiCmd);

        // Only decode what we need for verification
        (bytes memory proofData, bytes32[] memory publicInputs) = abi.decode(
            ffiResult,
            (bytes, bytes32[])
        );

        console2.log("Proof generated!");
        console2.log("  Proof size:", proofData.length, "bytes");
        console2.log("  Public inputs:", publicInputs.length);

        // Verify on-chain
        console2.log("");
        console2.log("--- On-Chain Verification ---");

        bool isValid = verifier.verify(proofData, publicInputs);

        if (isValid) {
            console2.log("");
            console2.log("============================================");
            console2.log("  SUCCESS! ZK PROOF VERIFIED ON-CHAIN!");
            console2.log("============================================");
        } else {
            console2.log("");
            console2.log("FAILED: Proof verification returned false");
            revert("Verification failed");
        }
    }
}
