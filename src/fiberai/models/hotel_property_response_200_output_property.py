from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hotel_property_response_200_output_property_type_type_1 import (
    HotelPropertyResponse200OutputPropertyTypeType1,
)
from ..models.hotel_property_response_200_output_property_type_type_2_type_1 import (
    HotelPropertyResponse200OutputPropertyTypeType2Type1,
)
from ..models.hotel_property_response_200_output_property_type_type_3_type_1 import (
    HotelPropertyResponse200OutputPropertyTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_property_response_200_output_property_coordinates_type_0 import (
        HotelPropertyResponse200OutputPropertyCoordinatesType0,
    )
    from ..models.hotel_property_response_200_output_property_images_item import (
        HotelPropertyResponse200OutputPropertyImagesItem,
    )
    from ..models.hotel_property_response_200_output_property_nearby_places_item import (
        HotelPropertyResponse200OutputPropertyNearbyPlacesItem,
    )
    from ..models.hotel_property_response_200_output_property_offers_item import (
        HotelPropertyResponse200OutputPropertyOffersItem,
    )
    from ..models.hotel_property_response_200_output_property_rate_per_night_type_0 import (
        HotelPropertyResponse200OutputPropertyRatePerNightType0,
    )
    from ..models.hotel_property_response_200_output_property_ratings_breakdown_type_0 import (
        HotelPropertyResponse200OutputPropertyRatingsBreakdownType0,
    )
    from ..models.hotel_property_response_200_output_property_reviews_breakdown_item import (
        HotelPropertyResponse200OutputPropertyReviewsBreakdownItem,
    )
    from ..models.hotel_property_response_200_output_property_total_rate_type_0 import (
        HotelPropertyResponse200OutputPropertyTotalRateType0,
    )
    from ..models.hotel_property_response_200_output_property_typical_price_range_type_0 import (
        HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0,
    )


T = TypeVar("T", bound="HotelPropertyResponse200OutputProperty")


@_attrs_define
class HotelPropertyResponse200OutputProperty:
    """Full property details including offers and amenities.

    Attributes:
        property_token (str): Opaque token identifying this property. Pass as `propertyToken` in POST
            /v1/hotels/property to retrieve full details. Always present on returned properties.
        name (str): Property display name.
        reviews_breakdown (list[HotelPropertyResponse200OutputPropertyReviewsBreakdownItem]): Breakdown of reviews by
            category.
        amenities (list[str]): Amenities offered by this property.
        excluded_amenities (list[str]): Amenities explicitly not offered.
        images (list[HotelPropertyResponse200OutputPropertyImagesItem]): Property images.
        nearby_places (list[HotelPropertyResponse200OutputPropertyNearbyPlacesItem]): Notable nearby places and transit
            options.
        essential_info (list[str]): Key facts for vacation rentals (e.g. 'Entire apartment', 'Sleeps 4').
        amenities_detailed (list[str]): Detailed amenity list for the property.
        offers (list[HotelPropertyResponse200OutputPropertyOffersItem]): Booking offers from online travel agencies.
        type_ (HotelPropertyResponse200OutputPropertyTypeType1 | HotelPropertyResponse200OutputPropertyTypeType2Type1 |
            HotelPropertyResponse200OutputPropertyTypeType3Type1 | None | Unset): Property category.
        description (None | str | Unset): Property description.
        url (None | str | Unset): Property website URL.
        coordinates (HotelPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset): Geographic coordinates of
            the property in decimal degrees.
        city (None | str | Unset): City name.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA').
        check_in_time (None | str | Unset): Check-in time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '15:00'). Null when unavailable.
        check_out_time (None | str | Unset): Check-out time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '11:00'). Null when unavailable.
        rate_per_night (HotelPropertyResponse200OutputPropertyRatePerNightType0 | None | Unset): Nightly rate summary
            for one night.
        total_rate (HotelPropertyResponse200OutputPropertyTotalRateType0 | None | Unset): Total rate summary for the
            entire requested stay, from check-in through check-out. The all-in amount includes taxes and fees when supplied;
            otherwise `baseCost` is provided.
        rating (float | None | Unset): Guest rating from 0 to 5.
        review_count (int | None | Unset): Total number of guest reviews.
        hotel_star_class (int | None | Unset): Observed hotel star class indicating how upscale the property is, from 1
            to 5 whole stars. This is a property classification, not a guest review rating.
        location_rating (float | None | Unset): Location quality rating from 0 to 5.
        deal (None | str | Unset): Deal label when the booking provider marks a promotion; may be present without
            `dealDescription`.
        deal_description (None | str | Unset): Short deal description when supplied by the booking provider; may be
            absent even when `deal` is present.
        address (None | str | Unset): Street address.
        phone (None | str | Unset): Contact phone number normalized to E.164 format.
        directions_url (None | str | Unset): URL with directions to the property.
        typical_price_range (HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0 | None | Unset): Typical price
            range for this property in whole currency units.
        ratings_breakdown (HotelPropertyResponse200OutputPropertyRatingsBreakdownType0 | None | Unset): Guest review
            counts grouped by one- through five-star rating.
    """

    property_token: str
    name: str
    reviews_breakdown: list[HotelPropertyResponse200OutputPropertyReviewsBreakdownItem]
    amenities: list[str]
    excluded_amenities: list[str]
    images: list[HotelPropertyResponse200OutputPropertyImagesItem]
    nearby_places: list[HotelPropertyResponse200OutputPropertyNearbyPlacesItem]
    essential_info: list[str]
    amenities_detailed: list[str]
    offers: list[HotelPropertyResponse200OutputPropertyOffersItem]
    type_: (
        HotelPropertyResponse200OutputPropertyTypeType1
        | HotelPropertyResponse200OutputPropertyTypeType2Type1
        | HotelPropertyResponse200OutputPropertyTypeType3Type1
        | None
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    coordinates: HotelPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset = UNSET
    city: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    rate_per_night: HotelPropertyResponse200OutputPropertyRatePerNightType0 | None | Unset = UNSET
    total_rate: HotelPropertyResponse200OutputPropertyTotalRateType0 | None | Unset = UNSET
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    hotel_star_class: int | None | Unset = UNSET
    location_rating: float | None | Unset = UNSET
    deal: None | str | Unset = UNSET
    deal_description: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    directions_url: None | str | Unset = UNSET
    typical_price_range: HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0 | None | Unset = UNSET
    ratings_breakdown: HotelPropertyResponse200OutputPropertyRatingsBreakdownType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hotel_property_response_200_output_property_coordinates_type_0 import (
            HotelPropertyResponse200OutputPropertyCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_rate_per_night_type_0 import (
            HotelPropertyResponse200OutputPropertyRatePerNightType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_ratings_breakdown_type_0 import (
            HotelPropertyResponse200OutputPropertyRatingsBreakdownType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_total_rate_type_0 import (
            HotelPropertyResponse200OutputPropertyTotalRateType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_typical_price_range_type_0 import (
            HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0,  # noqa: PLC0415
        )

        property_token = self.property_token

        name = self.name

        reviews_breakdown = []
        for reviews_breakdown_item_data in self.reviews_breakdown:
            reviews_breakdown_item = reviews_breakdown_item_data.to_dict()
            reviews_breakdown.append(reviews_breakdown_item)

        amenities = self.amenities

        excluded_amenities = self.excluded_amenities

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        nearby_places = []
        for nearby_places_item_data in self.nearby_places:
            nearby_places_item = nearby_places_item_data.to_dict()
            nearby_places.append(nearby_places_item)

        essential_info = self.essential_info

        amenities_detailed = self.amenities_detailed

        offers = []
        for offers_item_data in self.offers:
            offers_item = offers_item_data.to_dict()
            offers.append(offers_item)

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, HotelPropertyResponse200OutputPropertyTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, HotelPropertyResponse200OutputPropertyTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, HotelPropertyResponse200OutputPropertyTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, HotelPropertyResponse200OutputPropertyCoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        rate_per_night: dict[str, Any] | None | Unset
        if isinstance(self.rate_per_night, Unset):
            rate_per_night = UNSET
        elif isinstance(self.rate_per_night, HotelPropertyResponse200OutputPropertyRatePerNightType0):
            rate_per_night = self.rate_per_night.to_dict()
        else:
            rate_per_night = self.rate_per_night

        total_rate: dict[str, Any] | None | Unset
        if isinstance(self.total_rate, Unset):
            total_rate = UNSET
        elif isinstance(self.total_rate, HotelPropertyResponse200OutputPropertyTotalRateType0):
            total_rate = self.total_rate.to_dict()
        else:
            total_rate = self.total_rate

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

        hotel_star_class: int | None | Unset
        if isinstance(self.hotel_star_class, Unset):
            hotel_star_class = UNSET
        else:
            hotel_star_class = self.hotel_star_class

        location_rating: float | None | Unset
        if isinstance(self.location_rating, Unset):
            location_rating = UNSET
        else:
            location_rating = self.location_rating

        deal: None | str | Unset
        if isinstance(self.deal, Unset):
            deal = UNSET
        else:
            deal = self.deal

        deal_description: None | str | Unset
        if isinstance(self.deal_description, Unset):
            deal_description = UNSET
        else:
            deal_description = self.deal_description

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        directions_url: None | str | Unset
        if isinstance(self.directions_url, Unset):
            directions_url = UNSET
        else:
            directions_url = self.directions_url

        typical_price_range: dict[str, Any] | None | Unset
        if isinstance(self.typical_price_range, Unset):
            typical_price_range = UNSET
        elif isinstance(self.typical_price_range, HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0):
            typical_price_range = self.typical_price_range.to_dict()
        else:
            typical_price_range = self.typical_price_range

        ratings_breakdown: dict[str, Any] | None | Unset
        if isinstance(self.ratings_breakdown, Unset):
            ratings_breakdown = UNSET
        elif isinstance(self.ratings_breakdown, HotelPropertyResponse200OutputPropertyRatingsBreakdownType0):
            ratings_breakdown = self.ratings_breakdown.to_dict()
        else:
            ratings_breakdown = self.ratings_breakdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyToken": property_token,
                "name": name,
                "reviewsBreakdown": reviews_breakdown,
                "amenities": amenities,
                "excludedAmenities": excluded_amenities,
                "images": images,
                "nearbyPlaces": nearby_places,
                "essentialInfo": essential_info,
                "amenitiesDetailed": amenities_detailed,
                "offers": offers,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if rate_per_night is not UNSET:
            field_dict["ratePerNight"] = rate_per_night
        if total_rate is not UNSET:
            field_dict["totalRate"] = total_rate
        if rating is not UNSET:
            field_dict["rating"] = rating
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count
        if hotel_star_class is not UNSET:
            field_dict["hotelStarClass"] = hotel_star_class
        if location_rating is not UNSET:
            field_dict["locationRating"] = location_rating
        if deal is not UNSET:
            field_dict["deal"] = deal
        if deal_description is not UNSET:
            field_dict["dealDescription"] = deal_description
        if address is not UNSET:
            field_dict["address"] = address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if directions_url is not UNSET:
            field_dict["directionsUrl"] = directions_url
        if typical_price_range is not UNSET:
            field_dict["typicalPriceRange"] = typical_price_range
        if ratings_breakdown is not UNSET:
            field_dict["ratingsBreakdown"] = ratings_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_property_response_200_output_property_coordinates_type_0 import (
            HotelPropertyResponse200OutputPropertyCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_images_item import (
            HotelPropertyResponse200OutputPropertyImagesItem,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_nearby_places_item import (
            HotelPropertyResponse200OutputPropertyNearbyPlacesItem,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_offers_item import (
            HotelPropertyResponse200OutputPropertyOffersItem,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_rate_per_night_type_0 import (
            HotelPropertyResponse200OutputPropertyRatePerNightType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_ratings_breakdown_type_0 import (
            HotelPropertyResponse200OutputPropertyRatingsBreakdownType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_reviews_breakdown_item import (
            HotelPropertyResponse200OutputPropertyReviewsBreakdownItem,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_total_rate_type_0 import (
            HotelPropertyResponse200OutputPropertyTotalRateType0,  # noqa: PLC0415
        )
        from ..models.hotel_property_response_200_output_property_typical_price_range_type_0 import (
            HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        property_token = d.pop("propertyToken")

        name = d.pop("name")

        reviews_breakdown = []
        _reviews_breakdown = d.pop("reviewsBreakdown")
        for reviews_breakdown_item_data in _reviews_breakdown:
            reviews_breakdown_item = HotelPropertyResponse200OutputPropertyReviewsBreakdownItem.from_dict(
                reviews_breakdown_item_data
            )

            reviews_breakdown.append(reviews_breakdown_item)

        amenities = cast(list[str], d.pop("amenities"))

        excluded_amenities = cast(list[str], d.pop("excludedAmenities"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = HotelPropertyResponse200OutputPropertyImagesItem.from_dict(images_item_data)

            images.append(images_item)

        nearby_places = []
        _nearby_places = d.pop("nearbyPlaces")
        for nearby_places_item_data in _nearby_places:
            nearby_places_item = HotelPropertyResponse200OutputPropertyNearbyPlacesItem.from_dict(
                nearby_places_item_data
            )

            nearby_places.append(nearby_places_item)

        essential_info = cast(list[str], d.pop("essentialInfo"))

        amenities_detailed = cast(list[str], d.pop("amenitiesDetailed"))

        offers = []
        _offers = d.pop("offers")
        for offers_item_data in _offers:
            offers_item = HotelPropertyResponse200OutputPropertyOffersItem.from_dict(offers_item_data)

            offers.append(offers_item)

        def _parse_type_(
            data: object,
        ) -> (
            HotelPropertyResponse200OutputPropertyTypeType1
            | HotelPropertyResponse200OutputPropertyTypeType2Type1
            | HotelPropertyResponse200OutputPropertyTypeType3Type1
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
                type_type_1 = HotelPropertyResponse200OutputPropertyTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = HotelPropertyResponse200OutputPropertyTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = HotelPropertyResponse200OutputPropertyTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                HotelPropertyResponse200OutputPropertyTypeType1
                | HotelPropertyResponse200OutputPropertyTypeType2Type1
                | HotelPropertyResponse200OutputPropertyTypeType3Type1
                | None
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_coordinates(data: object) -> HotelPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = HotelPropertyResponse200OutputPropertyCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset, data)

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))

        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))

        def _parse_rate_per_night(
            data: object,
        ) -> HotelPropertyResponse200OutputPropertyRatePerNightType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_per_night_type_0 = HotelPropertyResponse200OutputPropertyRatePerNightType0.from_dict(data)

                return rate_per_night_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyRatePerNightType0 | None | Unset, data)

        rate_per_night = _parse_rate_per_night(d.pop("ratePerNight", UNSET))

        def _parse_total_rate(data: object) -> HotelPropertyResponse200OutputPropertyTotalRateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_rate_type_0 = HotelPropertyResponse200OutputPropertyTotalRateType0.from_dict(data)

                return total_rate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyTotalRateType0 | None | Unset, data)

        total_rate = _parse_total_rate(d.pop("totalRate", UNSET))

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

        def _parse_hotel_star_class(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hotel_star_class = _parse_hotel_star_class(d.pop("hotelStarClass", UNSET))

        def _parse_location_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        location_rating = _parse_location_rating(d.pop("locationRating", UNSET))

        def _parse_deal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deal = _parse_deal(d.pop("deal", UNSET))

        def _parse_deal_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deal_description = _parse_deal_description(d.pop("dealDescription", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_directions_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directions_url = _parse_directions_url(d.pop("directionsUrl", UNSET))

        def _parse_typical_price_range(
            data: object,
        ) -> HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                typical_price_range_type_0 = HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0.from_dict(
                    data
                )

                return typical_price_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyTypicalPriceRangeType0 | None | Unset, data)

        typical_price_range = _parse_typical_price_range(d.pop("typicalPriceRange", UNSET))

        def _parse_ratings_breakdown(
            data: object,
        ) -> HotelPropertyResponse200OutputPropertyRatingsBreakdownType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ratings_breakdown_type_0 = HotelPropertyResponse200OutputPropertyRatingsBreakdownType0.from_dict(data)

                return ratings_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyRatingsBreakdownType0 | None | Unset, data)

        ratings_breakdown = _parse_ratings_breakdown(d.pop("ratingsBreakdown", UNSET))

        hotel_property_response_200_output_property = cls(
            property_token=property_token,
            name=name,
            reviews_breakdown=reviews_breakdown,
            amenities=amenities,
            excluded_amenities=excluded_amenities,
            images=images,
            nearby_places=nearby_places,
            essential_info=essential_info,
            amenities_detailed=amenities_detailed,
            offers=offers,
            type_=type_,
            description=description,
            url=url,
            coordinates=coordinates,
            city=city,
            country_code=country_code,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            rate_per_night=rate_per_night,
            total_rate=total_rate,
            rating=rating,
            review_count=review_count,
            hotel_star_class=hotel_star_class,
            location_rating=location_rating,
            deal=deal,
            deal_description=deal_description,
            address=address,
            phone=phone,
            directions_url=directions_url,
            typical_price_range=typical_price_range,
            ratings_breakdown=ratings_breakdown,
        )

        hotel_property_response_200_output_property.additional_properties = d
        return hotel_property_response_200_output_property

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
