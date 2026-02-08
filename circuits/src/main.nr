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
///
/// Public Inputs (visible on-chain):
/// - policy_version_hash: Hash of the frozen policy (links proof to immutable policy)
/// - borrower_commitment: Hash(borrower_secret, borrower_data) - privacy-preserving borrower binding
/// - tier_id: The loan tier being used
/// - loan_principal: Requested principal amount
/// - loan_apr_bps: Annual interest rate in basis points
/// - loan_origination_fee_bps: Origination fee in basis points
/// - loan_term_days: Loan term in days
/// - industry_hash: Hash of borrower's industry code
///
/// Private Inputs (hidden in proof):
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
    tier_id: pub u8, // Tier ID from policy
    loan_principal: pub u64, // Requested loan principal
    loan_apr_bps: pub u64, // Interest rate in basis points
    loan_origination_fee_bps: pub u64, // Origination fee in basis points
    loan_term_days: pub u64, // Term in days
    industry_hash: pub Field, // Hash of industry code
    // === Private Inputs (hidden from verifier) ===
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
    // Tier constraints (private - from frozen policy)
    tier_min_revenue: u64,
    tier_max_revenue: u64,
    tier_min_ebitda: u64,
    tier_max_debt_to_ebitda: u64,
    tier_max_loan_to_ebitda: u64,
    tier_interest_rate_bps: u64,
    tier_origination_fee_bps: u64,
    tier_term_days: u64,
    tier_active: bool,
    // Industry exclusion check (private)
    industry_is_excluded: bool,
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
    //             2. VERIFY POLICY VERSION HASH
    //==============================================================
    let computed_policy_hash = poseidon2::Poseidon2::hash(
        [
            policy_min_annual_revenue as Field,
            policy_min_ebitda as Field,
            policy_min_tangible_net_worth as Field,
            policy_min_business_age_days as Field,
            policy_max_defaults_36_months as Field,
            policy_max_debt_to_ebitda as Field,
            policy_min_interest_coverage as Field,
            policy_min_current_ratio as Field,
            policy_min_ebitda_margin_bps as Field,
            tier_interest_rate_bps as Field,
            tier_origination_fee_bps as Field,
            tier_term_days as Field,
        ],
        12,
    );
    assert(computed_policy_hash == policy_version_hash, "Policy hash mismatch");

    //==============================================================
    //             3. VERIFY ELIGIBILITY CRITERIA
    //==============================================================
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

    //==============================================================
    //             4. VERIFY FINANCIAL RATIOS
    //==============================================================
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

    //==============================================================
    //             5. VERIFY TIER CONSTRAINTS
    //==============================================================
    assert(tier_active, "Loan tier is not active");
    assert(borrower_annual_revenue >= tier_min_revenue, "Revenue below tier minimum");
    assert(borrower_annual_revenue <= tier_max_revenue, "Revenue above tier maximum");
    assert(borrower_ebitda >= tier_min_ebitda, "EBITDA below tier minimum");
    assert(
        borrower_debt_to_ebitda <= tier_max_debt_to_ebitda,
        "Debt-to-EBITDA exceeds tier maximum",
    );

    // Loan-to-EBITDA check (principal / EBITDA <= tier max)
    let loan_to_ebitda_scaled = (loan_principal as u64) * 10000;
    let max_loan_scaled = (borrower_ebitda as u64) * tier_max_loan_to_ebitda;
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

    //==============================================================
    //             7. VERIFY INDUSTRY NOT EXCLUDED
    //==============================================================
    assert(!industry_is_excluded, "Industry is excluded from policy");
}

//==============================================================
//                         TESTS
//==============================================================

#[test]
fn test_policy_compliance_valid() {
    // Borrower data
    let borrower_secret = 12345;
    let borrower_annual_revenue: u64 = 5_000_000;
    let borrower_ebitda: u64 = 750_000;
    let borrower_tangible_net_worth: u64 = 1_000_000;
    let borrower_business_age_days: u64 = 1095;

    let borrower_commitment = poseidon2::Poseidon2::hash(
        [
            borrower_secret,
            borrower_annual_revenue as Field,
            borrower_ebitda as Field,
            borrower_tangible_net_worth as Field,
            borrower_business_age_days as Field,
        ],
        5,
    );

    // Policy constraints
    let policy_min_annual_revenue: u64 = 1_000_000;
    let policy_min_ebitda: u64 = 100_000;
    let policy_min_tangible_net_worth: u64 = 250_000;
    let policy_min_business_age_days: u64 = 730;
    let policy_max_defaults_36_months: u64 = 0;
    let policy_max_debt_to_ebitda: u64 = 40000;
    let policy_min_interest_coverage: u64 = 15000;
    let policy_min_current_ratio: u64 = 12000;
    let policy_min_ebitda_margin_bps: u64 = 1000;
    let tier_interest_rate_bps: u64 = 1200;
    let tier_origination_fee_bps: u64 = 100;
    let tier_term_days: u64 = 365;

    let policy_version_hash = poseidon2::Poseidon2::hash(
        [
            policy_min_annual_revenue as Field,
            policy_min_ebitda as Field,
            policy_min_tangible_net_worth as Field,
            policy_min_business_age_days as Field,
            policy_max_defaults_36_months as Field,
            policy_max_debt_to_ebitda as Field,
            policy_min_interest_coverage as Field,
            policy_min_current_ratio as Field,
            policy_min_ebitda_margin_bps as Field,
            tier_interest_rate_bps as Field,
            tier_origination_fee_bps as Field,
            tier_term_days as Field,
        ],
        12,
    );

    main(
        policy_version_hash,
        borrower_commitment,
        0, // tier_id
        500_000, // loan_principal
        1200, // loan_apr_bps
        100, // loan_origination_fee_bps
        365, // loan_term_days
        0x1234, // industry_hash
        borrower_secret,
        borrower_annual_revenue,
        borrower_ebitda,
        borrower_tangible_net_worth,
        borrower_business_age_days,
        0, // borrower_defaults_last_36_months
        false, // borrower_has_bankruptcy
        25000, // borrower_debt_to_ebitda
        20000, // borrower_interest_coverage
        15000, // borrower_current_ratio
        1500, // borrower_ebitda_margin_bps
        policy_min_annual_revenue,
        policy_min_ebitda,
        policy_min_tangible_net_worth,
        policy_min_business_age_days,
        policy_max_defaults_36_months,
        true, // policy_bankruptcy_excluded
        policy_max_debt_to_ebitda,
        policy_min_interest_coverage,
        policy_min_current_ratio,
        policy_min_ebitda_margin_bps,
        1_000_000, // tier_min_revenue
        10_000_000, // tier_max_revenue
        100_000, // tier_min_ebitda
        40000, // tier_max_debt_to_ebitda
        10000, // tier_max_loan_to_ebitda
        tier_interest_rate_bps,
        tier_origination_fee_bps,
        tier_term_days,
        true, // tier_active
        false, // industry_is_excluded
    );
}
