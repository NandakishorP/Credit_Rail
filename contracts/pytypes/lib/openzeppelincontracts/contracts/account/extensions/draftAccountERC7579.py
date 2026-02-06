
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.account.Account import Account_
from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC1271 import IERC1271
from pytypes.lib.openzeppelincontracts.contracts.interfaces.draftIERC7579 import IERC7579AccountConfig
from pytypes.lib.openzeppelincontracts.contracts.interfaces.draftIERC7579 import IERC7579Execution
from pytypes.lib.openzeppelincontracts.contracts.interfaces.draftIERC7579 import IERC7579ModuleConfig



class AccountERC7579(IERC7579ModuleConfig, IERC7579AccountConfig, IERC7579Execution, IERC1271, Account_):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#58)
    """
    _abi = {b'|\xf8c+': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'AccountUnauthorized', 'type': 'error'}, b'\x95\xd4\x8a[': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579AlreadyInstalledModule', 'type': 'error'}, b'\xfa)\x87\x11': {'inputs': [], 'name': 'ERC7579CannotDecodeFallbackData', 'type': 'error'}, b'\xeb\x0b\xcc]': {'inputs': [], 'name': 'ERC7579DecodingError', 'type': 'error'}, b'\x8f\x89Go': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579MismatchedModuleTypeId', 'type': 'error'}, b'\xafZr\x03': {'inputs': [{'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'ERC7579MissingFallbackHandler', 'type': 'error'}, b'\x13C\xd6\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ERC7579UninstalledModule', 'type': 'error'}, b'\xb1\xbej\x96': {'inputs': [{'internalType': 'CallType', 'name': 'callType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedCallType', 'type': 'error'}, b'#\xa2@\x85': {'inputs': [{'internalType': 'ExecType', 'name': 'execType', 'type': 'bytes1'}], 'name': 'ERC7579UnsupportedExecType', 'type': 'error'}, b'`\xfa+#': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'ERC7579UnsupportedModuleType', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b';\xa9v6': {'inputs': [], 'name': 'OutOfRangeAccess', 'type': 'error'}, b'.\xea/Q\xf89\x10H\x1fK[\xa2\x8bp\x03\xa6\xe0E\xd4\xb5\x9fg\xdf\xff\x8dL\x90\x11\x94\x05\x00\x89': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'batchExecutionIndex', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'returndata', 'type': 'bytes'}], 'name': 'ERC7579TryExecuteFail', 'type': 'event'}, b'\xd2\x1d\x0b(\x9f\x12lKG>\xa6A\x96>vh3\xc2\xf18f\xe4\xffH\n\xbdx|\x10\x0e\xf1#': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ModuleInstalled', 'type': 'event'}, b"4\x13GQj\x9d\xe3t\x85\x9d\xfd\xa7\x10\xfaH(\xb2\xd4\x8c\xb5}O\xbeL\x11Ia+\x8e\x02'n": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'module', 'type': 'address'}], 'name': 'ModuleUninstalled', 'type': 'event'}, 'fallback': {'stateMutability': 'payable', 'type': 'fallback'}, b'\x9c\xfd|\xff': {'inputs': [], 'name': 'accountId', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0\xd6\x91\xfe': {'inputs': [], 'name': 'entryPoint', 'outputs': [{'internalType': 'contract IEntryPoint', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\xae\\S': {'inputs': [{'internalType': 'bytes32', 'name': 'mode', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'executionCalldata', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xd6\x91\xc9d': {'inputs': [{'internalType': 'bytes32', 'name': 'mode', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'executionCalldata', 'type': 'bytes'}], 'name': 'executeFromExecutor', 'outputs': [{'internalType': 'bytes[]', 'name': 'returnData', 'type': 'bytes[]'}], 'stateMutability': 'payable', 'type': 'function'}, b'>\x1b\x08\x12': {'inputs': [{'internalType': 'uint192', 'name': 'key', 'type': 'uint192'}], 'name': 'getNonce', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\x87\xd2\x88': {'inputs': [], 'name': 'getNonce', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\x17\xe2\x9f': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'initData', 'type': 'bytes'}], 'name': 'installModule', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x11-:}': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'additionalContext', 'type': 'bytes'}], 'name': 'isModuleInstalled', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x16&\xba~': {'inputs': [{'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'isValidSignature', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0<y\x14': {'inputs': [{'internalType': 'bytes32', 'name': 'encodedMode', 'type': 'bytes32'}], 'name': 'supportsExecutionMode', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf2\xdci\x1d': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}], 'name': 'supportsModule', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa7\x17c\xa8': {'inputs': [{'internalType': 'uint256', 'name': 'moduleTypeId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'module', 'type': 'address'}, {'internalType': 'bytes', 'name': 'deInitData', 'type': 'bytes'}], 'name': 'uninstallModule', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x19\x82/|': {'inputs': [{'components': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nonce', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'initCode', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'callData', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'accountGasLimits', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'preVerificationGas', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'gasFees', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'paymasterAndData', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'internalType': 'struct PackedUserOperation', 'name': 'userOp', 'type': 'tuple'}, {'internalType': 'bytes32', 'name': 'userOpHash', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'missingAccountFunds', 'type': 'uint256'}], 'name': 'validateUserOp', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, 'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[{"astId":40091,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_validators","offset":0,"slot":0,"type":"t_struct(AddressSet)61401_storage"},{"astId":40094,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_executors","offset":0,"slot":2,"type":"t_struct(AddressSet)61401_storage"},{"astId":40098,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_fallbacks","offset":0,"slot":4,"type":"t_mapping(t_bytes4,t_address)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_mapping(t_bytes32,t_uint256)":{"encoding":"mapping","label":"mapping(bytes32 => uint256)","numberOfBytes":32,"key":"t_bytes32","value":"t_uint256"},"t_mapping(t_bytes4,t_address)":{"encoding":"mapping","label":"mapping(bytes4 => address)","numberOfBytes":32,"key":"t_bytes4","value":"t_address"},"t_struct(AddressSet)61401_storage":{"encoding":"inplace","label":"struct EnumerableSet.AddressSet","numberOfBytes":64,"members":[{"astId":61400,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_inner","offset":0,"slot":0,"type":"t_struct(Set)60915_storage"}]},"t_struct(Set)60915_storage":{"encoding":"inplace","label":"struct EnumerableSet.Set","numberOfBytes":64,"members":[{"astId":60910,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_values","offset":0,"slot":0,"type":"t_array(t_bytes32)dyn_storage"},{"astId":60914,"contract":"lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol:AccountERC7579","label":"_positions","offset":0,"slot":1,"type":"t_mapping(t_bytes32,t_uint256)"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> AccountERC7579:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[AccountERC7579]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, AccountERC7579, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[AccountERC7579]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class ERC7579MissingFallbackHandler(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#69)

        Attributes:
            selector_ (bytes4): bytes4
        """
        _abi = {'inputs': [{'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'ERC7579MissingFallbackHandler', 'type': 'error'}
        original_name = 'ERC7579MissingFallbackHandler'
        selector = bytes4(b'\xafZr\x03')

        selector_: bytes4 = dataclasses.field(metadata={"original_name": "selector"})


    @dataclasses.dataclass
    class ERC7579CannotDecodeFallbackData(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#72)
        """
        _abi = {'inputs': [], 'name': 'ERC7579CannotDecodeFallbackData', 'type': 'error'}
        original_name = 'ERC7579CannotDecodeFallbackData'
        selector = bytes4(b'\xfa)\x87\x11')



    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#86)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#86)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#86)

        Returns:
            string
        """
        ...

    @overload
    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#86)

        Returns:
            string
        """
        ...

    def accountId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#86)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "9cfd7cff", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def supportsExecutionMode(self, encodedMode: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#103)

        Args:
            encodedMode: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def supportsExecutionMode(self, encodedMode: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#103)

        Args:
            encodedMode: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def supportsExecutionMode(self, encodedMode: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#103)

        Args:
            encodedMode: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def supportsExecutionMode(self, encodedMode: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#103)

        Args:
            encodedMode: bytes32
        Returns:
            bool
        """
        ...

    def supportsExecutionMode(self, encodedMode: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#103)

        Args:
            encodedMode: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "d03c7914", [encodedMode], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#122)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#122)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#122)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    @overload
    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#122)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        ...

    def supportsModule(self, moduleTypeId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#122)

        Args:
            moduleTypeId: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "f2dc691d", [moduleTypeId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def installModule(self, moduleTypeId: uint256, module: Union[Account, Address], initData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#130)

        Args:
            moduleTypeId: uint256
            module: address
            initData: bytes
        """
        ...

    @overload
    def installModule(self, moduleTypeId: uint256, module: Union[Account, Address], initData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#130)

        Args:
            moduleTypeId: uint256
            module: address
            initData: bytes
        """
        ...

    @overload
    def installModule(self, moduleTypeId: uint256, module: Union[Account, Address], initData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#130)

        Args:
            moduleTypeId: uint256
            module: address
            initData: bytes
        """
        ...

    @overload
    def installModule(self, moduleTypeId: uint256, module: Union[Account, Address], initData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#130)

        Args:
            moduleTypeId: uint256
            module: address
            initData: bytes
        """
        ...

    def installModule(self, moduleTypeId: uint256, module: Union[Account, Address], initData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#130)

        Args:
            moduleTypeId: uint256
            module: address
            initData: bytes
        """
        return self._execute(self.chain, request_type, "9517e29f", [moduleTypeId, module, initData], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def uninstallModule(self, moduleTypeId: uint256, module: Union[Account, Address], deInitData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#139)

        Args:
            moduleTypeId: uint256
            module: address
            deInitData: bytes
        """
        ...

    @overload
    def uninstallModule(self, moduleTypeId: uint256, module: Union[Account, Address], deInitData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#139)

        Args:
            moduleTypeId: uint256
            module: address
            deInitData: bytes
        """
        ...

    @overload
    def uninstallModule(self, moduleTypeId: uint256, module: Union[Account, Address], deInitData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#139)

        Args:
            moduleTypeId: uint256
            module: address
            deInitData: bytes
        """
        ...

    @overload
    def uninstallModule(self, moduleTypeId: uint256, module: Union[Account, Address], deInitData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#139)

        Args:
            moduleTypeId: uint256
            module: address
            deInitData: bytes
        """
        ...

    def uninstallModule(self, moduleTypeId: uint256, module: Union[Account, Address], deInitData: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#139)

        Args:
            moduleTypeId: uint256
            module: address
            deInitData: bytes
        """
        return self._execute(self.chain, request_type, "a71763a8", [moduleTypeId, module, deInitData], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], additionalContext: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#148)

        Args:
            moduleTypeId: uint256
            module: address
            additionalContext: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], additionalContext: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#148)

        Args:
            moduleTypeId: uint256
            module: address
            additionalContext: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], additionalContext: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#148)

        Args:
            moduleTypeId: uint256
            module: address
            additionalContext: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], additionalContext: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#148)

        Args:
            moduleTypeId: uint256
            module: address
            additionalContext: bytes
        Returns:
            bool
        """
        ...

    def isModuleInstalled(self, moduleTypeId: uint256, module: Union[Account, Address], additionalContext: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#148)

        Args:
            moduleTypeId: uint256
            module: address
            additionalContext: bytes
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "112d3a7d", [moduleTypeId, module, additionalContext], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def execute(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#162)

        Args:
            mode: bytes32
            executionCalldata: bytes
        """
        ...

    @overload
    def execute(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#162)

        Args:
            mode: bytes32
            executionCalldata: bytes
        """
        ...

    @overload
    def execute(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#162)

        Args:
            mode: bytes32
            executionCalldata: bytes
        """
        ...

    @overload
    def execute(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#162)

        Args:
            mode: bytes32
            executionCalldata: bytes
        """
        ...

    def execute(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#162)

        Args:
            mode: bytes32
            executionCalldata: bytes
        """
        return self._execute(self.chain, request_type, "e9ae5c53", [mode, executionCalldata], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def executeFromExecutor(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#167)

        Args:
            mode: bytes32
            executionCalldata: bytes
        Returns:
            returnData: bytes[]
        """
        ...

    @overload
    def executeFromExecutor(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#167)

        Args:
            mode: bytes32
            executionCalldata: bytes
        Returns:
            returnData: bytes[]
        """
        ...

    @overload
    def executeFromExecutor(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#167)

        Args:
            mode: bytes32
            executionCalldata: bytes
        Returns:
            returnData: bytes[]
        """
        ...

    @overload
    def executeFromExecutor(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytearray]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#167)

        Args:
            mode: bytes32
            executionCalldata: bytes
        Returns:
            returnData: bytes[]
        """
        ...

    def executeFromExecutor(self, mode: bytes32, executionCalldata: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytearray], TransactionAbc[List[bytearray]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#167)

        Args:
            mode: bytes32
            executionCalldata: bytes
        Returns:
            returnData: bytes[]
        """
        return self._execute(self.chain, request_type, "d691c964", [mode, executionCalldata], True if request_type == "tx" else False, List[bytearray], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#187)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#187)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#187)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#187)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    def isValidSignature(self, hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/account/extensions/draft-AccountERC7579.sol#187)

        Args:
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "1626ba7e", [hash, signature], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

AccountERC7579.accountId.selector = bytes4(b'\x9c\xfd|\xff')
AccountERC7579.supportsExecutionMode.selector = bytes4(b'\xd0<y\x14')
AccountERC7579.supportsModule.selector = bytes4(b'\xf2\xdci\x1d')
AccountERC7579.installModule.selector = bytes4(b'\x95\x17\xe2\x9f')
AccountERC7579.uninstallModule.selector = bytes4(b'\xa7\x17c\xa8')
AccountERC7579.isModuleInstalled.selector = bytes4(b'\x11-:}')
AccountERC7579.execute.selector = bytes4(b'\xe9\xae\\S')
AccountERC7579.executeFromExecutor.selector = bytes4(b'\xd6\x91\xc9d')
AccountERC7579.isValidSignature.selector = bytes4(b'\x16&\xba~')
