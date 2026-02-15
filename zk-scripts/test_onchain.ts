/**
 * Test ZK Proof On-Chain Verification
 * 
 * This script:
 * 1. Generates a ZK proof using the Noir circuit
 * 2. Verifies it off-chain using bb.js
 * 3. Verifies it on-chain using the deployed HonkVerifier on anvil-zksync
 */

import { Barretenberg, UltraHonkBackend, Fr } from "@aztec/bb.js";
import { Noir } from "@noir-lang/noir_js";
import { ethers } from "ethers";
import fs from "fs";
import path from "path";

// Configuration
const VERIFIER_ADDRESS = process.env.VERIFIER_ADDRESS || "0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe";
const RPC_URL = process.env.RPC_URL || "http://127.0.0.1:8546";

// Load circuit
const circuitPath = path.resolve(__dirname, "../circuits/target/circuits.json");
const circuit = JSON.parse(fs.readFileSync(circuitPath, "utf-8"));

// HonkVerifier ABI (minimal interface)
const VERIFIER_ABI = [
  "function verify(bytes calldata _proof, bytes32[] calldata _publicInputs) external view returns (bool)"
];

async function main() {
  console.log("=".repeat(60));
  console.log("ZK Proof On-Chain Integration Test");
  console.log("=".repeat(60));
  console.log(`Verifier Address: ${VERIFIER_ADDRESS}`);
  console.log(`RPC URL: ${RPC_URL}`);
  console.log("");

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
  const timestamp = Math.floor(Date.now() / 1000);
  const loanId = 1;
  const attestation_timestamp = timestamp;
  
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

  const loan = {
    principal: 500000,
    apr: 1200,
    fee: 100,
    term: 365
  };

  // --- Generate Key (needed for hashes) ---
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

  // --- Compute Hashes ---
  console.log("Computing hashes...");
  
  // Borrower commitment: hash(secret, revenue, ebitda, net_worth, age) - 5 inputs
  const borrower_commitment = await poseidonHash([
    borrower_data.secret,
    borrower_data.revenue,
    borrower_data.ebitda,
    borrower_data.net_worth,
    borrower_data.age_days
  ]);

  // Policy version hash - matches circuit's compute_policy_version_hash
  const policy_version_hash = await poseidonHash([
    policy.min_revenue, policy.min_ebitda, policy.min_net_worth, policy.min_age,
    policy.max_defaults, Number(policy.bankruptcy_excluded), policy.max_debt_to_ebitda,
    policy.min_interest_coverage, policy.min_current_ratio, policy.min_margin_bps,
    policy.max_attestation_age, tier.id, tier.min_revenue, tier.max_revenue,
    tier.min_ebitda, tier.max_debt_to_ebitda, tier.max_loan_to_ebitda,
    tier.interest_rate, tier.origination_fee, tier.term, Number(tier.active)
  ]);

  const industry_hash = await poseidonHash([123]);

  // Loan hash - matches circuit's compute_loan_hash with 11 inputs
  const loan_hash = await poseidonHash([
    borrower_commitment,
    pubKeyX,
    pubKeyY,
    tier.id,
    loan.principal,
    loan.apr,
    loan.fee,
    loan.term,
    industry_hash,
    timestamp,
    loanId
  ]);

  // Nullifier hash - matches circuit: hash(loanId, secret, principal, attestation_timestamp) - 4 inputs
  const nullifier_hash = await poseidonHash([loanId, borrower_data.secret, loan.principal, attestation_timestamp]);

  // --- Build Circuit Inputs ---
  const inputs: any = {
    // Public inputs
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
    
    // Private inputs
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
    
    // Policy constraints
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
    
    // Tier constraints
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
  // The underwriter signs the raw data (without borrower commitment)
  // Must match exactly: 12 inputs in order
  const data_to_sign_hash = await poseidonHash([
    borrower_data.revenue,           // borrower_annual_revenue
    borrower_data.ebitda,            // borrower_ebitda
    borrower_data.net_worth,         // borrower_tangible_net_worth
    borrower_data.age_days,          // borrower_business_age_days
    borrower_data.defaults,          // borrower_defaults_last_36_months
    Number(borrower_data.bankruptcy), // borrower_has_bankruptcy
    borrower_data.debt_to_ebitda,    // borrower_debt_to_ebitda
    borrower_data.interest_coverage,  // borrower_interest_coverage
    borrower_data.current_ratio,      // borrower_current_ratio
    borrower_data.margin_bps,         // borrower_ebitda_margin_bps
    industry_hash,                    // industry_hash
    attestation_timestamp             // attestation_timestamp
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
  console.log("\n--- Proof Generation ---");
  const noir = new Noir(circuit);
  const honk = new UltraHonkBackend(circuit.bytecode, { threads: 1 });

  console.log("Generating witness...");
  const { witness } = await noir.execute(inputs);

  console.log("Generating proof...");
  const { proof, publicInputs } = await honk.generateProof(witness, { keccakZK: true });
  
  console.log(`  Proof size: ${proof.length} bytes`);
  console.log(`  Public inputs: ${publicInputs.length}`);

  // --- Off-Chain Verification ---
  console.log("\n--- Off-Chain Verification ---");
  // @ts-ignore
  const validOffChain = await honk.verifyProof({ proof, publicInputs }, { keccakZK: true });
  if (!validOffChain) {
    console.error("❌ Off-chain verification FAILED");
    process.exit(1);
  }
  console.log("✅ Off-chain verification PASSED");

  // --- On-Chain Verification ---
  console.log("\n--- On-Chain Verification ---");
  
  const provider = new ethers.JsonRpcProvider(RPC_URL);
  const verifier = new ethers.Contract(VERIFIER_ADDRESS, VERIFIER_ABI, provider);

  // Convert proof to bytes
  const proofHex = "0x" + Buffer.from(proof).toString("hex");
  
  // Convert public inputs to bytes32[]
  const publicInputsBytes32 = publicInputs.map((pi: string) => {
    // Ensure it's 32 bytes (pad left with zeros if needed)
    const hex = pi.startsWith("0x") ? pi.slice(2) : pi;
    return "0x" + hex.padStart(64, "0");
  });

  console.log(`  Calling verifier at ${VERIFIER_ADDRESS}...`);
  console.log(`  Proof (first 100 chars): ${proofHex.slice(0, 100)}...`);
  console.log(`  Public inputs count: ${publicInputsBytes32.length}`);

  try {
    const validOnChain = await verifier.verify(proofHex, publicInputsBytes32);
    
    if (validOnChain) {
      console.log("✅ ON-CHAIN VERIFICATION PASSED!");
      console.log("\n" + "=".repeat(60));
      console.log("🎉 SUCCESS: ZK Proof verified both off-chain and on-chain!");
      console.log("=".repeat(60));
    } else {
      console.error("❌ On-chain verification returned false");
      process.exit(1);
    }
  } catch (e: any) {
    console.error("❌ On-chain verification failed with error:");
    console.error(e.message || e);
    process.exit(1);
  }
}

main().catch(console.error);
