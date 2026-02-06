
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC6372 import IERC6372
from pytypes.lib.openzeppelincontracts.contracts.utils.introspection.IERC165 import IERC165



class IGovernor(IERC6372, IERC165):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#15)
    """
    _abi = {b'q\xc6\xafI': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorAlreadyCastVote', 'type': 'error'}, b'\xf2\x0e}7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorAlreadyQueuedProposal', 'type': 'error'}, b'\xe9\ne\x1e': {'inputs': [], 'name': 'GovernorDisabledDeposit', 'type': 'error'}, b'\xc2B\xee\x16': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'votes', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'threshold', 'type': 'uint256'}], 'name': 'GovernorInsufficientProposerVotes', 'type': 'error'}, b'D{\x05\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'targets', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'calldatas', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'values', 'type': 'uint256'}], 'name': 'GovernorInvalidProposalLength', 'type': 'error'}, b'\x94\xabl\x07': {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorInvalidSignature', 'type': 'error'}, b'\x86}\xb7q': {'inputs': [], 'name': 'GovernorInvalidVoteParams', 'type': 'error'}, b'\x06\xb37\xc2': {'inputs': [], 'name': 'GovernorInvalidVoteType', 'type': 'error'}, b'\xf1\xcf\xbf\x05': {'inputs': [{'internalType': 'uint256', 'name': 'votingPeriod', 'type': 'uint256'}], 'name': 'GovernorInvalidVotingPeriod', 'type': 'error'}, b'j\xd0`u': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNonexistentProposal', 'type': 'error'}, b'\xd5\xdd\xb8%': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNotQueuedProposal', 'type': 'error'}, b'G\tnG': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorOnlyExecutor', 'type': 'error'}, b'\x90\x88JF': {'inputs': [], 'name': 'GovernorQueueNotImplemented', 'type': 'error'}, b'\xd9\xb3\x95W': {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}], 'name': 'GovernorRestrictedProposer', 'type': 'error'}, b'\x8f\xe5\xd8\xa9': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorUnableToCancel', 'type': 'error'}, b'1\xb7^M': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'enum IGovernor.ProposalState', 'name': 'current', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'expectedStates', 'type': 'bytes32'}], 'name': 'GovernorUnexpectedProposalState', 'type': 'error'}, b'x\x9c\xf5[\xe9\x80s\x9d\xad\x1d\x06\x99\xb9;X\xe8\x06\xb5\x1c\x9d\x96a\x9b\xfa\x8f\xe0\xa2\x8a\xba\xa7\xb3\x0c': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalCanceled', 'type': 'event'}, b"}\x84\xa6&:\xe0\xd9\x8d3)\xbd{F\xbbN\x8do\x98\xcd5\xa7\xad\xb4\\'L\x8b\x7f\xd5\xeb\xd5\xe0": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'indexed': False, 'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'string[]', 'name': 'signatures', 'type': 'string[]'}, {'indexed': False, 'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteStart', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteEnd', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'ProposalCreated', 'type': 'event'}, b'q*\xe18?y\xac\x85?\x8d\x88!Sw\x8e\x02`\xef\x8f\x03\xb5\x04\xe2\x86n\x05\x93\xe0M+)\x1f': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalExecuted', 'type': 'event'}, b'\x9a.B\xfdg"\x81=i\x11>}\x00y\xd3\xd9@\x17\x14(\xdfss\xdf\x9c\x7fv\x17\xcf\xda(\x92': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'etaSeconds', 'type': 'uint256'}], 'name': 'ProposalQueued', 'type': 'event'}, b'\xb8\xe18\x88}\n\xa1;\xabD~\x82\xde\x9d\\\x17w\x04\x1e\xcd!\xca6\xba\x82O\xf1\xe6\xc0}\xdd\xa4': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'VoteCast', 'type': 'event'}, b'\xe2\xba\xbf\xba\xc5\x88\x9ap\x9bc\xbb\x7fY\x8b2N\x08\xbcZO\xb9\xecd\x7f\xb3\xcb\xc9\xec\x07\xeb\x87\x12': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'VoteCastWithParams', 'type': 'event'}, b'K\xf5\xd7\xe9': {'inputs': [], 'name': 'CLOCK_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddN+\xa5': {'inputs': [], 'name': 'COUNTING_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'E!\x15\xd6': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'cancel', 'outputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Vx\x13\x88': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}], 'name': 'castVote', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8f\xf2b\xe3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteBySig', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'{<q\xd3': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'castVoteWithReason', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_9\x8a\x14': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParams', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'[\x8d\x0e\r': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'castVoteWithReasonAndParamsBySig', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xdd\xad\xf4': {'inputs': [], 'name': 'clock', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'&V"}': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'execute', 'outputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xa8\xf8\xa6h': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'getProposalId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xeb\x90\x19\xd4': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'getVotes', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9a\x80*m': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'getVotesWithParams', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'C\x85\x962': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasVoted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\x90W\xe4': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'hashProposal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc0\x1f\x9e7': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalDeadline', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xabX\xfb\x8e': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalEta', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\xa9R\x94': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalNeedsQueuing', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x144\x89\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalProposer', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'-c\xf6\x93': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'proposalSnapshot', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5\x811\xb0': {'inputs': [], 'name': 'proposalThreshold', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'}^\x81\xe2': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'propose', 'outputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16\x0c\xbe\xd7': {'inputs': [{'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'internalType': 'bytes32', 'name': 'descriptionHash', 'type': 'bytes32'}], 'name': 'queue', 'outputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8\xceV\n': {'inputs': [{'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'quorum', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'>OI\xe6': {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'state', 'outputs': [{'internalType': 'enum IGovernor.ProposalState', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'T\xfdMP': {'inputs': [], 'name': 'version', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'92\xab\xb1': {'inputs': [], 'name': 'votingDelay', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x02\xa2Q\xa3': {'inputs': [], 'name': 'votingPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IGovernor:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IGovernor]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IGovernor, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IGovernor]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    class ProposalState(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#16)

        """
        Pending = 0
        Active = 1
        Canceled = 2
        Defeated = 3
        Succeeded = 4
        Queued = 5
        Expired = 6
        Executed = 7


    @dataclasses.dataclass
    class GovernorInvalidProposalLength(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#30)

        Attributes:
            targets (uint256): uint256
            calldatas (uint256): uint256
            values (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'targets', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'calldatas', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'values', 'type': 'uint256'}], 'name': 'GovernorInvalidProposalLength', 'type': 'error'}
        original_name = 'GovernorInvalidProposalLength'
        selector = bytes4(b'D{\x05\xd0')

        targets: uint256
        calldatas: uint256
        values: uint256


    @dataclasses.dataclass
    class GovernorAlreadyCastVote(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#35)

        Attributes:
            voter (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorAlreadyCastVote', 'type': 'error'}
        original_name = 'GovernorAlreadyCastVote'
        selector = bytes4(b'q\xc6\xafI')

        voter: Address


    @dataclasses.dataclass
    class GovernorDisabledDeposit(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#40)
        """
        _abi = {'inputs': [], 'name': 'GovernorDisabledDeposit', 'type': 'error'}
        original_name = 'GovernorDisabledDeposit'
        selector = bytes4(b'\xe9\ne\x1e')



    @dataclasses.dataclass
    class GovernorOnlyExecutor(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#45)

        Attributes:
            account (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorOnlyExecutor', 'type': 'error'}
        original_name = 'GovernorOnlyExecutor'
        selector = bytes4(b'G\tnG')

        account: Address


    @dataclasses.dataclass
    class GovernorNonexistentProposal(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#50)

        Attributes:
            proposalId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNonexistentProposal', 'type': 'error'}
        original_name = 'GovernorNonexistentProposal'
        selector = bytes4(b'j\xd0`u')

        proposalId: uint256


    @dataclasses.dataclass
    class GovernorUnexpectedProposalState(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#62)

        Attributes:
            proposalId (uint256): uint256
            current (IGovernor.ProposalState): enum IGovernor.ProposalState
            expectedStates (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'enum IGovernor.ProposalState', 'name': 'current', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'expectedStates', 'type': 'bytes32'}], 'name': 'GovernorUnexpectedProposalState', 'type': 'error'}
        original_name = 'GovernorUnexpectedProposalState'
        selector = bytes4(b'1\xb7^M')

        proposalId: uint256
        current: IGovernor.ProposalState
        expectedStates: bytes32


    @dataclasses.dataclass
    class GovernorInvalidVotingPeriod(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#67)

        Attributes:
            votingPeriod (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'votingPeriod', 'type': 'uint256'}], 'name': 'GovernorInvalidVotingPeriod', 'type': 'error'}
        original_name = 'GovernorInvalidVotingPeriod'
        selector = bytes4(b'\xf1\xcf\xbf\x05')

        votingPeriod: uint256


    @dataclasses.dataclass
    class GovernorInsufficientProposerVotes(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#72)

        Attributes:
            proposer (Address): address
            votes (uint256): uint256
            threshold (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'votes', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'threshold', 'type': 'uint256'}], 'name': 'GovernorInsufficientProposerVotes', 'type': 'error'}
        original_name = 'GovernorInsufficientProposerVotes'
        selector = bytes4(b'\xc2B\xee\x16')

        proposer: Address
        votes: uint256
        threshold: uint256


    @dataclasses.dataclass
    class GovernorRestrictedProposer(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#77)

        Attributes:
            proposer (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'proposer', 'type': 'address'}], 'name': 'GovernorRestrictedProposer', 'type': 'error'}
        original_name = 'GovernorRestrictedProposer'
        selector = bytes4(b'\xd9\xb3\x95W')

        proposer: Address


    @dataclasses.dataclass
    class GovernorInvalidVoteType(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#82)
        """
        _abi = {'inputs': [], 'name': 'GovernorInvalidVoteType', 'type': 'error'}
        original_name = 'GovernorInvalidVoteType'
        selector = bytes4(b'\x06\xb37\xc2')



    @dataclasses.dataclass
    class GovernorInvalidVoteParams(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#87)
        """
        _abi = {'inputs': [], 'name': 'GovernorInvalidVoteParams', 'type': 'error'}
        original_name = 'GovernorInvalidVoteParams'
        selector = bytes4(b'\x86}\xb7q')



    @dataclasses.dataclass
    class GovernorQueueNotImplemented(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#92)
        """
        _abi = {'inputs': [], 'name': 'GovernorQueueNotImplemented', 'type': 'error'}
        original_name = 'GovernorQueueNotImplemented'
        selector = bytes4(b'\x90\x88JF')



    @dataclasses.dataclass
    class GovernorNotQueuedProposal(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#97)

        Attributes:
            proposalId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorNotQueuedProposal', 'type': 'error'}
        original_name = 'GovernorNotQueuedProposal'
        selector = bytes4(b'\xd5\xdd\xb8%')

        proposalId: uint256


    @dataclasses.dataclass
    class GovernorAlreadyQueuedProposal(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#102)

        Attributes:
            proposalId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'GovernorAlreadyQueuedProposal', 'type': 'error'}
        original_name = 'GovernorAlreadyQueuedProposal'
        selector = bytes4(b'\xf2\x0e}7')

        proposalId: uint256


    @dataclasses.dataclass
    class GovernorInvalidSignature(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#108)

        Attributes:
            voter (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'voter', 'type': 'address'}], 'name': 'GovernorInvalidSignature', 'type': 'error'}
        original_name = 'GovernorInvalidSignature'
        selector = bytes4(b'\x94\xabl\x07')

        voter: Address


    @dataclasses.dataclass
    class GovernorUnableToCancel(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#113)

        Attributes:
            proposalId (uint256): uint256
            account (Address): address
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'GovernorUnableToCancel', 'type': 'error'}
        original_name = 'GovernorUnableToCancel'
        selector = bytes4(b'\x8f\xe5\xd8\xa9')

        proposalId: uint256
        account: Address


    @dataclasses.dataclass
    class ProposalCreated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#118)

        Attributes:
            proposalId (uint256): uint256
            proposer (Address): address
            targets (List[Address]): address[]
            values (List[uint256]): uint256[]
            signatures (List[str]): string[]
            calldatas (List[bytearray]): bytes[]
            voteStart (uint256): uint256
            voteEnd (uint256): uint256
            description (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'proposer', 'type': 'address'}, {'indexed': False, 'internalType': 'address[]', 'name': 'targets', 'type': 'address[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'string[]', 'name': 'signatures', 'type': 'string[]'}, {'indexed': False, 'internalType': 'bytes[]', 'name': 'calldatas', 'type': 'bytes[]'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteStart', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'voteEnd', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'description', 'type': 'string'}], 'name': 'ProposalCreated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ProposalCreated'
        selector = bytes32(b"}\x84\xa6&:\xe0\xd9\x8d3)\xbd{F\xbbN\x8do\x98\xcd5\xa7\xad\xb4\\'L\x8b\x7f\xd5\xeb\xd5\xe0")

        proposalId: uint256
        proposer: Address
        targets: List[Address]
        values: List[uint256]
        signatures: List[str]
        calldatas: List[bytearray]
        voteStart: uint256
        voteEnd: uint256
        description: str


    @dataclasses.dataclass
    class ProposalQueued:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#133)

        Attributes:
            proposalId (uint256): uint256
            etaSeconds (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'etaSeconds', 'type': 'uint256'}], 'name': 'ProposalQueued', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ProposalQueued'
        selector = bytes32(b'\x9a.B\xfdg"\x81=i\x11>}\x00y\xd3\xd9@\x17\x14(\xdfss\xdf\x9c\x7fv\x17\xcf\xda(\x92')

        proposalId: uint256
        etaSeconds: uint256


    @dataclasses.dataclass
    class ProposalExecuted:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#138)

        Attributes:
            proposalId (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalExecuted', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ProposalExecuted'
        selector = bytes32(b'q*\xe18?y\xac\x85?\x8d\x88!Sw\x8e\x02`\xef\x8f\x03\xb5\x04\xe2\x86n\x05\x93\xe0M+)\x1f')

        proposalId: uint256


    @dataclasses.dataclass
    class ProposalCanceled:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#143)

        Attributes:
            proposalId (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}], 'name': 'ProposalCanceled', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ProposalCanceled'
        selector = bytes32(b'x\x9c\xf5[\xe9\x80s\x9d\xad\x1d\x06\x99\xb9;X\xe8\x06\xb5\x1c\x9d\x96a\x9b\xfa\x8f\xe0\xa2\x8a\xba\xa7\xb3\x0c')

        proposalId: uint256


    @dataclasses.dataclass
    class VoteCast:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#150)

        Attributes:
            voter (Address): indexed address
            proposalId (uint256): uint256
            support (uint8): uint8
            weight (uint256): uint256
            reason (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}], 'name': 'VoteCast', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'VoteCast'
        selector = bytes32(b'\xb8\xe18\x88}\n\xa1;\xabD~\x82\xde\x9d\\\x17w\x04\x1e\xcd!\xca6\xba\x82O\xf1\xe6\xc0}\xdd\xa4')

        voter: Address
        proposalId: uint256
        support: uint8
        weight: uint256
        reason: str


    @dataclasses.dataclass
    class VoteCastWithParams:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#158)

        Attributes:
            voter (Address): indexed address
            proposalId (uint256): uint256
            support (uint8): uint8
            weight (uint256): uint256
            reason (str): string
            params (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'voter', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'proposalId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'support', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'reason', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'VoteCastWithParams', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'VoteCastWithParams'
        selector = bytes32(b'\xe2\xba\xbf\xba\xc5\x88\x9ap\x9bc\xbb\x7fY\x8b2N\x08\xbcZO\xb9\xecd\x7f\xb3\xcb\xc9\xec\x07\xeb\x87\x12')

        voter: Address
        proposalId: uint256
        support: uint8
        weight: uint256
        reason: str
        params: bytearray


    @overload
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#171)

        Returns:
            string
        """
        ...

    @overload
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#171)

        Returns:
            string
        """
        ...

    @overload
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#171)

        Returns:
            string
        """
        ...

    @overload
    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#171)

        Returns:
            string
        """
        ...

    def name(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#171)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "06fdde03", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def version(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#177)

        Returns:
            string
        """
        ...

    @overload
    def version(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#177)

        Returns:
            string
        """
        ...

    @overload
    def version(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#177)

        Returns:
            string
        """
        ...

    @overload
    def version(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#177)

        Returns:
            string
        """
        ...

    def version(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#177)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "54fd4d50", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def COUNTING_MODE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#202)

        Returns:
            string
        """
        ...

    @overload
    def COUNTING_MODE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#202)

        Returns:
            string
        """
        ...

    @overload
    def COUNTING_MODE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#202)

        Returns:
            string
        """
        ...

    @overload
    def COUNTING_MODE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#202)

        Returns:
            string
        """
        ...

    def COUNTING_MODE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#202)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "dd4e2ba5", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hashProposal(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#210)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def hashProposal(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#210)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def hashProposal(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#210)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def hashProposal(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#210)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    def hashProposal(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#210)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "c59057e4", [targets, values, calldatas, descriptionHash], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getProposalId(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#221)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def getProposalId(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#221)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def getProposalId(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#221)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def getProposalId(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#221)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        ...

    def getProposalId(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#221)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "a8f8a668", [targets, values, calldatas, descriptionHash], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IGovernor.ProposalState:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#232)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#232)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#232)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    @overload
    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IGovernor.ProposalState]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#232)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        ...

    def state(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IGovernor.ProposalState, TransactionAbc[IGovernor.ProposalState], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#232)

        Args:
            proposalId: uint256
        Returns:
            enum IGovernor.ProposalState
        """
        return self._execute(self.chain, request_type, "3e4f49e6", [proposalId], True if request_type == "tx" else False, IGovernor.ProposalState, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalThreshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#238)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalThreshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#238)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalThreshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#238)

        Returns:
            uint256
        """
        ...

    @overload
    def proposalThreshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#238)

        Returns:
            uint256
        """
        ...

    def proposalThreshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#238)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "b58131b0", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalSnapshot(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#246)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalSnapshot(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#246)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalSnapshot(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#246)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalSnapshot(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#246)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    def proposalSnapshot(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#246)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "2d63f693", [proposalId], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalDeadline(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#253)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalDeadline(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#253)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalDeadline(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#253)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalDeadline(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#253)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    def proposalDeadline(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#253)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "c01f9e37", [proposalId], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalProposer(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#259)

        Args:
            proposalId: uint256
        Returns:
            address
        """
        ...

    @overload
    def proposalProposer(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#259)

        Args:
            proposalId: uint256
        Returns:
            address
        """
        ...

    @overload
    def proposalProposer(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#259)

        Args:
            proposalId: uint256
        Returns:
            address
        """
        ...

    @overload
    def proposalProposer(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#259)

        Args:
            proposalId: uint256
        Returns:
            address
        """
        ...

    def proposalProposer(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#259)

        Args:
            proposalId: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "143489d0", [proposalId], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalEta(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#267)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalEta(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#267)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalEta(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#267)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def proposalEta(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#267)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        ...

    def proposalEta(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#267)

        Args:
            proposalId: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "ab58fb8e", [proposalId], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def proposalNeedsQueuing(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#273)

        Args:
            proposalId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#273)

        Args:
            proposalId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#273)

        Args:
            proposalId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def proposalNeedsQueuing(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#273)

        Args:
            proposalId: uint256
        Returns:
            bool
        """
        ...

    def proposalNeedsQueuing(self, proposalId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#273)

        Args:
            proposalId: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "a9a95294", [proposalId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def votingDelay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#286)

        Returns:
            uint256
        """
        ...

    @overload
    def votingDelay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#286)

        Returns:
            uint256
        """
        ...

    @overload
    def votingDelay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#286)

        Returns:
            uint256
        """
        ...

    @overload
    def votingDelay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#286)

        Returns:
            uint256
        """
        ...

    def votingDelay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#286)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "3932abb1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def votingPeriod(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#300)

        Returns:
            uint256
        """
        ...

    @overload
    def votingPeriod(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#300)

        Returns:
            uint256
        """
        ...

    @overload
    def votingPeriod(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#300)

        Returns:
            uint256
        """
        ...

    @overload
    def votingPeriod(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#300)

        Returns:
            uint256
        """
        ...

    def votingPeriod(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#300)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "02a251a3", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def quorum(self, timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#309)

        Args:
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def quorum(self, timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#309)

        Args:
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def quorum(self, timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#309)

        Args:
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def quorum(self, timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#309)

        Args:
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    def quorum(self, timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#309)

        Args:
            timepoint: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "f8ce560a", [timepoint], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getVotes(self, account: Union[Account, Address], timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#318)

        Args:
            account: address
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getVotes(self, account: Union[Account, Address], timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#318)

        Args:
            account: address
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getVotes(self, account: Union[Account, Address], timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#318)

        Args:
            account: address
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getVotes(self, account: Union[Account, Address], timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#318)

        Args:
            account: address
            timepoint: uint256
        Returns:
            uint256
        """
        ...

    def getVotes(self, account: Union[Account, Address], timepoint: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#318)

        Args:
            account: address
            timepoint: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "eb9019d4", [account, timepoint], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getVotesWithParams(self, account: Union[Account, Address], timepoint: uint256, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#324)

        Args:
            account: address
            timepoint: uint256
            params: bytes
        Returns:
            uint256
        """
        ...

    @overload
    def getVotesWithParams(self, account: Union[Account, Address], timepoint: uint256, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#324)

        Args:
            account: address
            timepoint: uint256
            params: bytes
        Returns:
            uint256
        """
        ...

    @overload
    def getVotesWithParams(self, account: Union[Account, Address], timepoint: uint256, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#324)

        Args:
            account: address
            timepoint: uint256
            params: bytes
        Returns:
            uint256
        """
        ...

    @overload
    def getVotesWithParams(self, account: Union[Account, Address], timepoint: uint256, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#324)

        Args:
            account: address
            timepoint: uint256
            params: bytes
        Returns:
            uint256
        """
        ...

    def getVotesWithParams(self, account: Union[Account, Address], timepoint: uint256, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#324)

        Args:
            account: address
            timepoint: uint256
            params: bytes
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "9a802a6d", [account, timepoint, params], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hasVoted(self, proposalId: uint256, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#334)

        Args:
            proposalId: uint256
            account: address
        Returns:
            bool
        """
        ...

    @overload
    def hasVoted(self, proposalId: uint256, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#334)

        Args:
            proposalId: uint256
            account: address
        Returns:
            bool
        """
        ...

    @overload
    def hasVoted(self, proposalId: uint256, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#334)

        Args:
            proposalId: uint256
            account: address
        Returns:
            bool
        """
        ...

    @overload
    def hasVoted(self, proposalId: uint256, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#334)

        Args:
            proposalId: uint256
            account: address
        Returns:
            bool
        """
        ...

    def hasVoted(self, proposalId: uint256, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#334)

        Args:
            proposalId: uint256
            account: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "43859632", [proposalId, account], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def propose(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], description: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#348)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            description: string
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def propose(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], description: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#348)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            description: string
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def propose(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], description: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#348)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            description: string
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def propose(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], description: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#348)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            description: string
        Returns:
            proposalId: uint256
        """
        ...

    def propose(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], description: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#348)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            description: string
        Returns:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "7d5e81e2", [targets, values, calldatas, description], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def queue(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#362)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def queue(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#362)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def queue(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#362)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def queue(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#362)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    def queue(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#362)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "160cbed7", [targets, values, calldatas, descriptionHash], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def execute(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#378)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def execute(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#378)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def execute(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#378)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def execute(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#378)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    def execute(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#378)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "2656227d", [targets, values, calldatas, descriptionHash], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def cancel(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#391)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def cancel(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#391)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def cancel(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#391)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    @overload
    def cancel(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#391)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        ...

    def cancel(self, targets: List[Union[Account, Address]], values: List[uint256], calldatas: List[Union[bytearray, bytes]], descriptionHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#391)

        Args:
            targets: address[]
            values: uint256[]
            calldatas: bytes[]
            descriptionHash: bytes32
        Returns:
            proposalId: uint256
        """
        return self._execute(self.chain, request_type, "452115d6", [targets, values, calldatas, descriptionHash], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def castVote(self, proposalId: uint256, support: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#403)

        Args:
            proposalId: uint256
            support: uint8
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVote(self, proposalId: uint256, support: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#403)

        Args:
            proposalId: uint256
            support: uint8
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVote(self, proposalId: uint256, support: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#403)

        Args:
            proposalId: uint256
            support: uint8
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVote(self, proposalId: uint256, support: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#403)

        Args:
            proposalId: uint256
            support: uint8
        Returns:
            balance: uint256
        """
        ...

    def castVote(self, proposalId: uint256, support: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#403)

        Args:
            proposalId: uint256
            support: uint8
        Returns:
            balance: uint256
        """
        return self._execute(self.chain, request_type, "56781388", [proposalId, support], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def castVoteWithReason(self, proposalId: uint256, support: uint8, reason: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#410)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReason(self, proposalId: uint256, support: uint8, reason: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#410)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReason(self, proposalId: uint256, support: uint8, reason: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#410)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReason(self, proposalId: uint256, support: uint8, reason: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#410)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
        Returns:
            balance: uint256
        """
        ...

    def castVoteWithReason(self, proposalId: uint256, support: uint8, reason: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#410)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
        Returns:
            balance: uint256
        """
        return self._execute(self.chain, request_type, "7b3c71d3", [proposalId, support, reason], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def castVoteWithReasonAndParams(self, proposalId: uint256, support: uint8, reason: str, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#421)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
            params: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParams(self, proposalId: uint256, support: uint8, reason: str, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#421)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
            params: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParams(self, proposalId: uint256, support: uint8, reason: str, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#421)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
            params: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParams(self, proposalId: uint256, support: uint8, reason: str, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#421)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
            params: bytes
        Returns:
            balance: uint256
        """
        ...

    def castVoteWithReasonAndParams(self, proposalId: uint256, support: uint8, reason: str, params: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#421)

        Args:
            proposalId: uint256
            support: uint8
            reason: string
            params: bytes
        Returns:
            balance: uint256
        """
        return self._execute(self.chain, request_type, "5f398a14", [proposalId, support, reason, params], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def castVoteBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#433)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#433)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#433)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#433)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    def castVoteBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#433)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            signature: bytes
        Returns:
            balance: uint256
        """
        return self._execute(self.chain, request_type, "8ff262e3", [proposalId, support, voter, signature], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def castVoteWithReasonAndParamsBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], reason: str, params: Union[bytearray, bytes], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#446)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            reason: string
            params: bytes
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParamsBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], reason: str, params: Union[bytearray, bytes], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#446)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            reason: string
            params: bytes
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParamsBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], reason: str, params: Union[bytearray, bytes], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#446)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            reason: string
            params: bytes
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    @overload
    def castVoteWithReasonAndParamsBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], reason: str, params: Union[bytearray, bytes], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#446)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            reason: string
            params: bytes
            signature: bytes
        Returns:
            balance: uint256
        """
        ...

    def castVoteWithReasonAndParamsBySig(self, proposalId: uint256, support: uint8, voter: Union[Account, Address], reason: str, params: Union[bytearray, bytes], signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/governance/IGovernor.sol#446)

        Args:
            proposalId: uint256
            support: uint8
            voter: address
            reason: string
            params: bytes
            signature: bytes
        Returns:
            balance: uint256
        """
        return self._execute(self.chain, request_type, "5b8d0e0d", [proposalId, support, voter, reason, params, signature], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IGovernor.name.selector = bytes4(b'\x06\xfd\xde\x03')
IGovernor.version.selector = bytes4(b'T\xfdMP')
IGovernor.COUNTING_MODE.selector = bytes4(b'\xddN+\xa5')
IGovernor.hashProposal.selector = bytes4(b'\xc5\x90W\xe4')
IGovernor.getProposalId.selector = bytes4(b'\xa8\xf8\xa6h')
IGovernor.state.selector = bytes4(b'>OI\xe6')
IGovernor.proposalThreshold.selector = bytes4(b'\xb5\x811\xb0')
IGovernor.proposalSnapshot.selector = bytes4(b'-c\xf6\x93')
IGovernor.proposalDeadline.selector = bytes4(b'\xc0\x1f\x9e7')
IGovernor.proposalProposer.selector = bytes4(b'\x144\x89\xd0')
IGovernor.proposalEta.selector = bytes4(b'\xabX\xfb\x8e')
IGovernor.proposalNeedsQueuing.selector = bytes4(b'\xa9\xa9R\x94')
IGovernor.votingDelay.selector = bytes4(b'92\xab\xb1')
IGovernor.votingPeriod.selector = bytes4(b'\x02\xa2Q\xa3')
IGovernor.quorum.selector = bytes4(b'\xf8\xceV\n')
IGovernor.getVotes.selector = bytes4(b'\xeb\x90\x19\xd4')
IGovernor.getVotesWithParams.selector = bytes4(b'\x9a\x80*m')
IGovernor.hasVoted.selector = bytes4(b'C\x85\x962')
IGovernor.propose.selector = bytes4(b'}^\x81\xe2')
IGovernor.queue.selector = bytes4(b'\x16\x0c\xbe\xd7')
IGovernor.execute.selector = bytes4(b'&V"}')
IGovernor.cancel.selector = bytes4(b'E!\x15\xd6')
IGovernor.castVote.selector = bytes4(b'Vx\x13\x88')
IGovernor.castVoteWithReason.selector = bytes4(b'{<q\xd3')
IGovernor.castVoteWithReasonAndParams.selector = bytes4(b'_9\x8a\x14')
IGovernor.castVoteBySig.selector = bytes4(b'\x8f\xf2b\xe3')
IGovernor.castVoteWithReasonAndParamsBySig.selector = bytes4(b'[\x8d\x0e\r')
