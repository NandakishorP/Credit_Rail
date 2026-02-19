/**
 * Generate test vectors for main() integration tests in Noir.
 * These vectors include all hashes + a valid Schnorr signature
 * so that main() can be called directly in Noir tests.
 */
import { Barretenberg, Fr } from "@aztec/bb.js";
import { schnorrSign, splitScalar } from "./grumpkin.js";

async function main() {
  const bb = await Barretenberg.new();
  const toFr = (val: any) => new Fr(BigInt(val));

  async function poseidonHash(inputs: any[]): Promise<Fr> {
    const frInputs = inputs.map((i) => toFr(i));
    return await bb.poseidon2Hash(frInputs);
  }

  async function poseidon2ForSchnorr(vals: bigint[]): Promise<bigint> {
    const frInputs = vals.map((i) => toFr(i));
    const result = await bb.poseidon2Hash(frInputs);
    return BigInt(result.toString());
  }

  // --- Fixed test inputs (matching test_policy_compliance_valid) ---
  const sk = BigInt(42);
  // PK = sk * G
  const { grumpkin } = await import("./grumpkin.js");
  const pkPoint = grumpkin.ProjectivePoint.BASE.multiply(sk).toAffine();
  const pk_x = pkPoint.x;
  const pk_y = pkPoint.y;

  const borrower_secret = BigInt(123);
  const borrower_annual_revenue = 5_000_000;
  const borrower_ebitda = 750_000;
  const borrower_tangible_net_worth = 1_000_000;
  const borrower_business_age_days = 1095;
  const borrower_defaults_last_36_months = 0;
  const borrower_has_bankruptcy = false;
  const borrower_debt_to_ebitda = 25000;
  const borrower_interest_coverage = 20000;
  const borrower_current_ratio = 15000;
  const borrower_ebitda_margin_bps = 1500;

  const policy_min_annual_revenue = 1_000_000;
  const policy_min_ebitda = 100_000;
  const policy_min_tangible_net_worth = 250_000;
  const policy_min_business_age_days = 730;
  const policy_max_defaults_36_months = 0;
  const policy_bankruptcy_excluded = true;
  const policy_max_debt_to_ebitda = 40000;
  const policy_min_interest_coverage = 15000;
  const policy_min_current_ratio = 12000;
  const policy_min_ebitda_margin_bps = 1000;
  const policy_max_attestation_age_days = 90;

  const tier_id = 1;
  const tier_min_revenue = 1_000_000;
  const tier_max_revenue = 10_000_000;
  const tier_min_ebitda = 100_000;
  const tier_max_debt_to_ebitda = 40000;
  const tier_max_loan_to_ebitda = BigInt("1000000000000000000");
  const tier_interest_rate_bps = 1200;
  const tier_origination_fee_bps = 100;
  const tier_term_days = 365;
  const tier_active = true;

  const loan_principal = 500_000;
  const loan_apr_bps = 1200;
  const loan_origination_fee_bps = 100;
  const loan_term_days = 365;

  const loanId = 1;
  const current_timestamp = 100000;
  const attestation_timestamp = 95000;
  const industry_hash_input = 123;

  // --- Compute all hashes ---
  const industry_hash = await poseidonHash([industry_hash_input]);
  const industry_hash_bn = BigInt(industry_hash.toString());

  const borrower_commitment = await poseidonHash([
    borrower_secret,
    borrower_annual_revenue,
    borrower_ebitda,
    borrower_tangible_net_worth,
    borrower_business_age_days,
  ]);
  const commitment_bn = BigInt(borrower_commitment.toString());

  const policy_version_hash = await poseidonHash([
    policy_min_annual_revenue,
    policy_min_ebitda,
    policy_min_tangible_net_worth,
    policy_min_business_age_days,
    policy_max_defaults_36_months,
    Number(policy_bankruptcy_excluded),
    policy_max_debt_to_ebitda,
    policy_min_interest_coverage,
    policy_min_current_ratio,
    policy_min_ebitda_margin_bps,
    policy_max_attestation_age_days,
    tier_id,
    tier_min_revenue,
    tier_max_revenue,
    tier_min_ebitda,
    tier_max_debt_to_ebitda,
    tier_max_loan_to_ebitda,
    tier_interest_rate_bps,
    tier_origination_fee_bps,
    tier_term_days,
    Number(tier_active),
  ]);
  const policy_hash_bn = BigInt(policy_version_hash.toString());

  const loan_hash = await poseidonHash([
    commitment_bn,
    pk_x,
    pk_y,
    tier_id,
    loan_principal,
    loan_apr_bps,
    loan_origination_fee_bps,
    loan_term_days,
    industry_hash_bn,
    current_timestamp,
    loanId,
  ]);
  const loan_hash_bn = BigInt(loan_hash.toString());

  const nullifier_hash = await poseidonHash([
    loanId,
    borrower_secret,
    loan_principal,
    attestation_timestamp,
  ]);
  const nullifier_hash_bn = BigInt(nullifier_hash.toString());

  // --- Schnorr signature ---
  const data_to_sign_hash = await poseidonHash([
    borrower_annual_revenue,
    borrower_ebitda,
    borrower_tangible_net_worth,
    borrower_business_age_days,
    borrower_defaults_last_36_months,
    Number(borrower_has_bankruptcy),
    borrower_debt_to_ebitda,
    borrower_interest_coverage,
    borrower_current_ratio,
    borrower_ebitda_margin_bps,
    industry_hash_bn,
    attestation_timestamp,
  ]);
  const data_hash_bn = BigInt(data_to_sign_hash.toString());

  const sig = await schnorrSign(sk, data_hash_bn, poseidon2ForSchnorr);

  // --- Print Noir test vector ---
  console.log("// ===== MAIN() INTEGRATION TEST VECTOR =====");
  console.log("// sk = 42, all other values match test_policy_compliance_valid");
  console.log("");
  console.log("// Public inputs");
  console.log(`let policy_version_hash: Field = ${policy_hash_bn};`);
  console.log(`let loan_hash: Field = ${loan_hash_bn};`);
  console.log(`let nullifierHash: Field = ${nullifier_hash_bn};`);
  console.log(`let borrower_commitment: Field = ${commitment_bn};`);
  console.log(`let underwriter_public_key_x: Field = ${pk_x};`);
  console.log(`let underwriter_public_key_y: Field = ${pk_y};`);
  console.log(`let tier_id: u8 = ${tier_id};`);
  console.log(`let loan_principal: u64 = ${loan_principal};`);
  console.log(`let loan_apr_bps: u64 = ${loan_apr_bps};`);
  console.log(`let loan_origination_fee_bps: u64 = ${loan_origination_fee_bps};`);
  console.log(`let loan_term_days: u64 = ${loan_term_days};`);
  console.log(`let industry_hash: Field = ${industry_hash_bn};`);
  console.log(`let current_timestamp: u64 = ${current_timestamp};`);
  console.log(`let loanId: u64 = ${loanId};`);
  console.log("");
  console.log("// Schnorr signature");
  console.log(`let underwriter_sig_s_low: Field = ${sig.sLow};`);
  console.log(`let underwriter_sig_s_high: Field = ${sig.sHigh};`);
  console.log(`let underwriter_sig_e: Field = ${sig.e};`);
  console.log("");
  console.log("// Private inputs");
  console.log(`let borrower_secret: Field = ${borrower_secret};`);
  console.log(`let borrower_annual_revenue: u64 = ${borrower_annual_revenue};`);
  console.log(`let borrower_ebitda: u64 = ${borrower_ebitda};`);
  console.log(`let borrower_tangible_net_worth: u64 = ${borrower_tangible_net_worth};`);
  console.log(`let borrower_business_age_days: u64 = ${borrower_business_age_days};`);
  console.log(`let borrower_defaults_last_36_months: u64 = ${borrower_defaults_last_36_months};`);
  console.log(`let borrower_has_bankruptcy: bool = ${borrower_has_bankruptcy};`);
  console.log(`let borrower_debt_to_ebitda: u64 = ${borrower_debt_to_ebitda};`);
  console.log(`let borrower_interest_coverage: u64 = ${borrower_interest_coverage};`);
  console.log(`let borrower_current_ratio: u64 = ${borrower_current_ratio};`);
  console.log(`let borrower_ebitda_margin_bps: u64 = ${borrower_ebitda_margin_bps};`);
  console.log(`let attestation_timestamp: u64 = ${attestation_timestamp};`);
  console.log("");
  console.log("// Policy constraints");
  console.log(`let policy_min_annual_revenue: u64 = ${policy_min_annual_revenue};`);
  console.log(`let policy_min_ebitda: u64 = ${policy_min_ebitda};`);
  console.log(`let policy_min_tangible_net_worth: u64 = ${policy_min_tangible_net_worth};`);
  console.log(`let policy_min_business_age_days: u64 = ${policy_min_business_age_days};`);
  console.log(`let policy_max_defaults_36_months: u64 = ${policy_max_defaults_36_months};`);
  console.log(`let policy_bankruptcy_excluded: bool = ${policy_bankruptcy_excluded};`);
  console.log(`let policy_max_debt_to_ebitda: u64 = ${policy_max_debt_to_ebitda};`);
  console.log(`let policy_min_interest_coverage: u64 = ${policy_min_interest_coverage};`);
  console.log(`let policy_min_current_ratio: u64 = ${policy_min_current_ratio};`);
  console.log(`let policy_min_ebitda_margin_bps: u64 = ${policy_min_ebitda_margin_bps};`);
  console.log(`let policy_max_attestation_age_days: u64 = ${policy_max_attestation_age_days};`);
  console.log("");
  console.log("// Tier constraints");
  console.log(`let tier_min_revenue: u64 = ${tier_min_revenue};`);
  console.log(`let tier_max_revenue: u64 = ${tier_max_revenue};`);
  console.log(`let tier_min_ebitda: u64 = ${tier_min_ebitda};`);
  console.log(`let tier_max_debt_to_ebitda: u64 = ${tier_max_debt_to_ebitda};`);
  console.log(`let tier_max_loan_to_ebitda: u64 = ${tier_max_loan_to_ebitda};`);
  console.log(`let tier_interest_rate_bps: u64 = ${tier_interest_rate_bps};`);
  console.log(`let tier_origination_fee_bps: u64 = ${tier_origination_fee_bps};`);
  console.log(`let tier_term_days: u64 = ${tier_term_days};`);
  console.log(`let tier_active: bool = ${tier_active};`);

  await bb.destroy();
}

main().catch(console.error);
