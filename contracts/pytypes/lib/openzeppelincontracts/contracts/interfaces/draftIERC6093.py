
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class IERC20Errors(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#10)
    """
    _abi = {b'\xfb\x8fA\xb2': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientAllowance', 'type': 'error'}, b'\xe4P\xd3\x8c': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientBalance', 'type': 'error'}, b'\xe6\x02\xdf\x05': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC20InvalidApprover', 'type': 'error'}, b'\xecD/\x05': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC20InvalidReceiver', 'type': 'error'}, b'\x96\xc6\xfd\x1e': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC20InvalidSender', 'type': 'error'}, b'\x94(\rb': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC20InvalidSpender', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC20Errors:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC20Errors]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC20Errors, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC20Errors]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class ERC20InsufficientBalance(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#17)

        Attributes:
            sender (Address): address
            balance (uint256): uint256
            needed (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientBalance', 'type': 'error'}
        original_name = 'ERC20InsufficientBalance'
        selector = bytes4(b'\xe4P\xd3\x8c')

        sender: Address
        balance: uint256
        needed: uint256


    @dataclasses.dataclass
    class ERC20InvalidSender(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#23)

        Attributes:
            sender (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC20InvalidSender', 'type': 'error'}
        original_name = 'ERC20InvalidSender'
        selector = bytes4(b'\x96\xc6\xfd\x1e')

        sender: Address


    @dataclasses.dataclass
    class ERC20InvalidReceiver(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#29)

        Attributes:
            receiver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC20InvalidReceiver', 'type': 'error'}
        original_name = 'ERC20InvalidReceiver'
        selector = bytes4(b'\xecD/\x05')

        receiver: Address


    @dataclasses.dataclass
    class ERC20InsufficientAllowance(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#37)

        Attributes:
            spender (Address): address
            allowance (uint256): uint256
            needed (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientAllowance', 'type': 'error'}
        original_name = 'ERC20InsufficientAllowance'
        selector = bytes4(b'\xfb\x8fA\xb2')

        spender: Address
        allowance: uint256
        needed: uint256


    @dataclasses.dataclass
    class ERC20InvalidApprover(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#43)

        Attributes:
            approver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC20InvalidApprover', 'type': 'error'}
        original_name = 'ERC20InvalidApprover'
        selector = bytes4(b'\xe6\x02\xdf\x05')

        approver: Address


    @dataclasses.dataclass
    class ERC20InvalidSpender(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#49)

        Attributes:
            spender (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC20InvalidSpender', 'type': 'error'}
        original_name = 'ERC20InvalidSpender'
        selector = bytes4(b'\x94(\rb')

        spender: Address


class IERC721Errors(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#56)
    """
    _abi = {b'd(={': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721IncorrectOwner', 'type': 'error'}, b'\x17~\x80/': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721InsufficientApproval', 'type': 'error'}, b'\xa9\xfb\xf5\x1f': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC721InvalidApprover', 'type': 'error'}, b'[\x08\xba\x18': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'ERC721InvalidOperator', 'type': 'error'}, b'\x89\xc6+d': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721InvalidOwner', 'type': 'error'}, b'd\xa0\xae\x92': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC721InvalidReceiver', 'type': 'error'}, b's\xc6\xacn': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC721InvalidSender', 'type': 'error'}, b"~'2\x89": {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721NonexistentToken', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC721Errors:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC721Errors]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC721Errors, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC721Errors]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class ERC721InvalidOwner(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#62)

        Attributes:
            owner (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721InvalidOwner', 'type': 'error'}
        original_name = 'ERC721InvalidOwner'
        selector = bytes4(b'\x89\xc6+d')

        owner: Address


    @dataclasses.dataclass
    class ERC721NonexistentToken(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#68)

        Attributes:
            tokenId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721NonexistentToken', 'type': 'error'}
        original_name = 'ERC721NonexistentToken'
        selector = bytes4(b"~'2\x89")

        tokenId: uint256


    @dataclasses.dataclass
    class ERC721IncorrectOwner(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#76)

        Attributes:
            sender (Address): address
            tokenId (uint256): uint256
            owner (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC721IncorrectOwner', 'type': 'error'}
        original_name = 'ERC721IncorrectOwner'
        selector = bytes4(b'd(={')

        sender: Address
        tokenId: uint256
        owner: Address


    @dataclasses.dataclass
    class ERC721InvalidSender(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#82)

        Attributes:
            sender (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC721InvalidSender', 'type': 'error'}
        original_name = 'ERC721InvalidSender'
        selector = bytes4(b's\xc6\xacn')

        sender: Address


    @dataclasses.dataclass
    class ERC721InvalidReceiver(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#88)

        Attributes:
            receiver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC721InvalidReceiver', 'type': 'error'}
        original_name = 'ERC721InvalidReceiver'
        selector = bytes4(b'd\xa0\xae\x92')

        receiver: Address


    @dataclasses.dataclass
    class ERC721InsufficientApproval(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#95)

        Attributes:
            operator (Address): address
            tokenId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC721InsufficientApproval', 'type': 'error'}
        original_name = 'ERC721InsufficientApproval'
        selector = bytes4(b'\x17~\x80/')

        operator: Address
        tokenId: uint256


    @dataclasses.dataclass
    class ERC721InvalidApprover(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#101)

        Attributes:
            approver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC721InvalidApprover', 'type': 'error'}
        original_name = 'ERC721InvalidApprover'
        selector = bytes4(b'\xa9\xfb\xf5\x1f')

        approver: Address


    @dataclasses.dataclass
    class ERC721InvalidOperator(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#107)

        Attributes:
            operator (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'ERC721InvalidOperator', 'type': 'error'}
        original_name = 'ERC721InvalidOperator'
        selector = bytes4(b'[\x08\xba\x18')

        operator: Address


class IERC1155Errors(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#114)
    """
    _abi = {b'\x03\xde\xe4\xc5': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC1155InsufficientBalance', 'type': 'error'}, b'>1\x88N': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC1155InvalidApprover', 'type': 'error'}, b'[\x05\x99\x91': {'inputs': [{'internalType': 'uint256', 'name': 'idsLength', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'valuesLength', 'type': 'uint256'}], 'name': 'ERC1155InvalidArrayLength', 'type': 'error'}, b'\xce\xd3\xe1\x00': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'ERC1155InvalidOperator', 'type': 'error'}, b'W\xf4G\xce': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC1155InvalidReceiver', 'type': 'error'}, b'\x01\xa85\x14': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC1155InvalidSender', 'type': 'error'}, b'\xe27\xd9"': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC1155MissingApprovalForAll', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IERC1155Errors:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IERC1155Errors]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IERC1155Errors, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IERC1155Errors]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class ERC1155InsufficientBalance(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#122)

        Attributes:
            sender (Address): address
            balance (uint256): uint256
            needed (uint256): uint256
            tokenId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ERC1155InsufficientBalance', 'type': 'error'}
        original_name = 'ERC1155InsufficientBalance'
        selector = bytes4(b'\x03\xde\xe4\xc5')

        sender: Address
        balance: uint256
        needed: uint256
        tokenId: uint256


    @dataclasses.dataclass
    class ERC1155InvalidSender(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#128)

        Attributes:
            sender (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC1155InvalidSender', 'type': 'error'}
        original_name = 'ERC1155InvalidSender'
        selector = bytes4(b'\x01\xa85\x14')

        sender: Address


    @dataclasses.dataclass
    class ERC1155InvalidReceiver(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#134)

        Attributes:
            receiver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC1155InvalidReceiver', 'type': 'error'}
        original_name = 'ERC1155InvalidReceiver'
        selector = bytes4(b'W\xf4G\xce')

        receiver: Address


    @dataclasses.dataclass
    class ERC1155MissingApprovalForAll(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#141)

        Attributes:
            operator (Address): address
            owner (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'ERC1155MissingApprovalForAll', 'type': 'error'}
        original_name = 'ERC1155MissingApprovalForAll'
        selector = bytes4(b'\xe27\xd9"')

        operator: Address
        owner: Address


    @dataclasses.dataclass
    class ERC1155InvalidApprover(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#147)

        Attributes:
            approver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC1155InvalidApprover', 'type': 'error'}
        original_name = 'ERC1155InvalidApprover'
        selector = bytes4(b'>1\x88N')

        approver: Address


    @dataclasses.dataclass
    class ERC1155InvalidOperator(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#153)

        Attributes:
            operator (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'ERC1155InvalidOperator', 'type': 'error'}
        original_name = 'ERC1155InvalidOperator'
        selector = bytes4(b'\xce\xd3\xe1\x00')

        operator: Address


    @dataclasses.dataclass
    class ERC1155InvalidArrayLength(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol#161)

        Attributes:
            idsLength (uint256): uint256
            valuesLength (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'idsLength', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'valuesLength', 'type': 'uint256'}], 'name': 'ERC1155InvalidArrayLength', 'type': 'error'}
        original_name = 'ERC1155InvalidArrayLength'
        selector = bytes4(b'[\x05\x99\x91')

        idsLength: uint256
        valuesLength: uint256


