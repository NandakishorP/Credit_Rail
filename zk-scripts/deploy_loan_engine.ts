import { ethers } from "ethers";
import fs from "fs";
import path from "path";

const RPC_URL = "http://127.0.0.1:8546";
const PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";

// Deployed contract addresses
const CREDIT_POLICY = "0x22D151A1313d9B517Fa437F1F5B3744E636D8790";
const VERIFIER = "0x6B828bcb33305478cd7d27eB323F5C5B7b4aFdbe";
const TRANCHE_POOL = "0xd7385ba726A7b72933E63FCb0Dfee8Bcae63478c";
const USDC = "0x82778c3185fD0666d3f34F8930B4287405D9fBe4";
const POSEIDON2 = "0x1B69c60F3ac12BC305C96D927573102f6617eb16";

// Load LoanEngine bytecode from zksolc output
const loanEngineArtifact = JSON.parse(
  fs.readFileSync(
    path.join(__dirname, "../contracts/zkout/LoanEngine.sol/LoanEngine.json"),
    "utf-8"
  )
);

async function main() {
  const provider = new ethers.JsonRpcProvider(RPC_URL);
  const signer = new ethers.Wallet(PRIVATE_KEY, provider);
  
  console.log("Deploying LoanEngine with real Poseidon2...");
  console.log("  CreditPolicy:", CREDIT_POLICY);
  console.log("  Verifier:", VERIFIER);
  console.log("  TranchePool:", TRANCHE_POOL);
  console.log("  USDC:", USDC);
  console.log("  Poseidon2:", POSEIDON2);
  
  const factory = new ethers.ContractFactory(
    loanEngineArtifact.abi,
    loanEngineArtifact.bytecode.object,
    signer
  );
  
  const loanEngine = await factory.deploy(
    CREDIT_POLICY,
    VERIFIER,
    500, // maxOriginationFeeBps
    TRANCHE_POOL,
    USDC,
    POSEIDON2
  );
  
  await loanEngine.waitForDeployment();
  const address = await loanEngine.getAddress();
  console.log("\n✅ LoanEngine deployed at:", address);
  
  // Update .env.deployed
  const envPath = path.join(__dirname, ".env.deployed");
  let envContent = fs.readFileSync(envPath, "utf-8");
  envContent = envContent.replace(/LOAN_ENGINE=.*/, `LOAN_ENGINE=${address}`);
  envContent = envContent.replace(/POSEIDON=.*/, `POSEIDON=${POSEIDON2}`);
  fs.writeFileSync(envPath, envContent);
  console.log("Updated .env.deployed");
}

main().catch(console.error);
