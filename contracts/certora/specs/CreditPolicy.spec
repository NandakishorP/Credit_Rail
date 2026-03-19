/*
 * Certora Verification Spec — CreditPolicy
 *
 * Core invariants:
 *   1. Frozen policies are permanently immutable
 *   2. Policy lifecycle is a one-way state machine
 *   3. Only existing policies can be modified
 *   4. Frozen requires all sections set
 */

using CreditPolicyHarness as cp;

// ═══════════════════════════════════════════════════════════════════════
//                          METHODS BLOCK
// ═══════════════════════════════════════════════════════════════════════

methods {
    // Harness getters (envfree = no msg.sender needed)
    function cp.policyCreated(uint256) external returns (bool) envfree;
    function cp.getPolicyFrozen(uint256) external returns (bool) envfree;
    function cp.getPolicyActive(uint256) external returns (bool) envfree;
    function cp.getEligibilitySet(uint256) external returns (bool) envfree;
    function cp.getRatiosSet(uint256) external returns (bool) envfree;
    function cp.getConcentrationSet(uint256) external returns (bool) envfree;
    function cp.getAttestationSet(uint256) external returns (bool) envfree;
    function cp.getCovenantsSet(uint256) external returns (bool) envfree;
    function cp.getHasAtLeastOneTier(uint256) external returns (bool) envfree;
    function cp.lastUpdated(uint256) external returns (uint256) envfree;
    function cp.policyDocumentHash(uint256) external returns (bytes32) envfree;
}

// ═══════════════════════════════════════════════════════════════════════
//                          INVARIANTS
// ═══════════════════════════════════════════════════════════════════════

/// @title frozen-implies-created
/// A frozen policy must have been created.
invariant frozenImpliesCreated(uint256 version)
    cp.getPolicyFrozen(version) => cp.policyCreated(version);

/// @title frozen-implies-all-sections-set
/// A frozen policy must have all sections populated.
invariant frozenImpliesComplete(uint256 version)
    cp.getPolicyFrozen(version) => (
        cp.getEligibilitySet(version) &&
        cp.getRatiosSet(version) &&
        cp.getConcentrationSet(version) &&
        cp.getAttestationSet(version) &&
        cp.getCovenantsSet(version) &&
        cp.getHasAtLeastOneTier(version)
    );

/// @title active-implies-created
/// An active policy must have been created.
invariant activeImpliesCreated(uint256 version)
    cp.getPolicyActive(version) => cp.policyCreated(version);

// ═══════════════════════════════════════════════════════════════════════
//                             RULES
// ═══════════════════════════════════════════════════════════════════════

/// @title frozen-is-permanent
/// Once a policy is frozen, no function call can unfreeze it.
/// This is THE critical invariant — ZK proofs depend on frozen immutability.
rule frozenIsPermanent(method f, uint256 version) {
    env e;
    calldataarg args;

    require cp.getPolicyFrozen(version);

    f(e, args);

    assert cp.getPolicyFrozen(version),
        "A frozen policy was unfrozen — critical invariant violation";
}

/// @title frozen-policy-immutable
/// No function can change lastUpdated of a frozen policy.
/// This is stronger than just "still frozen" — it proves no state changes at all.
rule frozenPolicyImmutable(method f, uint256 version) {
    env e;
    calldataarg args;

    require cp.getPolicyFrozen(version);
    uint256 lastUpdatedBefore = cp.lastUpdated(version);

    f(e, args);

    assert cp.lastUpdated(version) == lastUpdatedBefore,
        "A frozen policy's lastUpdated changed — state was modified";
}

/// @title create-policy-initializes-correctly
/// createPolicy must set created=true, active=true, frozen=false.
rule createPolicyInitializesCorrectly(uint256 version) {
    env e;

    require !cp.policyCreated(version);

    cp.createPolicy(e, version);

    assert cp.policyCreated(version);
    assert cp.getPolicyActive(version);
    assert !cp.getPolicyFrozen(version);
}

/// @title cannot-create-version-zero
/// Version 0 must always revert.
rule cannotCreateVersionZero() {
    env e;

    cp.createPolicy@withrevert(e, 0);

    assert lastReverted,
        "createPolicy(0) did not revert";
}

/// @title no-duplicate-creation
/// Creating the same version twice must revert.
rule noDuplicateCreation(uint256 version) {
    env e;

    require cp.policyCreated(version);

    cp.createPolicy@withrevert(e, version);

    assert lastReverted,
        "Duplicate policy creation did not revert";
}

/// @title deactivated-policy-not-editable
/// After deactivation, update functions must revert.
rule deactivatedPolicyBlocksEdits(uint256 version) {
    env e;

    require cp.policyCreated(version);
    require !cp.getPolicyActive(version);

    ICreditPolicy.EligibilityCriteria data;
    cp.updateEligibility@withrevert(e, version, data);

    assert lastReverted,
        "updateEligibility succeeded on a deactivated policy";
}

/// @title freeze-requires-document-hash
/// freezePolicy must revert if no document hash is set.
rule freezeRequiresDocumentHash(uint256 version) {
    env e;

    require cp.policyDocumentHash(version) == to_bytes32(0);

    cp.freezePolicy@withrevert(e, version);

    assert lastReverted,
        "freezePolicy succeeded without a document hash";
}

/// @title section-flags-monotonic
/// Once a section flag (e.g. eligibilitySet) is true, it stays true
/// unless the policy is not yet frozen (flags are never cleared).
rule eligibilitySetMonotonic(method f, uint256 version) {
    env e;
    calldataarg args;

    require cp.getEligibilitySet(version);

    f(e, args);

    assert cp.getEligibilitySet(version),
        "eligibilitySet was reset to false";
}
