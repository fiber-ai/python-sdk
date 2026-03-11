from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollGoogleMapsResultsBody")


@_attrs_define
class PollGoogleMapsResultsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        search_id (str): The ID of the Google Maps search. You should get this from the start endpoint.
        page_size (int | Unset): The number of results to return per page. Default: 25.
        cursor (None | str | Unset): A pagination cursor returned from a previous search response. Use this to fetch the
            next page of results. If this is null, then the first page of results will be returned.
    """

    api_key: str
    search_id: str
    page_size: int | Unset = 25
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        search_id = self.search_id

        page_size = self.page_size

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "searchID": search_id,
            }
        )
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        search_id = d.pop("searchID")

        page_size = d.pop("pageSize", UNSET)

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        poll_google_maps_results_body = cls(
            api_key=api_key,
            search_id=search_id,
            page_size=page_size,
            cursor=cursor,
        )

        poll_google_maps_results_body.additional_properties = d
        return poll_google_maps_results_body

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
