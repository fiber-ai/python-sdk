from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.yelp_reviews_response_200_output_reviews_item import YelpReviewsResponse200OutputReviewsItem


T = TypeVar("T", bound="YelpReviewsResponse200Output")


@_attrs_define
class YelpReviewsResponse200Output:
    """
    Attributes:
        reviews (list[YelpReviewsResponse200OutputReviewsItem]): Reviews of the business.
        total_review_count (int | None | Unset): Total number of reviews for the business.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
    """

    reviews: list[YelpReviewsResponse200OutputReviewsItem]
    total_review_count: int | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

        total_review_count: int | None | Unset
        if isinstance(self.total_review_count, Unset):
            total_review_count = UNSET
        else:
            total_review_count = self.total_review_count

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviews": reviews,
            }
        )
        if total_review_count is not UNSET:
            field_dict["totalReviewCount"] = total_review_count
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.yelp_reviews_response_200_output_reviews_item import (
            YelpReviewsResponse200OutputReviewsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = YelpReviewsResponse200OutputReviewsItem.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        def _parse_total_review_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_review_count = _parse_total_review_count(d.pop("totalReviewCount", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        yelp_reviews_response_200_output = cls(
            reviews=reviews,
            total_review_count=total_review_count,
            next_page_token=next_page_token,
        )

        yelp_reviews_response_200_output.additional_properties = d
        return yelp_reviews_response_200_output

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
