// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "forge-std/Script.sol";
import "../src/LoanEngine.sol";
import "../src/CreditPolicy.sol";
import {ICreditPolicy} from "../src/interfaces/ICreditPolicy.sol";
import "../src/TranchePool.sol";
import {HonkVerifier} from "../src-zk/Verifier.sol";
import "../test/mocks/MockPoseidon2.sol";
import "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

contract DeployAndSetup is Script {
    function run() external {
        uint256 deployerPrivateKey = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80;
        address deployer = vm.addr(deployerPrivateKey);

        vm.startBroadcast(deployerPrivateKey);

        // 1. Deploy MockPoseidon2
        MockPoseidon2 poseidon = new MockPoseidon2();
        console.log("MockPoseidon2:", address(poseidon));

        // 2. Deploy HonkVerifier (assumes ZKTranscriptLib is deployed)
        HonkVerifier verifier = new HonkVerifier();
        console.log("HonkVerifier:", address(verifier));

        // 3. Deploy CreditPolicy
        CreditPolicy policy = new CreditPolicy();
        console.log("CreditPolicy:", address(policy));

        // 4. Deploy ERC20Mock (USDC)
        ERC20Mock usdc = new ERC20Mock();
        console.log("USDC:", address(usdc));

        // 5. Deploy TranchePool
        TranchePool pool = new TranchePool(address(usdc));
        console.log("TranchePool:", address(pool));

        // 6. Deploy LoanEngine
        LoanEngine engine = new LoanEngine(
            address(policy),
            address(verifier),
            500, // maxOriginationFeeBps = 5%
            address(pool),
            address(usdc),
            address(poseidon)
        );
        console.log("LoanEngine:", address(engine));

        // 7. Setup Credit Policy (version 1)
        uint256 policyVersion = 1;
        policy.createPolicy(policyVersion);

        policy.updateEligibility(
            policyVersion,
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1000000,
                minEBITDA: 100000,
                minTangibleNetWorth: 250000,
                minBusinessAgeDays: 730,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );

        policy.updateRatios(
            policyVersion,
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 40000,
                minInterestCoverageRatio: 15000,
                minCurrentRatio: 12000,
                minEBITDAMarginBps: 1000
            })
        );

        policy.updateConcentration(
            policyVersion,
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 2500
            })
        );

        policy.updateAttestation(
            policyVersion,
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 365,
                requiresCPAAttestation: false
            })
        );

        policy.updateCovenants(
            policyVersion,
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 50000,
                minCoverageRatio: 10000,
                minLiquidityAmount: 50000,
                allowsDividends: true,
                reportingFrequencyDays: 90
            })
        );

        policy.setLoanTier(
            policyVersion,
            1,
            ICreditPolicy.LoanTier({
                name: "Standard",
                minRevenue: 1000000,
                maxRevenue: 10000000,
                minEBITDA: 100000,
                maxDebtToEBITDA: 40000,
                maxLoanToEBITDA: 1e18,
                interestRateBps: 1200,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            })
        );

        policy.setPolicyDocument(
            policyVersion,
            keccak256("policy_document_v1"),
            "ipfs://test"
        );
        policy.setPolicyScopeHash(policyVersion, keccak256("policy_scope_v1"));
        policy.freezePolicy(policyVersion);
        console.log("Policy frozen: version", policyVersion);

        // 8. Setup TranchePool
        pool.setLoanEngine(address(engine));
        pool.updateWhitelist(deployer, true);

        // Mint USDC and deposit to pool
        usdc.mint(deployer, 10_000_000e18);
        usdc.approve(address(pool), 10_000_000e18);
        usdc.transfer(address(pool), 5_000_000e18);

        pool.setPoolState(TranchePool.PoolState.COMMITED);
        console.log("Pool committed with capital");

        vm.stopBroadcast();

        console.log("");
        console.log("=== EXPORT THESE ===");
        console.log("LOAN_ENGINE=", address(engine));
        console.log("CREDIT_POLICY=", address(policy));
        console.log("TRANCHE_POOL=", address(pool));
        console.log("USDC=", address(usdc));
        console.log("VERIFIER=", address(verifier));
        console.log("POSEIDON=", address(poseidon));
    }
}
