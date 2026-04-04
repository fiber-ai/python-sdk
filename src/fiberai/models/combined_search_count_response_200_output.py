from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CombinedSearchCountResponse200Output")


@_attrs_define
class CombinedSearchCountResponse200Output:
    """
    Attributes:
        num_companies (float):
        num_profiles (float):
    """

    num_companies: float
    num_profiles: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_companies = self.num_companies

        num_profiles = self.num_profiles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numCompanies": num_companies,
                "numProfiles": num_profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_companies = d.pop("numCompanies")

        num_profiles = d.pop("numProfiles")

        combined_search_count_response_200_output = cls(
            num_companies=num_companies,
            num_profiles=num_profiles,
        )

        combined_search_count_response_200_output.additional_properties = d
        return combined_search_count_response_200_output

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
