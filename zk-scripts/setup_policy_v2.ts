import { ethers } from "ethers";
import * as fs from "fs";
import * as path from "path";
import { Barretenberg, Fr } from "@aztec/bb.js";

// Load .env.deployed
const envPath = path.join(__dirname, ".env.deployed");
if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, "utf8");
    const envVars = envContent.split("\n").filter(line => line.includes("="));
    envVars.forEach(line => {
        const [key, value] = line.split("=");
        process.env[key.trim()] = value.trim();
    });
}

// CreditPolicy ABI (partial)
const CREDIT_POLICY_ABI = [
    "function updateEligibility(uint256 version, tuple(uint256 minAnnualRevenue, uint256 minEBITDA, uint256 minTangibleNetWorth, uint256 minBusinessAgeDays, uint256 maxDefaultsLast36Months, bool bankruptcyExcluded) data) external",
    "function updateRatios(uint256 version, tuple(uint256 maxTotalDebtToEBITDA, uint256 minInterestCoverageRatio, uint256 minCurrentRatio, uint256 minEBITDAMarginBps) data) external",
    "function updateConcentration(uint256 version, tuple(uint256 maxSingleBorrowerBps, uint256 maxIndustryConcentrationBps) data) external",
    "function updateAttestation(uint256 version, tuple(uint256 maxAttestationAgeDays, uint256 reAttestationFrequencyDays, bool requiresCPAAttestation) data) external",
    "function updateCovenants(uint256 version, tuple(uint256 maxLeverageRatio, uint256 minCoverageRatio, uint256 minLiquidityAmount, bool allowsDividends, uint256 reportingFrequencyDays) data) external",
    "function setLoanTier(uint256 version, uint8 tierId, tuple(string name, uint256 minRevenue, uint256 maxRevenue, uint256 minEBITDA, uint256 maxDebtToEBITDA, uint256 maxLoanToEBITDA, uint256 interestRateBps, uint256 originationFeeBps, uint256 termDays, bool active) tier) external",
    "function setPolicyDocument(uint256 version, bytes32 hash, string uri) external",
    "function setPolicyScopeHash(uint256 version, bytes32 hash) external",
    "function freezePolicy(uint256 version) external",
    "function policyCreated(uint256) view returns (bool)",
    "function policyFrozen(uint256) view returns (bool)",
    "function eligibilitySet(uint256) view returns (bool)",
    "function ratiosSet(uint256) view returns (bool)",
    "function concentrationSet(uint256) view returns (bool)",
    "function attestationSet(uint256) view returns (bool)",
    "function covenantsSet(uint256) view returns (bool)",
    "function hasAtLeastOneTier(uint256) view returns (bool)",
    "function policyDocumentHash(uint256) view returns (bytes32)",
    "function policyScopeHash(uint256) view returns (bytes32)",
];

async function poseidonHash(inputs: bigint[]): Promise<string> {
    const bb = await Barretenberg.new({ threads: 1 });
    
    // Convert inputs to Fr elements
    const frInputs = inputs.map(x => new Fr(x));
    
    // Poseidon2 hash
    const result = await bb.poseidon2Hash(frInputs);
    
    await bb.destroy();
    
    // result.toString() gives hex like "0x..."
    return result.toString();
}

