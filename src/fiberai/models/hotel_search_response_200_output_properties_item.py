from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hotel_search_response_200_output_properties_item_type_type_1 import (
    HotelSearchResponse200OutputPropertiesItemTypeType1,
)
from ..models.hotel_search_response_200_output_properties_item_type_type_2_type_1 import (
    HotelSearchResponse200OutputPropertiesItemTypeType2Type1,
)
from ..models.hotel_search_response_200_output_properties_item_type_type_3_type_1 import (
    HotelSearchResponse200OutputPropertiesItemTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_search_response_200_output_properties_item_coordinates_type_0 import (
        HotelSearchResponse200OutputPropertiesItemCoordinatesType0,
    )
    from ..models.hotel_search_response_200_output_properties_item_images_item import (
        HotelSearchResponse200OutputPropertiesItemImagesItem,
    )
    from ..models.hotel_search_response_200_output_properties_item_nearby_places_item import (
        HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem,
    )
    from ..models.hotel_search_response_200_output_properties_item_rate_per_night_type_0 import (
        HotelSearchResponse200OutputPropertiesItemRatePerNightType0,
    )
    from ..models.hotel_search_response_200_output_properties_item_reviews_breakdown_item import (
        HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem,
    )
    from ..models.hotel_search_response_200_output_properties_item_total_rate_type_0 import (
        HotelSearchResponse200OutputPropertiesItemTotalRateType0,
    )


T = TypeVar("T", bound="HotelSearchResponse200OutputPropertiesItem")


@_attrs_define
class HotelSearchResponse200OutputPropertiesItem:
    """
    Attributes:
        property_token (str): Opaque token identifying this property. Pass as `propertyToken` in POST
            /v1/hotels/property to retrieve full details. Always present on returned properties.
        name (str): Property display name.
        reviews_breakdown (list[HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem]): Breakdown of reviews
            by category.
        amenities (list[str]): Amenities offered by this property.
        excluded_amenities (list[str]): Amenities explicitly not offered.
        images (list[HotelSearchResponse200OutputPropertiesItemImagesItem]): Property images.
        nearby_places (list[HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem]): Notable nearby places and
            transit options.
        essential_info (list[str]): Key facts for vacation rentals (e.g. 'Entire apartment', 'Sleeps 4').
        type_ (HotelSearchResponse200OutputPropertiesItemTypeType1 |
            HotelSearchResponse200OutputPropertiesItemTypeType2Type1 |
            HotelSearchResponse200OutputPropertiesItemTypeType3Type1 | None | Unset): Property category.
        description (None | str | Unset): Property description.
        url (None | str | Unset): Property website URL.
        coordinates (HotelSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset): Geographic coordinates
            of the property in decimal degrees.
        city (None | str | Unset): City name.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA').
        check_in_time (None | str | Unset): Check-in time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '15:00'). Null when unavailable.
        check_out_time (None | str | Unset): Check-out time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '11:00'). Null when unavailable.
        rate_per_night (HotelSearchResponse200OutputPropertiesItemRatePerNightType0 | None | Unset): Nightly rate
            summary for one night.
        total_rate (HotelSearchResponse200OutputPropertiesItemTotalRateType0 | None | Unset): Total rate summary for the
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
    """

    property_token: str
    name: str
    reviews_breakdown: list[HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem]
    amenities: list[str]
    excluded_amenities: list[str]
    images: list[HotelSearchResponse200OutputPropertiesItemImagesItem]
    nearby_places: list[HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem]
    essential_info: list[str]
    type_: (
        HotelSearchResponse200OutputPropertiesItemTypeType1
        | HotelSearchResponse200OutputPropertiesItemTypeType2Type1
        | HotelSearchResponse200OutputPropertiesItemTypeType3Type1
        | None
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    coordinates: HotelSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset = UNSET
    city: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    rate_per_night: HotelSearchResponse200OutputPropertiesItemRatePerNightType0 | None | Unset = UNSET
    total_rate: HotelSearchResponse200OutputPropertiesItemTotalRateType0 | None | Unset = UNSET
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    hotel_star_class: int | None | Unset = UNSET
    location_rating: float | None | Unset = UNSET
    deal: None | str | Unset = UNSET
    deal_description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hotel_search_response_200_output_properties_item_coordinates_type_0 import (
            HotelSearchResponse200OutputPropertiesItemCoordinatesType0,
        )
        from ..models.hotel_search_response_200_output_properties_item_rate_per_night_type_0 import (
            HotelSearchResponse200OutputPropertiesItemRatePerNightType0,
        )
        from ..models.hotel_search_response_200_output_properties_item_total_rate_type_0 import (
            HotelSearchResponse200OutputPropertiesItemTotalRateType0,
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

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, HotelSearchResponse200OutputPropertiesItemTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, HotelSearchResponse200OutputPropertiesItemTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, HotelSearchResponse200OutputPropertiesItemTypeType3Type1):
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
        elif isinstance(self.coordinates, HotelSearchResponse200OutputPropertiesItemCoordinatesType0):
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
        elif isinstance(self.rate_per_night, HotelSearchResponse200OutputPropertiesItemRatePerNightType0):
            rate_per_night = self.rate_per_night.to_dict()
        else:
            rate_per_night = self.rate_per_night

        total_rate: dict[str, Any] | None | Unset
        if isinstance(self.total_rate, Unset):
            total_rate = UNSET
        elif isinstance(self.total_rate, HotelSearchResponse200OutputPropertiesItemTotalRateType0):
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_search_response_200_output_properties_item_coordinates_type_0 import (
            HotelSearchResponse200OutputPropertiesItemCoordinatesType0,
        )
        from ..models.hotel_search_response_200_output_properties_item_images_item import (
            HotelSearchResponse200OutputPropertiesItemImagesItem,
        )
        from ..models.hotel_search_response_200_output_properties_item_nearby_places_item import (
            HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem,
        )
        from ..models.hotel_search_response_200_output_properties_item_rate_per_night_type_0 import (
            HotelSearchResponse200OutputPropertiesItemRatePerNightType0,
        )
        from ..models.hotel_search_response_200_output_properties_item_reviews_breakdown_item import (
            HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem,
        )
        from ..models.hotel_search_response_200_output_properties_item_total_rate_type_0 import (
            HotelSearchResponse200OutputPropertiesItemTotalRateType0,
        )

        d = dict(src_dict)
        property_token = d.pop("propertyToken")

        name = d.pop("name")

        reviews_breakdown = []
        _reviews_breakdown = d.pop("reviewsBreakdown")
        for reviews_breakdown_item_data in _reviews_breakdown:
            reviews_breakdown_item = HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem.from_dict(
                reviews_breakdown_item_data
            )

            reviews_breakdown.append(reviews_breakdown_item)

        amenities = cast(list[str], d.pop("amenities"))

        excluded_amenities = cast(list[str], d.pop("excludedAmenities"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = HotelSearchResponse200OutputPropertiesItemImagesItem.from_dict(images_item_data)

            images.append(images_item)

        nearby_places = []
        _nearby_places = d.pop("nearbyPlaces")
        for nearby_places_item_data in _nearby_places:
            nearby_places_item = HotelSearchResponse200OutputPropertiesItemNearbyPlacesItem.from_dict(
                nearby_places_item_data
            )

            nearby_places.append(nearby_places_item)

        essential_info = cast(list[str], d.pop("essentialInfo"))

        def _parse_type_(
            data: object,
        ) -> (
            HotelSearchResponse200OutputPropertiesItemTypeType1
            | HotelSearchResponse200OutputPropertiesItemTypeType2Type1
            | HotelSearchResponse200OutputPropertiesItemTypeType3Type1
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
                type_type_1 = HotelSearchResponse200OutputPropertiesItemTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = HotelSearchResponse200OutputPropertiesItemTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = HotelSearchResponse200OutputPropertiesItemTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                HotelSearchResponse200OutputPropertiesItemTypeType1
                | HotelSearchResponse200OutputPropertiesItemTypeType2Type1
                | HotelSearchResponse200OutputPropertiesItemTypeType3Type1
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

        def _parse_coordinates(
            data: object,
        ) -> HotelSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = HotelSearchResponse200OutputPropertiesItemCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset, data)

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
        ) -> HotelSearchResponse200OutputPropertiesItemRatePerNightType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_per_night_type_0 = HotelSearchResponse200OutputPropertiesItemRatePerNightType0.from_dict(data)

                return rate_per_night_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelSearchResponse200OutputPropertiesItemRatePerNightType0 | None | Unset, data)

        rate_per_night = _parse_rate_per_night(d.pop("ratePerNight", UNSET))

        def _parse_total_rate(data: object) -> HotelSearchResponse200OutputPropertiesItemTotalRateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_rate_type_0 = HotelSearchResponse200OutputPropertiesItemTotalRateType0.from_dict(data)

                return total_rate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelSearchResponse200OutputPropertiesItemTotalRateType0 | None | Unset, data)

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

        hotel_search_response_200_output_properties_item = cls(
            property_token=property_token,
            name=name,
            reviews_breakdown=reviews_breakdown,
            amenities=amenities,
            excluded_amenities=excluded_amenities,
            images=images,
            nearby_places=nearby_places,
            essential_info=essential_info,
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
        )

        hotel_search_response_200_output_properties_item.additional_properties = d
        return hotel_search_response_200_output_properties_item

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
