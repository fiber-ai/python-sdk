from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_subdivisions_response_200_output_subdivisions_item import (
        GetSubdivisionsResponse200OutputSubdivisionsItem,
    )


T = TypeVar("T", bound="GetSubdivisionsResponse200Output")


@_attrs_define
class GetSubdivisionsResponse200Output:
    """
    Attributes:
        country_code (str): The alpha-3 country code queried
        subdivisions (list[GetSubdivisionsResponse200OutputSubdivisionsItem]):
    """

    country_code: str
    subdivisions: list[GetSubdivisionsResponse200OutputSubdivisionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        subdivisions = []
        for subdivisions_item_data in self.subdivisions:
            subdivisions_item = subdivisions_item_data.to_dict()
            subdivisions.append(subdivisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryCode": country_code,
                "subdivisions": subdivisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subdivisions_response_200_output_subdivisions_item import (
            GetSubdivisionsResponse200OutputSubdivisionsItem,
        )

        d = dict(src_dict)
        country_code = d.pop("countryCode")

        subdivisions = []
        _subdivisions = d.pop("subdivisions")
        for subdivisions_item_data in _subdivisions:
            subdivisions_item = GetSubdivisionsResponse200OutputSubdivisionsItem.from_dict(subdivisions_item_data)

            subdivisions.append(subdivisions_item)

        get_subdivisions_response_200_output = cls(
            country_code=country_code,
            subdivisions=subdivisions,
        )

        get_subdivisions_response_200_output.additional_properties = d
        return get_subdivisions_response_200_output

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
