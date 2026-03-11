from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_naics_codes_response_200_output_naics_codes_item import (
        GetNaicsCodesResponse200OutputNaicsCodesItem,
    )


T = TypeVar("T", bound="GetNaicsCodesResponse200Output")


@_attrs_define
class GetNaicsCodesResponse200Output:
    """
    Attributes:
        naics_codes (list[GetNaicsCodesResponse200OutputNaicsCodesItem]): List of all NAICS codes with their titles.
            This is the 2017 version of the NAICS codes.
    """

    naics_codes: list[GetNaicsCodesResponse200OutputNaicsCodesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        naics_codes = []
        for naics_codes_item_data in self.naics_codes:
            naics_codes_item = naics_codes_item_data.to_dict()
            naics_codes.append(naics_codes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "naicsCodes": naics_codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_naics_codes_response_200_output_naics_codes_item import (
            GetNaicsCodesResponse200OutputNaicsCodesItem,
        )

        d = dict(src_dict)
        naics_codes = []
        _naics_codes = d.pop("naicsCodes")
        for naics_codes_item_data in _naics_codes:
            naics_codes_item = GetNaicsCodesResponse200OutputNaicsCodesItem.from_dict(naics_codes_item_data)

            naics_codes.append(naics_codes_item)

        get_naics_codes_response_200_output = cls(
            naics_codes=naics_codes,
        )

        get_naics_codes_response_200_output.additional_properties = d
        return get_naics_codes_response_200_output

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
