// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {LoanEngine} from "../../src/LoanEngine.sol";
import {ILoanEngine} from "../../src/interfaces/ILoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {Field} from "@poseidon2-evm/Field.sol";

/**
 * @title TestLoanEngineEvents
 * @notice Tests that LoanEngine emits the correct events with correct parameters
 *         for all 11 event types.
 */
contract TestLoanEngineEvents is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;
    LoanEngine loanEngine;
    MockLoanProofVerifier verifier;
    CreditPolicy creditPolicy;
    MockPoseidon2 mockPoseidon;

    address deployer = makeAddr("deployer");
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

        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), deployer))
        );
        tranchePool = TranchePool(address(tpProxy));

        mockPoseidon = new MockPoseidon2();

        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer))
        );
        creditPolicy = CreditPolicy(address(cpProxy));

        _setupCreditPolicy();

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

        loanEngine.setWhitelistedOffRampingEntity(offRampEntity, true);
        loanEngine.setWhitelistedRepaymentAgent(repaymentAgent, true);
        loanEngine.setWhitelistedRecoveryAgent(recoveryAgent, true);
        loanEngine.setWhitelistedFeeManager(feeManager, true);
        vm.stopPrank();

        _fundAndDeposit();

        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);
    }

    // =========================================================================
    //                    LoanCreated EVENT
    // =========================================================================

    function test_Event_LoanCreated() public {
        uint256 nextId = loanEngine.getNextLoanId();
        bytes32 nullifier = keccak256("eventNull1");
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                1,
                100_000 * USDT,
                800,
                100,
                365,
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

        vm.expectEmit(true, true, true, true);
        emit ILoanEngine.LoanCreated(
            nextId,
            testBorrowerCommitment,
            100_000 * USDT,
            1,
            block.timestamp
        );

        vm.prank(deployer);
        loanEngine.createLoan(params, testProofData, testPublicInputs);
    }

    // =========================================================================
    //                    LoanActivated EVENT
    // =========================================================================

    function test_Event_LoanActivated() public {
        uint256 loanId = _createLoanHelper(keccak256("activateEventNull"));

        uint256 principal = 100_000 * USDT;
        uint256 maturity = block.timestamp + (365 * 1 days);

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.LoanActivated(
            loanId,
            principal,
            block.timestamp,
            block.timestamp,
            maturity
        );

        vm.prank(deployer);
        loanEngine.activateLoan(loanId, offRampEntity, feeManager);
    }

    // =========================================================================
    //                    WhitelistedOffRampingEntityUpdated EVENT
    // =========================================================================

    function test_Event_WhitelistedOffRampingEntityUpdated() public {
        address newEntity = makeAddr("newEntity");

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.WhitelistedOffRampingEntityUpdated(newEntity, true);

        vm.prank(deployer);
        loanEngine.setWhitelistedOffRampingEntity(newEntity, true);
    }

    // =========================================================================
    //                    WhitelistedRecoveryAgentUpdated EVENT
    // =========================================================================

    function test_Event_WhitelistedRecoveryAgentUpdated() public {
        address newAgent = makeAddr("newRecoveryAgent");

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.WhitelistedRecoveryAgentUpdated(newAgent, true);

        vm.prank(deployer);
        loanEngine.setWhitelistedRecoveryAgent(newAgent, true);
    }

    // =========================================================================
    //                    WhitelistedRepaymentAgentUpdated EVENT
    // =========================================================================

    function test_Event_WhitelistedRepaymentAgentUpdated() public {
        address newAgent = makeAddr("newRepayAgent");

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.WhitelistedRepaymentAgentUpdated(newAgent, true);

        vm.prank(deployer);
        loanEngine.setWhitelistedRepaymentAgent(newAgent, true);
    }

    // =========================================================================
    //                    WhitelistedFeeManagerUpdated EVENT
    // =========================================================================

    function test_Event_WhitelistedFeeManagerUpdated() public {
        address newMgr = makeAddr("newFeeManager");

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.WhitelistedFeeManagerUpdated(newMgr, true);

        vm.prank(deployer);
        loanEngine.setWhitelistedFeeManager(newMgr, true);
    }

    // =========================================================================
    //                    MaxOriginationFeeBpsUpdated EVENT
    // =========================================================================

    function test_Event_MaxOriginationFeeBpsUpdated() public {
        vm.expectEmit(false, false, false, true);
        emit ILoanEngine.MaxOriginationFeeBpsUpdated(300);

        vm.prank(deployer);
        loanEngine.setMaxOriginationFeeBps(300);
    }

    // =========================================================================
    //                    UnderwriterAuthorizationUpdated EVENT
    // =========================================================================

    function test_Event_UnderwriterAuthorizationUpdated() public {
        bytes32 keyX = bytes32(uint256(11));
        bytes32 keyY = bytes32(uint256(22));
        bytes32 keyHash = keccak256(abi.encodePacked(keyX, keyY));

        vm.expectEmit(true, false, false, true);
        emit ILoanEngine.UnderwriterAuthorizationUpdated(
            keyHash,
            keyX,
            keyY,
            true,
            block.timestamp
        );

        vm.prank(deployer);
        loanEngine.setUnderwriterAuthorization(keyX, keyY, true);
    }

    // =========================================================================
    //                    DefaultAdminChanged EVENT
    // =========================================================================

    function test_Event_DefaultAdminChanged() public {
        address newAdmin = makeAddr("newAdmin");

        vm.expectEmit(true, true, false, false);
        emit ILoanEngine.DefaultAdminChanged(deployer, newAdmin);

        vm.prank(deployer);
        loanEngine.changeDefaultAdmin(newAdmin);
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

    function _computeLoanHash(
        uint8 tierId,
        uint256 principal,
        uint256 apr,
        uint256 fee,
        uint256 term,
        uint256 timestamp,
        uint256 loanId
    ) internal view returns (uint256) {
        Field.Type[] memory inputs = new Field.Type[](11);
        inputs[0] = Field.toField(uint256(testBorrowerCommitment));
        inputs[1] = Field.toField(uint256(testUnderwriterKeyX));
        inputs[2] = Field.toField(uint256(testUnderwriterKeyY));
        inputs[3] = Field.toField(uint256(tierId));
        inputs[4] = Field.toField(principal);
        inputs[5] = Field.toField(apr);
        inputs[6] = Field.toField(fee);
        inputs[7] = Field.toField(term);
        inputs[8] = Field.toField(uint256(testIndustry));
        inputs[9] = Field.toField(timestamp);
        inputs[10] = Field.toField(loanId);
        return Field.toUint256(mockPoseidon.hash(inputs));
    }

    function _createLoanHelper(bytes32 nullifier) internal returns (uint256) {
        uint256 nextId = loanEngine.getNextLoanId();
        testPublicInputs[2] = nullifier;
        testPublicInputs[1] = bytes32(
            _computeLoanHash(
                1,
                100_000 * USDT,
                800,
                100,
                365,
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
        loanEngine.createLoan(params, testProofData, testPublicInputs);
        return nextId;
    }

    function _setupCreditPolicy() internal {
        creditPolicy.createPolicy(1);
        creditPolicy.setPolicyScopeHash(1, 1, keccak256("scopeHash_v1_tier1"));
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
