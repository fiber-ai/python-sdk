from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_excluded_companies_for_exclusion_list_response_200_output_companies_item import (
        GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem,
    )


T = TypeVar("T", bound="GetExcludedCompaniesForExclusionListResponse200Output")


@_attrs_define
class GetExcludedCompaniesForExclusionListResponse200Output:
    """
    Attributes:
        companies (list[GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem]): List of excluded companies
        next_cursor (None | str): Cursor for the next page of results
        has_more (bool): Whether there are more results available
    """

    companies: list[GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem]
    next_cursor: None | str
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
                "nextCursor": next_cursor,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_excluded_companies_for_exclusion_list_response_200_output_companies_item import (
            GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem,
        )

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem.from_dict(
                companies_item_data
            )

            companies.append(companies_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        has_more = d.pop("hasMore")

        get_excluded_companies_for_exclusion_list_response_200_output = cls(
            companies=companies,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        get_excluded_companies_for_exclusion_list_response_200_output.additional_properties = d
        return get_excluded_companies_for_exclusion_list_response_200_output

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
