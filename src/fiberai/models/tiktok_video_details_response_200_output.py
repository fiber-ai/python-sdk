from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokVideoDetailsResponse200Output")


@_attrs_define
class TiktokVideoDetailsResponse200Output:
    """
    Attributes:
        id (None | str | Unset): Unique video identifier.
        caption (None | str | Unset): Video caption or description.
        like_count (float | None | Unset): Number of likes.
        comment_count (float | None | Unset): Number of comments.
        share_count (float | None | Unset): Number of shares.
        view_count (float | None | Unset): Number of views.
        duration_seconds (float | None | Unset): Video duration in seconds.
        thumbnail_url (None | str | Unset): URL of the video thumbnail.
        video_url (None | str | Unset): Direct URL to the TikTok video page.
        published_at (None | str | Unset): ISO 8601 timestamp of when the video was published.
    """

    id: None | str | Unset = UNSET
    caption: None | str | Unset = UNSET
    like_count: float | None | Unset = UNSET
    comment_count: float | None | Unset = UNSET
    share_count: float | None | Unset = UNSET
    view_count: float | None | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    published_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        like_count: float | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        comment_count: float | None | Unset
        if isinstance(self.comment_count, Unset):
            comment_count = UNSET
        else:
            comment_count = self.comment_count

        share_count: float | None | Unset
        if isinstance(self.share_count, Unset):
            share_count = UNSET
        else:
            share_count = self.share_count

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

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if caption is not UNSET:
            field_dict["caption"] = caption
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if share_count is not UNSET:
            field_dict["shareCount"] = share_count
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

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

        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_comment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        comment_count = _parse_comment_count(d.pop("commentCount", UNSET))

        def _parse_share_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        share_count = _parse_share_count(d.pop("shareCount", UNSET))

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

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("videoUrl", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        tiktok_video_details_response_200_output = cls(
            id=id,
            caption=caption,
            like_count=like_count,
            comment_count=comment_count,
            share_count=share_count,
            view_count=view_count,
            duration_seconds=duration_seconds,
            thumbnail_url=thumbnail_url,
            video_url=video_url,
            published_at=published_at,
        )

        tiktok_video_details_response_200_output.additional_properties = d
        return tiktok_video_details_response_200_output

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
