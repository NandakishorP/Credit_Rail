
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pytypes.src.CreditPolicy as CreditPolicy
else:
    import lazy_import

    CreditPolicy = lazy_import.lazy_module('pytypes.src.CreditPolicy')



class ICreditPolicy(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#5)
    """
    _abi = {b'\xf7pq;': {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'changePolicyAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x04\xbd\x12\xbb': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'createPolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0e\xde\xa5\xb8': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'deActivatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'L\xfaz\xf6': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'excludeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfbM\xcb\x8b': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'freezePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0c5)\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'includeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfaOZ\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'isIndustryExcluded', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x8a\xfaF': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyActive', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'L-b\xb7': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'[\x87\xec.': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'uint256', 'name': 'minRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLoanToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'active', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.LoanTier', 'name': 'tier', 'type': 'tuple'}], 'name': 'setLoanTier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"9'\xa4\xc3": {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'uri', 'type': 'string'}], 'name': 'setPolicyDocument', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Ie\x9c\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'tierExistsInPolicy', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'f0\xb0\x08': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxAttestationAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'reAttestationFrequencyDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'requiresCPAAttestation', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.AttestationRequirements', 'name': 'data', 'type': 'tuple'}], 'name': 'updateAttestation', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'i\xb6S1': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxSingleBorrowerBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxIndustryConcentrationBps', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.ConcentrationLimits', 'name': 'data', 'type': 'tuple'}], 'name': 'updateConcentration', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l\x11\xa3\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxLeverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minLiquidityAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'allowsDividends', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'reportingFrequencyDays', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.MaintenanceCovenants', 'name': 'data', 'type': 'tuple'}], 'name': 'updateCovenants', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'w\xe4\xd4\xad': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'minAnnualRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minTangibleNetWorth', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minBusinessAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDefaultsLast36Months', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'bankruptcyExcluded', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.EligibilityCriteria', 'name': 'data', 'type': 'tuple'}], 'name': 'updateEligibility', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa4\xd2F\xfa': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxTotalDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCurrentRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDAMarginBps', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.FinancialRatios', 'name': 'data', 'type': 'tuple'}], 'name': 'updateRatios', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ICreditPolicy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ICreditPolicy]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#6)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#6)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#6)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#6)

        Args:
            version: uint256
        """
        ...

    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#6)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "04bd12bb", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#8)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#8)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#8)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#8)

        Args:
            version: uint256
        """
        ...

    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#8)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "fb4dcb8b", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#10)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#10)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#10)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#10)

        Args:
            version: uint256
        """
        ...

    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#10)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "0edea5b8", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#12)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#12)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#12)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#12)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    def updateEligibility(self, version: uint256, data: CreditPolicy.CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#12)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        return self._execute(self.chain, request_type, "77e4d4ad", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#17)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#17)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#17)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#17)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    def updateRatios(self, version: uint256, data: CreditPolicy.CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#17)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        return self._execute(self.chain, request_type, "a4d246fa", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#22)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#22)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#22)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#22)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    def updateConcentration(self, version: uint256, data: CreditPolicy.CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#22)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        return self._execute(self.chain, request_type, "69b65331", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#27)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#27)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#27)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#27)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    def updateAttestation(self, version: uint256, data: CreditPolicy.CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#27)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        return self._execute(self.chain, request_type, "6630b008", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#32)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#32)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#32)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#32)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    def updateCovenants(self, version: uint256, data: CreditPolicy.CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#32)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        return self._execute(self.chain, request_type, "6c11a386", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#37)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#37)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#37)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#37)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#37)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        return self._execute(self.chain, request_type, "5b87ec2e", [version, tierId, tier], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#43)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#43)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#43)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#43)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#43)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "4cfa7af6", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#45)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#45)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#45)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#45)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#45)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "0c3529dc", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#47)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#47)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#47)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#47)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#47)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        return self._execute(self.chain, request_type, "3927a4c3", [version, hash, uri], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#53)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#53)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#53)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#53)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#53)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "49659cdc", [version, tierId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#58)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#58)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#58)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#58)

        Args:
            newAdmin: address
        """
        ...

    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#58)

        Args:
            newAdmin: address
        """
        return self._execute(self.chain, request_type, "f770713b", [newAdmin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#60)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#60)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#60)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#60)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#60)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "bd8afa46", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#62)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#62)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#62)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#62)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#62)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4c2d62b7", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#64)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#64)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#64)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#64)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/interfaces/ICreditPolicy.sol#64)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fa4f5a86", [version, industry], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ICreditPolicy.createPolicy.selector = bytes4(b'\x04\xbd\x12\xbb')
ICreditPolicy.freezePolicy.selector = bytes4(b'\xfbM\xcb\x8b')
ICreditPolicy.deActivatePolicy.selector = bytes4(b'\x0e\xde\xa5\xb8')
ICreditPolicy.updateEligibility.selector = bytes4(b'w\xe4\xd4\xad')
ICreditPolicy.updateRatios.selector = bytes4(b'\xa4\xd2F\xfa')
ICreditPolicy.updateConcentration.selector = bytes4(b'i\xb6S1')
ICreditPolicy.updateAttestation.selector = bytes4(b'f0\xb0\x08')
ICreditPolicy.updateCovenants.selector = bytes4(b'l\x11\xa3\x86')
ICreditPolicy.setLoanTier.selector = bytes4(b'[\x87\xec.')
ICreditPolicy.excludeIndustry.selector = bytes4(b'L\xfaz\xf6')
ICreditPolicy.includeIndustry.selector = bytes4(b'\x0c5)\xdc')
ICreditPolicy.setPolicyDocument.selector = bytes4(b"9'\xa4\xc3")
ICreditPolicy.tierExistsInPolicy.selector = bytes4(b'Ie\x9c\xdc')
ICreditPolicy.changePolicyAdmin.selector = bytes4(b'\xf7pq;')
ICreditPolicy.isPolicyActive.selector = bytes4(b'\xbd\x8a\xfaF')
ICreditPolicy.isPolicyFrozen.selector = bytes4(b'L-b\xb7')
ICreditPolicy.isIndustryExcluded.selector = bytes4(b'\xfaOZ\x86')
