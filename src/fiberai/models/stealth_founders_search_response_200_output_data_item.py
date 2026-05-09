from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stealth_founders_search_response_200_output_data_item_profile import (
        StealthFoundersSearchResponse200OutputDataItemProfile,
    )
    from ..models.stealth_founders_search_response_200_output_data_item_stealth_career import (
        StealthFoundersSearchResponse200OutputDataItemStealthCareer,
    )


T = TypeVar("T", bound="StealthFoundersSearchResponse200OutputDataItem")


@_attrs_define
class StealthFoundersSearchResponse200OutputDataItem:
    """
    Attributes:
        profile (StealthFoundersSearchResponse200OutputDataItemProfile):
        stealth_career (StealthFoundersSearchResponse200OutputDataItemStealthCareer):
    """

    profile: StealthFoundersSearchResponse200OutputDataItemProfile
    stealth_career: StealthFoundersSearchResponse200OutputDataItemStealthCareer
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile.to_dict()

        stealth_career = self.stealth_career.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile": profile,
                "stealthCareer": stealth_career,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stealth_founders_search_response_200_output_data_item_profile import (
            StealthFoundersSearchResponse200OutputDataItemProfile,
        )
        from ..models.stealth_founders_search_response_200_output_data_item_stealth_career import (
            StealthFoundersSearchResponse200OutputDataItemStealthCareer,
        )

        d = dict(src_dict)
        profile = StealthFoundersSearchResponse200OutputDataItemProfile.from_dict(d.pop("profile"))

        stealth_career = StealthFoundersSearchResponse200OutputDataItemStealthCareer.from_dict(d.pop("stealthCareer"))

        stealth_founders_search_response_200_output_data_item = cls(
            profile=profile,
            stealth_career=stealth_career,
        )

        stealth_founders_search_response_200_output_data_item.additional_properties = d
        return stealth_founders_search_response_200_output_data_item

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
