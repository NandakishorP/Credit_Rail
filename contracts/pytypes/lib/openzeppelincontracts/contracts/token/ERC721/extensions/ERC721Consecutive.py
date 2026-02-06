
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC2309 import IERC2309
from pytypes.lib.openzeppelincontracts.contracts.token.ERC721.ERC721 import ERC721



class ERC721Consecutive(ERC721, IERC2309):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol#30)
    """
    _abi = {b'\x8fX\xe5p': {'inputs': [{'internalType': 'uint256', 'name': 'batchSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxBatch', 'type': 'uint256'}], 'name': 'ERC721ExceededMaxBatchMint', 'type': 'error'}, b'\x1d\x08\x91e': {'inputs': [], 'name': 'ERC721ForbiddenBatchBurn', 'type': 'error'}, b'S\x9f\x90b': {'inputs': [], 'name': 'ERC721ForbiddenBatchMint', 'type': 'error'}, b'\xad\x89PR': {'inputs': [], 'name': 'ERC721ForbiddenMint', 'type': 'error'}, b'd(={': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721IncorrectOwner', 'type': 'error'}, b'\x17~\x80/': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721InsufficientApproval', 'type': 'error'}, b'\xa9\xfb\xf5\x1f': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC721InvalidApprover', 'type': 'error'}, b'[\x08\xba\x18': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'ERC721InvalidOperator', 'type': 'error'}, b'\x89\xc6+d': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721InvalidOwner', 'type': 'error'}, b'd\xa0\xae\x92': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC721InvalidReceiver', 'type': 'error'}, b's\xc6\xacn': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC721InvalidSender', 'type': 'error'}, b"~'2\x89": {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721NonexistentToken', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'approved', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}, b'\xde\xaa\x91\xb6\x12=\x06\x8fX!\xd0\xfb\x06xF=\x1a\x8a`y\xfe\x8a\xf5\xde<\xe5\xe8\x96\xdc\xf9\x13=': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'fromTokenId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'toTokenId', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'fromAddress', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'toAddress', 'type': 'address'}], 'name': 'ConsecutiveTransfer', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08\x18\x12\xfc': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getApproved', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\x85\xe9\xc5': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isApprovedForAll', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'B\x84.\x0e': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb8\x8dO\xde': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2,\xb4e': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc8{V\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'tokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":39990,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":39992,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_symbol","offset":0,"slot":1,"type":"t_string_storage"},{"astId":39996,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_owners","offset":0,"slot":2,"type":"t_mapping(t_uint256,t_address)"},{"astId":40000,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_balances","offset":0,"slot":3,"type":"t_mapping(t_address,t_uint256)"},{"astId":40004,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_tokenApprovals","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_address)"},{"astId":40010,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_operatorApprovals","offset":0,"slot":5,"type":"t_mapping(t_address,t_mapping(t_address,t_bool))"},{"astId":41075,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_sequentialOwnership","offset":0,"slot":6,"type":"t_struct(Trace160)49055_storage"},{"astId":41078,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_sequentialBurn","offset":0,"slot":7,"type":"t_struct(BitMap)47340_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_struct(Checkpoint160)49060_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct Checkpoints.Checkpoint160[]","numberOfBytes":32,"base":"t_struct(Checkpoint160)49060_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_bool))":{"encoding":"mapping","label":"mapping(address => mapping(address => bool))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_bool)"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_address)":{"encoding":"mapping","label":"mapping(uint256 => address)","numberOfBytes":32,"key":"t_uint256","value":"t_address"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(BitMap)47340_storage":{"encoding":"inplace","label":"struct BitMaps.BitMap","numberOfBytes":32,"members":[{"astId":47339,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_data","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_uint256)"}]},"t_struct(Checkpoint160)49060_storage":{"encoding":"inplace","label":"struct Checkpoints.Checkpoint160","numberOfBytes":32,"members":[{"astId":49057,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_key","offset":0,"slot":0,"type":"t_uint96"},{"astId":49059,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_value","offset":12,"slot":0,"type":"t_uint160"}]},"t_struct(Trace160)49055_storage":{"encoding":"inplace","label":"struct Checkpoints.Trace160","numberOfBytes":32,"members":[{"astId":49054,"contract":"lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol:ERC721Consecutive","label":"_checkpoints","offset":0,"slot":0,"type":"t_array(t_struct(Checkpoint160)49060_storage)dyn_storage"}]},"t_uint160":{"encoding":"inplace","label":"uint160","numberOfBytes":20},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint96":{"encoding":"inplace","label":"uint96","numberOfBytes":12}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC721Consecutive:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC721Consecutive]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC721Consecutive, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC721Consecutive]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class ERC721ForbiddenBatchMint(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol#42)
        """
        _abi = {'inputs': [], 'name': 'ERC721ForbiddenBatchMint', 'type': 'error'}
        original_name = 'ERC721ForbiddenBatchMint'
        selector = bytes4(b'S\x9f\x90b')



    @dataclasses.dataclass
    class ERC721ExceededMaxBatchMint(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol#47)

        Attributes:
            batchSize (uint256): uint256
            maxBatch (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'batchSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxBatch', 'type': 'uint256'}], 'name': 'ERC721ExceededMaxBatchMint', 'type': 'error'}
        original_name = 'ERC721ExceededMaxBatchMint'
        selector = bytes4(b'\x8fX\xe5p')

        batchSize: uint256
        maxBatch: uint256


    @dataclasses.dataclass
    class ERC721ForbiddenMint(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol#52)
        """
        _abi = {'inputs': [], 'name': 'ERC721ForbiddenMint', 'type': 'error'}
        original_name = 'ERC721ForbiddenMint'
        selector = bytes4(b'\xad\x89PR')



    @dataclasses.dataclass
    class ERC721ForbiddenBatchBurn(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC721/extensions/ERC721Consecutive.sol#57)
        """
        _abi = {'inputs': [], 'name': 'ERC721ForbiddenBatchBurn', 'type': 'error'}
        original_name = 'ERC721ForbiddenBatchBurn'
        selector = bytes4(b'\x1d\x08\x91e')



