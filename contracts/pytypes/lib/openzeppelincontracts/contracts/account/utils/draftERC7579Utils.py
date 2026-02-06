
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ERC7579Utils(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#22)
    """
    _abi = {b'\x95\xd4\x8a[': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579AlreadyInstalledModule', 'type': 'error'}, b'\xeb\x0b\xcc]': {'inputs': [], 'name': 'ERC7579DecodingError', 'type': 'error'}, b'\x8f\x89Go': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579MismatchedModuleTypeId', 'type': 'error'}, b'\x13C\xd6\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579UninstalledModule', 'type': 'error'}, b'\xb1\xbej\x96': {'inputs': [{'internalType': 'CallType', 'name': 'callType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedCallType', 'type': 'error'}, b'#\xa2@\x85': {'inputs': [{'internalType': 'ExecType', 'name': 'execType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedExecType', 'type': 'error'}, b'`\xfa+#': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'ERC7579UnsupportedModuleType', 'type': 'error'}, b'.\xea/Q\xf89\x10H\x1fK[\xa2\x8bp\x03\xa6\xe0E\xd4\xb5\x9fg\xdf\xff\x8dL\x90\x11\x94\x05\x00\x89': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'batchExecutionIndex', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'returndata', 'type': 'bytes'}], 'name': 'ERC7579TryExecuteFail', 'type': 'event'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220980937570b2eeb71c30f3fbea9d0471426e81845ec5889ebe45e647e14e8017c64736f6c63430008210033"

    _library_id = b'\x8b?\xa6\xcb\x16\xf7>\xfa@K\xe3dN\x9a\x1a\xbdu'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC7579Utils:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC7579Utils]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC7579Utils, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC7579Utils]]:
        return cls._deploy(request_type, [], return_tx, ERC7579Utils, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ERC7579UnsupportedCallType(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#48)

        Attributes:
            callType (bytes1): CallType
        """
        _abi = {'inputs': [{'internalType': 'CallType', 'name': 'callType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedCallType', 'type': 'error'}
        original_name = 'ERC7579UnsupportedCallType'
        selector = bytes4(b'\xb1\xbej\x96')

        callType: bytes1


    @dataclasses.dataclass
    class ERC7579UnsupportedExecType(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#51)

        Attributes:
            execType (bytes1): ExecType
        """
        _abi = {'inputs': [{'internalType': 'ExecType', 'name': 'execType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedExecType', 'type': 'error'}
        original_name = 'ERC7579UnsupportedExecType'
        selector = bytes4(b'#\xa2@\x85')

        execType: bytes1


    @dataclasses.dataclass
    class ERC7579MismatchedModuleTypeId(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#54)

        Attributes:
            moduleTypeId (uint256): uint256
            module (Address): address
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579MismatchedModuleTypeId', 'type': 'error'}
        original_name = 'ERC7579MismatchedModuleTypeId'
        selector = bytes4(b'\x8f\x89Go')

        moduleTypeId: uint256
        module: Address


    @dataclasses.dataclass
    class ERC7579UninstalledModule(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#57)

        Attributes:
            moduleTypeId (uint256): uint256
            module (Address): address
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579UninstalledModule', 'type': 'error'}
        original_name = 'ERC7579UninstalledModule'
        selector = bytes4(b'\x13C\xd6\x8d')

        moduleTypeId: uint256
        module: Address


    @dataclasses.dataclass
    class ERC7579AlreadyInstalledModule(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#60)

        Attributes:
            moduleTypeId (uint256): uint256
            module (Address): address
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579AlreadyInstalledModule', 'type': 'error'}
        original_name = 'ERC7579AlreadyInstalledModule'
        selector = bytes4(b'\x95\xd4\x8a[')

        moduleTypeId: uint256
        module: Address


    @dataclasses.dataclass
    class ERC7579UnsupportedModuleType(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#63)

        Attributes:
            moduleTypeId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'ERC7579UnsupportedModuleType', 'type': 'error'}
        original_name = 'ERC7579UnsupportedModuleType'
        selector = bytes4(b'`\xfa+#')

        moduleTypeId: uint256


    @dataclasses.dataclass
    class ERC7579DecodingError(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#66)
        """
        _abi = {'inputs': [], 'name': 'ERC7579DecodingError', 'type': 'error'}
        original_name = 'ERC7579DecodingError'
        selector = bytes4(b'\xeb\x0b\xcc]')



    @dataclasses.dataclass
    class ERC7579TryExecuteFail:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/utils/draft-ERC7579Utils.sol#45)

        Attributes:
            batchExecutionIndex (uint256): uint256
            returndata (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'batchExecutionIndex', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'returndata', 'type': 'bytes'}], 'name': 'ERC7579TryExecuteFail', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC7579TryExecuteFail'
        selector = bytes32(b'.\xea/Q\xf89\x10H\x1fK[\xa2\x8bp\x03\xa6\xe0E\xd4\xb5\x9fg\xdf\xff\x8dL\x90\x11\x94\x05\x00\x89')

        batchExecutionIndex: uint256
        returndata: bytearray


