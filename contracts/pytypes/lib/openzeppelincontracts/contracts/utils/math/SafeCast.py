
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class SafeCast(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/math/SafeCast.sol#19)
    """
    _abi = {b'2ri\xa7': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'int256', 'name': 'value', 'type': 'int256'}], 'name': 'SafeCastOverflowedIntDowncast', 'type': 'error'}, b'\xa8\xceD2': {'inputs': [{'internalType': 'int256', 'name': 'value', 'type': 'int256'}], 'name': 'SafeCastOverflowedIntToUint', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b'$w^\x06': {'inputs': [{'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintToInt', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220cd16b5423871b05f9d3a8ea2587a059d7d81af8ab4251bdb3c4a93d37afe081364736f6c63430008210033"

    _library_id = b'\xddS}\xc5\xfds\xedSG5e\xa8\xb7\x12\xcc\xaf%'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SafeCast:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SafeCast]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SafeCast, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SafeCast]]:
        return cls._deploy(request_type, [], return_tx, SafeCast, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class SafeCastOverflowedUintDowncast(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/math/SafeCast.sol#23)

        Attributes:
            bits (uint8): uint8
            value (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}
        original_name = 'SafeCastOverflowedUintDowncast'
        selector = bytes4(b'm\xfc\xc6P')

        bits: uint8
        value: uint256


    @dataclasses.dataclass
    class SafeCastOverflowedIntToUint(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/math/SafeCast.sol#28)

        Attributes:
            value (int256): int256
        """
        _abi = {'inputs': [{'internalType': 'int256', 'name': 'value', 'type': 'int256'}], 'name': 'SafeCastOverflowedIntToUint', 'type': 'error'}
        original_name = 'SafeCastOverflowedIntToUint'
        selector = bytes4(b'\xa8\xceD2')

        value: int256


    @dataclasses.dataclass
    class SafeCastOverflowedIntDowncast(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/math/SafeCast.sol#33)

        Attributes:
            bits (uint8): uint8
            value (int256): int256
        """
        _abi = {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'int256', 'name': 'value', 'type': 'int256'}], 'name': 'SafeCastOverflowedIntDowncast', 'type': 'error'}
        original_name = 'SafeCastOverflowedIntDowncast'
        selector = bytes4(b'2ri\xa7')

        bits: uint8
        value: int256


    @dataclasses.dataclass
    class SafeCastOverflowedUintToInt(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/math/SafeCast.sol#38)

        Attributes:
            value (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintToInt', 'type': 'error'}
        original_name = 'SafeCastOverflowedUintToInt'
        selector = bytes4(b'$w^\x06')

        value: uint256


