
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.proxy.utils.Initializable import Initializable



class SampleHuman(Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#21)
    """
    _abi = {b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\x81)\xfc\x1c': {'inputs': [], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Jl\x9d\xb6': {'inputs': [], 'name': 'isHuman', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleHuman","label":"isHuman","offset":0,"slot":0,"type":"t_bool"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1}}}
    _creation_code = "60808060405234601557610216908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c9081634a6c9db6146101775750638129fc1c14610032575f80fd5b34610173575f366003190112610173575f5160206101c15f395f51905f525460ff8160401c16159067ffffffffffffffff81168015908161016b575b6001149081610161575b159081610158575b506101495767ffffffffffffffff1981166001175f5160206101c15f395f51905f52558161011d575b506100b2610195565b6100ba610195565b600160ff195f5416175f556100cb57005b60ff60401b195f5160206101c15f395f51905f5254165f5160206101c15f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b68ffffffffffffffffff191668010000000000000001175f5160206101c15f395f51905f52555f6100a9565b63f92ee8a960e01b5f5260045ffd5b9050155f610080565b303b159150610078565b83915061006e565b5f80fd5b34610173575f3660031901126101735760209060ff5f541615158152f35b60ff5f5160206101c15f395f51905f525460401c16156101b157565b631afcd79f60e31b5f5260045ffdfef0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00a2646970667358221220017a770932175a1ef12dcd18260964b73af4349583ff30a8558834e15bde7e9864736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SampleHuman:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SampleHuman]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SampleHuman, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SampleHuman]]:
        return cls._deploy(request_type, [], return_tx, SampleHuman, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def isHuman(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#22)

        Returns:
            isHuman: bool
        """
        ...

    @overload
    def isHuman(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#22)

        Returns:
            isHuman: bool
        """
        ...

    @overload
    def isHuman(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#22)

        Returns:
            isHuman: bool
        """
        ...

    @overload
    def isHuman(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#22)

        Returns:
            isHuman: bool
        """
        ...

    def isHuman(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#22)

        Returns:
            isHuman: bool
        """
        return self._execute(self.chain, request_type, "4a6c9db6", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#24)
        """
        ...

    @overload
    def initialize(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#24)
        """
        ...

    @overload
    def initialize(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#24)
        """
        ...

    @overload
    def initialize(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#24)
        """
        ...

    def initialize(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#24)
        """
        return self._execute(self.chain, request_type, "8129fc1c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

SampleHuman.isHuman.selector = bytes4(b'Jl\x9d\xb6')
SampleHuman.initialize.selector = bytes4(b'\x81)\xfc\x1c')
class SampleMother(SampleHuman, Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#42)
    """
    _abi = {b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\x81)\xfc\x1c': {'inputs': [], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfeK\x84\xdf': {'inputs': [{'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Jl\x9d\xb6': {'inputs': [], 'name': 'isHuman', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xed}\xfe\xe3': {'inputs': [], 'name': 'mother', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleMother","label":"isHuman","offset":0,"slot":0,"type":"t_bool"},{"astId":44,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleMother","label":"mother","offset":0,"slot":1,"type":"t_uint256"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080806040523460155761032e908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c9081634a6c9db614610261575080638129fc1c146101a1578063ed7dfee3146101845763fe4b84df14610048575f80fd5b34610180576020366003190112610180575f5160206102d95f395f51905f525467ffffffffffffffff60ff8260401c1615911680159081610178575b600114908161016e575b159081610165575b5061015657806100a461027f565b610132575b6100b16102ad565b6100b96102ad565b6100c16102ad565b600160ff195f5416175f556100d46102ad565b6004356001556100e057005b60ff60401b195f5160206102d95f395f51905f5254165f5160206102d95f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b5f5160206102d95f395f51905f52805460ff60401b1916600160401b1790556100a9565b63f92ee8a960e01b5f5260045ffd5b9050155f610096565b303b15915061008e565b829150610084565b5f80fd5b34610180575f366003190112610180576020600154604051908152f35b34610180575f366003190112610180575f5160206102d95f395f51905f525467ffffffffffffffff60ff8260401c1615911680159081610259575b600114908161024f575b159081610246575b5061015657806101fc61027f565b610222575b6102096102ad565b6102116102ad565b600160ff195f5416175f556100e057005b5f5160206102d95f395f51905f52805460ff60401b1916600160401b179055610201565b905015826101ee565b303b1591506101e6565b8291506101dc565b34610180575f3660031901126101805760209060ff5f541615158152f35b600167ffffffffffffffff195f5160206102d95f395f51905f525416175f5160206102d95f395f51905f5255565b60ff5f5160206102d95f395f51905f525460401c16156102c957565b631afcd79f60e31b5f5260045ffdfef0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00a26469706673582212203cc76fb1e63c1401e404472ea46224952fa04aea56a62c61fa74d92e254b8e6264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SampleMother:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SampleMother]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SampleMother, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SampleMother]]:
        return cls._deploy(request_type, [], return_tx, SampleMother, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def mother(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#43)

        Returns:
            mother: uint256
        """
        ...

    @overload
    def mother(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#43)

        Returns:
            mother: uint256
        """
        ...

    @overload
    def mother(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#43)

        Returns:
            mother: uint256
        """
        ...

    @overload
    def mother(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#43)

        Returns:
            mother: uint256
        """
        ...

    def mother(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#43)

        Returns:
            mother: uint256
        """
        return self._execute(self.chain, request_type, "ed7dfee3", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize_(self, value_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#45)

        Args:
            value_: uint256
        """
        ...

    @overload
    def initialize_(self, value_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#45)

        Args:
            value_: uint256
        """
        ...

    @overload
    def initialize_(self, value_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#45)

        Args:
            value_: uint256
        """
        ...

    @overload
    def initialize_(self, value_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#45)

        Args:
            value_: uint256
        """
        ...

    def initialize_(self, value_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#45)

        Args:
            value_: uint256
        """
        return self._execute(self.chain, request_type, "fe4b84df", [value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

SampleMother.mother.selector = bytes4(b'\xed}\xfe\xe3')
SampleMother.initialize_.selector = bytes4(b'\xfeK\x84\xdf')
class SampleGramps(SampleHuman, Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#64)
    """
    _abi = {b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\xfa9\x85\x1f': {'inputs': [], 'name': 'gramps', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x81)\xfc\x1c': {'inputs': [], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf6-\x18\x88': {'inputs': [{'internalType': 'string', 'name': 'value', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Jl\x9d\xb6': {'inputs': [], 'name': 'isHuman', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleGramps","label":"isHuman","offset":0,"slot":0,"type":"t_bool"},{"astId":91,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleGramps","label":"gramps","offset":0,"slot":1,"type":"t_string_storage"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32}}}
    _creation_code = "608080604052346015576105fa908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c9081634a6c9db6146104d5575080638129fc1c14610416578063f62d18881461013d5763fa39851f14610048575f80fd5b34610139575f36600319011261013957604051600154905f61006983610514565b80835260208301936001811690811561011e57506001146100c0575b50906100958160409303826104f3565b8151928391602083525180918160208501528484015e5f828201840152601f01601f19168101030190f35b60015f9081527fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6939250905b80821061010457509091508101602001610095610085565b9192600181602092548385880101520191019092916100ec565b60ff1916855250151560051b82016020019050610095610085565b5f80fd5b34610139576020366003190112610139576004356001600160401b03811161013957366023820112156101395780600401356001600160401b0381116103b45760405191610195601f8301601f1916602001846104f3565b818352366024838301011161013957815f9260246020930183860137830101525f5160206105a55f395f51905f52546001600160401b0360ff8260401c161591168015908161040e575b6001149081610404575b1590816103fb575b506103ec57806101ff61054c565b6103c8575b61020c610579565b610214610579565b61021c610579565b600160ff195f5416175f5561022f610579565b81516001600160401b0381116103b45761024a600154610514565b601f8111610346575b50602092601f82116001146102e557928192935f926102da575b50508160011b915f199060031b1c1916176001555b61028857005b60ff60401b195f5160206105a55f395f51905f5254165f5160206105a55f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b01519050838061026d565b601f1982169360015f52805f20915f5b86811061032e5750836001959610610316575b505050811b01600155610282565b01515f1960f88460031b161c19169055838080610308565b919260206001819286850151815501940192016102f5565b818111156102535760015f52601f820160051c7fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6602084106103ac575b81601f9101920160051c03905f5b82811061039f575050610253565b5f82820155600101610391565b5f9150610383565b634e487b7160e01b5f52604160045260245ffd5b5f5160206105a55f395f51905f52805460ff60401b1916600160401b179055610204565b63f92ee8a960e01b5f5260045ffd5b905015836101f1565b303b1591506101e9565b8291506101df565b34610139575f366003190112610139575f5160206105a55f395f51905f52546001600160401b0360ff8260401c16159116801590816104cd575b60011490816104c3575b1590816104ba575b506103ec578061047061054c565b610496575b61047d610579565b610485610579565b600160ff195f5416175f5561028857005b5f5160206105a55f395f51905f52805460ff60401b1916600160401b179055610475565b90501582610462565b303b15915061045a565b829150610450565b34610139575f3660031901126101395760209060ff5f541615158152f35b90601f801991011681019081106001600160401b038211176103b457604052565b90600182811c92168015610542575b602083101461052e57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610523565b60016001600160401b03195f5160206105a55f395f51905f525416175f5160206105a55f395f51905f5255565b60ff5f5160206105a55f395f51905f525460401c161561059557565b631afcd79f60e31b5f5260045ffdfef0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00a2646970667358221220cb327a8ba00b87825ea0001c6f864cfd2fd083593a09b20548e8ac617979453a64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SampleGramps:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SampleGramps]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SampleGramps, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SampleGramps]]:
        return cls._deploy(request_type, [], return_tx, SampleGramps, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def gramps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#65)

        Returns:
            gramps: string
        """
        ...

    @overload
    def gramps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#65)

        Returns:
            gramps: string
        """
        ...

    @overload
    def gramps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#65)

        Returns:
            gramps: string
        """
        ...

    @overload
    def gramps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#65)

        Returns:
            gramps: string
        """
        ...

    def gramps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#65)

        Returns:
            gramps: string
        """
        return self._execute(self.chain, request_type, "fa39851f", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize_(self, value_: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#67)

        Args:
            value_: string
        """
        ...

    @overload
    def initialize_(self, value_: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#67)

        Args:
            value_: string
        """
        ...

    @overload
    def initialize_(self, value_: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#67)

        Args:
            value_: string
        """
        ...

    @overload
    def initialize_(self, value_: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#67)

        Args:
            value_: string
        """
        ...

    def initialize_(self, value_: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#67)

        Args:
            value_: string
        """
        return self._execute(self.chain, request_type, "f62d1888", [value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

SampleGramps.gramps.selector = bytes4(b'\xfa9\x85\x1f')
SampleGramps.initialize_.selector = bytes4(b'\xf6-\x18\x88')
class SampleFather(SampleGramps, Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#86)
    """
    _abi = {b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\x1c\x8a\xca;': {'inputs': [], 'name': 'father', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfa9\x85\x1f': {'inputs': [], 'name': 'gramps', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x81)\xfc\x1c': {'inputs': [], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8b\xea\xf7\xd7': {'inputs': [{'internalType': 'string', 'name': '_gramps', 'type': 'string'}, {'internalType': 'uint256', 'name': '_father', 'type': 'uint256'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf6-\x18\x88': {'inputs': [{'internalType': 'string', 'name': 'value', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Jl\x9d\xb6': {'inputs': [], 'name': 'isHuman', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleFather","label":"isHuman","offset":0,"slot":0,"type":"t_bool"},{"astId":91,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleFather","label":"gramps","offset":0,"slot":1,"type":"t_string_storage"},{"astId":138,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleFather","label":"father","offset":0,"slot":2,"type":"t_uint256"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234601557610853908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c9081631c8aca3b146106bd575080634a6c9db61461069c5780638129fc1c146105dd5780638beaf7d7146103be578063f62d1888146101405763fa39851f1461005e575f80fd5b3461013c575f36600319011261013c57604051600154905f61007f8361074d565b80835260208301936001811690811561012157506001146100d6575b50906100ab8160409303826106d7565b8151928391602083525180918160208501528484015e5f828201840152601f01601f19168101030190f35b60015f9081525f5160206107de5f395f51905f52939250905b808210610107575090915081016020016100ab61009b565b9192600181602092548385880101520191019092916100ef565b60ff1916855250151560051b820160200190506100ab61009b565b5f80fd5b3461013c57602036600319011261013c576004356001600160401b03811161013c576101709036906004016106f8565b5f5160206107fe5f395f51905f52546001600160401b0360ff8260401c16159116801590816103b6575b60011490816103ac575b1590816103a3575b5061039457806101ba610785565b610370575b6101c76107b2565b6101cf6107b2565b6101d76107b2565b600160ff195f5416175f556101ea6107b2565b81516001600160401b03811161035c5761020560015461074d565b601f8111610301575b50602092601f82116001146102a057928192935f92610295575b50508160011b915f199060031b1c1916176001555b61024357005b60ff60401b195f5160206107fe5f395f51905f5254165f5160206107fe5f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b015190508380610228565b601f1982169360015f52805f20915f5b8681106102e957508360019596106102d1575b505050811b0160015561023d565b01515f1960f88460031b161c191690558380806102c3565b919260206001819286850151815501940192016102b0565b8181111561020e5760015f52601f820160051c5f5160206107de5f395f51905f5260208410610354575b81601f9101920160051c03905f5b82811061034757505061020e565b5f82820155600101610339565b5f915061032b565b634e487b7160e01b5f52604160045260245ffd5b5f5160206107fe5f395f51905f52805460ff60401b1916600160401b1790556101bf565b63f92ee8a960e01b5f5260045ffd5b905015836101ac565b303b1591506101a4565b82915061019a565b3461013c57604036600319011261013c576004356001600160401b03811161013c576103ee9036906004016106f8565b5f5160206107fe5f395f51905f52546001600160401b0360ff8260401c16159116801590816105d5575b60011490816105cb575b1590816105c2575b506103945780610438610785565b61059e575b6104456107b2565b61044d6107b2565b6104556107b2565b61045d6107b2565b600160ff195f5416175f556104706107b2565b81516001600160401b03811161035c5761048b60015461074d565b601f8111610543575b50602092601f82116001146104e257928192935f926104d7575b50508160011b915f199060031b1c1916176001555b6104cb6107b2565b60243560025561024357005b0151905083806104ae565b601f1982169360015f52805f20915f5b86811061052b5750836001959610610513575b505050811b016001556104c3565b01515f1960f88460031b161c19169055838080610505565b919260206001819286850151815501940192016104f2565b818111156104945760015f52601f820160051c5f5160206107de5f395f51905f5260208410610596575b81601f9101920160051c03905f5b828110610589575050610494565b5f8282015560010161057b565b5f915061056d565b5f5160206107fe5f395f51905f52805460ff60401b1916600160401b17905561043d565b9050158361042a565b303b159150610422565b829150610418565b3461013c575f36600319011261013c575f5160206107fe5f395f51905f52546001600160401b0360ff8260401c1615911680159081610694575b600114908161068a575b159081610681575b506103945780610637610785565b61065d575b6106446107b2565b61064c6107b2565b600160ff195f5416175f5561024357005b5f5160206107fe5f395f51905f52805460ff60401b1916600160401b17905561063c565b90501582610629565b303b159150610621565b829150610617565b3461013c575f36600319011261013c57602060ff5f54166040519015158152f35b3461013c575f36600319011261013c576020906002548152f35b90601f801991011681019081106001600160401b0382111761035c57604052565b81601f8201121561013c578035906001600160401b03821161035c576040519261072c601f8401601f1916602001856106d7565b8284526020838301011161013c57815f926020809301838601378301015290565b90600182811c9216801561077b575b602083101461076757565b634e487b7160e01b5f52602260045260245ffd5b91607f169161075c565b60016001600160401b03195f5160206107fe5f395f51905f525416175f5160206107fe5f395f51905f5255565b60ff5f5160206107fe5f395f51905f525460401c16156107ce57565b631afcd79f60e31b5f5260045ffdfeb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6f0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00a2646970667358221220e096acf8125e9c105b314d485e61ff2c2939d0f716b89e9e87bd89fb0966d7c864736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SampleFather:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SampleFather]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SampleFather, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SampleFather]]:
        return cls._deploy(request_type, [], return_tx, SampleFather, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def father(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#87)

        Returns:
            father: uint256
        """
        ...

    @overload
    def father(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#87)

        Returns:
            father: uint256
        """
        ...

    @overload
    def father(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#87)

        Returns:
            father: uint256
        """
        ...

    @overload
    def father(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#87)

        Returns:
            father: uint256
        """
        ...

    def father(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#87)

        Returns:
            father: uint256
        """
        return self._execute(self.chain, request_type, "1c8aca3b", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize__(self, _gramps: str, _father: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#89)

        Args:
            _gramps: string
            _father: uint256
        """
        ...

    @overload
    def initialize__(self, _gramps: str, _father: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#89)

        Args:
            _gramps: string
            _father: uint256
        """
        ...

    @overload
    def initialize__(self, _gramps: str, _father: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#89)

        Args:
            _gramps: string
            _father: uint256
        """
        ...

    @overload
    def initialize__(self, _gramps: str, _father: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#89)

        Args:
            _gramps: string
            _father: uint256
        """
        ...

    def initialize__(self, _gramps: str, _father: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#89)

        Args:
            _gramps: string
            _father: uint256
        """
        return self._execute(self.chain, request_type, "8beaf7d7", [_gramps, _father], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

SampleFather.father.selector = bytes4(b'\x1c\x8a\xca;')
SampleFather.initialize__.selector = bytes4(b'\x8b\xea\xf7\xd7')
class SampleChild(SampleFather, SampleMother, Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#108)
    """
    _abi = {b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'#{^\x96': {'inputs': [], 'name': 'child', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1c\x8a\xca;': {'inputs': [], 'name': 'father', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfa9\x85\x1f': {'inputs': [], 'name': 'gramps', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'o.\xdb\xd2': {'inputs': [{'internalType': 'uint256', 'name': '_mother', 'type': 'uint256'}, {'internalType': 'string', 'name': '_gramps', 'type': 'string'}, {'internalType': 'uint256', 'name': '_father', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_child', 'type': 'uint256'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x81)\xfc\x1c': {'inputs': [], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8b\xea\xf7\xd7': {'inputs': [{'internalType': 'string', 'name': '_gramps', 'type': 'string'}, {'internalType': 'uint256', 'name': '_father', 'type': 'uint256'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf6-\x18\x88': {'inputs': [{'internalType': 'string', 'name': 'value', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfeK\x84\xdf': {'inputs': [{'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Jl\x9d\xb6': {'inputs': [], 'name': 'isHuman', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xed}\xfe\xe3': {'inputs': [], 'name': 'mother', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleChild","label":"isHuman","offset":0,"slot":0,"type":"t_bool"},{"astId":44,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleChild","label":"mother","offset":0,"slot":1,"type":"t_uint256"},{"astId":91,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleChild","label":"gramps","offset":0,"slot":2,"type":"t_string_storage"},{"astId":138,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleChild","label":"father","offset":0,"slot":3,"type":"t_uint256"},{"astId":193,"contract":"lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol:SampleChild","label":"child","offset":0,"slot":4,"type":"t_uint256"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234601557610bed908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c9081631c8aca3b14610a5757508063237b5e9614610a3a5780634a6c9db614610a195780636f2edbd2146107bb5780638129fc1c146106fc5780638beaf7d7146104dd578063ed7dfee3146104c0578063f62d1888146102a3578063fa39851f146101c55763fe4b84df1461008a575f80fd5b346101c15760203660031901126101c1575f516020610b985f395f51905f52546001600160401b0360ff8260401c16159116801590816101b9575b60011490816101af575b1590816101a6575b5061019757806100e5610b1f565b610173575b6100f2610b4c565b6100fa610b4c565b610102610b4c565b600160ff195f5416175f55610115610b4c565b60043560015561012157005b60ff60401b195f516020610b985f395f51905f5254165f516020610b985f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b5f516020610b985f395f51905f52805460ff60401b1916600160401b1790556100ea565b63f92ee8a960e01b5f5260045ffd5b9050155f6100d7565b303b1591506100cf565b8291506100c5565b5f80fd5b346101c1575f3660031901126101c157604051600254905f6101e683610ae7565b808352602083019360018116908115610288575060011461023d575b5090610212816040930382610a71565b8151928391602083525180918160208501528484015e5f828201840152601f01601f19168101030190f35b60025f9081525f516020610b785f395f51905f52939250905b80821061026e57509091508101602001610212610202565b919260018160209254838588010152019101909291610256565b60ff1916855250151560051b82016020019050610212610202565b346101c15760203660031901126101c1576004356001600160401b0381116101c1576102d3903690600401610a92565b5f516020610b985f395f51905f52546001600160401b0360ff8260401c16159116801590816104b8575b60011490816104ae575b1590816104a5575b50610197578061031d610b1f565b610481575b61032a610b4c565b610332610b4c565b61033a610b4c565b600160ff195f5416175f5561034d610b4c565b81516001600160401b03811161046d57610368600254610ae7565b601f8111610412575b50602092601f82116001146103b157928192935f926103a6575b50508160011b915f199060031b1c1916176002555b61012157005b01519050838061038b565b601f1982169360025f52805f20915f5b8681106103fa57508360019596106103e2575b505050811b016002556103a0565b01515f1960f88460031b161c191690558380806103d4565b919260206001819286850151815501940192016103c1565b818111156103715760025f52601f820160051c5f516020610b785f395f51905f5260208410610465575b81601f9101920160051c03905f5b828110610458575050610371565b5f8282015560010161044a565b5f915061043c565b634e487b7160e01b5f52604160045260245ffd5b5f516020610b985f395f51905f52805460ff60401b1916600160401b179055610322565b9050158361030f565b303b159150610307565b8291506102fd565b346101c1575f3660031901126101c1576020600154604051908152f35b346101c15760403660031901126101c1576004356001600160401b0381116101c15761050d903690600401610a92565b5f516020610b985f395f51905f52546001600160401b0360ff8260401c16159116801590816106f4575b60011490816106ea575b1590816106e1575b506101975780610557610b1f565b6106bd575b610564610b4c565b61056c610b4c565b610574610b4c565b61057c610b4c565b600160ff195f5416175f5561058f610b4c565b81516001600160401b03811161046d576105aa600254610ae7565b601f8111610662575b50602092601f821160011461060157928192935f926105f6575b50508160011b915f199060031b1c1916176002555b6105ea610b4c565b60243560035561012157005b0151905083806105cd565b601f1982169360025f52805f20915f5b86811061064a5750836001959610610632575b505050811b016002556105e2565b01515f1960f88460031b161c19169055838080610624565b91926020600181928685015181550194019201610611565b818111156105b35760025f52601f820160051c5f516020610b785f395f51905f52602084106106b5575b81601f9101920160051c03905f5b8281106106a85750506105b3565b5f8282015560010161069a565b5f915061068c565b5f516020610b985f395f51905f52805460ff60401b1916600160401b17905561055c565b90501583610549565b303b159150610541565b829150610537565b346101c1575f3660031901126101c1575f516020610b985f395f51905f52546001600160401b0360ff8260401c16159116801590816107b3575b60011490816107a9575b1590816107a0575b506101975780610756610b1f565b61077c575b610763610b4c565b61076b610b4c565b600160ff195f5416175f5561012157005b5f516020610b985f395f51905f52805460ff60401b1916600160401b17905561075b565b90501582610748565b303b159150610740565b829150610736565b346101c15760803660031901126101c1576024356001600160401b0381116101c1576107eb903690600401610a92565b5f516020610b985f395f51905f52546001600160401b0360ff8260401c1615911680159081610a11575b6001149081610a07575b1590816109fe575b506101975780610835610b1f565b6109da575b610842610b4c565b61084a610b4c565b610852610b4c565b61085a610b4c565b600160ff195f541617805f5561086e610b4c565b60043560015561087c610b4c565b610884610b4c565b61088c610b4c565b610894610b4c565b5f5561089e610b4c565b81516001600160401b03811161046d576108b9600254610ae7565b601f811161097f575b50602092601f821160011461091e57928192935f92610913575b50508160011b915f199060031b1c1916176002555b6108f9610b4c565b604435600355610907610b4c565b60643560045561012157005b0151905083806108dc565b601f1982169360025f52805f20915f5b868110610967575083600195961061094f575b505050811b016002556108f1565b01515f1960f88460031b161c19169055838080610941565b9192602060018192868501518155019401920161092e565b818111156108c25760025f52601f820160051c5f516020610b785f395f51905f52602084106109d2575b81601f9101920160051c03905f5b8281106109c55750506108c2565b5f828201556001016109b7565b5f91506109a9565b5f516020610b985f395f51905f52805460ff60401b1916600160401b17905561083a565b90501583610827565b303b15915061081f565b829150610815565b346101c1575f3660031901126101c157602060ff5f54166040519015158152f35b346101c1575f3660031901126101c1576020600454604051908152f35b346101c1575f3660031901126101c1576020906003548152f35b90601f801991011681019081106001600160401b0382111761046d57604052565b81601f820112156101c1578035906001600160401b03821161046d5760405192610ac6601f8401601f191660200185610a71565b828452602083830101116101c157815f926020809301838601378301015290565b90600182811c92168015610b15575b6020831014610b0157565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610af6565b60016001600160401b03195f516020610b985f395f51905f525416175f516020610b985f395f51905f5255565b60ff5f516020610b985f395f51905f525460401c1615610b6857565b631afcd79f60e31b5f5260045ffdfe405787fa12a823e0f2b7631cc41b3ba8828b3321ca811111fa75cd3aa3bb5acef0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00a26469706673582212202f91a968ad6e9b9f5404c85e0ea1225d41ab7d4330126c25bd04774db7143e9364736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> SampleChild:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[SampleChild]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, SampleChild, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[SampleChild]]:
        return cls._deploy(request_type, [], return_tx, SampleChild, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def child(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#109)

        Returns:
            child: uint256
        """
        ...

    @overload
    def child(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#109)

        Returns:
            child: uint256
        """
        ...

    @overload
    def child(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#109)

        Returns:
            child: uint256
        """
        ...

    @overload
    def child(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#109)

        Returns:
            child: uint256
        """
        ...

    def child(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#109)

        Returns:
            child: uint256
        """
        return self._execute(self.chain, request_type, "237b5e96", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize___(self, _mother: uint256, _gramps: str, _father: uint256, _child: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#111)

        Args:
            _mother: uint256
            _gramps: string
            _father: uint256
            _child: uint256
        """
        ...

    @overload
    def initialize___(self, _mother: uint256, _gramps: str, _father: uint256, _child: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#111)

        Args:
            _mother: uint256
            _gramps: string
            _father: uint256
            _child: uint256
        """
        ...

    @overload
    def initialize___(self, _mother: uint256, _gramps: str, _father: uint256, _child: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#111)

        Args:
            _mother: uint256
            _gramps: string
            _father: uint256
            _child: uint256
        """
        ...

    @overload
    def initialize___(self, _mother: uint256, _gramps: str, _father: uint256, _child: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#111)

        Args:
            _mother: uint256
            _gramps: string
            _father: uint256
            _child: uint256
        """
        ...

    def initialize___(self, _mother: uint256, _gramps: str, _father: uint256, _child: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/MultipleInheritanceInitializableMocks.sol#111)

        Args:
            _mother: uint256
            _gramps: string
            _father: uint256
            _child: uint256
        """
        return self._execute(self.chain, request_type, "6f2edbd2", [_mother, _gramps, _father, _child], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

SampleChild.child.selector = bytes4(b'#{^\x96')
SampleChild.initialize___.selector = bytes4(b'o.\xdb\xd2')
