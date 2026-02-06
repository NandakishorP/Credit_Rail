
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.interfaces.IERC165 import IERC165



class IERC1155(IERC165):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#9)
    """
    _abi = {b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': '_approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}, b'J9\xdc\x06\xd4\xc0\xdb\xc6Kp\xaf\x90\xfdi\x8a#:Q\x8a\xa5\xd0~Y]\x98;\x8c\x05&\xc8\xf7\xfb': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256[]', 'name': '_ids', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': '_values', 'type': 'uint256[]'}], 'name': 'TransferBatch', 'type': 'event'}, b'\xc3\xd5\x81h\xc5\xaes\x97s\x1d\x06=[\xbf=exTBsC\xf4\xc0\x83$\x0fz\xac\xaa-\x0fb': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_value', 'type': 'uint256'}], 'name': 'TransferSingle', 'type': 'event'}, b'k\xb7\xffp\x86\x19\xba\x06\x10\xcb\xa2\x95\xa5\x85\x92\xe0E\x1d\xee&"\x93\x8c\x87Ufv\x88\xda\xf3R\x9b': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '_value', 'type': 'string'}, {'indexed': True, 'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'URI', 'type': 'event'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'N\x12s\xf4': {'inputs': [{'internalType': 'address[]', 'name': '_owners', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': '_ids', 'type': 'uint256[]'}], 'name': 'balanceOfBatch', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\x85\xe9\xc5': {'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'internalType': 'address', 'name': '_operator', 'type': 'address'}], 'name': 'isApprovedForAll', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'.\xb2\xc2\xd6': {'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256[]', 'name': '_ids', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_values', 'type': 'uint256[]'}, {'internalType': 'bytes', 'name': '_data', 'type': 'bytes'}], 'name': 'safeBatchTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2BC*': {'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_value', 'type': 'uint256'}, {'internalType': 'bytes', 'name': '_data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2,\xb4e': {'inputs': [{'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'internalType': 'bool', 'name': '_approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceID', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC1155:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC1155]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC1155, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC1155]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class TransferSingle:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#19)

        Attributes:
            _operator (Address): indexed address
            _from (Address): indexed address
            _to (Address): indexed address
            _id (uint256): uint256
            _value (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': '_value', 'type': 'uint256'}], 'name': 'TransferSingle', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TransferSingle'
        selector = bytes32(b'\xc3\xd5\x81h\xc5\xaes\x97s\x1d\x06=[\xbf=exTBsC\xf4\xc0\x83$\x0fz\xac\xaa-\x0fb')

        _operator: Address
        _from: Address
        _to: Address
        _id: uint256
        _value: uint256


    @dataclasses.dataclass
    class TransferBatch:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#32)

        Attributes:
            _operator (Address): indexed address
            _from (Address): indexed address
            _to (Address): indexed address
            _ids (List[uint256]): uint256[]
            _values (List[uint256]): uint256[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256[]', 'name': '_ids', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': '_values', 'type': 'uint256[]'}], 'name': 'TransferBatch', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TransferBatch'
        selector = bytes32(b'J9\xdc\x06\xd4\xc0\xdb\xc6Kp\xaf\x90\xfdi\x8a#:Q\x8a\xa5\xd0~Y]\x98;\x8c\x05&\xc8\xf7\xfb')

        _operator: Address
        _from: Address
        _to: Address
        _ids: List[uint256]
        _values: List[uint256]


    @dataclasses.dataclass
    class ApprovalForAll:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#37)

        Attributes:
            _owner (Address): indexed address
            _operator (Address): indexed address
            _approved (bool): bool
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': '_operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': '_approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ApprovalForAll'
        selector = bytes32(b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1')

        _owner: Address
        _operator: Address
        _approved: bool


    @dataclasses.dataclass
    class URI:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#41)

        Attributes:
            _value (str): string
            _id (uint256): indexed uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '_value', 'type': 'string'}, {'indexed': True, 'internalType': 'uint256', 'name': '_id', 'type': 'uint256'}], 'name': 'URI', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'URI'
        selector = bytes32(b'k\xb7\xffp\x86\x19\xba\x06\x10\xcb\xa2\x95\xa5\x85\x92\xe0E\x1d\xee&"\x93\x8c\x87Ufv\x88\xda\xf3R\x9b')

        _value: str
        _id: uint256


    @overload
    def safeTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _id: uint256, _value: uint256, _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#55)

        Args:
            _from: address
            _to: address
            _id: uint256
            _value: uint256
            _data: bytes
        """
        ...

    @overload
    def safeTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _id: uint256, _value: uint256, _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#55)

        Args:
            _from: address
            _to: address
            _id: uint256
            _value: uint256
            _data: bytes
        """
        ...

    @overload
    def safeTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _id: uint256, _value: uint256, _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#55)

        Args:
            _from: address
            _to: address
            _id: uint256
            _value: uint256
            _data: bytes
        """
        ...

    @overload
    def safeTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _id: uint256, _value: uint256, _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#55)

        Args:
            _from: address
            _to: address
            _id: uint256
            _value: uint256
            _data: bytes
        """
        ...

    def safeTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _id: uint256, _value: uint256, _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#55)

        Args:
            _from: address
            _to: address
            _id: uint256
            _value: uint256
            _data: bytes
        """
        return self._execute(self.chain, request_type, "f242432a", [_from, _to, _id, _value, _data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def safeBatchTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _ids: List[uint256], _values: List[uint256], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#71)

        Args:
            _from: address
            _to: address
            _ids: uint256[]
            _values: uint256[]
            _data: bytes
        """
        ...

    @overload
    def safeBatchTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _ids: List[uint256], _values: List[uint256], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#71)

        Args:
            _from: address
            _to: address
            _ids: uint256[]
            _values: uint256[]
            _data: bytes
        """
        ...

    @overload
    def safeBatchTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _ids: List[uint256], _values: List[uint256], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#71)

        Args:
            _from: address
            _to: address
            _ids: uint256[]
            _values: uint256[]
            _data: bytes
        """
        ...

    @overload
    def safeBatchTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _ids: List[uint256], _values: List[uint256], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#71)

        Args:
            _from: address
            _to: address
            _ids: uint256[]
            _values: uint256[]
            _data: bytes
        """
        ...

    def safeBatchTransferFrom(self, _from: Union[Account, Address], _to: Union[Account, Address], _ids: List[uint256], _values: List[uint256], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#71)

        Args:
            _from: address
            _to: address
            _ids: uint256[]
            _values: uint256[]
            _data: bytes
        """
        return self._execute(self.chain, request_type, "2eb2c2d6", [_from, _to, _ids, _values, _data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def balanceOf(self, _owner: Union[Account, Address], _id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#83)

        Args:
            _owner: address
            _id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, _owner: Union[Account, Address], _id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#83)

        Args:
            _owner: address
            _id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, _owner: Union[Account, Address], _id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#83)

        Args:
            _owner: address
            _id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, _owner: Union[Account, Address], _id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#83)

        Args:
            _owner: address
            _id: uint256
        Returns:
            uint256
        """
        ...

    def balanceOf(self, _owner: Union[Account, Address], _id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#83)

        Args:
            _owner: address
            _id: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "00fdd58e", [_owner, _id], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def balanceOfBatch(self, _owners: List[Union[Account, Address]], _ids: List[uint256], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#89)

        Args:
            _owners: address[]
            _ids: uint256[]
        Returns:
            uint256[]
        """
        ...

    @overload
    def balanceOfBatch(self, _owners: List[Union[Account, Address]], _ids: List[uint256], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#89)

        Args:
            _owners: address[]
            _ids: uint256[]
        Returns:
            uint256[]
        """
        ...

    @overload
    def balanceOfBatch(self, _owners: List[Union[Account, Address]], _ids: List[uint256], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#89)

        Args:
            _owners: address[]
            _ids: uint256[]
        Returns:
            uint256[]
        """
        ...

    @overload
    def balanceOfBatch(self, _owners: List[Union[Account, Address]], _ids: List[uint256], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint256]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#89)

        Args:
            _owners: address[]
            _ids: uint256[]
        Returns:
            uint256[]
        """
        ...

    def balanceOfBatch(self, _owners: List[Union[Account, Address]], _ids: List[uint256], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint256], TransactionAbc[List[uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#89)

        Args:
            _owners: address[]
            _ids: uint256[]
        Returns:
            uint256[]
        """
        return self._execute(self.chain, request_type, "4e1273f4", [_owners, _ids], True if request_type == "tx" else False, List[uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setApprovalForAll(self, _operator: Union[Account, Address], _approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#98)

        Args:
            _operator: address
            _approved: bool
        """
        ...

    @overload
    def setApprovalForAll(self, _operator: Union[Account, Address], _approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#98)

        Args:
            _operator: address
            _approved: bool
        """
        ...

    @overload
    def setApprovalForAll(self, _operator: Union[Account, Address], _approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#98)

        Args:
            _operator: address
            _approved: bool
        """
        ...

    @overload
    def setApprovalForAll(self, _operator: Union[Account, Address], _approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#98)

        Args:
            _operator: address
            _approved: bool
        """
        ...

    def setApprovalForAll(self, _operator: Union[Account, Address], _approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#98)

        Args:
            _operator: address
            _approved: bool
        """
        return self._execute(self.chain, request_type, "a22cb465", [_operator, _approved], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isApprovedForAll(self, _owner: Union[Account, Address], _operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#104)

        Args:
            _owner: address
            _operator: address
        Returns:
            bool
        """
        ...

    @overload
    def isApprovedForAll(self, _owner: Union[Account, Address], _operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#104)

        Args:
            _owner: address
            _operator: address
        Returns:
            bool
        """
        ...

    @overload
    def isApprovedForAll(self, _owner: Union[Account, Address], _operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#104)

        Args:
            _owner: address
            _operator: address
        Returns:
            bool
        """
        ...

    @overload
    def isApprovedForAll(self, _owner: Union[Account, Address], _operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#104)

        Args:
            _owner: address
            _operator: address
        Returns:
            bool
        """
        ...

    def isApprovedForAll(self, _owner: Union[Account, Address], _operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC1155.sol#104)

        Args:
            _owner: address
            _operator: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e985e9c5", [_owner, _operator], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IERC1155.safeTransferFrom.selector = bytes4(b'\xf2BC*')
IERC1155.safeBatchTransferFrom.selector = bytes4(b'.\xb2\xc2\xd6')
IERC1155.balanceOf.selector = bytes4(b'\x00\xfd\xd5\x8e')
IERC1155.balanceOfBatch.selector = bytes4(b'N\x12s\xf4')
IERC1155.setApprovalForAll.selector = bytes4(b'\xa2,\xb4e')
IERC1155.isApprovedForAll.selector = bytes4(b'\xe9\x85\xe9\xc5')
