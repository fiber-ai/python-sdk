from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_company_rankings_response_200_output_list import ListCompanyRankingsResponse200OutputList

if TYPE_CHECKING:
    from ..models.list_company_rankings_response_200_output_companies_item import (
        ListCompanyRankingsResponse200OutputCompaniesItem,
    )


T = TypeVar("T", bound="ListCompanyRankingsResponse200Output")


@_attrs_define
class ListCompanyRankingsResponse200Output:
    """
    Attributes:
        list_ (ListCompanyRankingsResponse200OutputList):
        year (int): Edition year of the returned list.
        companies (list[ListCompanyRankingsResponse200OutputCompaniesItem]): Companies in rank order (rank 1 first).
    """

    list_: ListCompanyRankingsResponse200OutputList
    year: int
    companies: list[ListCompanyRankingsResponse200OutputCompaniesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_ = self.list_.value

        year = self.year

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list": list_,
                "year": year,
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_company_rankings_response_200_output_companies_item import (
            ListCompanyRankingsResponse200OutputCompaniesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        list_ = ListCompanyRankingsResponse200OutputList(d.pop("list"))

        year = d.pop("year")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = ListCompanyRankingsResponse200OutputCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        list_company_rankings_response_200_output = cls(
            list_=list_,
            year=year,
            companies=companies,
        )

        list_company_rankings_response_200_output.additional_properties = d
        return list_company_rankings_response_200_output

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
