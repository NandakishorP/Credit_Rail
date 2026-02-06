
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.lib.forgestd.src.Base import ScriptBase



class CompilationScriptBase(ScriptBase):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol#10)
    """
    _abi = {}
    _storage_layout = {"storage":[{"astId":61,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)5075_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)5050_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)5050_storage))"},"t_mapping(t_bytes32,t_struct(FindData)5050_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)5050_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)5050_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)5050_storage)"},"t_struct(FindData)5050_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":5043,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":5045,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":5047,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":5049,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)5075_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":5059,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)5050_storage)))"},{"astId":5062,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":5064,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":5066,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":5068,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":5070,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":5072,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":5074,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/compilation/CompilationScriptBase.sol:CompilationScriptBase","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "608080604052346013576039908160188239f35b5f80fdfe5f80fdfea2646970667358221220f648272681add2479eaf6525eebe02a9767c9faed61f1f7a86a32598846ae0db64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CompilationScriptBase:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CompilationScriptBase]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, CompilationScriptBase, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[CompilationScriptBase]]:
        return cls._deploy(request_type, [], return_tx, CompilationScriptBase, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

