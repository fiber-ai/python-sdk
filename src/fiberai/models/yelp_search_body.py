from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.yelp_search_body_sort_by_type_1 import YelpSearchBodySortByType1
from ..models.yelp_search_body_sort_by_type_2_type_1 import YelpSearchBodySortByType2Type1
from ..models.yelp_search_body_sort_by_type_3_type_1 import YelpSearchBodySortByType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="YelpSearchBody")


@_attrs_define
class YelpSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        location (str): Where to search. Accepts a city and state ('Austin, TX'), a full address ('706 Mission St, San
            Francisco, CA'), or a ZIP code ('94103').
        categories (list[str] | None | Unset): Categories or terms to search for (e.g. ['pizza', 'italian'] or ['coffee
            shop']). A business name ('Sushi Ran') also works as a term. Omit (or pass []) to browse all businesses in the
            location.
        sort_by (None | Unset | YelpSearchBodySortByType1 | YelpSearchBodySortByType2Type1 |
            YelpSearchBodySortByType3Type1): Sort criterion for results. 'relevance' ranks by overall match. 'highestRated'
            sorts by rating. 'mostReviewed' sorts by review count. Omit to sort by relevance.
        next_page_token (None | str | Unset): Pagination token from a prior search response's `nextPageToken`. Omit (or
            pass null) to fetch the first page.
    """

    api_key: str
    location: str
    categories: list[str] | None | Unset = UNSET
    sort_by: (
        None | Unset | YelpSearchBodySortByType1 | YelpSearchBodySortByType2Type1 | YelpSearchBodySortByType3Type1
    ) = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        location = self.location

        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, YelpSearchBodySortByType1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, YelpSearchBodySortByType2Type1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, YelpSearchBodySortByType3Type1):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

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
                "location": location,
            }
        )
        if categories is not UNSET:
            field_dict["categories"] = categories
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        location = d.pop("location")

        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_sort_by(
            data: object,
        ) -> None | Unset | YelpSearchBodySortByType1 | YelpSearchBodySortByType2Type1 | YelpSearchBodySortByType3Type1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_1 = YelpSearchBodySortByType1(data)

                return sort_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_2_type_1 = YelpSearchBodySortByType2Type1(data)

                return sort_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_3_type_1 = YelpSearchBodySortByType3Type1(data)

                return sort_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | YelpSearchBodySortByType1
                | YelpSearchBodySortByType2Type1
                | YelpSearchBodySortByType3Type1,
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

        yelp_search_body = cls(
            api_key=api_key,
            location=location,
            categories=categories,
            sort_by=sort_by,
            next_page_token=next_page_token,
        )

        yelp_search_body.additional_properties = d
        return yelp_search_body

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
