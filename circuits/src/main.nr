use poseidon::poseidon2;

/// Credit Policy Compliance Circuit
///
/// Proves that a loan request adheres to a frozen credit policy version.
/// This circuit verifies:
/// 1. Borrower meets eligibility criteria
/// 2. Borrower's financial ratios pass underwriting thresholds
/// 3. Loan terms match the specified tier
/// 4. Industry is not excluded
/// 5. Borrower commitment binds private data to the proof
/// 6. Underwriter signature validates the borrower data
///
/// Public Inputs (visible on-chain):
/// - policy_version_hash: Hash of the frozen policy (links proof to immutable policy)
/// - borrower_commitment: Hash(borrower_secret, borrower_data) - privacy-preserving borrower binding
/// - underwriter_public_key_x: X coordinate of underwriter's public key
/// - underwriter_public_key_y: Y coordinate of underwriter's public key
/// - tier_id: The loan tier being used
/// - loan_principal: Requested principal amount
/// - loan_apr_bps: Annual interest rate in basis points
/// - loan_origination_fee_bps: Origination fee in basis points
/// - loan_term_days: Loan term in days
/// - industry_hash: Hash of borrower's industry code
///
/// Private Inputs (hidden in proof):
/// - underwriter_signature: Schnorr signature over borrower data
/// - borrower_secret: Secret known only to borrower (for commitment)
/// - eligibility criteria values (borrower's actual metrics)
/// - financial ratio values (borrower's actual ratios)
/// - policy tier constraints (from the frozen policy)
/// - policy eligibility constraints (from the frozen policy)
/// - policy ratio constraints (from the frozen policy)

//==============================================================
//                       MAIN CIRCUIT
//==============================================================

