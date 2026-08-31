from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_booking_options_body_trip_type_0 import FlightBookingOptionsBodyTripType0
    from ..models.flight_booking_options_body_trip_type_1 import FlightBookingOptionsBodyTripType1
    from ..models.flight_booking_options_body_trip_type_2 import FlightBookingOptionsBodyTripType2


T = TypeVar("T", bound="FlightBookingOptionsBody")


@_attrs_define
class FlightBookingOptionsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        booking_token (str): Booking token from the `bookingToken` field of an itinerary returned by the flight search
            endpoint (`POST /v1/flights/search`).
        trip (FlightBookingOptionsBodyTripType0 | FlightBookingOptionsBodyTripType1 |
            FlightBookingOptionsBodyTripType2): Trip configuration. The shape is determined by flightType — see each variant
            for its required fields.
        currency_code (str | Unset): ISO 4217 currency code for prices in the response (e.g. 'EUR', 'GBP', 'CAD'). Case-
            insensitive. Defaults to USD. Match the value used in the original search so prices stay comparable. Default:
            'USD'.
        search_market_country_code (str | Unset): ISO 3166-1 alpha-3 country code that sets the search market. Match the
            value used in the original search for consistent pricing and availability. Case-insensitive. Default: 'USA'.
        language_code (str | Unset): Language for booking option labels (e.g. fare names). Pass a BCP-47 language tag
            such as 'en', 'en-US', 'pt-BR', 'zh-CN', 'ja', 'ko', 'fr', 'de', 'es'. Default: 'en'.
    """

    api_key: str
    booking_token: str
    trip: FlightBookingOptionsBodyTripType0 | FlightBookingOptionsBodyTripType1 | FlightBookingOptionsBodyTripType2
    currency_code: str | Unset = "USD"
    search_market_country_code: str | Unset = "USA"
    language_code: str | Unset = "en"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_booking_options_body_trip_type_0 import FlightBookingOptionsBodyTripType0  # noqa: PLC0415
        from ..models.flight_booking_options_body_trip_type_1 import FlightBookingOptionsBodyTripType1  # noqa: PLC0415

        api_key = self.api_key

        booking_token = self.booking_token

        trip: dict[str, Any]
        if isinstance(self.trip, FlightBookingOptionsBodyTripType0):
            trip = self.trip.to_dict()
        elif isinstance(self.trip, FlightBookingOptionsBodyTripType1):
            trip = self.trip.to_dict()
        else:
            trip = self.trip.to_dict()

        currency_code = self.currency_code

        search_market_country_code = self.search_market_country_code

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "bookingToken": booking_token,
                "trip": trip,
            }
        )
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if search_market_country_code is not UNSET:
            field_dict["searchMarketCountryCode"] = search_market_country_code
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_booking_options_body_trip_type_0 import FlightBookingOptionsBodyTripType0  # noqa: PLC0415
        from ..models.flight_booking_options_body_trip_type_1 import FlightBookingOptionsBodyTripType1  # noqa: PLC0415
        from ..models.flight_booking_options_body_trip_type_2 import FlightBookingOptionsBodyTripType2  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        booking_token = d.pop("bookingToken")

        def _parse_trip(
            data: object,
        ) -> FlightBookingOptionsBodyTripType0 | FlightBookingOptionsBodyTripType1 | FlightBookingOptionsBodyTripType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trip_type_0 = FlightBookingOptionsBodyTripType0.from_dict(data)

                return trip_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trip_type_1 = FlightBookingOptionsBodyTripType1.from_dict(data)

                return trip_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            trip_type_2 = FlightBookingOptionsBodyTripType2.from_dict(data)

            return trip_type_2

        trip = _parse_trip(d.pop("trip"))

        currency_code = d.pop("currencyCode", UNSET)

        search_market_country_code = d.pop("searchMarketCountryCode", UNSET)

        language_code = d.pop("languageCode", UNSET)

        flight_booking_options_body = cls(
            api_key=api_key,
            booking_token=booking_token,
            trip=trip,
            currency_code=currency_code,
            search_market_country_code=search_market_country_code,
            language_code=language_code,
        )

        flight_booking_options_body.additional_properties = d
        return flight_booking_options_body

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
