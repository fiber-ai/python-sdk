from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_body_return_time_window_type_0_arrival_type_0 import (
        FlightSearchBodyReturnTimeWindowType0ArrivalType0,
    )
    from ..models.flight_search_body_return_time_window_type_0_departure_type_0 import (
        FlightSearchBodyReturnTimeWindowType0DepartureType0,
    )


T = TypeVar("T", bound="FlightSearchBodyReturnTimeWindowType0")


@_attrs_define
class FlightSearchBodyReturnTimeWindowType0:
    """Time-of-day window for return flights (round-trip only). Both startHour and endHour must be provided together per
    sub-window.

        Attributes:
            departure (FlightSearchBodyReturnTimeWindowType0DepartureType0 | None | Unset): Restrict departure times to this
                hour range.
            arrival (FlightSearchBodyReturnTimeWindowType0ArrivalType0 | None | Unset): Restrict arrival times to this hour
                range.
    """

    departure: FlightSearchBodyReturnTimeWindowType0DepartureType0 | None | Unset = UNSET
    arrival: FlightSearchBodyReturnTimeWindowType0ArrivalType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_body_return_time_window_type_0_arrival_type_0 import (
            FlightSearchBodyReturnTimeWindowType0ArrivalType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_return_time_window_type_0_departure_type_0 import (
            FlightSearchBodyReturnTimeWindowType0DepartureType0,  # noqa: PLC0415
        )

        departure: dict[str, Any] | None | Unset
        if isinstance(self.departure, Unset):
            departure = UNSET
        elif isinstance(self.departure, FlightSearchBodyReturnTimeWindowType0DepartureType0):
            departure = self.departure.to_dict()
        else:
            departure = self.departure

        arrival: dict[str, Any] | None | Unset
        if isinstance(self.arrival, Unset):
            arrival = UNSET
        elif isinstance(self.arrival, FlightSearchBodyReturnTimeWindowType0ArrivalType0):
            arrival = self.arrival.to_dict()
        else:
            arrival = self.arrival

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if departure is not UNSET:
            field_dict["departure"] = departure
        if arrival is not UNSET:
            field_dict["arrival"] = arrival

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_body_return_time_window_type_0_arrival_type_0 import (
            FlightSearchBodyReturnTimeWindowType0ArrivalType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_return_time_window_type_0_departure_type_0 import (
            FlightSearchBodyReturnTimeWindowType0DepartureType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_departure(data: object) -> FlightSearchBodyReturnTimeWindowType0DepartureType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                departure_type_0 = FlightSearchBodyReturnTimeWindowType0DepartureType0.from_dict(data)

                return departure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyReturnTimeWindowType0DepartureType0 | None | Unset, data)

        departure = _parse_departure(d.pop("departure", UNSET))

        def _parse_arrival(data: object) -> FlightSearchBodyReturnTimeWindowType0ArrivalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                arrival_type_0 = FlightSearchBodyReturnTimeWindowType0ArrivalType0.from_dict(data)

                return arrival_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyReturnTimeWindowType0ArrivalType0 | None | Unset, data)

        arrival = _parse_arrival(d.pop("arrival", UNSET))

        flight_search_body_return_time_window_type_0 = cls(
            departure=departure,
            arrival=arrival,
        )

        flight_search_body_return_time_window_type_0.additional_properties = d
        return flight_search_body_return_time_window_type_0

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
