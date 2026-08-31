from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_hotel_property_types_response_200_output_property_types_item import (
        GetHotelPropertyTypesResponse200OutputPropertyTypesItem,
    )


T = TypeVar("T", bound="GetHotelPropertyTypesResponse200Output")


@_attrs_define
class GetHotelPropertyTypesResponse200Output:
    """
    Attributes:
        property_types (list[GetHotelPropertyTypesResponse200OutputPropertyTypesItem]): All supported hotel property
            type filter values.
    """

    property_types: list[GetHotelPropertyTypesResponse200OutputPropertyTypesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_types = []
        for property_types_item_data in self.property_types:
            property_types_item = property_types_item_data.to_dict()
            property_types.append(property_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyTypes": property_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_hotel_property_types_response_200_output_property_types_item import (
            GetHotelPropertyTypesResponse200OutputPropertyTypesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        property_types = []
        _property_types = d.pop("propertyTypes")
        for property_types_item_data in _property_types:
            property_types_item = GetHotelPropertyTypesResponse200OutputPropertyTypesItem.from_dict(
                property_types_item_data
            )

            property_types.append(property_types_item)

        get_hotel_property_types_response_200_output = cls(
            property_types=property_types,
        )

        get_hotel_property_types_response_200_output.additional_properties = d
        return get_hotel_property_types_response_200_output

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