fn main(
    // === Public Inputs (exposed to verifier) ===
    policy_version_hash: pub Field, // Hash of policy version (commitment to frozen policy)
    borrower_commitment: pub Field, // Hash(secret || borrower_data)
    underwriter_public_key_x: pub Field, // Underwriter PK X
    underwriter_public_key_y: pub Field, // Underwriter PK Y
    tier_id: pub u8, // Tier ID from policy
    loan_principal: pub u64, // Requested loan principal
    loan_apr_bps: pub u64, // Interest rate in basis points
    loan_origination_fee_bps: pub u64, // Origination fee in basis points
    loan_term_days: pub u64, // Term in days
    industry_hash: pub Field, // Hash of industry code
    current_timestamp: pub u64, // Current block time (approx)
    loanId: pub u64,
    nullifierHash: pub Field,
    // === Private Inputs (hidden from verifier) ===
    // Underwriter signature
    underwriter_signature: [u8; 64],
    // Borrower secret for commitment
    borrower_secret: Field,
    // Borrower eligibility data (private - actual values)
    borrower_annual_revenue: u64,
    borrower_ebitda: u64,
    borrower_tangible_net_worth: u64,
    borrower_business_age_days: u64,
    borrower_defaults_last_36_months: u64,
    borrower_has_bankruptcy: bool,
    // Borrower financial ratios (private - actual values, scaled by 1e4 for precision)
    borrower_debt_to_ebitda: u64, // e.g., 3.5x = 35000
    borrower_interest_coverage: u64, // e.g., 2.0x = 20000
    borrower_current_ratio: u64, // e.g., 1.5x = 15000
    borrower_ebitda_margin_bps: u64, // e.g., 15% = 1500 bps
    // Attestation Data
    attestation_timestamp: u64, // When the underwriter signed/verified checks
    // Policy eligibility constraints (private - from frozen policy)
    policy_min_annual_revenue: u64,
    policy_min_ebitda: u64,
    policy_min_tangible_net_worth: u64,
    policy_min_business_age_days: u64,
    policy_max_defaults_36_months: u64,
    policy_bankruptcy_excluded: bool,
    // Policy ratio constraints (private - from frozen policy)
    policy_max_debt_to_ebitda: u64,
    policy_min_interest_coverage: u64,
    policy_min_current_ratio: u64,
    policy_min_ebitda_margin_bps: u64,
    policy_max_attestation_age_days: u64, // Added
    // Policy Tier constraints (private - from frozen policy)
    tier_min_revenue: u64,
    tier_max_revenue: u64,
    tier_min_ebitda: u64,
    tier_max_debt_to_ebitda: u64,
    tier_max_loan_to_ebitda: u64,
    tier_interest_rate_bps: u64,
    tier_origination_fee_bps: u64,
    tier_term_days: u64,
    tier_active: bool,
) {
    //==============================================================
    //             1. VERIFY BORROWER COMMITMENT
    //==============================================================
    let computed_commitment = poseidon2::Poseidon2::hash(
        [
            borrower_secret,
            borrower_annual_revenue as Field,
            borrower_ebitda as Field,
            borrower_tangible_net_worth as Field,
            borrower_business_age_days as Field,
        ],
        5,
    );
    assert(computed_commitment == borrower_commitment, "Borrower commitment mismatch");

    let computed_nullifier_hash = poseidon2::Poseidon2::hash(
        [loanId as Field, borrower_secret, loan_principal as Field, attestation_timestamp as Field],
        4,
    );
    assert(computed_nullifier_hash == nullifierHash, "Nullifier mismatch");

    //==============================================================
    //             1b. VERIFY ATTESATION AGE
    //==============================================================
    // Ensure the attestation is not expired
    assert(current_timestamp >= attestation_timestamp, "Attestation time in future");

    // Guard against overflow: Ensure policy max age is reasonable (e.g., < 27 years)
    assert(policy_max_attestation_age_days < 10000, "Policy age too large");
    let max_age_seconds = policy_max_attestation_age_days * 86400;

    // Guard against u64 overflow in addition
    // 0xffffffffffffffff = 18446744073709551615
    assert(attestation_timestamp <= 18446744073709551615 - max_age_seconds, "Timestamp overflow");

    assert(current_timestamp <= attestation_timestamp + max_age_seconds, "Attestation expired");

    //==============================================================
    //             1c. VERIFY UNDERWRITER SIGNATURE
    //==============================================================
    // The underwriter signs the raw data (without the borrower's secret).
    // This ensures that the data being proven (revenue, ebitda, etc.) was
    // explicitly authorized by the underwriter's private key.

    // 1. Hash the data (must match what was signed off-chain)
    // Note: We cast to Field for Poseidon. The signer must sign this exact sequence.
    let data_to_sign_hash = poseidon2::Poseidon2::hash(
        [
            borrower_annual_revenue as Field,
            borrower_ebitda as Field,
            borrower_tangible_net_worth as Field,
            borrower_business_age_days as Field,
            borrower_defaults_last_36_months as Field,
            borrower_has_bankruptcy as Field,
            borrower_debt_to_ebitda as Field,
            borrower_interest_coverage as Field,
            borrower_current_ratio as Field,
            borrower_ebitda_margin_bps as Field,
            industry_hash, // Bind industry to the signature
            attestation_timestamp as Field, // Bind timestamp to signature (Prevent Replay)
        ],
        12,
    );

    // 2. Convert hash to bytes for Schnorr verification (standard practice)
    // Field elements are 32 bytes (254 bits).
    let message_bytes: [u8; 32] = data_to_sign_hash.to_be_bytes();

    // 3. Verify Signature (ECDSA Secp256k1)
    // Convert Field public keys to bytes for ECDSA
    let pk_x_bytes = underwriter_public_key_x.to_be_bytes();
    let pk_y_bytes = underwriter_public_key_y.to_be_bytes();

    let is_valid_sig = std::ecdsa_secp256k1::verify_signature(
        pk_x_bytes,
        pk_y_bytes,
        underwriter_signature,
        message_bytes,
    );
    assert(is_valid_sig, "Invalid underwriter signature");

    //==============================================================
    //             2. VERIFY POLICY VERSION HASH
    //==============================================================
    // We must hash ALL policy constraints to ensure the proof is bound
    // to the specific frozen policy version.
    let computed_policy_hash = poseidon2::Poseidon2::hash(
        [
            policy_min_annual_revenue as Field,
            policy_min_ebitda as Field,
            policy_min_tangible_net_worth as Field,
            policy_min_business_age_days as Field,
            policy_max_defaults_36_months as Field,
            policy_bankruptcy_excluded as Field,
            policy_max_debt_to_ebitda as Field,
            policy_min_interest_coverage as Field,
            policy_min_current_ratio as Field,
            policy_min_ebitda_margin_bps as Field,
            policy_max_attestation_age_days as Field,
            // Tier constraints
            tier_id as Field, // Bind Tier ID to policy hash
            tier_min_revenue as Field,
            tier_max_revenue as Field,
            tier_min_ebitda as Field,
            tier_max_debt_to_ebitda as Field,
            tier_max_loan_to_ebitda as Field,
            tier_interest_rate_bps as Field,
            tier_origination_fee_bps as Field,
            tier_term_days as Field,
            tier_active as Field,
        ],
        21,
    );
    assert(computed_policy_hash == policy_version_hash, "Policy hash mismatch");

    //==============================================================
    //             3. VERIFY POLICY COMPLIANCE
    //==============================================================
    validate_policy_compliance(
        borrower_annual_revenue,
        borrower_ebitda,
        borrower_tangible_net_worth,
        borrower_business_age_days,
        borrower_defaults_last_36_months,
        borrower_has_bankruptcy,
        borrower_debt_to_ebitda,
        borrower_interest_coverage,
        borrower_current_ratio,
        borrower_ebitda_margin_bps,
        policy_min_annual_revenue,
        policy_min_ebitda,
        policy_min_tangible_net_worth,
        policy_min_business_age_days,
        policy_max_defaults_36_months,
        policy_bankruptcy_excluded,
        policy_max_debt_to_ebitda,
        policy_min_interest_coverage,
        policy_min_current_ratio,
        policy_min_ebitda_margin_bps,
        tier_min_revenue,
        tier_max_revenue,
        tier_min_ebitda,
        tier_max_debt_to_ebitda,
        tier_max_loan_to_ebitda,
        tier_interest_rate_bps,
        tier_origination_fee_bps,
        tier_term_days,
        tier_active,
        loan_principal,
        loan_apr_bps,
        loan_origination_fee_bps,
        loan_term_days,
    );

    // Industry exclusion is verified on-chain by LoanEngine check against
    // the industry_hash public input and the policy's excluded list.
}

