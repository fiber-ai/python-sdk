from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_current_companies_in_saved_search_response_200_output_companies_item import (
        GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem,
    )


T = TypeVar("T", bound="GetCurrentCompaniesInSavedSearchResponse200Output")


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200Output:
    """
    Attributes:
        companies (list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem]): The companies that currently
            match the saved search, as of the latest run.
        next_cursor (None | str | Unset): The next cursor
        last_run_completed_at (None | str | Unset): The date and time the last run completed
    """

    companies: list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem]
    next_cursor: None | str | Unset = UNSET
    last_run_completed_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        last_run_completed_at: None | str | Unset
        if isinstance(self.last_run_completed_at, Unset):
            last_run_completed_at = UNSET
        else:
            last_run_completed_at = self.last_run_completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if last_run_completed_at is not UNSET:
            field_dict["lastRunCompletedAt"] = last_run_completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item import (
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem,
        )

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem.from_dict(
                companies_item_data
            )

            companies.append(companies_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        def _parse_last_run_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_run_completed_at = _parse_last_run_completed_at(d.pop("lastRunCompletedAt", UNSET))

        get_current_companies_in_saved_search_response_200_output = cls(
            companies=companies,
            next_cursor=next_cursor,
            last_run_completed_at=last_run_completed_at,
        )

        get_current_companies_in_saved_search_response_200_output.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output

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
