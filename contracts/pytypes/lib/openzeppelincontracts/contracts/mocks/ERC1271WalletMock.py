
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.access.Ownable import Ownable
from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC1271 import IERC1271



class ERC1271WalletMock(IERC1271, Ownable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#9)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'originalOwner', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xf6E\xee\xdf': {'inputs': [], 'name': 'ECDSAInvalidSignature', 'type': 'error'}, b'\xfc\xe6\x98\xf7': {'inputs': [{'internalType': 'uint256', 'name': 'length', 'type': 'uint256'}], 'name': 'ECDSAInvalidSignatureLength', 'type': 'error'}, b'\xd7\x8b\xce\x0c': {'inputs': [{'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'ECDSAInvalidSignatureS', 'type': 'error'}, b'\x1eO\xbd\xf7': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'OwnableInvalidOwner', 'type': 'error'}, b'\x11\x8c\xda\xa7': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'OwnableUnauthorizedAccount', 'type': 'error'}, b'\x8b\xe0\x07\x9cS\x16Y\x14\x13D\xcd\x1f\xd0\xa4\xf2\x84\x19I\x7f\x97"\xa3\xda\xaf\xe3\xb4\x18okdW\xe0': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'previousOwner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnershipTransferred', 'type': 'event'}, b'\x16&\xba~': {'inputs': [{'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'isValidSignature', 'outputs': [{'internalType': 'bytes4', 'name': 'magicValue', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8d\xa5\xcb[': {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'qP\x18\xa6': {'inputs': [], 'name': 'renounceOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xfd\xe3\x8b': {'inputs': [{'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'transferOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol:ERC1271WalletMock","label":"_owner","offset":0,"slot":0,"type":"t_address"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20}}}
    _creation_code = "60803460b857601f61049f38819003918201601f19168301916001600160401b0383118484101760bc5780849260209460405283398101031260b857516001600160a01b0381169081900360b857801560a5575f80546001600160a01b031981168317825560405192916001600160a01b03909116907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e09080a36103ce90816100d18239f35b631e4fbdf760e01b5f525f60045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe6080806040526004361015610012575f80fd5b5f3560e01c9081631626ba7e1461015357508063715018a6146100fc5780638da5cb5b146100d55763f2fde38b14610048575f80fd5b346100d15760203660031901126100d1576004356001600160a01b038116908190036100d157610076610241565b80156100be575f80546001600160a01b03198116831782556001600160a01b0316907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e09080a3005b631e4fbdf760e01b5f525f60045260245ffd5b5f80fd5b346100d1575f3660031901126100d1575f546040516001600160a01b039091168152602090f35b346100d1575f3660031901126100d157610114610241565b5f80546001600160a01b0319811682556001600160a01b03167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08280a3005b346100d15760403660031901126100d15760243567ffffffffffffffff81116100d157366023820112156100d15780600401359167ffffffffffffffff831161022d57601f8301601f19908116603f0116810167ffffffffffffffff81118282101761022d5760405282815236602484840101116100d1575f6020846101f39560246101ea96018386013783010152600435610267565b909291926102a1565b5f546001600160a01b03918216911603610225576020630b135d3f60e11b5b6040516001600160e01b03199091168152f35b60205f610212565b634e487b7160e01b5f52604160045260245ffd5b5f546001600160a01b0316330361025457565b63118cdaa760e01b5f523360045260245ffd5b8151919060418303610297576102909250602082015190606060408401519301515f1a90610315565b9192909190565b50505f9160029190565b600481101561030157806102b3575050565b600181036102ca5763f645eedf60e01b5f5260045ffd5b600281036102e5575063fce698f760e01b5f5260045260245ffd5b6003146102ef5750565b6335e2f38360e21b5f5260045260245ffd5b634e487b7160e01b5f52602160045260245ffd5b91906fa2a8918ca85bafe22016d0b997e4df60600160ff1b03841161038d579160209360809260ff5f9560405194855216868401526040830152606082015282805260015afa15610382575f516001600160a01b0381161561037857905f905f90565b505f906001905f90565b6040513d5f823e3d90fd5b5050505f916003919056fea2646970667358221220f3f234e9e74966bf2f610eb11df261282979c64c15cb39e445ed46b924d1e80d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1271WalletMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1271WalletMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        ...

    @classmethod
    def deploy(cls, originalOwner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1271WalletMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1271WalletMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#10)

        Args:
            originalOwner: address
        """
        return cls._deploy(request_type, [originalOwner], return_tx, ERC1271WalletMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#12)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            magicValue: bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#12)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            magicValue: bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#12)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            magicValue: bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#12)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            magicValue: bytes4
        """
        ...

    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#12)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            magicValue: bytes4
        """
        return self._execute(self.chain, request_type, "1626ba7e", [hash, signature], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC1271WalletMock.isValidSignature.selector = bytes4(b'\x16&\xba~')
class ERC1271MaliciousMock(IERC1271):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#17)
    """
    _abi = {b'\x16&\xba~': {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'isValidSignature', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'pure', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60808060405234601557610102908161001a8239f35b5f80fdfe608060405260043610156010575f80fd5b5f3560e01c631626ba7e146022575f80fd5b3460ab57604036600319011260ab5760243567ffffffffffffffff811160ab573660238201121560ab5780600401359067ffffffffffffffff821160af5760405191601f8101601f19908116603f0116830167ffffffffffffffff81118482101760af57604052808352366024828401011160ab575f92816024602094018483013701015260c3565b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b5f195f5260205ff3fea2646970667358221220ab0959d667516915940ef3ba8ff000aa5e00b5348166feca30dfa6ed3d6212f864736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1271MaliciousMock:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1271MaliciousMock]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1271MaliciousMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1271MaliciousMock]]:
        return cls._deploy(request_type, [], return_tx, ERC1271MaliciousMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def isValidSignature(self, arg1: bytes32, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#18)

        Args:
            arg1: bytes32
            arg2: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, arg1: bytes32, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#18)

        Args:
            arg1: bytes32
            arg2: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, arg1: bytes32, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#18)

        Args:
            arg1: bytes32
            arg2: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, arg1: bytes32, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#18)

        Args:
            arg1: bytes32
            arg2: bytes
        Returns:
            bytes4
        """
        ...

    def isValidSignature(self, arg1: bytes32, arg2: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC1271WalletMock.sol#18)

        Args:
            arg1: bytes32
            arg2: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "1626ba7e", [arg1, arg2], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC1271MaliciousMock.isValidSignature.selector = bytes4(b'\x16&\xba~')