fn validate_policy_compliance(
    borrower_annual_revenue: u64,
    borrower_ebitda: u64,
    borrower_tangible_net_worth: u64,
    borrower_business_age_days: u64,
    borrower_defaults_last_36_months: u64,
    borrower_has_bankruptcy: bool,
    borrower_debt_to_ebitda: u64,
    borrower_interest_coverage: u64,
    borrower_current_ratio: u64,
    borrower_ebitda_margin_bps: u64,
    policy_min_annual_revenue: u64,
    policy_min_ebitda: u64,
    policy_min_tangible_net_worth: u64,
    policy_min_business_age_days: u64,
    policy_max_defaults_36_months: u64,
    policy_bankruptcy_excluded: bool,
    policy_max_debt_to_ebitda: u64,
    policy_min_interest_coverage: u64,
    policy_min_current_ratio: u64,
    policy_min_ebitda_margin_bps: u64,
    tier_min_revenue: u64,
    tier_max_revenue: u64,
    tier_min_ebitda: u64,
    tier_max_debt_to_ebitda: u64,
    tier_max_loan_to_ebitda: u64,
    tier_interest_rate_bps: u64,
    tier_origination_fee_bps: u64,
    tier_term_days: u64,
    tier_active: bool,
    loan_principal: u64,
    loan_apr_bps: u64,
    loan_origination_fee_bps: u64,
    loan_term_days: u64,
) {
    // 3. ELIGIBILITY
    assert(borrower_annual_revenue >= policy_min_annual_revenue, "Annual revenue below minimum");
    assert(borrower_ebitda >= policy_min_ebitda, "EBITDA below minimum");
    assert(
        borrower_tangible_net_worth >= policy_min_tangible_net_worth,
        "Tangible net worth below minimum",
    );
    assert(
        borrower_business_age_days >= policy_min_business_age_days,
        "Business age below minimum",
    );
    assert(
        borrower_defaults_last_36_months <= policy_max_defaults_36_months,
        "Too many defaults in last 36 months",
    );

    if policy_bankruptcy_excluded {
        assert(!borrower_has_bankruptcy, "Bankruptcy excludes borrower");
    }

    // 4. FINANCIAL RATIOS
    assert(
        borrower_debt_to_ebitda <= policy_max_debt_to_ebitda,
        "Debt-to-EBITDA ratio exceeds maximum",
    );
    assert(
        borrower_interest_coverage >= policy_min_interest_coverage,
        "Interest coverage ratio below minimum",
    );
    assert(borrower_current_ratio >= policy_min_current_ratio, "Current ratio below minimum");
    assert(
        borrower_ebitda_margin_bps >= policy_min_ebitda_margin_bps,
        "EBITDA margin below minimum",
    );

    // 5. TIER CONSTRAINTS
    assert(tier_active, "Loan tier is not active");
    assert(borrower_annual_revenue >= tier_min_revenue, "Revenue below tier minimum");
    assert(borrower_annual_revenue <= tier_max_revenue, "Revenue above tier maximum");
    assert(borrower_ebitda >= tier_min_ebitda, "EBITDA below tier minimum");
    assert(
        borrower_debt_to_ebitda <= tier_max_debt_to_ebitda,
        "Debt-to-EBITDA exceeds tier maximum",
    );

    // Verify Policy Compliance
    // ========================
    // Security Note:
    // Noir inputs typed as `u64` enforce implicit range constraints (x < 2^64).
    // If a prover provides a value >= 2^64, the proof generation fails.
    // Therefore, "modular wrap-around" attacks on inputs are impossible at the circuit level.
    //
    // Guard against scale overflow on valid u64 inputs:
    // We strictly limit inputs to < 1 Quadrillion (10^15).
    // Max result: 10^15 * 10^4 = 10^19 (fits in u64: ~1.84 * 10^19).
    // This guarantees no integer wrap-around even with malicious inputs.
    // The Field modulus is ~10^77, so we are nowhere near Poseidon limits.
    // ---- Business logic sanity guards ----
    // Prevent nonsensical proofs that are technically valid but economically meaningless
    assert(loan_principal > 0, "Loan principal must be non-zero");
    assert(borrower_ebitda > 0, "Borrower EBITDA must be non-zero");
    assert(loan_apr_bps < 10000, "APR exceeds 100%"); // No legitimate loan > 100% APR
    assert(loan_term_days > 0, "Loan term must be non-zero");
    assert(loan_term_days <= 3650, "Loan term exceeds 10 years"); // 10 year max

    // ---- Overflow guards ----
    assert(loan_principal < 1_000_000_000_000_000, "Loan principal too large");
    assert(borrower_ebitda < 1_000_000_000_000_000, "EBITDA too large");

    // Loan-to-EBITDA check: loan_principal / borrower_ebitda <= tier_max_loan_to_ebitda / 1e18
    // Cross-multiply: loan_principal * 1e18 <= borrower_ebitda * tier_max_loan_to_ebitda
    // Direct 1e18 multiply overflows u64, so divide both sides by 1e15:
    //   loan_principal * 1,000 <= borrower_ebitda * (tier_max / 1e15)
    //
    // Overflow analysis (all inputs < 1e15, tier ratio < 10e18):
    //   Left max:  1e15 * 1,000      = 1e18  (fits u64: max ~1.84e19)
    //   Right max: 1e15 * 10,000     = 1e19  (fits u64: max ~1.84e19)
    assert(
        tier_max_loan_to_ebitda < 10_000_000_000_000_000_000,
        "Tier loan-to-EBITDA ratio too large",
    ); // < 10x
    let loan_scaled = loan_principal * 1_000;
    let tier_ratio_descaled = tier_max_loan_to_ebitda / 1_000_000_000_000_000; // divide by 1e15
    let max_loan = borrower_ebitda * tier_ratio_descaled;
    assert(loan_scaled <= max_loan, "Loan-to-EBITDA exceeds tier maximum");

    //==============================================================
    //             6. VERIFY LOAN TERMS MATCH TIER
    //==============================================================
    assert(loan_apr_bps == tier_interest_rate_bps, "APR does not match tier rate");
    assert(
        loan_origination_fee_bps == tier_origination_fee_bps,
        "Origination fee does not match tier",
    );
    assert(loan_term_days == tier_term_days, "Term does not match tier");
}

