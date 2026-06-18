from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSavedSearchRunStatusResponse200OutputRunCompaniesStats")


@_attrs_define
class GetSavedSearchRunStatusResponse200OutputRunCompaniesStats:
    """The companies stats. This includes the number of companies joined, departed, stayed, and returned so far.

    Attributes:
        num_companies_joined (float): The number of companies joined which means companies who appeared in the search
            results for the first time
        num_companies_departed (float): The number of companies departed which means companies who appeared in the
            search results previously and then disappeared in the latest search results
        num_companies_stayed (float): The number of companies stayed which means companies who appeared in the search
            results previously and then stayed in the latest search results
        num_companies_returned (float): The number of companies returned which means companies who appeared in the
            search results previously but departed and then appeared again in the latest search results
    """

    num_companies_joined: float
    num_companies_departed: float
    num_companies_stayed: float
    num_companies_returned: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_companies_joined = self.num_companies_joined

        num_companies_departed = self.num_companies_departed

        num_companies_stayed = self.num_companies_stayed

        num_companies_returned = self.num_companies_returned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numCompaniesJoined": num_companies_joined,
                "numCompaniesDeparted": num_companies_departed,
                "numCompaniesStayed": num_companies_stayed,
                "numCompaniesReturned": num_companies_returned,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_companies_joined = d.pop("numCompaniesJoined")

        num_companies_departed = d.pop("numCompaniesDeparted")

        num_companies_stayed = d.pop("numCompaniesStayed")

        num_companies_returned = d.pop("numCompaniesReturned")

        get_saved_search_run_status_response_200_output_run_companies_stats = cls(
            num_companies_joined=num_companies_joined,
            num_companies_departed=num_companies_departed,
            num_companies_stayed=num_companies_stayed,
            num_companies_returned=num_companies_returned,
        )

        get_saved_search_run_status_response_200_output_run_companies_stats.additional_properties = d
        return get_saved_search_run_status_response_200_output_run_companies_stats

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
