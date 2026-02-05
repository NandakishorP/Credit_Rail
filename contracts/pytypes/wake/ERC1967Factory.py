
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ERC1967Factory(Contract):
    """
    [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#7)
    """
    _abi = {b'0\x11d%': {'inputs': [], 'name': 'DeploymentFailed', 'type': 'error'}, b'/cH6': {'inputs': [], 'name': 'SaltDoesNotStartWithCaller', 'type': 'error'}, b'\x82\xb4)\x00': {'inputs': [], 'name': 'Unauthorized', 'type': 'error'}, b'U)\x9bI': {'inputs': [], 'name': 'UpgradeFailed', 'type': 'error'}, b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}, b'\xc9Y5\xa6m\x15\xe0\xda^A*\xca\n\xd2z\xe8\x91\xd2\x0b/\xb9\x1c\xf3\x99Kj;\xf2\xb8\x17\x80\x82': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'Deployed', 'type': 'event'}, b"]a\x1f1\x86\x80\xd0\x05\x98\xbbs]a\xba\xcf\x0cQLkP\xe1\xe5\xad0\x04\nM\xf2\xb1'\x91\xc7": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'*\xbb\xef\x15': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'name': 'adminOf', 'outputs': [{'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1a\xcf\xd0*': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'changeAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'T^|a': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'deploy', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'C\x14\xf1 ': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'deployAndCall', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'7)\xf9"': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'deployDeterministic', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xa9{\x90\xd5': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'address', 'name': 'admin', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'deployDeterministicAndCall', 'outputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, b'\xdbLT^': {'inputs': [], 'name': 'initCodeHash', 'outputs': [{'internalType': 'bytes32', 'name': 'result', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'T\x14\xdf\xf0': {'inputs': [{'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'predictDeterministicAddress', 'outputs': [{'internalType': 'address', 'name': 'predicted', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xa8\x8e\xc4': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'upgrade', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\x96#`\x9d': {'inputs': [{'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'upgradeAndCall', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60808060405234601557610764908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80631acfd02a146100b45780632abbef15146100af5780633729f922146100aa5780634314f120146100a55780635414dff0146100a0578063545e7c611461009b5780639623609d1461009657806399a88ec414610091578063a97b90d51461008c5763db4c545e14610087575f80fd5b610527565b6104cb565b610454565b6103cb565b610342565b6102f5565b61025c565b610179565b610148565b34610118576040366003190112610118576100cd61011c565b6100d5610132565b908060601b3381540361010b578290557f7e644d79422f17c01e4894b5f4f588d331ebfa28653d42ae832dc59e38c9798f5f80a3005b6382b429005f526004601cfd5b5f80fd5b600435906001600160a01b038216820361011857565b602435906001600160a01b038216820361011857565b3461011857602036600319011261011857602061016361011c565b60601b546040516001600160a01b039091168152f35b60603660031901126101185761018d61011c565b610195610132565b604435908160601c803314901517156101ca576020926101b8925f92369261054f565b6040516001600160a01b039091168152f35b632f6348365f526004601cfd5b9181601f840112156101185782359167ffffffffffffffff8311610118576020838186019501011161011857565b6060600319820112610118576004356001600160a01b038116810361011857916024356001600160a01b038116810361011857916044359067ffffffffffffffff821161011857610258916004016101d7565b9091565b61026536610205565b9091906102706105b3565b926088601385015ff09384156102e857825f9384938884525f51602061070f5f395f51905f52602085015260408401376040019034865af1156102da57602092818360601b55825f5160206106ef5f395f51905f525f80a46040516001600160a01b039091168152f35b3d156102e8573d5f803e3d5ffd5b63301164255f526004601cfd5b3461011857602036600319011261011857600435608860136103156105b3565b012060ff5f536035523060601b600152601552602060555f205f6035526040519060018060a01b03168152f35b60403660031901126101185761035661011c565b61035e610132565b6103666105b3565b906088601383015ff09182156102e8575f604082868394525f51602061070f5f395f51905f5260208201528236813734865af1156102da57602092818360601b55825f5160206106ef5f395f51905f525f80a46040516001600160a01b039091168152f35b6103d436610205565b929192338360601b540361010b575f91818392604051928784525f51602061070f5f395f51905f52602085015260408401376040019034855af115610439577f5d611f318680d00598bb735d61bacf0c514c6b50e1e5ad30040a4df2b12791c75f80a3005b3d15610447573d5f803e3d5ffd5b6355299b495f526004601cfd5b60403660031901126101185761046861011c565b610470610132565b90338160601b540361010b575f80604080518581525f51602061070f5f395f51905f5260208201528236813734855af115610439577f5d611f318680d00598bb735d61bacf0c514c6b50e1e5ad30040a4df2b12791c75f80a3005b6080366003190112610118576104df61011c565b6104e7610132565b9060443560643567ffffffffffffffff81116101185761050b9036906004016101d7565b918060601c803314901517156101ca576020946101b89461054f565b34610118575f366003190112610118576020608860136105456105b3565b0120604051908152f35b919493909261055c6105b3565b956088601388015ff59586156102e857825f9384938684525f51602061070f5f395f51905f52602085015260408401376040019034885af1156102da57818460601b55835f5160206106ef5f395f51905f525f80a4565b604051903060701c1561065757666052573d6000fd607b8301527f3d356020355560408036111560525736038060403d373d3d355af43d6000803e60748301527f3735a920a3ca505d382bbc545af43d6000803e6052573d6000fd5b3d6000f35b60548301527f14605757363d3d37363d7f360894a13ba1a3210667c828492db98dca3e2076cc60348301523060148301526c607f3d8160093d39f33d3d33738252565b66604c573d6000fd60758301527f3d3560203555604080361115604c5736038060403d373d3d355af43d6000803e606e8301527f3735a920a3ca505d382bbc545af43d6000803e604c573d6000fd5b3d6000f35b604e8301527f14605157363d3d37363d7f360894a13ba1a3210667c828492db98dca3e2076cc602e83015230600e8301526c60793d8160093d39f33d3d336d825256fec95935a66d15e0da5e412aca0ad27ae891d20b2fb91cf3994b6a3bf2b8178082360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbca264697066735822122029b5759b14a282aff0b7921c68050e96c8a0b51d08fb8b6b8b6859b0b227e90b64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1967Factory:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1967Factory]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1967Factory, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1967Factory]]:
        return cls._deploy(request_type, [], return_tx, ERC1967Factory, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Unauthorized(TransactionRevertedError):
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#13)
        """
        _abi = {'inputs': [], 'name': 'Unauthorized', 'type': 'error'}
        original_name = 'Unauthorized'
        selector = bytes4(b'\x82\xb4)\x00')



    @dataclasses.dataclass
    class DeploymentFailed(TransactionRevertedError):
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#16)
        """
        _abi = {'inputs': [], 'name': 'DeploymentFailed', 'type': 'error'}
        original_name = 'DeploymentFailed'
        selector = bytes4(b'0\x11d%')



    @dataclasses.dataclass
    class UpgradeFailed(TransactionRevertedError):
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#19)
        """
        _abi = {'inputs': [], 'name': 'UpgradeFailed', 'type': 'error'}
        original_name = 'UpgradeFailed'
        selector = bytes4(b'U)\x9bI')



    @dataclasses.dataclass
    class SaltDoesNotStartWithCaller(TransactionRevertedError):
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#22)
        """
        _abi = {'inputs': [], 'name': 'SaltDoesNotStartWithCaller', 'type': 'error'}
        original_name = 'SaltDoesNotStartWithCaller'
        selector = bytes4(b'/cH6')



    @dataclasses.dataclass
    class AdminChanged:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#41)

        Attributes:
            proxy (Address): indexed address
            admin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'AdminChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'AdminChanged'
        selector = bytes32(b'~dMyB/\x17\xc0\x1eH\x94\xb5\xf4\xf5\x88\xd31\xeb\xfa(e=B\xae\x83-\xc5\x9e8\xc9y\x8f')

        proxy: Address
        admin: Address


    @dataclasses.dataclass
    class Upgraded:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#44)

        Attributes:
            proxy (Address): indexed address
            implementation (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Upgraded'
        selector = bytes32(b"]a\x1f1\x86\x80\xd0\x05\x98\xbbs]a\xba\xcf\x0cQLkP\xe1\xe5\xad0\x04\nM\xf2\xb1'\x91\xc7")

        proxy: Address
        implementation: Address


    @dataclasses.dataclass
    class Deployed:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#47)

        Attributes:
            proxy (Address): indexed address
            implementation (Address): indexed address
            admin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'proxy', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'admin', 'type': 'address'}], 'name': 'Deployed', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Deployed'
        selector = bytes32(b'\xc9Y5\xa6m\x15\xe0\xda^A*\xca\n\xd2z\xe8\x91\xd2\x0b/\xb9\x1c\xf3\x99Kj;\xf2\xb8\x17\x80\x82')

        proxy: Address
        implementation: Address
        admin: Address


    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    @overload
    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        ...

    def adminOf(self, proxy: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#77)

        Args:
            proxy: address
        Returns:
            admin: address
        """
        return self._execute(self.chain, request_type, "2abbef15", [proxy], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    @overload
    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        ...

    def changeAdmin(self, proxy: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#85)

        Args:
            proxy: address
            admin: address
        """
        return self._execute(self.chain, request_type, "1acfd02a", [proxy, admin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    @overload
    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        ...

    def upgrade(self, proxy: Union[Account, Address], implementation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#105)

        Args:
            proxy: address
            implementation: address
        """
        return self._execute(self.chain, request_type, "99a88ec4", [proxy, implementation], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    @overload
    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        ...

    def upgradeAndCall(self, proxy: Union[Account, Address], implementation: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#112)

        Args:
            proxy: address
            implementation: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "9623609d", [proxy, implementation, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    @overload
    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        ...

    def deploy_(self, implementation: Union[Account, Address], admin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#150)

        Args:
            implementation: address
            admin: address
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "545e7c61", [implementation, admin], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        ...

    def deployAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#158)

        Args:
            implementation: address
            admin: address
            data: bytes
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "4314f120", [implementation, admin, data], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        ...

    def deployDeterministic(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#169)

        Args:
            implementation: address
            admin: address
            salt: bytes32
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "3729f922", [implementation, admin, salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    @overload
    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        ...

    def deployDeterministicAndCall(self, implementation: Union[Account, Address], admin: Union[Account, Address], salt: bytes32, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#181)

        Args:
            implementation: address
            admin: address
            salt: bytes32
            data: bytes
        Returns:
            proxy: address
        """
        return self._execute(self.chain, request_type, "a97b90d5", [implementation, admin, salt, data], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    @overload
    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        ...

    def predictDeterministicAddress(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#242)

        Args:
            salt: bytes32
        Returns:
            predicted: address
        """
        return self._execute(self.chain, request_type, "5414dff0", [salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    @overload
    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        ...

    def initCodeHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/ERC1967Factory.sol#261)

        Returns:
            result: bytes32
        """
        return self._execute(self.chain, request_type, "db4c545e", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC1967Factory.adminOf.selector = bytes4(b'*\xbb\xef\x15')
ERC1967Factory.changeAdmin.selector = bytes4(b'\x1a\xcf\xd0*')
ERC1967Factory.upgrade.selector = bytes4(b'\x99\xa8\x8e\xc4')
ERC1967Factory.upgradeAndCall.selector = bytes4(b'\x96#`\x9d')
ERC1967Factory.deploy_.selector = bytes4(b'T^|a')
ERC1967Factory.deployAndCall.selector = bytes4(b'C\x14\xf1 ')
ERC1967Factory.deployDeterministic.selector = bytes4(b'7)\xf9"')
ERC1967Factory.deployDeterministicAndCall.selector = bytes4(b'\xa9{\x90\xd5')
ERC1967Factory.predictDeterministicAddress.selector = bytes4(b'T\x14\xdf\xf0')
ERC1967Factory.initCodeHash.selector = bytes4(b'\xdbLT^')
