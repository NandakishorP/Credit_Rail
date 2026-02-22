use poseidon::poseidon2;
use std::embedded_curve_ops::EmbeddedCurvePoint;
use std::embedded_curve_ops::EmbeddedCurveScalar;
use std::embedded_curve_ops::multi_scalar_mul;

/// Credit Policy Compliance Circuit
///
/// Proves that a loan request adheres to a frozen credit policy version.
/// This circuit verifies:
/// 1. Borrower meets eligibility criteria
/// 2. Borrower's financial ratios pass underwriting thresholds
/// 3. Loan terms match the specified tier
/// 4. Industry is not excluded
/// 5. Borrower commitment binds private data to the proof
/// 6. Underwriter Schnorr signature (Grumpkin curve) validates the borrower data
///
/// Public Inputs (visible on-chain):
/// - policy_version_hash: Hash of the frozen policy (links proof to immutable policy)
/// - loan_hash: Hash binding all loan parameters to the proof
/// - nullifierHash: Prevents double-spending of proofs
///
/// Private Inputs (hidden in proof):
/// - underwriter Schnorr signature (s_low, s_high, e) over Grumpkin curve
/// - underwriter public key (Grumpkin point: x, y as Fields)
/// - borrower_secret: Secret known only to borrower (for commitment)
/// - eligibility criteria values (borrower's actual metrics)
/// - financial ratio values (borrower's actual ratios)
/// - policy tier constraints (from the frozen policy)
/// - policy eligibility constraints (from the frozen policy)
/// - policy ratio constraints (from the frozen policy)
///
/// Signature Scheme: Schnorr over Grumpkin (BN254 embedded curve)
///   - Native to Noir's backend => ~10x fewer constraints vs ECDSA secp256k1
///   - Verification: R = s*G + e*PK, check hash(R.x, R.y, msg_hash) == e
///   - Uses std::embedded_curve_ops (multi_scalar_mul) as a blackbox opcode

//==============================================================
//                       MAIN CIRCUIT
//==============================================================

