/**
 * Create Loan with ZK Proof
 * 
 * This script:
 * 1. Generates a ZK proof using the Noir circuit
 * 2. Submits createLoan transaction to LoanEngine on anvil-zksync
 */

import { Barretenberg, UltraHonkBackend, Fr } from "@aztec/bb.js";
import { Noir } from "@noir-lang/noir_js";
import { ethers } from "ethers";
import fs from "fs";
import path from "path";
import { generateDeterministicKeypair, schnorrSign, toHex32 } from "./grumpkin";

// Configuration
const RPC_URL = process.env.RPC_URL || "http://127.0.0.1:8546";
const PRIVATE_KEY = process.env.PRIVATE_KEY || "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
const LOAN_ENGINE = process.env.LOAN_ENGINE || "0xb98e374C912ff8C02ac7363c57d5bfdb48f40d53";
const CREDIT_POLICY = process.env.CREDIT_POLICY || "0x22D151A1313d9B517Fa437F1F5B3744E636D8790";
const TRANCHE_POOL = process.env.TRANCHE_POOL || "0xd7385ba726A7b72933E63FCb0Dfee8Bcae63478c";
const USDC = process.env.USDC || "0x82778c3185fD0666d3f34F8930B4287405D9fBe4";
const VERIFIER = process.env.VERIFIER || "0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe";

// Load circuit
const circuitPath = path.resolve(__dirname, "../circuits/target/circuits.json");
const circuit = JSON.parse(fs.readFileSync(circuitPath, "utf-8"));

const HONK_VERIFIER_ABI = [
  "function verify(bytes calldata proof, bytes32[] calldata publicInputs) external returns (bool)"
];

// LoanEngine ABI (partial)
const LOAN_ENGINE_ABI = [
  `function createLoan(
    (bytes32 borrowerCommitment, bytes32 nullifierHash, uint256 policyVersion, uint8 tierId, uint256 principalIssued, uint256 aprBps, uint256 originationFeeBps, uint256 termDays, bytes32 industry, bytes32 underwriterKeyX, bytes32 underwriterKeyY, uint256 proofTimestamp) params,
    bytes calldata proofData,
    bytes32[] calldata publicInputs
  ) external`,
  "function getNextLoanId() external view returns (uint256)",
  "function getLoanDetails(uint256 loanId) external view returns (tuple(uint8 state, bytes32 borrowerCommitment, uint256 policyVersion, uint8 tierId, uint256 principalIssued, uint256 aprBps, uint256 originationFeeBps, uint256 termDays, bytes32 industry, uint256 interestEarned, uint256 principalRepaid, bytes32 nullifierHash, uint256 createdAt, bytes32 underwriterKeyX, bytes32 underwriterKeyY))",
  "function setUnderwriterAuthorization(bytes32 keyX, bytes32 keyY, bool authorized) external",
  "function setWhitelistedOffRampingEntity(address entity, bool whitelisted) external",
  "function authorizedUnderwriters(bytes32 keyHash) external view returns (bool)"
];

