
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC1967 import IERC1967
from pytypes.lib.openzeppelincontracts.contracts.proxy.ERC1967.ERC1967Proxy import ERC1967Proxy



class ITransparentUpgradeableProxy(IERC1967):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#17)
    """
    _abi = {b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'previousAdmin', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}, b'\x1c\xf3\xb0:l\xf1\x9f\xa2\xba\xbaM\xf1H\xe9\xdc\xab\xed\xea\x7f\x8a\\\x07\x84\x0e ~\\\x08\x9b\xe9]>': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'beacon', 'type': 'address'}], 'name': 'BeaconUpgraded', 'type': 'event'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'O\x1e\xf2\x86': {'inputs': [{'internalType': 'address', 'name': 'newImplementation', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'upgradeToAndCall', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ITransparentUpgradeableProxy:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ITransparentUpgradeableProxy]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ITransparentUpgradeableProxy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ITransparentUpgradeableProxy]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @overload
    def upgradeToAndCall(self, newImplementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#19)

        Args:
            newImplementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeToAndCall(self, newImplementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#19)

        Args:
            newImplementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeToAndCall(self, newImplementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#19)

        Args:
            newImplementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeToAndCall(self, newImplementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#19)

        Args:
            newImplementation: address
            data: bytes
        """
        ...

    def upgradeToAndCall(self, newImplementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#19)

        Args:
            newImplementation: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "4f1ef286", [newImplementation, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ITransparentUpgradeableProxy.upgradeToAndCall.selector = bytes4(b'O\x1e\xf2\x86')
class TransparentUpgradeableProxy(ERC1967Proxy):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#62)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': '_logic', 'type': 'address'}, {'internalType': 'address', 'name': 'initialOwner', 'type': 'address'}, {'internalType': 'bytes', 'name': '_data', 'type': 'bytes'}], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'b\xe7{\xa2': {'inputs': [{'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'ERC1967InvalidAdmin', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xd2\xb5v\xec': {'inputs': [], 'name': 'ProxyDeniedAdminAccess', 'type': 'error'}, b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'previousAdmin', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, 'fallback': {'stateMutability': 'payable', 'type': 'fallback'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60a0604052610a69803803806100148161024a565b92833981016060828203126102465761002c8261026f565b906100396020840161026f565b604084015190936001600160401b038211610246570181601f82011215610246578051906001600160401b0382116101fa5761007e601f8301601f191660200161024a565b928284526020838301011161024657815f9260208093018386015e83010152813b15610225577f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc80546001600160a01b0319166001600160a01b0384169081179091557fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b5f80a280511561020e5761011591610283565b505b604051906104408083016001600160401b038111848210176101fa57602092849261060984396001600160a01b031681520301905ff080156101ef5760018060a01b0316806080525f516020610a495f395f51905f52547f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f6040805160018060a01b0384168152846020820152a181156101dc576001600160a01b031916175f516020610a495f395f51905f52556040516102f9908161031082396080518160070152f35b633173bdd160e11b5f525f60045260245ffd5b6040513d5f823e3d90fd5b634e487b7160e01b5f52604160045260245ffd5b505034156101175763b398979f60e01b5f5260045ffd5b50634c9c8ce360e01b5f9081526001600160a01b0391909116600452602490fd5b5f80fd5b6040519190601f01601f191682016001600160401b038111838210176101fa57604052565b51906001600160a01b038216820361024657565b905f8091602081519101845af480806102fc575b156102b75750506040513d81523d5f602083013e60203d82010160405290565b156102dc57639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d156102ed576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806102975750813b151561029756fe6080604052337f00000000000000000000000000000000000000000000000000000000000000006001600160a01b031603610066575f356001600160e01b03191663278f794360e11b1461005c576334ad5dbb60e21b5f5260045ffd5b6100646100c3565b005b7f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc545f9081906001600160a01b0316368280378136915af43d5f803e156100ab573d5ff35b3d5ffd5b634e487b7160e01b5f52604160045260245ffd5b36600411610173576040366003190112610173576004356001600160a01b03811690819003610173576024359067ffffffffffffffff821161017357366023830112156101735781600401359067ffffffffffffffff82116101775760405191601f8101601f19908116603f0116830167ffffffffffffffff811184821017610177576040528083523660248286010111610173576020815f9260246101719701838701378401015261017c565b565b5f80fd5b6100af565b90813b15610210577f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc80546001600160a01b0319166001600160a01b0384169081179091557fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b5f80a28051156101f8576101f591610231565b50565b50503461020157565b63b398979f60e01b5f5260045ffd5b50634c9c8ce360e01b5f9081526001600160a01b0391909116600452602490fd5b905f8091602081519101845af48080610297575b156102575750506102546102aa565b90565b1561027757639996b31560e01b5f526001600160a01b031660045260245ffd5b3d15610288576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806102455750813b1515610245565b604051903d82523d5f602084013e60203d83010160405256fea2646970667358221220b79d77189bce0548b7e990d4ab3a5d2fe2e0b117e5a98e3438978d87a21b21e264736f6c6343000821003360803460b857601f61044038819003918201601f19168301916001600160401b0383118484101760bc5780849260209460405283398101031260b857516001600160a01b0381169081900360b857801560a5575f80546001600160a01b031981168317825560405192916001600160a01b03909116907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e09080a361036f90816100d18239f35b631e4fbdf760e01b5f525f60045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f5f3560e01c8063715018a6146102765780638da5cb5b1461024f5780639623609d1461012c578063ad3cb1cc146100df5763f2fde38b14610051575f80fd5b346100dc5760203660031901126100dc576004356001600160a01b038116908190036100da5761007f610313565b80156100c65781546001600160a01b03198116821783556001600160a01b03167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08380a380f35b631e4fbdf760e01b82526004829052602482fd5b505b80fd5b50346100dc57806003193601126100dc57506101286040516101026040826102cd565b60058152640352e302e360dc1b60208201526040519182916020835260208301906102ef565b0390f35b506060366003190112610237576004356001600160a01b03811690819003610237576024356001600160a01b038116908190036102375760443567ffffffffffffffff8111610237573660238201121561023757806004013567ffffffffffffffff811161023b57604051916101ac601f8301601f1916602001846102cd565b818352366024838301011161023757815f9260246020930183860137830101526101d4610313565b823b156102375761020a925f9260405180958194829363278f794360e11b845260048401526040602484015260448301906102ef565b039134905af1801561022c5761021e575080f35b61022a91505f906102cd565b005b6040513d5f823e3d90fd5b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b34610237575f366003190112610237575f546040516001600160a01b039091168152602090f35b34610237575f3660031901126102375761028e610313565b5f80546001600160a01b0319811682556001600160a01b03167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08280a3005b90601f8019910116810190811067ffffffffffffffff82111761023b57604052565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b5f546001600160a01b0316330361032657565b63118cdaa760e01b5f523360045260245ffdfea2646970667358221220932bb9650fa3195658bce2703b1cb321333078d8f41080e62a107958ec24b44864736f6c63430008210033b53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103"

    @overload
    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransparentUpgradeableProxy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[TransparentUpgradeableProxy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        ...

    @classmethod
    def deploy(cls, _logic: Union[Account, Address], initialOwner: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, TransparentUpgradeableProxy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[TransparentUpgradeableProxy]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#79)

        Args:
            _logic: address
            initialOwner: address
            _data: bytes
        """
        return cls._deploy(request_type, [_logic, initialOwner, _data], return_tx, TransparentUpgradeableProxy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ProxyDeniedAdminAccess(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/transparent/TransparentUpgradeableProxy.sol#72)
        """
        _abi = {'inputs': [], 'name': 'ProxyDeniedAdminAccess', 'type': 'error'}
        original_name = 'ProxyDeniedAdminAccess'
        selector = bytes4(b'\xd2\xb5v\xec')



