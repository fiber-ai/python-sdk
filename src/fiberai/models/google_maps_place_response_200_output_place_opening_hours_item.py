from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_place_response_200_output_place_opening_hours_item_day_of_week import (
    GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItemDayOfWeek,
)

T = TypeVar("T", bound="GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem")


@_attrs_define
class GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem:
    """
    Attributes:
        day_of_week (GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItemDayOfWeek): Day of the week.
        hours (str): Opening hours for the day, as displayed on the Google Maps page for the place (e.g. '12–2:30 PM,
            5–9 PM').
    """

    day_of_week: GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItemDayOfWeek
    hours: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_of_week = self.day_of_week.value

        hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dayOfWeek": day_of_week,
                "hours": hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day_of_week = GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItemDayOfWeek(d.pop("dayOfWeek"))

        hours = d.pop("hours")

        google_maps_place_response_200_output_place_opening_hours_item = cls(
            day_of_week=day_of_week,
            hours=hours,
        )

        google_maps_place_response_200_output_place_opening_hours_item.additional_properties = d
        return google_maps_place_response_200_output_place_opening_hours_item

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