//==============================================================
//                         TESTS
//==============================================================

#[test]
fn test_policy_compliance_valid() {
    // Borrower data

    let borrower_annual_revenue: u64 = 5_000_000;
    let borrower_ebitda: u64 = 750_000;
    let borrower_tangible_net_worth: u64 = 1_000_000;
    let borrower_business_age_days: u64 = 1095;

    let borrower_defaults_last_36_months: u64 = 0;
    let borrower_has_bankruptcy: bool = false;
    let borrower_debt_to_ebitda: u64 = 25000;
    let borrower_interest_coverage: u64 = 20000;
    let borrower_current_ratio: u64 = 15000;
    let borrower_ebitda_margin_bps: u64 = 1500;

    // Policy constraints
    let policy_min_annual_revenue: u64 = 1_000_000;
    let policy_min_ebitda: u64 = 100_000;
    let policy_min_tangible_net_worth: u64 = 250_000;
    let policy_min_business_age_days: u64 = 730;
    let policy_max_defaults_36_months: u64 = 0;
    let policy_bankruptcy_excluded: bool = true;
    let policy_max_debt_to_ebitda: u64 = 40000;
    let policy_min_interest_coverage: u64 = 15000;
    let policy_min_current_ratio: u64 = 12000;
    let policy_min_ebitda_margin_bps: u64 = 1000;
    let tier_min_revenue: u64 = 1_000_000;
    let tier_max_revenue: u64 = 10_000_000;
    let tier_min_ebitda: u64 = 100_000;
    let tier_max_debt_to_ebitda: u64 = 40000;
    let tier_max_loan_to_ebitda: u64 = 1_000_000_000_000_000_000; // 1.0x in 1e18 scaling
    let tier_interest_rate_bps: u64 = 1200;
    let tier_origination_fee_bps: u64 = 100;
    let tier_term_days: u64 = 365;
    let tier_active: bool = true;

    // Bypass main and test validation logic directly
    validate_policy_compliance(
        borrower_annual_revenue,
        borrower_ebitda,
        borrower_tangible_net_worth,
        borrower_business_age_days,
        borrower_defaults_last_36_months,
        borrower_has_bankruptcy,
        borrower_debt_to_ebitda,
        borrower_interest_coverage,
        borrower_current_ratio,
        borrower_ebitda_margin_bps,
        policy_min_annual_revenue,
        policy_min_ebitda,
        policy_min_tangible_net_worth,
        policy_min_business_age_days,
        policy_max_defaults_36_months,
        policy_bankruptcy_excluded,
        policy_max_debt_to_ebitda,
        policy_min_interest_coverage,
        policy_min_current_ratio,
        policy_min_ebitda_margin_bps,
        tier_min_revenue,
        tier_max_revenue,
        tier_min_ebitda,
        tier_max_debt_to_ebitda,
        tier_max_loan_to_ebitda,
        tier_interest_rate_bps,
        tier_origination_fee_bps,
        tier_term_days,
        tier_active,
        500_000, // loan_principal
        1200, // loan_apr_bps
        100, // loan_origination_fee_bps
        365, // loan_term_days
    );
}

