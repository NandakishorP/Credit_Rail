
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.governance.utils.Votes import Votes
from pytypes.lib.openzeppelincontracts.contracts.token.ERC20.ERC20 import ERC20
from pytypes.lib.openzeppelincontracts.contracts.utils.structs.Checkpoints import Checkpoints



class ERC20Votes(Votes, ERC20):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#23)
    """
    _abi = {b'% `\x1d': {'inputs': [], 'name': 'CheckpointUnorderedInsertion', 'type': 'error'}, b'\xf6E\xee\xdf': {'inputs': [], 'name': 'ECDSAInvalidSignature', 'type': 'error'}, b'\xfc\xe6\x98\xf7': {'inputs': [{'internalType': 'uint256', 'name': 'length', 'type': 'uint256'}], 'name': 'ECDSAInvalidSignatureLength', 'type': 'error'}, b'\xd7\x8b\xce\x0c': {'inputs': [{'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'ECDSAInvalidSignatureS', 'type': 'error'}, b'\x1c\xb1]&': {'inputs': [{'internalType': 'uint256', 'name': 'increasedSupply', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'cap', 'type': 'uint256'}], 'name': 'ERC20ExceededSafeSupply', 'type': 'error'}, b'\xfb\x8fA\xb2': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientAllowance', 'type': 'error'}, b'\xe4P\xd3\x8c': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientBalance', 'type': 'error'}, b'\xe6\x02\xdf\x05': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC20InvalidApprover', 'type': 'error'}, b'\xecD/\x05': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC20InvalidReceiver', 'type': 'error'}, b'\x96\xc6\xfd\x1e': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC20InvalidSender', 'type': 'error'}, b'\x94(\rb': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC20InvalidSpender', 'type': 'error'}, b'\xec\xd3\xf8\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}, {'internalType': 'uint48', 'name': 'clock', 'type': 'uint48'}], 'name': 'ERC5805FutureLookup', 'type': 'error'}, b'o\xf0q@': {'inputs': [], 'name': 'ERC6372InconsistentClock', 'type': 'error'}, b'u-\x88\xc0': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentNonce', 'type': 'uint256'}], 'name': 'InvalidAccountNonce', 'type': 'error'}, b'\xb3Q+\x0c': {'inputs': [], 'name': 'InvalidShortString', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b"0Z'\xa9": {'inputs': [{'internalType': 'string', 'name': 'str', 'type': 'string'}], 'name': 'StringTooLong', 'type': 'error'}, b'F\x83\xaf\x0e': {'inputs': [{'internalType': 'uint256', 'name': 'expiry', 'type': 'uint256'}], 'name': 'VotesExpiredSignature', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'14\xe8\xa2\xe6\xd9~\x92\x9a~T\x01\x1e\xa5H]}\x19m\xd5\xf0\xbaMN\xf9X\x03\xe8\xe3\xfc%\x7f': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'delegator', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'fromDelegate', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'toDelegate', 'type': 'address'}], 'name': 'DelegateChanged', 'type': 'event'}, b'\xde\xc2\xba\xcd\xd2\xf0[Y\xde4\xda\x9bR=\xff\x8b\xe4.^8\xe8\x18\xc8/\xdb\x0b\xaewC\x87\xa7$': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'delegate', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'previousVotes', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'newVotes', 'type': 'uint256'}], 'name': 'DelegateVotesChanged', 'type': 'event'}, b'\nc\x87\xc9\xea6(\xb8\x8ac;\xb4\xf3\xb1Qw\x0fp\x08Q\x17\xa1_\x9b\xf3x|\xdaS\xf1=1': {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'K\xf5\xd7\xe9': {'inputs': [], 'name': 'CLOCK_MODE', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf1\x12~\xd8': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint32', 'name': 'pos', 'type': 'uint32'}], 'name': 'checkpoints', 'outputs': [{'components': [{'internalType': 'uint48', 'name': '_key', 'type': 'uint48'}, {'internalType': 'uint208', 'name': '_value', 'type': 'uint208'}], 'internalType': 'struct Checkpoints.Checkpoint208', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91\xdd\xad\xf4': {'inputs': [], 'name': 'clock', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\\\x19\xa9\\': {'inputs': [{'internalType': 'address', 'name': 'delegatee', 'type': 'address'}], 'name': 'delegate', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc3\xcd\xa5 ': {'inputs': [{'internalType': 'address', 'name': 'delegatee', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nonce', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expiry', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'delegateBySig', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'X|\xde\x1e': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'delegates', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x84\xb0\x19n': {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8eS\x9e\x8c': {'inputs': [{'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'getPastTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b':F\xb1\xa8': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timepoint', 'type': 'uint256'}], 'name': 'getPastVotes', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9a\xb2N\xb0': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'getVotes', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'o\xcf\xffE': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'numCheckpoints', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":44413,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_uint256)"},{"astId":44419,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_allowances","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_uint256))"},{"astId":44421,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_totalSupply","offset":0,"slot":2,"type":"t_uint256"},{"astId":44423,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_name","offset":0,"slot":3,"type":"t_string_storage"},{"astId":44425,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_symbol","offset":0,"slot":4,"type":"t_string_storage"},{"astId":48910,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_nameFallback","offset":0,"slot":5,"type":"t_string_storage"},{"astId":48912,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_versionFallback","offset":0,"slot":6,"type":"t_string_storage"},{"astId":46487,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_nonces","offset":0,"slot":7,"type":"t_mapping(t_address,t_uint256)"},{"astId":43307,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_delegatee","offset":0,"slot":8,"type":"t_mapping(t_address,t_address)"},{"astId":43312,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_delegateCheckpoints","offset":0,"slot":9,"type":"t_mapping(t_address,t_struct(Trace208)54159_storage)"},{"astId":43315,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_totalCheckpoints","offset":0,"slot":10,"type":"t_struct(Trace208)54159_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_struct(Checkpoint208)54164_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct Checkpoints.Checkpoint208[]","numberOfBytes":32,"base":"t_struct(Checkpoint208)54164_storage"},"t_mapping(t_address,t_address)":{"encoding":"mapping","label":"mapping(address => address)","numberOfBytes":32,"key":"t_address","value":"t_address"},"t_mapping(t_address,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(address => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_address,t_struct(Trace208)54159_storage)":{"encoding":"mapping","label":"mapping(address => struct Checkpoints.Trace208)","numberOfBytes":32,"key":"t_address","value":"t_struct(Trace208)54159_storage"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Checkpoint208)54164_storage":{"encoding":"inplace","label":"struct Checkpoints.Checkpoint208","numberOfBytes":32,"members":[{"astId":54161,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_key","offset":0,"slot":0,"type":"t_uint48"},{"astId":54163,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_value","offset":6,"slot":0,"type":"t_uint208"}]},"t_struct(Trace208)54159_storage":{"encoding":"inplace","label":"struct Checkpoints.Trace208","numberOfBytes":32,"members":[{"astId":54158,"contract":"lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol:ERC20Votes","label":"_checkpoints","offset":0,"slot":0,"type":"t_array(t_struct(Checkpoint208)54164_storage)dyn_storage"}]},"t_uint208":{"encoding":"inplace","label":"uint208","numberOfBytes":26},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint48":{"encoding":"inplace","label":"uint48","numberOfBytes":6}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC20Votes:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC20Votes]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC20Votes, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC20Votes]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class ERC20ExceededSafeSupply(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#27)

        Attributes:
            increasedSupply (uint256): uint256
            cap (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'increasedSupply', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'cap', 'type': 'uint256'}], 'name': 'ERC20ExceededSafeSupply', 'type': 'error'}
        original_name = 'ERC20ExceededSafeSupply'
        selector = bytes4(b'\x1c\xb1]&')

        increasedSupply: uint256
        cap: uint256


    @overload
    def numCheckpoints(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#73)

        Args:
            account: address
        Returns:
            uint32
        """
        ...

    @overload
    def numCheckpoints(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#73)

        Args:
            account: address
        Returns:
            uint32
        """
        ...

    @overload
    def numCheckpoints(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#73)

        Args:
            account: address
        Returns:
            uint32
        """
        ...

    @overload
    def numCheckpoints(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#73)

        Args:
            account: address
        Returns:
            uint32
        """
        ...

    def numCheckpoints(self, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#73)

        Args:
            account: address
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "6fcfff45", [account], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def checkpoints(self, account: Union[Account, Address], pos: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Checkpoints.Checkpoint208:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#80)

        Args:
            account: address
            pos: uint32
        Returns:
            struct Checkpoints.Checkpoint208
        """
        ...

    @overload
    def checkpoints(self, account: Union[Account, Address], pos: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#80)

        Args:
            account: address
            pos: uint32
        Returns:
            struct Checkpoints.Checkpoint208
        """
        ...

    @overload
    def checkpoints(self, account: Union[Account, Address], pos: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#80)

        Args:
            account: address
            pos: uint32
        Returns:
            struct Checkpoints.Checkpoint208
        """
        ...

    @overload
    def checkpoints(self, account: Union[Account, Address], pos: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Checkpoints.Checkpoint208]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#80)

        Args:
            account: address
            pos: uint32
        Returns:
            struct Checkpoints.Checkpoint208
        """
        ...

    def checkpoints(self, account: Union[Account, Address], pos: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Checkpoints.Checkpoint208, TransactionAbc[Checkpoints.Checkpoint208], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/extensions/ERC20Votes.sol#80)

        Args:
            account: address
            pos: uint32
        Returns:
            struct Checkpoints.Checkpoint208
        """
        return self._execute(self.chain, request_type, "f1127ed8", [account, pos], True if request_type == "tx" else False, Checkpoints.Checkpoint208, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC20Votes.numCheckpoints.selector = bytes4(b'o\xcf\xffE')
ERC20Votes.checkpoints.selector = bytes4(b'\xf1\x12~\xd8')
