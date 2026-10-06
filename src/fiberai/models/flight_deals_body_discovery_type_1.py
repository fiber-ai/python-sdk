from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.flight_deals_body_discovery_type_1_mode import FlightDealsBodyDiscoveryType1Mode
from ..models.flight_deals_body_discovery_type_1_travel_class_type_1 import (
    FlightDealsBodyDiscoveryType1TravelClassType1,
)
from ..models.flight_deals_body_discovery_type_1_travel_class_type_2_type_1 import (
    FlightDealsBodyDiscoveryType1TravelClassType2Type1,
)
from ..models.flight_deals_body_discovery_type_1_travel_class_type_3_type_1 import (
    FlightDealsBodyDiscoveryType1TravelClassType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_deals_body_discovery_type_1_airlines_type_0 import FlightDealsBodyDiscoveryType1AirlinesType0


T = TypeVar("T", bound="FlightDealsBodyDiscoveryType1")


@_attrs_define
class FlightDealsBodyDiscoveryType1:
    """
    Attributes:
        mode (FlightDealsBodyDiscoveryType1Mode):
        max_price (int | None | Unset): Maximum round-trip price in the requested currency. Omit for no cap.
        max_stops (int | None | Unset): Maximum number of stops allowed. 0 = nonstop only, 1 = one stop or fewer, 2 =
            two stops or fewer. Omit to allow any number of stops.
        travel_class (FlightDealsBodyDiscoveryType1TravelClassType1 | FlightDealsBodyDiscoveryType1TravelClassType2Type1
            | FlightDealsBodyDiscoveryType1TravelClassType3Type1 | None | Unset): Preferred cabin class. Omit to consider
            flights across all cabin classes.
        airlines (FlightDealsBodyDiscoveryType1AirlinesType0 | None | Unset): Filter by airline. By default all airlines
            are considered. If you pass 'include', only deals from those airlines are returned.
    """

    mode: FlightDealsBodyDiscoveryType1Mode
    max_price: int | None | Unset = UNSET
    max_stops: int | None | Unset = UNSET
    travel_class: (
        FlightDealsBodyDiscoveryType1TravelClassType1
        | FlightDealsBodyDiscoveryType1TravelClassType2Type1
        | FlightDealsBodyDiscoveryType1TravelClassType3Type1
        | None
        | Unset
    ) = UNSET
    airlines: FlightDealsBodyDiscoveryType1AirlinesType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_deals_body_discovery_type_1_airlines_type_0 import (
            FlightDealsBodyDiscoveryType1AirlinesType0,  # noqa: PLC0415
        )

        mode = self.mode.value

        max_price: int | None | Unset
        if isinstance(self.max_price, Unset):
            max_price = UNSET
        else:
            max_price = self.max_price

        max_stops: int | None | Unset
        if isinstance(self.max_stops, Unset):
            max_stops = UNSET
        else:
            max_stops = self.max_stops

        travel_class: None | str | Unset
        if isinstance(self.travel_class, Unset):
            travel_class = UNSET
        elif isinstance(self.travel_class, FlightDealsBodyDiscoveryType1TravelClassType1):
            travel_class = self.travel_class.value
        elif isinstance(self.travel_class, FlightDealsBodyDiscoveryType1TravelClassType2Type1):
            travel_class = self.travel_class.value
        elif isinstance(self.travel_class, FlightDealsBodyDiscoveryType1TravelClassType3Type1):
            travel_class = self.travel_class.value
        else:
            travel_class = self.travel_class

        airlines: dict[str, Any] | None | Unset
        if isinstance(self.airlines, Unset):
            airlines = UNSET
        elif isinstance(self.airlines, FlightDealsBodyDiscoveryType1AirlinesType0):
            airlines = self.airlines.to_dict()
        else:
            airlines = self.airlines

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if max_stops is not UNSET:
            field_dict["maxStops"] = max_stops
        if travel_class is not UNSET:
            field_dict["travelClass"] = travel_class
        if airlines is not UNSET:
            field_dict["airlines"] = airlines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_deals_body_discovery_type_1_airlines_type_0 import (
            FlightDealsBodyDiscoveryType1AirlinesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        mode = FlightDealsBodyDiscoveryType1Mode(d.pop("mode"))

        def _parse_max_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_price = _parse_max_price(d.pop("maxPrice", UNSET))

        def _parse_max_stops(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_stops = _parse_max_stops(d.pop("maxStops", UNSET))

        def _parse_travel_class(
            data: object,
        ) -> (
            FlightDealsBodyDiscoveryType1TravelClassType1
            | FlightDealsBodyDiscoveryType1TravelClassType2Type1
            | FlightDealsBodyDiscoveryType1TravelClassType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                travel_class_type_1 = FlightDealsBodyDiscoveryType1TravelClassType1(data)

                return travel_class_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                travel_class_type_2_type_1 = FlightDealsBodyDiscoveryType1TravelClassType2Type1(data)

                return travel_class_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                travel_class_type_3_type_1 = FlightDealsBodyDiscoveryType1TravelClassType3Type1(data)

                return travel_class_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FlightDealsBodyDiscoveryType1TravelClassType1
                | FlightDealsBodyDiscoveryType1TravelClassType2Type1
                | FlightDealsBodyDiscoveryType1TravelClassType3Type1
                | None
                | Unset,
                data,
            )

        travel_class = _parse_travel_class(d.pop("travelClass", UNSET))

        def _parse_airlines(data: object) -> FlightDealsBodyDiscoveryType1AirlinesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airlines_type_0 = FlightDealsBodyDiscoveryType1AirlinesType0.from_dict(data)

                return airlines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightDealsBodyDiscoveryType1AirlinesType0 | None | Unset, data)

        airlines = _parse_airlines(d.pop("airlines", UNSET))

        flight_deals_body_discovery_type_1 = cls(
            mode=mode,
            max_price=max_price,
            max_stops=max_stops,
            travel_class=travel_class,
            airlines=airlines,
        )

        return flight_deals_body_discovery_type_1
