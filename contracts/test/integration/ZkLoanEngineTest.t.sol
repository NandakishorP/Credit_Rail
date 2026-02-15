// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test, console2} from "forge-std/Test.sol";
import {LoanEngine} from "../../src/LoanEngine.sol";
import {HonkVerifier} from "../../src/Verifier.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {ERC20} from "lib/openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";

// --- Mocks ---

contract MockUSDC is ERC20 {
    constructor() ERC20("USDC", "USDC") {}

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }
}

contract MockCreditPolicy is ICreditPolicy {
    mapping(uint256 => bytes32) public policyHashes;

    // Minimal Implementation
    function createPolicy(uint256) external {}

    function freezePolicy(uint256) external {}

    function deActivatePolicy(uint256) external {}

    function updateEligibility(
        uint256,
        CreditPolicy.EligibilityCriteria calldata
    ) external {}

    function updateRatios(
        uint256,
        CreditPolicy.FinancialRatios calldata
    ) external {}

    function updateConcentration(
        uint256,
        CreditPolicy.ConcentrationLimits calldata
    ) external {}

    function updateAttestation(
        uint256,
        CreditPolicy.AttestationRequirements calldata
    ) external {}

    function updateCovenants(
        uint256,
        CreditPolicy.MaintenanceCovenants calldata
    ) external {}

    function setLoanTier(
        uint256,
        uint8,
        CreditPolicy.LoanTier calldata
    ) external {}

    function excludeIndustry(uint256, bytes32) external {}

    function includeIndustry(uint256, bytes32) external {}

    function setPolicyDocument(uint256, bytes32, string calldata) external {}

    function tierExistsInPolicy(uint256, uint8) external pure returns (bool) {
        return true;
    }

    function changePolicyAdmin(address) external {}

    function isPolicyActive(uint256) external pure returns (bool) {
        return true;
    }

    function isPolicyFrozen(uint256) external pure returns (bool) {
        return true;
    }

    function isIndustryExcluded(uint256, bytes32) external pure returns (bool) {
        return false;
    }

    function policyScopeHash(uint256 version) external view returns (bytes32) {
        return policyHashes[version];
    }

    function setPolicyScopeHash(uint256 version, bytes32 hash) external {
        policyHashes[version] = hash;
    }
}

contract MockTranchePool is ITranchePool {
    function getPoolState() external pure returns (TranchePool.PoolState) {
        return TranchePool.PoolState.DEPLOYED;
    }

    function withdrawEquityTrancheByAmount(uint256) external {}

    function withdrawJuniorTrancheByAmount(uint256) external {}

    function withdrawSeniorTrancheByAmount(uint256) external {}

    function withdrawEquityTranche(uint256) external {}

    function withdrawJuniorTranche(uint256) external {}

    function withdrawSeniorTranche(uint256) external {}

    function onInterestAccrued(uint256) external {}

    function onRepayment(uint256, uint256) external {}

    function onRecovery(uint256) external {}

    function allocateCapital(
        uint256 totalDisbursement,
        uint256,
        address,
        address
    ) external pure returns (uint256, uint256, uint256) {
        // Just return full amount as Senior for simplicity in this unit test unless constraints exist
        return (totalDisbursement, 0, 0);
    }

    function depositEquityTranche(uint256) external {}

    function depositJuniorTranche(uint256) external {}

    function depositSeniorTranche(uint256) external {}

    function updateEquityTrancheWhiteList(address, bool) external {}

    function updateWhitelist(address, bool) external {}

    function onLoss(uint256, uint256) external {}

    function setLoanEngine(address) external {}

    function setTargetJuniorAPR(uint256) external {}

    function setSeniorAPR(uint256) external {}

    function setTrancheCapitalAllocationFactorJunior(uint256) external {}

    function setTrancheCapitalAllocationFactorSenior(uint256) external {}

    function setMinimumDepositAmountEquityTranche(uint256) external {}

    function setMinimumDepositAmountSeniorTranche(uint256) external {}

    function setMinimumDepositAmountJuniorTranche(uint256) external {}

    function getEquityTrancheBalance(address) external pure returns (uint256) {
        return 0;
    }

    function getJuniorTrancheBalance(address) external pure returns (uint256) {
        return 0;
    }

    function getSeniorTrancheBalance(address) external pure returns (uint256) {
        return 0;
    }

    function getSeniorAllocationRatio() external pure returns (uint256) {
        return 0;
    }

    function getJuniorAllocationRatio() external pure returns (uint256) {
        return 0;
    }

    function getTotalIdleValue() external pure returns (uint256) {
        return type(uint256).max;
    }
}

// --- Test Contract ---