const CREDIT_POLICY_ABI = [
  "function createPolicy(uint256 version) external",
  "function freezePolicy(uint256 policyId) external",
  "function isPolicyFrozen(uint256 policyId) external view returns (bool)",
  "function policyCreated(uint256 version) external view returns (bool)",
  "function policyScopeHash(uint256 version) external view returns (bytes32)",
  `function updateEligibility(uint256 version, (uint256 minAnnualRevenue, uint256 minEBITDA, uint256 minTangibleNetWorth, uint256 minBusinessAgeDays, uint256 maxDefaultsLast36Months, bool bankruptcyExcluded) data) external`,
  `function updateRatios(uint256 version, (uint256 maxTotalDebtToEBITDA, uint256 minInterestCoverageRatio, uint256 minCurrentRatio, uint256 minEBITDAMarginBps) data) external`,
  `function updateConcentration(uint256 version, (uint256 maxSingleBorrowerBps, uint256 maxIndustryConcentrationBps) data) external`,
  `function updateAttestation(uint256 version, (uint256 maxAttestationAgeDays, uint256 reAttestationFrequencyDays, bool requiresCPAAttestation) data) external`,
  `function updateCovenants(uint256 version, (uint256 maxLeverageRatio, uint256 minCoverageRatio, uint256 minLiquidityAmount, bool allowsDividends, uint256 reportingFrequencyDays) data) external`,
  `function setLoanTier(uint256 version, uint8 tierId, (string name, uint256 minRevenue, uint256 maxRevenue, uint256 minEBITDA, uint256 maxDebtToEBITDA, uint256 maxLoanToEBITDA, uint256 interestRateBps, uint256 originationFeeBps, uint256 termDays, bool active) tier) external`,
  `function setPolicyDocument(uint256 version, bytes32 hash, string uri) external`,
  `function setPolicyScopeHash(uint256 version, bytes32 hash) external`
];

const TRANCHE_POOL_ABI = [
  "function whitelistAddress(address addr) external",
  "function isAddressWhitelisted(address addr) external view returns (bool)",
  "function getPoolState() external view returns (uint8)",
  "function commit() external",
  "function deploy() external",
  "function allocateCapital(address loanEngine, uint256 amount) external",
  "function getAllocation(address loanEngine) external view returns (uint256)"
];

const ERC20_ABI = [
  "function mint(address to, uint256 amount) external",
  "function approve(address spender, uint256 amount) external returns (bool)",
  "function balanceOf(address account) external view returns (uint256)",
  "function transfer(address to, uint256 amount) external returns (bool)"
];

