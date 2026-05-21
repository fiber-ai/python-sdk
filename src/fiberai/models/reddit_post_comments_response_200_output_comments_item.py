from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RedditPostCommentsResponse200OutputCommentsItem")


@_attrs_define
class RedditPostCommentsResponse200OutputCommentsItem:
    """
    Attributes:
        id (str): Stable Reddit comment identifier (e.g. `ed1czme`). Use this as the primary key when storing comments
            in a database.
        parent_comment_id (None | str | Unset): Parent comment ID when this entry is a reply to another comment. Null
            for top-level comments (whose parent is the post). Use this field to rebuild the thread tree by grouping
            comments on `parentCommentId`.
        author (None | str | Unset): Comment author username.
        body_text (None | str | Unset): Comment body text.
        score (float | None | Unset): Net vote score (upvotes minus downvotes, subject to Reddit vote fuzzing).
        published_at (None | str | Unset): Comment timestamp in ISO 8601 format.
        reply_count (float | None | Unset): Total number of direct replies on this comment. May exceed the number of
            reply entries actually present in `comments[]` when some replies are collapsed by Reddit and not included in the
            current page.
        permalink (None | str | Unset): Canonical Reddit permalink for the comment.
    """

    id: str
    parent_comment_id: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    body_text: None | str | Unset = UNSET
    score: float | None | Unset = UNSET
    published_at: None | str | Unset = UNSET
    reply_count: float | None | Unset = UNSET
    permalink: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_comment_id: None | str | Unset
        if isinstance(self.parent_comment_id, Unset):
            parent_comment_id = UNSET
        else:
            parent_comment_id = self.parent_comment_id

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        body_text: None | str | Unset
        if isinstance(self.body_text, Unset):
            body_text = UNSET
        else:
            body_text = self.body_text

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        reply_count: float | None | Unset
        if isinstance(self.reply_count, Unset):
            reply_count = UNSET
        else:
            reply_count = self.reply_count

        permalink: None | str | Unset
        if isinstance(self.permalink, Unset):
            permalink = UNSET
        else:
            permalink = self.permalink

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if parent_comment_id is not UNSET:
            field_dict["parentCommentId"] = parent_comment_id
        if author is not UNSET:
            field_dict["author"] = author
        if body_text is not UNSET:
            field_dict["bodyText"] = body_text
        if score is not UNSET:
            field_dict["score"] = score
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if permalink is not UNSET:
            field_dict["permalink"] = permalink

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_parent_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_comment_id = _parse_parent_comment_id(d.pop("parentCommentId", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_body_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_text = _parse_body_text(d.pop("bodyText", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_reply_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reply_count = _parse_reply_count(d.pop("replyCount", UNSET))

        def _parse_permalink(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permalink = _parse_permalink(d.pop("permalink", UNSET))

        reddit_post_comments_response_200_output_comments_item = cls(
            id=id,
            parent_comment_id=parent_comment_id,
            author=author,
            body_text=body_text,
            score=score,
            published_at=published_at,
            reply_count=reply_count,
            permalink=permalink,
        )

        reddit_post_comments_response_200_output_comments_item.additional_properties = d
        return reddit_post_comments_response_200_output_comments_item

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
