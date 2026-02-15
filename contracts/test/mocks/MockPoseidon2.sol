// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Field} from "@poseidon2-evm/Field.sol";
import {IPoseidon2} from "../../src/interfaces/IPoseidon2.sol";

/**
 * @title MockPoseidon2
 * @notice A mock Poseidon2 hasher for testing that returns deterministic hashes
 *         without the complex assembly that causes stack depth issues in standard solc.
 */
contract MockPoseidon2 is IPoseidon2 {
    using Field for *;

    // BN254 scalar field modulus
    uint256 constant FIELD_MODULUS =
        21888242871839275222246405745257275088548364400416034343698204186575808495617;

    function _toFieldSafe(uint256 value) internal pure returns (Field.Type) {
        return Field.toField(value % FIELD_MODULUS);
    }

    function hash_1(Field.Type x) public pure returns (Field.Type) {
        return _toFieldSafe(uint256(keccak256(abi.encode(x))));
    }

    function hash_2(
        Field.Type x,
        Field.Type y
    ) public pure returns (Field.Type) {
        return _toFieldSafe(uint256(keccak256(abi.encode(x, y))));
    }

    function hash_3(
        Field.Type x,
        Field.Type y,
        Field.Type z
    ) public pure returns (Field.Type) {
        return _toFieldSafe(uint256(keccak256(abi.encode(x, y, z))));
    }

    function hash(Field.Type[] memory input) public pure returns (Field.Type) {
        return _toFieldSafe(uint256(keccak256(abi.encode(input))));
    }

    function hash(
        Field.Type[] memory input,
        uint256 std_input_length,
        bool is_variable_length
    ) public pure returns (Field.Type) {
        return
            _toFieldSafe(
                uint256(
                    keccak256(
                        abi.encode(input, std_input_length, is_variable_length)
                    )
                )
            );
    }
}
