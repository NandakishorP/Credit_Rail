// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {HonkVerifier} from "../src-zk/Verifier.sol";
import {LoanEngine} from "../src/LoanEngine.sol";
import {CreditPolicy} from "../src/CreditPolicy.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {Poseidon2} from "@poseidon2-evm/Poseidon2.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

/**
 * @title DeployFullSystem
 * @notice Deploys the full Credit Rail system to anvil-zksync
 *
 * Usage:
 * forge script script/DeployFullSystem.s.sol:DeployFullSystem \
 *   --zk-compile --rpc-url http://127.0.0.1:8546 \
 *   --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 \
 *   --broadcast -vvv
 */
contract DeployFullSystem is Script {
    // Deployed addresses (set after deployment)
    address public verifier;
    address public creditPolicy;
    address public tranchePool;
    address public loanEngine;
    address public stablecoin;
    address public poseidon2;

    function run() external {
        uint256 deployerPrivateKey = vm.envOr(
            "PRIVATE_KEY",
            uint256(
                0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
            )
        );
        address deployer = vm.addr(deployerPrivateKey);

        console2.log("Deployer:", deployer);
        console2.log("");

        vm.startBroadcast(deployerPrivateKey);

        // 1. Deploy Mock Stablecoin (USDC)
        ERC20Mock usdc = new ERC20Mock();
        stablecoin = address(usdc);
        console2.log("1. USDC Mock deployed at:", stablecoin);

        // 2. Deploy Poseidon2 hash function
        Poseidon2 _poseidon2 = new Poseidon2();
        poseidon2 = address(_poseidon2);
        console2.log("2. Poseidon2 deployed at:", poseidon2);

        // 3. Deploy HonkVerifier (ZK proof verifier)
        HonkVerifier _verifier = new HonkVerifier();
        verifier = address(_verifier);
        console2.log("3. HonkVerifier deployed at:", verifier);

        // 4. Deploy CreditPolicy via proxy
        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer, poseidon2))
        );
        creditPolicy = address(cpProxy);
        console2.log("4. CreditPolicy deployed at:", creditPolicy);

        // 5. Deploy TranchePool via proxy
        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (stablecoin, deployer))
        );
        tranchePool = address(tpProxy);
        console2.log("5. TranchePool deployed at:", tranchePool);

        // 6. Deploy LoanEngine via proxy
        LoanEngine leImpl = new LoanEngine();
        ERC1967Proxy leProxy = new ERC1967Proxy(
            address(leImpl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    creditPolicy,
                    verifier,
                    1000, // maxOriginationFeeBps (10%)
                    tranchePool,
                    stablecoin,
                    poseidon2,
                    deployer
                )
            )
        );
        loanEngine = address(leProxy);
        console2.log("6. LoanEngine deployed at:", loanEngine);

        // 7. Setup: Set LoanEngine as the engine for TranchePool
        TranchePool(tranchePool).setLoanEngine(loanEngine);
        console2.log("7. TranchePool engine set to LoanEngine");

        // 8. Mint some USDC for testing
        usdc.mint(deployer, 10_000_000 * 1e6); // 10M USDC
        usdc.mint(tranchePool, 1_000_000 * 1e6); // 1M USDC to pool
        console2.log("8. Minted USDC to deployer and pool");

        vm.stopBroadcast();

        console2.log("");
        console2.log("=== Deployment Complete ===");
        console2.log("");
        console2.log("Export these for the test script:");
        console2.log("export VERIFIER_ADDRESS=", verifier);
        console2.log("export LOAN_ENGINE_ADDRESS=", loanEngine);
        console2.log("export CREDIT_POLICY_ADDRESS=", creditPolicy);
        console2.log("export TRANCHE_POOL_ADDRESS=", tranchePool);
        console2.log("export STABLECOIN_ADDRESS=", stablecoin);
        console2.log("export POSEIDON2_ADDRESS=", poseidon2);
    }
}
