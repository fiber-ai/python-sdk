from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FlightSearchBodyReturnTimeWindowType0DepartureType0")


@_attrs_define
class FlightSearchBodyReturnTimeWindowType0DepartureType0:
    """Restrict departure times to this hour range.

    Attributes:
        start_hour (int): Start of the hour range (inclusive), in 24-hour format.
        end_hour (int): End of the hour range (inclusive), in 24-hour format.
    """

    start_hour: int
    end_hour: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_hour = self.start_hour

        end_hour = self.end_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startHour": start_hour,
                "endHour": end_hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_hour = d.pop("startHour")

        end_hour = d.pop("endHour")

        flight_search_body_return_time_window_type_0_departure_type_0 = cls(
            start_hour=start_hour,
            end_hour=end_hour,
        )

        flight_search_body_return_time_window_type_0_departure_type_0.additional_properties = d
        return flight_search_body_return_time_window_type_0_departure_type_0

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
