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
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(1_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapSeniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(3_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(2_00_00_000 * USDT);
        creditPolicy = new CreditPolicy();
        MockLoanProofVerifier mockLoanProofVerifier = new MockLoanProofVerifier();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(mockLoanProofVerifier),
            maxOriginationFeeBps,
            address(tranchePool),
            address(usdt)
        );

        handler = new Handler(loanEngine, tranchePool, creditPolicy, usdt);
        vm.stopPrank();
        bytes4[] memory selectors = new bytes4[](10);
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
        targetSelector(
            FuzzSelector({addr: address(handler), selectors: selectors})
        );
        targetContract(address(handler));
    }

    function invariant__totalIdleAndDeployedValueMatchesAccounting()
        public
        view
    {
        assertEq(
            tranchePool.getTotalIdleValue() +
                tranchePool.getTotalDeployedValue(),
            tranchePool.getTotalDeposited() +
                tranchePool.getTotalLoss() -
                tranchePool.getTotalRecovered(),
            "Total idle and deployed value does not match handler accounting"
        );
    }

    function invariant__poolAccountingMatchesTokenBalance() public view {
        uint256 poolBalance = usdt.balanceOf(address(tranchePool));

        uint256 internalAccounting = tranchePool.getTotalIdleValue() +
            tranchePool.getTotalDeployedValue() +
            tranchePool.getProtocolRevenue();

        assertEq(poolBalance, internalAccounting);
    }

    function invariant__OutStandingPrincipalMatchesDeployed() public view {
        assertEq(
            handler.outStandingPrincipal(),
            tranchePool.getTotalDeployedValue(),
            "Outstanding principal does not match deployed minus recovered and loss"
        );
    }

    function invariant_totalSeniorDepositsMatchesIdleSeniorValue() public view {
        assertEq(
            handler.getSeniorTrancheIdleValue(),
            tranchePool.getSeniorTrancheIdleValue(),
            "Total senior deposits do not match senior tranche idle value"
        );
    }

    function invariant_sumOfIndividualSeniorDepositsMatchesTotalIdleValue()
        public
        view
    {
        assertEq(
            handler.totalExpectedSeniorDeposits(),
            tranchePool.getSeniorTrancheIdleValue(),
            "Sum of individual senior shares does not match total senior shares"
        );
    }

    function invariant_totalSeniorSharesExpectedMatchesTranchePool()
        public
        view
    {
        assertEq(
            handler.totalExpectedSeniorShares(),
            tranchePool.getTotalSeniorShares(),
            "Total senior shares expected does not match tranche pool"
        );
    }

    function invariant_totalSeniorSharesMarkedByHandlersMatchesTranchePool()
        public
        view
    {
        assertEq(
            handler.getSeniorTrancheTotalShares(),
            tranchePool.getTotalSeniorShares(),
            "Total senior shares expected does not match tranche pool"
        );
    }

    function invariant_totalJuniorDepositsMatchesIdleJuniorValue() public view {
        assertEq(
            handler.getJuniorTrancheIdleValue(),
            tranchePool.getJuniorTrancheIdleValue(),
            "Total junior deposits do not match junior tranche idle value"
        );
    }

    function invariant_sumOfIndividualJuniorDepositsMatchesTotalIdleValue()
        public
        view
    {
        assertEq(
            handler.totalExpectedJuniorDeposits(),
            tranchePool.getJuniorTrancheIdleValue(),
            "Sum of individual junior shares does not match total junior shares"
        );
    }

    function invariant_totalJuniorSharesExpectedMatchesTranchePool()
        public
        view
    {
        assertEq(
            handler.totalExpectedJuniorShares(),
            tranchePool.getTotalJuniorShares(),
            "Total junior shares expected does not match tranche pool"
        );
    }

    function invariant_totalJuniorSharesMarkedByHandlersMatchesTranchePool()
        public
        view
    {
        assertEq(
            handler.getJuniorTrancheTotalShares(),
            tranchePool.getTotalJuniorShares(),
            "Total junior shares expected does not match tranche pool"
        );
    }
}