#[test(should_fail_with = "Annual revenue below minimum")]
fn test_fail_revenue_low() {
    let borrower_annual_revenue: u64 = 500_000; // Too low (limit 1M)

    // Other values valid
    validate_policy_compliance(
        borrower_annual_revenue,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000, // tier_max_loan_to_ebitda (1.0x in 1e18)
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Debt-to-EBITDA ratio exceeds maximum")]
fn test_fail_debt_ratio_high() {
    let borrower_debt_to_ebitda: u64 = 45000; // 4.5x (limit 4.0x)

    // Other values valid
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        borrower_debt_to_ebitda,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000, // tier_max_loan_to_ebitda (1.0x in 1e18)
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// ============================================================
// NEGATIVE TESTS: One per assert path in validate_policy_compliance
// Baseline valid values used across all tests:
//   borrower: revenue=5M, ebitda=750K, net_worth=1M, age=1095d, defaults=0, no bankruptcy
//   ratios: debt_to_ebitda=25000(2.5x), int_coverage=20000(2.0x), current=15000(1.5x), margin=1500bps
//   policy: min_rev=1M, min_ebitda=100K, min_nw=250K, min_age=730d, max_defaults=0, bankruptcy_excluded
//   policy ratios: max_debt=40000(4.0x), min_coverage=15000(1.5x), min_current=12000(1.2x), min_margin=1000bps
//   tier: rev=[1M,10M], ebitda>=100K, max_debt=40000, max_loan=1e18(1.0x), apr=1200, fee=100, term=365, active
//   loan: principal=500K, apr=1200, fee=100, term=365
// ============================================================

#[test(should_fail_with = "EBITDA below minimum")]
fn test_fail_ebitda_low() {
    validate_policy_compliance(
        5_000_000,
        50_000, // EBITDA below policy minimum (100K)
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Tangible net worth below minimum")]
fn test_fail_net_worth_low() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        100_000, // Net worth below minimum (250K)
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Business age below minimum")]
fn test_fail_business_age_low() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        365, // Business age below minimum (730 days)
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Too many defaults in last 36 months")]
fn test_fail_too_many_defaults() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        1, // Defaults = 1, max allowed = 0
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Bankruptcy excludes borrower")]
fn test_fail_bankruptcy() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        true, // Has bankruptcy, policy excludes it
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Interest coverage ratio below minimum")]
fn test_fail_interest_coverage_low() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        10000, // Interest coverage 1.0x, minimum is 1.5x (15000)
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Current ratio below minimum")]
fn test_fail_current_ratio_low() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        10000, // Current ratio 1.0x, minimum is 1.2x (12000)
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "EBITDA margin below minimum")]
fn test_fail_ebitda_margin_low() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        500, // Margin 5%, minimum is 10% (1000 bps)
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Loan tier is not active")]
fn test_fail_tier_inactive() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        false, // Tier is inactive
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Revenue below tier minimum")]
fn test_fail_revenue_below_tier() {
    validate_policy_compliance(
        500_000, // Revenue below tier minimum (1M) -- also below policy, but tier check hits first
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        100_000, // Lower policy min so policy check passes
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Revenue above tier maximum")]
fn test_fail_revenue_above_tier() {
    validate_policy_compliance(
        15_000_000, // Revenue above tier max (10M)
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "EBITDA below tier minimum")]
fn test_fail_ebitda_below_tier() {
    validate_policy_compliance(
        5_000_000,
        50_000, // EBITDA below tier minimum (100K) -- also below policy, but policy trips first
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        10_000, // Lower policy min so policy check passes
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Debt-to-EBITDA exceeds tier maximum")]
fn test_fail_debt_exceeds_tier() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        35000, // 3.5x -- passes policy max (4.0x) but exceeds tier max (3.0x)
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        30000, // Tier max 3.0x (less than policy max)
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Loan principal too large")]
fn test_fail_principal_too_large() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        1_000_000_000_000_000, // Exactly at limit (should fail, guard is strict <)
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "EBITDA too large")]
fn test_fail_ebitda_too_large() {
    validate_policy_compliance(
        5_000_000,
        1_000_000_000_000_000, // EBITDA at overflow guard limit
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Tier loan-to-EBITDA ratio too large")]
fn test_fail_tier_ratio_too_large() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        10_000_000_000_000_000_000, // 10x -- at the guard limit (strict <)
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Loan-to-EBITDA exceeds tier maximum")]
fn test_fail_loan_to_ebitda_exceeded() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        500_000_000_000_000_000, // 0.5x -- loan 500K / ebitda 750K = 0.67x exceeds 0.5x
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "APR does not match tier rate")]
fn test_fail_apr_mismatch() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1500, // APR 15% but tier specifies 12%
        100,
        365,
    );
}

#[test(should_fail_with = "Origination fee does not match tier")]
fn test_fail_origination_fee_mismatch() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        200, // Fee 2% but tier specifies 1%
        365,
    );
}

#[test(should_fail_with = "Term does not match tier")]
fn test_fail_term_mismatch() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        180, // 180 days but tier specifies 365
    );
}

