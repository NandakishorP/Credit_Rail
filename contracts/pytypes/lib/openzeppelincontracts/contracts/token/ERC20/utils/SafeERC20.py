
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class SafeERC20(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol#18)
    """
    _abi = {b'\xe5p\x11\x0f': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentAllowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'requestedDecrease', 'type': 'uint256'}], 'name': 'SafeERC20FailedDecreaseAllowance', 'type': 'error'}, b'Rt\xaf\xe7': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'SafeERC20FailedOperation', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220bc7716218a5f36ccdc0da8f710c37c85ebf2c3763dfa037034f707c9f734981b64736f6c63430008210033"

    _library_id = b'ww@#\xe8P+\xd4\x18t*\xf1:\xb4\x89\xeeX'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SafeERC20:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SafeERC20]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SafeERC20, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SafeERC20]]:
        return cls._deploy(request_type, [], return_tx, SafeERC20, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class SafeERC20FailedOperation(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol#22)

        Attributes:
            token (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'SafeERC20FailedOperation', 'type': 'error'}
        original_name = 'SafeERC20FailedOperation'
        selector = bytes4(b'Rt\xaf\xe7')

        token: Address


    @dataclasses.dataclass
    class SafeERC20FailedDecreaseAllowance(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol#27)

        Attributes:
            spender (Address): address
            currentAllowance (uint256): uint256
            requestedDecrease (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentAllowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'requestedDecrease', 'type': 'uint256'}], 'name': 'SafeERC20FailedDecreaseAllowance', 'type': 'error'}
        original_name = 'SafeERC20FailedDecreaseAllowance'
        selector = bytes4(b'\xe5p\x11\x0f')

        spender: Address
        currentAllowance: uint256
        requestedDecrease: uint256


