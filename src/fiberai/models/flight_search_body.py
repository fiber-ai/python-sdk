from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_search_body_sort_by_type_1 import FlightSearchBodySortByType1
from ..models.flight_search_body_sort_by_type_2_type_1 import FlightSearchBodySortByType2Type1
from ..models.flight_search_body_sort_by_type_3_type_1 import FlightSearchBodySortByType3Type1
from ..models.flight_search_body_travel_class_type_1 import FlightSearchBodyTravelClassType1
from ..models.flight_search_body_travel_class_type_2_type_1 import FlightSearchBodyTravelClassType2Type1
from ..models.flight_search_body_travel_class_type_3_type_1 import FlightSearchBodyTravelClassType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_body_airlines_type_0 import FlightSearchBodyAirlinesType0
    from ..models.flight_search_body_connecting_airports_type_0 import FlightSearchBodyConnectingAirportsType0
    from ..models.flight_search_body_layover_duration_type_0 import FlightSearchBodyLayoverDurationType0
    from ..models.flight_search_body_outbound_time_window_type_0 import FlightSearchBodyOutboundTimeWindowType0
    from ..models.flight_search_body_return_time_window_type_0 import FlightSearchBodyReturnTimeWindowType0
    from ..models.flight_search_body_trip_type_0 import FlightSearchBodyTripType0
    from ..models.flight_search_body_trip_type_1 import FlightSearchBodyTripType1
    from ..models.flight_search_body_trip_type_2 import FlightSearchBodyTripType2


T = TypeVar("T", bound="FlightSearchBody")


