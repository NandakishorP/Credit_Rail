
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.governance.Governor import Governor
from pytypes.lib.openzeppelincontracts.contracts.governance.IGovernor import IGovernor
from pytypes.lib.openzeppelincontracts.contracts.vendor.compound.ICompoundTimelock import ICompoundTimelock



class GovernorTimelockCompound(Governor):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#21)
    """
    _abi = {b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'q\xc6\xafI': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorAlreadyCastVote', 'type': 'error'}, b'\xf2\x0e}7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorAlreadyQueuedProposal', 'type': 'error'}, b'\xe9\ne\x1e': {'inputs': [], 'name': 'GovernorDisabledDeposit', 'type': 'error'}, b'\xc2B\xee\x16': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'votes', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'threshold', 'type': 'uint256'}], 'name': 'GovernorInsufficientProposerVotes', 'type': 'error'}, b'D{\x05\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'targets', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'calldatas', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'values', 'type': 'uint256'}], 'name': 'GovernorInvalidProposalLength', 'type': 'error'}, b'\x94\xabl\x07': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorInvalidSignature', 'type': 'error'}, b'\x86}\xb7q': {'inputs': [], 'name': 'GovernorInvalidVoteParams', 'type': 'error'}, b'\x06\xb37\xc2': {'inputs': [], 'name': 'GovernorInvalidVoteType', 'type': 'error'}, b'\xf1\xcf\xbf\x05': {'inputs': [{'internalType': 'uint256', 'name': 'votingPeriod', 'type': 'uint256'}], 'name': 'GovernorInvalidVotingPeriod', 'type': 'error'}, b'j\xd0`u': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNonexistentProposal', 'type': 'error'}, b'\xd5\xdd\xb8%': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNotQueuedProposal', 'type': 'error'}, b'G\tnG': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorOnlyExecutor', 'type': 'error'}, b'\x90\x88JF': {'inputs': [], 'name': 'GovernorQueueNotImplemented', 'type': 'error'}, b'\xd9\xb3\x95W': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}], 'name': 'GovernorRestrictedProposer', 'type': 'error'}, b'\x8f\xe5\xd8\xa9': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorUnableToCancel', 'type': 'error'}, b'1\xb7^M': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'enum IGovernor.ProposalState', 'name': 'current', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'expectedStates', 'type': 'bytes32'}], 'name': 'GovernorUnexpectedProposalState', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'u-\x88\xc0': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentNonce', 'type': 'uint256'}], 'name': 'InvalidAccountNonce', 'type': 'error'}, b'\xb3Q+\x0c': {'inputs': [], 'name': 'InvalidShortString', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b"0Z'\xa9": {'inputs': [{'internalType': 'string', 'name': 'str', 'type': 'string'}], 'name': 'StringTooLong', 'type': 'error'}, b'\nc\x87\xc9\xea6(\xb8\x8ac;\xb4\xf3\xb1Qw\x0fp\x08Q\x17\xa1_\x9b\xf3x|\xdaS\xf1=1': {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, b'x\x9c\xf5[\xe9\x80s\x9d\xad\x1d\x06\x99\xb9;X\xe8\x06\xb5\x1c\x9d\x96a\x9b\xfa\x8f\xe0\xa2\x8a\xba\xa7\xb3\x0c': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalCanceled', 'type': 'event'}, b"}\x84\xa6&:\xe0\xd9\x8d3)\xbd{F\xbbN\x8do\x98\xcd5\xa7\xad\xb4\\'L\x8b\x7f\xd5\xeb\xd5\xe0": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'indexed': False, 'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'string[]', 'name': 'signatures', 'type': 'string[]'}, {'indexed': False, 'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteStart', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteEnd', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'ProposalCreated', 'type': 'event'}, b'q*\xe18?y\xac\x85?\x8d\x88!Sw\x8e\x02`\xef\x8f\x03\xb5\x04\xe2\x86n\x05\x93\xe0M+)\x1f': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalExecuted', 'type': 'event'}, b'\x9a.B\xfdg"\x81=i\x11>}\x00y\xd3\xd9@\x17\x14(\xdfss\xdf\x9c\x7fv\x17\xcf\xda(\x92': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'etaSeconds', 'type': 'uint256'}], 'name': 'ProposalQueued', 'type': 'event'}, b'\x08\xf7N\xa4n\xf7\x89Oe\xea\xbf\xb5\xe6\xe6\x95\xdew:\x00\x0bG\xc5)\xabU\x91x\x06\x9b"d\x01': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'oldTimelock', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newTimelock', 'type': 'address'}], 'name': 'TimelockChange', 'type': 'event'}, b'\xb8\xe18\x88}\n\xa1;\xabD~\x82\xde\x9d\\\x17w\x04\x1e\xcd!\xca6\xba\x82O\xf1\xe6\xc0}\xdd\xa4': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'VoteCast', 'type': 'event'}, b'\xe2\xba\xbf\xba\xc5\x88\x9ap\x9bc\xbb\x7fY\x8b2N\x08\xbcZO\xb9\xecd\x7f\xb3\xcb\xc9\xec\x07\xeb\x87\x12': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'VoteCastWithParams', 'type': 'event'}, b'\xde\xaa\xa7\xcc': {'inputs': [], 'name': 'BALLOT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'K\xf5\xd7\xe9': {'inputs': [], 'name': 'CLOCK_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddN+\xa5': {'inputs': [], 'name': 'COUNTING_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'/\xe3\xe2a': {'inputs': [], 'name': 'EXTENDED_BALLOT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb9\xa6\x19a': {'inputs': [], 'name': '__acceptAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'E!\x15\xd6': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'cancel', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Vx\x13\x88': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}], 'name': 'castVote', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8f\xf2b\xe3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteBySig', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'{<q\xd3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'castVoteWithReason', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_9\x8a\x14': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParams', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'[\x8d\x0e\r': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParamsBySig', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xdd\xad\xf4': {'inputs': [], 'name': 'clock', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'\x84\xb0\x19n': {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, b'&V"}': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'execute', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xa8\xf8\xa6h': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'getProposalId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xeb\x90\x19\xd4': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'getVotes', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9a\x80*m': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'getVotesWithParams', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'C\x85\x962': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasVoted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\x90W\xe4': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'hashProposal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbc\x19|\x81': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC1155BatchReceived', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2:na': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC1155Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x15\x0bz\x02': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC721Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc0\x1f\x9e7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalDeadline', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xabX\xfb\x8e': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalEta', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\xa9R\x94': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'proposalNeedsQueuing', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x144\x89\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalProposer', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'-c\xf6\x93': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalSnapshot', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5\x811\xb0': {'inputs': [], 'name': 'proposalThreshold', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'}^\x81\xe2': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'propose', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16\x0c\xbe\xd7': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'queue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8\xceV\n': {'inputs': [{'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'quorum', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc2\x8b\xc2\xfa': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'relay', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'>OI\xe6': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'state', 'outputs': [{'internalType': 'enum IGovernor.ProposalState', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd32\x19\xb4': {'inputs': [], 'name': 'timelock', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa8\x90\xc9\x10': {'inputs': [{'internalType': 'contract ICompoundTimelock', 'name': 'newTimelock', 'type': 'address'}], 'name': 'updateTimelock', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'T\xfdMP': {'inputs': [], 'name': 'version', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'92\xab\xb1': {'inputs': [], 'name': 'votingDelay', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x02\xa2Q\xa3': {'inputs': [], 'name': 'votingPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, 'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[{"astId":7605,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_nameFallback","offset":0,"slot":0,"type":"t_string_storage"},{"astId":7607,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_versionFallback","offset":0,"slot":1,"type":"t_string_storage"},{"astId":5182,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_nonces","offset":0,"slot":2,"type":"t_mapping(t_address,t_uint256)"},{"astId":91,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_name","offset":0,"slot":3,"type":"t_string_storage"},{"astId":96,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_proposals","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_struct(ProposalCore)69_storage)"},{"astId":99,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_governanceCall","offset":0,"slot":5,"type":"t_struct(Bytes32Deque)13913_storage"},{"astId":2758,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_timelock","offset":0,"slot":7,"type":"t_contract(ICompoundTimelock)14681"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_contract(ICompoundTimelock)14681":{"encoding":"inplace","label":"contract ICompoundTimelock","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint128,t_bytes32)":{"encoding":"mapping","label":"mapping(uint128 => bytes32)","numberOfBytes":32,"key":"t_uint128","value":"t_bytes32"},"t_mapping(t_uint256,t_struct(ProposalCore)69_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct Governor.ProposalCore)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(ProposalCore)69_storage"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Bytes32Deque)13913_storage":{"encoding":"inplace","label":"struct DoubleEndedQueue.Bytes32Deque","numberOfBytes":64,"members":[{"astId":13906,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_begin","offset":0,"slot":0,"type":"t_uint128"},{"astId":13908,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_end","offset":16,"slot":0,"type":"t_uint128"},{"astId":13912,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"_data","offset":0,"slot":1,"type":"t_mapping(t_uint128,t_bytes32)"}]},"t_struct(ProposalCore)69_storage":{"encoding":"inplace","label":"struct Governor.ProposalCore","numberOfBytes":64,"members":[{"astId":58,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"proposer","offset":0,"slot":0,"type":"t_address"},{"astId":60,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"voteStart","offset":20,"slot":0,"type":"t_uint48"},{"astId":62,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"voteDuration","offset":26,"slot":0,"type":"t_uint32"},{"astId":64,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"executed","offset":30,"slot":0,"type":"t_bool"},{"astId":66,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"canceled","offset":31,"slot":0,"type":"t_bool"},{"astId":68,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol:GovernorTimelockCompound","label":"etaSeconds","offset":0,"slot":1,"type":"t_uint48"}]},"t_uint128":{"encoding":"inplace","label":"uint128","numberOfBytes":16},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint32":{"encoding":"inplace","label":"uint32","numberOfBytes":4},"t_uint48":{"encoding":"inplace","label":"uint48","numberOfBytes":6}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> GovernorTimelockCompound:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[GovernorTimelockCompound]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        ...

    @classmethod
    def deploy(cls, timelockAddress: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, GovernorTimelockCompound, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[GovernorTimelockCompound]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#32)

        Args:
            timelockAddress: contract ICompoundTimelock
        """
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class TimelockChange:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#27)

        Attributes:
            oldTimelock (Address): address
            newTimelock (Address): address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'oldTimelock', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newTimelock', 'type': 'address'}], 'name': 'TimelockChange', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TimelockChange'
        selector = bytes32(b'\x08\xf7N\xa4n\xf7\x89Oe\xea\xbf\xb5\xe6\xe6\x95\xdew:\x00\x0bG\xc5)\xabU\x91x\x06\x9b"d\x01')

        oldTimelock: Address
        newTimelock: Address


    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IGovernor.ProposalState:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#39)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#39)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#39)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IGovernor.ProposalState]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#39)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IGovernor.ProposalState, TransactionAbc[IGovernor.ProposalState], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#39)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        return self._execute(self.chain, request_type, "3e4f49e6", [proposalId], True if request_type == "tx" else False, IGovernor.ProposalState, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def timelock(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#52)

        Returns:
            address
        """
        ...

    @overload
    def timelock(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#52)

        Returns:
            address
        """
        ...

    @overload
    def timelock(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#52)

        Returns:
            address
        """
        ...

    @overload
    def timelock(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#52)

        Returns:
            address
        """
        ...

    def timelock(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#52)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "d33219b4", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalNeedsQueuing(self, arg1: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#57)

        Args:
            arg1: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, arg1: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#57)

        Args:
            arg1: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, arg1: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#57)

        Args:
            arg1: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, arg1: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#57)

        Args:
            arg1: uint256
        Returns:
            bool
        """
        ...

    def proposalNeedsQueuing(self, arg1: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#57)

        Args:
            arg1: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "a9a95294", [arg1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def _acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#140)
        """
        ...

    @overload
    def _acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#140)
        """
        ...

    @overload
    def _acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#140)
        """
        ...

    @overload
    def _acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#140)
        """
        ...

    def _acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#140)
        """
        return self._execute(self.chain, request_type, "b9a61961", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateTimelock(self, newTimelock: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#157)

        Args:
            newTimelock: contract ICompoundTimelock
        """
        ...

    @overload
    def updateTimelock(self, newTimelock: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#157)

        Args:
            newTimelock: contract ICompoundTimelock
        """
        ...

    @overload
    def updateTimelock(self, newTimelock: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#157)

        Args:
            newTimelock: contract ICompoundTimelock
        """
        ...

    @overload
    def updateTimelock(self, newTimelock: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#157)

        Args:
            newTimelock: contract ICompoundTimelock
        """
        ...

    def updateTimelock(self, newTimelock: ICompoundTimelock, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorTimelockCompound.sol#157)

        Args:
            newTimelock: contract ICompoundTimelock
        """
        return self._execute(self.chain, request_type, "a890c910", [newTimelock], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

GovernorTimelockCompound.state.selector = bytes4(b'>OI\xe6')
GovernorTimelockCompound.timelock.selector = bytes4(b'\xd32\x19\xb4')
GovernorTimelockCompound.proposalNeedsQueuing.selector = bytes4(b'\xa9\xa9R\x94')
GovernorTimelockCompound._acceptAdmin.selector = bytes4(b'\xb9\xa6\x19a')
GovernorTimelockCompound.updateTimelock.selector = bytes4(b'\xa8\x90\xc9\x10')
