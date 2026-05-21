from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RedditPostCommentsResponse200OutputPostType0")


@_attrs_define
class RedditPostCommentsResponse200OutputPostType0:
    """Post metadata for the requested comment thread.

    Attributes:
        id (str): Stable Reddit post identifier (e.g. `ablzuq`). Use this as the primary key when storing posts in a
            database. Pass as `t3_<id>` to `/reddit/post/comments` to fetch comments for this post.
        title (None | str | Unset): Post title.
        author (None | str | Unset): Author username.
        subreddit (None | str | Unset): Subreddit name.
        body_text (None | str | Unset): Post body text.
        url (None | str | Unset): Content URL. For link posts this is the external URL the post points at; for text and
            media posts it is the post's permalink on Reddit.
        permalink (None | str | Unset): Reddit discussion URL. Always points at the post's comments page on reddit.com
            regardless of post type.
        score (float | None | Unset): Net vote score (upvotes minus downvotes, subject to Reddit vote fuzzing).
        upvote_ratio (float | None | Unset): Ratio of upvotes to total votes (0 to 1).
        comment_count (float | None | Unset): Number of comments.
        thumbnail_url (None | str | Unset): Thumbnail URL when available.
        published_at (None | str | Unset): Publication timestamp in ISO 8601 format.
        is_video (bool | None | Unset): True when the post contains video media.
        is_over_18 (bool | None | Unset): True when the post is marked NSFW.
        is_spoiler (bool | None | Unset): True when the post is marked as a spoiler.
    """

    id: str
    title: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    subreddit: None | str | Unset = UNSET
    body_text: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    permalink: None | str | Unset = UNSET
    score: float | None | Unset = UNSET
    upvote_ratio: float | None | Unset = UNSET
    comment_count: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    published_at: None | str | Unset = UNSET
    is_video: bool | None | Unset = UNSET
    is_over_18: bool | None | Unset = UNSET
    is_spoiler: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        subreddit: None | str | Unset
        if isinstance(self.subreddit, Unset):
            subreddit = UNSET
        else:
            subreddit = self.subreddit

        body_text: None | str | Unset
        if isinstance(self.body_text, Unset):
            body_text = UNSET
        else:
            body_text = self.body_text

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        permalink: None | str | Unset
        if isinstance(self.permalink, Unset):
            permalink = UNSET
        else:
            permalink = self.permalink

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        upvote_ratio: float | None | Unset
        if isinstance(self.upvote_ratio, Unset):
            upvote_ratio = UNSET
        else:
            upvote_ratio = self.upvote_ratio

        comment_count: float | None | Unset
        if isinstance(self.comment_count, Unset):
            comment_count = UNSET
        else:
            comment_count = self.comment_count

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

        is_video: bool | None | Unset
        if isinstance(self.is_video, Unset):
            is_video = UNSET
        else:
            is_video = self.is_video

        is_over_18: bool | None | Unset
        if isinstance(self.is_over_18, Unset):
            is_over_18 = UNSET
        else:
            is_over_18 = self.is_over_18

        is_spoiler: bool | None | Unset
        if isinstance(self.is_spoiler, Unset):
            is_spoiler = UNSET
        else:
            is_spoiler = self.is_spoiler

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author
        if subreddit is not UNSET:
            field_dict["subreddit"] = subreddit
        if body_text is not UNSET:
            field_dict["bodyText"] = body_text
        if url is not UNSET:
            field_dict["url"] = url
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if score is not UNSET:
            field_dict["score"] = score
        if upvote_ratio is not UNSET:
            field_dict["upvoteRatio"] = upvote_ratio
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if is_video is not UNSET:
            field_dict["isVideo"] = is_video
        if is_over_18 is not UNSET:
            field_dict["isOver18"] = is_over_18
        if is_spoiler is not UNSET:
            field_dict["isSpoiler"] = is_spoiler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_subreddit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subreddit = _parse_subreddit(d.pop("subreddit", UNSET))

        def _parse_body_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_text = _parse_body_text(d.pop("bodyText", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_permalink(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permalink = _parse_permalink(d.pop("permalink", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_upvote_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upvote_ratio = _parse_upvote_ratio(d.pop("upvoteRatio", UNSET))

        def _parse_comment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        comment_count = _parse_comment_count(d.pop("commentCount", UNSET))

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

        def _parse_is_video(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_video = _parse_is_video(d.pop("isVideo", UNSET))

        def _parse_is_over_18(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_over_18 = _parse_is_over_18(d.pop("isOver18", UNSET))

        def _parse_is_spoiler(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_spoiler = _parse_is_spoiler(d.pop("isSpoiler", UNSET))

        reddit_post_comments_response_200_output_post_type_0 = cls(
            id=id,
            title=title,
            author=author,
            subreddit=subreddit,
            body_text=body_text,
            url=url,
            permalink=permalink,
            score=score,
            upvote_ratio=upvote_ratio,
            comment_count=comment_count,
            thumbnail_url=thumbnail_url,
            published_at=published_at,
            is_video=is_video,
            is_over_18=is_over_18,
            is_spoiler=is_spoiler,
        )

        reddit_post_comments_response_200_output_post_type_0.additional_properties = d
        return reddit_post_comments_response_200_output_post_type_0

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
