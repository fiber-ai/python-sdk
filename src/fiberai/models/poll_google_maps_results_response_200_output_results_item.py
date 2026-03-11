from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollGoogleMapsResultsResponse200OutputResultsItem")


@_attrs_define
class PollGoogleMapsResultsResponse200OutputResultsItem:
    """
    Attributes:
        place_id (str):
        name (str):
        latitude (float):
        longitude (float):
        all_types (list[str]):
        google_maps_url (str): The Google Maps URL of the place
        address (None | str | Unset):
        description (None | str | Unset):
        website (None | str | Unset):
        rating (float | None | Unset):
        num_reviews (int | None | Unset):
        primary_type (None | str | Unset):
        price_level (None | str | Unset):
        phone_number (None | str | Unset):
        country_iso_code (None | str | Unset):
    """

    place_id: str
    name: str
    latitude: float
    longitude: float
    all_types: list[str]
    google_maps_url: str
    address: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    rating: float | None | Unset = UNSET
    num_reviews: int | None | Unset = UNSET
    primary_type: None | str | Unset = UNSET
    price_level: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    country_iso_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        name = self.name

        latitude = self.latitude

        longitude = self.longitude

        all_types = self.all_types

        google_maps_url = self.google_maps_url

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        num_reviews: int | None | Unset
        if isinstance(self.num_reviews, Unset):
            num_reviews = UNSET
        else:
            num_reviews = self.num_reviews

        primary_type: None | str | Unset
        if isinstance(self.primary_type, Unset):
            primary_type = UNSET
        else:
            primary_type = self.primary_type

        price_level: None | str | Unset
        if isinstance(self.price_level, Unset):
            price_level = UNSET
        else:
            price_level = self.price_level

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        country_iso_code: None | str | Unset
        if isinstance(self.country_iso_code, Unset):
            country_iso_code = UNSET
        else:
            country_iso_code = self.country_iso_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placeId": place_id,
                "name": name,
                "latitude": latitude,
                "longitude": longitude,
                "allTypes": all_types,
                "googleMapsURL": google_maps_url,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if description is not UNSET:
            field_dict["description"] = description
        if website is not UNSET:
            field_dict["website"] = website
        if rating is not UNSET:
            field_dict["rating"] = rating
        if num_reviews is not UNSET:
            field_dict["numReviews"] = num_reviews
        if primary_type is not UNSET:
            field_dict["primaryType"] = primary_type
        if price_level is not UNSET:
            field_dict["priceLevel"] = price_level
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if country_iso_code is not UNSET:
            field_dict["countryIsoCode"] = country_iso_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("placeId")

        name = d.pop("name")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        all_types = cast(list[str], d.pop("allTypes"))

        google_maps_url = d.pop("googleMapsURL")

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_num_reviews(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_reviews = _parse_num_reviews(d.pop("numReviews", UNSET))

        def _parse_primary_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_type = _parse_primary_type(d.pop("primaryType", UNSET))

        def _parse_price_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_level = _parse_price_level(d.pop("priceLevel", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_country_iso_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_iso_code = _parse_country_iso_code(d.pop("countryIsoCode", UNSET))

        poll_google_maps_results_response_200_output_results_item = cls(
            place_id=place_id,
            name=name,
            latitude=latitude,
            longitude=longitude,
            all_types=all_types,
            google_maps_url=google_maps_url,
            address=address,
            description=description,
            website=website,
            rating=rating,
            num_reviews=num_reviews,
            primary_type=primary_type,
            price_level=price_level,
            phone_number=phone_number,
            country_iso_code=country_iso_code,
        )

        poll_google_maps_results_response_200_output_results_item.additional_properties = d
        return poll_google_maps_results_response_200_output_results_item

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
