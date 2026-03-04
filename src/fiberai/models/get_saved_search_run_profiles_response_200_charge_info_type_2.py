from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_saved_search_run_profiles_response_200_charge_info_type_2_method import GetSavedSearchRunProfilesResponse200ChargeInfoType2Method






T = TypeVar("T", bound="GetSavedSearchRunProfilesResponse200ChargeInfoType2")



@_attrs_define
class GetSavedSearchRunProfilesResponse200ChargeInfoType2:
    """ Credits that were charged for an asynchronous operation

        Attributes:
            method (GetSavedSearchRunProfilesResponse200ChargeInfoType2Method):
            credits_charged (float):
            message (str):
     """

    method: GetSavedSearchRunProfilesResponse200ChargeInfoType2Method
    credits_charged: float
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        credits_charged = self.credits_charged

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "creditsCharged": credits_charged,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = GetSavedSearchRunProfilesResponse200ChargeInfoType2Method(d.pop("method"))




        credits_charged = d.pop("creditsCharged")

        message = d.pop("message")

        get_saved_search_run_profiles_response_200_charge_info_type_2 = cls(
            method=method,
            credits_charged=credits_charged,
            message=message,
        )


        get_saved_search_run_profiles_response_200_charge_info_type_2.additional_properties = d
        return get_saved_search_run_profiles_response_200_charge_info_type_2

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
