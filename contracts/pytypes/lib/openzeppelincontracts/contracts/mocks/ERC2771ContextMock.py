
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.metatx.ERC2771Context import ERC2771Context
from pytypes.lib.openzeppelincontracts.contracts.mocks.ContextMock import ContextMock
from pytypes.lib.openzeppelincontracts.contracts.utils.Multicall import Multicall



class ERC2771ContextMock(Multicall, ERC2771Context, ContextMock):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#11)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'trustedForwarder', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xaf#ST\xa0\xa4|\x91\xee\x17\x19a2c5\xcb-\x1a\x8eU\xb8\xa8\x98Y\xb0\xe6\x1e\xb0I\xe5\x0e\xa0': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'integerValue', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'stringValue', 'type': 'string'}], 'name': 'Data', 'type': 'event'}, b'm|\xecq\xeb\xa4g)M\x924\x1d\xdcN\x864\xebMt*\x90\xe1o@\x8f\x06\xe4\xb7\x0b\xc4\xcdf': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'DataShort', 'type': 'event'}, b"\xd6U\x8c>\xd9\x10\xd9Y'\x10TG\x1f\xd1\xc3&g\x9d\x9f\xec\xe9\x9cP\x91\xb0\x0e\xd8\x96'\xcf+\xfc": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'Sender', 'type': 'event'}, b'W+l\x05': {'inputs': [{'internalType': 'address', 'name': 'forwarder', 'type': 'address'}], 'name': 'isTrustedForwarder', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'7k\xf2b': {'inputs': [{'internalType': 'uint256', 'name': 'integerValue', 'type': 'uint256'}, {'internalType': 'string', 'name': 'stringValue', 'type': 'string'}], 'name': 'msgData', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xff_kY': {'inputs': [], 'name': 'msgDataShort', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd77\xd0\xc7': {'inputs': [], 'name': 'msgSender', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xac\x96P\xd8': {'inputs': [{'internalType': 'bytes[]', 'name': 'data', 'type': 'bytes[]'}], 'name': 'multicall', 'outputs': [{'internalType': 'bytes[]', 'name': 'results', 'type': 'bytes[]'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'}\xa0\xa8w': {'inputs': [], 'name': 'trustedForwarder', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60a0346100bb57601f6107cd38819003918201601f19168301916001600160401b038311848410176100bf578084926020946040528339810103126100bb57516001600160a01b03811681036100bb576080527fd6558c3ed910d959271054471fd1c326679d9fece99c5091b00ed89627cf2bfc602061007d6100d3565b6040516001600160a01b039091168152a16040516106be908161010f82396080518181816103230152818161037d01528181610601015261065a0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b6014361015806100fa575b156100f65760131936013681116100bb573560601c90565b3390565b506080516001600160a01b031633146100de56fe60806040526004361015610011575f80fd5b5f3560e01c8063376bf262146103af578063572b6c05146103525780637da0a8771461030e578063ac9650d814610102578063d737d0c7146100b45763ff5f6b591461005b575f80fd5b346100b0575f3660031901126100b0577f6d7cec71eba467294d92341ddc4e8634eb4d742a90e16f408f06e4b70bc4cd666100946105d5565b6100ab6040519283926020845260208401916104ea565b0390a1005b5f80fd5b346100b0575f3660031901126100b0577fd6558c3ed910d959271054471fd1c326679d9fece99c5091b00ed89627cf2bfc60206100ef61062f565b6040516001600160a01b039091168152a1005b346100b05760203660031901126100b0576004356001600160401b0381116100b057366023820112156100b0578060040135906001600160401b0382116100b0573660248360051b830101116100b0576001600160a01b0361016261062f565b1633145f146102d95760405161017960208261044c565b5f8082523660208301379190915b6101908261050a565b9261019e604051948561044c565b828452601f196101ad8461050a565b015f5b8181106102c65750503681900360421901905f5b8481101561025f5760248160051b83010135838112156100b0578201906024820135916001600160401b0383116100b05760440182360381136100b0578261023d610243926020806001976040519586948386013783018b8282015f8152815193849201905e01015f815203601f19810183528261044c565b30610549565b61024d8289610521565b526102588188610521565b50016101c4565b856040518091602082016020835281518091526040830190602060408260051b8601019301915f905b82821061029757505050500390f35b919360019193955060206102b68192603f198a820301865288516104c6565b9601920192018594939192610288565b60606020828801810191909152016101b0565b60131936013681116102fa576102f29060143691610481565b919091610187565b634e487b7160e01b5f52601160045260245ffd5b346100b0575f3660031901126100b0576040517f00000000000000000000000000000000000000000000000000000000000000006001600160a01b03168152602090f35b346100b05760203660031901126100b0576004356001600160a01b038116908190036100b0576040517f00000000000000000000000000000000000000000000000000000000000000006001600160a01b03169091148152602090f35b346100b05760403660031901126100b0576024356001600160401b0381116100b057366023820112156100b0576104117faf235354a0a47c91ee171961326335cb2d1a8e55b8a89859b0e61eb049e50ea0913690602481600401359101610481565b6100ab61041c6105d5565b9190926104366040519485946060865260608601916104ea565b90600435602085015283820360408501526104c6565b90601f801991011681019081106001600160401b0382111761046d57604052565b634e487b7160e01b5f52604160045260245ffd5b9291926001600160401b03821161046d57604051916104aa601f8201601f19166020018461044c565b8294818452818301116100b0578281602093845f960137010152565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b908060209392818452848401375f828201840152601f01601f1916010190565b6001600160401b03811161046d5760051b60200190565b80518210156105355760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b905f8091602081519101845af480806105c2575b1561057d5750506040513d81523d5f602083013e60203d82010160405290565b156105a257639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d156105b3576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d15158061055d5750813b151561055d565b6014361015806105fd575b156105f7576013193601903682116100b0575f9190565b5f903690565b50337f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316146105e0565b601436101580610656575b156106525760131936013681116100b0573560601c90565b3390565b50337f00000000000000000000000000000000000000000000000000000000000000006001600160a01b03161461063a56fea2646970667358221220cd5b9f3ebb2b1a3cef3f287d9febb96f5d00bbcfa7562979acee699ad8442a6664736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC2771ContextMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC2771ContextMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        ...

    @classmethod
    def deploy(cls, trustedForwarder: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC2771ContextMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC2771ContextMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ERC2771ContextMock.sol#13)

        Args:
            trustedForwarder: address
        """
        return cls._deploy(request_type, [trustedForwarder], return_tx, ERC2771ContextMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

