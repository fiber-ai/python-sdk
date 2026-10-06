from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleMapsPlaceResponse200OutputPlaceReviewsItem")


@_attrs_define
class GoogleMapsPlaceResponse200OutputPlaceReviewsItem:
    """
    Attributes:
        photo_urls (list[str]): Photo URLs attached to the review.
        author_name (None | str | Unset): Reviewer's display name.
        author_is_local_guide (bool | None | Unset): True when the reviewer is a Google Local Guide.
        rating (int | None | Unset): Star rating given by the reviewer, from 1 to 5.
        published_at (None | str | Unset): Review publication time in ISO 8601 format.
        text (None | str | Unset): Review text.
        like_count (int | None | Unset): Number of likes the review received.
        review_url (None | str | Unset): Public URL for this review.
    """

    photo_urls: list[str]
    author_name: None | str | Unset = UNSET
    author_is_local_guide: bool | None | Unset = UNSET
    rating: int | None | Unset = UNSET
    published_at: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    like_count: int | None | Unset = UNSET
    review_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo_urls = self.photo_urls

        author_name: None | str | Unset
        if isinstance(self.author_name, Unset):
            author_name = UNSET
        else:
            author_name = self.author_name

        author_is_local_guide: bool | None | Unset
        if isinstance(self.author_is_local_guide, Unset):
            author_is_local_guide = UNSET
        else:
            author_is_local_guide = self.author_is_local_guide

        rating: int | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        like_count: int | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        review_url: None | str | Unset
        if isinstance(self.review_url, Unset):
            review_url = UNSET
        else:
            review_url = self.review_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photoUrls": photo_urls,
            }
        )
        if author_name is not UNSET:
            field_dict["authorName"] = author_name
        if author_is_local_guide is not UNSET:
            field_dict["authorIsLocalGuide"] = author_is_local_guide
        if rating is not UNSET:
            field_dict["rating"] = rating
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if text is not UNSET:
            field_dict["text"] = text
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if review_url is not UNSET:
            field_dict["reviewUrl"] = review_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_urls = cast(list[str], d.pop("photoUrls"))

        def _parse_author_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_name = _parse_author_name(d.pop("authorName", UNSET))

        def _parse_author_is_local_guide(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        author_is_local_guide = _parse_author_is_local_guide(d.pop("authorIsLocalGuide", UNSET))

        def _parse_rating(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_like_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_review_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_url = _parse_review_url(d.pop("reviewUrl", UNSET))

        google_maps_place_response_200_output_place_reviews_item = cls(
            photo_urls=photo_urls,
            author_name=author_name,
            author_is_local_guide=author_is_local_guide,
            rating=rating,
            published_at=published_at,
            text=text,
            like_count=like_count,
            review_url=review_url,
        )

        google_maps_place_response_200_output_place_reviews_item.additional_properties = d
        return google_maps_place_response_200_output_place_reviews_item

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
