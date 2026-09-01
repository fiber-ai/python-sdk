from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YelpSearchResponse200OutputBusinessesItem")


@_attrs_define
class YelpSearchResponse200OutputBusinessesItem:
    """
    Attributes:
        place_id (str): Yelp business ID. Use with POST /v1/yelp/place and POST /v1/yelp/reviews.
        name (str): Business display name.
        categories (list[str]): Business categories (e.g. 'Coffee Roasteries').
        url (None | str | Unset): yelp.com page for this business.
        rating (float | None | Unset): Average star rating from 0 to 5.
        review_count (int | None | Unset): Total review count.
        phone_number (None | str | Unset): Contact phone number normalized to E.164 format.
        price_level (int | None | Unset): Price level from 1 (least expensive) to 4 (most expensive), as classified on
            Yelp. Null when no price is shown.
        neighborhood (None | str | Unset): Neighborhood the business is located in.
        thumbnail_url (None | str | Unset): Thumbnail image URL for this business.
    """

    place_id: str
    name: str
    categories: list[str]
    url: None | str | Unset = UNSET
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    price_level: int | None | Unset = UNSET
    neighborhood: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        name = self.name

        categories = self.categories

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

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        price_level: int | None | Unset
        if isinstance(self.price_level, Unset):
            price_level = UNSET
        else:
            price_level = self.price_level

        neighborhood: None | str | Unset
        if isinstance(self.neighborhood, Unset):
            neighborhood = UNSET
        else:
            neighborhood = self.neighborhood

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placeId": place_id,
                "name": name,
                "categories": categories,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if rating is not UNSET:
            field_dict["rating"] = rating
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if price_level is not UNSET:
            field_dict["priceLevel"] = price_level
        if neighborhood is not UNSET:
            field_dict["neighborhood"] = neighborhood
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("placeId")

        name = d.pop("name")

        categories = cast(list[str], d.pop("categories"))

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

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_price_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_level = _parse_price_level(d.pop("priceLevel", UNSET))

        def _parse_neighborhood(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        neighborhood = _parse_neighborhood(d.pop("neighborhood", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        yelp_search_response_200_output_businesses_item = cls(
            place_id=place_id,
            name=name,
            categories=categories,
            url=url,
            rating=rating,
            review_count=review_count,
            phone_number=phone_number,
            price_level=price_level,
            neighborhood=neighborhood,
            thumbnail_url=thumbnail_url,
        )

        yelp_search_response_200_output_businesses_item.additional_properties = d
        return yelp_search_response_200_output_businesses_item

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
