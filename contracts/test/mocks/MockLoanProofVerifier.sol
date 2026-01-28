// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract MockLoanProofVerifier {
    function verify(
        bytes calldata proof,
        bytes32[] calldata publicInputs
    ) external pure returns (bool) {
        return true;
    }
}