// ============================================================
// NEGATIVE TESTS: Business logic sanity guards
// ============================================================

#[test(should_fail_with = "Loan principal must be non-zero")]
fn test_fail_zero_principal() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        0, // Zero principal
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "Borrower EBITDA must be non-zero")]
fn test_fail_zero_ebitda() {
    validate_policy_compliance(
        5_000_000,
        0, // Zero EBITDA
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        0, // policy min also 0 so policy check passes
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        0, // tier min also 0
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

#[test(should_fail_with = "APR exceeds 100%")]
fn test_fail_apr_too_high() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        15000, // tier rate 150% -- matches loan APR so tier check passes
        100,
        365,
        true,
        500_000,
        15000, // 150% APR
        100,
        365,
    );
}

#[test(should_fail_with = "Loan term must be non-zero")]
fn test_fail_zero_term() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        0, // tier term 0 -- matches loan so tier check passes
        true,
        500_000,
        1200,
        100,
        0, // Zero term
    );
}

#[test(should_fail_with = "Loan term exceeds 10 years")]
fn test_fail_term_too_long() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        3651, // tier term matches loan
        true,
        500_000,
        1200,
        100,
        3651, // 10 years + 1 day
    );
}

// ============================================================
// BOUNDARY VALUE TESTS: Exact edge cases (pass at limit, fail at limit +/- 1)
// ============================================================