async function main() {
    const rpcUrl = process.env.RPC_URL || "http://127.0.0.1:8546";
    const policyAddress = process.env.CREDIT_POLICY!;
    
    // Private key for anvil account 0
    const privateKey = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
    
    const provider = new ethers.JsonRpcProvider(rpcUrl);
    const signer = new ethers.Wallet(privateKey, provider);
    
    const creditPolicy = new ethers.Contract(policyAddress, CREDIT_POLICY_ABI, signer);
    
    const POLICY_VERSION = 2;
    
    console.log(`Setting up CreditPolicy v${POLICY_VERSION} at ${policyAddress}`);
    
    // Check if policy exists
    const exists = await creditPolicy.policyCreated(POLICY_VERSION);
    console.log(`Policy v${POLICY_VERSION} exists: ${exists}`);
    
    if (!exists) {
        console.log("Error: Policy v2 does not exist!");
        return;
    }
    
    const frozen = await creditPolicy.policyFrozen(POLICY_VERSION);
    if (frozen) {
        console.log("Policy v2 is already frozen!");
        return;
    }
    
    // Policy parameters matching the circuit (from compute_policy_hash.ts)
    const policy = {
        min_revenue: 1000000n,         // minAnnualRevenue
        min_ebitda: 100000n,           // minEBITDA
        min_net_worth: 250000n,        // minTangibleNetWorth (was 50000)
        min_age: 730n,                 // minBusinessAgeDays (was 365)
        max_defaults: 0n,              // maxDefaultsLast36Months
        bankruptcy_excluded: true,     // bankruptcyExcluded (was false)
        max_debt_to_ebitda: 40000n,    // maxTotalDebtToEBITDA (was 500)
        min_interest_coverage: 15000n, // minInterestCoverageRatio (was 125)
        min_current_ratio: 12000n,     // minCurrentRatio (was 150)
        min_margin_bps: 1000n,         // minEBITDAMarginBps (10%)
        max_attestation_age: 90n,      // maxAttestationAgeDays (was 86400)
    };
    
    // Tier 1 parameters (from compute_policy_hash.ts)
    const tier = {
        id: 1n,
        min_revenue: 1000000n,         // was 500000
        max_revenue: 10000000n,        // was 5000000
        min_ebitda: 100000n,           // was 50000
        max_debt_to_ebitda: 40000n,    // was 600
        max_loan_to_ebitda: BigInt("1000000000000000000"), // was 300
        interest_rate: 1200n,          // 12.00%
        origination_fee: 100n,         // 1.00%
        term: 365n,                    // was 730
        active: true,
    };
    
    // Compute Poseidon hash of policy parameters
    console.log("\nComputing policy scope hash...");
    const policyVersionHashStr = await poseidonHash([
        policy.min_revenue,
        policy.min_ebitda,
        policy.min_net_worth,
        policy.min_age,
        policy.max_defaults,
        policy.bankruptcy_excluded ? 1n : 0n,
        policy.max_debt_to_ebitda,
        policy.min_interest_coverage,
        policy.min_current_ratio,
        policy.min_margin_bps,
        policy.max_attestation_age,
        tier.id,
        tier.min_revenue,
        tier.max_revenue,
        tier.min_ebitda,
        tier.max_debt_to_ebitda,
        tier.max_loan_to_ebitda,
        tier.interest_rate,
        tier.origination_fee,
        tier.term,
        tier.active ? 1n : 0n,
    ]);
    
    // Ensure proper padding to 32 bytes
    const policyHashHex = "0x" + policyVersionHashStr.slice(2).padStart(64, "0");
    console.log(`Policy Version Hash: ${policyHashHex}`);
    
    // Check what's already set
    const eligibilityAlreadySet = await creditPolicy.eligibilitySet(POLICY_VERSION);
    const ratiosAlreadySet = await creditPolicy.ratiosSet(POLICY_VERSION);
    const concentrationAlreadySet = await creditPolicy.concentrationSet(POLICY_VERSION);
    const attestationAlreadySet = await creditPolicy.attestationSet(POLICY_VERSION);
    const covenantsAlreadySet = await creditPolicy.covenantsSet(POLICY_VERSION);
    const tierAlreadySet = await creditPolicy.hasAtLeastOneTier(POLICY_VERSION);
    const docHashAlready = await creditPolicy.policyDocumentHash(POLICY_VERSION);
    const scopeHashAlready = await creditPolicy.policyScopeHash(POLICY_VERSION);
    
    // 1. Set eligibility
    if (!eligibilityAlreadySet) {
        console.log("\n1. Setting eligibility...");
        const eligibilityTx = await creditPolicy.updateEligibility(POLICY_VERSION, {
            minAnnualRevenue: policy.min_revenue,
            minEBITDA: policy.min_ebitda,
            minTangibleNetWorth: policy.min_net_worth,
            minBusinessAgeDays: policy.min_age,
            maxDefaultsLast36Months: policy.max_defaults,
            bankruptcyExcluded: policy.bankruptcy_excluded,
        });
        await eligibilityTx.wait();
        console.log("   ✅ Eligibility set");
    } else {
        console.log("\n1. Eligibility already set, skipping");
    }
    
    // 2. Set ratios
    if (!ratiosAlreadySet) {
        console.log("2. Setting ratios...");
        const ratiosTx = await creditPolicy.updateRatios(POLICY_VERSION, {
            maxTotalDebtToEBITDA: policy.max_debt_to_ebitda,
            minInterestCoverageRatio: policy.min_interest_coverage,
            minCurrentRatio: policy.min_current_ratio,
            minEBITDAMarginBps: policy.min_margin_bps,
        });
        await ratiosTx.wait();
        console.log("   ✅ Ratios set");
    } else {
        console.log("2. Ratios already set, skipping");
    }
    
    // 3. Set concentration
    if (!concentrationAlreadySet) {
        console.log("3. Setting concentration...");
        const concentrationTx = await creditPolicy.updateConcentration(POLICY_VERSION, {
            maxSingleBorrowerBps: 1000n,      // 10%
            maxIndustryConcentrationBps: 3000n, // 30%
        });
        await concentrationTx.wait();
        console.log("   ✅ Concentration set");
    } else {
        console.log("3. Concentration already set, skipping");
    }
    
    // 4. Set attestation
    if (!attestationAlreadySet) {
        console.log("4. Setting attestation...");
        const attestationTx = await creditPolicy.updateAttestation(POLICY_VERSION, {
            maxAttestationAgeDays: policy.max_attestation_age,
            reAttestationFrequencyDays: 365n,
            requiresCPAAttestation: true,
        });
        await attestationTx.wait();
        console.log("   ✅ Attestation set");
    } else {
        console.log("4. Attestation already set, skipping");
    }
    
    // 5. Set covenants
    if (!covenantsAlreadySet) {
        console.log("5. Setting covenants...");
        const covenantsTx = await creditPolicy.updateCovenants(POLICY_VERSION, {
            maxLeverageRatio: 150n,       // 1.5x
            minCoverageRatio: 120n,       // 1.2x
            minLiquidityAmount: 110n,     // 1.1x
            allowsDividends: false,
            reportingFrequencyDays: 90n,  // quarterly
        });
        await covenantsTx.wait();
        console.log("   ✅ Covenants set");
    } else {
        console.log("5. Covenants already set, skipping");
    }
    
    // 6. Set loan tier
    if (!tierAlreadySet) {
        console.log("6. Setting loan tier...");
        const tierTx = await creditPolicy.setLoanTier(POLICY_VERSION, 1, {
            name: "Tier 1 - Small Business",
            minRevenue: tier.min_revenue,
            maxRevenue: tier.max_revenue,
            minEBITDA: tier.min_ebitda,
            maxDebtToEBITDA: tier.max_debt_to_ebitda,
            maxLoanToEBITDA: tier.max_loan_to_ebitda,
            interestRateBps: tier.interest_rate,
            originationFeeBps: tier.origination_fee,
            termDays: tier.term,
            active: tier.active,
        });
        await tierTx.wait();
        console.log("   ✅ Loan tier set");
    } else {
        console.log("6. Loan tier already set, skipping");
    }
    
    // 7. Set policy document
    const docHash = ethers.keccak256(ethers.toUtf8Bytes("policy_document_v2"));
    if (docHashAlready === ethers.ZeroHash) {
        console.log("7. Setting policy document...");
        const docTx = await creditPolicy.setPolicyDocument(POLICY_VERSION, docHash, "https://example.com/policy/v2");
        await docTx.wait();
        console.log("   ✅ Policy document set");
    } else {
        console.log("7. Policy document already set, skipping");
    }
    
    // 8. Set policy scope hash (the Poseidon hash!)
    if (scopeHashAlready === ethers.ZeroHash) {
        console.log("8. Setting policy scope hash...");
        const scopeTx = await creditPolicy.setPolicyScopeHash(POLICY_VERSION, policyHashHex);
        await scopeTx.wait();
        console.log(`   ✅ Policy scope hash set: ${policyHashHex}`);
    } else {
        console.log(`8. Policy scope hash already set: ${scopeHashAlready}`);
    }
    
    // 9. Freeze policy
    console.log("9. Freezing policy...");
    const freezeTx = await creditPolicy.freezePolicy(POLICY_VERSION);
    await freezeTx.wait();
    console.log("   ✅ Policy frozen");
    
    // Verify
    console.log("\n--- Verification ---");
    const finalScopeHash = await creditPolicy.policyScopeHash(POLICY_VERSION);
    console.log(`On-chain policyScopeHash: ${finalScopeHash}`);
    console.log(`Expected:                 ${policyHashHex}`);
    console.log(`Match: ${finalScopeHash.toLowerCase() === policyHashHex.toLowerCase()}`);
    
    console.log("\n✅ Policy v2 setup complete!");
}

main().catch(console.error);
