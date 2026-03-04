from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.domain_lookup_polling_response_200_warnings_type_0_item import DomainLookupPollingResponse200WarningsType0Item
  from ..models.domain_lookup_polling_response_200_charge_info_type_0 import DomainLookupPollingResponse200ChargeInfoType0
  from ..models.domain_lookup_polling_response_200_output import DomainLookupPollingResponse200Output
  from ..models.domain_lookup_polling_response_200_charge_info_type_2 import DomainLookupPollingResponse200ChargeInfoType2
  from ..models.domain_lookup_polling_response_200_charge_info_type_1 import DomainLookupPollingResponse200ChargeInfoType1
  from ..models.domain_lookup_polling_response_200_charge_info_type_3 import DomainLookupPollingResponse200ChargeInfoType3





T = TypeVar("T", bound="DomainLookupPollingResponse200")



@_attrs_define
class DomainLookupPollingResponse200:
    """ 
        Attributes:
            output (DomainLookupPollingResponse200Output):
            charge_info (Union['DomainLookupPollingResponse200ChargeInfoType0',
                'DomainLookupPollingResponse200ChargeInfoType1', 'DomainLookupPollingResponse200ChargeInfoType2',
                'DomainLookupPollingResponse200ChargeInfoType3']):
            warnings (Union[None, Unset, list['DomainLookupPollingResponse200WarningsType0Item']]): Warnings about
                extraneous fields in request
     """

    output: 'DomainLookupPollingResponse200Output'
    charge_info: Union['DomainLookupPollingResponse200ChargeInfoType0', 'DomainLookupPollingResponse200ChargeInfoType1', 'DomainLookupPollingResponse200ChargeInfoType2', 'DomainLookupPollingResponse200ChargeInfoType3']
    warnings: Union[None, Unset, list['DomainLookupPollingResponse200WarningsType0Item']] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_lookup_polling_response_200_warnings_type_0_item import DomainLookupPollingResponse200WarningsType0Item
        from ..models.domain_lookup_polling_response_200_charge_info_type_0 import DomainLookupPollingResponse200ChargeInfoType0
        from ..models.domain_lookup_polling_response_200_output import DomainLookupPollingResponse200Output
        from ..models.domain_lookup_polling_response_200_charge_info_type_2 import DomainLookupPollingResponse200ChargeInfoType2
        from ..models.domain_lookup_polling_response_200_charge_info_type_1 import DomainLookupPollingResponse200ChargeInfoType1
        from ..models.domain_lookup_polling_response_200_charge_info_type_3 import DomainLookupPollingResponse200ChargeInfoType3
        output = self.output.to_dict()

        charge_info: dict[str, Any]
        if isinstance(self.charge_info, DomainLookupPollingResponse200ChargeInfoType0):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, DomainLookupPollingResponse200ChargeInfoType1):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, DomainLookupPollingResponse200ChargeInfoType2):
            charge_info = self.charge_info.to_dict()
        else:
            charge_info = self.charge_info.to_dict()


        warnings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)


        else:
            warnings = self.warnings


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "output": output,
            "chargeInfo": charge_info,
        })
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_lookup_polling_response_200_warnings_type_0_item import DomainLookupPollingResponse200WarningsType0Item
        from ..models.domain_lookup_polling_response_200_charge_info_type_0 import DomainLookupPollingResponse200ChargeInfoType0
        from ..models.domain_lookup_polling_response_200_output import DomainLookupPollingResponse200Output
        from ..models.domain_lookup_polling_response_200_charge_info_type_2 import DomainLookupPollingResponse200ChargeInfoType2
        from ..models.domain_lookup_polling_response_200_charge_info_type_1 import DomainLookupPollingResponse200ChargeInfoType1
        from ..models.domain_lookup_polling_response_200_charge_info_type_3 import DomainLookupPollingResponse200ChargeInfoType3
        d = dict(src_dict)
        output = DomainLookupPollingResponse200Output.from_dict(d.pop("output"))




        def _parse_charge_info(data: object) -> Union['DomainLookupPollingResponse200ChargeInfoType0', 'DomainLookupPollingResponse200ChargeInfoType1', 'DomainLookupPollingResponse200ChargeInfoType2', 'DomainLookupPollingResponse200ChargeInfoType3']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_0 = DomainLookupPollingResponse200ChargeInfoType0.from_dict(data)



                return charge_info_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_1 = DomainLookupPollingResponse200ChargeInfoType1.from_dict(data)



                return charge_info_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_2 = DomainLookupPollingResponse200ChargeInfoType2.from_dict(data)



                return charge_info_type_2
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            charge_info_type_3 = DomainLookupPollingResponse200ChargeInfoType3.from_dict(data)



            return charge_info_type_3

        charge_info = _parse_charge_info(d.pop("chargeInfo"))


        def _parse_warnings(data: object) -> Union[None, Unset, list['DomainLookupPollingResponse200WarningsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in (_warnings_type_0):
                    warnings_type_0_item = DomainLookupPollingResponse200WarningsType0Item.from_dict(warnings_type_0_item_data)



                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['DomainLookupPollingResponse200WarningsType0Item']], data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        domain_lookup_polling_response_200 = cls(
            output=output,
            charge_info=charge_info,
            warnings=warnings,
        )

        return domain_lookup_polling_response_200

