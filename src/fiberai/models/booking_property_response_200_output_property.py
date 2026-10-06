from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_property_response_200_output_property_coordinates_type_0 import (
        BookingPropertyResponse200OutputPropertyCoordinatesType0,
    )
    from ..models.booking_property_response_200_output_property_house_rules_type_0 import (
        BookingPropertyResponse200OutputPropertyHouseRulesType0,
    )
    from ..models.booking_property_response_200_output_property_score_breakdown_type_0 import (
        BookingPropertyResponse200OutputPropertyScoreBreakdownType0,
    )


T = TypeVar("T", bound="BookingPropertyResponse200OutputProperty")


@_attrs_define
class BookingPropertyResponse200OutputProperty:
    """Full property details including amenities, photos, and house rules.

    Attributes:
        property_id (str): Booking.com property identifier.
        name (str): Property display name.
        property_url (str): Full Booking.com property URL. Pass as `propertyUrl` in POST /v1/booking/property.
        amenities (list[str]): Amenities offered by this property.
        photo_urls (list[str]): Property photo URLs.
        languages_spoken (list[str]): BCP-47 language tags for the languages property staff speak (e.g. ['en', 'hr',
            'pt-BR']).
        address (None | str | Unset): Street address.
        city (None | str | Unset): City name.
        district (None | str | Unset): District or neighborhood.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA').
        coordinates (BookingPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset): Geographic coordinates of
            the property in decimal degrees.
        hotel_star_class (int | None | Unset): Hotel star class from 1 to 5, indicating how upscale the property is.
            This is a property classification, not a guest review score.
        review_score (float | None | Unset): Guest review score from 0 to 10.
        review_count (int | None | Unset): Total number of guest reviews.
        thumbnail_url (None | str | Unset): Thumbnail image URL.
        is_preferred (bool | None | Unset): True when the property belongs to Booking.com's Preferred Partner programme,
            which promotes it in Booking.com's own result ranking.
        description (None | str | Unset): Property description.
        accommodation_type (None | str | Unset): Accommodation type (e.g. 'hotel', 'guestHouse').
        check_in_time (None | str | Unset): Check-in time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '15:00').
        check_out_time (None | str | Unset): Check-out time in 24-hour `HH:mm` format, where `HH` is 00 through 23 (e.g.
            '11:00').
        score_breakdown (BookingPropertyResponse200OutputPropertyScoreBreakdownType0 | None | Unset): Guest review
            scores by category, each from 0 to 10.
        house_rules (BookingPropertyResponse200OutputPropertyHouseRulesType0 | None | Unset): Published house rules for
            the property.
        is_sustainable (bool | None | Unset): True when the property is marked as a sustainable stay.
    """

    property_id: str
    name: str
    property_url: str
    amenities: list[str]
    photo_urls: list[str]
    languages_spoken: list[str]
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    coordinates: BookingPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset = UNSET
    hotel_star_class: int | None | Unset = UNSET
    review_score: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    is_preferred: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    accommodation_type: None | str | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    score_breakdown: BookingPropertyResponse200OutputPropertyScoreBreakdownType0 | None | Unset = UNSET
    house_rules: BookingPropertyResponse200OutputPropertyHouseRulesType0 | None | Unset = UNSET
    is_sustainable: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_property_response_200_output_property_coordinates_type_0 import (
            BookingPropertyResponse200OutputPropertyCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.booking_property_response_200_output_property_house_rules_type_0 import (
            BookingPropertyResponse200OutputPropertyHouseRulesType0,  # noqa: PLC0415
        )
        from ..models.booking_property_response_200_output_property_score_breakdown_type_0 import (
            BookingPropertyResponse200OutputPropertyScoreBreakdownType0,  # noqa: PLC0415
        )

        property_id = self.property_id

        name = self.name

        property_url = self.property_url

        amenities = self.amenities

        photo_urls = self.photo_urls

        languages_spoken = self.languages_spoken

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
        elif isinstance(self.coordinates, BookingPropertyResponse200OutputPropertyCoordinatesType0):
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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        accommodation_type: None | str | Unset
        if isinstance(self.accommodation_type, Unset):
            accommodation_type = UNSET
        else:
            accommodation_type = self.accommodation_type

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

        score_breakdown: dict[str, Any] | None | Unset
        if isinstance(self.score_breakdown, Unset):
            score_breakdown = UNSET
        elif isinstance(self.score_breakdown, BookingPropertyResponse200OutputPropertyScoreBreakdownType0):
            score_breakdown = self.score_breakdown.to_dict()
        else:
            score_breakdown = self.score_breakdown

        house_rules: dict[str, Any] | None | Unset
        if isinstance(self.house_rules, Unset):
            house_rules = UNSET
        elif isinstance(self.house_rules, BookingPropertyResponse200OutputPropertyHouseRulesType0):
            house_rules = self.house_rules.to_dict()
        else:
            house_rules = self.house_rules

        is_sustainable: bool | None | Unset
        if isinstance(self.is_sustainable, Unset):
            is_sustainable = UNSET
        else:
            is_sustainable = self.is_sustainable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyId": property_id,
                "name": name,
                "propertyUrl": property_url,
                "amenities": amenities,
                "photoUrls": photo_urls,
                "languagesSpoken": languages_spoken,
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
        if description is not UNSET:
            field_dict["description"] = description
        if accommodation_type is not UNSET:
            field_dict["accommodationType"] = accommodation_type
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if score_breakdown is not UNSET:
            field_dict["scoreBreakdown"] = score_breakdown
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if is_sustainable is not UNSET:
            field_dict["isSustainable"] = is_sustainable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_property_response_200_output_property_coordinates_type_0 import (
            BookingPropertyResponse200OutputPropertyCoordinatesType0,  # noqa: PLC0415
        )
        from ..models.booking_property_response_200_output_property_house_rules_type_0 import (
            BookingPropertyResponse200OutputPropertyHouseRulesType0,  # noqa: PLC0415
        )
        from ..models.booking_property_response_200_output_property_score_breakdown_type_0 import (
            BookingPropertyResponse200OutputPropertyScoreBreakdownType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        property_id = d.pop("propertyId")

        name = d.pop("name")

        property_url = d.pop("propertyUrl")

        amenities = cast(list[str], d.pop("amenities"))

        photo_urls = cast(list[str], d.pop("photoUrls"))

        languages_spoken = cast(list[str], d.pop("languagesSpoken"))

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

        def _parse_coordinates(data: object) -> BookingPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = BookingPropertyResponse200OutputPropertyCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingPropertyResponse200OutputPropertyCoordinatesType0 | None | Unset, data)

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_accommodation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accommodation_type = _parse_accommodation_type(d.pop("accommodationType", UNSET))

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

        def _parse_score_breakdown(
            data: object,
        ) -> BookingPropertyResponse200OutputPropertyScoreBreakdownType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_0 = BookingPropertyResponse200OutputPropertyScoreBreakdownType0.from_dict(data)

                return score_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingPropertyResponse200OutputPropertyScoreBreakdownType0 | None | Unset, data)

        score_breakdown = _parse_score_breakdown(d.pop("scoreBreakdown", UNSET))

        def _parse_house_rules(data: object) -> BookingPropertyResponse200OutputPropertyHouseRulesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                house_rules_type_0 = BookingPropertyResponse200OutputPropertyHouseRulesType0.from_dict(data)

                return house_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BookingPropertyResponse200OutputPropertyHouseRulesType0 | None | Unset, data)

        house_rules = _parse_house_rules(d.pop("houseRules", UNSET))

        def _parse_is_sustainable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_sustainable = _parse_is_sustainable(d.pop("isSustainable", UNSET))

        booking_property_response_200_output_property = cls(
            property_id=property_id,
            name=name,
            property_url=property_url,
            amenities=amenities,
            photo_urls=photo_urls,
            languages_spoken=languages_spoken,
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
            description=description,
            accommodation_type=accommodation_type,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            score_breakdown=score_breakdown,
            house_rules=house_rules,
            is_sustainable=is_sustainable,
        )

        booking_property_response_200_output_property.additional_properties = d
        return booking_property_response_200_output_property

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
