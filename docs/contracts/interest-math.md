# InterestMath

`InterestMath` is a pure Solidity library used internally by `TranchePool`. It contains three math helpers for interest computation. All functions are `internal pure` — they have no side effects and zero deployment overhead.

---

## Constants

```solidity
uint256 internal constant INDEX_PRECISION  = 1e18;
uint256 internal constant SECONDS_PER_YEAR = 365 days;   // 31_536_000 seconds
uint256 internal constant BPS_DENOMINATOR  = 10_000;     // 100% = 10,000 bps
```

---

## Functions

### `accrueTargetInterest`

Computes the interest accrued on a deployed principal over an elapsed time at a fixed APR.

```solidity
function accrueTargetInterest(
    uint256 deployedValue,
    uint256 aprBps,
    uint256 timeElapsed
) internal pure returns (uint256 accrued)
```

**Formula:**
```
accrued = deployedValue × aprBps × timeElapsed
          ─────────────────────────────────────
              SECONDS_PER_YEAR × BPS_DENOMINATOR
```

**Notes:**
- Returns `0` if `deployedValue == 0` or `timeElapsed == 0`
- APR is in basis points: 1200 bps = 12% APR
- `timeElapsed` is in seconds
- Uses integer division — small rounding losses are expected and acceptable

---

### `calculateClaimable`

Computes how much interest an LP can claim based on the difference between the current global interest index and the index at their last claim.

```solidity
function calculateClaimable(
    uint256 userShares,
    uint256 currentIndex,
    uint256 userIndex
) internal pure returns (uint256 claimable)
```

**Formula:**
```
claimable = userShares × (currentIndex - userIndex)
            ─────────────────────────────────────────
                          INDEX_PRECISION
```

**Notes:**
- Returns `0` if `userShares == 0` or `currentIndex <= userIndex`
- `INDEX_PRECISION` (`1e18`) is divided out to convert back from index-scaled units to token units
- The LP's `userIndex` is updated to `currentIndex` after a successful claim

---

### `computeIndexDelta`

Computes the increment to add to the global interest index when distributing a payment across all shares.

```solidity
function computeIndexDelta(
    uint256 paidAmount,
    uint256 totalShares
) internal pure returns (uint256 indexDelta)
```

**Formula:**
```
indexDelta = paidAmount × INDEX_PRECISION
             ──────────────────────────────
                      totalShares
```

**Notes:**
- Returns `0` if `totalShares == 0`
- Multiplying by `INDEX_PRECISION` before dividing preserves precision — avoiding the integer truncation that would occur if dividing first
- The resulting `indexDelta` is added to `tranche.interestIndex`, which `calculateClaimable` later divides out

---

## Why the Index Pattern?

A naive implementation would iterate over all LPs to distribute interest on every repayment. This would make gas cost proportional to the number of LPs — unusable at scale.

The global index pattern solves this:
- One division per distribution (when `computeIndexDelta` is called)
- One multiplication per LP claim (when `calculateClaimable` is called)
- Gas cost is constant regardless of how many LPs are in the pool

This is the same pattern used by Aave's liquidity index and Compound's exchange rate model.
