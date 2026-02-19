/**
 * Grumpkin curve definition and Schnorr signature utilities.
 *
 * Grumpkin is the "embedded curve" of BN254 (alt_bn128):
 *   - Base field  p = BN254 scalar field r
 *   - Scalar field n = BN254 base field p
 *   - Equation: y^2 = x^3 - 17
 *   - Cofactor h = 1
 *
 * Schnorr scheme (matching the Noir circuit verify_schnorr_signature):
 *   Sign(sk, msg_hash):
 *     k  = random nonce (deterministic via RFC 6979 from noble-curves)
 *     R  = k * G
 *     e  = Poseidon2(R.x, R.y, msg_hash)
 *     s  = k - e * sk   (mod n)
 *     return (s_low, s_high, e)   -- s split into 128-bit limbs
 *
 *   Verify(PK, (s_low, s_high, e), msg_hash):
 *     R' = s*G + e*PK
 *     e' = Poseidon2(R'.x, R'.y, msg_hash)
 *     accept iff e' == e
 */

import { weierstrass } from "@noble/curves/abstract/weierstrass";
import { Field as NobleField } from "@noble/curves/abstract/modular";
import { sha256 } from "@noble/hashes/sha256";
import { hmac } from "@noble/hashes/hmac";
import { concatBytes, randomBytes } from "@noble/hashes/utils";

// ---- Grumpkin curve parameters ----
// BN254 scalar field (becomes Grumpkin base field)
const GRUMPKIN_P = BigInt(
  "21888242871839275222246405745257275088548364400416034343698204186575808495617"
);
// BN254 base field (becomes Grumpkin scalar field / curve order)
const GRUMPKIN_N = BigInt(
  "21888242871839275222246405745257275088696311157297823662689037894645226208583"
);

// Grumpkin generator point
// Standard generator from Aztec/Barretenberg:
const GRUMPKIN_Gx = BigInt(1);
// y coordinate for x=1 on y^2 = x^3 - 17 mod p
// y^2 = 1 - 17 = -16 mod p
// y = sqrt(-16 mod p)
const GRUMPKIN_Gy = BigInt(
  "17631683881184975370165255887551781615748388533673675138860"
);

export const grumpkin = weierstrass({
  a: BigInt(0),
  b: GRUMPKIN_P - BigInt(17), // -17 mod p
  Fp: NobleField(GRUMPKIN_P),
  n: GRUMPKIN_N,
  Gx: GRUMPKIN_Gx,
  Gy: GRUMPKIN_Gy,
  h: BigInt(1),
  hash: sha256,
  hmac: (key: Uint8Array, ...msgs: Uint8Array[]) =>
    hmac(sha256, key, concatBytes(...msgs)),
  randomBytes,
});

/** The 128-bit mask for splitting a scalar into lo/hi limbs */
const LIMB_MASK = (BigInt(1) << BigInt(128)) - BigInt(1);

/**
 * Split a bigint into (lo, hi) 128-bit limbs.
 * lo = value & ((1<<128)-1)
 * hi = value >> 128
 */
export function splitScalar(value: bigint): { lo: bigint; hi: bigint } {
  return {
    lo: value & LIMB_MASK,
    hi: value >> BigInt(128),
  };
}

/**
 * Generate a Grumpkin keypair.
 * Returns { privateKey: bigint, publicKey: { x: bigint, y: bigint } }
 */
export function generateKeypair(seed?: Uint8Array) {
  let privKeyBytes: Uint8Array;
  if (seed) {
    // Use provided seed (must be 32 bytes)
    privKeyBytes = seed;
  } else {
    privKeyBytes = randomBytes(32);
  }

  // Ensure private key is in valid range [1, n-1]
  let sk = BigInt(0);
  for (const b of privKeyBytes) {
    sk = (sk << BigInt(8)) | BigInt(b);
  }
  sk = ((sk % (GRUMPKIN_N - BigInt(1))) + BigInt(1)); // Ensure non-zero, in range

  const pk = grumpkin.ProjectivePoint.BASE.multiply(sk).toAffine();
  return {
    privateKey: sk,
    publicKey: { x: pk.x, y: pk.y },
  };
}

/**
 * Deterministic keypair from a counter-based seed (matching the old ethers pattern).
 * Loops until a valid keypair whose coordinates are within BN254 Field range.
 *
 * Since Grumpkin base field == BN254 scalar field, coordinates are always valid
 * Noir Field elements (both < BN254 scalar field modulus). No filtering needed.
 */
export function generateDeterministicKeypair(seedPrefix: string, startCounter = 1) {
  // Use a simple hash-based seed
  const encoder = new TextEncoder();
  const seedBytes = encoder.encode(`${seedPrefix}-${startCounter}`);

  // Hash to get 32 bytes
  // We use sha256 since it's already imported
  const hash = sha256(seedBytes);

  return generateKeypair(hash);
}

export interface SchnorrSignature {
  sLow: bigint;   // s scalar low 128 bits
  sHigh: bigint;  // s scalar high 128 bits
  e: bigint;      // challenge hash (full Field element)
}

/**
 * Sign a message hash using Schnorr over Grumpkin.
 *
 * @param sk      - private key (bigint, mod Grumpkin order)
 * @param msgHash - the Poseidon2 hash to sign (bigint, a BN254 Field element)
 * @param poseidon2HashFn - async function that computes Poseidon2 hash
 *                          Takes [R.x, R.y, msgHash] and returns a Field (bigint)
 *
 * The signing uses a deterministic nonce k = H(sk || msgHash) for safety,
 * so the same (sk, msg) always produces the same signature.
 */
export async function schnorrSign(
  sk: bigint,
  msgHash: bigint,
  poseidon2HashFn: (inputs: bigint[]) => Promise<bigint>
): Promise<SchnorrSignature> {
  // Deterministic nonce: k = sha256(sk_bytes || msgHash_bytes) mod n
  const skBytes = bigintToBytes32(sk);
  const msgBytes = bigintToBytes32(msgHash);
  const nonceHash = sha256(concatBytes(skBytes, msgBytes));
  let k = BigInt(0);
  for (const b of nonceHash) {
    k = (k << BigInt(8)) | BigInt(b);
  }
  k = ((k % (GRUMPKIN_N - BigInt(1))) + BigInt(1)); // Ensure k in [1, n-1]

  // R = k * G
  const R = grumpkin.ProjectivePoint.BASE.multiply(k).toAffine();

  // e = Poseidon2(R.x, R.y, msgHash)
  const e = await poseidon2HashFn([R.x, R.y, msgHash]);

  // s = k - e * sk  (mod n)
  let s = (k - ((e % GRUMPKIN_N) * sk) % GRUMPKIN_N) % GRUMPKIN_N;
  if (s < BigInt(0)) s += GRUMPKIN_N;

  // Split s into 128-bit limbs
  const { lo: sLow, hi: sHigh } = splitScalar(s);

  return { sLow, sHigh, e };
}

/**
 * Convert a bigint to a 32-byte big-endian Uint8Array.
 */
function bigintToBytes32(val: bigint): Uint8Array {
  const bytes = new Uint8Array(32);
  let v = val;
  for (let i = 31; i >= 0; i--) {
    bytes[i] = Number(v & BigInt(0xff));
    v >>= BigInt(8);
  }
  return bytes;
}

/**
 * Convert a bigint to a hex string with 0x prefix padded to 64 chars.
 */
export function toHex32(val: bigint): string {
  return "0x" + val.toString(16).padStart(64, "0");
}
