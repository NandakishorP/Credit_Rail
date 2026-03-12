// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {LoanEngine} from "../../src/LoanEngine.sol";
import {ILoanEngine} from "../../src/interfaces/ILoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {Field} from "@poseidon2-evm/Field.sol";

/**
 * @title TestLoanEngineSecurity
 * @notice Security-focused tests for LoanEngine: initializer re-entry, UUPS upgrade
 *         authorization, pause/unpause, ZK proof validation edge cases.
 */
contract TestLoanEngineSecurity is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;
    LoanEngine loanEngine;
    MockLoanProofVerifier verifier;
    CreditPolicy creditPolicy;
    MockPoseidon2 mockPoseidon;

    address deployer = makeAddr("deployer");
    address attacker = makeAddr("attacker");
    address seniorUser1 = makeAddr("seniorUser1");
    address juniorUser1 = makeAddr("juniorUser1");
    address equityUser1 = makeAddr("equityUser1");
    address offRampEntity = makeAddr("offRampEntity");
    address repaymentAgent = makeAddr("repaymentAgent");
    address recoveryAgent = makeAddr("recoveryAgent");
    address feeManager = makeAddr("feeManager");

    uint256 public USDT = 1e6;

    bytes32 testBorrowerCommitment =
        bytes32(
            uint256(keccak256("borrower123")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );
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

    bytes testProofData = hex"1234";
    bytes32[] testPublicInputs;

    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);

        verifier = new MockLoanProofVerifier();

        // Deploy TranchePool
        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), deployer))
        );
        tranchePool = TranchePool(address(tpProxy));

        // Deploy CreditPolicy
        mockPoseidon = new MockPoseidon2();
        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer, address(mockPoseidon)))
        );
        creditPolicy = CreditPolicy(address(cpProxy));

        _setupCreditPolicy();

        // Deploy LoanEngine
        LoanEngine leImpl = new LoanEngine();
        ERC1967Proxy leProxy = new ERC1967Proxy(
            address(leImpl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    500,
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
        loanEngine = LoanEngine(address(leProxy));

        loanEngine.setUnderwriterAuthorization(
            testUnderwriterKeyX,
            testUnderwriterKeyY,
            true
        );

        testPublicInputs = new bytes32[](3);
        testPublicInputs[0] = creditPolicy.policyScopeHash(1, 1);

        _setupTranchePool();
        _setupWhitelists();
        vm.stopPrank();

        _fundAndDeposit();

        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);
    }

    // =========================================================================
    //                    INITIALIZER SECURITY
    // =========================================================================

    function test_Initialize_CannotReinitializeProxy() public {
        vm.expectRevert();
        loanEngine.initialize(
            address(creditPolicy),
            address(verifier),
            500,
            address(tranchePool),
            address(usdt),
            address(mockPoseidon),
            deployer
        );
    }

    function test_Initialize_RevertsOnZeroCreditPolicy() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(0),
                    address(verifier),
                    500,
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
    }

    function test_Initialize_RevertsOnZeroVerifier() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(0),
                    500,
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
    }

    function test_Initialize_RevertsOnZeroTranchePool() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    500,
                    address(0),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
    }

    function test_Initialize_RevertsOnZeroStablecoin() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    500,
                    address(tranchePool),
                    address(0),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
    }

    function test_Initialize_RevertsOnZeroPoseidon() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    500,
                    address(tranchePool),
                    address(usdt),
                    address(0),
                    deployer
                )
            )
        );
    }

    function test_Initialize_RevertsOnZeroAdmin() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    500,
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    address(0)
                )
            )
        );
    }

    function test_Initialize_RevertsOnExcessiveOriginationFee() public {
        LoanEngine impl = new LoanEngine();
        vm.expectRevert();
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(verifier),
                    10_001, // > 10,000 bps
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
    }

    // =========================================================================
    //                    UUPS UPGRADE AUTHORIZATION
    // =========================================================================

    function test_Upgrade_OnlyDefaultAdmin() public {
        LoanEngine newImpl = new LoanEngine();
        vm.prank(deployer);
        loanEngine.upgradeToAndCall(address(newImpl), "");
    }

    function test_Upgrade_RevertsForNonAdmin() public {
        LoanEngine newImpl = new LoanEngine();
        vm.prank(attacker);
        vm.expectRevert();
        loanEngine.upgradeToAndCall(address(newImpl), "");
    }

    // =========================================================================
    //                    PAUSE / UNPAUSE
    // =========================================================================

    function test_Pause_OnlyEmergencyAdmin() public {
        vm.prank(deployer);
        loanEngine.pause();
        assertTrue(loanEngine.paused());
    }

    function test_Unpause_OnlyEmergencyAdmin() public {
        vm.prank(deployer);
        loanEngine.pause();

        vm.prank(deployer);
        loanEngine.unpause();
        assertFalse(loanEngine.paused());
    }

    function test_Pause_RevertsForNonEmergencyAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        loanEngine.pause();
    }

    function test_Unpause_RevertsForNonEmergencyAdmin() public {
        vm.prank(deployer);
        loanEngine.pause();

        vm.prank(attacker);
        vm.expectRevert();
        loanEngine.unpause();
    }

    function test_CreateLoan_RevertsWhenPaused() public {
        vm.prank(deployer);
        loanEngine.pause();

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("pauseNullifier")
        );

        vm.prank(deployer);
        vm.expectRevert();
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_ActivateLoan_RevertsWhenPaused() public {
        // Create a loan first
        uint256 loanId = _createLoanHelper(keccak256("activatePauseNull"));

        vm.prank(deployer);
        loanEngine.pause();

        vm.prank(deployer);
        vm.expectRevert();
        loanEngine.activateLoan(loanId, offRampEntity, feeManager);
    }

    // =========================================================================
    //                    ZK PROOF SECURITY
    // =========================================================================

    function test_CreateLoan_RevertsOnNullifierReplay() public {
        bytes32 nullifier = keccak256("replayNullifier");
        _createLoanHelper(nullifier);

        // Attempt to reuse the same nullifier
        testPublicInputs[2] = nullifier;
        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            100_000 * USDT,
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ProofAlreadyUsed.selector);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnExpiredProof() public {
        vm.warp(1_700_000_000); // realistic timestamp to avoid underflow
        bytes32 nullifier = keccak256("expiredProofNull");
        uint256 oldTimestamp = block.timestamp - 2 hours; // > 1 hour

        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                oldTimestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            100_000 * USDT,
            800,
            100,
            365,
            oldTimestamp
        );

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__ProofExpired.selector,
                oldTimestamp,
                block.timestamp
            )
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnFutureProof() public {
        bytes32 nullifier = keccak256("futureProofNull");
        uint256 futureTimestamp = block.timestamp + 1 hours;

        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                futureTimestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            100_000 * USDT,
            800,
            100,
            365,
            futureTimestamp
        );

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__ProofFromFuture.selector,
                futureTimestamp,
                block.timestamp
            )
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnUnauthorizedUnderwriter() public {
        bytes32 nullifier = keccak256("badUnderwriterNull");
        bytes32 badKeyX = bytes32(uint256(999));
        bytes32 badKeyY = bytes32(uint256(998));

        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;

        Field.Type[] memory inputs = new Field.Type[](11);
        inputs[0] = Field.toField(uint256(testBorrowerCommitment));
        inputs[1] = Field.toField(uint256(badKeyX));
        inputs[2] = Field.toField(uint256(badKeyY));
        inputs[3] = Field.toField(uint256(1));
        inputs[4] = Field.toField(100_000 * USDT);
        inputs[5] = Field.toField(uint256(800));
        inputs[6] = Field.toField(uint256(100));
        inputs[7] = Field.toField(uint256(365));
        inputs[8] = Field.toField(uint256(testIndustry));
        inputs[9] = Field.toField(block.timestamp);
        inputs[10] = Field.toField(nextId);

        testPublicInputs[1] = bytes32(
            Field.toUint256(mockPoseidon.hash(inputs))
        );

        ILoanEngine.CreateLoanParams memory params = ILoanEngine
            .CreateLoanParams({
                borrowerCommitment: testBorrowerCommitment,
                nullifierHash: nullifier,
                policyVersion: 1,
                tierId: 1,
                principalIssued: 100_000 * USDT,
                aprBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                industry: testIndustry,
                underwriterKeyX: badKeyX,
                underwriterKeyY: badKeyY,
                proofTimestamp: block.timestamp
            });

        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__InvalidUnderwriterKey.selector);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnInsufficientPoolLiquidity() public {
        bytes32 nullifier = keccak256("bigLoanNull");
        uint256 hugePrincipal = 999_999_999 * USDT; // Far more than pool has

        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                hugePrincipal,
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            hugePrincipal,
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert(
            ILoanEngine.LoanEngine__InsufficientPoolLiquidity.selector
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnInvalidPublicInputsLength() public {
        bytes32[] memory shortInputs = new bytes32[](2); // Need 3
        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            keccak256("shortInputsNull")
        );

        vm.prank(deployer);
        vm.expectRevert(
            ILoanEngine.LoanEngine__InvalidPublicInputsLength.selector
        );
        loanEngine.createLoan(params, testProofData, shortInputs);
    }

    function test_CreateLoan_RevertsOnPolicyNotActive() public {
        // Create policy 99, populate all sections, freeze it, then deactivate it.
        // This way isPolicyFrozen(99)==true but isPolicyActive(99)==false.
        vm.startPrank(deployer);
        creditPolicy.createPolicy(99);
        creditPolicy.updateEligibility(
            99,
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_000_000,
                minEBITDA: 100_000,
                minTangibleNetWorth: 5_000_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );
        creditPolicy.updateRatios(
            99,
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            })
        );
        creditPolicy.updateConcentration(
            99,
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            })
        );
        creditPolicy.updateAttestation(
            99,
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            })
        );
        creditPolicy.updateCovenants(
            99,
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_000_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            })
        );
        creditPolicy.setLoanTier(
            99,
            1,
            ICreditPolicy.LoanTier({
                name: "Tier 1",
                minRevenue: 1_000_000,
                maxRevenue: 5_000_000,
                minEBITDA: 100_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            })
        );
        creditPolicy.setPolicyDocument(99, keccak256("doc99"), "ipfs://doc99");
        creditPolicy.freezePolicy(99);
        // Now deactivate to make isPolicyActive==false while frozen==true
        creditPolicy.deActivatePolicy(99);
        vm.stopPrank();

        bytes32 nullifier = keccak256("inactivePolicyNull");
        uint256 nextId = loanEngine.getNextLoanId();

        bytes32[] memory inputs = new bytes32[](3);
        inputs[0] = creditPolicy.policyScopeHash(99, 1);
        inputs[2] = nullifier;
        inputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            99,
            1,
            100_000 * USDT,
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__PolicyNotActive.selector,
                99
            )
        );
        loanEngine.createLoan(params, testProofData, inputs);
    }

    function test_CreateLoan_RevertsOnExcludedIndustry() public {
        bytes32 excludedIndustry = bytes32(
            uint256(keccak256("GAMBLING")) %
                21888242871839275222246405745257275088548364400416034343698204186575808495617
        );

        // Create a new policy version 2, exclude industry, and freeze it
        vm.startPrank(deployer);
        creditPolicy.createPolicy(2);
        creditPolicy.updateEligibility(
            2,
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_000_000,
                minEBITDA: 100_000,
                minTangibleNetWorth: 5_000_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );
        creditPolicy.updateRatios(
            2,
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            })
        );
        creditPolicy.updateConcentration(
            2,
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            })
        );
        creditPolicy.updateAttestation(
            2,
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            })
        );
        creditPolicy.updateCovenants(
            2,
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_000_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            })
        );
        creditPolicy.setLoanTier(
            2,
            1,
            ICreditPolicy.LoanTier({
                name: "Tier 1",
                minRevenue: 1_000_000,
                maxRevenue: 5_000_000,
                minEBITDA: 100_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            })
        );
        creditPolicy.excludeIndustry(2, excludedIndustry);
        creditPolicy.setPolicyDocument(2, keccak256("doc2"), "ipfs://doc2");
        creditPolicy.freezePolicy(2);
        vm.stopPrank();

        bytes32 scopeHash2 = creditPolicy.policyScopeHash(2, 1);

        bytes32 nullifier = keccak256("excludedIndustryNull");
        uint256 nextId = loanEngine.getNextLoanId();

        bytes32[] memory inputs2 = new bytes32[](3);
        inputs2[0] = scopeHash2;
        inputs2[2] = nullifier;
        inputs2[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                excludedIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = ILoanEngine
            .CreateLoanParams({
                borrowerCommitment: testBorrowerCommitment,
                nullifierHash: nullifier,
                policyVersion: 2,
                tierId: 1,
                principalIssued: 100_000 * USDT,
                aprBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                industry: excludedIndustry,
                underwriterKeyX: testUnderwriterKeyX,
                underwriterKeyY: testUnderwriterKeyY,
                proofTimestamp: block.timestamp
            });

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__IndustryExcluded.selector,
                2,
                excludedIndustry
            )
        );
        loanEngine.createLoan(params, testProofData, inputs2);
    }

    function test_CreateLoan_RevertsOnValueExceedsU64() public {
        bytes32 nullifier = keccak256("u64OverflowNull");
        uint256 tooBig = uint256(type(uint64).max) + 1;

        testPublicInputs[2] = nullifier;
        // principalIssued > u64 max
        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            tooBig, // principal exceeds u64
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                ILoanEngine.LoanEngine__ValueExceedsU64.selector,
                "principalIssued",
                tooBig
            )
        );
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    function test_CreateLoan_RevertsOnWrongPolicyScopeHash() public {
        bytes32 nullifier = keccak256("wrongScopeNull");
        uint256 nextId = loanEngine.getNextLoanId();

        bytes32[] memory badInputs = new bytes32[](3);
        badInputs[0] = keccak256("wrong_scope"); // Wrong policy scope hash
        badInputs[2] = nullifier;
        badInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            100_000 * USDT,
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__InvalidPublicInputs.selector);
        loanEngine.createLoan(params, testProofData, badInputs);
    }

    function test_CreateLoan_RevertsOnZeroPrincipal() public {
        bytes32 nullifier = keccak256("zeroPrincipalNull");
        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                0, // zero principal
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildParams(
            nullifier,
            1,
            1,
            0, // zero
            800,
            100,
            365,
            block.timestamp
        );

        vm.prank(deployer);
        vm.expectRevert();
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    // =========================================================================
    //                    HELPERS
    // =========================================================================

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

    function _buildStandardParams(
        bytes32 nullifier
    ) internal view returns (ILoanEngine.CreateLoanParams memory) {
        return
            _buildParams(
                nullifier,
                1,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                block.timestamp
            );
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
        return Field.toUint256(mockPoseidon.hash(inputs));
    }

    function _createLoanHelper(bytes32 nullifier) internal returns (uint256) {
        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                testBorrowerCommitment,
                testUnderwriterKeyX,
                testUnderwriterKeyY,
                1,
                100_000 * USDT,
                800,
                100,
                365,
                testIndustry,
                block.timestamp,
                nextId
            )
        );

        ILoanEngine.CreateLoanParams memory params = _buildStandardParams(
            nullifier
        );

        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
        return nextId;
    }

    function _setupCreditPolicy() internal {
        creditPolicy.createPolicy(1);
        creditPolicy.updateEligibility(
            1,
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_000_000,
                minEBITDA: 100_000,
                minTangibleNetWorth: 5_000_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );
        creditPolicy.updateRatios(
            1,
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            })
        );
        creditPolicy.updateConcentration(
            1,
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            })
        );
        creditPolicy.updateAttestation(
            1,
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            })
        );
        creditPolicy.updateCovenants(
            1,
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_000_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            })
        );
        creditPolicy.setMaxTiers(2);
        creditPolicy.setLoanTier(
            1,
            1,
            ICreditPolicy.LoanTier({
                name: "Tier 1",
                minRevenue: 1_000_000,
                maxRevenue: 5_000_000,
                minEBITDA: 100_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            })
        );
        creditPolicy.setPolicyDocument(1, keccak256("doc"), "ipfs://doc");
        creditPolicy.freezePolicy(1);
    }

    function _setupTranchePool() internal {
        tranchePool.setMaxDepositCapSeniorTranche(10_000_000 * USDT);
        tranchePool.setMaxDepositCapJuniorTranche(5_000_000 * USDT);
        tranchePool.setMaxDepositCapEquityTranche(3_000_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(50_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(50_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setSeniorAPR(500);
        tranchePool.setTargetJuniorAPR(1000);
        tranchePool.updateWhitelist(seniorUser1, true);
        tranchePool.updateWhitelist(juniorUser1, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser1, true);
        tranchePool.setLoanEngine(address(loanEngine));
    }

    function _setupWhitelists() internal {
        loanEngine.setWhitelistedOffRampingEntity(offRampEntity, true);
        loanEngine.setWhitelistedRepaymentAgent(repaymentAgent, true);
        loanEngine.setWhitelistedRecoveryAgent(recoveryAgent, true);
        loanEngine.setWhitelistedFeeManager(feeManager, true);
    }

    function _fundAndDeposit() internal {
        deal(address(usdt), seniorUser1, 5_000_000 * USDT);
        deal(address(usdt), juniorUser1, 2_000_000 * USDT);
        deal(address(usdt), equityUser1, 1_000_000 * USDT);

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
}