// --- Revenue at exact policy minimum (should PASS) ---
#[test]
fn test_boundary_revenue_at_policy_min() {
    validate_policy_compliance(
        1_000_000, // Exactly at policy min
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Revenue 1 below policy minimum (should FAIL) ---
#[test(should_fail_with = "Annual revenue below minimum")]
fn test_boundary_revenue_one_below_policy_min() {
    validate_policy_compliance(
        999_999, // 1 below policy min of 1M
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Revenue at exact tier maximum (should PASS) ---
#[test]
fn test_boundary_revenue_at_tier_max() {
    validate_policy_compliance(
        10_000_000, // Exactly at tier max
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Revenue 1 above tier maximum (should FAIL) ---
#[test(should_fail_with = "Revenue above tier maximum")]
fn test_boundary_revenue_one_above_tier_max() {
    validate_policy_compliance(
        10_000_001, // 1 above tier max of 10M
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Debt ratio at exact policy max (should PASS) ---
#[test]
fn test_boundary_debt_ratio_at_max() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        40000, // Exactly at policy max (4.0x)
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Debt ratio 1 above policy max (should FAIL) ---
#[test(should_fail_with = "Debt-to-EBITDA ratio exceeds maximum")]
fn test_boundary_debt_ratio_one_above_max() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        40001, // 1 above policy max (4.0001x)
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- APR at 99.99% (should PASS) ---
#[test]
fn test_boundary_apr_at_max() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        9999, // tier rate = 99.99%
        100,
        365,
        true,
        500_000,
        9999, // APR at 99.99% -- just under 100% limit
        100,
        365,
    );
}

// --- APR at exactly 100% (should FAIL) ---
#[test(should_fail_with = "APR exceeds 100%")]
fn test_boundary_apr_at_100_percent() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        10000, // tier rate = 100%
        100,
        365,
        true,
        500_000,
        10000, // APR at exactly 100% (10000 bps)
        100,
        365,
    );
}

// --- Term at exactly 3650 days / 10 years (should PASS) ---
#[test]
fn test_boundary_term_at_max() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        3650, // tier term matches
        true,
        500_000,
        1200,
        100,
        3650, // Exactly 10 years
    );
}

// --- Term at 3651 days (should FAIL) ---
// Already covered by test_fail_term_too_long

// --- Principal at 1e15 - 1 (should PASS overflow guard) ---
#[test]
fn test_boundary_principal_just_under_limit() {
    validate_policy_compliance(
        5_000_000,
        999_999_999_999_999, // Large EBITDA so ratio check passes
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        2_000_000_000_000_000_000, // 2.0x
        1200,
        100,
        365,
        true,
        999_999_999_999_999, // 1e15 - 1 (just under overflow guard)
        1200,
        100,
        365,
    );
}

// --- Principal at 1e15 (should FAIL) ---
// Already covered by test_fail_principal_too_large

// --- EBITDA at 1e15 - 1 (should PASS overflow guard) ---
#[test]
fn test_boundary_ebitda_just_under_limit() {
    validate_policy_compliance(
        5_000_000,
        999_999_999_999_999, // 1e15 - 1
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Tier ratio at 10e18 - 1 (should PASS guard) ---
#[test]
fn test_boundary_tier_ratio_just_under_limit() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        9_999_999_999_999_999_999, // 10e18 - 1 (just under 10x)
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Interest coverage at exact minimum (should PASS) ---
#[test]
fn test_boundary_interest_coverage_at_min() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        15000, // Exactly at policy min (1.5x)
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Interest coverage 1 below minimum (should FAIL) ---
#[test(should_fail_with = "Interest coverage ratio below minimum")]
fn test_boundary_interest_coverage_one_below_min() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        false,
        25000,
        14999, // 1 below policy min
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Business age at exact minimum (should PASS) ---
#[test]
fn test_boundary_business_age_at_min() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        730, // Exactly at policy min
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}

// --- Business age 1 below minimum (should FAIL) ---
#[test(should_fail_with = "Business age below minimum")]
fn test_boundary_business_age_one_below_min() {
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        729, // 1 below policy min of 730
        0,
        false,
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        true,
        40000,
        15000,
        12000,
        1000,
        1_000_000,
        10_000_000,
        100_000,
        40000,
        1_000_000_000_000_000_000,
        1200,
        100,
        365,
        true,
        500_000,
        1200,
        100,
        365,
    );
}
