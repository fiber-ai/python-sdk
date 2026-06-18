from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListSavedSearchRunsBody")


@_attrs_define
class ListSavedSearchRunsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        saved_search_id (str): The ID of the saved search. Use /saved-search/list to get the ID of a saved search.
        cursor (None | str | Unset): The cursor to start from. You can pass null to get the first page of results.
        page_size (int | Unset): The number of runs to return Default: 100.
    """

    api_key: str
    saved_search_id: str
    cursor: None | str | Unset = UNSET
    page_size: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        saved_search_id = self.saved_search_id

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "savedSearchId": saved_search_id,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        saved_search_id = d.pop("savedSearchId")

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        page_size = d.pop("pageSize", UNSET)

        list_saved_search_runs_body = cls(
            api_key=api_key,
            saved_search_id=saved_search_id,
            cursor=cursor,
            page_size=page_size,
        )

        list_saved_search_runs_body.additional_properties = d
        return list_saved_search_runs_body

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
