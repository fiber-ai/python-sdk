from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.youtube_channel_response_200_output_videos_item_published_at_type_0 import (
        YoutubeChannelResponse200OutputVideosItemPublishedAtType0,
    )


T = TypeVar("T", bound="YoutubeChannelResponse200OutputVideosItem")


@_attrs_define
class YoutubeChannelResponse200OutputVideosItem:
    """
    Attributes:
        id (str): YouTube video ID — the unique identifier found in the URL. For example, in
            'https://www.youtube.com/watch?v=094y1Z2wpJg', the video ID is '094y1Z2wpJg'.
        title (str): Video title.
        url (None | str | Unset): URL to the video.
        published_at (None | Unset | YoutubeChannelResponse200OutputVideosItemPublishedAtType0): Publication date. When
            YouTube only provides approximate time (e.g. '2 years ago'), we estimate the date and set `estimated: true`.
        view_count (float | None | Unset): Number of views.
        duration_seconds (float | None | Unset): Video duration in seconds.
        thumbnail_url (None | str | Unset): URL of the video thumbnail.
    """

    id: str
    title: str
    url: None | str | Unset = UNSET
    published_at: None | Unset | YoutubeChannelResponse200OutputVideosItemPublishedAtType0 = UNSET
    view_count: float | None | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.youtube_channel_response_200_output_videos_item_published_at_type_0 import (
            YoutubeChannelResponse200OutputVideosItemPublishedAtType0,  # noqa: PLC0415
        )

        id = self.id

        title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        published_at: dict[str, Any] | None | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, YoutubeChannelResponse200OutputVideosItemPublishedAtType0):
            published_at = self.published_at.to_dict()
        else:
            published_at = self.published_at

        view_count: float | None | Unset
        if isinstance(self.view_count, Unset):
            view_count = UNSET
        else:
            view_count = self.view_count

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

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
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_channel_response_200_output_videos_item_published_at_type_0 import (
            YoutubeChannelResponse200OutputVideosItemPublishedAtType0,  # noqa: PLC0415
        )

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

        def _parse_published_at(
            data: object,
        ) -> None | Unset | YoutubeChannelResponse200OutputVideosItemPublishedAtType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                published_at_type_0 = YoutubeChannelResponse200OutputVideosItemPublishedAtType0.from_dict(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | YoutubeChannelResponse200OutputVideosItemPublishedAtType0, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        youtube_channel_response_200_output_videos_item = cls(
            id=id,
            title=title,
            url=url,
            published_at=published_at,
            view_count=view_count,
            duration_seconds=duration_seconds,
            thumbnail_url=thumbnail_url,
        )

        youtube_channel_response_200_output_videos_item.additional_properties = d
        return youtube_channel_response_200_output_videos_item

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
