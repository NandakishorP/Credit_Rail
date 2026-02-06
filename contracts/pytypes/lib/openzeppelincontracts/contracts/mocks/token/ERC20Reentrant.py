
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.token.ERC20.ERC20 import ERC20



class ERC20Reentrant(ERC20):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#7)
    """
    _abi = {b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'\xfb\x8fA\xb2': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientAllowance', 'type': 'error'}, b'\xe4P\xd3\x8c': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientBalance', 'type': 'error'}, b'\xe6\x02\xdf\x05': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC20InvalidApprover', 'type': 'error'}, b'\xecD/\x05': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC20InvalidReceiver', 'type': 'error'}, b'\x96\xc6\xfd\x1e': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC20InvalidSender', 'type': 'error'}, b'\x94(\rb': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC20InvalidSpender', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa0\xb5\xff\xb0': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'functionCall', 'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcdYKc': {'inputs': [{'internalType': 'enum ERC20Reentrant.Type', 'name': 'when', 'type': 'uint8'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'scheduleReenter', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":271,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_uint256)"},{"astId":277,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_allowances","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_uint256))"},{"astId":279,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_totalSupply","offset":0,"slot":2,"type":"t_uint256"},{"astId":281,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_name","offset":0,"slot":3,"type":"t_string_storage"},{"astId":283,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_symbol","offset":0,"slot":4,"type":"t_string_storage"},{"astId":153,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_reenterType","offset":0,"slot":5,"type":"t_enum(Type)150"},{"astId":155,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_reenterTarget","offset":1,"slot":5,"type":"t_address"},{"astId":157,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol:ERC20Reentrant","label":"_reenterData","offset":0,"slot":6,"type":"t_bytes_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_enum(Type)150":{"encoding":"inplace","label":"enum ERC20Reentrant.Type","numberOfBytes":1},"t_mapping(t_address,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(address => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60806040523461032357604080519081016001600160401b0381118282101761022b5760409081526004825263151154d560e21b602083015280519081016001600160401b0381118282101761022b5760405260038152621514d560ea1b602082015281516001600160401b03811161022b57600354600181811c91168015610319575b602082101461020d57601f81116102ab575b50602092601f821160011461024a57928192935f9261023f575b50508160011b915f199060031b1c1916176003555b80516001600160401b03811161022b57600454600181811c91168015610221575b602082101461020d57601f811161019f575b50602091601f821160011461013f579181925f92610134575b50508160011b915f199060031b1c1916176004555b604051610a4090816103288239f35b015190505f80610110565b601f1982169260045f52805f20915f5b8581106101875750836001951061016f575b505050811b01600455610125565b01515f1960f88460031b161c191690555f8080610161565b9192602060018192868501518155019401920161014f565b818111156100f75760045f52601f820160051c7f8a35acfbc15ff81a39ae7d344fd709f28e8600b4aa8c65c6b64bfe7fe36bd19b60208410610205575b81601f9101920160051c03905f5b8281106101f85750506100f7565b5f828201556001016101ea565b5f91506101dc565b634e487b7160e01b5f52602260045260245ffd5b90607f16906100e5565b634e487b7160e01b5f52604160045260245ffd5b015190505f806100af565b601f1982169360035f52805f20915f5b868110610293575083600195961061027b575b505050811b016003556100c4565b01515f1960f88460031b161c191690555f808061026d565b9192602060018192868501518155019401920161025a565b818111156100955760035f52601f820160051c7fc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b60208410610311575b81601f9101920160051c03905f5b828110610304575050610095565b5f828201556001016102f6565b5f91506102e8565b90607f1690610083565b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c90816306fdde031461062557508063095ea7b3146105a357806318160ddd1461058657806323b872dd146104a7578063313ce5671461048c57806370a082311461045557806395d89b411461038b578063a0b5ffb0146102d1578063a9059cbb146102a0578063cd594b63146100e95763dd62ed3e14610095575f80fd5b346100e55760403660031901126100e5576100ae6106eb565b6100b6610701565b6001600160a01b039182165f908152600160209081526040808320949093168252928352819020549051908152f35b5f80fd5b346100e55760603660031901126100e55760043560038110156100e55761010e610701565b906044359167ffffffffffffffff83116100e557366023840112156100e55782600401359167ffffffffffffffff83116100e55736602484860101116100e557600580546001600160a81b03191660ff929092169190911760089290921b610100600160a81b031691909117905560065461018890610739565b601f8111610232575b505f601f82116001146101cd5781925f926101bf575b50505f19600383901b1c191660019190911b17600655005b6024925001013582806101a7565b601f1982169260065f5260205f20915f5b858110610217575083600195106101fb575b505050811b01600655005b01602401355f19600384901b60f8161c191690558280806101f0565b909260206001819260248787010135815501940191016101de565b818111156101915760065f52601f820160051c7ff652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f60208410610298575b81601f9101920160051c03905f5b82811061028b575050610191565b5f8282015560010161027d565b5f915061026f565b346100e55760403660031901126100e5576102c66102bc6106eb565b6024359033610771565b602060405160018152f35b346100e55760403660031901126100e5576102ea6106eb565b60243567ffffffffffffffff81116100e557366023820112156100e55780600401359167ffffffffffffffff83116103775760405190610334601f8501601f191660200183610717565b83825236602485850101116100e5575f60208561037396602461035f9701838701378401015261097d565b6040519182916020835260208301906106c7565b0390f35b634e487b7160e01b5f52604160045260245ffd5b346100e5575f3660031901126100e5576040515f6004546103ab81610739565b808452906001811690811561043157506001146103d3575b6103738361035f81850382610717565b60045f9081527f8a35acfbc15ff81a39ae7d344fd709f28e8600b4aa8c65c6b64bfe7fe36bd19b939250905b8082106104175750909150810160200161035f6103c3565b9192600181602092548385880101520191019092916103ff565b60ff191660208086019190915291151560051b8401909101915061035f90506103c3565b346100e55760203660031901126100e5576001600160a01b036104766106eb565b165f525f602052602060405f2054604051908152f35b346100e5575f3660031901126100e557602060405160128152f35b346100e55760603660031901126100e5576104c06106eb565b6104c8610701565b6001600160a01b0382165f818152600160209081526040808320338452909152902054909260443592915f198110610506575b506102c69350610771565b83811061056b578415610558573315610545576102c6945f52600160205260405f2060018060a01b0333165f526020528360405f2091039055846104fb565b634a1406b160e11b5f525f60045260245ffd5b63e602df0560e01b5f525f60045260245ffd5b8390637dc7a0d960e11b5f523360045260245260445260645ffd5b346100e5575f3660031901126100e5576020600254604051908152f35b346100e55760403660031901126100e5576105bc6106eb565b602435903315610558576001600160a01b031690811561054557335f52600160205260405f20825f526020528060405f20556040519081527f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560203392a3602060405160018152f35b346100e5575f3660031901126100e5575f60035461064281610739565b80845290600181169081156104315750600114610669576103738361035f81850382610717565b60035f9081527fc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b939250905b8082106106ad5750909150810160200161035f6103c3565b919260018160209254838588010152019101909291610695565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b600435906001600160a01b03821682036100e557565b602435906001600160a01b03821682036100e557565b90601f8019910116810190811067ffffffffffffffff82111761037757604052565b90600182811c92168015610767575b602083101461075357565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610748565b6001600160a01b03169081156108b3576001600160a01b03169182156108a05760ff60055416600381101561084957600114610876575b815f525f60205260405f205481811061085d57817fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef92602092855f525f84520360405f2055845f525f825260405f20818154019055604051908152a360ff6005541660038110156108495760021461081c57565b6005805460ff1981169091556108469060081c6001600160a01b03166108406108c6565b9061097d565b50565b634e487b7160e01b5f52602160045260245ffd5b8263391434e360e21b5f5260045260245260445260645ffd5b6005805460ff19811690915561089a9060081c6001600160a01b03166108406108c6565b506107a8565b63ec442f0560e01b5f525f60045260245ffd5b634b637e8f60e11b5f525f60045260245ffd5b604051905f82600654916108d983610739565b808352926001811690811561095e57506001146108ff575b6108fd92500383610717565b565b5060065f90815290917ff652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f5b8183106109425750509060206108fd928201016108f1565b602091935080600191548385890101520191019091849261092a565b602092506108fd94915060ff191682840152151560051b8201016108f1565b905f809160208151910182855af180806109f7575b156109b25750506040513d81523d5f602083013e60203d82010160405290565b156109d757639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d156109e8576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806109925750813b151561099256fea2646970667358221220a71d88bba3f5ff87635854f151b96e354981f638dda4902f7fb0c266abe3ed3764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC20Reentrant:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC20Reentrant]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC20Reentrant, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC20Reentrant]]:
        return cls._deploy(request_type, [], return_tx, ERC20Reentrant, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class Type(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#8)

        """
        No = 0
        Before = 1
        After = 2


    @overload
    def scheduleReenter(self, when: ERC20Reentrant.Type, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#18)

        Args:
            when: enum ERC20Reentrant.Type
            target: address
            data: bytes
        """
        ...

    @overload
    def scheduleReenter(self, when: ERC20Reentrant.Type, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#18)

        Args:
            when: enum ERC20Reentrant.Type
            target: address
            data: bytes
        """
        ...

    @overload
    def scheduleReenter(self, when: ERC20Reentrant.Type, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#18)

        Args:
            when: enum ERC20Reentrant.Type
            target: address
            data: bytes
        """
        ...

    @overload
    def scheduleReenter(self, when: ERC20Reentrant.Type, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#18)

        Args:
            when: enum ERC20Reentrant.Type
            target: address
            data: bytes
        """
        ...

    def scheduleReenter(self, when: ERC20Reentrant.Type, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#18)

        Args:
            when: enum ERC20Reentrant.Type
            target: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "cd594b63", [when, target, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def functionCall(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#24)

        Args:
            target: address
            data: bytes
        Returns:
            bytes
        """
        ...

    @overload
    def functionCall(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#24)

        Args:
            target: address
            data: bytes
        Returns:
            bytes
        """
        ...

    @overload
    def functionCall(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#24)

        Args:
            target: address
            data: bytes
        Returns:
            bytes
        """
        ...

    @overload
    def functionCall(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#24)

        Args:
            target: address
            data: bytes
        Returns:
            bytes
        """
        ...

    def functionCall(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, TransactionAbc[bytearray], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Reentrant.sol#24)

        Args:
            target: address
            data: bytes
        Returns:
            bytes
        """
        return self._execute(self.chain, request_type, "a0b5ffb0", [target, data], True if request_type == "tx" else False, bytearray, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC20Reentrant.scheduleReenter.selector = bytes4(b'\xcdYKc')
ERC20Reentrant.functionCall.selector = bytes4(b'\xa0\xb5\xff\xb0')
