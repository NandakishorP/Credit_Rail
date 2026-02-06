
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class Checkpoints(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#16)
    """
    _abi = {b'% `\x1d': {'inputs': [], 'name': 'CheckpointUnorderedInsertion', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220346dbaed9a36ee53dd5b2ce48d98007930f0f4198a2b556007305ce20fa8004f64736f6c63430008210033"

    _library_id = b'\xec\xc66\x97%Z\\2\xf5"\xe29\xdc:\x8c\r\xba'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Checkpoints:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Checkpoints]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Checkpoints, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Checkpoints]]:
        return cls._deploy(request_type, [], return_tx, Checkpoints, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Trace256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#22)

        Attributes:
            _checkpoints (List[Checkpoints.Checkpoint256]): struct Checkpoints.Checkpoint256[]
        """
        original_name = 'Trace256'

        _checkpoints: List[Checkpoints.Checkpoint256]


    @dataclasses.dataclass
    class Checkpoint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#26)

        Attributes:
            _key (uint256): uint256
            _value (uint256): uint256
        """
        original_name = 'Checkpoint256'

        _key: uint256
        _value: uint256


    @dataclasses.dataclass
    class Trace224:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#225)

        Attributes:
            _checkpoints (List[Checkpoints.Checkpoint224]): struct Checkpoints.Checkpoint224[]
        """
        original_name = 'Trace224'

        _checkpoints: List[Checkpoints.Checkpoint224]


    @dataclasses.dataclass
    class Checkpoint224:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#229)

        Attributes:
            _key (uint32): uint32
            _value (uint224): uint224
        """
        original_name = 'Checkpoint224'

        _key: uint32
        _value: uint224


    @dataclasses.dataclass
    class Trace208:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#428)

        Attributes:
            _checkpoints (List[Checkpoints.Checkpoint208]): struct Checkpoints.Checkpoint208[]
        """
        original_name = 'Trace208'

        _checkpoints: List[Checkpoints.Checkpoint208]


    @dataclasses.dataclass
    class Checkpoint208:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#432)

        Attributes:
            _key (uint48): uint48
            _value (uint208): uint208
        """
        original_name = 'Checkpoint208'

        _key: uint48
        _value: uint208


    @dataclasses.dataclass
    class Trace160:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#631)

        Attributes:
            _checkpoints (List[Checkpoints.Checkpoint160]): struct Checkpoints.Checkpoint160[]
        """
        original_name = 'Trace160'

        _checkpoints: List[Checkpoints.Checkpoint160]


    @dataclasses.dataclass
    class Checkpoint160:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#635)

        Attributes:
            _key (uint96): uint96
            _value (uint160): uint160
        """
        original_name = 'Checkpoint160'

        _key: uint96
        _value: uint160


    @dataclasses.dataclass
    class CheckpointUnorderedInsertion(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/Checkpoints.sol#20)
        """
        _abi = {'inputs': [], 'name': 'CheckpointUnorderedInsertion', 'type': 'error'}
        original_name = 'CheckpointUnorderedInsertion'
        selector = bytes4(b'% `\x1d')



