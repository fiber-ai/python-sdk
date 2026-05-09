from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstagramUserPostsResponse200OutputPostsItem")


@_attrs_define
class InstagramUserPostsResponse200OutputPostsItem:
    """
    Attributes:
        id (str): Unique post identifier.
        is_video (bool): True if the post is a video or reel. False if it is an image.
        shortcode (None | str | Unset): Post shortcode — the unique identifier from the URL. For example, in
            'https://www.instagram.com/p/DVoDVg5DkXM/', the shortcode is 'DVoDVg5DkXM'.
        caption (None | str | Unset): Post caption text.
        like_count (float | None | Unset): Number of likes.
        comment_count (float | None | Unset): Number of comments.
        play_count (float | None | Unset): Number of plays or views (video/reel only).
        thumbnail_url (None | str | Unset): URL of the post image or video thumbnail.
        published_at (None | str | Unset): ISO 8601 timestamp of when the post was published.
    """

    id: str
    is_video: bool
    shortcode: None | str | Unset = UNSET
    caption: None | str | Unset = UNSET
    like_count: float | None | Unset = UNSET
    comment_count: float | None | Unset = UNSET
    play_count: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    published_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_video = self.is_video

        shortcode: None | str | Unset
        if isinstance(self.shortcode, Unset):
            shortcode = UNSET
        else:
            shortcode = self.shortcode

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

        play_count: float | None | Unset
        if isinstance(self.play_count, Unset):
            play_count = UNSET
        else:
            play_count = self.play_count

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isVideo": is_video,
            }
        )
        if shortcode is not UNSET:
            field_dict["shortcode"] = shortcode
        if caption is not UNSET:
            field_dict["caption"] = caption
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if play_count is not UNSET:
            field_dict["playCount"] = play_count
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_video = d.pop("isVideo")

        def _parse_shortcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shortcode = _parse_shortcode(d.pop("shortcode", UNSET))

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

        def _parse_play_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        play_count = _parse_play_count(d.pop("playCount", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        instagram_user_posts_response_200_output_posts_item = cls(
            id=id,
            is_video=is_video,
            shortcode=shortcode,
            caption=caption,
            like_count=like_count,
            comment_count=comment_count,
            play_count=play_count,
            thumbnail_url=thumbnail_url,
            published_at=published_at,
        )

        instagram_user_posts_response_200_output_posts_item.additional_properties = d
        return instagram_user_posts_response_200_output_posts_item

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
