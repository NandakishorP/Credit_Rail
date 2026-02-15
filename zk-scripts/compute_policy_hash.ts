import { Barretenberg, Fr } from "@aztec/bb.js";

async function main() {
  const bb = await Barretenberg.new();
  const toFr = (val: any) => new Fr(BigInt(val));
  
  async function poseidonHash(inputs: any[]) {
    const frInputs = inputs.map(i => toFr(i));
    return await bb.poseidon2Hash(frInputs);
  }

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

  const tier = {
    id: 1,
    min_revenue: 1000000,
    max_revenue: 10000000,
    min_ebitda: 100000,
    max_debt_to_ebitda: 40000,
    max_loan_to_ebitda: "1000000000000000000",
    interest_rate: 1200,
    origination_fee: 100,
    term: 365,
    active: true
  };

  const policy_version_hash = await poseidonHash([
    policy.min_revenue, policy.min_ebitda, policy.min_net_worth, policy.min_age,
    policy.max_defaults, Number(policy.bankruptcy_excluded), policy.max_debt_to_ebitda,
    policy.min_interest_coverage, policy.min_current_ratio, policy.min_margin_bps,
    policy.max_attestation_age, tier.id, tier.min_revenue, tier.max_revenue,
    tier.min_ebitda, tier.max_debt_to_ebitda, tier.max_loan_to_ebitda,
    tier.interest_rate, tier.origination_fee, tier.term, Number(tier.active)
  ]);

  console.log("Policy Version Hash (Poseidon):");
  console.log(policy_version_hash.toString());
  console.log("");
  console.log("Padded to 32 bytes:");
  console.log("0x" + policy_version_hash.toString().slice(2).padStart(64, '0'));
  
  process.exit(0);
}

main();
