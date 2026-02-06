
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.account.extensions.draftAccountERC7579 import AccountERC7579



class AccountERC7579Hooked(AccountERC7579):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#22)
    """
    _abi = {b'|\xf8c+': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'AccountUnauthorized', 'type': 'error'}, b'\x95\xd4\x8a[': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579AlreadyInstalledModule', 'type': 'error'}, b'\xfa)\x87\x11': {'inputs': [], 'name': 'ERC7579CannotDecodeFallbackData', 'type': 'error'}, b'\xeb\x0b\xcc]': {'inputs': [], 'name': 'ERC7579DecodingError', 'type': 'error'}, b'\x18\x00\xbd\x1a': {'inputs': [{'internalType': 'address', 'name': 'hook', 'type': 'address'}], 'name': 'ERC7579HookModuleAlreadyPresent', 'type': 'error'}, b'\x8f\x89Go': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579MismatchedModuleTypeId', 'type': 'error'}, b'\xafZr\x03': {'inputs': [{'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'ERC7579MissingFallbackHandler', 'type': 'error'}, b'\x13C\xd6\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579UninstalledModule', 'type': 'error'}, b'\xb1\xbej\x96': {'inputs': [{'internalType': 'CallType', 'name': 'callType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedCallType', 'type': 'error'}, b'#\xa2@\x85': {'inputs': [{'internalType': 'ExecType', 'name': 'execType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedExecType', 'type': 'error'}, b'`\xfa+#': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'ERC7579UnsupportedModuleType', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b';\xa9v6': {'inputs': [], 'name': 'OutOfRangeAccess', 'type': 'error'}, b'.\xea/Q\xf89\x10H\x1fK[\xa2\x8bp\x03\xa6\xe0E\xd4\xb5\x9fg\xdf\xff\x8dL\x90\x11\x94\x05\x00\x89': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'batchExecutionIndex', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'returndata', 'type': 'bytes'}], 'name': 'ERC7579TryExecuteFail', 'type': 'event'}, b'\xd2\x1d\x0b(\x9f\x12lKG>\xa6A\x96>vh3\xc2\xf18f\xe4\xffH\n\xbdx|\x10\x0e\xf1#': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ModuleInstalled', 'type': 'event'}, b"4\x13GQj\x9d\xe3t\x85\x9d\xfd\xa7\x10\xfaH(\xb2\xd4\x8c\xb5}O\xbeL\x11Ia+\x8e\x02'n": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ModuleUninstalled', 'type': 'event'}, 'fallback': {'stateMutability': 'payable', 'type': 'fallback'}, b'\x9c\xfd|\xff': {'inputs': [], 'name': 'accountId', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0\xd6\x91\xfe': {'inputs': [], 'name': 'entryPoint', 'outputs': [{'internalType': 'contract IEntryPoint', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\xae\\S': {'inputs': [{'internalType': 'bytes32', 'name': 'mode', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'executionCalldata', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xd6\x91\xc9d': {'inputs': [{'internalType': 'bytes32', 'name': 'mode', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'executionCalldata', 'type': 'bytes'}], 'name': 'executeFromExecutor', 'outputs': [{'internalType': 'bytes[]', 'name': 'returnData', 'type': 'bytes[]'}], 'stateMutability': 'payable', 'type': 'function'}, b'>\x1b\x08\x12': {'inputs': [{'internalType': 'uint192', 'name': 'key', 'type': 'uint192'}], 'name': 'getNonce', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\x87\xd2\x88': {'inputs': [], 'name': 'getNonce', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x7fZ|{': {'inputs': [], 'name': 'hook', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\x17\xe2\x9f': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'initData', 'type': 'bytes'}], 'name': 'installModule', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x11-:}': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'isModuleInstalled', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x16&\xba~': {'inputs': [{'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'isValidSignature', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0<y\x14': {'inputs': [{'internalType': 'bytes32', 'name': 'encodedMode', 'type': 'bytes32'}], 'name': 'supportsExecutionMode', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf2\xdci\x1d': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'supportsModule', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa7\x17c\xa8': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'deInitData', 'type': 'bytes'}], 'name': 'uninstallModule', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x19\x82/|': {'inputs': [{'components': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nonce', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'initCode', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'callData', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'accountGasLimits', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'preVerificationGas', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'gasFees', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'paymasterAndData', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'internalType': 'struct PackedUserOperation', 'name': 'userOp', 'type': 'tuple'}, {'internalType': 'bytes32', 'name': 'userOpHash', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'missingAccountFunds', 'type': 'uint256'}], 'name': 'validateUserOp', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, 'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[{"astId":40091,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_validators","offset":0,"slot":0,"type":"t_struct(AddressSet)61401_storage"},{"astId":40094,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_executors","offset":0,"slot":2,"type":"t_struct(AddressSet)61401_storage"},{"astId":40098,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_fallbacks","offset":0,"slot":4,"type":"t_mapping(t_bytes4,t_address)"},{"astId":40934,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_hook","offset":0,"slot":5,"type":"t_address"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_mapping(t_bytes32,t_uint256)":{"encoding":"mapping","label":"mapping(bytes32 => uint256)","numberOfBytes":32,"key":"t_bytes32","value":"t_uint256"},"t_mapping(t_bytes4,t_address)":{"encoding":"mapping","label":"mapping(bytes4 => address)","numberOfBytes":32,"key":"t_bytes4","value":"t_address"},"t_struct(AddressSet)61401_storage":{"encoding":"inplace","label":"struct EnumerableSet.AddressSet","numberOfBytes":64,"members":[{"astId":61400,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_inner","offset":0,"slot":0,"type":"t_struct(Set)60915_storage"}]},"t_struct(Set)60915_storage":{"encoding":"inplace","label":"struct EnumerableSet.Set","numberOfBytes":64,"members":[{"astId":60910,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_values","offset":0,"slot":0,"type":"t_array(t_bytes32)dyn_storage"},{"astId":60914,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol:AccountERC7579Hooked","label":"_positions","offset":0,"slot":1,"type":"t_mapping(t_bytes32,t_uint256)"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> AccountERC7579Hooked:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[AccountERC7579Hooked]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, AccountERC7579Hooked, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[AccountERC7579Hooked]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class ERC7579HookModuleAlreadyPresent(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#26)

        Attributes:
            hook (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'hook', 'type': 'address'}], 'name': 'ERC7579HookModuleAlreadyPresent', 'type': 'error'}
        original_name = 'ERC7579HookModuleAlreadyPresent'
        selector = bytes4(b'\x18\x00\xbd\x1a')

        hook: Address


    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#43)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#43)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#43)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#43)

        Returns:
            string
        """
        ...

    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#43)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "9cfd7cff", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hook(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#49)

        Returns:
            address
        """
        ...

    @overload
    def hook(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#49)

        Returns:
            address
        """
        ...

    @overload
    def hook(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#49)

        Returns:
            address
        """
        ...

    @overload
    def hook(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#49)

        Returns:
            address
        """
        ...

    def hook(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#49)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "7f5a7c7b", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#54)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#54)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#54)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#54)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#54)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "f2dc691d", [moduleTypeId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#59)

        Args:
            moduleTypeId: uint256
            module: address
            data: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#59)

        Args:
            moduleTypeId: uint256
            module: address
            data: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#59)

        Args:
            moduleTypeId: uint256
            module: address
            data: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#59)

        Args:
            moduleTypeId: uint256
            module: address
            data: bytes
        Returns:
            bool
        """
        ...

    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579Hooked.sol#59)

        Args:
            moduleTypeId: uint256
            module: address
            data: bytes
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "112d3a7d", [moduleTypeId, module, data], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

AccountERC7579Hooked.accountId.selector = bytes4(b'\x9c\xfd|\xff')
AccountERC7579Hooked.hook.selector = bytes4(b'\x7fZ|{')
AccountERC7579Hooked.supportsModule.selector = bytes4(b'\xf2\xdci\x1d')
AccountERC7579Hooked.isModuleInstalled.selector = bytes4(b'\x11-:}')
