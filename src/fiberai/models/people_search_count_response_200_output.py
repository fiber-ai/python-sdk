from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PeopleSearchCountResponse200Output")


@_attrs_define
class PeopleSearchCountResponse200Output:
    """
    Attributes:
        total_profiles_found (int): Total number of profiles matching the search criteria including exclusion lists
    """

    total_profiles_found: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_profiles_found = self.total_profiles_found

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalProfilesFound": total_profiles_found,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_profiles_found = d.pop("totalProfilesFound")

        people_search_count_response_200_output = cls(
            total_profiles_found=total_profiles_found,
        )

        people_search_count_response_200_output.additional_properties = d
        return people_search_count_response_200_output

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
