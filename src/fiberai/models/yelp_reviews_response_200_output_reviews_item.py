from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YelpReviewsResponse200OutputReviewsItem")


@_attrs_define
class YelpReviewsResponse200OutputReviewsItem:
    """
    Attributes:
        rating (int): Star rating given by the reviewer, from 1 to 5.
        photo_urls (list[str]): Photo URLs attached to the review.
        author_name (None | str | Unset): Reviewer's display name.
        author_location (None | str | Unset): Reviewer's location (e.g. 'Austin, TX').
        author_is_elite (bool | None | Unset): True when the reviewer has elite status on Yelp.
        date (None | str | Unset): Review date in ISO 8601 format.
        text (None | str | Unset): Review text.
        language_code (None | str | Unset): Language of the review text (e.g. 'en').
        useful_count (int | None | Unset): Number of 'useful' votes the review received.
        funny_count (int | None | Unset): Number of 'funny' votes the review received.
        cool_count (int | None | Unset): Number of 'cool' votes the review received.
    """

    rating: int
    photo_urls: list[str]
    author_name: None | str | Unset = UNSET
    author_location: None | str | Unset = UNSET
    author_is_elite: bool | None | Unset = UNSET
    date: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    language_code: None | str | Unset = UNSET
    useful_count: int | None | Unset = UNSET
    funny_count: int | None | Unset = UNSET
    cool_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating = self.rating

        photo_urls = self.photo_urls

        author_name: None | str | Unset
        if isinstance(self.author_name, Unset):
            author_name = UNSET
        else:
            author_name = self.author_name

        author_location: None | str | Unset
        if isinstance(self.author_location, Unset):
            author_location = UNSET
        else:
            author_location = self.author_location

        author_is_elite: bool | None | Unset
        if isinstance(self.author_is_elite, Unset):
            author_is_elite = UNSET
        else:
            author_is_elite = self.author_is_elite

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        useful_count: int | None | Unset
        if isinstance(self.useful_count, Unset):
            useful_count = UNSET
        else:
            useful_count = self.useful_count

        funny_count: int | None | Unset
        if isinstance(self.funny_count, Unset):
            funny_count = UNSET
        else:
            funny_count = self.funny_count

        cool_count: int | None | Unset
        if isinstance(self.cool_count, Unset):
            cool_count = UNSET
        else:
            cool_count = self.cool_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rating": rating,
                "photoUrls": photo_urls,
            }
        )
        if author_name is not UNSET:
            field_dict["authorName"] = author_name
        if author_location is not UNSET:
            field_dict["authorLocation"] = author_location
        if author_is_elite is not UNSET:
            field_dict["authorIsElite"] = author_is_elite
        if date is not UNSET:
            field_dict["date"] = date
        if text is not UNSET:
            field_dict["text"] = text
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if useful_count is not UNSET:
            field_dict["usefulCount"] = useful_count
        if funny_count is not UNSET:
            field_dict["funnyCount"] = funny_count
        if cool_count is not UNSET:
            field_dict["coolCount"] = cool_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rating = d.pop("rating")

        photo_urls = cast(list[str], d.pop("photoUrls"))

        def _parse_author_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_name = _parse_author_name(d.pop("authorName", UNSET))

        def _parse_author_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_location = _parse_author_location(d.pop("authorLocation", UNSET))

        def _parse_author_is_elite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        author_is_elite = _parse_author_is_elite(d.pop("authorIsElite", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("languageCode", UNSET))

        def _parse_useful_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        useful_count = _parse_useful_count(d.pop("usefulCount", UNSET))

        def _parse_funny_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funny_count = _parse_funny_count(d.pop("funnyCount", UNSET))

        def _parse_cool_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cool_count = _parse_cool_count(d.pop("coolCount", UNSET))

        yelp_reviews_response_200_output_reviews_item = cls(
            rating=rating,
            photo_urls=photo_urls,
            author_name=author_name,
            author_location=author_location,
            author_is_elite=author_is_elite,
            date=date,
            text=text,
            language_code=language_code,
            useful_count=useful_count,
            funny_count=funny_count,
            cool_count=cool_count,
        )

        yelp_reviews_response_200_output_reviews_item.additional_properties = d
        return yelp_reviews_response_200_output_reviews_item

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
