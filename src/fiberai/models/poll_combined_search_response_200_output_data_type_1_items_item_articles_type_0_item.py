from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType1ItemsItemArticlesType0Item")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType1ItemsItemArticlesType0Item:
    """
    Attributes:
        id (None | str | Unset):
        title (None | str | Unset):
        date_published (None | str | Unset):
    """

    id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    date_published: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        date_published: None | str | Unset
        if isinstance(self.date_published, Unset):
            date_published = UNSET
        else:
            date_published = self.date_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if date_published is not UNSET:
            field_dict["date_published"] = date_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_date_published(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_published = _parse_date_published(d.pop("date_published", UNSET))

        poll_combined_search_response_200_output_data_type_1_items_item_articles_type_0_item = cls(
            id=id,
            title=title,
            date_published=date_published,
        )

        poll_combined_search_response_200_output_data_type_1_items_item_articles_type_0_item.additional_properties = d
        return poll_combined_search_response_200_output_data_type_1_items_item_articles_type_0_item

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