fn main(
    // === Public Inputs (exposed to verifier) ===
    policy_version_hash: pub Field, // Hash of policy version (commitment to frozen policy)
    loan_hash: pub Field,
    nullifierHash: pub Field,
    borrower_commitment: Field, // Hash(secret || borrower_data)
    underwriter_public_key_x: Field, // Underwriter PK X
    underwriter_public_key_y: Field, // Underwriter PK Y
    tier_id: u8, // Tier ID from policy
    loan_principal: u64, // Requested loan principal
    loan_apr_bps: u64, // Interest rate in basis points
    loan_origination_fee_bps: u64, // Origination fee in basis points
    loan_term_days: u64, // Term in days
    industry_hash: Field, // Hash of industry code
    current_timestamp: u64, // Current block time (approx)
    loanId: u64,
    // === Private Inputs (hidden from verifier) ===
    // Underwriter Schnorr signature (Grumpkin curve)
    underwriter_sig_s_low: Field,   // s scalar low 128 bits
    underwriter_sig_s_high: Field,  // s scalar high 128 bits
    underwriter_sig_e: Field,       // e challenge hash
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
    let computed_loan_hash = compute_loan_hash(
        borrower_commitment,
        underwriter_public_key_x,
        underwriter_public_key_y,
        tier_id,
        loan_principal,
        loan_apr_bps,
        loan_origination_fee_bps,
        loan_term_days,
        industry_hash,
        current_timestamp,
        loanId,
    );

    assert(computed_loan_hash == loan_hash, "Loan hash mismatch");
    //==============================================================
    //             1. VERIFY BORROWER COMMITMENT
    //==============================================================
    verify_borrower_commitment(
        borrower_commitment,
        borrower_secret,
        borrower_annual_revenue,
        borrower_ebitda,
        borrower_tangible_net_worth,
        borrower_business_age_days,
    );

    let computed_nullifier_hash = poseidon2::Poseidon2::hash(
        [loanId as Field, borrower_secret, loan_principal as Field, attestation_timestamp as Field],
        4,
    );
    assert(computed_nullifier_hash == nullifierHash, "Nullifier mismatch");

    //==============================================================
    //             1b. VERIFY ATTESATION AGE
    //==============================================================
    verify_attestation_age(
        current_timestamp,
        attestation_timestamp,
        policy_max_attestation_age_days,
    );

    //==============================================================
    //             1c. VERIFY UNDERWRITER SIGNATURE (Schnorr / Grumpkin)
    //==============================================================
    // The underwriter signs the raw data (without the borrower's secret).
    // This ensures that the data being proven (revenue, ebitda, etc.) was
    // explicitly authorized by the underwriter's private key.
    //
    // Schnorr over Grumpkin (BN254 embedded curve) is ~10x cheaper than
    // ECDSA secp256k1 in constraints because Grumpkin arithmetic is native
    // to the BN254 proving backend.

    // 1. Hash the data (must match what was signed off-chain)
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

    // 2. Verify Schnorr signature over Grumpkin embedded curve
    verify_schnorr_signature(
        underwriter_public_key_x,
        underwriter_public_key_y,
        underwriter_sig_s_low,
        underwriter_sig_s_high,
        underwriter_sig_e,
        data_to_sign_hash,
    );

    //==============================================================
    //             2. VERIFY POLICY VERSION HASH
    //==============================================================
    // We must hash ALL policy constraints to ensure the proof is bound
    // to the specific frozen policy version.
    let computed_policy_hash = compute_policy_hash(
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
        tier_active,
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

fn compute_loan_hash(
    borrower_commitment: Field,
    underwriter_public_key_x: Field,
    underwriter_public_key_y: Field,
    tier_id: u8,
    loan_principal: u64,
    loan_apr_bps: u64,
    loan_origination_fee_bps: u64,
    loan_term_days: u64,
    industry_hash: Field,
    current_timestamp: u64,
    loanId: u64,
) -> Field {
    poseidon2::Poseidon2::hash(
        [
            borrower_commitment,
            underwriter_public_key_x,
            underwriter_public_key_y,
            tier_id as Field,
            loan_principal as Field,
            loan_apr_bps as Field,
            loan_origination_fee_bps as Field,
            loan_term_days as Field,
            industry_hash,
            current_timestamp as Field,
            loanId as Field,
        ],
        11,
    )
}

fn verify_borrower_commitment(
    borrower_commitment: Field,
    borrower_secret: Field,
    borrower_annual_revenue: u64,
    borrower_ebitda: u64,
    borrower_tangible_net_worth: u64,
    borrower_business_age_days: u64,
) {
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
}

fn verify_attestation_age(
    current_timestamp: u64,
    attestation_timestamp: u64,
    policy_max_attestation_age_days: u64,
) {
    // Ensure the attestation is not expired
    assert(current_timestamp >= attestation_timestamp, "Attestation time in future");

    // Guard against overflow: Ensure policy max age is reasonable (e.g., < 27 years)
    assert(policy_max_attestation_age_days < 10000, "Policy age too large");
    let max_age_seconds = policy_max_attestation_age_days * 86400;

    // Guard against u64 overflow in addition
    // 0xffffffffffffffff = 18446744073709551615
    assert(attestation_timestamp <= 18446744073709551615 - max_age_seconds, "Timestamp overflow");

    assert(current_timestamp <= attestation_timestamp + max_age_seconds, "Attestation expired");
}

/// Verify a Schnorr signature over the Grumpkin embedded curve.
///
/// Schnorr signature scheme:
///   Sign(sk, m):
///     k = random nonce
///     R = k*G
///     e = H(R.x, R.y, m)
///     s = k - e*sk   (mod curve order)
///     signature = (s, e)
///
///   Verify(PK, (s, e), m):
///     R' = s*G + e*PK
///     e' = H(R'.x, R'.y, m)
///     accept if e' == e
///
/// The scalar `s` is split into (s_low, s_high) for the 128-bit limb
/// representation required by EmbeddedCurveScalar.
fn verify_schnorr_signature(
    pk_x: Field,
    pk_y: Field,
    sig_s_low: Field,
    sig_s_high: Field,
    sig_e: Field,
    msg_hash: Field,
) {
    // Validate public key is not the zero/identity point
    assert((pk_x != 0) | (pk_y != 0), "Underwriter PK cannot be the zero point");

    // Reconstruct R' = s*G + e*PK via multi_scalar_mul
    // multi_scalar_mul takes arrays of points and scalars
    let pk = EmbeddedCurvePoint { x: pk_x, y: pk_y, is_infinite: false };

    // s scalar (split into 128-bit limbs)
    let s_scalar = EmbeddedCurveScalar { lo: sig_s_low, hi: sig_s_high };

    // e scalar - fits in low limb (it's a Poseidon hash, < Field modulus, but we
    // need it as a scalar). Since e < 2^254 we put it entirely in lo with hi=0.
    // However, EmbeddedCurveScalar lo/hi are 128-bit limbs, so we must decompose e.
    let e_bytes: [u8; 32] = sig_e.to_be_bytes();
    // High 128 bits = bytes [0..16], low 128 bits = bytes [16..32]
    let mut e_hi_acc: Field = 0;
    for i in 0..16 {
        e_hi_acc = e_hi_acc * 256 + e_bytes[i] as Field;
    }
    let mut e_lo_acc: Field = 0;
    for i in 16..32 {
        e_lo_acc = e_lo_acc * 256 + e_bytes[i] as Field;
    }
    let e_scalar = EmbeddedCurveScalar { lo: e_lo_acc, hi: e_hi_acc };

    // R' = s*G + e*PK  (G is the Grumpkin generator, implicit in multi_scalar_mul
    // when used with fixed_base_scalar_mul - but multi_scalar_mul needs explicit points)
    //
    // We get G by using fixed_base_scalar_mul(1):
    let generator = std::embedded_curve_ops::fixed_base_scalar_mul(
        EmbeddedCurveScalar { lo: 1, hi: 0 },
    );

    // multi_scalar_mul: takes [Point; N], [Scalar; N] -> Point
    let r_prime = multi_scalar_mul([generator, pk], [s_scalar, e_scalar]);

    // Recompute challenge: e' = H(R'.x, R'.y, msg_hash)
    let e_prime = poseidon2::Poseidon2::hash([r_prime.x, r_prime.y, msg_hash], 3);

    assert(e_prime == sig_e, "Invalid underwriter Schnorr signature");
}

fn compute_policy_hash(
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
    policy_max_attestation_age_days: u64,
    tier_id: u8,
    tier_min_revenue: u64,
    tier_max_revenue: u64,
    tier_min_ebitda: u64,
    tier_max_debt_to_ebitda: u64,
    tier_max_loan_to_ebitda: u64,
    tier_interest_rate_bps: u64,
    tier_origination_fee_bps: u64,
    tier_term_days: u64,
    tier_active: bool,
) -> Field {
    poseidon2::Poseidon2::hash(
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
    )
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

#[test]
fn test_loan_hash_computation() {
    let hash = compute_loan_hash(
        123, // commitment
        456, // pk_x
        789, // pk_y
        1, // tier_id
        100000, // principal
        500, // apr
        100, // fee
        365, // term
        111, // industry
        1625097600, // timestamp
        999, // loanId
    );
    // Since poseidon is deterministic, we can just assert it runs and returns a field.
    assert(hash != 0);
}

// ----------------------------------------------------
// New Unit Tests for Logic Helper Functions
// ----------------------------------------------------

#[test]
fn test_verify_attestation_age_valid() {
    let now: u64 = 100000;
    let attested: u64 = 95000;
    let max_age_days: u64 = 1; // 86400 seconds
    // 95000 + 86400 = 181400 > 100000. Valid.
    verify_attestation_age(now, attested, max_age_days);
}

#[test(should_fail_with = "Attestation expired")]
fn test_verify_attestation_age_expired() {
    let now: u64 = 200000;
    let attested: u64 = 100000;
    let max_age_days: u64 = 1; // 86400 seconds
    // 100000 + 86400 = 186400 < 200000. Expired.
    verify_attestation_age(now, attested, max_age_days);
}

#[test(should_fail_with = "Attestation time in future")]
fn test_verify_attestation_future() {
    let now: u64 = 100000;
    let attested: u64 = 100001; // Future
    let max_age_days: u64 = 1;
    verify_attestation_age(now, attested, max_age_days);
}

#[test]
fn test_verify_borrower_commitment_valid() {
    let secret = 123;
    let rev = 100;
    let ebitda = 50;
    let nw = 200;
    let age = 365;

    let expected_commitment = poseidon2::Poseidon2::hash(
        [secret, rev as Field, ebitda as Field, nw as Field, age as Field],
        5,
    );

    verify_borrower_commitment(expected_commitment, secret, rev, ebitda, nw, age);
}

#[test(should_fail_with = "Borrower commitment mismatch")]
fn test_verify_borrower_commitment_invalid() {
    let secret = 123;
    let rev = 100;
    let ebitda = 50;
    let nw = 200;
    let age = 365;

    let fake_commitment = 999999; // Random wrong commitment

    verify_borrower_commitment(fake_commitment, secret, rev, ebitda, nw, age);
}

#[test]
fn test_compute_policy_hash_deterministic() {
    // Just verify it computes something non-zero given inputs
    let h1 = compute_policy_hash(
        1,
        1,
        1,
        1,
        1,
        true,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        true,
    );
    let h2 = compute_policy_hash(
        1,
        1,
        1,
        1,
        1,
        true,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        true,
    );
    assert(h1 == h2);
    assert(h1 != 0);
}

#[test]
fn test_grumpkin_generator_coords() {
    let g = std::embedded_curve_ops::fixed_base_scalar_mul(
        EmbeddedCurveScalar { lo: 1, hi: 0 },
    );
    std::println(g.x);
    std::println(g.y);

    // Also test sk=42 to cross-check with TS
    let pk42 = std::embedded_curve_ops::fixed_base_scalar_mul(
        EmbeddedCurveScalar { lo: 42, hi: 0 },
    );
    std::println(pk42.x);
    std::println(pk42.y);
}

// ============================================================
//  Schnorr Signature Verification Tests
// ============================================================
//
// These tests exercise verify_schnorr_signature by constructing
// valid and invalid signatures entirely within Noir using the
// embedded curve ops.
//
// Signing protocol (Schnorr over Grumpkin):
//   sk = private key scalar
//   PK = sk * G
//   k  = nonce scalar
//   R  = k * G
//   e  = Poseidon2(R.x, R.y, msg_hash)
//   s  = k - e * sk  (mod Grumpkin scalar order n)
//
// Verification:
//   R' = s*G + e*PK = (k - e*sk)*G + e*sk*G = k*G = R
//   check Poseidon2(R'.x, R'.y, msg_hash) == e
//
// Since Noir's Field type operates mod BN254 base field p (which equals
// Grumpkin's scalar order n), we can compute s = k - e*sk directly
// using Field arithmetic.
//
// NOTE: Noir's Field type is mod BN254 scalar field p, which does NOT
// equal the Grumpkin scalar order n. Therefore in-circuit Field
// arithmetic cannot produce valid Schnorr signatures. All test
// signatures below are generated by TypeScript (schnorrSign in
// grumpkin.ts) and hardcoded as test vectors.

#[test]
fn test_schnorr_valid_signature() {
    // Test vector: sk=42, msg=0xdeadbeef (generated by TypeScript schnorrSign)
    let pk_x = 7356913722468763155518092886238006860757299964193402191943647957243737021149;
    let pk_y = 8353686781200727416994686754908207716480106082647483667993604622182232784267;
    let sig_s_low = 239691899743278106023958643179483275456;
    let sig_s_high = 20285776104987388408700744573459738998;
    let sig_e = 2263663622233631258871148244031462747863520636951402879255806273135809089081;
    let msg_hash: Field = 0xdeadbeef;

    verify_schnorr_signature(pk_x, pk_y, sig_s_low, sig_s_high, sig_e, msg_hash);
}

#[test]
fn test_schnorr_valid_large_sk() {
    // Test vector: sk=12345, msg=0xcafe (generated by TypeScript schnorrSign)
    let pk_x = 12983840661618469667233340731503097704297377111146975658191126072435762649408;
    let pk_y = 12645901681510652395728541071285820781853167265721931988194496645906048137939;
    let sig_s_low = 332804858176902642648104489817274073478;
    let sig_s_high = 54911992435943237621340322912179742042;
    let sig_e = 21149884334567027842596724270199376388227141601980304887596315064398561333563;
    let msg_hash: Field = 0xcafe;

    verify_schnorr_signature(pk_x, pk_y, sig_s_low, sig_s_high, sig_e, msg_hash);
}

#[test]
fn test_schnorr_valid_different_messages() {
    // Same key (sk=77), two different messages -- both must verify
    let pk_x = 16478903724406101174873470909116486657403755693362912144061088127147109524999;
    let pk_y = 3057788770079463243986437324855748999702106205315072343993692932576828382893;

    // msg=111
    let sig_s_low_1 = 290882239702340463173567823677734749077;
    let sig_s_high_1 = 30406343263459881465363027257861652895;
    let sig_e_1 = 4309089213680855468287950649974997525399998383791693354011540108894293293581;

    // msg=222
    let sig_s_low_2 = 280419616473957570045209596377341127731;
    let sig_s_high_2 = 61987935101476112642766862984663336503;
    let sig_e_2 = 1335173776104721676306764661871271864756702805900421312806320873038703470755;

    // Both should verify
    verify_schnorr_signature(pk_x, pk_y, sig_s_low_1, sig_s_high_1, sig_e_1, 111);
    verify_schnorr_signature(pk_x, pk_y, sig_s_low_2, sig_s_high_2, sig_e_2, 222);

    // Challenge values must differ for different messages
    assert(sig_e_1 != sig_e_2, "Different messages should produce different challenges");
}

#[test(should_fail_with = "Invalid underwriter Schnorr signature")]
fn test_schnorr_wrong_message() {
    // Valid signature for msg=0x1111, try to verify against msg=0x2222
    let pk_x = 7356913722468763155518092886238006860757299964193402191943647957243737021149;
    let pk_y = 8353686781200727416994686754908207716480106082647483667993604622182232784267;
    let sig_s_low = 125056436142939145343778422004400335356;
    let sig_s_high = 15662354792048400410136113730557135474;
    let sig_e = 18020095578277275912538112712761083170695526776091538795513379203519625261795;

    // Should fail: signature was for 0x1111, not 0x2222
    verify_schnorr_signature(pk_x, pk_y, sig_s_low, sig_s_high, sig_e, 0x2222);
}

#[test(should_fail_with = "Invalid underwriter Schnorr signature")]
fn test_schnorr_wrong_public_key() {
    // Valid signature for sk=42/msg=0xdeadbeef, verify with sk=43's PK
    let sig_s_low = 239691899743278106023958643179483275456;
    let sig_s_high = 20285776104987388408700744573459738998;
    let sig_e = 2263663622233631258871148244031462747863520636951402879255806273135809089081;
    let msg_hash: Field = 0xdeadbeef;

    // Wrong public key (sk=43 instead of sk=42)
    let wrong_pk = std::embedded_curve_ops::fixed_base_scalar_mul(
        EmbeddedCurveScalar { lo: 43, hi: 0 },
    );

    verify_schnorr_signature(wrong_pk.x, wrong_pk.y, sig_s_low, sig_s_high, sig_e, msg_hash);
}

#[test(should_fail_with = "Invalid underwriter Schnorr signature")]
fn test_schnorr_tampered_s() {
    // Valid signature for sk=42/msg=0xface, then tamper with s_low
    let pk_x = 7356913722468763155518092886238006860757299964193402191943647957243737021149;
    let pk_y = 8353686781200727416994686754908207716480106082647483667993604622182232784267;
    let sig_s_low = 129311341365362439092422143280891672891;
    let sig_s_high = 35492193621350813989390517770614126479;
    let sig_e = 4938537043264212081904207534205945477452377293286042797542487186792401195769;

    let tampered_s_low = sig_s_low + 1;
    verify_schnorr_signature(pk_x, pk_y, tampered_s_low, sig_s_high, sig_e, 0xface);
}

#[test(should_fail_with = "Invalid underwriter Schnorr signature")]
fn test_schnorr_tampered_e() {
    // Valid signature for sk=42/msg=0xcafe, then tamper with e
    let pk_x = 7356913722468763155518092886238006860757299964193402191943647957243737021149;
    let pk_y = 8353686781200727416994686754908207716480106082647483667993604622182232784267;
    let sig_s_low = 142326886320579092766793351128361157861;
    let sig_s_high = 5083313180816318310038162783017495710;
    let sig_e = 7656672681989068073501783532716333911644106932609772507122090876583816299100;

    let tampered_e = sig_e + 1;
    verify_schnorr_signature(pk_x, pk_y, sig_s_low, sig_s_high, tampered_e, 0xcafe);
}

#[test(should_fail_with = "Invalid underwriter Schnorr signature")]
fn test_schnorr_swapped_sig_components() {
    // Valid signature for sk=42/msg=0xbeef -- try swapping s and e
    let pk_x = 7356913722468763155518092886238006860757299964193402191943647957243737021149;
    let pk_y = 8353686781200727416994686754908207716480106082647483667993604622182232784267;
    let sig_s_low = 176755168560199693824817678629895782718;
    let sig_s_high = 29198021629027676170138550864250908891;
    let sig_e = 16200705133017239460030128758837100432433406722313276157003224697790481918224;

    // Swap: use e's limbs as s, and s's value as e
    let e_bytes: [u8; 32] = sig_e.to_be_bytes();
    let mut e_hi: Field = 0;
    for i in 0..16 {
        e_hi = e_hi * 256 + e_bytes[i] as Field;
    }
    let mut e_lo: Field = 0;
    for i in 16..32 {
        e_lo = e_lo * 256 + e_bytes[i] as Field;
    }

    let mut two_128: Field = 1;
    for _ in 0..128 {
        two_128 = two_128 * 2;
    }
    let s_as_field = sig_s_high * two_128 + sig_s_low;

    verify_schnorr_signature(pk_x, pk_y, e_lo, e_hi, s_as_field, 0xbeef);
}

// ============================================================
//  Nullifier Hash Tests
// ============================================================

#[test]
fn test_nullifier_hash_deterministic() {
    // Same inputs should produce the same nullifier
    let loan_id: u64 = 1;
    let secret: Field = 0x1234;
    let principal: u64 = 500000;
    let att_time: u64 = 1000000;

    let h1 = poseidon2::Poseidon2::hash(
        [loan_id as Field, secret, principal as Field, att_time as Field], 4,
    );
    let h2 = poseidon2::Poseidon2::hash(
        [loan_id as Field, secret, principal as Field, att_time as Field], 4,
    );
    assert(h1 == h2, "Nullifier hash should be deterministic");
    assert(h1 != 0, "Nullifier hash should be non-zero");
}

#[test]
fn test_nullifier_hash_unique_per_loan() {
    // Different loanIds must produce different nullifiers
    let secret: Field = 0x1234;
    let principal: u64 = 500000;
    let att_time: u64 = 1000000;

    let h1 = poseidon2::Poseidon2::hash(
        [1 as Field, secret, principal as Field, att_time as Field], 4,
    );
    let h2 = poseidon2::Poseidon2::hash(
        [2 as Field, secret, principal as Field, att_time as Field], 4,
    );
    assert(h1 != h2, "Different loanIds must produce different nullifiers");
}

#[test]
fn test_nullifier_hash_unique_per_secret() {
    // Different secrets must produce different nullifiers
    let loan_id: u64 = 1;
    let principal: u64 = 500000;
    let att_time: u64 = 1000000;

    let h1 = poseidon2::Poseidon2::hash(
        [loan_id as Field, 0xaaaa as Field, principal as Field, att_time as Field], 4,
    );
    let h2 = poseidon2::Poseidon2::hash(
        [loan_id as Field, 0xbbbb as Field, principal as Field, att_time as Field], 4,
    );
    assert(h1 != h2, "Different secrets must produce different nullifiers");
}

// ============================================================
//  Loan Hash Uniqueness Tests
// ============================================================

#[test]
fn test_loan_hash_unique_per_loan_id() {
    let commitment: Field = 123;
    let pk_x: Field = 456;
    let pk_y: Field = 789;

    let h1 = compute_loan_hash(commitment, pk_x, pk_y, 1, 100000, 500, 100, 365, 111, 1625097600, 1);
    let h2 = compute_loan_hash(commitment, pk_x, pk_y, 1, 100000, 500, 100, 365, 111, 1625097600, 2);
    assert(h1 != h2, "Different loanIds must produce different loan hashes");
}

#[test]
fn test_loan_hash_unique_per_principal() {
    let commitment: Field = 123;
    let pk_x: Field = 456;
    let pk_y: Field = 789;

    let h1 = compute_loan_hash(commitment, pk_x, pk_y, 1, 100000, 500, 100, 365, 111, 1625097600, 1);
    let h2 = compute_loan_hash(commitment, pk_x, pk_y, 1, 200000, 500, 100, 365, 111, 1625097600, 1);
    assert(h1 != h2, "Different principals must produce different loan hashes");
}

#[test]
fn test_loan_hash_unique_per_underwriter() {
    let commitment: Field = 123;

    let h1 = compute_loan_hash(commitment, 456, 789, 1, 100000, 500, 100, 365, 111, 1625097600, 1);
    let h2 = compute_loan_hash(commitment, 999, 789, 1, 100000, 500, 100, 365, 111, 1625097600, 1);
    assert(h1 != h2, "Different underwriter keys must produce different loan hashes");
}

// ============================================================
//  Policy Hash Sensitivity Tests
// ============================================================

#[test(should_fail_with = "Policy age too large")]
fn test_verify_attestation_age_policy_too_large() {
    let now: u64 = 100000;
    let attested: u64 = 95000;
    let max_age_days: u64 = 10000; // Exactly at limit (>= 10000 should fail)
    verify_attestation_age(now, attested, max_age_days);
}

#[test(should_fail_with = "Timestamp overflow")]
fn test_verify_attestation_age_timestamp_overflow() {
    // attestation_timestamp is so large that adding max_age_seconds overflows u64
    let now: u64 = 18446744073709551615; // u64 max
    let attested: u64 = 18446744073709551615; // u64 max
    let max_age_days: u64 = 1; // 86400 seconds - attested + 86400 overflows
    verify_attestation_age(now, attested, max_age_days);
}

#[test]
fn test_bankruptcy_not_excluded_allows_bankrupt_borrower() {
    // When policy_bankruptcy_excluded = false, a borrower WITH bankruptcy should PASS
    validate_policy_compliance(
        5_000_000,
        750_000,
        1_000_000,
        1095,
        0,
        true,  // borrower HAS bankruptcy
        25000,
        20000,
        15000,
        1500,
        1_000_000,
        100_000,
        250_000,
        730,
        0,
        false, // policy does NOT exclude bankruptcy
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

#[test]
fn test_policy_hash_changes_with_single_param() {
    // Changing any single policy parameter must change the hash
    let base = compute_policy_hash(
        1000000, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1, 1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );

    // Change min_revenue
    let h1 = compute_policy_hash(
        1000001, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1, 1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );
    assert(base != h1, "Changing min_revenue must change policy hash");

    // Change tier_active
    let h2 = compute_policy_hash(
        1000000, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1, 1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, false,
    );
    assert(base != h2, "Changing tier_active must change policy hash");

    // Change bankruptcy_excluded
    let h3 = compute_policy_hash(
        1000000, 100000, 250000, 730, 0, false,
        40000, 15000, 12000, 1000, 90,
        1, 1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );
    assert(base != h3, "Changing bankruptcy_excluded must change policy hash");
}

// ============================================================
//  main() Integration Tests
//  These test vectors include valid Schnorr signatures generated
//  externally by TypeScript (gen_main_test_vectors.ts).
// ============================================================

#[test]
fn test_main_integration_happy_path() {
    // Full end-to-end: calls main() with all valid inputs
    main(
        // Public inputs
        13092986158241335727976825583457317324074370493817574499628845613236736334438, // policy_version_hash
        402538460424446851722261610110794666385356654680636238801022324790394451883,   // loan_hash
        17192326775865708290513230403267052356039504450017621353910650748243352732394, // nullifierHash
        9565104342849014344519519188506829113523896995659714250752383551693562949437,  // borrower_commitment
        7356913722468763155518092886238006860757299964193402191943647957243737021149,  // underwriter_pk_x
        8353686781200727416994686754908207716480106082647483667993604622182232784267,  // underwriter_pk_y
        1,       // tier_id
        500000,  // loan_principal
        1200,    // loan_apr_bps
        100,     // loan_origination_fee_bps
        365,     // loan_term_days
        19731118065711264997944706594056596257023240707061919347492376397191952734924, // industry_hash
        100000,  // current_timestamp
        1,       // loanId
        // Schnorr signature
        172931110297095260686301740567448529116,  // sig_s_low
        35221310651795293325313958262584868104,   // sig_s_high
        5846913548619941884626780670715341130882531025441799743459978411396200179723, // sig_e
        // Private inputs
        123,        // borrower_secret
        5000000,    // borrower_annual_revenue
        750000,     // borrower_ebitda
        1000000,    // borrower_tangible_net_worth
        1095,       // borrower_business_age_days
        0,          // borrower_defaults_last_36_months
        false,      // borrower_has_bankruptcy
        25000,      // borrower_debt_to_ebitda
        20000,      // borrower_interest_coverage
        15000,      // borrower_current_ratio
        1500,       // borrower_ebitda_margin_bps
        95000,      // attestation_timestamp
        // Policy constraints
        1000000,    // policy_min_annual_revenue
        100000,     // policy_min_ebitda
        250000,     // policy_min_tangible_net_worth
        730,        // policy_min_business_age_days
        0,          // policy_max_defaults_36_months
        true,       // policy_bankruptcy_excluded
        40000,      // policy_max_debt_to_ebitda
        15000,      // policy_min_interest_coverage
        12000,      // policy_min_current_ratio
        1000,       // policy_min_ebitda_margin_bps
        90,         // policy_max_attestation_age_days
        // Tier constraints
        1000000,    // tier_min_revenue
        10000000,   // tier_max_revenue
        100000,     // tier_min_ebitda
        40000,      // tier_max_debt_to_ebitda
        1000000000000000000, // tier_max_loan_to_ebitda
        1200,       // tier_interest_rate_bps
        100,        // tier_origination_fee_bps
        365,        // tier_term_days
        true,       // tier_active
    );
}

#[test(should_fail_with = "Loan hash mismatch")]
fn test_main_fail_loan_hash_mismatch() {
    // Same valid inputs but wrong loan_hash
    main(
        13092986158241335727976825583457317324074370493817574499628845613236736334438,
        999999, // WRONG loan_hash
        17192326775865708290513230403267052356039504450017621353910650748243352732394,
        9565104342849014344519519188506829113523896995659714250752383551693562949437,
        7356913722468763155518092886238006860757299964193402191943647957243737021149,
        8353686781200727416994686754908207716480106082647483667993604622182232784267,
        1, 500000, 1200, 100, 365,
        19731118065711264997944706594056596257023240707061919347492376397191952734924,
        100000, 1,
        172931110297095260686301740567448529116,
        35221310651795293325313958262584868104,
        5846913548619941884626780670715341130882531025441799743459978411396200179723,
        123, 5000000, 750000, 1000000, 1095, 0, false,
        25000, 20000, 15000, 1500, 95000,
        1000000, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );
}

#[test(should_fail_with = "Nullifier mismatch")]
fn test_main_fail_nullifier_mismatch() {
    // Same valid inputs but wrong nullifierHash
    main(
        13092986158241335727976825583457317324074370493817574499628845613236736334438,
        402538460424446851722261610110794666385356654680636238801022324790394451883,
        888888, // WRONG nullifierHash
        9565104342849014344519519188506829113523896995659714250752383551693562949437,
        7356913722468763155518092886238006860757299964193402191943647957243737021149,
        8353686781200727416994686754908207716480106082647483667993604622182232784267,
        1, 500000, 1200, 100, 365,
        19731118065711264997944706594056596257023240707061919347492376397191952734924,
        100000, 1,
        172931110297095260686301740567448529116,
        35221310651795293325313958262584868104,
        5846913548619941884626780670715341130882531025441799743459978411396200179723,
        123, 5000000, 750000, 1000000, 1095, 0, false,
        25000, 20000, 15000, 1500, 95000,
        1000000, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );
}

#[test(should_fail_with = "Policy hash mismatch")]
fn test_main_fail_policy_hash_mismatch() {
    // Same valid inputs but wrong policy_version_hash
    main(
        777777, // WRONG policy_version_hash
        402538460424446851722261610110794666385356654680636238801022324790394451883,
        17192326775865708290513230403267052356039504450017621353910650748243352732394,
        9565104342849014344519519188506829113523896995659714250752383551693562949437,
        7356913722468763155518092886238006860757299964193402191943647957243737021149,
        8353686781200727416994686754908207716480106082647483667993604622182232784267,
        1, 500000, 1200, 100, 365,
        19731118065711264997944706594056596257023240707061919347492376397191952734924,
        100000, 1,
        172931110297095260686301740567448529116,
        35221310651795293325313958262584868104,
        5846913548619941884626780670715341130882531025441799743459978411396200179723,
        123, 5000000, 750000, 1000000, 1095, 0, false,
        25000, 20000, 15000, 1500, 95000,
        1000000, 100000, 250000, 730, 0, true,
        40000, 15000, 12000, 1000, 90,
        1000000, 10000000, 100000, 40000,
        1000000000000000000, 1200, 100, 365, true,
    );
}
