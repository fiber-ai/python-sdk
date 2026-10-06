from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_search_response_200_output_properties_item_coordinates_type_0 import (
        BookingSearchResponse200OutputPropertiesItemCoordinatesType0,
    )
    from ..models.booking_search_response_200_output_properties_item_nightly_price_type_0 import (
        BookingSearchResponse200OutputPropertiesItemNightlyPriceType0,
    )
    from ..models.booking_search_response_200_output_properties_item_original_price_type_0 import (
        BookingSearchResponse200OutputPropertiesItemOriginalPriceType0,
    )
    from ..models.booking_search_response_200_output_properties_item_total_price_type_0 import (
        BookingSearchResponse200OutputPropertiesItemTotalPriceType0,
    )


T = TypeVar("T", bound="BookingSearchResponse200OutputPropertiesItem")


@_attrs_define
class BookingSearchResponse200OutputPropertiesItem:
    """
    Attributes:
        property_id (str): Booking.com property identifier.
        name (str): Property display name.
        property_url (str): Full Booking.com property URL. Pass as `propertyUrl` in POST /v1/booking/property.
        address (None | str | Unset): Street address.
        city (None | str | Unset): City name.
        district (None | str | Unset): District or neighborhood.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA').
        coordinates (BookingSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset): Geographic
            coordinates of the property in decimal degrees.
        hotel_star_class (int | None | Unset): Hotel star class from 1 to 5, indicating how upscale the property is.
            This is a property classification, not a guest review score.
        review_score (float | None | Unset): Guest review score from 0 to 10.
        review_count (int | None | Unset): Total number of guest reviews.
        thumbnail_url (None | str | Unset): Thumbnail image URL.
        is_preferred (bool | None | Unset): True when the property belongs to Booking.com's Preferred Partner programme,
            which promotes it in Booking.com's own result ranking.
        total_price (BookingSearchResponse200OutputPropertiesItemTotalPriceType0 | None | Unset): Total price for the
            requested stay. Null when Booking.com shows no rate for these dates, for example when the property is sold out.
        nightly_price (BookingSearchResponse200OutputPropertiesItemNightlyPriceType0 | None | Unset): Average nightly
            price for the requested stay.
        original_price (BookingSearchResponse200OutputPropertiesItemOriginalPriceType0 | None | Unset): List price
            before discounts, when a promotion applies.
        has_free_cancellation (bool | None | Unset): True when the listed rate includes free cancellation.
        is_sold_out (bool | None | Unset): True when the property has no remaining availability for the requested dates.
        meal_plan (None | str | Unset): Meal plan included with the listed rate, as Booking.com publishes it (e.g.
            'Breakfast included').
    """

    property_id: str
    name: str
    property_url: str
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    coordinates: BookingSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset = UNSET
    hotel_star_class: int | None | Unset = UNSET
    review_score: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    is_preferred: bool | None | Unset = UNSET
    total_price: BookingSearchResponse200OutputPropertiesItemTotalPriceType0 | None | Unset = UNSET
    nightly_price: BookingSearchResponse200OutputPropertiesItemNightlyPriceType0 | None | Unset = UNSET
    original_price: BookingSearchResponse200OutputPropertiesItemOriginalPriceType0 | None | Unset = UNSET
    has_free_cancellation: bool | None | Unset = UNSET
    is_sold_out: bool | None | Unset = UNSET
    meal_plan: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_search_response_200_output_properties_item_coordinates_type_0 import (
            BookingSearchResponse200OutputPropertiesItemCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_nightly_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemNightlyPriceType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_original_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemOriginalPriceType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_total_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemTotalPriceType0,  # noqa: PLC0415
        )

        property_id = self.property_id

        name = self.name

        property_url = self.property_url

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, BookingSearchResponse200OutputPropertiesItemCoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        hotel_star_class: int | None | Unset
        if isinstance(self.hotel_star_class, Unset):
            hotel_star_class = UNSET
        else:
            hotel_star_class = self.hotel_star_class

        review_score: float | None | Unset
        if isinstance(self.review_score, Unset):
            review_score = UNSET
        else:
            review_score = self.review_score

        review_count: int | None | Unset
        if isinstance(self.review_count, Unset):
            review_count = UNSET
        else:
            review_count = self.review_count

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        is_preferred: bool | None | Unset
        if isinstance(self.is_preferred, Unset):
            is_preferred = UNSET
        else:
            is_preferred = self.is_preferred

        total_price: dict[str, Any] | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        elif isinstance(self.total_price, BookingSearchResponse200OutputPropertiesItemTotalPriceType0):
            total_price = self.total_price.to_dict()
        else:
            total_price = self.total_price

        nightly_price: dict[str, Any] | None | Unset
        if isinstance(self.nightly_price, Unset):
            nightly_price = UNSET
        elif isinstance(self.nightly_price, BookingSearchResponse200OutputPropertiesItemNightlyPriceType0):
            nightly_price = self.nightly_price.to_dict()
        else:
            nightly_price = self.nightly_price

        original_price: dict[str, Any] | None | Unset
        if isinstance(self.original_price, Unset):
            original_price = UNSET
        elif isinstance(self.original_price, BookingSearchResponse200OutputPropertiesItemOriginalPriceType0):
            original_price = self.original_price.to_dict()
        else:
            original_price = self.original_price

        has_free_cancellation: bool | None | Unset
        if isinstance(self.has_free_cancellation, Unset):
            has_free_cancellation = UNSET
        else:
            has_free_cancellation = self.has_free_cancellation

        is_sold_out: bool | None | Unset
        if isinstance(self.is_sold_out, Unset):
            is_sold_out = UNSET
        else:
            is_sold_out = self.is_sold_out

        meal_plan: None | str | Unset
        if isinstance(self.meal_plan, Unset):
            meal_plan = UNSET
        else:
            meal_plan = self.meal_plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyId": property_id,
                "name": name,
                "propertyUrl": property_url,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if district is not UNSET:
            field_dict["district"] = district
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if hotel_star_class is not UNSET:
            field_dict["hotelStarClass"] = hotel_star_class
        if review_score is not UNSET:
            field_dict["reviewScore"] = review_score
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if is_preferred is not UNSET:
            field_dict["isPreferred"] = is_preferred
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if nightly_price is not UNSET:
            field_dict["nightlyPrice"] = nightly_price
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if has_free_cancellation is not UNSET:
            field_dict["hasFreeCancellation"] = has_free_cancellation
        if is_sold_out is not UNSET:
            field_dict["isSoldOut"] = is_sold_out
        if meal_plan is not UNSET:
            field_dict["mealPlan"] = meal_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_search_response_200_output_properties_item_coordinates_type_0 import (
            BookingSearchResponse200OutputPropertiesItemCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_nightly_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemNightlyPriceType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_original_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemOriginalPriceType0,  # noqa: PLC0415
        )
        from ..models.booking_search_response_200_output_properties_item_total_price_type_0 import (
            BookingSearchResponse200OutputPropertiesItemTotalPriceType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        property_id = d.pop("propertyId")

        name = d.pop("name")

        property_url = d.pop("propertyUrl")

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_coordinates(
            data: object,
        ) -> BookingSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = BookingSearchResponse200OutputPropertiesItemCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingSearchResponse200OutputPropertiesItemCoordinatesType0 | None | Unset, data)

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_hotel_star_class(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hotel_star_class = _parse_hotel_star_class(d.pop("hotelStarClass", UNSET))

        def _parse_review_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        review_score = _parse_review_score(d.pop("reviewScore", UNSET))

        def _parse_review_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        review_count = _parse_review_count(d.pop("reviewCount", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_is_preferred(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_preferred = _parse_is_preferred(d.pop("isPreferred", UNSET))

        def _parse_total_price(
            data: object,
        ) -> BookingSearchResponse200OutputPropertiesItemTotalPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_price_type_0 = BookingSearchResponse200OutputPropertiesItemTotalPriceType0.from_dict(data)

                return total_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingSearchResponse200OutputPropertiesItemTotalPriceType0 | None | Unset, data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))

        def _parse_nightly_price(
            data: object,
        ) -> BookingSearchResponse200OutputPropertiesItemNightlyPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nightly_price_type_0 = BookingSearchResponse200OutputPropertiesItemNightlyPriceType0.from_dict(data)

                return nightly_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingSearchResponse200OutputPropertiesItemNightlyPriceType0 | None | Unset, data)

        nightly_price = _parse_nightly_price(d.pop("nightlyPrice", UNSET))

        def _parse_original_price(
            data: object,
        ) -> BookingSearchResponse200OutputPropertiesItemOriginalPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                original_price_type_0 = BookingSearchResponse200OutputPropertiesItemOriginalPriceType0.from_dict(data)

                return original_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingSearchResponse200OutputPropertiesItemOriginalPriceType0 | None | Unset, data)

        original_price = _parse_original_price(d.pop("originalPrice", UNSET))

        def _parse_has_free_cancellation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_free_cancellation = _parse_has_free_cancellation(d.pop("hasFreeCancellation", UNSET))

        def _parse_is_sold_out(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_sold_out = _parse_is_sold_out(d.pop("isSoldOut", UNSET))

        def _parse_meal_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meal_plan = _parse_meal_plan(d.pop("mealPlan", UNSET))

        booking_search_response_200_output_properties_item = cls(
            property_id=property_id,
            name=name,
            property_url=property_url,
            address=address,
            city=city,
            district=district,
            country_code=country_code,
            coordinates=coordinates,
            hotel_star_class=hotel_star_class,
            review_score=review_score,
            review_count=review_count,
            thumbnail_url=thumbnail_url,
            is_preferred=is_preferred,
            total_price=total_price,
            nightly_price=nightly_price,
            original_price=original_price,
            has_free_cancellation=has_free_cancellation,
            is_sold_out=is_sold_out,
            meal_plan=meal_plan,
        )

        booking_search_response_200_output_properties_item.additional_properties = d
        return booking_search_response_200_output_properties_item

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
