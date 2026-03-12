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
 * @notice Full production deployment with proper governance / operations role separation.
 *
 * ROLE SEPARATION:
 *
 *   ┌─────────────────────────────────────────────────────────────────────┐
 *   │  GOVERNANCE (ProtocolController — timelock + multisig, 48h delay)  │
 *   │                                                                     │
 *   │  • DEFAULT_ADMIN_ROLE  — upgrades, role grants/revokes             │
 *   │  • POOL_ADMIN_ROLE    — pool state changes, setLoanEngine          │
 *   │  • POLICY_ADMIN_ROLE  — create / freeze / deactivate policies      │
 *   └─────────────────────────────────────────────────────────────────────┘
 *
 *   ┌─────────────────────────────────────────────────────────────────────┐
 *   │  OPERATIONS (operations multisig — direct, NO timelock)            │
 *   │                                                                     │
 *   │  • FUND_MANAGER_ROLE    — create loans (bounded by ZK proof)       │
 *   │  • SERVICER_ROLE        — activate / repay / recover loans         │
 *   │  • RISK_ADMIN_ROLE      — declare defaults, write off loans        │
 *   │  • CONFIG_ADMIN_ROLE    — whitelists, underwriter keys, fees       │
 *   │  • WHITELIST_ADMIN_ROLE — LP deposit whitelist                     │
 *   │  • POLICY_EDITOR_ROLE   — edit unfrozen policy parameters          │
 *   │  • INDUSTRY_ADMIN_ROLE  — manage industry exclusions               │
 *   │  • TREASURY_ROLE        — sweep protocol revenue                   │
 *   └─────────────────────────────────────────────────────────────────────┘
 *
 *   ┌─────────────────────────────────────────────────────────────────────┐
 *   │  EMERGENCY (guardian wallet — direct, NO timelock)                  │
 *   │                                                                     │
 *   │  • EMERGENCY_ADMIN_ROLE — pause / unpause (must be instant)        │
 *   │  • Can also cancel pending timelock ops on ProtocolController      │
 *   └─────────────────────────────────────────────────────────────────────┘
 *
 * WHY THIS SEPARATION:
 *   - Governance roles change the protocol itself (upgrades, new contracts,
 *     lifecycle transitions). These are rare, high-impact, and must be delayed
 *     so the community / LPs can react.
 *   - Operational roles run daily business (originate loans, process repayments).
 *     Putting these behind a 48h delay would make the protocol unusable.
 *   - Emergency roles must be instant — you can't wait 48h to pause a hack.
 *
 * DEPLOYMENT FLOW:
 *   1. Deploy infrastructure (USDC mock, Poseidon2, HonkVerifier)
 *   2. Deploy core contracts via UUPS proxies (deployer as initialAdmin)
 *   3. Wire TranchePool ↔ LoanEngine
 *   4. Deploy ProtocolController (TimelockController)
 *   5. Grant GOVERNANCE roles to ProtocolController (timelock)
 *   6. Grant OPERATIONAL roles to operations multisig (direct)
 *   7. Grant EMERGENCY roles to guardian (direct)
 *   8. Deployer renounces ALL roles
 *   9. Verify final state
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

        // ── Governance multisig (proposer + executor on ProtocolController) ──
        address multisig = vm.envOr("MULTISIG_ADDRESS", deployer);

        // ── Operations multisig (daily loan ops, whitelists, etc.) ──
        address operationsMultisig = vm.envOr("OPERATIONS_MULTISIG", deployer);

        // ── Guardian (can pause instantly + cancel pending timelock ops) ──
        address guardian = vm.envOr("GUARDIAN_ADDRESS", address(0));

        // ── Timelock delay: 48h production, 60s testing ──
        uint256 timelockDelay = vm.envOr("TIMELOCK_DELAY", uint256(48 hours));

        console2.log("============================================");
        console2.log("  Credit Rail: Full Governance Deployment");
        console2.log("============================================");
        console2.log("");
        console2.log("Deployer:            ", deployer);
        console2.log("Governance Multisig: ", multisig);
        console2.log("Operations Multisig: ", operationsMultisig);
        console2.log("Guardian:            ", guardian);
        console2.log("Timelock Delay:      ", timelockDelay, "seconds");
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
            abi.encodeCall(CreditPolicy.initialize, (deployer, address(poseidon2)))
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
        // PHASE 4: Grant GOVERNANCE roles to ProtocolController
        //          (these go through the 48h timelock)
        // ====================================================
        console2.log("");
        console2.log(
            "--- Phase 4: Governance Roles -> ProtocolController (timelock) ---"
        );

        bytes32 DEFAULT_ADMIN_ROLE = 0x00;

        CreditPolicy cp = CreditPolicy(creditPolicyProxy);
        TranchePool tp = TranchePool(tranchePoolProxy);
        LoanEngine le = LoanEngine(loanEngineProxy);

        // DEFAULT_ADMIN_ROLE on all contracts (upgrades + role management)
        cp.grantRole(DEFAULT_ADMIN_ROLE, protocolController);
        tp.grantRole(DEFAULT_ADMIN_ROLE, protocolController);
        le.grantRole(DEFAULT_ADMIN_ROLE, protocolController);

        // POOL_ADMIN_ROLE (pool state transitions — rare, high-impact)
        tp.grantRole(tp.POOL_ADMIN_ROLE(), protocolController);

        // POLICY_ADMIN_ROLE (create/freeze/deactivate policies — rare, high-impact)
        cp.grantRole(cp.POLICY_ADMIN_ROLE(), protocolController);

        console2.log("  All contracts: DEFAULT_ADMIN_ROLE  -> controller");
        console2.log("  TranchePool:   POOL_ADMIN_ROLE     -> controller");
        console2.log("  CreditPolicy:  POLICY_ADMIN_ROLE   -> controller");

        // ====================================================
        // PHASE 5: Grant OPERATIONAL roles to operations multisig
        //          (these are direct — no timelock delay)
        // ====================================================
        console2.log("");
        console2.log(
            "--- Phase 5: Operational Roles -> Operations Multisig (direct) ---"
        );

        // LoanEngine operational roles
        le.grantRole(le.FUND_MANAGER_ROLE(), operationsMultisig);
        le.grantRole(le.SERVICER_ROLE(), operationsMultisig);
        le.grantRole(le.RISK_ADMIN_ROLE(), operationsMultisig);
        le.grantRole(le.CONFIG_ADMIN_ROLE(), operationsMultisig);
        console2.log(
            "  LoanEngine:    FUND_MANAGER / SERVICER / RISK_ADMIN / CONFIG_ADMIN -> ops"
        );

        // TranchePool operational roles
        tp.grantRole(tp.CONFIG_ADMIN_ROLE(), operationsMultisig);
        tp.grantRole(tp.WHITELIST_ADMIN_ROLE(), operationsMultisig);
        tp.grantRole(tp.TREASURY_ROLE(), operationsMultisig);
        console2.log(
            "  TranchePool:   CONFIG_ADMIN / WHITELIST_ADMIN / TREASURY -> ops"
        );

        // CreditPolicy operational roles
        cp.grantRole(cp.POLICY_EDITOR_ROLE(), operationsMultisig);
        cp.grantRole(cp.INDUSTRY_ADMIN_ROLE(), operationsMultisig);
        console2.log("  CreditPolicy:  POLICY_EDITOR / INDUSTRY_ADMIN -> ops");

        // ====================================================
        // PHASE 6: Grant EMERGENCY roles to guardian
        //          (must be instant — no timelock)
        // ====================================================
        console2.log("");
        console2.log("--- Phase 6: Emergency Roles -> Guardian (direct) ---");

        if (guardian != address(0)) {
            le.grantRole(le.EMERGENCY_ADMIN_ROLE(), guardian);
            tp.grantRole(tp.EMERGENCY_ADMIN_ROLE(), guardian);
            console2.log("  LoanEngine:    EMERGENCY_ADMIN -> guardian");
            console2.log("  TranchePool:   EMERGENCY_ADMIN -> guardian");
        } else {
            // No guardian — grant emergency to operations multisig as fallback
            le.grantRole(le.EMERGENCY_ADMIN_ROLE(), operationsMultisig);
            tp.grantRole(tp.EMERGENCY_ADMIN_ROLE(), operationsMultisig);
            console2.log(
                "  WARNING: No guardian set, EMERGENCY_ADMIN -> ops multisig (fallback)"
            );
        }

        // ====================================================
        // PHASE 7: Deployer Renounces ALL Roles
        // ====================================================
        console2.log("");
        console2.log("--- Phase 7: Deployer Renounces ---");

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
        // PHASE 8: Verification
        // ====================================================
        console2.log("");
        console2.log("--- Phase 8: Verification ---");

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

        // Verify ProtocolController IS admin (governance)
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

        // Verify operations multisig has operational roles
        require(
            le.hasRole(le.SERVICER_ROLE(), operationsMultisig),
            "FAIL: ops missing SERVICER_ROLE"
        );
        console2.log("  LoanEngine:   ops has SERVICER       [OK]");

        require(
            tp.hasRole(tp.WHITELIST_ADMIN_ROLE(), operationsMultisig),
            "FAIL: ops missing WHITELIST_ADMIN_ROLE"
        );
        console2.log("  TranchePool:  ops has WHITELIST_ADMIN [OK]");

        // ====================================================
        // Summary
        // ====================================================
        console2.log("");
        console2.log("============================================");
        console2.log("  Deployment Complete");
        console2.log("============================================");
        console2.log("");
        console2.log("  CreditPolicy:        ", creditPolicyProxy);
        console2.log("  TranchePool:          ", tranchePoolProxy);
        console2.log("  LoanEngine:           ", loanEngineProxy);
        console2.log("  ProtocolController:   ", protocolController);
        console2.log("");
        console2.log("  Deployer admin:        RENOUNCED");
        console2.log("");
        console2.log("  GOVERNANCE (48h timelock):");
        console2.log("    DEFAULT_ADMIN / POOL_ADMIN / POLICY_ADMIN");
        console2.log("    -> ProtocolController:", protocolController);
        console2.log("");
        console2.log("  OPERATIONS (direct, no delay):");
        console2.log("    FUND_MANAGER / SERVICER / RISK_ADMIN / CONFIG_ADMIN");
        console2.log(
            "    WHITELIST_ADMIN / POLICY_EDITOR / INDUSTRY_ADMIN / TREASURY"
        );
        console2.log("    -> Operations Multisig:", operationsMultisig);
        console2.log("");
        console2.log("  EMERGENCY (instant):");
        console2.log("    EMERGENCY_ADMIN (pause/unpause)");
        if (guardian != address(0)) {
            console2.log("    -> Guardian:", guardian);
        } else {
            console2.log(
                "    -> Operations Multisig (fallback):",
                operationsMultisig
            );
        }
        console2.log("");
        console2.log("  Timelock delay:       ", timelockDelay, "seconds");
    }
}
