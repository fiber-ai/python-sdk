from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_search_response_200_output_properties_item_nearby_places_item_transportations_item import (
        HotelSearchResponse200OutputPropertiesItemNearbyPlacesItemTransportationsItem,
    )


T = TypeVar("T", bound="HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem")


@_attrs_define
class HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem:
    """
    Attributes:
        transportations (list[HotelSearchResponse200OutputPropertiesItemNearbyPlacesItemTransportationsItem]):
            Transportation options to reach this place.
        name (None | str | Unset): Nearby place name.
    """

    transportations: list[HotelSearchResponse200OutputPropertiesItemNearbyPlacesItemTransportationsItem]
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transportations = []
        for transportations_item_data in self.transportations:
            transportations_item = transportations_item_data.to_dict()
            transportations.append(transportations_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transportations": transportations,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_search_response_200_output_properties_item_nearby_places_item_transportations_item import (
            HotelSearchResponse200OutputPropertiesItemNearbyPlacesItemTransportationsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        transportations = []
        _transportations = d.pop("transportations")
        for transportations_item_data in _transportations:
            transportations_item = (
                HotelSearchResponse200OutputPropertiesItemNearbyPlacesItemTransportationsItem.from_dict(
                    transportations_item_data
                )
            )

            transportations.append(transportations_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        hotel_search_response_200_output_properties_item_nearby_places_item = cls(
            transportations=transportations,
            name=name,
        )

        hotel_search_response_200_output_properties_item_nearby_places_item.additional_properties = d
        return hotel_search_response_200_output_properties_item_nearby_places_item

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