async function main() {
  console.log("=".repeat(60));
  console.log("Create Loan with ZK Proof");
  console.log("=".repeat(60));
  console.log(`LoanEngine: ${LOAN_ENGINE}`);
  console.log(`RPC URL: ${RPC_URL}`);
  console.log("");

  // Setup provider and signer
  const provider = new ethers.JsonRpcProvider(RPC_URL);
  const signer = new ethers.Wallet(PRIVATE_KEY, provider);
  const loanEngine = new ethers.Contract(LOAN_ENGINE, LOAN_ENGINE_ABI, signer);
  const creditPolicy = new ethers.Contract(CREDIT_POLICY, CREDIT_POLICY_ABI, signer);
  const tranchePool = new ethers.Contract(TRANCHE_POOL, TRANCHE_POOL_ABI, signer);
  const usdc = new ethers.Contract(USDC, ERC20_ABI, signer);

  // Initialize Barretenberg
  console.log("Initializing Barretenberg...");
  const bb = await Barretenberg.new();
  
  // @ts-ignore
  const FrConstructor = Fr || bb.Fr;
  const toFr = (val: any) => new FrConstructor(BigInt(val));

  async function poseidonHash(inputs: any[]) {
    const frInputs = inputs.map(i => toFr(i));
    return await bb.poseidon2Hash(frInputs);
  }

  // --- Define Test Data ---
  // Get the current block timestamp from the chain (anvil-zksync has a low genesis timestamp)
  const latestBlock = await provider.getBlock("latest");
  const blockTimestamp = Number(latestBlock!.timestamp);
  console.log(`Current block timestamp: ${blockTimestamp}`);
  
  // Use the chain's block timestamp, not real-world Date.now()
  const timestamp = blockTimestamp;
  const loanId = Number(await loanEngine.getNextLoanId());
  const attestation_timestamp = timestamp;
  
  // Use policy version 2 (because full_deploy.sh created version 1 with wrong scope hash)
  let policyId = 2;
  
  console.log(`Creating loan ID: ${loanId}`);

  // Define policy and tier constants first (used for both policy setup and circuit)
  const policy = {
    min_revenue: 1000000,
    min_ebitda: 100000,
    min_net_worth: 250000,
    min_age: 730,
    max_defaults: 0,
    bankruptcy_excluded: true,
    max_debt_to_ebitda: 40000,
    min_interest_coverage: 15000,
    min_current_ratio: 12000,
    min_margin_bps: 1000,
    max_attestation_age: 90
  };

  const tier = {
    id: 1,
    min_revenue: 1000000,
    max_revenue: 10000000,
    min_ebitda: 100000,
    max_debt_to_ebitda: 40000,
    max_loan_to_ebitda: "1000000000000000000",
    interest_rate: 1200,
    origination_fee: 100,
    term: 365,
    active: true
  };

  // Compute the policy_version_hash (Poseidon2) that the circuit will output
  const policy_version_hash = await poseidonHash([
    policy.min_revenue, policy.min_ebitda, policy.min_net_worth, policy.min_age,
    policy.max_defaults, Number(policy.bankruptcy_excluded), policy.max_debt_to_ebitda,
    policy.min_interest_coverage, policy.min_current_ratio, policy.min_margin_bps,
    policy.max_attestation_age, tier.id, tier.min_revenue, tier.max_revenue,
    tier.min_ebitda, tier.max_debt_to_ebitda, tier.max_loan_to_ebitda,
    tier.interest_rate, tier.origination_fee, tier.term, Number(tier.active)
  ]);
  const policy_version_hash_bytes32 = "0x" + policy_version_hash.toString().slice(2).padStart(64, '0');
  console.log(`Policy version hash (Poseidon2): ${policy_version_hash_bytes32}`);

  // Check if policy exists and is frozen - policy setup is done via setup_policy2.sh or cast commands
  const policyExists = await creditPolicy.policyCreated(policyId);
  const isFrozen = policyExists ? await creditPolicy.isPolicyFrozen(policyId) : false;
  
  if (!isFrozen) {
    console.error(`❌ Policy ${policyId} is not frozen. Please run the policy setup first.`);
    console.error("   Use cast commands or setup_policy2.sh to create and freeze the policy.");
    process.exit(1);
  }
  
  console.log(`✅ Using frozen policy version ${policyId}`);

  // Verify the on-chain scope hash matches our computed hash
  const onChainScopeHash = await creditPolicy.policyScopeHash(policyId);
  console.log(`  On-chain scope hash: ${onChainScopeHash}`);
  console.log(`  Expected hash:       ${policy_version_hash_bytes32}`);
  if (onChainScopeHash.toLowerCase() !== policy_version_hash_bytes32.toLowerCase()) {
    console.error("❌ Scope hash mismatch! The policy was set up with a different scope hash.");
    process.exit(1);
  }
  console.log("  ✅ Scope hash matches!");

  // --- TranchePool is already set up by full_deploy.sh ---
  console.log("\nTranchePool already configured by deployment script");
  
  // Check pool state (0=OPEN, 1=COMMITED, 2=DEPLOYED)
  const poolState = await tranchePool.getPoolState();
  console.log(`  Current pool state: ${poolState} (expected: 2 = DEPLOYED)`);
  
  if (poolState !== 2n) {
    console.error("Error: Pool is not in DEPLOYED state. Run full_deploy.sh first.");
    process.exit(1);
  }
  
  console.log("  ✅ TranchePool ready!");

  // Borrower data
  const borrower_data = {
    revenue: 5000000,
    ebitda: 750000,
    net_worth: 1000000,
    age_days: 1095,
    defaults: 0,
    bankruptcy: false,
    debt_to_ebitda: 25000,
    interest_coverage: 20000,
    current_ratio: 15000,
    margin_bps: 1500,
    secret: "0x1234567890123456789012345678901234567890123456789012345678901234"
  };

  const loan = {
    principal: 500000,
    apr: 1200,
    fee: 100,
    term: 365
  };

  // Industry hash
  const industryValue = 123;
  const industry_hash = await poseidonHash([industryValue]);
  const industryBytes32 = "0x" + industry_hash.toString().slice(2).padStart(64, '0');

  // --- Generate Grumpkin Key ---
  console.log("Generating Grumpkin underwriter key...");
  const { privateKey: underwriterSk, publicKey: underwriterPk } =
    generateDeterministicKeypair("deterministic_seed");
  const pubKeyX = underwriterPk.x;
  const pubKeyY = underwriterPk.y;
  console.log(`  Generated Grumpkin keypair`);

  // --- Compute Hashes ---
  console.log("Computing hashes...");
  
  const borrower_commitment = await poseidonHash([
    borrower_data.secret,
    borrower_data.revenue,
    borrower_data.ebitda,
    borrower_data.net_worth,
    borrower_data.age_days
  ]);

  // policy_version_hash already computed earlier in the script

  const loan_hash = await poseidonHash([
    borrower_commitment, pubKeyX, pubKeyY, tier.id, loan.principal, loan.apr,
    loan.fee, loan.term, industry_hash, timestamp, loanId
  ]);

  const nullifier_hash = await poseidonHash([loanId, borrower_data.secret, loan.principal, attestation_timestamp]);

  // --- Build Circuit Inputs ---
  const inputs: any = {
    policy_version_hash: policy_version_hash.toString(),
    loan_hash: loan_hash.toString(),
    nullifierHash: nullifier_hash.toString(),
    borrower_commitment: borrower_commitment.toString(),
    underwriter_public_key_x: "0x" + pubKeyX.toString(16).padStart(64, "0"),
    underwriter_public_key_y: "0x" + pubKeyY.toString(16).padStart(64, "0"),
    tier_id: tier.id,
    loan_principal: loan.principal,
    loan_apr_bps: loan.apr,
    loan_origination_fee_bps: loan.fee,
    loan_term_days: loan.term,
    industry_hash: industry_hash.toString(),
    current_timestamp: timestamp,
    loanId: loanId,
    underwriter_sig_s_low: "0" as string,
    underwriter_sig_s_high: "0" as string,
    underwriter_sig_e: "0" as string,
    borrower_secret: borrower_data.secret,
    borrower_annual_revenue: borrower_data.revenue,
    borrower_ebitda: borrower_data.ebitda,
    borrower_tangible_net_worth: borrower_data.net_worth,
    borrower_business_age_days: borrower_data.age_days,
    borrower_defaults_last_36_months: borrower_data.defaults,
    borrower_has_bankruptcy: borrower_data.bankruptcy,
    borrower_debt_to_ebitda: borrower_data.debt_to_ebitda,
    borrower_interest_coverage: borrower_data.interest_coverage,
    borrower_current_ratio: borrower_data.current_ratio,
    borrower_ebitda_margin_bps: borrower_data.margin_bps,
    attestation_timestamp: attestation_timestamp,
    policy_min_annual_revenue: policy.min_revenue,
    policy_min_ebitda: policy.min_ebitda,
    policy_min_tangible_net_worth: policy.min_net_worth,
    policy_min_business_age_days: policy.min_age,
    policy_max_defaults_36_months: policy.max_defaults,
    policy_bankruptcy_excluded: policy.bankruptcy_excluded,
    policy_max_debt_to_ebitda: policy.max_debt_to_ebitda,
    policy_min_interest_coverage: policy.min_interest_coverage,
    policy_min_current_ratio: policy.min_current_ratio,
    policy_min_ebitda_margin_bps: policy.min_margin_bps,
    policy_max_attestation_age_days: policy.max_attestation_age,
    tier_min_revenue: tier.min_revenue,
    tier_max_revenue: tier.max_revenue,
    tier_min_ebitda: tier.min_ebitda,
    tier_max_debt_to_ebitda: tier.max_debt_to_ebitda,
    tier_max_loan_to_ebitda: tier.max_loan_to_ebitda,
    tier_interest_rate_bps: tier.interest_rate,
    tier_origination_fee_bps: tier.origination_fee,
    tier_term_days: tier.term,
    tier_active: tier.active
  };

  // --- Schnorr Sign Data ---
  console.log("Signing attestation data with Schnorr (Grumpkin)...");
  const data_to_sign_hash = await poseidonHash([
    borrower_data.revenue, borrower_data.ebitda, borrower_data.net_worth,
    borrower_data.age_days, borrower_data.defaults, Number(borrower_data.bankruptcy),
    borrower_data.debt_to_ebitda, borrower_data.interest_coverage,
    borrower_data.current_ratio, borrower_data.margin_bps,
    industry_hash, attestation_timestamp
  ]);

  // Poseidon2 hash wrapper for Schnorr signing
  async function poseidon2ForSchnorr(vals: bigint[]): Promise<bigint> {
    const frInputs = vals.map(i => toFr(i));
    const result = await bb.poseidon2Hash(frInputs);
    return BigInt(result.toString());
  }

  const msgHashBigint = BigInt(data_to_sign_hash.toString());
  const schnorrSig = await schnorrSign(underwriterSk, msgHashBigint, poseidon2ForSchnorr);

  inputs.underwriter_sig_s_low = toFr(schnorrSig.sLow).toString();
  inputs.underwriter_sig_s_high = toFr(schnorrSig.sHigh).toString();
  inputs.underwriter_sig_e = toFr(schnorrSig.e).toString();

  // --- Generate Proof ---
  console.log("\nGenerating ZK Proof...");
  const noir = new Noir(circuit);
  const honk = new UltraHonkBackend(circuit.bytecode, { threads: 1 });

  const { witness } = await noir.execute(inputs);
  const { proof, publicInputs } = await honk.generateProof(witness, { keccakZK: true });
  
  console.log(`  Proof size: ${proof.length} bytes`);
  console.log(`  Public inputs: ${publicInputs.length}`);

  // --- Verify off-chain first ---
  console.log("\nVerifying off-chain...");
  // @ts-ignore
  const validOffChain = await honk.verifyProof({ proof, publicInputs }, { keccakZK: true });
  if (!validOffChain) {
    console.error("❌ Off-chain verification FAILED");
    process.exit(1);
  }
  console.log("✅ Off-chain verification PASSED");

  // --- Prepare createLoan parameters ---
  const proofHex = "0x" + Buffer.from(proof).toString("hex");
  const publicInputsBytes32 = publicInputs.map((pi: string) => {
    const hex = pi.startsWith("0x") ? pi.slice(2) : pi;
    return "0x" + hex.padStart(64, "0");
  });

  const createLoanParams = {
    borrowerCommitment: "0x" + borrower_commitment.toString().slice(2).padStart(64, '0'),
    nullifierHash: "0x" + nullifier_hash.toString().slice(2).padStart(64, '0'),
    policyVersion: policyId,
    tierId: tier.id,
    principalIssued: loan.principal,
    aprBps: loan.apr,
    originationFeeBps: loan.fee,
    termDays: loan.term,
    industry: industryBytes32,
    underwriterKeyX: "0x" + pubKeyX.toString(16).padStart(64, '0'),
    underwriterKeyY: "0x" + pubKeyY.toString(16).padStart(64, '0'),
    proofTimestamp: timestamp
  };

  console.log("\n--- Creating Loan ---");
  console.log("Params:", JSON.stringify(createLoanParams, null, 2));

  // Authorize underwriter key if not already authorized
  const underwriterKeyXBytes = "0x" + pubKeyX.toString(16).padStart(64, '0');
  const underwriterKeyYBytes = "0x" + pubKeyY.toString(16).padStart(64, '0');
  const underwriterKeyHash = ethers.keccak256(ethers.solidityPacked(["bytes32", "bytes32"], [underwriterKeyXBytes, underwriterKeyYBytes]));
  
  console.log("\nAuthorizing underwriter...");
  const isAuthorized = await loanEngine.authorizedUnderwriters(underwriterKeyHash);
  if (!isAuthorized) {
    console.log("  Setting underwriter authorization...");
    const authTx = await loanEngine.setUnderwriterAuthorization(underwriterKeyXBytes, underwriterKeyYBytes, true);
    await authTx.wait();
    console.log("  ✅ Underwriter authorized");
  } else {
    console.log("  Underwriter already authorized");
  }

  // Whitelist off-ramping entity (the deployer/signer)
  const signerAddress = await signer.getAddress();
  console.log("\nWhitelisting off-ramping entity...");
  try {
    const whitelistTx = await loanEngine.setWhitelistedOffRampingEntity(signerAddress, true);
    await whitelistTx.wait();
    console.log("  ✅ Off-ramping entity whitelisted");
  } catch (e: any) {
    // May already be whitelisted
    console.log("  Off-ramping entity may already be whitelisted");
  }

  // ========================================
  // DIRECT VERIFIER TEST
  // ========================================
  console.log("\n" + "=".repeat(60));
  console.log("DIRECT VERIFIER TEST");
  console.log("=".repeat(60));
  
  const verifier = new ethers.Contract(VERIFIER, HONK_VERIFIER_ABI, signer);
  
  console.log(`\nVerifier address: ${VERIFIER}`);
  console.log(`Proof length: ${proofHex.length} bytes`);
  console.log(`Public inputs count: ${publicInputsBytes32.length}`);
  
  console.log("\nCalling verifier.verify() directly...");
  try {
    const isValid = await verifier.verify.staticCall(proofHex, publicInputsBytes32);
    console.log(`✅ Verifier returned: ${isValid}`);
  } catch (verifyError: any) {
    console.error("❌ Direct verifier call FAILED:");
    console.error(verifyError.message || verifyError);
    
    // Try to get more details
    try {
      const gasEstimate = await verifier.verify.estimateGas(proofHex, publicInputsBytes32);
      console.log(`Gas estimate would be: ${gasEstimate.toString()}`);
    } catch (gasError: any) {
      console.error("Gas estimation also failed:", gasError.message);
    }
  }

  console.log("\nSubmitting createLoan transaction...");
  try {
    // First try a static call to get a revert reason
    console.log("Testing with staticCall first...");
    try {
      await loanEngine.createLoan.staticCall(
        createLoanParams,
        proofHex,
        publicInputsBytes32
      );
      console.log("✅ staticCall passed!");
    } catch (staticError: any) {
      console.error("❌ staticCall failed with:", staticError.reason || staticError.message);
      // Try to decode the error
      if (staticError.data) {
        console.error("Error data:", staticError.data);
      }
    }
    
    // Get the current nonce from the network to avoid desync
    const currentNonce = await provider.getTransactionCount(signerAddress, "pending");
    console.log(`Using nonce: ${currentNonce}`);
    
    const tx = await loanEngine.createLoan(
      createLoanParams,
      proofHex,
      publicInputsBytes32,
      { gasLimit: 10000000, nonce: currentNonce }
    );
    
    console.log(`Transaction hash: ${tx.hash}`);
    const receipt = await tx.wait();
    console.log(`Transaction confirmed in block ${receipt.blockNumber}`);
    
    // Verify the loan was created
    const loanDetails = await loanEngine.getLoanDetails(loanId);
    console.log("\n✅ LOAN CREATED SUCCESSFULLY!");
    console.log(`  Loan ID: ${loanId}`);
    console.log(`  State: ${loanDetails.state}`);
    console.log(`  Principal: ${loanDetails.principalIssued}`);
    console.log(`  APR (bps): ${loanDetails.aprBps}`);
    
  } catch (e: any) {
    console.error("❌ Transaction failed:");
    console.error(e.message || e);
    process.exit(1);
  }

  console.log("\n" + "=".repeat(60));
  console.log("🎉 SUCCESS: ZK-proven loan created on-chain!");
  console.log("=".repeat(60));
}

main().catch(console.error);
