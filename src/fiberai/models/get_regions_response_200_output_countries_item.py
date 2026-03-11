from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetRegionsResponse200OutputCountriesItem")


@_attrs_define
class GetRegionsResponse200OutputCountriesItem:
    """
    Attributes:
        name (str): The common name of the country
        api_code (str): The code you need to use to filter by this country in our API
        iso_code_alpha_3 (str): ISO 3166-1 alpha-3 country code, like 'USA' or 'CAN'
        iso_code_alpha_2 (str): ISO 3166-1 alpha-2 country code, like 'US' or 'CA'
        flag (str): Unicode flag emoji for the country
    """

    name: str
    api_code: str
    iso_code_alpha_3: str
    iso_code_alpha_2: str
    flag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        api_code = self.api_code

        iso_code_alpha_3 = self.iso_code_alpha_3

        iso_code_alpha_2 = self.iso_code_alpha_2

        flag = self.flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "apiCode": api_code,
                "isoCodeAlpha3": iso_code_alpha_3,
                "isoCodeAlpha2": iso_code_alpha_2,
                "flag": flag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        api_code = d.pop("apiCode")

        iso_code_alpha_3 = d.pop("isoCodeAlpha3")

        iso_code_alpha_2 = d.pop("isoCodeAlpha2")

        flag = d.pop("flag")

        get_regions_response_200_output_countries_item = cls(
            name=name,
            api_code=api_code,
            iso_code_alpha_3=iso_code_alpha_3,
            iso_code_alpha_2=iso_code_alpha_2,
            flag=flag,
        )

        get_regions_response_200_output_countries_item.additional_properties = d
        return get_regions_response_200_output_countries_item

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
