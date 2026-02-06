
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.interfaces.IERC7575 import IERC7575



class IERC7540Operator(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#8)
    """
    _abi = {b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': 'status', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC7540Operator:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC7540Operator]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC7540Operator, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC7540Operator]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class OperatorSet:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#16)

        Attributes:
            controller (Address): indexed address
            operator (Address): indexed address
            approved (bool): bool
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'OperatorSet'
        selector = bytes32(b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g')

        controller: Address
        operator: Address
        approved: bool


    @overload
    def setOperator(self, operator: Union[Account, Address], approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#25)

        Args:
            operator: address
            approved: bool
        Returns:
            bool
        """
        ...

    @overload
    def setOperator(self, operator: Union[Account, Address], approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#25)

        Args:
            operator: address
            approved: bool
        Returns:
            bool
        """
        ...

    @overload
    def setOperator(self, operator: Union[Account, Address], approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#25)

        Args:
            operator: address
            approved: bool
        Returns:
            bool
        """
        ...

    @overload
    def setOperator(self, operator: Union[Account, Address], approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#25)

        Args:
            operator: address
            approved: bool
        Returns:
            bool
        """
        ...

    def setOperator(self, operator: Union[Account, Address], approved: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#25)

        Args:
            operator: address
            approved: bool
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "558a7297", [operator, approved], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isOperator(self, controller: Union[Account, Address], operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#34)

        Args:
            controller: address
            operator: address
        Returns:
            status: bool
        """
        ...

    @overload
    def isOperator(self, controller: Union[Account, Address], operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#34)

        Args:
            controller: address
            operator: address
        Returns:
            status: bool
        """
        ...

    @overload
    def isOperator(self, controller: Union[Account, Address], operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#34)

        Args:
            controller: address
            operator: address
        Returns:
            status: bool
        """
        ...

    @overload
    def isOperator(self, controller: Union[Account, Address], operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#34)

        Args:
            controller: address
            operator: address
        Returns:
            status: bool
        """
        ...

    def isOperator(self, controller: Union[Account, Address], operator: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#34)

        Args:
            controller: address
            operator: address
        Returns:
            status: bool
        """
        return self._execute(self.chain, request_type, "b6363cf2", [controller, operator], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IERC7540Operator.setOperator.selector = bytes4(b'U\x8ar\x97')
IERC7540Operator.isOperator.selector = bytes4(b'\xb66<\xf2')
class IERC7540Deposit(IERC7540Operator):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#39)
    """
    _abi = {b'\xbbXB\x0b\xb8\xceD\xe1\x1b\x84\xe2\x14\xcc\r\xe1\x0c\xe5\xe7\xc2M\x03U\xb2\x81\\=u\x8bQL\xaer': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'DepositRequest', 'type': 'event'}, b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x99^\xa2\x1a': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'claimableDepositRequest', 'outputs': [{'internalType': 'uint256', 'name': 'claimableAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'.-)\x84': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'deposit', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': 'status', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xda9\xb3\xe7': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'&\xc6\xf9l': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'pendingDepositRequest', 'outputs': [{'internalType': 'uint256', 'name': 'pendingAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85\xb7\x7fE': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'requestDeposit', 'outputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC7540Deposit:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC7540Deposit]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC7540Deposit, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC7540Deposit]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class DepositRequest:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#40)

        Attributes:
            controller (Address): indexed address
            owner (Address): indexed address
            requestId (uint256): indexed uint256
            sender (Address): address
            assets (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'DepositRequest', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'DepositRequest'
        selector = bytes32(b'\xbbXB\x0b\xb8\xceD\xe1\x1b\x84\xe2\x14\xcc\r\xe1\x0c\xe5\xe7\xc2M\x03U\xb2\x81\\=u\x8bQL\xaer')

        controller: Address
        owner: Address
        requestId: uint256
        sender: Address
        assets: uint256


    @overload
    def requestDeposit(self, assets: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#58)

        Args:
            assets: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestDeposit(self, assets: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#58)

        Args:
            assets: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestDeposit(self, assets: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#58)

        Args:
            assets: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestDeposit(self, assets: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#58)

        Args:
            assets: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    def requestDeposit(self, assets: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#58)

        Args:
            assets: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        return self._execute(self.chain, request_type, "85b77f45", [assets, controller, owner], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def pendingDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#67)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingAssets: uint256
        """
        ...

    @overload
    def pendingDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#67)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingAssets: uint256
        """
        ...

    @overload
    def pendingDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#67)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingAssets: uint256
        """
        ...

    @overload
    def pendingDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#67)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingAssets: uint256
        """
        ...

    def pendingDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#67)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingAssets: uint256
        """
        return self._execute(self.chain, request_type, "26c6f96c", [requestId, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def claimableDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#76)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableAssets: uint256
        """
        ...

    @overload
    def claimableDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#76)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableAssets: uint256
        """
        ...

    @overload
    def claimableDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#76)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableAssets: uint256
        """
        ...

    @overload
    def claimableDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#76)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableAssets: uint256
        """
        ...

    def claimableDepositRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#76)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableAssets: uint256
        """
        return self._execute(self.chain, request_type, "995ea21a", [requestId, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deposit(self, assets: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#87)

        Args:
            assets: uint256
            receiver: address
            controller: address
        Returns:
            shares: uint256
        """
        ...

    @overload
    def deposit(self, assets: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#87)

        Args:
            assets: uint256
            receiver: address
            controller: address
        Returns:
            shares: uint256
        """
        ...

    @overload
    def deposit(self, assets: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#87)

        Args:
            assets: uint256
            receiver: address
            controller: address
        Returns:
            shares: uint256
        """
        ...

    @overload
    def deposit(self, assets: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#87)

        Args:
            assets: uint256
            receiver: address
            controller: address
        Returns:
            shares: uint256
        """
        ...

    def deposit(self, assets: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#87)

        Args:
            assets: uint256
            receiver: address
            controller: address
        Returns:
            shares: uint256
        """
        return self._execute(self.chain, request_type, "2e2d2984", [assets, receiver, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def mint(self, shares: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#95)

        Args:
            shares: uint256
            receiver: address
            controller: address
        Returns:
            assets: uint256
        """
        ...

    @overload
    def mint(self, shares: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#95)

        Args:
            shares: uint256
            receiver: address
            controller: address
        Returns:
            assets: uint256
        """
        ...

    @overload
    def mint(self, shares: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#95)

        Args:
            shares: uint256
            receiver: address
            controller: address
        Returns:
            assets: uint256
        """
        ...

    @overload
    def mint(self, shares: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#95)

        Args:
            shares: uint256
            receiver: address
            controller: address
        Returns:
            assets: uint256
        """
        ...

    def mint(self, shares: uint256, receiver: Union[Account, Address], controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#95)

        Args:
            shares: uint256
            receiver: address
            controller: address
        Returns:
            assets: uint256
        """
        return self._execute(self.chain, request_type, "da39b3e7", [shares, receiver, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IERC7540Deposit.requestDeposit.selector = bytes4(b'\x85\xb7\x7fE')
IERC7540Deposit.pendingDepositRequest.selector = bytes4(b'&\xc6\xf9l')
IERC7540Deposit.claimableDepositRequest.selector = bytes4(b'\x99^\xa2\x1a')
IERC7540Deposit.deposit.selector = bytes4(b'.-)\x84')
IERC7540Deposit.mint.selector = bytes4(b'\xda9\xb3\xe7')
class IERC7540Redeem(IERC7540Operator):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#100)
    """
    _abi = {b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x1f\xdch\x1a\x13\xd8\xc5\xdaT\xe3\x01\xc7\xceeB\xdc\xdeE\x81\xe4rPC\xfd\xab-\xb1-\xdcWE\x06': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'RedeemRequest', 'type': 'event'}, b'\xea\xed\x1d\x07': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'claimableRedeemRequest', 'outputs': [{'internalType': 'uint256', 'name': 'claimableShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': 'status', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf5\xa2=\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'pendingRedeemRequest', 'outputs': [{'internalType': 'uint256', 'name': 'pendingShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'}A\xc8n': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'requestRedeem', 'outputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC7540Redeem:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC7540Redeem]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC7540Redeem, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC7540Redeem]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class RedeemRequest:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#101)

        Attributes:
            controller (Address): indexed address
            owner (Address): indexed address
            requestId (uint256): indexed uint256
            sender (Address): address
            assets (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'RedeemRequest', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RedeemRequest'
        selector = bytes32(b'\x1f\xdch\x1a\x13\xd8\xc5\xdaT\xe3\x01\xc7\xceeB\xdc\xdeE\x81\xe4rPC\xfd\xab-\xb1-\xdcWE\x06')

        controller: Address
        owner: Address
        requestId: uint256
        sender: Address
        assets: uint256


    @overload
    def requestRedeem(self, shares: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#118)

        Args:
            shares: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestRedeem(self, shares: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#118)

        Args:
            shares: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestRedeem(self, shares: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#118)

        Args:
            shares: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    @overload
    def requestRedeem(self, shares: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#118)

        Args:
            shares: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        ...

    def requestRedeem(self, shares: uint256, controller: Union[Account, Address], owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#118)

        Args:
            shares: uint256
            controller: address
            owner: address
        Returns:
            requestId: uint256
        """
        return self._execute(self.chain, request_type, "7d41c86e", [shares, controller, owner], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def pendingRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#127)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingShares: uint256
        """
        ...

    @overload
    def pendingRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#127)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingShares: uint256
        """
        ...

    @overload
    def pendingRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#127)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingShares: uint256
        """
        ...

    @overload
    def pendingRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#127)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingShares: uint256
        """
        ...

    def pendingRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#127)

        Args:
            requestId: uint256
            controller: address
        Returns:
            pendingShares: uint256
        """
        return self._execute(self.chain, request_type, "f5a23d8d", [requestId, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def claimableRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#136)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableShares: uint256
        """
        ...

    @overload
    def claimableRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#136)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableShares: uint256
        """
        ...

    @overload
    def claimableRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#136)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableShares: uint256
        """
        ...

    @overload
    def claimableRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#136)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableShares: uint256
        """
        ...

    def claimableRedeemRequest(self, requestId: uint256, controller: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#136)

        Args:
            requestId: uint256
            controller: address
        Returns:
            claimableShares: uint256
        """
        return self._execute(self.chain, request_type, "eaed1d07", [requestId, controller], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IERC7540Redeem.requestRedeem.selector = bytes4(b'}A\xc8n')
IERC7540Redeem.pendingRedeemRequest.selector = bytes4(b'\xf5\xa2=\x8d')
IERC7540Redeem.claimableRedeemRequest.selector = bytes4(b'\xea\xed\x1d\x07')
class IERC7540(IERC7575, IERC7540Redeem, IERC7540Deposit):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/interfaces/IERC7540.sol#144)
    """
    _abi = {b'\xdc\xbc\x1c\x05$\x0f1\xff:\xd0g\xef\x1e\xe3\\\xe4\x99wbu.:\tR\x84uED\xf4\xc7\t\xd7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'name': 'Deposit', 'type': 'event'}, b'\xbbXB\x0b\xb8\xceD\xe1\x1b\x84\xe2\x14\xcc\r\xe1\x0c\xe5\xe7\xc2M\x03U\xb2\x81\\=u\x8bQL\xaer': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'DepositRequest', 'type': 'event'}, b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x1f\xdch\x1a\x13\xd8\xc5\xdaT\xe3\x01\xc7\xceeB\xdc\xdeE\x81\xe4rPC\xfd\xab-\xb1-\xdcWE\x06': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'RedeemRequest', 'type': 'event'}, b'\xfb\xdey} \x1ch\x1b\x91\x05e)\x11\x9e\x0b\x02@|{\xb9jJ,u\xc0\x1f\xc9fr2\xc8\xdb': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'name': 'Withdraw', 'type': 'event'}, b'8\xd5.\x0f': {'inputs': [], 'name': 'asset', 'outputs': [{'internalType': 'address', 'name': 'assetTokenAddress', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99^\xa2\x1a': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'claimableDepositRequest', 'outputs': [{'internalType': 'uint256', 'name': 'claimableAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xea\xed\x1d\x07': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'claimableRedeemRequest', 'outputs': [{'internalType': 'uint256', 'name': 'claimableShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x07\xa2\xd1:': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'name': 'convertToAssets', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc6\xe6\xf5\x92': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'convertToShares', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'.-)\x84': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'deposit', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'nU?e': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'deposit', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': 'status', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'@-&}': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'maxDeposit', 'outputs': [{'internalType': 'uint256', 'name': 'maxAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc6=u\xb6': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'maxMint', 'outputs': [{'internalType': 'uint256', 'name': 'maxShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd9\x05w~': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'maxRedeem', 'outputs': [{'internalType': 'uint256', 'name': 'maxShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xce\x96\xcbw': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'maxWithdraw', 'outputs': [{'internalType': 'uint256', 'name': 'maxAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x94\xbf\x80M': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xda9\xb3\xe7': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'&\xc6\xf9l': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'pendingDepositRequest', 'outputs': [{'internalType': 'uint256', 'name': 'pendingAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf5\xa2=\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}], 'name': 'pendingRedeemRequest', 'outputs': [{'internalType': 'uint256', 'name': 'pendingShares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xef\x8b0\xf7': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'previewDeposit', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb3\xd7\xf6\xb9': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'name': 'previewMint', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'L\xda\xd5\x06': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'name': 'previewRedeem', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\n(\xa4w': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'name': 'previewWithdraw', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xba\x08vR': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'redeem', 'outputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x85\xb7\x7fE': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'requestDeposit', 'outputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'}A\xc8n': {'inputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}, {'internalType': 'address', 'name': 'controller', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'requestRedeem', 'outputs': [{'internalType': 'uint256', 'name': 'requestId', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa8\xd5\xfde': {'inputs': [], 'name': 'share', 'outputs': [{'internalType': 'address', 'name': 'shareTokenAddress', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceID', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xe1\xd1\x14': {'inputs': [], 'name': 'totalAssets', 'outputs': [{'internalType': 'uint256', 'name': 'totalManagedAssets', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb4`\xaf\x94': {'inputs': [{'internalType': 'uint256', 'name': 'assets', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'withdraw', 'outputs': [{'internalType': 'uint256', 'name': 'shares', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC7540:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC7540]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC7540, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC7540]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

