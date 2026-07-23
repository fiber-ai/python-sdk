from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_hotel_amenities_response_200_output_amenities_item import (
        GetHotelAmenitiesResponse200OutputAmenitiesItem,
    )


T = TypeVar("T", bound="GetHotelAmenitiesResponse200Output")


@_attrs_define
class GetHotelAmenitiesResponse200Output:
    """
    Attributes:
        amenities (list[GetHotelAmenitiesResponse200OutputAmenitiesItem]): All supported hotel amenity filter values.
    """

    amenities: list[GetHotelAmenitiesResponse200OutputAmenitiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amenities = []
        for amenities_item_data in self.amenities:
            amenities_item = amenities_item_data.to_dict()
            amenities.append(amenities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amenities": amenities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_hotel_amenities_response_200_output_amenities_item import (
            GetHotelAmenitiesResponse200OutputAmenitiesItem,
        )

        d = dict(src_dict)
        amenities = []
        _amenities = d.pop("amenities")
        for amenities_item_data in _amenities:
            amenities_item = GetHotelAmenitiesResponse200OutputAmenitiesItem.from_dict(amenities_item_data)

            amenities.append(amenities_item)

        get_hotel_amenities_response_200_output = cls(
            amenities=amenities,
        )

        get_hotel_amenities_response_200_output.additional_properties = d
        return get_hotel_amenities_response_200_output

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
