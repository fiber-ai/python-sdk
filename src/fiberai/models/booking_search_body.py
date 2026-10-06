from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.booking_search_body_sort_by_type_1 import BookingSearchBodySortByType1
from ..models.booking_search_body_sort_by_type_2_type_1 import BookingSearchBodySortByType2Type1
from ..models.booking_search_body_sort_by_type_3_type_1 import BookingSearchBodySortByType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingSearchBody")


@_attrs_define
class BookingSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        query (str): Destination to search (city, region, or landmark). For example, 'Dubrovnik' or 'Rome, Italy'.
        check_in_date (str): Check-in date for the stay.
        check_out_date (str): Check-out date for the stay. Must be at least one calendar day after `checkInDate`.
        hotel_star_classes (list[int] | None | Unset): Filter to specific hotel star classes. This is a list of exact
            classes, not a range: [3, 5] returns only 3- and 5-star properties and excludes 4-star, so list every class you
            want (e.g. [3, 4, 5]).
        sort_by (BookingSearchBodySortByType1 | BookingSearchBodySortByType2Type1 | BookingSearchBodySortByType3Type1 |
            None | Unset): Sort criterion for results. 'relevance' ranks by overall match. 'lowestPrice' sorts cheapest
            first. 'highestRating' sorts by guest review score. 'mostReviewed' uses Booking.com's top-reviewed ranking,
            which weighs review score by review volume. Omit to sort by relevance.
        next_page_token (None | str | Unset): Opaque pagination token from a prior search response's `nextPageToken`.
            Send it with the same search parameters that produced it. Omit (or pass null) to fetch the first page.
        adults (int | Unset): Number of adult guests (at least 1). Total guests (`adults` + `children`) must not exceed
            30. Default: 2.
        children (int | Unset): Number of child guests. Total guests (`adults` + `children`) must not exceed 30.
            Default: 0.
        children_ages (list[int] | Unset): Ages of each child guest. Must contain exactly `children` entries when
            `children` is greater than zero.
        rooms (int | Unset): Number of rooms to search for. Defaults to 1. Default: 1.
        currency_code (str | Unset): ISO 4217 currency code for prices in the response (e.g. 'EUR', 'GBP', 'CAD'). Case-
            insensitive. Defaults to USD. Default: 'USD'.
        language_code (None | str | Unset): Language for property names, descriptions, and labels. Pass a BCP-47
            language tag such as 'en', 'en-US', 'fr', 'de', or 'es'. Omit for English.
    """

    api_key: str
    query: str
    check_in_date: str
    check_out_date: str
    hotel_star_classes: list[int] | None | Unset = UNSET
    sort_by: (
        BookingSearchBodySortByType1
        | BookingSearchBodySortByType2Type1
        | BookingSearchBodySortByType3Type1
        | None
        | Unset
    ) = UNSET
    next_page_token: None | str | Unset = UNSET
    adults: int | Unset = 2
    children: int | Unset = 0
    children_ages: list[int] | Unset = UNSET
    rooms: int | Unset = 1
    currency_code: str | Unset = "USD"
    language_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query = self.query

        check_in_date = self.check_in_date

        check_out_date = self.check_out_date

        hotel_star_classes: list[int] | None | Unset
        if isinstance(self.hotel_star_classes, Unset):
            hotel_star_classes = UNSET
        elif isinstance(self.hotel_star_classes, list):
            hotel_star_classes = self.hotel_star_classes

        else:
            hotel_star_classes = self.hotel_star_classes

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, BookingSearchBodySortByType1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, BookingSearchBodySortByType2Type1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, BookingSearchBodySortByType3Type1):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        adults = self.adults

        children = self.children

        children_ages: list[int] | Unset = UNSET
        if not isinstance(self.children_ages, Unset):
            children_ages = self.children_ages

        rooms = self.rooms

        currency_code = self.currency_code

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "query": query,
                "checkInDate": check_in_date,
                "checkOutDate": check_out_date,
            }
        )
        if hotel_star_classes is not UNSET:
            field_dict["hotelStarClasses"] = hotel_star_classes
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if children_ages is not UNSET:
            field_dict["childrenAges"] = children_ages
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        check_in_date = d.pop("checkInDate")

        check_out_date = d.pop("checkOutDate")

        def _parse_hotel_star_classes(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hotel_star_classes_type_0 = cast(list[int], data)

                return hotel_star_classes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        hotel_star_classes = _parse_hotel_star_classes(d.pop("hotelStarClasses", UNSET))

        def _parse_sort_by(
            data: object,
        ) -> (
            BookingSearchBodySortByType1
            | BookingSearchBodySortByType2Type1
            | BookingSearchBodySortByType3Type1
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
                sort_by_type_1 = BookingSearchBodySortByType1(data)

                return sort_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_2_type_1 = BookingSearchBodySortByType2Type1(data)

                return sort_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_3_type_1 = BookingSearchBodySortByType3Type1(data)

                return sort_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BookingSearchBodySortByType1
                | BookingSearchBodySortByType2Type1
                | BookingSearchBodySortByType3Type1
                | None
                | Unset,
                data,
            )

        sort_by = _parse_sort_by(d.pop("sortBy", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        adults = d.pop("adults", UNSET)

        children = d.pop("children", UNSET)

        children_ages = cast(list[int], d.pop("childrenAges", UNSET))

        rooms = d.pop("rooms", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("languageCode", UNSET))

        booking_search_body = cls(
            api_key=api_key,
            query=query,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            hotel_star_classes=hotel_star_classes,
            sort_by=sort_by,
            next_page_token=next_page_token,
            adults=adults,
            children=children,
            children_ages=children_ages,
            rooms=rooms,
            currency_code=currency_code,
            language_code=language_code,
        )

        booking_search_body.additional_properties = d
        return booking_search_body

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
