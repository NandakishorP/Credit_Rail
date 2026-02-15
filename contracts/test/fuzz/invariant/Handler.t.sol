// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {Test, console} from "forge-std/Test.sol";
import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {Poseidon2} from "@poseidon2-evm/Poseidon2.sol";
import {Field} from "@poseidon2-evm/Field.sol";

contract Handler is Test {
    LoanEngine loanEngine;
    TranchePool tranchePool;
    ERC20Mock usdt;
    CreditPolicy creditPolicy;
    address deployer = makeAddr("deployer");
    uint256 public USDT = 1e18;
    bool allowFullDeployment = true;
    // 100m$ is the expected principal from lp's
    uint256 public expectedPrincipal = 10_00_00_000 * USDT;
    uint256 public minimumLoanPrincipal = 10_00_000 * USDT;
    uint256 public maximumLoanPrincipal = 2_00_00_000 * USDT;
    uint256 public minimumOriginationFeeBps = 50; // 0.5%
    uint256 public minimumTermDays = 180;
    uint256 public maximumTermDays = 480;
    address[] public seniorUsers;
    address[] public juniorUsers;
    address[] public equityUsers;
    uint256 public activePolicyVersion = 1;
    uint256 public defaultCounter;
    uint256 public writeOffCounter;
    uint256 public recoveryCounter;

    uint256 public seniorTrancheIdleValue;
    uint256 public seniorTrancheDeployedValue;

    uint256 public juniorTrancheIdleValue;
    uint256 public juniorTrancheDeployedValue;

    uint256 public equityTrancheIdleValue;
    uint256 public equityTrancheDeployedValue;

    uint256 public seniorTrancheTotalShares;
    mapping(address => uint256) public seniorTrancheShares;
    mapping(address => uint256) public seniorTrancheDeposits;
    mapping(address => uint256) public seniorUserIndex;

    uint256 public juniorTrancheTotalShares;
    mapping(address => uint256) public juniorTrancheShares;
    mapping(address => uint256) public juniorTrancheDeposits;
    mapping(address => uint256) public juniorUserIndex;

    uint256 public equityTrancheTotalShares;
    mapping(address => uint256) public equityTrancheShares;
    mapping(address => uint256) public equityTrancheDeposits;
    mapping(address => uint256) public equityUserIndex;

    address[] public loanBorrowers;

    address public recevingEntity = makeAddr("recevingEntity");
    address public feeManager = makeAddr("feeManager");

    uint256 public totalIdleValue;
    uint256 public totalDeployedValue;
    uint256 public totalDeposited;
    uint256 public totalLoss;
    uint256 public totalRecovered;
    uint256 public totalUnclaimedInterest;

    uint256 public outStandingPrincipal;

    constructor(
        LoanEngine _loanEngine,
        TranchePool _tranchePool,
        CreditPolicy _creditPolicy,
        ERC20Mock _usdt
    ) {
        loanEngine = _loanEngine;
        tranchePool = _tranchePool;
        usdt = _usdt;
        creditPolicy = _creditPolicy;

        vm.startPrank(deployer);
        loanEngine.setWhitelistedFeeManager(feeManager, true);
        loanEngine.setWhitelistedOffRampingEntity(recevingEntity, true);
        loanEngine.setWhitelistedRepaymentAgent(recevingEntity, true);
        loanEngine.setWhitelistedRecoveryAgent(recevingEntity, true);
        loanEngine.setUnderwriterAuthorization(bytes32(uint256(1)), bytes32(uint256(2)), true);

        tranchePool.setSeniorAPR(500);
        tranchePool.setTargetJuniorAPR(1000);

        for (uint160 i = 1; i < 10; i++) {
            seniorUsers.push(address(i));
            vm.deal(address(i), 100 ether); // Fund with ETH for gas
            if (i % 2 == 0) {
                ERC20Mock(usdt).mint(address(i), 1_00_00_00000 * 1e18);
                tranchePool.updateWhitelist(address(i), true);
            } else if (i % 3 == 0) {
                ERC20Mock(usdt).mint(address(i), 50_0000_0000 * 1e18);
                tranchePool.updateWhitelist(address(i), true);
            } else {
                ERC20Mock(usdt).mint(address(i), 10_000_0000000 * 1e18);
                tranchePool.updateWhitelist(address(i), true);
            }
        }
        for (uint160 i = 1; i < 5; i++) {
            juniorUsers.push(address(i));
            vm.deal(address(i), 100 ether); // Fund with ETH for gas
            if (i % 2 == 0) {
                ERC20Mock(usdt).mint(address(i), 500000_00_000 * 1e18);
                tranchePool.updateWhitelist(address(i), true);
            } else {
                tranchePool.updateWhitelist(address(i), true);
                ERC20Mock(usdt).mint(address(i), 10_000000_000 * 1e18);
            }
        }
        for (uint160 i = 1; i < 3; i++) {
            equityUsers.push(address(i));
            vm.deal(address(i), 100 ether); // Fund with ETH for gas
            ERC20Mock(usdt).mint(address(i), 50_0000_0000 * 1e18);
            tranchePool.updateEquityTrancheWhiteList(address(i), true);
        }

        for (uint160 i = 200; i < 205; i++) {
            loanBorrowers.push(address(i));
            vm.deal(address(i), 100 ether); // Fund with ETH for gas
        }
        vm.deal(address(recevingEntity), 100 ether); // Fund receiving entity
        vm.deal(address(feeManager), 100 ether); // Fund fee manager
        ERC20Mock(usdt).mint(address(recevingEntity), 50_0000_0000 * 1e18);

        vm.stopPrank();
    }

    function depositSeniorTranche(uint256 userIndex, uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) {
            return;
        }
        address user = seniorUsers[userIndex % seniorUsers.length];
        amount = bound(
            amount,
            tranchePool.getSeniorTrancheMinimumDepositAmount(),
            tranchePool.getSeniorTrancheMaxDepositCap()
        );
        if (
            amount + seniorTrancheIdleValue + seniorTrancheDeployedValue >
            tranchePool.getSeniorTrancheMaxDepositCap()
        ) {
            amount =
                tranchePool.getSeniorTrancheMaxDepositCap() -
                seniorTrancheIdleValue -
                seniorTrancheDeployedValue;
            if (amount < tranchePool.getSeniorTrancheMinimumDepositAmount()) {
                return;
            }
        }
        if (amount == 0) return;
        vm.startPrank(user);
        ERC20Mock(usdt).approve(address(tranchePool), amount);
        tranchePool.depositSeniorTranche(amount);
        seniorTrancheIdleValue += amount;
        seniorTrancheDeposits[user] += amount;
        seniorTrancheShares[user] += amount;
        seniorTrancheTotalShares += amount;
        totalIdleValue += amount;
        seniorUserIndex[user] = tranchePool.getSeniorInterestIndex();
        vm.stopPrank();
    }

    function depositJuniorTranche(uint256 userIndex, uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) {
            return;
        }
        address user = juniorUsers[userIndex % juniorUsers.length];
        amount = bound(
            amount,
            tranchePool.getJuniorTrancheMinimumDepositAmount(),
            tranchePool.getJuniorTrancheMaxDepositCap()
        );
        if (
            amount + juniorTrancheIdleValue + juniorTrancheDeployedValue >
            tranchePool.getJuniorTrancheMaxDepositCap()
        ) {
            amount =
                tranchePool.getJuniorTrancheMaxDepositCap() -
                juniorTrancheIdleValue -
                juniorTrancheDeployedValue;
            if (amount < tranchePool.getJuniorTrancheMinimumDepositAmount()) {
                return;
            }
        }
        if (amount == 0) return;
        vm.startPrank(user);
        ERC20Mock(usdt).approve(address(tranchePool), amount);
        tranchePool.depositJuniorTranche(amount);
        juniorTrancheIdleValue += amount;
        juniorTrancheDeposits[user] += amount;
        juniorTrancheShares[user] += amount;
        juniorTrancheTotalShares += amount;
        totalIdleValue += amount;
        juniorUserIndex[user] = tranchePool.getJuniorInterestIndex();
        vm.stopPrank();
    }

    function depositEquityTranche(uint256 userIndex, uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) {
            return;
        }
        address user = equityUsers[userIndex % equityUsers.length];
        amount = bound(
            amount,
            tranchePool.getEquityTrancheMinimumDepositAmount(),
            tranchePool.getEquityTrancheMaxDepositCap()
        );
        if (
            amount +
                tranchePool.getEquityTrancheIdleValue() +
                tranchePool.getEquityTrancheDeployedValue() >
            tranchePool.getEquityTrancheMaxDepositCap()
        ) {
            amount =
                tranchePool.getEquityTrancheMaxDepositCap() -
                tranchePool.getEquityTrancheIdleValue() -
                tranchePool.getEquityTrancheDeployedValue();
            if (amount < tranchePool.getEquityTrancheMinimumDepositAmount()) {
                return;
            }
        }
        if (amount == 0) return;
        vm.startPrank(user);
        ERC20Mock(usdt).approve(address(tranchePool), amount);
        tranchePool.depositEquityTranche(amount);
        
        // Ghost State Updates
        equityTrancheIdleValue += amount;
        equityTrancheDeposits[user] += amount;
        equityTrancheShares[user] += amount;
        equityTrancheTotalShares += amount;
        totalIdleValue += amount;
        equityUserIndex[user] = tranchePool.getEquityInterestIndex();
        
        vm.stopPrank();
    }

    function maybeCommitPool() public {
        if (
            tranchePool.getPoolState() == TranchePool.PoolState.OPEN &&
            tranchePool.getTotalIdleValue() > 0
        ) {
            vm.prank(deployer);
            tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
            totalDeposited = tranchePool.getTotalIdleValue();
        }
    }

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays,
        uint256 userIndex
    ) public {
        if (
            tranchePool.getPoolState() != TranchePool.PoolState.COMMITED &&
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED
        ) {
            return;
        }
        // 10% is reserved(no full deployment)
        uint256 minPrincipal = minimumLoanPrincipal;

        if (allowFullDeployment) {
            if (tranchePool.getTotalIdleValue() < minPrincipal) {
                minPrincipal = tranchePool.getTotalIdleValue();
            }
        } else {
            if (tranchePool.getTotalIdleValue() < minPrincipal * 10) {
                return;
            }
        }

        if (tranchePool.getTotalIdleValue() < minimumLoanPrincipal) {
            return;
        }

        principalIssued = bound(
            principalIssued,
            minimumLoanPrincipal,
            _min(maximumLoanPrincipal, tranchePool.getTotalIdleValue())
        );

        if (principalIssued > tranchePool.getTotalIdleValue() / 10) {
            principalIssued = tranchePool.getTotalIdleValue() / 10;
        }

        originationFeeBps = bound(
            originationFeeBps,
            minimumOriginationFeeBps,
            loanEngine.getMaxOriginationFeeBps()
        );
        termDays = bound(termDays, minimumTermDays, maximumTermDays);
        if (!creditPolicy.isPolicyFrozen(activePolicyVersion)) {
            return;
        }

        bytes32 borrowerCommitment = bytes32(uint256(keccak256(
            abi.encodePacked(
                loanBorrowers[userIndex % loanBorrowers.length],
                userIndex
            )
        )) % 21888242871839275222246405745257275088548364400416034343698204186575808495617);

        // Get nextLoanId BEFORE vm.prank to avoid consuming the prank
        uint256 nextLoanId = loanEngine.getNextLoanId();
        bytes memory proofData = abi.encodePacked(
            nextLoanId,
            userIndex,
            principalIssued,
            originationFeeBps,
            termDays
        );

        // Prepare public inputs
        // Prepare public inputs
        bytes32 nullifierHash = keccak256(abi.encode(nextLoanId,userIndex,borrowerCommitment, block.timestamp));
        bytes32[] memory publicInputs = new bytes32[](3);
        publicInputs[0] = creditPolicy.policyScopeHash(activePolicyVersion);
        publicInputs[2] = nullifierHash; // NULLIFIER_HASH_INDEX

        bytes32 keyX = bytes32(uint256(1));
        bytes32 keyY = bytes32(uint256(2));
        
        publicInputs[1] = bytes32(_computeLoanHash(borrowerCommitment, keyX, keyY, 1, principalIssued, 500, originationFeeBps, termDays, bytes32(0), block.timestamp, nextLoanId));

        vm.prank(deployer);
        loanEngine.createLoan(
            borrowerCommitment,
            nullifierHash,
            activePolicyVersion,
            1,
            principalIssued,
            500,
            originationFeeBps,
            termDays,
            bytes32(0), // industry
            keyX,
            keyY,
            block.timestamp,
            proofData,
            publicInputs
        );
    }

    function activateLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() != 1) {
            loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        }

        if (
            loanEngine.getLoanDetails(loanId).state !=
            LoanEngine.LoanState.CREATED
        ) {
            return;
        }
         if (
            tranchePool.getPoolState() != TranchePool.PoolState.COMMITED &&
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED
        ) {
            return;
        }

        if (
            loanEngine.getLoanDetails(loanId).principalIssued >
            tranchePool.getTotalIdleValue()
        ) {
            return;
        }

        vm.prank(deployer);
        loanEngine.activateLoan(loanId, recevingEntity, feeManager);
        totalDeployedValue += loanEngine.getLoanDetails(loanId).principalIssued;
        totalIdleValue -= loanEngine.getLoanDetails(loanId).principalIssued;
        outStandingPrincipal += loanEngine
            .getLoanDetails(loanId)
            .principalIssued;

        // Sync ghost variables with contract state to prevent underflow
        seniorTrancheIdleValue = tranchePool.getSeniorTrancheIdleValue();
        juniorTrancheIdleValue = tranchePool.getJuniorTrancheIdleValue();
        equityTrancheIdleValue = tranchePool.getEquityTrancheIdleValue();
        totalIdleValue = tranchePool.getTotalIdleValue();
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        if (loanEngine.getNextLoanId() == 1) {
            return;
        }
        loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        LoanEngine.Loan memory loanDetails = loanEngine.getLoanDetails(loanId);
        if (loanDetails.state != LoanEngine.LoanState.ACTIVE) {
            return;
        }
        console.log("here");
        principalAmount = bound(
            principalAmount,
            0,
            loanDetails.principalOutstanding
        );

        uint256 pendingInterest = _accrueInterest(loanId);
        uint256 totalInterestDue = loanDetails.interestAccrued +
            pendingInterest;

        interestAmount = bound(interestAmount, 0, totalInterestDue);

        if (principalAmount == 0 && interestAmount == 0) {
            return;
        }

        if (
            principalAmount > 0 && interestAmount == 0 && totalInterestDue > 0
        ) {
            return;
        }

        uint256 totalRepayAmount = principalAmount + interestAmount;
        uint256 interestAccrued = loanDetails.interestAccrued +
            _accrueInterest(loanId);
        uint256 actualInterestPaid = _min(totalRepayAmount, interestAccrued);
        uint256 actualPrincipalPaid = _min(
            totalRepayAmount - actualInterestPaid,
            loanDetails.principalOutstanding
        );

        vm.prank(recevingEntity);
        ERC20Mock(usdt).approve(address(loanEngine), totalRepayAmount);
        totalUnclaimedInterest += actualInterestPaid;
        vm.prank(deployer);
        loanEngine.repayLoan(
            loanId,
            principalAmount,
            interestAmount,
            recevingEntity,
            block.timestamp
        );

        outStandingPrincipal -= actualPrincipalPaid;

    }

    function warpTime(uint256 daysToWarp) public {
        daysToWarp = bound(daysToWarp, 1, 365);
        vm.warp(block.timestamp + (daysToWarp * 1 days));
    }

    function maybeDeclareDefault(uint256 loanId, bytes32 reasonHash) public {
        if (loanEngine.getNextLoanId() == 1) {
            return;
        }
        defaultCounter++;

        if (defaultCounter % 10 != 0) {
            return;
        }

        loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);

        if (loan.state != LoanEngine.LoanState.ACTIVE) {
            return;
        }

        vm.prank(deployer);
        loanEngine.declareDefault(loanId, reasonHash, block.timestamp);
    }

    function maybeWriteOffLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() == 1) {
            return;
        }

        writeOffCounter++;

        

        loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        if (
            loanEngine.getLoanDetails(loanId).state !=
            LoanEngine.LoanState.DEFAULTED
        ) {
            return;
        }

        // Read principal before writeoff as it zeroes it out
        uint256 principalOutstanding = loanEngine
            .getLoanDetails(loanId)
            .principalOutstanding;

        vm.prank(deployer);
        loanEngine.writeOffLoan(loanId);
        totalDeployedValue -= principalOutstanding;
        outStandingPrincipal -= principalOutstanding;
        
        // Sync idle values just in case writeoff affects them (though it shouldn't affect idle directly, best to be safe)
        totalIdleValue = tranchePool.getTotalIdleValue();
        seniorTrancheIdleValue = tranchePool.getSeniorTrancheIdleValue();
        juniorTrancheIdleValue = tranchePool.getJuniorTrancheIdleValue();
        equityTrancheIdleValue = tranchePool.getEquityTrancheIdleValue();

        totalLoss += principalOutstanding;
    }

    function maybeRecoverLoan(
        uint256 loanId,
        uint256 amount,
        uint256 agentIndex
    ) public {
        if (loanEngine.getNextLoanId() == 1) {
            return;
        }
        recoveryCounter++;

        

        loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.WRITTEN_OFF) {
            return;
        }


        amount = bound(amount, 1, loan.principalIssued);

        vm.prank(recevingEntity);
        ERC20Mock(usdt).approve(address(loanEngine), amount);

        vm.prank(deployer);
        loanEngine.recoverLoan(loanId, amount, recevingEntity);
        totalIdleValue += amount;
        totalRecovered += amount;
    }

    // accounting functions for invariants

    function mayClosePool() public {
        if(tranchePool.getTotalDeployedValue() > 0 || tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED){
            return;
        }
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.CLOSED);
    }

    function claimSeniorTrancheInterest(uint256 userIndex) public {
        userIndex = bound(userIndex, 0, seniorUsers.length - 1);
        if (tranchePool.poolState() != TranchePool.PoolState.CLOSED) {
            return;
        }
        address user = seniorUsers[userIndex];
        if (tranchePool.getSeniorTrancheShares(user) == 0) {
            return;
        }
        if (
            tranchePool.getSeniorInterestIndex() -
                tranchePool.getSeniorUserIndex(user) <=
            0
        ) {
            return;
        }
        totalUnclaimedInterest -= tranchePool.getSeniorTrancheShares(user) * (tranchePool.getSeniorInterestIndex() - tranchePool.getSeniorUserIndex(user)) / 1e18;
        vm.prank(user);
        tranchePool.claimSeniorInterest();
    }

    function claimJuniorTrancheInterest(uint256 userIndex) public {
        userIndex = bound(userIndex, 0, juniorUsers.length - 1);
        if (tranchePool.poolState() != TranchePool.PoolState.CLOSED) {
            return;
        }
        address user = juniorUsers[userIndex];
        if (tranchePool.getJuniorTrancheShares(user) == 0) {
            return;
        }
        if (
            tranchePool.getJuniorInterestIndex() -
                tranchePool.getJuniorUserIndex(user) <=
            0
        ) {
            return;
        }
        totalUnclaimedInterest -= tranchePool.getJuniorTrancheShares(user) * (tranchePool.getJuniorInterestIndex() - tranchePool.getJuniorUserIndex(user)) / 1e18;
        vm.prank(user);
        tranchePool.claimJuniorInterest();
    }

    function claimEquityTrancheInterest(uint256 userIndex) public {
        userIndex = bound(userIndex, 0, equityUsers.length - 1);
        if (tranchePool.poolState() != TranchePool.PoolState.CLOSED) {
            return;
        }
        address user = equityUsers[userIndex];
        if (tranchePool.getEquityTrancheShares(user) == 0) {
            return;
        }
        if (
            tranchePool.getEquityInterestIndex() -
                tranchePool.getEquityUserIndex(user) ==
            0
        ) {
            return;
        }
        totalUnclaimedInterest -= tranchePool.getEquityTrancheShares(user) * (tranchePool.getEquityInterestIndex() - tranchePool.getEquityUserIndex(user)) / 1e18;
        vm.prank(user);
        tranchePool.claimEquityInterest();
    }

    function withdrawSeniorTranche(uint256 userIndex, uint256 amount) public {
        if(tranchePool.getPoolState() != TranchePool.PoolState.CLOSED){
            return;
        }
        userIndex = bound(userIndex, 0, seniorUsers.length - 1);
        address user = seniorUsers[userIndex];
        amount = bound(amount, 0, tranchePool.getSeniorTrancheShares(user));
        
        if (amount == 0) return;
        
        // Ensure interest is claimed before withdraw (as per new contract guard)
        if (tranchePool.getSeniorInterestIndex() != tranchePool.getSeniorUserIndex(user)) {
             claimSeniorTrancheInterest(userIndex);
        }

        // Calculate expected asset withdrawal based on HANDLER's view of state
        // Replicating contract logic: (shares * idle) / totalShares
        uint256 currentIdle = seniorTrancheIdleValue;
        uint256 currentShares = seniorTrancheTotalShares;
        
        uint256 amountToWithdraw = (amount * currentIdle) / currentShares;

        vm.prank(user);
        tranchePool.withdrawSeniorTranche(amount);
        
        // Update Ghost State
        if (seniorTrancheDeposits[user] >= amountToWithdraw) {
            seniorTrancheDeposits[user] -= amountToWithdraw;
        } else {
            seniorTrancheDeposits[user] = 0;
        }

        seniorTrancheShares[user] -= amount;
        seniorTrancheTotalShares -= amount;
        
        seniorTrancheIdleValue -= amountToWithdraw;
        totalIdleValue -= amountToWithdraw;
    }

    function withdrawJuniorTranche(uint256 userIndex, uint256 amount) public {
        if(tranchePool.getPoolState() != TranchePool.PoolState.CLOSED){
            return;
        }
        userIndex = bound(userIndex, 0, juniorUsers.length - 1);
        address user = juniorUsers[userIndex];
        amount = bound(amount, 0, tranchePool.getJuniorTrancheShares(user));

        if (amount == 0) return;

        if (tranchePool.getJuniorInterestIndex() != tranchePool.getJuniorUserIndex(user)) {
             claimJuniorTrancheInterest(userIndex);
        }

        uint256 currentIdle = juniorTrancheIdleValue;
        uint256 currentShares = juniorTrancheTotalShares;
        
        uint256 amountToWithdraw = (amount * currentIdle) / currentShares;

        vm.prank(user);
        tranchePool.withdrawJuniorTranche(amount);
        
         if (juniorTrancheDeposits[user] >= amountToWithdraw) {
            juniorTrancheDeposits[user] -= amountToWithdraw;
        } else {
             juniorTrancheDeposits[user] = 0;
        }
        
        juniorTrancheShares[user] -= amount;
        juniorTrancheTotalShares -= amount;
        juniorTrancheIdleValue -= amountToWithdraw;
        totalIdleValue -= amountToWithdraw;
    }

    function withdrawEquityTranche(uint256 userIndex, uint256 amount) public {
        if(tranchePool.getPoolState() != TranchePool.PoolState.CLOSED){
            return;
        }
        userIndex = bound(userIndex, 0, equityUsers.length - 1);
        address user = equityUsers[userIndex];
        amount = bound(amount, 0, tranchePool.getEquityTrancheShares(user));
        if (amount == 0) return;

         if (tranchePool.getEquityInterestIndex() != tranchePool.getEquityUserIndex(user)) {
             claimEquityTrancheInterest(userIndex);
        }

        uint256 currentIdle = equityTrancheIdleValue;
        uint256 currentShares = equityTrancheTotalShares;
        
        // Safety check to avoid div by zero if logic is flawed elsewhere
        if (currentShares == 0) return;

        uint256 amountToWithdraw = (amount * currentIdle) / currentShares;

        vm.prank(user);
        tranchePool.withdrawEquityTranche(amount);
        
        if (equityTrancheDeposits[user] >= amountToWithdraw) {
            equityTrancheDeposits[user] -= amountToWithdraw;
        } else {
            equityTrancheDeposits[user] = 0;
        }

        equityTrancheShares[user] -= amount;
        equityTrancheTotalShares -= amount;
        equityTrancheIdleValue -= amountToWithdraw;
        totalIdleValue -= amountToWithdraw;
    }

    function totalExpectedSeniorDeposits() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < seniorUsers.length; i++) {
            total += seniorTrancheDeposits[seniorUsers[i]];
        }
        return total;
    }

    function totalExpectedJuniorDeposits() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < juniorUsers.length; i++) {
            total += juniorTrancheDeposits[juniorUsers[i]];
        }
        return total;
    }

    function totalExpectedSeniorShares() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < seniorUsers.length; i++) {
            total += seniorTrancheShares[seniorUsers[i]];
        }
        return total;
    }

    function totalExpectedJuniorShares() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < juniorUsers.length; i++) {
            total += juniorTrancheShares[juniorUsers[i]];
        }
        return total;
    }

    function getSeniorTrancheIdleValue() public view returns (uint256) {
        return seniorTrancheIdleValue;
    }

    function getJuniorTrancheIdleValue() public view returns (uint256) {
        return juniorTrancheIdleValue;
    }

    function getSeniorTrancheTotalShares() public view returns (uint256) {
        return seniorTrancheTotalShares;
    }

    function getJuniorTrancheTotalShares() public view returns (uint256) {
        return juniorTrancheTotalShares;
    }

    function _min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }

    function _computeLoanHash(
        bytes32 borrowerCommitment,
        bytes32 underwriterKeyX,
        bytes32 underwriterKeyY,
        uint8 tierId,
        uint256 principal,
        uint256 apr,
        uint256 fee,
        uint256 term,
        bytes32 industry,
        uint256 timestamp,
        uint256 loanId
    ) internal view returns (uint256) {
        Field.Type[] memory inputs = new Field.Type[](11);
        inputs[0] = Field.toField(uint256(borrowerCommitment));
        inputs[1] = Field.toField(uint256(underwriterKeyX));
        inputs[2] = Field.toField(uint256(underwriterKeyY));
        inputs[3] = Field.toField(uint256(tierId));
        inputs[4] = Field.toField(principal);
        inputs[5] = Field.toField(apr);
        inputs[6] = Field.toField(fee);
        inputs[7] = Field.toField(term);
        inputs[8] = Field.toField(uint256(industry));
        inputs[9] = Field.toField(timestamp);
        inputs[10] = Field.toField(loanId);
        return Field.toUint256(Poseidon2(address(loanEngine.poseidon2())).hash(inputs));
    }

    function _accrueInterest(uint256 loanId) internal view returns (uint256) {
        // Implementation goes here
        loanId = bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);

        uint256 timeElapsed = block.timestamp - loan.lastAccrualTimestamp;
        if (loan.principalOutstanding == 0) {
            return 0;
        }

        uint256 interest = (loan.principalOutstanding *
            loan.aprBps *
            timeElapsed) / (365 days * 10_000);

        return interest;
    }
}
