from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeSearchResponse200OutputShortsItem")


@_attrs_define
class YoutubeSearchResponse200OutputShortsItem:
    """
    Attributes:
        id (str): YouTube video ID for this short — the unique identifier found in the URL. For example, in
            'https://www.youtube.com/shorts/gGtuw7Rejtk', the video ID is 'gGtuw7Rejtk'.
        title (str): Short title.
        url (None | str | Unset): URL to the short.
        view_count (float | None | Unset): Number of views.
        thumbnail_url (None | str | Unset): URL of the short thumbnail.
    """

    id: str
    title: str
    url: None | str | Unset = UNSET
    view_count: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        view_count: float | None | Unset
        if isinstance(self.view_count, Unset):
            view_count = UNSET
        else:
            view_count = self.view_count

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        youtube_search_response_200_output_shorts_item = cls(
            id=id,
            title=title,
            url=url,
            view_count=view_count,
            thumbnail_url=thumbnail_url,
        )

        youtube_search_response_200_output_shorts_item.additional_properties = d
        return youtube_search_response_200_output_shorts_item

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
