// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {HonkVerifier} from "../src/Verifier.sol";

/**
 * @title TestZkProof
 * @notice Script to test ZK proof verification on Anvil
 * @dev Run with: forge script script/TestZkProof.s.sol --rpc-url http://127.0.0.1:8545 --broadcast
 */
contract TestZkProof is Script {
    function run() external {
        // Get verifier address from env
        address verifierAddress = vm.envAddress("VERIFIER_ADDRESS");
        HonkVerifier verifier = HonkVerifier(verifierAddress);

        console2.log("Testing ZK proof verification...");
        console2.log("Verifier address:", verifierAddress);

        // Run FFI to generate proof
        string[] memory cmds = new string[](3);
        cmds[0] = "npx";
        cmds[1] = "ts-node";
        cmds[2] = "../zk-scripts/generate_proof_ffi.ts";

        bytes memory result = vm.ffi(cmds);

        // Decode the ABI-encoded result
        (bytes memory proofData, bytes32[] memory publicInputs) = abi.decode(
            result,
            (bytes, bytes32[])
        );

        console2.log("Proof generated successfully");
        console2.log("Proof length:", proofData.length);
        console2.log("Public inputs count:", publicInputs.length);

        // Call the verifier
        bool isValid = verifier.verify(proofData, publicInputs);

        if (isValid) {
            console2.log("SUCCESS: ZK proof verified on-chain!");
        } else {
            console2.log("FAILED: ZK proof verification failed");
            revert("Proof verification failed");
        }
    }
}
