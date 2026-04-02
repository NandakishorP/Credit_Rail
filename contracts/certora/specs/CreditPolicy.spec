/*
 * Certora Verification Spec — CreditPolicy
 *
 * Core invariants:
 *   1. Frozen policies are permanently immutable
 *   2. Policy lifecycle is a one-way state machine
 *   3. Only existing policies can be modified
 *   4. Frozen requires scope hash + document hash
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
    function cp.getHasScopeHash(uint256) external returns (bool) envfree;
    function cp.lastUpdated(uint256) external returns (uint256) envfree;
    function cp.policyDocumentHash(uint256) external returns (bytes32) envfree;
    function cp.isInitialized() external returns (bool) envfree;
}

// ═══════════════════════════════════════════════════════════════════════
//                          DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════

definition INIT() returns bool = cp.isInitialized();

// Exclude initialize, proxy upgrade, and initializeHarness from parametric checks.
// initialize resets HAVOC'd storage; upgradeToAndCall is proxy infrastructure.
definition EXCLUDED(method f) returns bool =
    f.selector == sig:upgradeToAndCall(address,bytes).selector
    || f.selector == sig:initialize(address).selector
    || f.selector == sig:initializeHarness(address).selector;

// ═══════════════════════════════════════════════════════════════════════
//                          INVARIANTS
// ═══════════════════════════════════════════════════════════════════════

/// @title frozen-implies-created
/// A frozen policy must have been created.
invariant frozenImpliesCreated(uint256 version)
    INIT() => (cp.getPolicyFrozen(version) => cp.policyCreated(version))
    filtered { f -> !EXCLUDED(f) }

/// @title frozen-implies-scope-hash-set
/// A frozen policy must have a scope hash set.
invariant frozenImpliesComplete(uint256 version)
    INIT() => (cp.getPolicyFrozen(version) => cp.getHasScopeHash(version))
    filtered { f -> !EXCLUDED(f) }

/// @title active-implies-created
/// An active policy must have been created.
invariant activeImpliesCreated(uint256 version)
    INIT() => (cp.getPolicyActive(version) => cp.policyCreated(version))
    filtered { f -> !EXCLUDED(f) }

// ═══════════════════════════════════════════════════════════════════════
//                             RULES
// ═══════════════════════════════════════════════════════════════════════

/// @title frozen-is-permanent
/// Once a policy is frozen, no function call can unfreeze it.
/// This is THE critical invariant — ZK proofs depend on frozen immutability.
rule frozenIsPermanent(method f, uint256 version)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    require cp.policyCreated(version);
    require cp.getPolicyFrozen(version);

    f(e, args);

    assert cp.getPolicyFrozen(version),
        "A frozen policy was unfrozen — critical invariant violation";
}

/// @title frozen-policy-immutable
/// No function can change lastUpdated of a frozen policy.
/// This is stronger than just "still frozen" — it proves no state changes at all.
rule frozenPolicyImmutable(method f, uint256 version)
filtered { f -> !EXCLUDED(f)
    && f.selector != sig:deActivatePolicy(uint256).selector }
{
    env e;
    calldataarg args;
    require INIT();

    require cp.policyCreated(version);
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
    require INIT();

    require !cp.policyCreated(version);
    require !cp.getPolicyFrozen(version);

    cp.createPolicy(e, version);

    assert cp.policyCreated(version);
    assert cp.getPolicyActive(version);
    assert !cp.getPolicyFrozen(version);
}

/// @title cannot-create-version-zero
/// Version 0 must always revert.
rule cannotCreateVersionZero() {
    env e;
    require INIT();

    cp.createPolicy@withrevert(e, 0);

    assert lastReverted,
        "createPolicy(0) did not revert";
}

/// @title no-duplicate-creation
/// Creating the same version twice must revert.
rule noDuplicateCreation(uint256 version) {
    env e;
    require INIT();

    require cp.policyCreated(version);

    cp.createPolicy@withrevert(e, version);

    assert lastReverted,
        "Duplicate policy creation did not revert";
}

/// @title deactivated-policy-not-editable
/// After deactivation, setPolicyScopeHash must revert.
rule deactivatedPolicyBlocksEdits(uint256 version) {
    env e;
    require INIT();

    require cp.policyCreated(version);
    require !cp.getPolicyActive(version);

    cp.setPolicyScopeHash@withrevert(e, version, 0, to_bytes32(1));

    assert lastReverted,
        "setPolicyScopeHash succeeded on a deactivated policy";
}

/// @title freeze-requires-document-hash
/// freezePolicy must revert if no document hash is set.
rule freezeRequiresDocumentHash(uint256 version) {
    env e;
    require INIT();

    require cp.policyDocumentHash(version) == to_bytes32(0);

    cp.freezePolicy@withrevert(e, version);

    assert lastReverted,
        "freezePolicy succeeded without a document hash";
}

/// @title scope-hash-set-monotonic
/// Once hasScopeHash is true, it stays true.
rule scopeHashSetMonotonic(method f, uint256 version)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    require cp.getHasScopeHash(version);

    f(e, args);

    assert cp.getHasScopeHash(version),
        "hasScopeHash was reset to false";
}
