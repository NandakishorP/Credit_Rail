
import { Barretenberg, UltraHonkBackend, Fr } from "@aztec/bb.js";
import { Noir } from "@noir-lang/noir_js";
import { ethers } from "ethers";
import fs from "fs";
import path from "path";
import { generateDeterministicKeypair, schnorrSign, toHex32 } from "./grumpkin";

// Load circuit
const circuitPath = path.resolve(__dirname, "../circuits/target/circuits.json");
const circuit = JSON.parse(fs.readFileSync(circuitPath, "utf-8"));

async function main() {
  console.log("Initializing Barretenberg...");
  const bb = await Barretenberg.new();
  
  // Helper to create Fr
  // @ts-ignore
  const FrConstructor = Fr || bb.Fr;
  const toFr = (val: any) => new FrConstructor(BigInt(val));

  // Helper for Poseidon Hashing
  // Matches noir: poseidon2::Poseidon2::hash(inputs)
  async function poseidonHash(inputs: any[]) {
    const frInputs = inputs.map(i => toFr(i));
    return await bb.poseidon2Hash(frInputs);
  }

  // --- 1. Define Data Values (matching test_policy_compliance_valid) ---
  const timestamp = Math.floor(Date.now() / 1000);
  const loanId = 1;
  const attestation_timestamp = timestamp;
  
  // Borrower Data
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

  // Policy Constraints
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

  // Tier Constraints
  const tier = {
    id: 1,
    min_revenue: 1000000,
    max_revenue: 10000000,
    min_ebitda: 100000,
    max_debt_to_ebitda: 40000,
    max_loan_to_ebitda: "1000000000000000000", // 1e18
    interest_rate: 1200,
    origination_fee: 100,
    term: 365,
    active: true
  };

  // Loan Request
  const loan = {
    principal: 500000,
    apr: 1200,
    fee: 100,
    term: 365
  };

  // Underwriter - will be set by Grumpkin keypair generation below
  let pubKeyX: bigint;
  let pubKeyY: bigint;
  let underwriterSk: bigint;

  // --- 2. Compute Hashes ---

  // Borrower Commitment: Hash(secret, revenue, ebitda, net_worth, age)
  // verify_borrower_commitment in main.nr
  const borrower_commitment = await poseidonHash([
    borrower_data.secret,
    borrower_data.revenue,
    borrower_data.ebitda,
    borrower_data.net_worth,
    borrower_data.age_days
  ]);

  // Policy Version Hash: Hash(all policy + tier fields)
  // compute_policy_hash in main.nr
  const policy_version_hash = await poseidonHash([
    policy.min_revenue,
    policy.min_ebitda,
    policy.min_net_worth,
    policy.min_age,
    policy.max_defaults,
    Number(policy.bankruptcy_excluded), // bool -> field (0/1)
    policy.max_debt_to_ebitda,
    policy.min_interest_coverage,
    policy.min_current_ratio,
    policy.min_margin_bps,
    policy.max_attestation_age,
    
    tier.id,
    tier.min_revenue,
    tier.max_revenue,
    tier.min_ebitda,
    tier.max_debt_to_ebitda,
    tier.max_loan_to_ebitda,
    tier.interest_rate,
    tier.origination_fee,
    tier.term,
    Number(tier.active)
  ]);

  // Industry Hash (just a placeholder for now, verified on-chain)
  const industry_hash = await poseidonHash([123]); 

  // --- Generate Grumpkin Key (needed for hashes) ---
  console.log("Generating Grumpkin underwriter key...");
  const keypair = generateDeterministicKeypair("deterministic_seed");
  underwriterSk = keypair.privateKey;
  pubKeyX = keypair.publicKey.x;
  pubKeyY = keypair.publicKey.y;
  console.log(`  Generated Grumpkin keypair`);

  // Loan Hash: Hash(commitment, pk, tier, loan details, industry, time, loanId)
  // compute_loan_hash in main.nr
  // Inputs: commitment, pk_x, pk_y, tier_id, principal, apr, fee, term, industry, time, loanId
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

  // Nullifier Hash: Hash(loanId, secret, principal, attestation_time)
  // main.nr line 128
  const nullifierHash = await poseidonHash([
    loanId,
    borrower_data.secret,
    loan.principal,
    attestation_timestamp
  ]);

  // --- 3. Construct Input Object ---
  
  console.log("Constructing Inputs...");
  const inputs = {
    // Public Inputs
    policy_version_hash: policy_version_hash.toString(),
    loan_hash: loan_hash.toString(),
    nullifierHash: nullifierHash.toString(),
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

    // Private Inputs
    underwriter_sig_s_low: "0" as string,
    underwriter_sig_s_high: "0" as string,
    underwriter_sig_e: "0" as string,
    borrower_secret: toFr(borrower_data.secret).toString(),
    
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
    inputs.borrower_annual_revenue,
    inputs.borrower_ebitda,
    inputs.borrower_tangible_net_worth,
    inputs.borrower_business_age_days,
    inputs.borrower_defaults_last_36_months,
    Number(inputs.borrower_has_bankruptcy),
    inputs.borrower_debt_to_ebitda,
    inputs.borrower_interest_coverage,
    inputs.borrower_current_ratio,
    inputs.borrower_ebitda_margin_bps,
    industry_hash,
    attestation_timestamp
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

    // --- Execution ---
  try {
    const noir = new Noir(circuit);
    const honk = new UltraHonkBackend(circuit.bytecode, { threads: 1 });

    console.log("Generating Witness...");
    const { witness } = await noir.execute(inputs);

    console.log("Generating Proof...");
    const { proof, publicInputs } = await honk.generateProof(witness, { keccakZK: true });
    
    console.log("Proof Length:", proof.length);
    console.log("Public Inputs Length:", publicInputs.length);
    console.log("Public Inputs:", publicInputs);

    console.log("Verifying Off-Chain...");
    // @ts-ignore
    const valid = await honk.verifyProof({ proof, publicInputs }, { keccakZK: true });
    if (!valid) throw new Error("Off-chain verification failed");
    console.log("✅ Off-chain verification passed!");

    // Setup for On-Chain (Mock) - Ready for deployment integration
    if (process.env.VERIFIER_ADDRESS) {
       console.log("Proceeding to on-chain verification...");
       // Note: To verify on-chain, ensure to pass the full public inputs array
       // logic would go here using ethers
    }

  } catch(e) {
    console.error("❌ Verification Failed:", e);
    process.exit(1);
  }
}

main();
