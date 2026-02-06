
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ERC1967Utils(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Utils.sol#15)
    """
    _abi = {b'b\xe7{\xa2': {'inputs': [{'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'ERC1967InvalidAdmin', 'type': 'error'}, b'd\xce\xd0\xec': {'inputs': [{'internalType': 'address', 'name': 'beacon', 'type': 'address'}], 'name': 'ERC1967InvalidBeacon', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea26469706673582212205a3c7ac0460fffe7845d0d1a7ebcd4ec1050f244f029b75d434b0d05cd2cb7e564736f6c63430008210033"

    _library_id = b'\xfcP4$y\xfd\xb1\ng\xfb\xdd\xfb\xd5\xb7\x96\xba\xa6'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1967Utils:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1967Utils]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1967Utils, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1967Utils]]:
        return cls._deploy(request_type, [], return_tx, ERC1967Utils, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ERC1967InvalidImplementation(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Utils.sol#26)

        Attributes:
            implementation (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}
        original_name = 'ERC1967InvalidImplementation'
        selector = bytes4(b'L\x9c\x8c\xe3')

        implementation: Address


    @dataclasses.dataclass
    class ERC1967InvalidAdmin(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Utils.sol#31)

        Attributes:
            admin (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'ERC1967InvalidAdmin', 'type': 'error'}
        original_name = 'ERC1967InvalidAdmin'
        selector = bytes4(b'b\xe7{\xa2')

        admin: Address


    @dataclasses.dataclass
    class ERC1967InvalidBeacon(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Utils.sol#36)

        Attributes:
            beacon (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'beacon', 'type': 'address'}], 'name': 'ERC1967InvalidBeacon', 'type': 'error'}
        original_name = 'ERC1967InvalidBeacon'
        selector = bytes4(b'd\xce\xd0\xec')

        beacon: Address


    @dataclasses.dataclass
    class ERC1967NonPayable(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Utils.sol#41)
        """
        _abi = {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}
        original_name = 'ERC1967NonPayable'
        selector = bytes4(b'\xb3\x98\x97\x9f')



