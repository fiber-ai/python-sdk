from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_company_exclusion_list_from_audience_response_200_charge_info_type_3_method import CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3Method






T = TypeVar("T", bound="CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3")



@_attrs_define
class CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3:
    """ No credits were charged for this operation

        Attributes:
            method (CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3Method):
            message (str):
     """

    method: CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3Method
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = CreateCompanyExclusionListFromAudienceResponse200ChargeInfoType3Method(d.pop("method"))




        message = d.pop("message")

        create_company_exclusion_list_from_audience_response_200_charge_info_type_3 = cls(
            method=method,
            message=message,
        )


        create_company_exclusion_list_from_audience_response_200_charge_info_type_3.additional_properties = d
        return create_company_exclusion_list_from_audience_response_200_charge_info_type_3

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
