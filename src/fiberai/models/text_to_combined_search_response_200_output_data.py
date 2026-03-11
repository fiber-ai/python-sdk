from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_data_companies_item import (
        TextToCombinedSearchResponse200OutputDataCompaniesItem,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItem,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputData")


@_attrs_define
class TextToCombinedSearchResponse200OutputData:
    """
    Attributes:
        companies (list[TextToCombinedSearchResponse200OutputDataCompaniesItem]):
        profiles (list[TextToCombinedSearchResponse200OutputDataProfilesItem]):
    """

    companies: list[TextToCombinedSearchResponse200OutputDataCompaniesItem]
    profiles: list[TextToCombinedSearchResponse200OutputDataProfilesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
                "profiles": profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_companies_item import (
            TextToCombinedSearchResponse200OutputDataCompaniesItem,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItem,
        )

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = TextToCombinedSearchResponse200OutputDataCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = TextToCombinedSearchResponse200OutputDataProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        text_to_combined_search_response_200_output_data = cls(
            companies=companies,
            profiles=profiles,
        )

        text_to_combined_search_response_200_output_data.additional_properties = d
        return text_to_combined_search_response_200_output_data

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
