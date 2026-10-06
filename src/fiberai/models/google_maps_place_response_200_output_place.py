from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_maps_place_response_200_output_place_attributes_item import (
        GoogleMapsPlaceResponse200OutputPlaceAttributesItem,
    )
    from ..models.google_maps_place_response_200_output_place_coordinates_type_0 import (
        GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0,
    )
    from ..models.google_maps_place_response_200_output_place_opening_hours_item import (
        GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem,
    )
    from ..models.google_maps_place_response_200_output_place_rating_breakdown_item import (
        GoogleMapsPlaceResponse200OutputPlaceRatingBreakdownItem,
    )
    from ..models.google_maps_place_response_200_output_place_reviews_item import (
        GoogleMapsPlaceResponse200OutputPlaceReviewsItem,
    )


T = TypeVar("T", bound="GoogleMapsPlaceResponse200OutputPlace")


@_attrs_define
class GoogleMapsPlaceResponse200OutputPlace:
    """Detailed information about the Google Maps place.

    Attributes:
        place_id (str): Google Maps place ID. Use with POST /v1/google-maps/place and POST /v1/google-maps/reviews.
        name (str): Place display name.
        url (str): Google Maps page for this place.
        categories (list[str]): Categories this place belongs to (e.g. 'Coffee shop', 'Park', 'Subway station').
        opening_hours (list[GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem]): Opening hours by day of the week,
            when available.
        rating_breakdown (list[GoogleMapsPlaceResponse200OutputPlaceRatingBreakdownItem]): Count of reviews per star
            rating, when available.
        attributes (list[GoogleMapsPlaceResponse200OutputPlaceAttributesItem]): Grouped attributes such as service
            options, highlights, offerings, and accessibility.
        reviews (list[GoogleMapsPlaceResponse200OutputPlaceReviewsItem]): A sample of recent reviews included with the
            place. Use POST /v1/google-maps/reviews for the full paginated list.
        rating (float | None | Unset): Average star rating from 0 to 5.
        review_count (int | None | Unset): Total review count.
        phone_number (None | str | Unset): Contact phone number in E.164 format when the country can be determined,
            otherwise as listed on Google Maps.
        website_url (None | str | Unset): Website URL for this place.
        address (None | str | Unset): Street address of the place.
        coordinates (GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0 | None | Unset): Geographic coordinates of
            the place.
        thumbnail_url (None | str | Unset): Thumbnail image URL for this place.
        description (None | str | Unset): Short description of the place.
    """

    place_id: str
    name: str
    url: str
    categories: list[str]
    opening_hours: list[GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem]
    rating_breakdown: list[GoogleMapsPlaceResponse200OutputPlaceRatingBreakdownItem]
    attributes: list[GoogleMapsPlaceResponse200OutputPlaceAttributesItem]
    reviews: list[GoogleMapsPlaceResponse200OutputPlaceReviewsItem]
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    coordinates: GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0 | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_maps_place_response_200_output_place_coordinates_type_0 import (
            GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0,  # noqa: PLC0415
        )

        place_id = self.place_id

        name = self.name

        url = self.url

        categories = self.categories

        opening_hours = []
        for opening_hours_item_data in self.opening_hours:
            opening_hours_item = opening_hours_item_data.to_dict()
            opening_hours.append(opening_hours_item)

        rating_breakdown = []
        for rating_breakdown_item_data in self.rating_breakdown:
            rating_breakdown_item = rating_breakdown_item_data.to_dict()
            rating_breakdown.append(rating_breakdown_item)

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

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

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placeId": place_id,
                "name": name,
                "url": url,
                "categories": categories,
                "openingHours": opening_hours,
                "ratingBreakdown": rating_breakdown,
                "attributes": attributes,
                "reviews": reviews,
            }
        )
        if rating is not UNSET:
            field_dict["rating"] = rating
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url
        if address is not UNSET:
            field_dict["address"] = address
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_place_response_200_output_place_attributes_item import (
            GoogleMapsPlaceResponse200OutputPlaceAttributesItem,  # noqa: PLC0415
        )
        from ..models.google_maps_place_response_200_output_place_coordinates_type_0 import (
            GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.google_maps_place_response_200_output_place_opening_hours_item import (
            GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem,  # noqa: PLC0415
        )
        from ..models.google_maps_place_response_200_output_place_rating_breakdown_item import (
            GoogleMapsPlaceResponse200OutputPlaceRatingBreakdownItem,  # noqa: PLC0415
        )
        from ..models.google_maps_place_response_200_output_place_reviews_item import (
            GoogleMapsPlaceResponse200OutputPlaceReviewsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        place_id = d.pop("placeId")

        name = d.pop("name")

        url = d.pop("url")

        categories = cast(list[str], d.pop("categories"))

        opening_hours = []
        _opening_hours = d.pop("openingHours")
        for opening_hours_item_data in _opening_hours:
            opening_hours_item = GoogleMapsPlaceResponse200OutputPlaceOpeningHoursItem.from_dict(
                opening_hours_item_data
            )

            opening_hours.append(opening_hours_item)

        rating_breakdown = []
        _rating_breakdown = d.pop("ratingBreakdown")
        for rating_breakdown_item_data in _rating_breakdown:
            rating_breakdown_item = GoogleMapsPlaceResponse200OutputPlaceRatingBreakdownItem.from_dict(
                rating_breakdown_item_data
            )

            rating_breakdown.append(rating_breakdown_item)

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = GoogleMapsPlaceResponse200OutputPlaceAttributesItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = GoogleMapsPlaceResponse200OutputPlaceReviewsItem.from_dict(reviews_item_data)

            reviews.append(reviews_item)

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

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("websiteUrl", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_coordinates(data: object) -> GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GoogleMapsPlaceResponse200OutputPlaceCoordinatesType0 | None | Unset, data)

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        google_maps_place_response_200_output_place = cls(
            place_id=place_id,
            name=name,
            url=url,
            categories=categories,
            opening_hours=opening_hours,
            rating_breakdown=rating_breakdown,
            attributes=attributes,
            reviews=reviews,
            rating=rating,
            review_count=review_count,
            phone_number=phone_number,
            website_url=website_url,
            address=address,
            coordinates=coordinates,
            thumbnail_url=thumbnail_url,
            description=description,
        )

        google_maps_place_response_200_output_place.additional_properties = d
        return google_maps_place_response_200_output_place

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
