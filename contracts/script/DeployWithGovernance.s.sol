// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {LoanEngine} from "../src/LoanEngine.sol";
import {CreditPolicy} from "../src/CreditPolicy.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ProtocolController} from "../src/ProtocolController.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {Poseidon2} from "@poseidon2-evm/Poseidon2.sol";
import {HonkVerifier} from "../src-zk/Verifier.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {IAccessControl} from "@openzeppelin/contracts/access/IAccessControl.sol";

/**
 * @title DeployWithGovernance
 * @notice Full production deployment: UUPS proxies + ProtocolController timelock
 *
 * This script demonstrates the complete deployment and governance handoff:
 *   1. Deploy all core contracts behind ERC1967 proxies
 *   2. Deploy the ProtocolController (TimelockController)
 *   3. Grant DEFAULT_ADMIN_ROLE on all contracts to the ProtocolController
 *   4. Deployer renounces all admin privileges
 *
 * After this script completes, the deployer holds ZERO admin rights.
 * All governance flows through the ProtocolController timelock.
 *
 * Usage:
 * forge script script/DeployWithGovernance.s.sol:DeployWithGovernance \
 *   --rpc-url <RPC_URL> --private-key <PK> --broadcast -vvv
 */
contract DeployWithGovernance is Script {
    // Deployment addresses
    address public creditPolicyProxy;
    address public tranchePoolProxy;
    address public loanEngineProxy;
    address public protocolController;

    function run() external {
        uint256 deployerPrivateKey = vm.envOr(
            "PRIVATE_KEY",
            uint256(
                0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
            )
        );
        address deployer = vm.addr(deployerPrivateKey);

        // In production, this would be a Gnosis Safe address
        address multisig = vm.envOr("MULTISIG_ADDRESS", deployer);
        // Optional guardian that can cancel pending timelock operations
        address guardian = vm.envOr("GUARDIAN_ADDRESS", address(0));
        // Timelock delay: 48 hours for production, 1 minute for testing
        uint256 timelockDelay = vm.envOr("TIMELOCK_DELAY", uint256(48 hours));

        console2.log("============================================");
        console2.log("  Credit Rail: Full Governance Deployment");
        console2.log("============================================");
        console2.log("");
        console2.log("Deployer:", deployer);
        console2.log("Multisig:", multisig);
        console2.log("Guardian:", guardian);
        console2.log("Timelock Delay:", timelockDelay, "seconds");
        console2.log("");

        vm.startBroadcast(deployerPrivateKey);

        // ====================================================
        // PHASE 1: Deploy Infrastructure
        // ====================================================
        console2.log("--- Phase 1: Infrastructure ---");

        ERC20Mock usdc = new ERC20Mock();
        console2.log("[1/7] USDC Mock:", address(usdc));

        Poseidon2 poseidon2 = new Poseidon2();
        console2.log("[2/7] Poseidon2:", address(poseidon2));

        HonkVerifier verifier = new HonkVerifier();
        console2.log("[3/7] HonkVerifier:", address(verifier));

        // ====================================================
        // PHASE 2: Deploy Core Contracts via UUPS Proxies
        // ====================================================
        console2.log("");
        console2.log("--- Phase 2: Core Contracts (UUPS Proxies) ---");

        // CreditPolicy
        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer))
        );
        creditPolicyProxy = address(cpProxy);
        console2.log("[4/7] CreditPolicy proxy:", creditPolicyProxy);

        // TranchePool
        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (address(usdc), deployer))
        );
        tranchePoolProxy = address(tpProxy);
        console2.log("[5/7] TranchePool proxy:", tranchePoolProxy);

        // LoanEngine
        LoanEngine leImpl = new LoanEngine();
        ERC1967Proxy leProxy = new ERC1967Proxy(
            address(leImpl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    creditPolicyProxy,
                    address(verifier),
                    1000, // maxOriginationFeeBps (10%)
                    tranchePoolProxy,
                    address(usdc),
                    address(poseidon2),
                    deployer
                )
            )
        );
        loanEngineProxy = address(leProxy);
        console2.log("[6/7] LoanEngine proxy:", loanEngineProxy);

        // Wire TranchePool to LoanEngine
        TranchePool(tranchePoolProxy).setLoanEngine(loanEngineProxy);
        console2.log("       TranchePool -> LoanEngine wired");

        // ====================================================
        // PHASE 3: Deploy ProtocolController (Timelock)
        // ====================================================
        console2.log("");
        console2.log("--- Phase 3: Governance (ProtocolController) ---");

        ProtocolController controller = new ProtocolController(
            timelockDelay,
            multisig,
            guardian
        );
        protocolController = address(controller);
        console2.log("[7/7] ProtocolController:", protocolController);

        // ====================================================
        // PHASE 4: Transfer Admin Rights to ProtocolController
        // ====================================================
        console2.log("");
        console2.log("--- Phase 4: Admin Transfer ---");

        bytes32 DEFAULT_ADMIN_ROLE = 0x00;

        // --- CreditPolicy: grant all roles to ProtocolController ---
        CreditPolicy cp = CreditPolicy(creditPolicyProxy);
        cp.grantRole(DEFAULT_ADMIN_ROLE, protocolController);
        cp.grantRole(cp.POLICY_ADMIN_ROLE(), protocolController);
        cp.grantRole(cp.POLICY_EDITOR_ROLE(), protocolController);
        cp.grantRole(cp.INDUSTRY_ADMIN_ROLE(), protocolController);
        console2.log("  CreditPolicy: granted all roles to controller");

        // --- TranchePool: grant all roles to ProtocolController ---
        TranchePool tp = TranchePool(tranchePoolProxy);
        tp.grantRole(DEFAULT_ADMIN_ROLE, protocolController);
        tp.grantRole(tp.POOL_ADMIN_ROLE(), protocolController);
        tp.grantRole(tp.CONFIG_ADMIN_ROLE(), protocolController);
        tp.grantRole(tp.WHITELIST_ADMIN_ROLE(), protocolController);
        tp.grantRole(tp.EMERGENCY_ADMIN_ROLE(), protocolController);
        tp.grantRole(tp.TREASURY_ROLE(), protocolController);
        console2.log("  TranchePool:  granted all roles to controller");

        // --- LoanEngine: grant all roles to ProtocolController ---
        LoanEngine le = LoanEngine(loanEngineProxy);
        le.grantRole(DEFAULT_ADMIN_ROLE, protocolController);
        le.grantRole(le.FUND_MANAGER_ROLE(), protocolController);
        le.grantRole(le.SERVICER_ROLE(), protocolController);
        le.grantRole(le.RISK_ADMIN_ROLE(), protocolController);
        le.grantRole(le.CONFIG_ADMIN_ROLE(), protocolController);
        le.grantRole(le.EMERGENCY_ADMIN_ROLE(), protocolController);
        console2.log("  LoanEngine:   granted all roles to controller");

        // ====================================================
        // PHASE 5: Deployer Renounces All Admin Privileges
        // ====================================================
        console2.log("");
        console2.log("--- Phase 5: Deployer Renounces ---");

        // CreditPolicy
        cp.renounceRole(DEFAULT_ADMIN_ROLE, deployer);
        cp.renounceRole(cp.POLICY_ADMIN_ROLE(), deployer);
        cp.renounceRole(cp.POLICY_EDITOR_ROLE(), deployer);
        cp.renounceRole(cp.INDUSTRY_ADMIN_ROLE(), deployer);
        console2.log("  CreditPolicy: deployer renounced all roles");

        // TranchePool
        tp.renounceRole(DEFAULT_ADMIN_ROLE, deployer);
        tp.renounceRole(tp.POOL_ADMIN_ROLE(), deployer);
        tp.renounceRole(tp.CONFIG_ADMIN_ROLE(), deployer);
        tp.renounceRole(tp.WHITELIST_ADMIN_ROLE(), deployer);
        tp.renounceRole(tp.EMERGENCY_ADMIN_ROLE(), deployer);
        tp.renounceRole(tp.TREASURY_ROLE(), deployer);
        console2.log("  TranchePool:  deployer renounced all roles");

        // LoanEngine
        le.renounceRole(DEFAULT_ADMIN_ROLE, deployer);
        le.renounceRole(le.FUND_MANAGER_ROLE(), deployer);
        le.renounceRole(le.SERVICER_ROLE(), deployer);
        le.renounceRole(le.RISK_ADMIN_ROLE(), deployer);
        le.renounceRole(le.CONFIG_ADMIN_ROLE(), deployer);
        le.renounceRole(le.EMERGENCY_ADMIN_ROLE(), deployer);
        console2.log("  LoanEngine:   deployer renounced all roles");

        vm.stopBroadcast();

        // ====================================================
        // PHASE 6: Verification
        // ====================================================
        console2.log("");
        console2.log("--- Verification ---");

        // Verify deployer has NO admin
        bool deployerHasAdmin;

        deployerHasAdmin = cp.hasRole(DEFAULT_ADMIN_ROLE, deployer);
        require(
            !deployerHasAdmin,
            "FAIL: deployer still admin on CreditPolicy"
        );
        console2.log("  CreditPolicy: deployer has NO admin  [OK]");

        deployerHasAdmin = tp.hasRole(DEFAULT_ADMIN_ROLE, deployer);
        require(!deployerHasAdmin, "FAIL: deployer still admin on TranchePool");
        console2.log("  TranchePool:  deployer has NO admin  [OK]");

        deployerHasAdmin = le.hasRole(DEFAULT_ADMIN_ROLE, deployer);
        require(!deployerHasAdmin, "FAIL: deployer still admin on LoanEngine");
        console2.log("  LoanEngine:   deployer has NO admin  [OK]");

        // Verify ProtocolController IS admin
        bool controllerIsAdmin;

        controllerIsAdmin = cp.hasRole(DEFAULT_ADMIN_ROLE, protocolController);
        require(
            controllerIsAdmin,
            "FAIL: controller not admin on CreditPolicy"
        );
        console2.log("  CreditPolicy: controller IS admin    [OK]");

        controllerIsAdmin = tp.hasRole(DEFAULT_ADMIN_ROLE, protocolController);
        require(controllerIsAdmin, "FAIL: controller not admin on TranchePool");
        console2.log("  TranchePool:  controller IS admin    [OK]");

        controllerIsAdmin = le.hasRole(DEFAULT_ADMIN_ROLE, protocolController);
        require(controllerIsAdmin, "FAIL: controller not admin on LoanEngine");
        console2.log("  LoanEngine:   controller IS admin    [OK]");

        // ====================================================
        // Summary
        // ====================================================
        console2.log("");
        console2.log("============================================");
        console2.log("  Deployment Complete");
        console2.log("============================================");
        console2.log("");
        console2.log("  CreditPolicy:       ", creditPolicyProxy);
        console2.log("  TranchePool:         ", tranchePoolProxy);
        console2.log("  LoanEngine:          ", loanEngineProxy);
        console2.log("  ProtocolController:  ", protocolController);
        console2.log("");
        console2.log("  Deployer admin:       RENOUNCED");
        console2.log("  Governance via:       ProtocolController (timelock)");
        console2.log("  Timelock delay:      ", timelockDelay, "seconds");
        console2.log("");
        console2.log("  All future admin operations must be scheduled,");
        console2.log("  delayed, and executed through the ProtocolController.");
    }
}
