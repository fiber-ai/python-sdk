from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_reviews_body_sort_by import GoogleMapsReviewsBodySortBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleMapsReviewsBody")


@_attrs_define
class GoogleMapsReviewsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        place_id (str): Google Maps place ID (e.g. 'ChIJN1t_tDeuEmsRUsoyG83frY4'). Obtain it from the `placeId` of a
            result returned by the Google Maps search endpoint (`POST /v1/google-maps/search`).
        sort_by (GoogleMapsReviewsBodySortBy | Unset): Sort criterion for reviews. Applies to the first page only: later
            pages keep the sort the first page used, so changing it mid-pagination has no effect. Default:
            GoogleMapsReviewsBodySortBy.RELEVANCE.
        next_page_token (None | str | Unset): Pagination token from a prior response's `nextPageToken`. Omit (or pass
            null) to fetch the first page.
    """

    api_key: str
    place_id: str
    sort_by: GoogleMapsReviewsBodySortBy | Unset = GoogleMapsReviewsBodySortBy.RELEVANCE
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        place_id = self.place_id

        sort_by: str | Unset = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

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
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        place_id = d.pop("placeId")

        _sort_by = d.pop("sortBy", UNSET)
        sort_by: GoogleMapsReviewsBodySortBy | Unset
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = GoogleMapsReviewsBodySortBy(_sort_by)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        google_maps_reviews_body = cls(
            api_key=api_key,
            place_id=place_id,
            sort_by=sort_by,
            next_page_token=next_page_token,
        )

        google_maps_reviews_body.additional_properties = d
        return google_maps_reviews_body

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
