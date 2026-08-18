from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTalentFlowResponse200OutputBreakdownsByCountryItem")


@_attrs_define
class GetTalentFlowResponse200OutputBreakdownsByCountryItem:
    """
    Attributes:
        country_code (str): ISO 3166-1 alpha-3 country code (e.g. 'USA', 'GBR', 'IND').
        country_name (str): Full English country name.
        count (int): Number of people in this country.
        percent (float): Percentage of total people (0-100).
    """

    country_code: str
    country_name: str
    count: int
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        country_name = self.country_name

        count = self.count

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryCode": country_code,
                "countryName": country_name,
                "count": count,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode")

        country_name = d.pop("countryName")

        count = d.pop("count")

        percent = d.pop("percent")

        get_talent_flow_response_200_output_breakdowns_by_country_item = cls(
            country_code=country_code,
            country_name=country_name,
            count=count,
            percent=percent,
        )

        get_talent_flow_response_200_output_breakdowns_by_country_item.additional_properties = d
        return get_talent_flow_response_200_output_breakdowns_by_country_item

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
