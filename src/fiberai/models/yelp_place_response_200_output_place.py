from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.yelp_place_response_200_output_place_opening_hours_item import (
        YelpPlaceResponse200OutputPlaceOpeningHoursItem,
    )
    from ..models.yelp_place_response_200_output_place_services_item import YelpPlaceResponse200OutputPlaceServicesItem


T = TypeVar("T", bound="YelpPlaceResponse200OutputPlace")


@_attrs_define
class YelpPlaceResponse200OutputPlace:
    """Detailed information about the Yelp business.

    Attributes:
        place_id (str): Yelp business ID.
        name (str): Business display name.
        categories (list[str]): Business categories (e.g. 'Bakeries').
        neighborhoods (list[str]): Neighborhoods the business is located in.
        opening_hours (list[YelpPlaceResponse200OutputPlaceOpeningHoursItem]): Opening hours by day of the week.
        services (list[YelpPlaceResponse200OutputPlaceServicesItem]): Services and features the business offers.
        image_urls (list[str]): Photo URLs for this business.
        slug (None | str | Unset): Business slug from its yelp.com page.
        url (None | str | Unset): yelp.com page for this business.
        rating (float | None | Unset): Average star rating from 0 to 5.
        review_count (int | None | Unset): Total review count.
        is_claimed (bool | None | Unset): True when the business owner has claimed the business page.
        price_level (int | None | Unset): Price level from 1 (least expensive) to 4 (most expensive), as classified on
            Yelp. Null when no price is shown.
        phone_number (None | str | Unset): Contact phone number normalized to E.164 format.
        address (None | str | Unset): Street address of the business.
        website_url (None | str | Unset): Business's own website URL, when available.
        directions_url (None | str | Unset): URL with a map and directions to the business.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA').
    """

    place_id: str
    name: str
    categories: list[str]
    neighborhoods: list[str]
    opening_hours: list[YelpPlaceResponse200OutputPlaceOpeningHoursItem]
    services: list[YelpPlaceResponse200OutputPlaceServicesItem]
    image_urls: list[str]
    slug: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    is_claimed: bool | None | Unset = UNSET
    price_level: int | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    directions_url: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        name = self.name

        categories = self.categories

        neighborhoods = self.neighborhoods

        opening_hours = []
        for opening_hours_item_data in self.opening_hours:
            opening_hours_item = opening_hours_item_data.to_dict()
            opening_hours.append(opening_hours_item)

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        image_urls = self.image_urls

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        review_count: int | None | Unset
        if isinstance(self.review_count, Unset):
            review_count = UNSET
        else:
            review_count = self.review_count

        is_claimed: bool | None | Unset
        if isinstance(self.is_claimed, Unset):
            is_claimed = UNSET
        else:
            is_claimed = self.is_claimed

        price_level: int | None | Unset
        if isinstance(self.price_level, Unset):
            price_level = UNSET
        else:
            price_level = self.price_level

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        directions_url: None | str | Unset
        if isinstance(self.directions_url, Unset):
            directions_url = UNSET
        else:
            directions_url = self.directions_url

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placeId": place_id,
                "name": name,
                "categories": categories,
                "neighborhoods": neighborhoods,
                "openingHours": opening_hours,
                "services": services,
                "imageUrls": image_urls,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if url is not UNSET:
            field_dict["url"] = url
        if rating is not UNSET:
            field_dict["rating"] = rating
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count
        if is_claimed is not UNSET:
            field_dict["isClaimed"] = is_claimed
        if price_level is not UNSET:
            field_dict["priceLevel"] = price_level
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if address is not UNSET:
            field_dict["address"] = address
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url
        if directions_url is not UNSET:
            field_dict["directionsUrl"] = directions_url
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.yelp_place_response_200_output_place_opening_hours_item import (
            YelpPlaceResponse200OutputPlaceOpeningHoursItem,  # noqa: PLC0415
        )
        from ..models.yelp_place_response_200_output_place_services_item import (
            YelpPlaceResponse200OutputPlaceServicesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        place_id = d.pop("placeId")

        name = d.pop("name")

        categories = cast(list[str], d.pop("categories"))

        neighborhoods = cast(list[str], d.pop("neighborhoods"))

        opening_hours = []
        _opening_hours = d.pop("openingHours")
        for opening_hours_item_data in _opening_hours:
            opening_hours_item = YelpPlaceResponse200OutputPlaceOpeningHoursItem.from_dict(opening_hours_item_data)

            opening_hours.append(opening_hours_item)

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = YelpPlaceResponse200OutputPlaceServicesItem.from_dict(services_item_data)

            services.append(services_item)

        image_urls = cast(list[str], d.pop("imageUrls"))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_review_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        review_count = _parse_review_count(d.pop("reviewCount", UNSET))

        def _parse_is_claimed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_claimed = _parse_is_claimed(d.pop("isClaimed", UNSET))

        def _parse_price_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_level = _parse_price_level(d.pop("priceLevel", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("websiteUrl", UNSET))

        def _parse_directions_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directions_url = _parse_directions_url(d.pop("directionsUrl", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        yelp_place_response_200_output_place = cls(
            place_id=place_id,
            name=name,
            categories=categories,
            neighborhoods=neighborhoods,
            opening_hours=opening_hours,
            services=services,
            image_urls=image_urls,
            slug=slug,
            url=url,
            rating=rating,
            review_count=review_count,
            is_claimed=is_claimed,
            price_level=price_level,
            phone_number=phone_number,
            address=address,
            website_url=website_url,
            directions_url=directions_url,
            country_code=country_code,
        )

        yelp_place_response_200_output_place.additional_properties = d
        return yelp_place_response_200_output_place

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
