from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelSearchResponse200OutputSearchInformationType0")


@_attrs_define
class HotelSearchResponse200OutputSearchInformationType0:
    """Summary information about the search results.

    Attributes:
        total_result_count (int | None | Unset): Approximate total number of matching properties.
    """

    total_result_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_result_count: int | None | Unset
        if isinstance(self.total_result_count, Unset):
            total_result_count = UNSET
        else:
            total_result_count = self.total_result_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_result_count is not UNSET:
            field_dict["totalResultCount"] = total_result_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_total_result_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_result_count = _parse_total_result_count(d.pop("totalResultCount", UNSET))

        hotel_search_response_200_output_search_information_type_0 = cls(
            total_result_count=total_result_count,
        )

        hotel_search_response_200_output_search_information_type_0.additional_properties = d
        return hotel_search_response_200_output_search_information_type_0

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
