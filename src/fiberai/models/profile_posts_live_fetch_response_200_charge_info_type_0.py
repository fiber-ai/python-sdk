from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.profile_posts_live_fetch_response_200_charge_info_type_0_method import ProfilePostsLiveFetchResponse200ChargeInfoType0Method






T = TypeVar("T", bound="ProfilePostsLiveFetchResponse200ChargeInfoType0")



@_attrs_define
class ProfilePostsLiveFetchResponse200ChargeInfoType0:
    """ Credits were charged immediately for this operation

        Attributes:
            method (ProfilePostsLiveFetchResponse200ChargeInfoType0Method):
            credits_charged (float):
     """

    method: ProfilePostsLiveFetchResponse200ChargeInfoType0Method
    credits_charged: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        credits_charged = self.credits_charged


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "creditsCharged": credits_charged,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = ProfilePostsLiveFetchResponse200ChargeInfoType0Method(d.pop("method"))




        credits_charged = d.pop("creditsCharged")

        profile_posts_live_fetch_response_200_charge_info_type_0 = cls(
            method=method,
            credits_charged=credits_charged,
        )


        profile_posts_live_fetch_response_200_charge_info_type_0.additional_properties = d
        return profile_posts_live_fetch_response_200_charge_info_type_0

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
