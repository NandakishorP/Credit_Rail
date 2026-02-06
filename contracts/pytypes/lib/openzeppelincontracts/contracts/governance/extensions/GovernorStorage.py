
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.governance.Governor import Governor



class GovernorStorage(Governor):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#17)
    """
    _abi = {b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'q\xc6\xafI': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorAlreadyCastVote', 'type': 'error'}, b'\xf2\x0e}7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorAlreadyQueuedProposal', 'type': 'error'}, b'\xe9\ne\x1e': {'inputs': [], 'name': 'GovernorDisabledDeposit', 'type': 'error'}, b'\xc2B\xee\x16': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'votes', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'threshold', 'type': 'uint256'}], 'name': 'GovernorInsufficientProposerVotes', 'type': 'error'}, b'D{\x05\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'targets', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'calldatas', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'values', 'type': 'uint256'}], 'name': 'GovernorInvalidProposalLength', 'type': 'error'}, b'\x94\xabl\x07': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorInvalidSignature', 'type': 'error'}, b'\x86}\xb7q': {'inputs': [], 'name': 'GovernorInvalidVoteParams', 'type': 'error'}, b'\x06\xb37\xc2': {'inputs': [], 'name': 'GovernorInvalidVoteType', 'type': 'error'}, b'\xf1\xcf\xbf\x05': {'inputs': [{'internalType': 'uint256', 'name': 'votingPeriod', 'type': 'uint256'}], 'name': 'GovernorInvalidVotingPeriod', 'type': 'error'}, b'j\xd0`u': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNonexistentProposal', 'type': 'error'}, b'\xd5\xdd\xb8%': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNotQueuedProposal', 'type': 'error'}, b'G\tnG': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorOnlyExecutor', 'type': 'error'}, b'\x90\x88JF': {'inputs': [], 'name': 'GovernorQueueNotImplemented', 'type': 'error'}, b'\xd9\xb3\x95W': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}], 'name': 'GovernorRestrictedProposer', 'type': 'error'}, b'\x8f\xe5\xd8\xa9': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorUnableToCancel', 'type': 'error'}, b'1\xb7^M': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'enum IGovernor.ProposalState', 'name': 'current', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'expectedStates', 'type': 'bytes32'}], 'name': 'GovernorUnexpectedProposalState', 'type': 'error'}, b'u-\x88\xc0': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentNonce', 'type': 'uint256'}], 'name': 'InvalidAccountNonce', 'type': 'error'}, b'\xb3Q+\x0c': {'inputs': [], 'name': 'InvalidShortString', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b"0Z'\xa9": {'inputs': [{'internalType': 'string', 'name': 'str', 'type': 'string'}], 'name': 'StringTooLong', 'type': 'error'}, b'\nc\x87\xc9\xea6(\xb8\x8ac;\xb4\xf3\xb1Qw\x0fp\x08Q\x17\xa1_\x9b\xf3x|\xdaS\xf1=1': {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, b'x\x9c\xf5[\xe9\x80s\x9d\xad\x1d\x06\x99\xb9;X\xe8\x06\xb5\x1c\x9d\x96a\x9b\xfa\x8f\xe0\xa2\x8a\xba\xa7\xb3\x0c': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalCanceled', 'type': 'event'}, b"}\x84\xa6&:\xe0\xd9\x8d3)\xbd{F\xbbN\x8do\x98\xcd5\xa7\xad\xb4\\'L\x8b\x7f\xd5\xeb\xd5\xe0": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'indexed': False, 'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'string[]', 'name': 'signatures', 'type': 'string[]'}, {'indexed': False, 'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteStart', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteEnd', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'ProposalCreated', 'type': 'event'}, b'q*\xe18?y\xac\x85?\x8d\x88!Sw\x8e\x02`\xef\x8f\x03\xb5\x04\xe2\x86n\x05\x93\xe0M+)\x1f': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalExecuted', 'type': 'event'}, b'\x9a.B\xfdg"\x81=i\x11>}\x00y\xd3\xd9@\x17\x14(\xdfss\xdf\x9c\x7fv\x17\xcf\xda(\x92': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'etaSeconds', 'type': 'uint256'}], 'name': 'ProposalQueued', 'type': 'event'}, b'\xb8\xe18\x88}\n\xa1;\xabD~\x82\xde\x9d\\\x17w\x04\x1e\xcd!\xca6\xba\x82O\xf1\xe6\xc0}\xdd\xa4': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'VoteCast', 'type': 'event'}, b'\xe2\xba\xbf\xba\xc5\x88\x9ap\x9bc\xbb\x7fY\x8b2N\x08\xbcZO\xb9\xecd\x7f\xb3\xcb\xc9\xec\x07\xeb\x87\x12': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'VoteCastWithParams', 'type': 'event'}, b'\xde\xaa\xa7\xcc': {'inputs': [], 'name': 'BALLOT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'K\xf5\xd7\xe9': {'inputs': [], 'name': 'CLOCK_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddN+\xa5': {'inputs': [], 'name': 'COUNTING_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'/\xe3\xe2a': {'inputs': [], 'name': 'EXTENDED_BALLOT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'@\xe5\x8e\xe5': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'cancel', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'E!\x15\xd6': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'cancel', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Vx\x13\x88': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}], 'name': 'castVote', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8f\xf2b\xe3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteBySig', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'{<q\xd3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'castVoteWithReason', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_9\x8a\x14': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParams', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'[\x8d\x0e\r': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParamsBySig', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xdd\xad\xf4': {'inputs': [], 'name': 'clock', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'\x84\xb0\x19n': {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, b'&V"}': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'execute', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xfe\r\x94\xc1': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xa8\xf8\xa6h': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'getProposalId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xeb\x90\x19\xd4': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'getVotes', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9a\x80*m': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'getVotesWithParams', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'C\x85\x962': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasVoted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\x90W\xe4': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'hashProposal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbc\x19|\x81': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC1155BatchReceived', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2:na': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC1155Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x15\x0bz\x02': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'onERC721Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xda5\xc6d': {'inputs': [], 'name': 'proposalCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc0\x1f\x9e7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalDeadline', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x16\xe9\xea\xec': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalDetails', 'outputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'.\x82\xdb\x94': {'inputs': [{'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'proposalDetailsAt', 'outputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xabX\xfb\x8e': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalEta', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\xa9R\x94': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'proposalNeedsQueuing', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x144\x89\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalProposer', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'-c\xf6\x93': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalSnapshot', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5\x811\xb0': {'inputs': [], 'name': 'proposalThreshold', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'}^\x81\xe2': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'propose', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16\x0c\xbe\xd7': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'queue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdd\xf0\xb0\t': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'queue', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8\xceV\n': {'inputs': [{'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'quorum', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc2\x8b\xc2\xfa': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'relay', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'>OI\xe6': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'state', 'outputs': [{'internalType': 'enum IGovernor.ProposalState', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'T\xfdMP': {'inputs': [], 'name': 'version', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'92\xab\xb1': {'inputs': [], 'name': 'votingDelay', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x02\xa2Q\xa3': {'inputs': [], 'name': 'votingPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, 'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[{"astId":9349,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_nameFallback","offset":0,"slot":0,"type":"t_string_storage"},{"astId":9351,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_versionFallback","offset":0,"slot":1,"type":"t_string_storage"},{"astId":6926,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_nonces","offset":0,"slot":2,"type":"t_mapping(t_address,t_uint256)"},{"astId":471,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_name","offset":0,"slot":3,"type":"t_string_storage"},{"astId":476,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_proposals","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_struct(ProposalCore)449_storage)"},{"astId":479,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_governanceCall","offset":0,"slot":5,"type":"t_struct(Bytes32Deque)15657_storage"},{"astId":4165,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_proposalIds","offset":0,"slot":7,"type":"t_array(t_uint256)dyn_storage"},{"astId":4170,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_proposalDetails","offset":0,"slot":8,"type":"t_mapping(t_uint256,t_struct(ProposalDetails)4162_storage)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes_storage)dyn_storage":{"encoding":"dynamic_array","label":"bytes[]","numberOfBytes":32,"base":"t_bytes_storage"},"t_array(t_uint256)dyn_storage":{"encoding":"dynamic_array","label":"uint256[]","numberOfBytes":32,"base":"t_uint256"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint128,t_bytes32)":{"encoding":"mapping","label":"mapping(uint128 => bytes32)","numberOfBytes":32,"key":"t_uint128","value":"t_bytes32"},"t_mapping(t_uint256,t_struct(ProposalCore)449_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct Governor.ProposalCore)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(ProposalCore)449_storage"},"t_mapping(t_uint256,t_struct(ProposalDetails)4162_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct GovernorStorage.ProposalDetails)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(ProposalDetails)4162_storage"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Bytes32Deque)15657_storage":{"encoding":"inplace","label":"struct DoubleEndedQueue.Bytes32Deque","numberOfBytes":64,"members":[{"astId":15650,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_begin","offset":0,"slot":0,"type":"t_uint128"},{"astId":15652,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_end","offset":16,"slot":0,"type":"t_uint128"},{"astId":15656,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"_data","offset":0,"slot":1,"type":"t_mapping(t_uint128,t_bytes32)"}]},"t_struct(ProposalCore)449_storage":{"encoding":"inplace","label":"struct Governor.ProposalCore","numberOfBytes":64,"members":[{"astId":438,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"proposer","offset":0,"slot":0,"type":"t_address"},{"astId":440,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"voteStart","offset":20,"slot":0,"type":"t_uint48"},{"astId":442,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"voteDuration","offset":26,"slot":0,"type":"t_uint32"},{"astId":444,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"executed","offset":30,"slot":0,"type":"t_bool"},{"astId":446,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"canceled","offset":31,"slot":0,"type":"t_bool"},{"astId":448,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"etaSeconds","offset":0,"slot":1,"type":"t_uint48"}]},"t_struct(ProposalDetails)4162_storage":{"encoding":"inplace","label":"struct GovernorStorage.ProposalDetails","numberOfBytes":128,"members":[{"astId":4153,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"targets","offset":0,"slot":0,"type":"t_array(t_address)dyn_storage"},{"astId":4156,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"values","offset":0,"slot":1,"type":"t_array(t_uint256)dyn_storage"},{"astId":4159,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"calldatas","offset":0,"slot":2,"type":"t_array(t_bytes_storage)dyn_storage"},{"astId":4161,"contract":"lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol:GovernorStorage","label":"descriptionHash","offset":0,"slot":3,"type":"t_bytes32"}]},"t_uint128":{"encoding":"inplace","label":"uint128","numberOfBytes":16},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint32":{"encoding":"inplace","label":"uint32","numberOfBytes":4},"t_uint48":{"encoding":"inplace","label":"uint48","numberOfBytes":6}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> GovernorStorage:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[GovernorStorage]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, GovernorStorage, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[GovernorStorage]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class ProposalDetails:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#18)

        Attributes:
            targets (List[Address]): address[]
            values (List[uint256]): uint256[]
            calldatas (List[bytearray]): bytes[]
            descriptionHash (bytes32): bytes32
        """
        original_name = 'ProposalDetails'

        targets: List[Address]
        values: List[uint256]
        calldatas: List[bytearray]
        descriptionHash: bytes32


    @overload
    def queue_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#55)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def queue_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#55)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def queue_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#55)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def queue_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#55)

        Args:
            proposalId: uint256
        """
        ...

    def queue_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#55)

        Args:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "ddf0b009", [proposalId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def execute_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#64)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def execute_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#64)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def execute_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#64)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def execute_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#64)

        Args:
            proposalId: uint256
        """
        ...

    def execute_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#64)

        Args:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "fe0d94c1", [proposalId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def cancel_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#73)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def cancel_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#73)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def cancel_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#73)

        Args:
            proposalId: uint256
        """
        ...

    @overload
    def cancel_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#73)

        Args:
            proposalId: uint256
        """
        ...

    def cancel_(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#73)

        Args:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "40e58ee5", [proposalId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#82)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#82)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#82)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#82)

        Returns:
            uint256
        """
        ...

    def proposalCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#82)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "da35c664", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalDetails(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[List[Address], List[uint256], List[bytearray], bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#89)

        Args:
            proposalId: uint256
        Returns:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetails(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#89)

        Args:
            proposalId: uint256
        Returns:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetails(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#89)

        Args:
            proposalId: uint256
        Returns:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetails(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[List[Address], List[uint256], List[bytearray], bytes32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#89)

        Args:
            proposalId: uint256
        Returns:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    def proposalDetails(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[List[Address], List[uint256], List[bytearray], bytes32], TransactionAbc[Tuple[List[Address], List[uint256], List[bytearray], bytes32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#89)

        Args:
            proposalId: uint256
        Returns:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        return self._execute(self.chain, request_type, "16e9eaec", [proposalId], True if request_type == "tx" else False, Tuple[List[Address], List[uint256], List[bytearray], bytes32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalDetailsAt(self, index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint256, List[Address], List[uint256], List[bytearray], bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#108)

        Args:
            index: uint256
        Returns:
            proposalId: uint256
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetailsAt(self, index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#108)

        Args:
            index: uint256
        Returns:
            proposalId: uint256
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetailsAt(self, index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#108)

        Args:
            index: uint256
        Returns:
            proposalId: uint256
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    @overload
    def proposalDetailsAt(self, index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint256, List[Address], List[uint256], List[bytearray], bytes32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#108)

        Args:
            index: uint256
        Returns:
            proposalId: uint256
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        ...

    def proposalDetailsAt(self, index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint256, List[Address], List[uint256], List[bytearray], bytes32], TransactionAbc[Tuple[uint256, List[Address], List[uint256], List[bytearray], bytes32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/extensions/GovernorStorage.sol#108)

        Args:
            index: uint256
        Returns:
            proposalId: uint256
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        """
        return self._execute(self.chain, request_type, "2e82db94", [index], True if request_type == "tx" else False, Tuple[uint256, List[Address], List[uint256], List[bytearray], bytes32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

GovernorStorage.queue_.selector = bytes4(b'\xdd\xf0\xb0\t')
GovernorStorage.execute_.selector = bytes4(b'\xfe\r\x94\xc1')
GovernorStorage.cancel_.selector = bytes4(b'@\xe5\x8e\xe5')
GovernorStorage.proposalCount.selector = bytes4(b'\xda5\xc6d')
GovernorStorage.proposalDetails.selector = bytes4(b'\x16\xe9\xea\xec')
GovernorStorage.proposalDetailsAt.selector = bytes4(b'.\x82\xdb\x94')
