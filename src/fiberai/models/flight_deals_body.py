from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_deals_body_discovery_type_0 import FlightDealsBodyDiscoveryType0
    from ..models.flight_deals_body_discovery_type_1 import FlightDealsBodyDiscoveryType1


T = TypeVar("T", bound="FlightDealsBody")


@_attrs_define
class FlightDealsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        departure_airports (str): Where to find deals from. Accepts a single 3-letter IATA airport code (e.g. 'JFK'), an
            X- metro alias that covers every airport in a metro area (e.g. 'X-NYC' — call GET /v1/enums/flight-regions for
            the full list), or a Freebase ID — a stable location identifier beginning with '/m/' or '/g/' (e.g. '/m/02_286'
            for New York City), listed as `freebaseId` in GET /v1/enums/flight-regions. Comma-separated airport lists are
            not supported; use an X- alias instead. Case-insensitive except Freebase IDs.
        currency_code (str | Unset): ISO 4217 currency code for prices in the response (e.g. 'EUR', 'GBP', 'CAD'). Case-
            insensitive. Defaults to USD. Default: 'USD'.
        language_code (str | Unset): Language for destination names and descriptions. Pass a BCP-47 language tag such as
            'en', 'en-US', 'pt-BR', 'zh-CN', 'ja', 'ko', 'fr', 'de', 'es'. Does not change which deals are returned.
            Defaults to en. Default: 'en'.
        discovery (FlightDealsBodyDiscoveryType0 | FlightDealsBodyDiscoveryType1 | None | Unset): How to narrow the
            deals. Omit to return the cheapest round-trip deals from the departure location. Use the `freeText` mode to
            describe the kind of destinations you want in plain language (e.g. 'beaches and islands'); use the `filters`
            mode for precise constraints on price, stops, cabin class, or airline. Provide exactly one mode — they cannot be
            combined.
    """

    api_key: str
    departure_airports: str
    currency_code: str | Unset = "USD"
    language_code: str | Unset = "en"
    discovery: FlightDealsBodyDiscoveryType0 | FlightDealsBodyDiscoveryType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_deals_body_discovery_type_0 import FlightDealsBodyDiscoveryType0  # noqa: PLC0415
        from ..models.flight_deals_body_discovery_type_1 import FlightDealsBodyDiscoveryType1  # noqa: PLC0415

        api_key = self.api_key

        departure_airports = self.departure_airports

        currency_code = self.currency_code

        language_code = self.language_code

        discovery: dict[str, Any] | None | Unset
        if isinstance(self.discovery, Unset):
            discovery = UNSET
        elif isinstance(self.discovery, FlightDealsBodyDiscoveryType0):
            discovery = self.discovery.to_dict()
        elif isinstance(self.discovery, FlightDealsBodyDiscoveryType1):
            discovery = self.discovery.to_dict()
        else:
            discovery = self.discovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "departureAirports": departure_airports,
            }
        )
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if discovery is not UNSET:
            field_dict["discovery"] = discovery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_deals_body_discovery_type_0 import FlightDealsBodyDiscoveryType0  # noqa: PLC0415
        from ..models.flight_deals_body_discovery_type_1 import FlightDealsBodyDiscoveryType1  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        departure_airports = d.pop("departureAirports")

        currency_code = d.pop("currencyCode", UNSET)

        language_code = d.pop("languageCode", UNSET)

        def _parse_discovery(
            data: object,
        ) -> FlightDealsBodyDiscoveryType0 | FlightDealsBodyDiscoveryType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discovery_type_0 = FlightDealsBodyDiscoveryType0.from_dict(data)

                return discovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discovery_type_1 = FlightDealsBodyDiscoveryType1.from_dict(data)

                return discovery_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightDealsBodyDiscoveryType0 | FlightDealsBodyDiscoveryType1 | None | Unset, data)

        discovery = _parse_discovery(d.pop("discovery", UNSET))

        flight_deals_body = cls(
            api_key=api_key,
            departure_airports=departure_airports,
            currency_code=currency_code,
            language_code=language_code,
            discovery=discovery,
        )

        flight_deals_body.additional_properties = d
        return flight_deals_body

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
