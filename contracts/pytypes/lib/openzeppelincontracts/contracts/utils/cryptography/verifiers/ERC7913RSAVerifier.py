
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC7913 import IERC7913SignatureVerifier



class ERC7913RSAVerifier(IERC7913SignatureVerifier):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#14)
    """
    _abi = {b'\x02J\xd3\x18': {'inputs': [{'internalType': 'bytes', 'name': 'key', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'verify', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608080604052346015576104ea908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c63024ad31814610024575f80fd5b3461014d57606036600319011261014d576004356001600160401b03811161014d57610054903690600401610151565b906044356001600160401b03811161014d57610074903690600401610151565b919092810160408282031261014d5781356001600160401b03811161014d578161009f9184016101f8565b916020810135906001600160401b03821161014d576020925f926100c392016101f8565b936100e9604051968488019260243584528589526100e260408a61017e565b36916101b3565b95604051918291518091835e8101838152039060025afa1561014257610110925f51610216565b1561013257602062495a6360e31b5b6040516001600160e01b03199091168152f35b60206001600160e01b031961011f565b6040513d5f823e3d90fd5b5f80fd5b9181601f8401121561014d578235916001600160401b03831161014d576020838186019501011161014d57565b90601f801991011681019081106001600160401b0382111761019f57604052565b634e487b7160e01b5f52604160045260245ffd5b9291926001600160401b03821161019f57604051916101dc601f8201601f19166020018461017e565b82948184528183011161014d578281602093845f960137010152565b9080601f8301121561014d57816020610213933591016101b3565b90565b9092805192610100841080156103c8575b6103bf57601f198401945f5b858110610373575b50610248939495506103d3565b929015610361578083016011198101519091906001600160f81b031916603160f81b0361031757720181898068304b0432400b281820100828002160651b906bffffffffffffffffffffffff19906034905b0360025b8181106102e9575060208601516001600160f01b031916600160f01b1495866102d7575b50505050826102d057505090565b5114919050565b0160200151161492505f8080806102c2565b602081880101516001600160f81b031916600160f81b0161030c5760010161029e565b505050505050505f90565b600f198201516001600160f81b031916602f60f81b0361035957700181798058304b0432400b28182010082160751b906001600160701b03199060329061029a565b505050505f90565b634e487b715f5260126020526024601cfd5b8681108782180287186020818401015160208287010151908181105f1461039c5750505061023b565b1190889082156103b5575b505061030c57602001610233565b149050875f6103a7565b50505050505f90565b508451841415610227565b92906103de8361047f565b61045d5760209061044884519183875196608082845194816040519c8d978289019d8e5260408901528960608901528051918291018589015e8601908382015f8152815193849201905e0101905f8252805192839101825e015f815203601f19810187528661017e565b80859486518160055afa948181520101604052565b509150506040519061047060208361017e565b5f8083523660208401375f9190565b5f5b81518110156104ad57818101602001516001600160f81b0319166104a757600101610481565b50505f90565b505060019056fea26469706673582212203632fa6cb313c50aa2bb42b80345ea9856dfb99d1d200b1051998169bfe6660164736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC7913RSAVerifier:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC7913RSAVerifier]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC7913RSAVerifier, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC7913RSAVerifier]]:
        return cls._deploy(request_type, [], return_tx, ERC7913RSAVerifier, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913RSAVerifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "024ad318", [key, hash, signature], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC7913RSAVerifier.verify.selector = bytes4(b'\x02J\xd3\x18')
