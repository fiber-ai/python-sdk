from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_response_200_output_airports_item import FlightSearchResponse200OutputAirportsItem
    from ..models.flight_search_response_200_output_best_flights_item import (
        FlightSearchResponse200OutputBestFlightsItem,
    )
    from ..models.flight_search_response_200_output_other_flights_item import (
        FlightSearchResponse200OutputOtherFlightsItem,
    )
    from ..models.flight_search_response_200_output_price_insights_type_0 import (
        FlightSearchResponse200OutputPriceInsightsType0,
    )


T = TypeVar("T", bound="FlightSearchResponse200Output")


@_attrs_define
class FlightSearchResponse200Output:
    """
    Attributes:
        best_flights (list[FlightSearchResponse200OutputBestFlightsItem]): Best flight itineraries for this query.
        other_flights (list[FlightSearchResponse200OutputOtherFlightsItem]): Additional flight itineraries for this
            query.
        airports (list[FlightSearchResponse200OutputAirportsItem]): Airports recognized for departure and arrival in
            this query.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
        currency_code (None | str | Unset): ISO 4217 currency code for prices in this response (e.g. 'USD', 'EUR',
            'GBP').
        price_insights (FlightSearchResponse200OutputPriceInsightsType0 | None | Unset): Price-insight summary for this
            route query.
    """

    best_flights: list[FlightSearchResponse200OutputBestFlightsItem]
    other_flights: list[FlightSearchResponse200OutputOtherFlightsItem]
    airports: list[FlightSearchResponse200OutputAirportsItem]
    next_page_token: None | str | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    price_insights: FlightSearchResponse200OutputPriceInsightsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_response_200_output_price_insights_type_0 import (
            FlightSearchResponse200OutputPriceInsightsType0,
        )

        best_flights = []
        for best_flights_item_data in self.best_flights:
            best_flights_item = best_flights_item_data.to_dict()
            best_flights.append(best_flights_item)

        other_flights = []
        for other_flights_item_data in self.other_flights:
            other_flights_item = other_flights_item_data.to_dict()
            other_flights.append(other_flights_item)

        airports = []
        for airports_item_data in self.airports:
            airports_item = airports_item_data.to_dict()
            airports.append(airports_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        price_insights: dict[str, Any] | None | Unset
        if isinstance(self.price_insights, Unset):
            price_insights = UNSET
        elif isinstance(self.price_insights, FlightSearchResponse200OutputPriceInsightsType0):
            price_insights = self.price_insights.to_dict()
        else:
            price_insights = self.price_insights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bestFlights": best_flights,
                "otherFlights": other_flights,
                "airports": airports,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if price_insights is not UNSET:
            field_dict["priceInsights"] = price_insights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_response_200_output_airports_item import FlightSearchResponse200OutputAirportsItem
        from ..models.flight_search_response_200_output_best_flights_item import (
            FlightSearchResponse200OutputBestFlightsItem,
        )
        from ..models.flight_search_response_200_output_other_flights_item import (
            FlightSearchResponse200OutputOtherFlightsItem,
        )
        from ..models.flight_search_response_200_output_price_insights_type_0 import (
            FlightSearchResponse200OutputPriceInsightsType0,
        )

        d = dict(src_dict)
        best_flights = []
        _best_flights = d.pop("bestFlights")
        for best_flights_item_data in _best_flights:
            best_flights_item = FlightSearchResponse200OutputBestFlightsItem.from_dict(best_flights_item_data)

            best_flights.append(best_flights_item)

        other_flights = []
        _other_flights = d.pop("otherFlights")
        for other_flights_item_data in _other_flights:
            other_flights_item = FlightSearchResponse200OutputOtherFlightsItem.from_dict(other_flights_item_data)

            other_flights.append(other_flights_item)

        airports = []
        _airports = d.pop("airports")
        for airports_item_data in _airports:
            airports_item = FlightSearchResponse200OutputAirportsItem.from_dict(airports_item_data)

            airports.append(airports_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_price_insights(data: object) -> FlightSearchResponse200OutputPriceInsightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_insights_type_0 = FlightSearchResponse200OutputPriceInsightsType0.from_dict(data)

                return price_insights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchResponse200OutputPriceInsightsType0 | None | Unset, data)

        price_insights = _parse_price_insights(d.pop("priceInsights", UNSET))

        flight_search_response_200_output = cls(
            best_flights=best_flights,
            other_flights=other_flights,
            airports=airports,
            next_page_token=next_page_token,
            currency_code=currency_code,
            price_insights=price_insights,
        )

        flight_search_response_200_output.additional_properties = d
        return flight_search_response_200_output

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
