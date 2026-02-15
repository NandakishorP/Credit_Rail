// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Field} from "@poseidon2-evm/Field.sol";

/**
 * @title IPoseidon2
 * @notice Interface for Poseidon2 hash function
 */
interface IPoseidon2 {
    function hash_1(Field.Type x) external pure returns (Field.Type);

    function hash_2(
        Field.Type x,
        Field.Type y
    ) external pure returns (Field.Type);

    function hash_3(
        Field.Type x,
        Field.Type y,
        Field.Type z
    ) external pure returns (Field.Type);

    function hash(Field.Type[] memory input) external pure returns (Field.Type);

    function hash(
        Field.Type[] memory input,
        uint256 std_input_length,
        bool is_variable_length
    ) external pure returns (Field.Type);
}
