from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAcceleratorsResponse200OutputItemYearsType0Item")


@_attrs_define
class GetAcceleratorsResponse200OutputItemYearsType0Item:
    """
    Attributes:
        year (int): The year the companies participated in the accelerator
        num_companies (int): Number of companies in this year for this accelerator
    """

    year: int
    num_companies: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        num_companies = self.num_companies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "numCompanies": num_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        num_companies = d.pop("numCompanies")

        get_accelerators_response_200_output_item_years_type_0_item = cls(
            year=year,
            num_companies=num_companies,
        )

        get_accelerators_response_200_output_item_years_type_0_item.additional_properties = d
        return get_accelerators_response_200_output_item_years_type_0_item

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
