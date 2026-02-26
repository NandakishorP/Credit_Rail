// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../src/LoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {MockLoanProofVerifier} from "./MockLoanProofVerifier.sol";
import {ProtocolController} from "../../src/ProtocolController.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

// This contract forces Wake to compile these external dependencies for Python fuzzing
contract WakeImports {

}

import {Field} from "@poseidon2-evm/Field.sol";

contract MockPoseidon2 {
    function hash(
        Field.Type[] memory input
    ) external pure returns (Field.Type) {
        return Field.toField(uint256(0));
    }
}
