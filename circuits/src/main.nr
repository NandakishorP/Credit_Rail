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
    // Suppress unused variable warnings for public inputs used for on-chain binding
    let _ = tier_id;
    let _ = industry_hash;

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
            industry_hash, // Bind industry to the signature too
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
            policy_bankruptcy_excluded as Field, // Added
            policy_max_debt_to_ebitda as Field,
            policy_min_interest_coverage as Field,
            policy_min_current_ratio as Field,
            policy_min_ebitda_margin_bps as Field,
            policy_max_attestation_age_days as Field, // Added
            // Tier constraints
            tier_min_revenue as Field, // Added
            tier_max_revenue as Field, // Added
            tier_min_ebitda as Field, // Added
            tier_max_debt_to_ebitda as Field, // Added
            tier_max_loan_to_ebitda as Field, // Added
            tier_interest_rate_bps as Field,
            tier_origination_fee_bps as Field,
            tier_term_days as Field,
            tier_active as Field, // Added
        ],
        20,
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

    //==============================================================
    //             6. VERIFY LOAN TERMS MATCH TIER
    //==============================================================
    assert(loan_apr_bps == tier_interest_rate_bps, "APR does not match tier rate");
    assert(
        loan_origination_fee_bps == tier_origination_fee_bps,
        "Origination fee does not match tier",
    );
    assert(loan_term_days == tier_term_days, "Term does not match tier");

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

    assert(loan_principal < 1_000_000_000_000_000, "Loan principal too large");
    assert(borrower_ebitda < 1_000_000_000_000_000, "EBITDA too large");

    let loan_to_ebitda_scaled = loan_principal * 10000;
    let max_loan_scaled = borrower_ebitda * tier_max_loan_to_ebitda;
    assert(loan_to_ebitda_scaled <= max_loan_scaled, "Loan-to-EBITDA exceeds tier maximum");

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
    let tier_max_loan_to_ebitda: u64 = 10000;
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
        10000,
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
        10000,
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
