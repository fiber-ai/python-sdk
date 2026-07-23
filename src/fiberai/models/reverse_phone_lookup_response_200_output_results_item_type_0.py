from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reverse_phone_lookup_response_200_output_results_item_type_0_type import (
    ReversePhoneLookupResponse200OutputResultsItemType0Type,
)

if TYPE_CHECKING:
    from ..models.reverse_phone_lookup_response_200_output_results_item_type_0_profile import (
        ReversePhoneLookupResponse200OutputResultsItemType0Profile,
    )


T = TypeVar("T", bound="ReversePhoneLookupResponse200OutputResultsItemType0")


@_attrs_define
class ReversePhoneLookupResponse200OutputResultsItemType0:
    """
    Attributes:
        type_ (ReversePhoneLookupResponse200OutputResultsItemType0Type):
        profile (ReversePhoneLookupResponse200OutputResultsItemType0Profile):
    """

    type_: ReversePhoneLookupResponse200OutputResultsItemType0Type
    profile: ReversePhoneLookupResponse200OutputResultsItemType0Profile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "profile": profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reverse_phone_lookup_response_200_output_results_item_type_0_profile import (
            ReversePhoneLookupResponse200OutputResultsItemType0Profile,
        )

        d = dict(src_dict)
        type_ = ReversePhoneLookupResponse200OutputResultsItemType0Type(d.pop("type"))

        profile = ReversePhoneLookupResponse200OutputResultsItemType0Profile.from_dict(d.pop("profile"))

        reverse_phone_lookup_response_200_output_results_item_type_0 = cls(
            type_=type_,
            profile=profile,
        )

        reverse_phone_lookup_response_200_output_results_item_type_0.additional_properties = d
        return reverse_phone_lookup_response_200_output_results_item_type_0

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
