from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_local_business_search_body_data_item_type_0_source import (
    StartLocalBusinessSearchBodyDataItemType0Source,
)

if TYPE_CHECKING:
    from ..models.start_local_business_search_body_data_item_type_0_companies_item import (
        StartLocalBusinessSearchBodyDataItemType0CompaniesItem,
    )


T = TypeVar("T", bound="StartLocalBusinessSearchBodyDataItemType0")


@_attrs_define
class StartLocalBusinessSearchBodyDataItemType0:
    """
    Attributes:
        source (StartLocalBusinessSearchBodyDataItemType0Source):
        companies (list[StartLocalBusinessSearchBodyDataItemType0CompaniesItem]): Companies to search for
    """

    source: StartLocalBusinessSearchBodyDataItemType0Source
    companies: list[StartLocalBusinessSearchBodyDataItemType0CompaniesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_local_business_search_body_data_item_type_0_companies_item import (
            StartLocalBusinessSearchBodyDataItemType0CompaniesItem,
        )

        d = dict(src_dict)
        source = StartLocalBusinessSearchBodyDataItemType0Source(d.pop("source"))

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = StartLocalBusinessSearchBodyDataItemType0CompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        start_local_business_search_body_data_item_type_0 = cls(
            source=source,
            companies=companies,
        )

        start_local_business_search_body_data_item_type_0.additional_properties = d
        return start_local_business_search_body_data_item_type_0

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
