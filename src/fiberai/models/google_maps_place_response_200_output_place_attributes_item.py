from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GoogleMapsPlaceResponse200OutputPlaceAttributesItem")


@_attrs_define
class GoogleMapsPlaceResponse200OutputPlaceAttributesItem:
    """
    Attributes:
        category (str): Attribute group name (e.g. 'Service options', 'Highlights', 'Accessibility').
        values (list[str]): Attribute values in this group (e.g. 'Dine-in', 'Delivery').
    """

    category: str
    values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        values = cast(list[str], d.pop("values"))

        google_maps_place_response_200_output_place_attributes_item = cls(
            category=category,
            values=values,
        )

        google_maps_place_response_200_output_place_attributes_item.additional_properties = d
        return google_maps_place_response_200_output_place_attributes_item

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
