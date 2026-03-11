from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemSimilarCompaniesType0Item")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemSimilarCompaniesType0Item:
    """
    Attributes:
        name (None | str | Unset):
        industries (list[str] | None | Unset):
        employee_count (float | None | Unset):
        revenue (float | None | Unset):
        logo_url (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    industries: list[str] | None | Unset = UNSET
    employee_count: float | None | Unset = UNSET
    revenue: float | None | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        industries: list[str] | None | Unset
        if isinstance(self.industries, Unset):
            industries = UNSET
        elif isinstance(self.industries, list):
            industries = self.industries

        else:
            industries = self.industries

        employee_count: float | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        revenue: float | None | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if industries is not UNSET:
            field_dict["industries"] = industries
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_industries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = cast(list[str], data)

                return industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        industries = _parse_industries(d.pop("industries", UNSET))

        def _parse_employee_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        def _parse_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        poll_combined_search_response_200_output_data_type_0_items_item_similar_companies_type_0_item = cls(
            name=name,
            industries=industries,
            employee_count=employee_count,
            revenue=revenue,
            logo_url=logo_url,
        )

        poll_combined_search_response_200_output_data_type_0_items_item_similar_companies_type_0_item.additional_properties = d
        return poll_combined_search_response_200_output_data_type_0_items_item_similar_companies_type_0_item

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
