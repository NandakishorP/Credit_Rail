
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ECDSA(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol#12)
    """
    _abi = {b'\xf6E\xee\xdf': {'inputs': [], 'name': 'ECDSAInvalidSignature', 'type': 'error'}, b'\xfc\xe6\x98\xf7': {'inputs': [{'internalType': 'uint256', 'name': 'length', 'type': 'uint256'}], 'name': 'ECDSAInvalidSignatureLength', 'type': 'error'}, b'\xd7\x8b\xce\x0c': {'inputs': [{'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'ECDSAInvalidSignatureS', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220d85783993fb6d9b5e43a5bbeef8935cbb4701b9af9f17d2fee1b4b8731dfd28f64736f6c63430008210033"

    _library_id = b')\x7f\xe3\x00\x03\x13\xe1>1\x90\xcb\xfa\xef\xbd\x8c\xe4#'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ECDSA:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ECDSA]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ECDSA, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ECDSA]]:
        return cls._deploy(request_type, [], return_tx, ECDSA, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class RecoverError(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol#13)

        """
        NoError = 0
        InvalidSignature = 1
        InvalidSignatureLength = 2
        InvalidSignatureS = 3


    @dataclasses.dataclass
    class ECDSAInvalidSignature(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol#23)
        """
        _abi = {'inputs': [], 'name': 'ECDSAInvalidSignature', 'type': 'error'}
        original_name = 'ECDSAInvalidSignature'
        selector = bytes4(b'\xf6E\xee\xdf')



    @dataclasses.dataclass
    class ECDSAInvalidSignatureLength(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol#28)

        Attributes:
            length (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'length', 'type': 'uint256'}], 'name': 'ECDSAInvalidSignatureLength', 'type': 'error'}
        original_name = 'ECDSAInvalidSignatureLength'
        selector = bytes4(b'\xfc\xe6\x98\xf7')

        length: uint256


    @dataclasses.dataclass
    class ECDSAInvalidSignatureS(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/ECDSA.sol#33)

        Attributes:
            s (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'ECDSAInvalidSignatureS', 'type': 'error'}
        original_name = 'ECDSAInvalidSignatureS'
        selector = bytes4(b'\xd7\x8b\xce\x0c')

        s: bytes32


