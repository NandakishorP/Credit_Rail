// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {LoanEngine} from "../../src/LoanEngine.sol";
import {ILoanEngine} from "../../src/interfaces/ILoanEngine.sol";
import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";
import {Field} from "@poseidon2-evm/Field.sol";

contract TestLoanEngineComplete is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;
    LoanEngine loanEngine;
    MockLoanProofVerifier verifier;
    CreditPolicy creditPolicy;

    address deployer = makeAddr("deployer");
    address seniorUser1 = makeAddr("seniorUser1");
    address juniorUser1 = makeAddr("juniorUser1");
    address equityUser1 = makeAddr("equityUser1");
    address offRampEntity = makeAddr("offRampEntity");
    address repaymentAgent = makeAddr("repaymentAgent");
    address recoveryAgent = makeAddr("recoveryAgent");
    address feeManager = makeAddr("feeManager");
    uint256 public USDT = 1e18;

    // Test loan parameters
    bytes32 testBorrowerCommitment =
        bytes32(
            uint256(keccak256("borrower123")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );
    uint256 testPolicyVersion = 1;
    uint8 testTierId = 1;
    uint256 testPrincipal = 1_000_000 * USDT;
    uint256 testAprBps = 800; // 8%
    uint256 testOriginationFeeBps = 100; // 1%
    uint256 testTermDays = 365;
    bytes testProofData = hex"1234";
    bytes32[] testPublicInputs;

    bytes32 testUnderwriterKeyX =
        bytes32(
            uint256(keccak256("underwriterX")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );
    bytes32 testUnderwriterKeyY =
        bytes32(
            uint256(keccak256("underwriterY")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );
    bytes32 testIndustry =
        bytes32(
            uint256(keccak256("TECH")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );

    // Helper to create CreateLoanParams struct with custom nullifier, policyVersion, tierId, principal, apr, fee, term, and timestamp
    function _buildParams(
        bytes32 nullifier,
        uint256 policyVersion,
        uint8 tierId,
        uint256 principal,
        uint256 apr,
        uint256 fee,
        uint256 term,
        uint256 timestamp
    ) internal view returns (ILoanEngine.CreateLoanParams memory) {
        return
            ILoanEngine.CreateLoanParams({
                borrowerCommitment: testBorrowerCommitment,
                nullifierHash: nullifier,
                policyVersion: policyVersion,
                tierId: tierId,
                principalIssued: principal,
                aprBps: apr,
                originationFeeBps: fee,
                termDays: term,
                industry: testIndustry,
                underwriterKeyX: testUnderwriterKeyX,
                underwriterKeyY: testUnderwriterKeyY,
                proofTimestamp: timestamp
            });
    }

    // Convenience wrapper for standard test params with just nullifier override
    function _buildStandardParams(
        bytes32 nullifier
    ) internal view returns (ILoanEngine.CreateLoanParams memory) {
        return
            _buildParams(
                nullifier,
                testPolicyVersion,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                block.timestamp
            );
    }

    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);

        verifier = new MockLoanProofVerifier();
        tranchePool = new TranchePool(address(usdt));
        creditPolicy = new CreditPolicy();

        // Setup credit policy
        creditPolicy.createPolicy(1);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setMaxTiers(2);

        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        // Set policy scope hash to match what we will use in public inputs
        bytes32 scopeHash = keccak256("policyScope1");
        creditPolicy.setPolicyScopeHash(1, scopeHash);

        creditPolicy.freezePolicy(1);

        // Setup loan engine
        MockPoseidon2 mockPoseidon = new MockPoseidon2();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            500, // max origination fee 5%
            address(tranchePool),
            address(usdt),
            address(mockPoseidon)
        );

        // Authorize underwriter
        loanEngine.setUnderwriterAuthorization(
            testUnderwriterKeyX,
            testUnderwriterKeyY,
            true
        );

        // Initialize public inputs with 3 fields (Policy, LoanHash, Nullifier)
        testPublicInputs = new bytes32[](3);
        testPublicInputs[0] = scopeHash; // POLICY_VERSION_HASH_INDEX
        // Index 1 (LOAN_HASH) will be set dynamically by tests
        testPublicInputs[2] = keccak256("nullifier1"); // NULLIFIER_HASH_INDEX

        // Setup tranche pool
        _setupTranchePool();

        // Whitelist entities
        loanEngine.setWhitelistedOffRampingEntity(offRampEntity, true);
        loanEngine.setWhitelistedRepaymentAgent(repaymentAgent, true);
        loanEngine.setWhitelistedRecoveryAgent(recoveryAgent, true);
        loanEngine.setWhitelistedFeeManager(feeManager, true);
        vm.stopPrank();

        // Fund users
        _fundUsers();

        // Users deposit to tranches
        _makeDeposits();

        // Set pool to COMMITED state
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
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
        return
            Field.toUint256(
                MockPoseidon2(address(loanEngine.poseidon2())).hash(inputs)
            );
    }

    function _hashString(string memory str) internal pure returns (bytes32) {
        return keccak256(bytes(str));
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN CREATION TESTS
    //////////////////////////////////////////////////////////////*/

    function test_CreateLoan_Success() public {
        uint256 nextLoanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                nextLoanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier1")
        );

        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        (
            uint256 loanId,
            bytes32 borrowerCommitment,
            uint256 policyVersion,
            uint8 tierId,
            uint256 principalIssued,
            uint256 principalOutstanding,
            uint256 aprBps,
            uint256 originationFeeBps,
            ,
            ,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(loanId, 1);
        assertEq(borrowerCommitment, testBorrowerCommitment);
        assertEq(policyVersion, testPolicyVersion);
        assertEq(tierId, testTierId);
        assertEq(principalIssued, testPrincipal);
        assertEq(principalOutstanding, 0);
        assertEq(aprBps, testAprBps);
        assertEq(originationFeeBps, testOriginationFeeBps);
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.CREATED));
    }

    function test_CreateLoan_RevertIf_PolicyNotFrozen() public {
        // Create unfrozen policy
        vm.startPrank(deployer);
        creditPolicy.createPolicy(2);
        creditPolicy.updateEligibility(2, _createEligibilityCriteria());
        creditPolicy.setLoanTier(2, 1, _createMockTier("Tier 1"));

        testPublicInputs[2] = keccak256("nullifier2");
        testPublicInputs[0] = creditPolicy.policyScopeHash(2);
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__PolicyNotFrozen.selector,
                2
            )
        );
        ILoanEngine.CreateLoanParams memory params = _buildParams(
            keccak256("nullifier2"),
            2, // policyVersion 2 (unfrozen)
            testTierId,
            testPrincipal,
            testAprBps,
            testOriginationFeeBps,
            testTermDays,
            block.timestamp
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);
        vm.stopPrank();
    }

    function test_CreateLoan_RevertIf_TierNotInPolicy() public {
        testPublicInputs[2] = keccak256("nullifier3");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                99,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanTierIsNotInPolicy.selector,
                testPolicyVersion,
                99
            )
        );
        ILoanEngine.CreateLoanParams memory params = _buildParams(
            keccak256("nullifier3"),
            testPolicyVersion,
            99, // Invalid tier
            testPrincipal,
            testAprBps,
            testOriginationFeeBps,
            testTermDays,
            block.timestamp
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertIf_OriginationFeeExceeded() public {
        testPublicInputs[2] = keccak256("nullifier4");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                600,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__MaxOriginationFeeExceeded.selector,
                1,
                600,
                500
            )
        );
        ILoanEngine.CreateLoanParams memory params = _buildParams(
            keccak256("nullifier4"),
            testPolicyVersion,
            testTierId,
            testPrincipal,
            testAprBps,
            600, // 6% > max 5%
            testTermDays,
            block.timestamp
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertIf_InvalidParameters_ZeroPrincipal() public {
        uint256 invalidPrincipal = 0;

        testPublicInputs[2] = keccak256("nullifier5");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                0,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__InvalidLoanParameters.selector,
                1,
                0,
                testAprBps,
                testTermDays
            )
        );
        ILoanEngine.CreateLoanParams memory params = _buildParams(
            keccak256("nullifier5"),
            testPolicyVersion,
            testTierId,
            0, // Zero principal
            testAprBps,
            testOriginationFeeBps,
            testTermDays,
            block.timestamp
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertIf_NotOwner() public {
        testPublicInputs[2] = keccak256("nullifier6");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier6")
        );

        vm.expectRevert();
        vm.prank(seniorUser1);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN ACTIVATION TESTS
    //////////////////////////////////////////////////////////////*/

    function test_ActivateLoan_Success() public {
        // Create loan first
        testPublicInputs[2] = keccak256("nullifier7");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier7")
        );

        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        uint256 poolBalanceBefore = usdt.balanceOf(address(tranchePool));
        uint256 offRampBalanceBefore = usdt.balanceOf(offRampEntity);
        uint256 feeManagerBalanceBefore = usdt.balanceOf(feeManager); // ADD THIS

        vm.prank(deployer);
        loanEngine.activateLoan(1, offRampEntity, feeManager);

        (
            ,
            ,
            ,
            ,
            ,
            uint256 principalOutstanding,
            ,
            ,
            ,
            ,
            uint256 lastAccrualTimestamp,
            uint256 startTimestamp,
            uint256 maturityTimestamp,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(principalOutstanding, testPrincipal);
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.ACTIVE));
        assertEq(lastAccrualTimestamp, block.timestamp);
        assertEq(startTimestamp, block.timestamp);
        assertEq(maturityTimestamp, block.timestamp + (testTermDays * 1 days));

        // Check fund transfers
        uint256 originationFee = (testPrincipal * testOriginationFeeBps) /
            10000;
        uint256 netDisbursement = testPrincipal - originationFee;

        // OffRamp entity receives net disbursement
        assertEq(
            usdt.balanceOf(offRampEntity),
            offRampBalanceBefore + netDisbursement
        );

        // Fee manager receives origination fee
        assertEq(
            usdt.balanceOf(feeManager),
            feeManagerBalanceBefore + originationFee
        );

        // TranchePool loses the full principal amount (disbursement + fee)
        assertEq(
            usdt.balanceOf(address(tranchePool)),
            poolBalanceBefore - testPrincipal // CHANGE THIS LINE (was: poolBalanceBefore - netDisbursement)
        );
    }

    function test_ActivateLoan_RevertIf_NotInCreatedState() public {
        vm.startPrank(deployer);
        testPublicInputs[2] = keccak256("nullifier8");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier8")
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        loanEngine.activateLoan(1, offRampEntity, feeManager);

        // Try to activate again
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanIsNotInCreatedState.selector,
                1
            )
        );
        loanEngine.activateLoan(1, offRampEntity, feeManager);
        vm.stopPrank();
    }

    function test_ActivateLoan_RevertIf_NotWhitelistedEntity() public {
        vm.startPrank(deployer);
        testPublicInputs[2] = keccak256("nullifier9");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier9")
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        address nonWhitelistedEntity = makeAddr("nonWhitelisted");
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__InvalidOffRampingEntity.selector,
                nonWhitelistedEntity
            )
        );
        loanEngine.activateLoan(1, nonWhitelistedEntity, feeManager);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN REPAYMENT TESTS
    //////////////////////////////////////////////////////////////*/

    function test_RepayLoan_FullRepayment() public {
        // Create and activate loan
        _createAndActivateLoan();

        // Advance time by 180 days
        vm.warp(block.timestamp + 180 days);

        // Calculate expected interest
        uint256 timeElapsed = 180 days;
        uint256 expectedInterest = (testPrincipal * testAprBps * timeElapsed) /
            (365 days * 10_000);

        // Fund repayment agent
        deal(address(usdt), repaymentAgent, testPrincipal + expectedInterest);

        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), testPrincipal + expectedInterest);

        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            testPrincipal,
            expectedInterest,
            repaymentAgent,
            block.timestamp
        );

        (
            ,
            ,
            ,
            ,
            ,
            uint256 principalOutstanding,
            ,
            ,
            uint256 interestAccrued,
            uint256 interestPaid,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(principalOutstanding, 0);
        assertEq(interestAccrued, 0);
        assertEq(interestPaid, expectedInterest);
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.REPAID));
    }

    function test_RepayLoan_PartialRepayment() public {
        _createAndActivateLoan();

        vm.warp(block.timestamp + 90 days);

        uint256 partialPrincipal = testPrincipal / 2;
        uint256 timeElapsed = 90 days;
        uint256 expectedInterest = (testPrincipal * testAprBps * timeElapsed) /
            (365 days * 10_000);

        deal(
            address(usdt),
            repaymentAgent,
            partialPrincipal + expectedInterest
        );

        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), partialPrincipal + expectedInterest);

        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            partialPrincipal,
            expectedInterest,
            repaymentAgent,
            block.timestamp
        );

        (
            ,
            ,
            ,
            ,
            ,
            uint256 principalOutstanding,
            ,
            ,
            uint256 interestAccrued,
            ,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(principalOutstanding, testPrincipal - partialPrincipal);
        assertEq(interestAccrued, 0); // All interest paid
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.ACTIVE)); // Still active
    }

    function test_RepayLoan_Waterfall_IgnoresLabels() public {
        _createAndActivateLoan();

        // Advance time to accrue interest
        vm.warp(block.timestamp + 90 days);

        uint256 timeElapsed = 90 days;
        uint256 expectedInterest = (testPrincipal * testAprBps * timeElapsed) /
            (365 days * 10_000); // approx 17,753 if principal is 1M

        uint256 repaymentAmount = 50_000 * USDT; // More than interest

        deal(address(usdt), repaymentAgent, repaymentAmount);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), repaymentAmount);

        // INTENTIONALLY MISLABEL: Say it's all Principal, 0 Interest
        // The waterfall should override this and pay interest first.
        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            repaymentAmount, // principalAmount labeled
            0, // interestAmount labeled
            repaymentAgent,
            block.timestamp
        );

        (
            ,
            ,
            ,
            ,
            ,
            uint256 principalOutstanding, // 5
            ,
            ,
            uint256 interestAccrued, // 8
            uint256 interestPaid, // 9 // 14
            ,
            ,
            ,
            ,
            ,
            ,
            ,

        ) = loanEngine.s_loans(1);

        // CHECK 1: Interest Accrued should be 0 (fully paid first)
        assertEq(interestAccrued, 0, "Waterfall should pay interest first");

        // CHECK 2: Interest Paid should track the amount paid
        assertEq(
            interestPaid,
            expectedInterest,
            "Interest paid tracks correct amount"
        );

        // CHECK 3: Principal Outstanding should reduce by (Repayment - Interest)
        // repaymentAmount (50k) - expectedInterest (~17k) = ~33k principal reduction
        uint256 expectedPrincipalPaid = repaymentAmount - expectedInterest;
        assertEq(
            principalOutstanding,
            testPrincipal - expectedPrincipalPaid,
            "Principal reduced by remainder"
        );
    }

    function test_RepayLoan_RevertIf_NotActive() public {
        testPublicInputs[2] = keccak256("nullifier10");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier10")
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanIsNotActive.selector,
                1
            )
        );
        loanEngine.repayLoan(1, 1000, 1000, repaymentAgent, block.timestamp);
    }

    function test_RepayLoan_RevertIf_ZeroRepayment() public {
        _createAndActivateLoan();

        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__InvalidRepayment.selector);
        loanEngine.repayLoan(1, 0, 0, repaymentAgent, block.timestamp);
    }

    function test_RepayLoan_RevertIf_NotWhitelistedAgent() public {
        _createAndActivateLoan();

        address nonWhitelistedAgent = makeAddr("nonWhitelistedAgent");

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__InvalidRepaymentAgent.selector,
                nonWhitelistedAgent
            )
        );
        loanEngine.repayLoan(
            1,
            1000,
            1000,
            nonWhitelistedAgent,
            block.timestamp
        );
    }

    /*//////////////////////////////////////////////////////////////
                        DEFAULT & WRITE-OFF TESTS
    //////////////////////////////////////////////////////////////*/

    function test_DeclareDefault_Success() public {
        _createAndActivateLoan();

        vm.warp(block.timestamp + 100 days);

        bytes32 reasonHash = keccak256("Missed payment");

        vm.prank(deployer);
        loanEngine.declareDefault(1, reasonHash, block.timestamp);

        (
            ,
            ,
            ,
            ,
            ,
            ,
            ,
            ,
            ,
            ,
            uint256 interestAccrued,
            ,
            ,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(uint256(state), uint256(ILoanEngine.LoanState.DEFAULTED));
        assertGt(interestAccrued, 0); // Interest was accrued before default
    }

    function test_DeclareDefault_RevertIf_NotActive() public {
        testPublicInputs[2] = keccak256("nullifier11");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier11")
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanIsNotActive.selector,
                1
            )
        );
        loanEngine.declareDefault(1, keccak256("reason"), block.timestamp);
    }

    function test_WriteOffLoan_Success() public {
        _createAndActivateLoan();

        vm.warp(block.timestamp + 100 days);

        // Declare default first
        vm.prank(deployer);
        loanEngine.declareDefault(
            1,
            keccak256("Missed payment"),
            block.timestamp
        );

        (
            ,
            ,
            ,
            ,
            ,
            // loanId
            // borrowerCommitment
            // policyVersion
            // tierId
            // principalIssued
            uint256 principalOutstandingBefore, // principalOutstanding (position 5) // aprBps // originationFeeBps
            ,
            ,
            uint256 interestAccruedBefore, // interestAccrued (position 8) // interestPaid // lastAccrualTimestamp // startTimestamp // maturityTimestamp // termDays
            ,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState stateBefore, // state (position 14) // totalRecovered (position 15)
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(uint256(stateBefore), uint256(ILoanEngine.LoanState.DEFAULTED));
        assertGt(principalOutstandingBefore, 0);
        assertGt(interestAccruedBefore, 0);

        // Write off
        vm.prank(deployer);
        loanEngine.writeOffLoan(1);

        (
            ,
            ,
            ,
            ,
            ,
            // loanId
            // borrowerCommitment
            // policyVersion
            // tierId
            // principalIssued
            uint256 principalOutstanding, // principalOutstanding (position 5) // aprBps // originationFeeBps
            ,
            ,
            uint256 interestAccrued, // interestAccrued (position 8) // interestPaid // lastAccrualTimestamp // startTimestamp // maturityTimestamp // termDays
            ,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState state, // state (position 14) // totalRecovered (position 15)
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(principalOutstanding, 0);
        assertEq(interestAccrued, 0);
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.WRITTEN_OFF));
    }

    function test_WriteOffLoan_RevertIf_NotDefaulted() public {
        _createAndActivateLoan();

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanIsNotDefaulted.selector,
                1
            )
        );
        loanEngine.writeOffLoan(1);
    }

    function test_WriteOffLoan_RevertIf_ZeroLoss() public {
        _createAndActivateLoan();

        // Fully repay the loan
        vm.warp(block.timestamp + 180 days);

        uint256 timeElapsed = 180 days;
        uint256 expectedInterest = (testPrincipal * testAprBps * timeElapsed) /
            (365 days * 10_000);

        deal(address(usdt), repaymentAgent, testPrincipal + expectedInterest);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), testPrincipal + expectedInterest);

        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            testPrincipal,
            expectedInterest,
            repaymentAgent,
            block.timestamp
        );

        // Now try to default and write off a fully repaid loan
        // First we need to manipulate state (this is theoretical)
        // In practice, you can't default a repaid loan, so let's test differently
    }

    /*//////////////////////////////////////////////////////////////
                        RECOVERY TESTS
    //////////////////////////////////////////////////////////////*/

    function test_RecoverLoan_Success() public {
        _createAndActivateLoan();

        vm.warp(block.timestamp + 100 days);

        // Default and write off
        vm.startPrank(deployer);
        loanEngine.declareDefault(
            1,
            keccak256("Missed payment"),
            block.timestamp
        );
        loanEngine.writeOffLoan(1);
        vm.stopPrank();

        // Recover some amount
        uint256 recoveryPrincipal = 100_000 * USDT;
        uint256 recoveryInterest = 10_000 * USDT;

        deal(
            address(usdt),
            recoveryAgent,
            recoveryPrincipal + recoveryInterest
        );
        vm.prank(recoveryAgent);
        usdt.approve(address(loanEngine), recoveryPrincipal + recoveryInterest);

        vm.prank(deployer);
        loanEngine.recoverLoan(
            1,
            recoveryPrincipal + recoveryInterest,
            recoveryAgent
        );

        (, , , , , , , , , , , , , , , uint256 totalRecovered, , ) = loanEngine
            .s_loans(1);

        assertEq(totalRecovered, recoveryPrincipal + recoveryInterest);
    }

    function test_RecoverLoan_RevertIf_NotWrittenOff() public {
        _createAndActivateLoan();

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__LoanNotRecoverable.selector,
                1
            )
        );
        loanEngine.recoverLoan(1, 1000000, recoveryAgent);
    }

    function test_RecoverLoan_RevertIf_ZeroRecovery() public {
        _createAndActivateLoan();

        vm.startPrank(deployer);
        loanEngine.declareDefault(1, keccak256("reason"), block.timestamp);
        loanEngine.writeOffLoan(1);

        vm.expectRevert(ILoanEngine.LoanEngine__ZeroRecovery.selector);
        loanEngine.recoverLoan(1, 0, recoveryAgent);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        INTEREST ACCRUAL TESTS
    //////////////////////////////////////////////////////////////*/

    function test_InterestAccrual_30Days() public {
        _createAndActivateLoan();

        uint256 timeElapsed = 30 days;
        vm.warp(block.timestamp + timeElapsed);

        // Trigger interest accrual via repayment
        deal(address(usdt), repaymentAgent, 1);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), 1);

        vm.prank(deployer);
        loanEngine.repayLoan(1, 0, 1, repaymentAgent, block.timestamp);

        (, , , , , , , , uint256 interestAccrued, , , , , , , , , ) = loanEngine
            .s_loans(1);

        uint256 expectedInterest = (testPrincipal * testAprBps * timeElapsed) /
            (365 days * 10_000);

        assertApproxEqRel(interestAccrued, expectedInterest, 0.01e18); // 1% tolerance
    }

    function test_InterestAccrual_365Days() public {
        _createAndActivateLoan();

        uint256 timeElapsed = 365 days;
        vm.warp(block.timestamp + timeElapsed);

        deal(address(usdt), repaymentAgent, 1);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), 1);

        vm.prank(deployer);
        loanEngine.repayLoan(1, 0, 1, repaymentAgent, block.timestamp);

        (, , , , , , , , uint256 interestAccrued, , , , , , , , , ) = loanEngine
            .s_loans(1);

        // After 1 year at 8% APR
        uint256 expectedInterest = (testPrincipal * testAprBps) / 10_000;

        assertApproxEqRel(interestAccrued, expectedInterest, 0.01e18);
    }

    /*//////////////////////////////////////////////////////////////
                        ADMIN FUNCTIONS TESTS
    //////////////////////////////////////////////////////////////*/

    function test_SetMaxOriginationFeeBps() public {
        vm.prank(deployer);
        loanEngine.setMaxOriginationFeeBps(1000);

        assertEq(loanEngine.s_maxOriginationFeeBps(), 1000);
    }

    function test_SetWhitelistedOffRampingEntity() public {
        address newEntity = makeAddr("newEntity");

        vm.prank(deployer);
        loanEngine.setWhitelistedOffRampingEntity(newEntity, true);

        assertTrue(loanEngine.whitelistedOffRampingEntities(newEntity));
    }

    function test_SetWhitelistedRepaymentAgent() public {
        address newAgent = makeAddr("newRepaymentAgent");

        vm.prank(deployer);
        loanEngine.setWhitelistedRepaymentAgent(newAgent, true);

        assertTrue(loanEngine.whitelistedRepaymentAgents(newAgent));
    }

    function test_SetWhitelistedRecoveryAgent() public {
        address newAgent = makeAddr("newRecoveryAgent");

        vm.prank(deployer);
        loanEngine.setWhitelistedRecoveryAgent(newAgent, true);

        assertTrue(loanEngine.whitelistedRecoveryAgents(newAgent));
    }

    /*//////////////////////////////////////////////////////////////
                        INTEGRATION TESTS
    //////////////////////////////////////////////////////////////*/

    function test_Integration_FullLoanLifecycle() public {
        // 1. Create loan
        testPublicInputs[2] = keccak256("nullifier12");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier12")
        );
        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        // 2. Activate loan
        vm.prank(deployer);
        loanEngine.activateLoan(1, offRampEntity, feeManager);

        // 3. Partial repayment after 90 days
        vm.warp(block.timestamp + 90 days);

        uint256 partialPrincipal = testPrincipal / 4;
        uint256 interest1 = (testPrincipal * testAprBps * 90 days) /
            (365 days * 10_000);

        deal(address(usdt), repaymentAgent, partialPrincipal + interest1);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), partialPrincipal + interest1);

        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            partialPrincipal,
            interest1,
            repaymentAgent,
            block.timestamp
        );

        // 4. Another partial repayment after 180 more days
        vm.warp(block.timestamp + 180 days);

        uint256 remainingPrincipal = testPrincipal - partialPrincipal;
        uint256 interest2 = (remainingPrincipal * testAprBps * 180 days) /
            (365 days * 10_000);

        deal(address(usdt), repaymentAgent, remainingPrincipal + interest2);
        vm.prank(repaymentAgent);
        usdt.approve(address(loanEngine), remainingPrincipal + interest2);

        vm.prank(deployer);
        loanEngine.repayLoan(
            1,
            remainingPrincipal,
            interest2,
            repaymentAgent,
            block.timestamp
        );

        // Verify final state
        (
            ,
            ,
            ,
            ,
            ,
            uint256 principalOutstanding,
            ,
            ,
            uint256 interestAccrued,
            ,
            ,
            ,
            ,
            ,
            ILoanEngine.LoanState state,
            ,
            ,

        ) = loanEngine.s_loans(1);

        assertEq(principalOutstanding, 0);
        assertEq(interestAccrued, 0);
        assertEq(uint256(state), uint256(ILoanEngine.LoanState.REPAID));
    }

    function test_Integration_DefaultAndRecovery() public {
        // Create a smaller loan to avoid exceeding deployed capital with interest
        vm.startPrank(deployer);

        uint256 smallerPrincipal = testPrincipal; // Must match liquidity due to bug

        testPublicInputs[2] = keccak256("nullifier13");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                smallerPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier13")
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        loanEngine.activateLoan(1, offRampEntity, feeManager);
        vm.stopPrank();

        // Let some time pass - REDUCE TO 30 DAYS
        vm.warp(block.timestamp + 30 days); // CHANGED from 200 days

        // Default
        vm.startPrank(deployer);
        loanEngine.declareDefault(
            1,
            keccak256("Payment default"),
            block.timestamp
        );

        // Write off
        loanEngine.writeOffLoan(1);
        vm.stopPrank();

        // Recovery
        uint256 recoveryAmount = 250_000 * USDT;
        deal(address(usdt), recoveryAgent, recoveryAmount);
        vm.prank(recoveryAgent);
        usdt.approve(address(loanEngine), recoveryAmount);

        vm.prank(deployer);
        loanEngine.recoverLoan(1, recoveryAmount, recoveryAgent);

        (, , , , , , , , , , , , , , , uint256 totalRecovered, , ) = loanEngine
            .s_loans(1);

        assertEq(totalRecovered, recoveryAmount);
    }

    /*//////////////////////////////////////////////////////////////
                        HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function _createAndConfigurePolicy(uint256 version) internal {
        creditPolicy.createPolicy(version);
        creditPolicy.updateEligibility(version, _createEligibilityCriteria());
        creditPolicy.updateRatios(version, _createFinancialRatios());
        creditPolicy.updateConcentration(version, _createConcentrationLimits());
        creditPolicy.updateAttestation(
            version,
            _createAttestationRequirements()
        );
        creditPolicy.updateCovenants(version, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(version, 1, _createMockTier("Tier 1"));
        creditPolicy.freezePolicy(version);
    }

    function _setupTranchePool() internal {
        tranchePool.setMaxAllocationCapSeniorTranche(10_000_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(5_000_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(2_000_000 * USDT);

        tranchePool.setMinimumDepositAmountSeniorTranche(500_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(100_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(50_000 * USDT);

        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);

        tranchePool.updateWhitelist(seniorUser1, true);
        tranchePool.updateWhitelist(juniorUser1, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser1, true);

        tranchePool.setLoanEngine(address(loanEngine));
    }

    function _fundUsers() internal {
        deal(address(usdt), seniorUser1, 5_000_000 * USDT);
        deal(address(usdt), juniorUser1, 2_000_000 * USDT);
        deal(address(usdt), equityUser1, 1_000_000 * USDT);
    }

    function _makeDeposits() internal {
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), 800_000 * USDT);
        tranchePool.depositSeniorTranche(800_000 * USDT);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), 150_000 * USDT);
        tranchePool.depositJuniorTranche(150_000 * USDT);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), 50_000 * USDT);
        tranchePool.depositEquityTranche(50_000 * USDT);
        vm.stopPrank();
    }

    function _createAndActivateLoan() internal returns (uint256) {
        vm.startPrank(deployer);
        testPublicInputs[2] = keccak256("nullifier14");
        uint256 loanId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                testTierId,
                testPrincipal,
                testAprBps,
                testOriginationFeeBps,
                testTermDays,
                testIndustry,
                block.timestamp,
                loanId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("nullifier14")
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);

        loanEngine.activateLoan(1, offRampEntity, feeManager);
        vm.stopPrank();

        return 1;
    }

    function _createEligibilityCriteria()
        internal
        pure
        returns (ICreditPolicy.EligibilityCriteria memory)
    {
        return
            ICreditPolicy.EligibilityCriteria({
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
        returns (ICreditPolicy.FinancialRatios memory)
    {
        return
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
    }

    function _createConcentrationLimits()
        internal
        pure
        returns (ICreditPolicy.ConcentrationLimits memory)
    {
        return
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
    }

    function _createAttestationRequirements()
        internal
        pure
        returns (ICreditPolicy.AttestationRequirements memory)
    {
        return
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
    }

    function _createMaintenanceCovenants()
        internal
        pure
        returns (ICreditPolicy.MaintenanceCovenants memory)
    {
        return
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
    }

    function _createMockTier(
        string memory name
    ) internal pure returns (ICreditPolicy.LoanTier memory) {
        return
            ICreditPolicy.LoanTier({
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
}