@_attrs_define
class FlightSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        trip (FlightSearchBodyTripType0 | FlightSearchBodyTripType1 | FlightSearchBodyTripType2): Trip configuration.
            The shape is determined by flightType — see each variant for its required fields.
        travel_class (FlightSearchBodyTravelClassType1 | FlightSearchBodyTravelClassType2Type1 |
            FlightSearchBodyTravelClassType3Type1 | None | Unset): Preferred cabin class. Omit to consider flights across
            all cabin classes.
        adults (int | Unset): Number of adult passengers (ages 12+). Default: 1.
        children (int | Unset): Number of child passengers (ages 2-11). Default: 0.
        infants_in_seat (int | Unset): Number of infants (under 2) with their own seat. Default: 0.
        infants_on_lap (int | Unset): Number of infants (under 2) on an adult's lap. Default: 0.
        max_stops (int | None | Unset): Maximum number of stops allowed. 0 = nonstop only, 1 = one stop or fewer, 2 =
            two stops or fewer. Omit to allow any number of stops.
        sort_by (FlightSearchBodySortByType1 | FlightSearchBodySortByType2Type1 | FlightSearchBodySortByType3Type1 |
            None | Unset): Sort criterion for results. 'top' ranks by overall value. 'price' sorts cheapest first.
            'departureTime' and 'arrivalTime' sort earliest first. 'duration' sorts shortest first. 'emissions' sorts lowest
            carbon first. Direction is always ascending and cannot be changed. Omit to sort by 'top'.
        airlines (FlightSearchBodyAirlinesType0 | None | Unset): Filter by airline. By default all airlines are
            considered. If you pass 'include', only flights from those airlines are returned. If you pass 'exclude', flights
            from those airlines are removed.
        min_carry_on_bags (int | None | Unset): Minimum carry-on bags the itinerary must include. Omit for no
            requirement.
        min_checked_bags (int | None | Unset): Minimum checked bags the itinerary must include. Omit for no requirement.
            Honored on a best-effort basis: not every itinerary exposes checked-bag inclusion.
        max_price (int | None | Unset): Maximum total itinerary price in whole currency units. You may want to set
            `currencyCode` as well so the price cap is in the currency you expect (default currency is USD). Omit for no
            price cap.
        outbound_time_window (FlightSearchBodyOutboundTimeWindowType0 | None | Unset): Time-of-day window for outbound
            flights. For multi-city trips this constrains the first segment. Both startHour and endHour must be provided
            together per sub-window.
        return_time_window (FlightSearchBodyReturnTimeWindowType0 | None | Unset): Time-of-day window for return flights
            (round-trip only). Both startHour and endHour must be provided together per sub-window.
        layover_duration (FlightSearchBodyLayoverDurationType0 | None | Unset): Constrain layover duration. Omit to
            allow any layover length.
        max_flight_duration_minutes (int | None | Unset): Maximum total flight duration in minutes. Omit for no limit.
        connecting_airports (FlightSearchBodyConnectingAirportsType0 | None | Unset): Filter by connecting airports. By
            default all connecting airports are allowed. We recommend not passing this unless you have a good reason — it
            significantly reduces the number of results returned.
        only_show_low_emission_flights (bool | Unset): When true, only return flights with lower-than-typical carbon
            emissions. When false (default), return all flights. Default: False.
        show_hidden (bool | Unset): When true, include itineraries that would normally be hidden (e.g. very late or
            undesirable schedules). Default: True.
        hide_separate_tickets (bool | Unset): When true, drop itineraries that combine separately-issued tickets (which
            carry higher disruption risk). Default: False.
        currency_code (str | Unset): ISO 4217 currency code for prices in the response (e.g. 'EUR', 'GBP', 'CAD'). Case-
            insensitive. Defaults to USD. Default: 'USD'.
        search_market_country_code (str | Unset): ISO 3166-1 alpha-3 country code that sets the search market (e.g.
            'GBR', 'BRA'). This affects regional pricing and flight availability — the same route may show different prices
            and options depending on the market. Case-insensitive. Default: 'USA'.
        language_code (str | Unset): Language for search results (airport names, airline names, labels). Pass a BCP-47
            language tag such as 'en', 'en-US', 'pt-BR', 'zh-CN', 'ja', 'ko', 'fr', 'de', 'es'. Default: 'en'.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as nextPageToken in the next
            request. Null if no more pages.
    """

    api_key: str
    trip: FlightSearchBodyTripType0 | FlightSearchBodyTripType1 | FlightSearchBodyTripType2
    travel_class: (
        FlightSearchBodyTravelClassType1
        | FlightSearchBodyTravelClassType2Type1
        | FlightSearchBodyTravelClassType3Type1
        | None
        | Unset
    ) = UNSET
    adults: int | Unset = 1
    children: int | Unset = 0
    infants_in_seat: int | Unset = 0
    infants_on_lap: int | Unset = 0
    max_stops: int | None | Unset = UNSET
    sort_by: (
        FlightSearchBodySortByType1 | FlightSearchBodySortByType2Type1 | FlightSearchBodySortByType3Type1 | None | Unset
    ) = UNSET
    airlines: FlightSearchBodyAirlinesType0 | None | Unset = UNSET
    min_carry_on_bags: int | None | Unset = UNSET
    min_checked_bags: int | None | Unset = UNSET
    max_price: int | None | Unset = UNSET
    outbound_time_window: FlightSearchBodyOutboundTimeWindowType0 | None | Unset = UNSET
    return_time_window: FlightSearchBodyReturnTimeWindowType0 | None | Unset = UNSET
    layover_duration: FlightSearchBodyLayoverDurationType0 | None | Unset = UNSET
    max_flight_duration_minutes: int | None | Unset = UNSET
    connecting_airports: FlightSearchBodyConnectingAirportsType0 | None | Unset = UNSET
    only_show_low_emission_flights: bool | Unset = False
    show_hidden: bool | Unset = True
    hide_separate_tickets: bool | Unset = False
    currency_code: str | Unset = "USD"
    search_market_country_code: str | Unset = "USA"
    language_code: str | Unset = "en"
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_body_airlines_type_0 import FlightSearchBodyAirlinesType0  # noqa: PLC0415
        from ..models.flight_search_body_connecting_airports_type_0 import (
            FlightSearchBodyConnectingAirportsType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_layover_duration_type_0 import (
            FlightSearchBodyLayoverDurationType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_outbound_time_window_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_return_time_window_type_0 import (
            FlightSearchBodyReturnTimeWindowType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_trip_type_0 import FlightSearchBodyTripType0  # noqa: PLC0415
        from ..models.flight_search_body_trip_type_1 import FlightSearchBodyTripType1  # noqa: PLC0415

        api_key = self.api_key

        trip: dict[str, Any]
        if isinstance(self.trip, FlightSearchBodyTripType0):
            trip = self.trip.to_dict()
        elif isinstance(self.trip, FlightSearchBodyTripType1):
            trip = self.trip.to_dict()
        else:
            trip = self.trip.to_dict()

        travel_class: None | str | Unset
        if isinstance(self.travel_class, Unset):
            travel_class = UNSET
        elif isinstance(self.travel_class, FlightSearchBodyTravelClassType1):
            travel_class = self.travel_class.value
        elif isinstance(self.travel_class, FlightSearchBodyTravelClassType2Type1):
            travel_class = self.travel_class.value
        elif isinstance(self.travel_class, FlightSearchBodyTravelClassType3Type1):
            travel_class = self.travel_class.value
        else:
            travel_class = self.travel_class

        adults = self.adults

        children = self.children

        infants_in_seat = self.infants_in_seat

        infants_on_lap = self.infants_on_lap

        max_stops: int | None | Unset
        if isinstance(self.max_stops, Unset):
            max_stops = UNSET
        else:
            max_stops = self.max_stops

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, FlightSearchBodySortByType1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, FlightSearchBodySortByType2Type1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, FlightSearchBodySortByType3Type1):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

        airlines: dict[str, Any] | None | Unset
        if isinstance(self.airlines, Unset):
            airlines = UNSET
        elif isinstance(self.airlines, FlightSearchBodyAirlinesType0):
            airlines = self.airlines.to_dict()
        else:
            airlines = self.airlines

        min_carry_on_bags: int | None | Unset
        if isinstance(self.min_carry_on_bags, Unset):
            min_carry_on_bags = UNSET
        else:
            min_carry_on_bags = self.min_carry_on_bags

        min_checked_bags: int | None | Unset
        if isinstance(self.min_checked_bags, Unset):
            min_checked_bags = UNSET
        else:
            min_checked_bags = self.min_checked_bags

        max_price: int | None | Unset
        if isinstance(self.max_price, Unset):
            max_price = UNSET
        else:
            max_price = self.max_price

        outbound_time_window: dict[str, Any] | None | Unset
        if isinstance(self.outbound_time_window, Unset):
            outbound_time_window = UNSET
        elif isinstance(self.outbound_time_window, FlightSearchBodyOutboundTimeWindowType0):
            outbound_time_window = self.outbound_time_window.to_dict()
        else:
            outbound_time_window = self.outbound_time_window

        return_time_window: dict[str, Any] | None | Unset
        if isinstance(self.return_time_window, Unset):
            return_time_window = UNSET
        elif isinstance(self.return_time_window, FlightSearchBodyReturnTimeWindowType0):
            return_time_window = self.return_time_window.to_dict()
        else:
            return_time_window = self.return_time_window

        layover_duration: dict[str, Any] | None | Unset
        if isinstance(self.layover_duration, Unset):
            layover_duration = UNSET
        elif isinstance(self.layover_duration, FlightSearchBodyLayoverDurationType0):
            layover_duration = self.layover_duration.to_dict()
        else:
            layover_duration = self.layover_duration

        max_flight_duration_minutes: int | None | Unset
        if isinstance(self.max_flight_duration_minutes, Unset):
            max_flight_duration_minutes = UNSET
        else:
            max_flight_duration_minutes = self.max_flight_duration_minutes

        connecting_airports: dict[str, Any] | None | Unset
        if isinstance(self.connecting_airports, Unset):
            connecting_airports = UNSET
        elif isinstance(self.connecting_airports, FlightSearchBodyConnectingAirportsType0):
            connecting_airports = self.connecting_airports.to_dict()
        else:
            connecting_airports = self.connecting_airports

        only_show_low_emission_flights = self.only_show_low_emission_flights

        show_hidden = self.show_hidden

        hide_separate_tickets = self.hide_separate_tickets

        currency_code = self.currency_code

        search_market_country_code = self.search_market_country_code

        language_code = self.language_code

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "trip": trip,
            }
        )
        if travel_class is not UNSET:
            field_dict["travelClass"] = travel_class
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if infants_in_seat is not UNSET:
            field_dict["infantsInSeat"] = infants_in_seat
        if infants_on_lap is not UNSET:
            field_dict["infantsOnLap"] = infants_on_lap
        if max_stops is not UNSET:
            field_dict["maxStops"] = max_stops
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if airlines is not UNSET:
            field_dict["airlines"] = airlines
        if min_carry_on_bags is not UNSET:
            field_dict["minCarryOnBags"] = min_carry_on_bags
        if min_checked_bags is not UNSET:
            field_dict["minCheckedBags"] = min_checked_bags
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if outbound_time_window is not UNSET:
            field_dict["outboundTimeWindow"] = outbound_time_window
        if return_time_window is not UNSET:
            field_dict["returnTimeWindow"] = return_time_window
        if layover_duration is not UNSET:
            field_dict["layoverDuration"] = layover_duration
        if max_flight_duration_minutes is not UNSET:
            field_dict["maxFlightDurationMinutes"] = max_flight_duration_minutes
        if connecting_airports is not UNSET:
            field_dict["connectingAirports"] = connecting_airports
        if only_show_low_emission_flights is not UNSET:
            field_dict["onlyShowLowEmissionFlights"] = only_show_low_emission_flights
        if show_hidden is not UNSET:
            field_dict["showHidden"] = show_hidden
        if hide_separate_tickets is not UNSET:
            field_dict["hideSeparateTickets"] = hide_separate_tickets
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if search_market_country_code is not UNSET:
            field_dict["searchMarketCountryCode"] = search_market_country_code
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_body_airlines_type_0 import FlightSearchBodyAirlinesType0  # noqa: PLC0415
        from ..models.flight_search_body_connecting_airports_type_0 import (
            FlightSearchBodyConnectingAirportsType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_layover_duration_type_0 import (
            FlightSearchBodyLayoverDurationType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_outbound_time_window_type_0 import (
            FlightSearchBodyOutboundTimeWindowType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_return_time_window_type_0 import (
            FlightSearchBodyReturnTimeWindowType0,  # noqa: PLC0415
        )
        from ..models.flight_search_body_trip_type_0 import FlightSearchBodyTripType0  # noqa: PLC0415
        from ..models.flight_search_body_trip_type_1 import FlightSearchBodyTripType1  # noqa: PLC0415
        from ..models.flight_search_body_trip_type_2 import FlightSearchBodyTripType2  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_trip(
            data: object,
        ) -> FlightSearchBodyTripType0 | FlightSearchBodyTripType1 | FlightSearchBodyTripType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trip_type_0 = FlightSearchBodyTripType0.from_dict(data)

                return trip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trip_type_1 = FlightSearchBodyTripType1.from_dict(data)

                return trip_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            trip_type_2 = FlightSearchBodyTripType2.from_dict(data)

            return trip_type_2

        trip = _parse_trip(d.pop("trip"))

        def _parse_travel_class(
            data: object,
        ) -> (
            FlightSearchBodyTravelClassType1
            | FlightSearchBodyTravelClassType2Type1
            | FlightSearchBodyTravelClassType3Type1
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
                travel_class_type_1 = FlightSearchBodyTravelClassType1(data)

                return travel_class_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                travel_class_type_2_type_1 = FlightSearchBodyTravelClassType2Type1(data)

                return travel_class_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                travel_class_type_3_type_1 = FlightSearchBodyTravelClassType3Type1(data)

                return travel_class_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FlightSearchBodyTravelClassType1
                | FlightSearchBodyTravelClassType2Type1
                | FlightSearchBodyTravelClassType3Type1
                | None
                | Unset,
                data,
            )

        travel_class = _parse_travel_class(d.pop("travelClass", UNSET))

        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        infants_in_seat = d.pop("infantsInSeat", UNSET)

        infants_on_lap = d.pop("infantsOnLap", UNSET)

        def _parse_max_stops(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_stops = _parse_max_stops(d.pop("maxStops", UNSET))

        def _parse_sort_by(
            data: object,
        ) -> (
            FlightSearchBodySortByType1
            | FlightSearchBodySortByType2Type1
            | FlightSearchBodySortByType3Type1
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
                sort_by_type_1 = FlightSearchBodySortByType1(data)

                return sort_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_2_type_1 = FlightSearchBodySortByType2Type1(data)

                return sort_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_3_type_1 = FlightSearchBodySortByType3Type1(data)

                return sort_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FlightSearchBodySortByType1
                | FlightSearchBodySortByType2Type1
                | FlightSearchBodySortByType3Type1
                | None
                | Unset,
                data,
            )

        sort_by = _parse_sort_by(d.pop("sortBy", UNSET))

        def _parse_airlines(data: object) -> FlightSearchBodyAirlinesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airlines_type_0 = FlightSearchBodyAirlinesType0.from_dict(data)

                return airlines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyAirlinesType0 | None | Unset, data)

        airlines = _parse_airlines(d.pop("airlines", UNSET))

        def _parse_min_carry_on_bags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_carry_on_bags = _parse_min_carry_on_bags(d.pop("minCarryOnBags", UNSET))

        def _parse_min_checked_bags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_checked_bags = _parse_min_checked_bags(d.pop("minCheckedBags", UNSET))

        def _parse_max_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_price = _parse_max_price(d.pop("maxPrice", UNSET))

        def _parse_outbound_time_window(data: object) -> FlightSearchBodyOutboundTimeWindowType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outbound_time_window_type_0 = FlightSearchBodyOutboundTimeWindowType0.from_dict(data)

                return outbound_time_window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyOutboundTimeWindowType0 | None | Unset, data)

        outbound_time_window = _parse_outbound_time_window(d.pop("outboundTimeWindow", UNSET))

        def _parse_return_time_window(data: object) -> FlightSearchBodyReturnTimeWindowType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                return_time_window_type_0 = FlightSearchBodyReturnTimeWindowType0.from_dict(data)

                return return_time_window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyReturnTimeWindowType0 | None | Unset, data)

        return_time_window = _parse_return_time_window(d.pop("returnTimeWindow", UNSET))

        def _parse_layover_duration(data: object) -> FlightSearchBodyLayoverDurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                layover_duration_type_0 = FlightSearchBodyLayoverDurationType0.from_dict(data)

                return layover_duration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyLayoverDurationType0 | None | Unset, data)

        layover_duration = _parse_layover_duration(d.pop("layoverDuration", UNSET))

        def _parse_max_flight_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_flight_duration_minutes = _parse_max_flight_duration_minutes(d.pop("maxFlightDurationMinutes", UNSET))

        def _parse_connecting_airports(data: object) -> FlightSearchBodyConnectingAirportsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connecting_airports_type_0 = FlightSearchBodyConnectingAirportsType0.from_dict(data)

                return connecting_airports_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchBodyConnectingAirportsType0 | None | Unset, data)

        connecting_airports = _parse_connecting_airports(d.pop("connectingAirports", UNSET))

        only_show_low_emission_flights = d.pop("onlyShowLowEmissionFlights", UNSET)

        show_hidden = d.pop("showHidden", UNSET)

        hide_separate_tickets = d.pop("hideSeparateTickets", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        search_market_country_code = d.pop("searchMarketCountryCode", UNSET)

        language_code = d.pop("languageCode", UNSET)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        flight_search_body = cls(
            api_key=api_key,
            trip=trip,
            travel_class=travel_class,
            adults=adults,
            children=children,
            infants_in_seat=infants_in_seat,
            infants_on_lap=infants_on_lap,
            max_stops=max_stops,
            sort_by=sort_by,
            airlines=airlines,
            min_carry_on_bags=min_carry_on_bags,
            min_checked_bags=min_checked_bags,
            max_price=max_price,
            outbound_time_window=outbound_time_window,
            return_time_window=return_time_window,
            layover_duration=layover_duration,
            max_flight_duration_minutes=max_flight_duration_minutes,
            connecting_airports=connecting_airports,
            only_show_low_emission_flights=only_show_low_emission_flights,
            show_hidden=show_hidden,
            hide_separate_tickets=hide_separate_tickets,
            currency_code=currency_code,
            search_market_country_code=search_market_country_code,
            language_code=language_code,
            next_page_token=next_page_token,
        )

        flight_search_body.additional_properties = d
        return flight_search_body

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
