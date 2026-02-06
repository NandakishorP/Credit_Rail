
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC3156FlashBorrower import IERC3156FlashBorrower



class ERC3156FlashBorrowerMock(IERC3156FlashBorrower):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#16)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'bool', 'name': 'enableReturn', 'type': 'bool'}, {'internalType': 'bool', 'name': 'enableApprove', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'o\xf2\xac\xfc\xb0y\x17\xb1\xe8\x0eS\xf0\xfe9\x0bF{\x11Q\xd1[8s\nn\x089w\x99\xc0Z\x8b': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'BalanceOf', 'type': 'event'}, b'rI\xfdL\x03\xcc\xe0\x9b0\xa1=w\x80K\x19\x8e&G\xc0\xcc\xd5\x9e\xad\xf4\xdeN|\x16\t\x9b\xad\xc5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'TotalSupply', 'type': 'event'}, b'#\xe3\x0c\x8b': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': 'token', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'fee', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'onFlashLoan', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60c034607257601f6104e338819003918201601f19168301916001600160401b038311848410176076578084926040948552833981010312607257604b6020604583608a565b9201608a565b60805260a05260405161044c908161009782396080518161016e015260a051816101970152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b5190811515820360725756fe6080806040526004361015610012575f80fd5b5f3560e01c6323e30c8b14610025575f80fd5b346102705760a03660031901126102705761003e61033d565b506024356001600160a01b03811691828203610270576044359060843567ffffffffffffffff811161027057366023820112156102705780600401359167ffffffffffffffff831161027057366024848401011161027057853303610270576370a0823160e01b8152306004820152602081602481895afa90811561027c575f9161030a575b5060607f6ff2acfcb07917b1e80e53f0fe390b467b1151d15b38730a6e08397799c05a8b91604051908882523060208301526040820152a16040516318160ddd60e01b8152602081600481895afa90811561027c575f916102d6575b50604080516001600160a01b038716815260208101929092527f7249fd4c03cce09b30a13d77804b198e2647c0ccd59eadf4de4e7c16099badc59190819081015b0390a18161029b575b50507f00000000000000000000000000000000000000000000000000000000000000006101f0575b5050507f00000000000000000000000000000000000000000000000000000000000000005f146101e85760207f439148f0bbc682ca079e46d6e2c2f0c1e3b820f1a291b069d8882abf8cf18dd95b604051908152f35b60205f6101e0565b60643581018091116102875760405163095ea7b360e01b81526001600160a01b03929092166004830152602482015290602090829060449082905f905af1801561027c57610240575b8080610192565b6020813d602011610274575b8161025960209383610353565b81010312610270575180151503610270575f610239565b5f80fd5b3d915061024c565b6040513d5f823e3d90fd5b634e487b7160e01b5f52601160045260245ffd5b5f60206102ce93806024604051956102bc85601f19601f8601160188610353565b82875201838601378301015283610389565b505f8061016a565b90506020813d602011610302575b816102f160209383610353565b810103126102705751610161610120565b3d91506102e4565b90506020813d602011610335575b8161032560209383610353565b81010312610270575160606100c4565b3d9150610318565b600435906001600160a01b038216820361027057565b90601f8019910116810190811067ffffffffffffffff82111761037557604052565b634e487b7160e01b5f52604160045260245ffd5b905f809160208151910182855af18080610403575b156103be5750506040513d81523d5f602083013e60203d82010160405290565b156103e357639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d156103f4576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d15158061039e5750813b151561039e56fea26469706673582212200a33a2bbc71921339f7acfc0d6f142c285cafc210d413a10f931a2c93583e28f64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        ...

    @overload
    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC3156FlashBorrowerMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        ...

    @overload
    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        ...

    @overload
    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        ...

    @overload
    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC3156FlashBorrowerMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        ...

    @classmethod
    def deploy(cls, enableReturn: bool, enableApprove: bool, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC3156FlashBorrowerMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC3156FlashBorrowerMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#25)

        Args:
            enableReturn: bool
            enableApprove: bool
        """
        return cls._deploy(request_type, [enableReturn, enableApprove], return_tx, ERC3156FlashBorrowerMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class BalanceOf:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#22)

        Attributes:
            token (Address): address
            account (Address): address
            value (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'BalanceOf', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'BalanceOf'
        selector = bytes32(b'o\xf2\xac\xfc\xb0y\x17\xb1\xe8\x0eS\xf0\xfe9\x0bF{\x11Q\xd1[8s\nn\x089w\x99\xc0Z\x8b')

        token: Address
        account: Address
        value: uint256


    @dataclasses.dataclass
    class TotalSupply:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#23)

        Attributes:
            token (Address): address
            value (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'TotalSupply', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TotalSupply'
        selector = bytes32(b'rI\xfdL\x03\xcc\xe0\x9b0\xa1=w\x80K\x19\x8e&G\xc0\xcc\xd5\x9e\xad\xf4\xdeN|\x16\t\x9b\xad\xc5')

        token: Address
        value: uint256


    @overload
    def onFlashLoan(self, arg1: Union[Account, Address], token: Union[Account, Address], amount: uint256, fee: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#30)

        Args:
            arg1: address
            token: address
            amount: uint256
            fee: uint256
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def onFlashLoan(self, arg1: Union[Account, Address], token: Union[Account, Address], amount: uint256, fee: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#30)

        Args:
            arg1: address
            token: address
            amount: uint256
            fee: uint256
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def onFlashLoan(self, arg1: Union[Account, Address], token: Union[Account, Address], amount: uint256, fee: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#30)

        Args:
            arg1: address
            token: address
            amount: uint256
            fee: uint256
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def onFlashLoan(self, arg1: Union[Account, Address], token: Union[Account, Address], amount: uint256, fee: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#30)

        Args:
            arg1: address
            token: address
            amount: uint256
            fee: uint256
            data: bytes
        Returns:
            bytes32
        """
        ...

    def onFlashLoan(self, arg1: Union[Account, Address], token: Union[Account, Address], amount: uint256, fee: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC3156FlashBorrowerMock.sol#30)

        Args:
            arg1: address
            token: address
            amount: uint256
            fee: uint256
            data: bytes
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "23e30c8b", [arg1, token, amount, fee, data], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC3156FlashBorrowerMock.onFlashLoan.selector = bytes4(b'#\xe3\x0c\x8b')
