
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class StdCheatsSafe(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#10)
    """
    _abi = {}
    _storage_layout = {"storage":[{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheatsSafe","label":"gasMeteringOff","offset":0,"slot":0,"type":"t_bool"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdCheatsSafe:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdCheatsSafe]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdCheatsSafe, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdCheatsSafe]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    class AddressType(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#200)

        """
        Payable = 0
        NonPayable = 1
        ZeroAddress = 2
        Precompile = 3
        ForgeAddress = 4


    @dataclasses.dataclass
    class RawTx1559:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#22)

        Attributes:
            arguments (List[str]): string[]
            contractAddress (Address): address
            contractName (str): string
            functionSig (str): string
            hash (bytes32): bytes32
            txDetail (StdCheatsSafe.RawTx1559Detail): struct StdCheatsSafe.RawTx1559Detail
            opcode (str): string
        """
        original_name = 'RawTx1559'

        arguments: List[str]
        contractAddress: Address
        contractName: str
        functionSig: str
        hash: bytes32
        txDetail: StdCheatsSafe.RawTx1559Detail
        opcode: str


    @dataclasses.dataclass
    class RawTx1559Detail:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#35)

        Attributes:
            accessList (List[StdCheatsSafe.AccessList]): struct StdCheatsSafe.AccessList[]
            data (bytearray): bytes
            from_ (Address): address
            gas (bytearray): bytes
            nonce (bytearray): bytes
            to (Address): address
            txType (bytearray): bytes
            value (bytearray): bytes
        """
        original_name = 'RawTx1559Detail'

        accessList: List[StdCheatsSafe.AccessList]
        data: bytearray
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        gas: bytearray
        nonce: bytearray
        to: Address
        txType: bytearray
        value: bytearray


    @dataclasses.dataclass
    class Tx1559:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#46)

        Attributes:
            arguments (List[str]): string[]
            contractAddress (Address): address
            contractName (str): string
            functionSig (str): string
            hash (bytes32): bytes32
            txDetail (StdCheatsSafe.Tx1559Detail): struct StdCheatsSafe.Tx1559Detail
            opcode (str): string
        """
        original_name = 'Tx1559'

        arguments: List[str]
        contractAddress: Address
        contractName: str
        functionSig: str
        hash: bytes32
        txDetail: StdCheatsSafe.Tx1559Detail
        opcode: str


    @dataclasses.dataclass
    class Tx1559Detail:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#56)

        Attributes:
            accessList (List[StdCheatsSafe.AccessList]): struct StdCheatsSafe.AccessList[]
            data (bytearray): bytes
            from_ (Address): address
            gas (uint256): uint256
            nonce (uint256): uint256
            to (Address): address
            txType (uint256): uint256
            value (uint256): uint256
        """
        original_name = 'Tx1559Detail'

        accessList: List[StdCheatsSafe.AccessList]
        data: bytearray
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        gas: uint256
        nonce: uint256
        to: Address
        txType: uint256
        value: uint256


    @dataclasses.dataclass
    class TxLegacy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#71)

        Attributes:
            arguments (List[str]): string[]
            contractAddress (Address): address
            contractName (str): string
            functionSig (str): string
            hash (str): string
            opcode (str): string
            transaction (StdCheatsSafe.TxDetailLegacy): struct StdCheatsSafe.TxDetailLegacy
        """
        original_name = 'TxLegacy'

        arguments: List[str]
        contractAddress: Address
        contractName: str
        functionSig: str
        hash: str
        opcode: str
        transaction: StdCheatsSafe.TxDetailLegacy


    @dataclasses.dataclass
    class TxDetailLegacy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#81)

        Attributes:
            accessList (List[StdCheatsSafe.AccessList]): struct StdCheatsSafe.AccessList[]
            chainId (uint256): uint256
            data (bytearray): bytes
            from_ (Address): address
            gas (uint256): uint256
            gasPrice (uint256): uint256
            hash (bytes32): bytes32
            nonce (uint256): uint256
            opcode (bytes1): bytes1
            r (bytes32): bytes32
            s (bytes32): bytes32
            txType (uint256): uint256
            to (Address): address
            v (uint8): uint8
            value (uint256): uint256
        """
        original_name = 'TxDetailLegacy'

        accessList: List[StdCheatsSafe.AccessList]
        chainId: uint256
        data: bytearray
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        gas: uint256
        gasPrice: uint256
        hash: bytes32
        nonce: uint256
        opcode: bytes1
        r: bytes32
        s: bytes32
        txType: uint256
        to: Address
        v: uint8
        value: uint256


    @dataclasses.dataclass
    class AccessList:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#99)

        Attributes:
            accessAddress (Address): address
            storageKeys (List[bytes32]): bytes32[]
        """
        original_name = 'AccessList'

        accessAddress: Address
        storageKeys: List[bytes32]


    @dataclasses.dataclass
    class RawReceipt:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#108)

        Attributes:
            blockHash (bytes32): bytes32
            blockNumber (bytearray): bytes
            contractAddress (Address): address
            cumulativeGasUsed (bytearray): bytes
            effectiveGasPrice (bytearray): bytes
            from_ (Address): address
            gasUsed (bytearray): bytes
            logs (List[StdCheatsSafe.RawReceiptLog]): struct StdCheatsSafe.RawReceiptLog[]
            logsBloom (bytearray): bytes
            status (bytearray): bytes
            to (Address): address
            transactionHash (bytes32): bytes32
            transactionIndex (bytearray): bytes
        """
        original_name = 'RawReceipt'

        blockHash: bytes32
        blockNumber: bytearray
        contractAddress: Address
        cumulativeGasUsed: bytearray
        effectiveGasPrice: bytearray
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        gasUsed: bytearray
        logs: List[StdCheatsSafe.RawReceiptLog]
        logsBloom: bytearray
        status: bytearray
        to: Address
        transactionHash: bytes32
        transactionIndex: bytearray


    @dataclasses.dataclass
    class Receipt:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#124)

        Attributes:
            blockHash (bytes32): bytes32
            blockNumber (uint256): uint256
            contractAddress (Address): address
            cumulativeGasUsed (uint256): uint256
            effectiveGasPrice (uint256): uint256
            from_ (Address): address
            gasUsed (uint256): uint256
            logs (List[StdCheatsSafe.ReceiptLog]): struct StdCheatsSafe.ReceiptLog[]
            logsBloom (bytearray): bytes
            status (uint256): uint256
            to (Address): address
            transactionHash (bytes32): bytes32
            transactionIndex (uint256): uint256
        """
        original_name = 'Receipt'

        blockHash: bytes32
        blockNumber: uint256
        contractAddress: Address
        cumulativeGasUsed: uint256
        effectiveGasPrice: uint256
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        gasUsed: uint256
        logs: List[StdCheatsSafe.ReceiptLog]
        logsBloom: bytearray
        status: uint256
        to: Address
        transactionHash: bytes32
        transactionIndex: uint256


    @dataclasses.dataclass
    class EIP1559ScriptArtifact:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#143)

        Attributes:
            libraries (List[str]): string[]
            path (str): string
            pending (List[str]): string[]
            receipts (List[StdCheatsSafe.Receipt]): struct StdCheatsSafe.Receipt[]
            timestamp (uint256): uint256
            transactions (List[StdCheatsSafe.Tx1559]): struct StdCheatsSafe.Tx1559[]
            txReturns (List[StdCheatsSafe.TxReturn]): struct StdCheatsSafe.TxReturn[]
        """
        original_name = 'EIP1559ScriptArtifact'

        libraries: List[str]
        path: str
        pending: List[str]
        receipts: List[StdCheatsSafe.Receipt]
        timestamp: uint256
        transactions: List[StdCheatsSafe.Tx1559]
        txReturns: List[StdCheatsSafe.TxReturn]


    @dataclasses.dataclass
    class RawEIP1559ScriptArtifact:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#153)

        Attributes:
            libraries (List[str]): string[]
            path (str): string
            pending (List[str]): string[]
            receipts (List[StdCheatsSafe.RawReceipt]): struct StdCheatsSafe.RawReceipt[]
            txReturns (List[StdCheatsSafe.TxReturn]): struct StdCheatsSafe.TxReturn[]
            timestamp (uint256): uint256
            transactions (List[StdCheatsSafe.RawTx1559]): struct StdCheatsSafe.RawTx1559[]
        """
        original_name = 'RawEIP1559ScriptArtifact'

        libraries: List[str]
        path: str
        pending: List[str]
        receipts: List[StdCheatsSafe.RawReceipt]
        txReturns: List[StdCheatsSafe.TxReturn]
        timestamp: uint256
        transactions: List[StdCheatsSafe.RawTx1559]


    @dataclasses.dataclass
    class RawReceiptLog:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#163)

        Attributes:
            logAddress (Address): address
            blockHash (bytes32): bytes32
            blockNumber (bytearray): bytes
            data (bytearray): bytes
            logIndex (bytearray): bytes
            removed (bool): bool
            topics (List[bytes32]): bytes32[]
            transactionHash (bytes32): bytes32
            transactionIndex (bytearray): bytes
            transactionLogIndex (bytearray): bytes
        """
        original_name = 'RawReceiptLog'

        logAddress: Address
        blockHash: bytes32
        blockNumber: bytearray
        data: bytearray
        logIndex: bytearray
        removed: bool
        topics: List[bytes32]
        transactionHash: bytes32
        transactionIndex: bytearray
        transactionLogIndex: bytearray


    @dataclasses.dataclass
    class ReceiptLog:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#177)

        Attributes:
            logAddress (Address): address
            blockHash (bytes32): bytes32
            blockNumber (uint256): uint256
            data (bytearray): bytes
            logIndex (uint256): uint256
            topics (List[bytes32]): bytes32[]
            transactionIndex (uint256): uint256
            transactionLogIndex (uint256): uint256
            removed (bool): bool
        """
        original_name = 'ReceiptLog'

        logAddress: Address
        blockHash: bytes32
        blockNumber: uint256
        data: bytearray
        logIndex: uint256
        topics: List[bytes32]
        transactionIndex: uint256
        transactionLogIndex: uint256
        removed: bool


    @dataclasses.dataclass
    class TxReturn:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#190)

        Attributes:
            internalType (str): string
            value (str): string
        """
        original_name = 'TxReturn'

        internalType: str
        value: str


    @dataclasses.dataclass
    class Account_:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#195)

        Attributes:
            addr (Address): address
            key (uint256): uint256
        """
        original_name = 'Account'

        addr: Address
        key: uint256


class StdCheats(StdCheatsSafe):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol#651)
    """
    _abi = {}
    _storage_layout = {"storage":[{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"gasMeteringOff","offset":0,"slot":0,"type":"t_bool"},{"astId":5747,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"stdstore","offset":0,"slot":1,"type":"t_struct(StdStorage)8017_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/src/StdCheats.sol:StdCheats","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdCheats:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdCheats]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdCheats, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdCheats]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

