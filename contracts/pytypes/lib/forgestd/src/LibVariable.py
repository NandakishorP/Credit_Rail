
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



@dataclasses.dataclass
class Variable:
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#7)

    Attributes:
        ty (Type): struct Type
        data (bytearray): bytes
    """
    original_name = 'Variable'

    ty: Type
    data: bytearray


@dataclasses.dataclass
class Type:
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#12)

    Attributes:
        kind (TypeKind): enum TypeKind
        isArray (bool): bool
    """
    original_name = 'Type'

    kind: TypeKind
    isArray: bool


class TypeKind(IntEnum):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#17)

    """
    None_ = 0
    Bool = 1
    Address_ = 2
    Bytes32 = 3
    Uint256 = 4
    Int256 = 5
    String = 6
    Bytes = 7


class LibVariable(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#55)
    """
    _abi = {b'\x87\x13\x8d\\': {'inputs': [], 'name': 'NotInitialized', 'type': 'error'}, b'\xb0,\xf7\x1d': {'inputs': [{'internalType': 'string', 'name': 'expected', 'type': 'string'}, {'internalType': 'string', 'name': 'actual', 'type': 'string'}], 'name': 'TypeMismatch', 'type': 'error'}, b'\x9f\x9d\xda\xbb': {'inputs': [{'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'UnsafeCast', 'type': 'error'}, b'\x15\xaf\x8f\xee': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'TypeKind'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'self', 'type': 'tuple'}], 'name': 'assertExists', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608080604052346019576101b6908161001e823930815050f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c6315af8fee14610024575f80fd5b60203660031901126101485760043567ffffffffffffffff81116101485760031981360301906060821261014857604061005c610160565b92126101485761006a610160565b8160040135600881101561014857815260248201358015158103610148576020820152825260448101359067ffffffffffffffff821161014857013660238201121561014857600481013567ffffffffffffffff811161014c5760405191601f8201601f19908116603f0116830167ffffffffffffffff81118482101761014c57604052818352366024828401011161014857815f926024602093018386013783010152602082015251516008811015610134571561012557005b6321c4e35760e21b5f5260045ffd5b634e487b7160e01b5f52602160045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b604051906040820182811067ffffffffffffffff82111761014c5760405256fea264697066735822122032379243f2424f91afe7afd846f3120de68c4d4adfaab7d4ed99f4bd327b45e264736f6c63430008210033"

    _library_id = b'X\x0c\xbfWf\x1cc\xd0\xb7\x88\xabv\xfaX\xc1\x93\xa5'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LibVariable:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LibVariable]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, LibVariable, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[LibVariable]]:
        return cls._deploy(request_type, [], return_tx, LibVariable, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class NotInitialized(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#56)
        """
        _abi = {'inputs': [], 'name': 'NotInitialized', 'type': 'error'}
        original_name = 'NotInitialized'
        selector = bytes4(b'\x87\x13\x8d\\')



    @dataclasses.dataclass
    class TypeMismatch(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#57)

        Attributes:
            expected (str): string
            actual (str): string
        """
        _abi = {'inputs': [{'internalType': 'string', 'name': 'expected', 'type': 'string'}, {'internalType': 'string', 'name': 'actual', 'type': 'string'}], 'name': 'TypeMismatch', 'type': 'error'}
        original_name = 'TypeMismatch'
        selector = bytes4(b'\xb0,\xf7\x1d')

        expected: str
        actual: str


    @dataclasses.dataclass
    class UnsafeCast(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#58)

        Attributes:
            message (str): string
        """
        _abi = {'inputs': [{'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'UnsafeCast', 'type': 'error'}
        original_name = 'UnsafeCast'
        selector = bytes4(b'\x9f\x9d\xda\xbb')

        message: str


    @overload
    def assertExists(self, self_: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#118)

        Args:
            self_: struct Variable
        """
        ...

    @overload
    def assertExists(self, self_: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#118)

        Args:
            self_: struct Variable
        """
        ...

    @overload
    def assertExists(self, self_: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#118)

        Args:
            self_: struct Variable
        """
        ...

    @overload
    def assertExists(self, self_: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#118)

        Args:
            self_: struct Variable
        """
        ...

    def assertExists(self, self_: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/LibVariable.sol#118)

        Args:
            self_: struct Variable
        """
        return self._execute(self.chain, request_type, "15af8fee", [self_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

LibVariable.assertExists.selector = bytes4(b'\x15\xaf\x8f\xee')
