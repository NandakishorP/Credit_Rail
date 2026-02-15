// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {HonkVerifier} from "../src/Verifier.sol";
import {LoanEngine} from "../src/LoanEngine.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {Poseidon2} from "@poseidon2-evm/Poseidon2.sol";
import {IVerifier} from "../src/interfaces/IVerifier.sol";
import {ICreditPolicy} from "../src/interfaces/ICreditPolicy.sol";

/**
 * @title E2EZkLoanTest
 * @notice End-to-end test: Deploy system, generate proof, verify, create loan
 *
 * This is a comprehensive script that:
 * 1. Deploys all contracts
 * 2. Sets up credit policy
 * 3. Generates a ZK proof via FFI
 * 4. Verifies the proof on-chain
 * 5. Creates a loan
 *
 * Usage:
 * forge script script/E2EZkLoanTest.s.sol:E2EZkLoanTest \
 *   --zk-compile --rpc-url http://127.0.0.1:8546 \
 *   --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 \
 *   --broadcast --ffi -vvv
 */
contract E2EZkLoanTest is Script {
    // Contract instances
    HonkVerifier public verifier;
    LoanEngine public loanEngine;
    CreditPolicy public creditPolicy;
    TranchePool public tranchePool;
    ERC20Mock public usdc;
    Poseidon2 public poseidon2;

    function run() external {
        uint256 deployerPrivateKey = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80;
        address deployer = vm.addr(deployerPrivateKey);

        console2.log("============================================");
        console2.log("  E2E ZK Loan Creation Test");
        console2.log("============================================");
        console2.log("");
        console2.log("Deployer:", deployer);
        console2.log("");

        vm.startBroadcast(deployerPrivateKey);

        // ========== PHASE 1: Deploy Contracts ==========
        console2.log("--- Phase 1: Deploying Contracts ---");

        usdc = new ERC20Mock();
        console2.log("[1/6] USDC:", address(usdc));

        poseidon2 = new Poseidon2();
        console2.log("[2/6] Poseidon2:", address(poseidon2));

        verifier = new HonkVerifier();
        console2.log("[3/6] HonkVerifier:", address(verifier));

        creditPolicy = new CreditPolicy();
        console2.log("[4/6] CreditPolicy:", address(creditPolicy));

        tranchePool = new TranchePool(
            address(usdc),
            "Senior Tranche",
            "SR-TRN"
        );
        console2.log("[5/6] TranchePool:", address(tranchePool));

        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            1000,
            address(tranchePool),
            address(usdc),
            address(poseidon2)
        );
        console2.log("[6/6] LoanEngine:", address(loanEngine));

        // Setup pool
        tranchePool.setEngine(address(loanEngine));
        usdc.mint(address(tranchePool), 10_000_000 * 1e6);
        console2.log("      Pool funded with 10M USDC");

        // ========== PHASE 2: Setup Credit Policy ==========
        console2.log("");
        console2.log("--- Phase 2: Setting Up Credit Policy ---");

        uint256 policyVersion = 1;
        creditPolicy.createPolicy(policyVersion);

        creditPolicy.updateEligibility(
            policyVersion,
            CreditPolicy.EligibilityCriteria({
                minRevenue: 1_000_000,
                minEbitda: 100_000,
                minNetWorth: 250_000,
                minAgeDays: 730,
                maxDefaults: 0,
                bankruptcyExcluded: true
            })
        );

        creditPolicy.updateRatios(
            policyVersion,
            CreditPolicy.FinancialRatios({
                maxDebtToEbitda: 40_000,
                minInterestCoverage: 15_000,
                minCurrentRatio: 12_000,
                minEbitdaMarginBps: 1000
            })
        );

        creditPolicy.updateConcentration(
            policyVersion,
            CreditPolicy.ConcentrationLimits({
                maxSingleExposure: 10_000_000,
                maxIndustryExposure: 50_000_000,
                maxGeographicExposure: 30_000_000
            })
        );

        creditPolicy.updateAttestation(
            policyVersion,
            CreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                requiredAttestationLevel: 1,
                requiresMultipleUnderwriters: false
            })
        );

        creditPolicy.updateCovenants(
            policyVersion,
            CreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 50_000,
                minLiquidityRatio: 10_000,
                requiresPeriodicReporting: true,
                reportingFrequencyDays: 30
            })
        );

        creditPolicy.setLoanTier(
            policyVersion,
            1,
            CreditPolicy.LoanTier({
                minRevenue: 1_000_000,
                maxRevenue: 10_000_000,
                minEbitda: 100_000,
                maxDebtToEbitda: 40_000,
                maxLoanToEbitda: 1e18,
                interestRateBps: 1200,
                originationFeeBps: 100,
                maxTermDays: 365,
                active: true
            })
        );

        creditPolicy.freezePolicy(policyVersion);
        console2.log("      Policy created and frozen");

        // Transition pool to DEPLOYED state
        tranchePool.transitionToCommitted();
        tranchePool.transitionToDeployed();
        console2.log("      TranchePool transitioned to DEPLOYED");

        vm.stopBroadcast();

        // ========== PHASE 3: Generate ZK Proof ==========
        console2.log("");
        console2.log("--- Phase 3: Generating ZK Proof via FFI ---");

        string[] memory ffiCmd = new string[](3);
        ffiCmd[0] = "npx";
        ffiCmd[1] = "tsx";
        ffiCmd[2] = "../zk-scripts/generate_proof_ffi.ts";

        bytes memory ffiResult = vm.ffi(ffiCmd);

        (
            bytes memory proofData,
            bytes32[] memory publicInputs,
            bytes32 policyHash,
            bytes32 loanHash,
            bytes32 nullifierHash,
            bytes32 borrowerCommitment,
            bytes32 underwriterKeyX,
            bytes32 underwriterKeyY,
            bytes32 industryHash,
            uint256 proofTimestamp
        ) = abi.decode(
                ffiResult,
                (
                    bytes,
                    bytes32[],
                    bytes32,
                    bytes32,
                    bytes32,
                    bytes32,
                    bytes32,
                    bytes32,
                    bytes32,
                    uint256
                )
            );

        console2.log("      Proof generated!");
        console2.log("      Proof size:", proofData.length, "bytes");
        console2.log("      Public inputs:", publicInputs.length);

        // ========== PHASE 4: Verify Proof On-Chain ==========
        console2.log("");
        console2.log("--- Phase 4: On-Chain Proof Verification ---");

        bool isValid = verifier.verify(proofData, publicInputs);
        require(isValid, "PROOF VERIFICATION FAILED!");
        console2.log("      Proof VERIFIED on-chain!");

        // ========== PHASE 5: Create Loan ==========
        console2.log("");
        console2.log("--- Phase 5: Creating Loan ---");

        vm.startBroadcast(deployerPrivateKey);

        LoanEngine.CreateLoanParams memory loanParams = LoanEngine
            .CreateLoanParams({
                borrowerCommitment: borrowerCommitment,
                nullifierHash: nullifierHash,
                policyVersion: policyVersion,
                tierId: 1,
                principalIssued: 500_000 * 1e6,
                aprBps: 1200,
                originationFeeBps: 100,
                termDays: 365,
                industry: industryHash,
                underwriterKeyX: underwriterKeyX,
                underwriterKeyY: underwriterKeyY,
                proofTimestamp: proofTimestamp
            });

        loanEngine.createLoan(loanParams, proofData, publicInputs);

        uint256 loanId = loanEngine.getNextLoanId() - 1;
        console2.log("      Loan created! ID:", loanId);

        // Get loan details
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        console2.log("      Principal:", loan.principalIssued / 1e6, "USDC");
        console2.log("      APR:", loan.aprBps / 100, "%");
        console2.log("      Term:", loan.termDays, "days");

        vm.stopBroadcast();

        // ========== SUCCESS ==========
        console2.log("");
        console2.log("============================================");
        console2.log("  SUCCESS! ZK Proof Integration Complete");
        console2.log("============================================");
        console2.log("");
        console2.log("Summary:");
        console2.log("  - Deployed 6 contracts");
        console2.log("  - Created and froze credit policy");
        console2.log("  - Generated ZK proof off-chain");
        console2.log("  - Verified proof on-chain (HonkVerifier)");
        console2.log("  - Created loan with ZK-verified credentials");
        console2.log("");
        console2.log("Loan ID:", loanId);
        console2.log("Verifier:", address(verifier));
        console2.log("LoanEngine:", address(loanEngine));
    }
}
