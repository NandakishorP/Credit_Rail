// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {HonkVerifier} from "../src-zk/Verifier.sol";

contract DeployVerifier is Script {
    function run() external returns (address) {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");

        vm.startBroadcast(deployerPrivateKey);

        HonkVerifier verifier = new HonkVerifier();

        vm.stopBroadcast();

        console2.log("HonkVerifier deployed at:", address(verifier));

        return address(verifier);
    }
}
