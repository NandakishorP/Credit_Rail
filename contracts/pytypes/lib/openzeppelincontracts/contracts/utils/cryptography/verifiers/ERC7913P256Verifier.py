
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC7913 import IERC7913SignatureVerifier



class ERC7913P256Verifier(IERC7913SignatureVerifier):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#14)
    """
    _abi = {b'\x02J\xd3\x18': {'inputs': [{'internalType': 'bytes', 'name': 'key', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'verify', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60808060405234601557610c5a908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c63024ad31814610024575f80fd5b3461009c57606036600319011261009c5760043567ffffffffffffffff811161009c576100559036906004016100a0565b906044359067ffffffffffffffff821161009c5760209261007d6100899336906004016100a0565b929091602435916100ce565b6040516001600160e01b03199091168152f35b5f80fd5b9181601f8401121561009c5782359167ffffffffffffffff831161009c576020838186019501011161009c57565b939091936040831480610163575b6100f3575b506001600160e01b0319949350505050565b8260201161009c5780359260401161009c5760200135928160201161009c5780359160401161009c57602001359061012e848484848961016e565b909590156101545750505050505b61014a575f808080806100e1565b62495a6360e31b90565b61015e955061028a565b61013c565b5060408210156100dc565b9091929361017c8484610638565b158015610279575b156101955750505050505f90600190565b6020945f9460a094604051948552878501526040840152606083015260808201528280526101005afa15610277575f51156101d257600190600190565b60205f60a06040517fbb5a52f42f9c9261ed4361f59422a1e30036e7c32b270c8807a419feca6050238152600584820152600160408201527fa71af64de5126a4a4e02b7922d66ce9415ce88a4c9d25514d91082c8725ac95760608201527f5d47723c8fbe580bb369fec9c2665d8e30a435b9932645482e7c9f11e872296b60808201528280526101005afa15610277575f5115610271575f90600190565b5f905f90565bfe5b50610284818661069c565b15610184565b919093926102988286610638565b158015610627575b61061e576040519361020085810167ffffffffffffffff81118782101761060a576040525f5b8181106105f55750506020926104545f9360c0936102e2610716565b868152868882015286604082015289526102fa610716565b91825286820152600160408201528588019081528761044561031a610716565b7f6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c29681527f4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f58982015260016040820152608083019081526104366104276103808651610775565b92604086019384526103928151610775565b9061010087019182526103a888518651906107ae565b96606081019788526103bd89518351906107ae565b60a08201526103cf86518351906107ae565b8c8201526103e088518351906107ae565b60e08201526103f289518451906107ae565b61012082015261040586518451906107ae565b61014082015261016061041b89518551906107ae565b910152519051906107ae565b6101808d0181815295516107ae565b6101a08c0152518351906107ae565b6101c08a0152519051906107ae565b6101e087015260405190848252848083015284604083015260608201527bffffffff00000000000000004319055258e8617b0c46353d039cdab01960808201527bffffffff00000000000000004319055258e8617b0c46353d039cdaae1960a082015260055afa905f5191156105e3579091905f516020610c055f395f51905f52838509925f516020610c055f395f51905f529109905f905f925f945f915b6080831061051f57505050509061050a9291610b53565b505f516020610c055f395f51905f5290061490565b866105c1575b8160fe1c600c8260fc1c1617604061053d8287610750565b510151610559575b5060019060021b9160021b920191906104f3565b96919590948261059d575050506105708583610750565b5151936001604061059060206105868a88610750565b5101519886610750565b5101519695945b90610545565b906105b692916105b06001989987610750565b516108cc565b969195909594610597565b93956105d291956105d893976107cd565b916107cd565b959194909493610525565b634e487b715f5260126020526024601cfd5b602090610600610736565b81890152016102c6565b634e487b7160e01b5f52604160045260245ffd5b50505050505f90565b50610632848261069c565b156102a0565b908115159182610685575b508161067b575b81610653575090565b7f7fffffff800000007fffffffffffffffde737d56d38bcf4279dce5617e3192a89150111590565b801515915061064a565b5f516020610c055f395f51905f521191505f610643565b600160601b63ffffffff60c01b03197f5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b8183816003600160601b0363ffffffff60c01b031981838009080908600160601b63ffffffff60c01b031983800914600160601b63ffffffff60c01b031992831191909211161690565b604051906060820182811067ffffffffffffffff82111761060a57604052565b61073e610716565b905f82525f60208301525f6040830152565b9060108110156107615760051b0190565b634e487b7160e01b5f52603260045260245ffd5b61079590610781610736565b5080519060406020820151910151916107cd565b9061079e610716565b9283526020830152604082015290565b610795916107ba610736565b50805160406020830151920151926108cc565b929091600160601b63ffffffff60c01b0319838009600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b03199182910960020990565b60408101515f958695869591949391929091600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b031984800992600160601b63ffffffff60c01b03198086860960208501510991600160601b63ffffffff60c01b031983810381808585098a09089351600160601b63ffffffff60c01b03199086900990600160601b63ffffffff60c01b0319908282039082908b090890811585151694855f14610a82575050505050600114610987575b50505050565b929650909450919250600160601b63ffffffff60c01b031984800990600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b031991829109600209905f808080610981565b939c50919a5097985093969550929350600160601b63ffffffff60c01b03199150849050800991600160601b63ffffffff60c01b03199083900991600160601b63ffffffff60c01b031990840991600160601b63ffffffff60c01b03198082600209600160601b63ffffffff60c01b03199081039085810381868009080897600160601b63ffffffff60c01b031993849109600160601b63ffffffff60c01b031990810392909182908a8203900890090893600160601b63ffffffff60c01b0319928391099009905f808080610981565b92918015610bfa5760408051602080825281810181905291810182905260608101929092526bfffffffffffffffffffffffe63ffffffff60c01b03196080830152600160601b63ffffffff60c01b031960a0830152905f9060c09060055afa905f5191156105e357600160601b63ffffffff60c01b031982800993600160601b63ffffffff60c01b03199085900993600160601b63ffffffff60c01b031992839109900990565b505090505f905f9056feffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551a26469706673582212203906d386dfde6b5093fab343f945a170cbffe5a13a28c50bc9aef19d30b4eca764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC7913P256Verifier:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC7913P256Verifier]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC7913P256Verifier, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC7913P256Verifier]]:
        return cls._deploy(request_type, [], return_tx, ERC7913P256Verifier, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#16)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#16)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#16)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#16)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913P256Verifier.sol#16)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "024ad318", [key, hash, signature], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC7913P256Verifier.verify.selector = bytes4(b'\x02J\xd3\x18')
