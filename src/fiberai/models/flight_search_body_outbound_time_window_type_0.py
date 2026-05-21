from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_body_outbound_time_window_type_0_arrival_type_0 import (
        FlightSearchBodyOutboundTimeWindowType0ArrivalType0,
    )
    from ..models.flight_search_body_outbound_time_window_type_0_departure_type_0 import (
        FlightSearchBodyOutboundTimeWindowType0DepartureType0,
    )


T = TypeVar("T", bound="FlightSearchBodyOutboundTimeWindowType0")


@_attrs_define
class FlightSearchBodyOutboundTimeWindowType0:
    """Time-of-day window for outbound flights. For multi-city trips this constrains the first segment. Both startHour and
    endHour must be provided together per sub-window.

        Attributes:
            departure (FlightSearchBodyOutboundTimeWindowType0DepartureType0 | None | Unset): Restrict departure times to
                this hour range.
            arrival (FlightSearchBodyOutboundTimeWindowType0ArrivalType0 | None | Unset): Restrict arrival times to this
                hour range.
    """

    departure: FlightSearchBodyOutboundTimeWindowType0DepartureType0 | None | Unset = UNSET
    arrival: FlightSearchBodyOutboundTimeWindowType0ArrivalType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_body_outbound_time_window_type_0_arrival_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0ArrivalType0,
        )
        from ..models.flight_search_body_outbound_time_window_type_0_departure_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0DepartureType0,
        )

        departure: dict[str, Any] | None | Unset
        if isinstance(self.departure, Unset):
            departure = UNSET
        elif isinstance(self.departure, FlightSearchBodyOutboundTimeWindowType0DepartureType0):
            departure = self.departure.to_dict()
        else:
            departure = self.departure

        arrival: dict[str, Any] | None | Unset
        if isinstance(self.arrival, Unset):
            arrival = UNSET
        elif isinstance(self.arrival, FlightSearchBodyOutboundTimeWindowType0ArrivalType0):
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
        from ..models.flight_search_body_outbound_time_window_type_0_arrival_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0ArrivalType0,
        )
        from ..models.flight_search_body_outbound_time_window_type_0_departure_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0DepartureType0,
        )

        d = dict(src_dict)

        def _parse_departure(data: object) -> FlightSearchBodyOutboundTimeWindowType0DepartureType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                departure_type_0 = FlightSearchBodyOutboundTimeWindowType0DepartureType0.from_dict(data)

                return departure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyOutboundTimeWindowType0DepartureType0 | None | Unset, data)

        departure = _parse_departure(d.pop("departure", UNSET))

        def _parse_arrival(data: object) -> FlightSearchBodyOutboundTimeWindowType0ArrivalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                arrival_type_0 = FlightSearchBodyOutboundTimeWindowType0ArrivalType0.from_dict(data)

                return arrival_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyOutboundTimeWindowType0ArrivalType0 | None | Unset, data)

        arrival = _parse_arrival(d.pop("arrival", UNSET))

        flight_search_body_outbound_time_window_type_0 = cls(
            departure=departure,
            arrival=arrival,
        )

        flight_search_body_outbound_time_window_type_0.additional_properties = d
        return flight_search_body_outbound_time_window_type_0

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
