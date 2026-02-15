// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {LoanEngine} from "../src/LoanEngine.sol";

contract DeployLoanEngine is Script {
    function run() external {
        // Constructor arguments
        address creditPolicy = 0x22D151A1313d9B517Fa437F1F5B3744E636D8790;
        address verifier = 0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe;
        uint256 maxOriginationFeeBps = 500;
        address tranchePool = 0xd7385ba726A7b72933E63FCb0Dfee8Bcae63478c;
        address stableCoin = 0x82778c3185fD0666d3f34F8930B4287405D9fBe4;
        address poseidon2 = 0x1B69c60F3ac12BC305C96D927573102f6617eb16; // Real Poseidon2

        vm.startBroadcast();

        LoanEngine engine = new LoanEngine(
            creditPolicy,
            verifier,
            maxOriginationFeeBps,
            tranchePool,
            stableCoin,
            poseidon2
        );

        console2.log("LoanEngine deployed to:", address(engine));

        vm.stopBroadcast();
    }
}
