from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.youtube_video_comments_response_200_output_comments_item_published_at_type_0 import (
        YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0,
    )


T = TypeVar("T", bound="YoutubeVideoCommentsResponse200OutputCommentsItem")


@_attrs_define
class YoutubeVideoCommentsResponse200OutputCommentsItem:
    """
    Attributes:
        id (None | str | Unset): Unique identifier for this comment.
        text (None | str | Unset): Comment text.
        like_count (float | None | Unset): Number of likes on this comment.
        author (None | str | Unset): Comment author display name.
        published_at (None | Unset | YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0): Publication
            date. When YouTube only provides approximate time (e.g. '2 years ago'), we estimate the date and set `estimated:
            true`.
        reply_count (float | None | Unset): Number of replies to this comment.
    """

    id: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    like_count: float | None | Unset = UNSET
    author: None | str | Unset = UNSET
    published_at: None | Unset | YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0 = UNSET
    reply_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.youtube_video_comments_response_200_output_comments_item_published_at_type_0 import (
            YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0,  # noqa: PLC0415
        )

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        like_count: float | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        published_at: dict[str, Any] | None | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0):
            published_at = self.published_at.to_dict()
        else:
            published_at = self.published_at

        reply_count: float | None | Unset
        if isinstance(self.reply_count, Unset):
            reply_count = UNSET
        else:
            reply_count = self.reply_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if author is not UNSET:
            field_dict["author"] = author
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_video_comments_response_200_output_comments_item_published_at_type_0 import (
            YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_published_at(
            data: object,
        ) -> None | Unset | YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                published_at_type_0 = YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0.from_dict(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_reply_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reply_count = _parse_reply_count(d.pop("replyCount", UNSET))

        youtube_video_comments_response_200_output_comments_item = cls(
            id=id,
            text=text,
            like_count=like_count,
            author=author,
            published_at=published_at,
            reply_count=reply_count,
        )

        youtube_video_comments_response_200_output_comments_item.additional_properties = d
        return youtube_video_comments_response_200_output_comments_item

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
