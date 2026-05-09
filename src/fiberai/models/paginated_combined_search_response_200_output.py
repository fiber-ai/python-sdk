from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_response_200_output_companies_item import (
        PaginatedCombinedSearchResponse200OutputCompaniesItem,
    )
    from ..models.paginated_combined_search_response_200_output_profiles_item import (
        PaginatedCombinedSearchResponse200OutputProfilesItem,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchResponse200Output")


@_attrs_define
class PaginatedCombinedSearchResponse200Output:
    """
    Attributes:
        companies (list[PaginatedCombinedSearchResponse200OutputCompaniesItem]):
        profiles (list[PaginatedCombinedSearchResponse200OutputProfilesItem]):
        next_companies_cursor (None | str | Unset): Pass this as companiesCursor in a subsequent request to get the next
            page of companies. Null when there are no more companies to return.
        next_profiles_cursor (None | str | Unset): Pass this as profilesCursor in a subsequent request to get the next
            page of profiles. Null when there are no more profiles to return.
    """

    companies: list[PaginatedCombinedSearchResponse200OutputCompaniesItem]
    profiles: list[PaginatedCombinedSearchResponse200OutputProfilesItem]
    next_companies_cursor: None | str | Unset = UNSET
    next_profiles_cursor: None | str | Unset = UNSET
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

        next_companies_cursor: None | str | Unset
        if isinstance(self.next_companies_cursor, Unset):
            next_companies_cursor = UNSET
        else:
            next_companies_cursor = self.next_companies_cursor

        next_profiles_cursor: None | str | Unset
        if isinstance(self.next_profiles_cursor, Unset):
            next_profiles_cursor = UNSET
        else:
            next_profiles_cursor = self.next_profiles_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
                "profiles": profiles,
            }
        )
        if next_companies_cursor is not UNSET:
            field_dict["nextCompaniesCursor"] = next_companies_cursor
        if next_profiles_cursor is not UNSET:
            field_dict["nextProfilesCursor"] = next_profiles_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_response_200_output_companies_item import (
            PaginatedCombinedSearchResponse200OutputCompaniesItem,
        )
        from ..models.paginated_combined_search_response_200_output_profiles_item import (
            PaginatedCombinedSearchResponse200OutputProfilesItem,
        )

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = PaginatedCombinedSearchResponse200OutputCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = PaginatedCombinedSearchResponse200OutputProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        def _parse_next_companies_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_companies_cursor = _parse_next_companies_cursor(d.pop("nextCompaniesCursor", UNSET))

        def _parse_next_profiles_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_profiles_cursor = _parse_next_profiles_cursor(d.pop("nextProfilesCursor", UNSET))

        paginated_combined_search_response_200_output = cls(
            companies=companies,
            profiles=profiles,
            next_companies_cursor=next_companies_cursor,
            next_profiles_cursor=next_profiles_cursor,
        )

        paginated_combined_search_response_200_output.additional_properties = d
        return paginated_combined_search_response_200_output

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
