from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelPropertyBody")


@_attrs_define
class HotelPropertyBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        property_token (str): Opaque identifier for a specific hotel or vacation rental. Obtain it from the
            `propertyToken` of a result returned by the hotel search endpoint (`POST /v1/hotels/search`).
        check_in_date (str): Check-in date for the stay.
        check_out_date (str): Check-out date for the stay.
        adults (int | Unset): Number of adult guests (at least 1). Total guests (`adults` + `children`) must not exceed
            6 for hotels or 10 for vacation rentals. Default: 2.
        children (int | Unset): Number of child guests. Total guests (`adults` + `children`) must not exceed 6 for
            hotels or 10 for vacation rentals. Default: 0.
        children_ages (list[int] | Unset): Ages of each child guest. Must contain exactly `children` entries when
            `children` is greater than zero.
        currency_code (str | Unset): ISO 4217 currency code for prices in the response (e.g. 'EUR', 'GBP', 'CAD'). Case-
            insensitive. Defaults to USD. Default: 'USD'.
        search_market_country_code (str | Unset): ISO 3166-1 alpha-3 country code that sets the search market (e.g.
            'GBR', 'BRA'). This affects regional pricing and availability. Case-insensitive. Default: 'USA'.
        language_code (str | Unset): Language for results such as property names and amenity labels. Pass a BCP-47
            language tag such as 'en', 'en-US', 'pt-BR', 'zh-CN', 'ja', 'ko', 'fr', 'de', or 'es'. Defaults to en. Default:
            'en'.
    """

    api_key: str
    property_token: str
    check_in_date: str
    check_out_date: str
    adults: int | Unset = 2
    children: int | Unset = 0
    children_ages: list[int] | Unset = UNSET
    currency_code: str | Unset = "USD"
    search_market_country_code: str | Unset = "USA"
    language_code: str | Unset = "en"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        property_token = self.property_token

        check_in_date = self.check_in_date

        check_out_date = self.check_out_date

        adults = self.adults

        children = self.children

        children_ages: list[int] | Unset = UNSET
        if not isinstance(self.children_ages, Unset):
            children_ages = self.children_ages

        currency_code = self.currency_code

        search_market_country_code = self.search_market_country_code

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "propertyToken": property_token,
                "checkInDate": check_in_date,
                "checkOutDate": check_out_date,
            }
        )
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if children_ages is not UNSET:
            field_dict["childrenAges"] = children_ages
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if search_market_country_code is not UNSET:
            field_dict["searchMarketCountryCode"] = search_market_country_code
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        property_token = d.pop("propertyToken")

        check_in_date = d.pop("checkInDate")

        check_out_date = d.pop("checkOutDate")

        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        children_ages = cast(list[int], d.pop("childrenAges", UNSET))

        currency_code = d.pop("currencyCode", UNSET)

        search_market_country_code = d.pop("searchMarketCountryCode", UNSET)

        language_code = d.pop("languageCode", UNSET)

        hotel_property_body = cls(
            api_key=api_key,
            property_token=property_token,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            adults=adults,
            children=children,
            children_ages=children_ages,
            currency_code=currency_code,
            search_market_country_code=search_market_country_code,
            language_code=language_code,
        )

        hotel_property_body.additional_properties = d
        return hotel_property_body

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
