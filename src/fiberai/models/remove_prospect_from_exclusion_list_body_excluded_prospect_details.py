from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoveProspectFromExclusionListBodyExcludedProspectDetails")


@_attrs_define
class RemoveProspectFromExclusionListBodyExcludedProspectDetails:
    """Details of the prospects to remove from the exclusion list

    Attributes:
        linkedin_urls (list[str]): LinkedIn URLs of the prospects to remove from the exclusion list
    """

    linkedin_urls: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_urls = self.linkedin_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrls": linkedin_urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_urls = cast(list[str], d.pop("linkedinUrls"))

        remove_prospect_from_exclusion_list_body_excluded_prospect_details = cls(
            linkedin_urls=linkedin_urls,
        )

        remove_prospect_from_exclusion_list_body_excluded_prospect_details.additional_properties = d
        return remove_prospect_from_exclusion_list_body_excluded_prospect_details

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
