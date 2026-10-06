from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GoogleMapsPlaceBody")


@_attrs_define
class GoogleMapsPlaceBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        place_id (str): Google Maps place ID (e.g. 'ChIJN1t_tDeuEmsRUsoyG83frY4'). Obtain it from the `placeId` of a
            result returned by the Google Maps search endpoint (`POST /v1/google-maps/search`).
    """

    api_key: str
    place_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        place_id = self.place_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "placeId": place_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        place_id = d.pop("placeId")

        google_maps_place_body = cls(
            api_key=api_key,
            place_id=place_id,
        )

        google_maps_place_body.additional_properties = d
        return google_maps_place_body

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
