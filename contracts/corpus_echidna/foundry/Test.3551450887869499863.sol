// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "forge-std/Test.sol";

contract FoundryTest is Test {
    address constant USER1 = address(0x10000);

    // TODO: Replace with your actual contract instance
    EchidnaTest Target;

  function setUp() public {
      // TODO: Initialize your contract here
      Target = new EchidnaTest();
  }

  function test_replay() public {
        _setUpActor(USER1);
        Target.commitPool();
        _setUpActor(USER1);
        Target.createLoan(0, 0, 0);
        _setUpActor(USER1);
        Target.activateLoan(0);
        _delay(0x1, 0x1);
    _setUpActor(USER1);
        Target.repayLoan(0, 2550350574773906, 0);
        _setUpActor(USER1);
        Target.declareDefault(0);
        _setUpActor(USER1);
        Target.writeOffLoan(0);
        _setUpActor(USER1);
        Target.recoverLoan(0, 1003178549270217343675026);
        _setUpActor(USER1);
        Target.createLoan(0, 0, 0);
        _setUpActor(USER1);
        Target.activateLoan(1);
        _setUpActor(USER1);
        Target.declareDefault(1);
        _setUpActor(USER1);
        Target.writeOffLoan(1);
  }

  function _setUpActor(address actor) internal {
      vm.startPrank(actor);
      // Add any additional actor setup here if needed
  }

  function _delay(uint256 timeInSeconds, uint256 numBlocks) internal {
      vm.warp(block.timestamp + timeInSeconds);
      vm.roll(block.number + numBlocks);
  }
}
