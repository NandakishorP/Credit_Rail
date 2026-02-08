// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {TimelockController} from "@openzeppelin/contracts/governance/TimelockController.sol";

/**
 * @title ProtocolController
 * @notice Timelock controller for protocol governance with multisig integration
 * @dev Uses OpenZeppelin's battle-tested TimelockController
 * 
 * Architecture:
 * - Deploy a Safe (Gnosis Safe) multisig separately
 * - Pass the Safe address as both proposer and executor
 * - This contract enforces a time delay on all admin operations
 * 
 * Flow:
 * 1. Multisig proposes a transaction (schedule)
 * 2. Timelock delay passes (e.g., 48 hours)
 * 3. Multisig executes the transaction
 * 
 * Usage:
 * - Set this contract as the owner of LoanEngine, CreditPolicy, TranchePool
 * - All admin functions will require multisig + timelock
 */
contract ProtocolController is TimelockController {
    /**
     * @notice Initialize the protocol controller with timelock + multisig
     * @param minDelay Minimum delay in seconds for operations (e.g., 172800 = 48 hours)
     * @param multisig Address of the Safe multisig (proposer + executor)
     * @param guardian Optional address that can cancel operations (set to address(0) to disable)
     */
    constructor(
        uint256 minDelay,
        address multisig,
        address guardian
    )
        TimelockController(
            minDelay,
            _toArray(multisig),      
            _toArray(multisig),      
            guardian                  
        )
    {}

    /**
     * @dev Helper to convert single address to array for constructor
     */
    function _toArray(address addr) private pure returns (address[] memory) {
        address[] memory arr = new address[](1);
        arr[0] = addr;
        return arr;
    }
}