contract ZkLoanEngineTest is Test {
    LoanEngine loanEngine;
    HonkVerifier verifier;
    MockCreditPolicy creditPolicy;
    MockTranchePool tranchePool;
    MockUSDC usdc;

    function setUp() public {
        verifier = new HonkVerifier();
        creditPolicy = new MockCreditPolicy();
        tranchePool = new MockTranchePool();
        usdc = new MockUSDC();

        // Deploy MockPoseidon2 for testing
        MockPoseidon2 poseidon = new MockPoseidon2();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            1000,
            address(tranchePool),
            address(usdc),
            address(poseidon)
        );
    }

    struct ProofResult {
        bytes proof;
        bytes32[] publicInputs;
        bytes32 policyHash;
        bytes32 loanHash;
        bytes32 nullifierHash;
        bytes32 borrowerCommitment;
        bytes32 underwriterKeyX;
        bytes32 underwriterKeyY;
        bytes32 industryHash;
        uint256 timestamp;
    }

    function _runProofGeneratorFFI() internal returns (ProofResult memory p) {
        // Run the TypeScript proof generator via FFI
        string[] memory inputs = new string[](3);
        inputs[0] = "npx";
        inputs[1] = "ts-node";
        inputs[2] = "../zk-scripts/generate_proof_ffi.ts";

        bytes memory result = vm.ffi(inputs);

        // Decode directly into the struct to avoid stack depth issues
        (
            p.proof,
            p.publicInputs,
            p.policyHash,
            p.loanHash,
            p.nullifierHash,
            p.borrowerCommitment,
            p.underwriterKeyX,
            p.underwriterKeyY,
            p.industryHash,
            p.timestamp
        ) = abi.decode(
            result,
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
    }

    function _buildCreateLoanParams(
        ProofResult memory p
    ) internal pure returns (LoanEngine.CreateLoanParams memory) {
        return
            LoanEngine.CreateLoanParams({
                borrowerCommitment: p.borrowerCommitment,
                nullifierHash: p.nullifierHash,
                policyVersion: 1,
                tierId: 1,
                principalIssued: 500000,
                aprBps: 1200,
                originationFeeBps: 100,
                termDays: 365,
                industry: p.industryHash,
                underwriterKeyX: p.underwriterKeyX,
                underwriterKeyY: p.underwriterKeyY,
                proofTimestamp: p.timestamp
            });
    }

    function _createLoanWithProof(ProofResult memory p) internal {
        // Setup: configure policy hash for version 1
        creditPolicy.setPolicyScopeHash(1, p.policyHash);

        // Authorize the underwriter
        loanEngine.setUnderwriterAuthorization(
            p.underwriterKeyX,
            p.underwriterKeyY,
            true
        );

        // Warp to match the proof timestamp so proof is not expired/from future
        vm.warp(p.timestamp);

        // Build params struct
        LoanEngine.CreateLoanParams memory params = _buildCreateLoanParams(p);

        // Call createLoan with struct
        loanEngine.createLoan(params, p.proof, p.publicInputs);

        console2.log("Loan Created Successfully with Valid ZK Proof!");
    }

    function test_CreateLoanWithZkProof() public {
        // Generate proof via FFI
        ProofResult memory proofData = _runProofGeneratorFFI();

        // Create loan using the generated proof
        _createLoanWithProof(proofData);

        // Verify the loan was created
        (uint256 loanId, , , , , , , , , , , , , , , , , ) = loanEngine.s_loans(
            1
        );
        assertEq(loanId, 1, "Loan should have been created with ID 1");

        // Verify nullifier was marked as used
        assertTrue(
            loanEngine.s_nullifierHashes(proofData.nullifierHash),
            "Nullifier should be marked as used"
        );
    }

    function test_RejectDuplicateNullifier() public {
        // Generate proof via FFI
        ProofResult memory proofData = _runProofGeneratorFFI();

        // Create loan first time - should succeed
        _createLoanWithProof(proofData);

        // Re-configure for second attempt (reset policy hash since createLoan increments loanId)
        creditPolicy.setPolicyScopeHash(1, proofData.policyHash);

        // Build params struct
        LoanEngine.CreateLoanParams memory params = _buildCreateLoanParams(
            proofData
        );

        // Try to create loan again with same proof - should fail due to nullifier reuse
        vm.expectRevert(LoanEngine.LoanEngine__ProofAlreadyUsed.selector);
        loanEngine.createLoan(params, proofData.proof, proofData.publicInputs);
    }

    function test_RejectUnauthorizedUnderwriter() public {
        // Generate proof via FFI
        ProofResult memory proofData = _runProofGeneratorFFI();

        // Setup policy but DON'T authorize the underwriter
        creditPolicy.setPolicyScopeHash(1, proofData.policyHash);
        vm.warp(proofData.timestamp);

        // Build params struct
        LoanEngine.CreateLoanParams memory params = _buildCreateLoanParams(
            proofData
        );

        // Should revert with invalid underwriter key
        vm.expectRevert(LoanEngine.LoanEngine__InvalidUnderwriterKey.selector);
        loanEngine.createLoan(params, proofData.proof, proofData.publicInputs);
    }

    function test_RejectExpiredProof() public {
        // Generate proof via FFI
        ProofResult memory proofData = _runProofGeneratorFFI();

        // Setup
        creditPolicy.setPolicyScopeHash(1, proofData.policyHash);
        loanEngine.setUnderwriterAuthorization(
            proofData.underwriterKeyX,
            proofData.underwriterKeyY,
            true
        );

        // Warp far into the future so proof is expired (> 1 hour)
        vm.warp(proofData.timestamp + 2 hours);

        // Build params struct
        LoanEngine.CreateLoanParams memory params = _buildCreateLoanParams(
            proofData
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                LoanEngine.LoanEngine__ProofExpired.selector,
                proofData.timestamp,
                proofData.timestamp + 2 hours
            )
        );
        loanEngine.createLoan(params, proofData.proof, proofData.publicInputs);
    }

    function test_RejectFutureProof() public {
        // Generate proof via FFI
        ProofResult memory proofData = _runProofGeneratorFFI();

        // Setup
        creditPolicy.setPolicyScopeHash(1, proofData.policyHash);
        loanEngine.setUnderwriterAuthorization(
            proofData.underwriterKeyX,
            proofData.underwriterKeyY,
            true
        );

        // Warp to BEFORE the proof timestamp
        vm.warp(proofData.timestamp - 10);

        // Build params struct
        LoanEngine.CreateLoanParams memory params = _buildCreateLoanParams(
            proofData
        );

        vm.expectRevert(
            abi.encodeWithSelector(
                LoanEngine.LoanEngine__ProofFromFuture.selector,
                proofData.timestamp,
                proofData.timestamp - 10
            )
        );
        loanEngine.createLoan(params, proofData.proof, proofData.publicInputs);
    }
}
