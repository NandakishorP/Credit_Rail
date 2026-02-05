// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

import {Handler} from "./Handler.t.sol";
import {Test} from "forge-std/Test.sol";
import {StdInvariant} from "forge-std/StdInvariant.sol";

// we assume protocol revenue is zero as we have equity tranche
contract CreditRailStateFullFuzzTest is StdInvariant, Test {
    Handler public handler;
    ERC20Mock public usdt;
    uint256 public maxOriginationFeeBps = 500; // 5%
    TranchePool public tranchePool;
    LoanEngine public loanEngine;
    CreditPolicy public creditPolicy;
    uint256 public USDT = 1e18;
    address public deployer = makeAddr("deployer");

    constructor() {
        vm.startPrank(deployer);
        usdt = new ERC20Mock();
        tranchePool = new TranchePool(address(usdt));
        tranchePool.setMaxAllocationCapSeniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(3_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(2_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(1_00_00_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setSeniorAPR(8);
        tranchePool.setTargetJuniorAPR(15);

        creditPolicy = new CreditPolicy();
        creditPolicy.setMaxTiers(3);
        creditPolicy.createPolicy(1);

        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        creditPolicy.freezePolicy(1);

        MockLoanProofVerifier mockLoanProofVerifier = new MockLoanProofVerifier();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(mockLoanProofVerifier),
            maxOriginationFeeBps,
            address(tranchePool),
            address(usdt)
        );
        loanEngine.setMaxOriginationFeeBps(500);
        tranchePool.setLoanEngine(address(loanEngine));

        handler = new Handler(loanEngine, tranchePool, creditPolicy, usdt);
        vm.stopPrank();
        bytes4[] memory selectors = new bytes4[](18);
        selectors[0] = handler.depositSeniorTranche.selector;
        selectors[1] = handler.depositJuniorTranche.selector;
        selectors[2] = handler.depositEquityTranche.selector;
        selectors[3] = handler.maybeCommitPool.selector;
        selectors[4] = handler.createLoan.selector;
        selectors[5] = handler.activateLoan.selector;
        selectors[6] = handler.repayLoan.selector;
        selectors[7] = handler.maybeDeclareDefault.selector;
        selectors[8] = handler.maybeWriteOffLoan.selector;
        selectors[9] = handler.maybeRecoverLoan.selector;
        selectors[10] = handler.warpTime.selector;
        selectors[11] = handler.mayClosePool.selector;
        selectors[12] = handler.claimSeniorTrancheInterest.selector;
        selectors[13] = handler.claimJuniorTrancheInterest.selector;
        selectors[14] = handler.claimEquityTrancheInterest.selector;
        selectors[15] = handler.withdrawSeniorTranche.selector;
        selectors[16] = handler.withdrawJuniorTranche.selector;
        selectors[17] = handler.withdrawEquityTranche.selector;
        targetSelector(
            FuzzSelector({addr: address(handler), selectors: selectors})
        );
        targetContract(address(handler));
    }

    function _createEligibilityCriteria()
        internal
        pure
        returns (CreditPolicy.EligibilityCriteria memory)
    {
        return
            CreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
    }

    function _createFinancialRatios()
        internal
        pure
        returns (CreditPolicy.FinancialRatios memory)
    {
        return
            CreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
    }

    function _createConcentrationLimits()
        internal
        pure
        returns (CreditPolicy.ConcentrationLimits memory)
    {
        return
            CreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
    }

    function _createAttestationRequirements()
        internal
        pure
        returns (CreditPolicy.AttestationRequirements memory)
    {
        return
            CreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
    }

    function _createMaintenanceCovenants()
        internal
        pure
        returns (CreditPolicy.MaintenanceCovenants memory)
    {
        return
            CreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
    }

    function _createMockTier(
        string memory name
    ) internal pure returns (CreditPolicy.LoanTier memory) {
        return
            CreditPolicy.LoanTier({
                name: name,
                minRevenue: 1_00_00_000,
                maxRevenue: 5_00_00_000,
                minEBITDA: 10_00_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            });
    }

    function _hashString(string memory str) internal pure returns (bytes32) {
        return keccak256(bytes(str));
    }

    function invariant__totalIdleAndDeployedValueMatchesAccounting()
        public
        view
    {
        assertEq(
            tranchePool.getTotalIdleValue() +
                tranchePool.getTotalDeployedValue(),
            tranchePool.getTotalDeposited() -
                tranchePool.getTotalLoss() +
                tranchePool.getTotalRecovered(),
            "Total idle and deployed value does not match handler accounting"
        );
    }

    function invariant__OutStandingPrincipalMatchesDeployed() public view {
        assertEq(
            handler.outStandingPrincipal(),
            tranchePool.getTotalDeployedValue(),
            "Outstanding principal does not match deployed minus recovered and loss"
        );
    }
}
