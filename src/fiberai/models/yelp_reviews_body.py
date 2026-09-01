from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.yelp_reviews_body_sort_by_type_1 import YelpReviewsBodySortByType1
from ..models.yelp_reviews_body_sort_by_type_2_type_1 import YelpReviewsBodySortByType2Type1
from ..models.yelp_reviews_body_sort_by_type_3_type_1 import YelpReviewsBodySortByType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="YelpReviewsBody")


@_attrs_define
class YelpReviewsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        place_id (str): Yelp business ID (e.g. 'U5hCNNyJmb7f3dmC1HTzSQ'). Obtain it from the `placeId` of a result
            returned by the Yelp search endpoint (`POST /v1/yelp/search`).
        sort_by (None | Unset | YelpReviewsBodySortByType1 | YelpReviewsBodySortByType2Type1 |
            YelpReviewsBodySortByType3Type1): Sort criterion for reviews. 'relevance' is the platform's default ranking.
            'elitesFirst' puts reviews from elite reviewers first. Omit to sort by relevance.
        ratings (list[int] | None | Unset): Only return reviews with these star ratings (e.g. [5] for five-star reviews
            only, [5, 4] for five- and four-star reviews). Omit (or pass []) to include all ratings.
        keywords (list[str] | None | Unset): Only return reviews whose text matches these keywords (e.g. ['crust',
            'delivery']). Omit (or pass []) to include all reviews.
        language_code (None | str | Unset): Language for review text (e.g. 'en', 'es', 'fr'). Omit for English.
        next_page_token (None | str | Unset): Pagination token from a prior reviews response's `nextPageToken`. Omit (or
            pass null) to fetch the first page.
    """

    api_key: str
    place_id: str
    sort_by: (
        None | Unset | YelpReviewsBodySortByType1 | YelpReviewsBodySortByType2Type1 | YelpReviewsBodySortByType3Type1
    ) = UNSET
    ratings: list[int] | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    language_code: None | str | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        place_id = self.place_id

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, YelpReviewsBodySortByType1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, YelpReviewsBodySortByType2Type1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, YelpReviewsBodySortByType3Type1):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

        ratings: list[int] | None | Unset
        if isinstance(self.ratings, Unset):
            ratings = UNSET
        elif isinstance(self.ratings, list):
            ratings = self.ratings

        else:
            ratings = self.ratings

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "placeId": place_id,
            }
        )
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        place_id = d.pop("placeId")

        def _parse_sort_by(
            data: object,
        ) -> (
            None
            | Unset
            | YelpReviewsBodySortByType1
            | YelpReviewsBodySortByType2Type1
            | YelpReviewsBodySortByType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_1 = YelpReviewsBodySortByType1(data)

                return sort_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_2_type_1 = YelpReviewsBodySortByType2Type1(data)

                return sort_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_3_type_1 = YelpReviewsBodySortByType3Type1(data)

                return sort_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | YelpReviewsBodySortByType1
                | YelpReviewsBodySortByType2Type1
                | YelpReviewsBodySortByType3Type1,
                data,
            )

        sort_by = _parse_sort_by(d.pop("sortBy", UNSET))

        def _parse_ratings(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ratings_type_0 = cast(list[int], data)

                return ratings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ratings = _parse_ratings(d.pop("ratings", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("languageCode", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        yelp_reviews_body = cls(
            api_key=api_key,
            place_id=place_id,
            sort_by=sort_by,
            ratings=ratings,
            keywords=keywords,
            language_code=language_code,
            next_page_token=next_page_token,
        )

        yelp_reviews_body.additional_properties = d
        return yelp_reviews_body

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
