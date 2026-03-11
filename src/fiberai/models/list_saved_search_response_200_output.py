from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_saved_search_response_200_output_saved_searches_item import (
        ListSavedSearchResponse200OutputSavedSearchesItem,
    )


T = TypeVar("T", bound="ListSavedSearchResponse200Output")


@_attrs_define
class ListSavedSearchResponse200Output:
    """
    Attributes:
        saved_searches (list[ListSavedSearchResponse200OutputSavedSearchesItem]): The saved searches
        next_cursor (None | str | Unset): The next cursor. You can call this endpoint again with this cursor to get the
            next page of results. If null, there are no more results.
    """

    saved_searches: list[ListSavedSearchResponse200OutputSavedSearchesItem]
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        saved_searches = []
        for saved_searches_item_data in self.saved_searches:
            saved_searches_item = saved_searches_item_data.to_dict()
            saved_searches.append(saved_searches_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "savedSearches": saved_searches,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_saved_search_response_200_output_saved_searches_item import (
            ListSavedSearchResponse200OutputSavedSearchesItem,
        )

        d = dict(src_dict)
        saved_searches = []
        _saved_searches = d.pop("savedSearches")
        for saved_searches_item_data in _saved_searches:
            saved_searches_item = ListSavedSearchResponse200OutputSavedSearchesItem.from_dict(saved_searches_item_data)

            saved_searches.append(saved_searches_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        list_saved_search_response_200_output = cls(
            saved_searches=saved_searches,
            next_cursor=next_cursor,
        )

        list_saved_search_response_200_output.additional_properties = d
        return list_saved_search_response_200_output

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
