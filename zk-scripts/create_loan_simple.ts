/**
 * Create Loan with ZK Proof (Simple Version)
 * 
 * Prerequisites:
 * - All contracts deployed to anvil-zksync
 * - CreditPolicy v1 frozen
 * - TranchePool in COMMITED state with funds
 * 
 * Run the full_deploy.sh script first to set up everything.
 */

import { Barretenberg, UltraHonkBackend, Fr } from "@aztec/bb.js";
import { Noir } from "@noir-lang/noir_js";
import { ethers } from "ethers";
import fs from "fs";
import path from "path";

// Configuration - these match the deployed contracts
const RPC_URL = "http://127.0.0.1:8546";
const PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
const LOAN_ENGINE = "0x46F2Dc79c3D6E9DDb3F263FF3B6331d4938f198b";  // With REAL Poseidon2

// Load circuit
const circuitPath = path.resolve(__dirname, "../circuits/target/circuits.json");
const circuit = JSON.parse(fs.readFileSync(circuitPath, "utf-8"));

// LoanEngine ABI (partial)
const LOAN_ENGINE_ABI = [
  `function createLoan(
    (bytes32 borrowerCommitment, bytes32 nullifierHash, uint256 policyVersion, uint8 tierId, uint256 principalIssued, uint256 aprBps, uint256 originationFeeBps, uint256 termDays, bytes32 industry, bytes32 underwriterKeyX, bytes32 underwriterKeyY, uint256 proofTimestamp) params,
    bytes calldata proofData,
    bytes32[] calldata publicInputs
  ) external`,
  "function getNextLoanId() external view returns (uint256)",
  "function getLoanDetails(uint256 loanId) external view returns (tuple(uint8 state, bytes32 borrowerCommitment, uint256 policyVersion, uint8 tierId, uint256 principalIssued, uint256 aprBps, uint256 originationFeeBps, uint256 termDays, bytes32 industry, uint256 interestEarned, uint256 principalRepaid, bytes32 nullifierHash, uint256 createdAt, bytes32 underwriterKeyX, bytes32 underwriterKeyY))",
  "function setUnderwriterAuthorization(bytes32 keyX, bytes32 keyY, bool isAuthorized) external",
  "function authorizedUnderwriters(bytes32 keyHash) external view returns (bool)"
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

  // Get the current block timestamp from the chain
  const latestBlock = await provider.getBlock('latest');
  const chainTimestamp = latestBlock ? Number(latestBlock.timestamp) : Math.floor(Date.now() / 1000);
  console.log(`Chain timestamp: ${chainTimestamp} (block ${latestBlock?.number})`);

  // --- Define Test Data ---
  const timestamp = chainTimestamp;  // Use chain timestamp, not real world time
  const loanId = Number(await loanEngine.getNextLoanId());
  const attestation_timestamp = timestamp;
  const policyId = 2;  // Policy version 2 with correct Poseidon hash
  const tierId = 1;
  
  console.log(`Creating loan ID: ${loanId}`);

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
    id: tierId,
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

  // --- Generate Key ---
  console.log("Generating underwriter key...");
  const BN254_MODULUS = BigInt("21888242871839275222246405745257275088548364400416034343698204186575808495617");
  
  let wallet: ethers.Wallet;
  let pubKeyX: bigint;
  let pubKeyY: bigint;
  let counter = 0;
  
  while (true) {
    counter++;
    const seed = ethers.keccak256(ethers.toUtf8Bytes(`deterministic_seed_${counter}`));
    wallet = new ethers.Wallet(seed);
    const uncompressed = wallet.signingKey.publicKey;
    pubKeyX = BigInt("0x" + uncompressed.slice(4, 68));
    pubKeyY = BigInt("0x" + uncompressed.slice(68, 132));
    if (pubKeyX < BN254_MODULUS && pubKeyY < BN254_MODULUS) break;
  }
  
  console.log(`  Key found after ${counter} iterations`);

  // Authorize the underwriter key
  const keyXBytes32 = "0x" + pubKeyX.toString(16).padStart(64, '0');
  const keyYBytes32 = "0x" + pubKeyY.toString(16).padStart(64, '0');
  const keyHash = ethers.keccak256(ethers.solidityPacked(['bytes32', 'bytes32'], [keyXBytes32, keyYBytes32]));
  const isAuthorized = await loanEngine.authorizedUnderwriters(keyHash);
  if (!isAuthorized) {
    console.log("  Authorizing underwriter key...");
    const tx = await loanEngine.setUnderwriterAuthorization(keyXBytes32, keyYBytes32, true);
    await tx.wait();
    console.log("  ✅ Underwriter authorized");
  }

  // --- Compute Hashes ---
  console.log("Computing hashes...");
  
  const borrower_commitment = await poseidonHash([
    borrower_data.secret,
    borrower_data.revenue,
    borrower_data.ebitda,
    borrower_data.net_worth,
    borrower_data.age_days
  ]);

  const policy_version_hash = await poseidonHash([
    policy.min_revenue, policy.min_ebitda, policy.min_net_worth, policy.min_age,
    policy.max_defaults, Number(policy.bankruptcy_excluded), policy.max_debt_to_ebitda,
    policy.min_interest_coverage, policy.min_current_ratio, policy.min_margin_bps,
    policy.max_attestation_age, tier.id, tier.min_revenue, tier.max_revenue,
    tier.min_ebitda, tier.max_debt_to_ebitda, tier.max_loan_to_ebitda,
    tier.interest_rate, tier.origination_fee, tier.term, Number(tier.active)
  ]);

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
    underwriter_signature: [] as number[],
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

  // --- Sign Data ---
  console.log("Signing attestation data...");
  const data_to_sign_hash = await poseidonHash([
    borrower_data.revenue, borrower_data.ebitda, borrower_data.net_worth,
    borrower_data.age_days, borrower_data.defaults, Number(borrower_data.bankruptcy),
    borrower_data.debt_to_ebitda, borrower_data.interest_coverage,
    borrower_data.current_ratio, borrower_data.margin_bps,
    industry_hash, attestation_timestamp
  ]);

  const hashHex = data_to_sign_hash.toString();
  const msgHashBytes = ethers.getBytes(hashHex);
  const paddedMsgHash = new Uint8Array(32);
  paddedMsgHash.set(msgHashBytes, 32 - msgHashBytes.length);

  const sig = wallet.signingKey.sign(paddedMsgHash);
  const sigR = ethers.getBytes(sig.r);
  const sigS = ethers.getBytes(sig.s);
  const signature = new Uint8Array(64);
  signature.set(sigR, 0);
  signature.set(sigS, 32);
  inputs.underwriter_signature = Array.from(signature);

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
  console.log("Params:", JSON.stringify({
    ...createLoanParams,
    policyVersion: createLoanParams.policyVersion.toString(),
    tierId: createLoanParams.tierId.toString(),
    principalIssued: createLoanParams.principalIssued.toString(),
    aprBps: createLoanParams.aprBps.toString(),
    originationFeeBps: createLoanParams.originationFeeBps.toString(),
    termDays: createLoanParams.termDays.toString(),
    proofTimestamp: createLoanParams.proofTimestamp.toString()
  }, null, 2));

  // Debug: Print public inputs
  console.log("\nPublic Inputs for verification:");
  console.log(`  [0] policy_version_hash: ${publicInputsBytes32[0]}`);
  console.log(`  [1] loan_hash:           ${publicInputsBytes32[1]}`);
  console.log(`  [2] nullifier_hash:      ${publicInputsBytes32[2]}`);
  
  // Debug: Check on-chain policyScopeHash
  const CREDIT_POLICY_ABI = ["function policyScopeHash(uint256) view returns (bytes32)"];
  const creditPolicyAddress = "0x22D151A1313d9B517Fa437F1F5B3744E636D8790";
  const creditPolicy = new ethers.Contract(creditPolicyAddress, CREDIT_POLICY_ABI, provider);
  const onChainPolicyHash = await creditPolicy.policyScopeHash(policyId);
  console.log(`\nOn-chain policyScopeHash(${policyId}): ${onChainPolicyHash}`);
  console.log(`Match: ${publicInputsBytes32[0].toLowerCase() === onChainPolicyHash.toLowerCase()}`);

  // Debug: Test the Poseidon2 hash computation on-chain
  console.log("\n--- Debug: Computing loan_hash on-chain ---");
  const POSEIDON2_ABI = ["function hash(uint256[] calldata inputs) external view returns (bytes32)"];
  const poseidon2Address = "0x1B69c60F3ac12BC305C96D927573102f6617eb16";
  const poseidon2Contract = new ethers.Contract(poseidon2Address, POSEIDON2_ABI, provider);
  
  // Loan hash inputs: [borrower_commitment, loanId, principal, apr, fee, term, timestamp, industry]
  const loanHashInputs = [
    BigInt(borrower_commitment.toString()),
    BigInt(loanId),
    BigInt(loan.principal),
    BigInt(loan.apr),
    BigInt(loan.fee),
    BigInt(loan.term),
    BigInt(timestamp),
    BigInt(industryBytes32)
  ];
  console.log("Loan hash inputs:");
  loanHashInputs.forEach((inp, i) => console.log(`  [${i}]: ${inp.toString(16).padStart(64, '0')}`));
  
  try {
    const onChainLoanHash = await poseidon2Contract.hash(loanHashInputs);
    console.log(`On-chain Poseidon2 loan_hash: ${onChainLoanHash}`);
    console.log(`Off-chain loan_hash:          ${publicInputsBytes32[1]}`);
    console.log(`Match: ${onChainLoanHash.toLowerCase() === publicInputsBytes32[1].toLowerCase()}`);
  } catch (e: any) {
    console.log("Failed to compute on-chain hash:", e.message);
  }

  // Try static call first to get revert reason
  console.log("\n--- Attempting staticCall to get revert reason ---");
  try {
    await loanEngine.createLoan.staticCall(
      createLoanParams,
      proofHex,
      publicInputsBytes32
    );
    console.log("Static call succeeded - transaction should work");
  } catch (e: any) {
    console.log("Static call failed with:", e.reason || e.message);
    if (e.data) console.log("Revert data:", e.data);
  }

  try {
    const tx = await loanEngine.createLoan(
      createLoanParams,
      proofHex,
      publicInputsBytes32,
      { gasLimit: 30000000 }
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
    if (e.data) {
      console.error("Error data:", e.data);
    }
    process.exit(1);
  }

  console.log("\n" + "=".repeat(60));
  console.log("🎉 SUCCESS: ZK-proven loan created on-chain!");
  console.log("=".repeat(60));
}

main().catch(console.error);
