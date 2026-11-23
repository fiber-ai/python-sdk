from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.facebook_group_posts_response_200_output_posts_item_author_type_0 import (
        FacebookGroupPostsResponse200OutputPostsItemAuthorType0,
    )


T = TypeVar("T", bound="FacebookGroupPostsResponse200OutputPostsItem")


@_attrs_define
class FacebookGroupPostsResponse200OutputPostsItem:
    """
    Attributes:
        id (str): Unique post ID.
        url (None | str | Unset): URL of the post.
        text (None | str | Unset): Post text or caption.
        author (FacebookGroupPostsResponse200OutputPostsItemAuthorType0 | None | Unset): Author of the post.
        published_at (None | str | Unset): ISO 8601 timestamp of when the post was published.
        reaction_count (float | None | Unset): Number of reactions on the post.
        comment_count (float | None | Unset): Number of comments on the post.
        share_count (float | None | Unset): Number of shares of the post.
        feedback_id (None | str | Unset): Feedback ID of the post. Pass as `feedbackId` when fetching its comments to
            make that request faster.
    """

    id: str
    url: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    author: FacebookGroupPostsResponse200OutputPostsItemAuthorType0 | None | Unset = UNSET
    published_at: None | str | Unset = UNSET
    reaction_count: float | None | Unset = UNSET
    comment_count: float | None | Unset = UNSET
    share_count: float | None | Unset = UNSET
    feedback_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.facebook_group_posts_response_200_output_posts_item_author_type_0 import (
            FacebookGroupPostsResponse200OutputPostsItemAuthorType0,  # noqa: PLC0415
        )

        id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, FacebookGroupPostsResponse200OutputPostsItemAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        reaction_count: float | None | Unset
        if isinstance(self.reaction_count, Unset):
            reaction_count = UNSET
        else:
            reaction_count = self.reaction_count

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

        feedback_id: None | str | Unset
        if isinstance(self.feedback_id, Unset):
            feedback_id = UNSET
        else:
            feedback_id = self.feedback_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if text is not UNSET:
            field_dict["text"] = text
        if author is not UNSET:
            field_dict["author"] = author
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if reaction_count is not UNSET:
            field_dict["reactionCount"] = reaction_count
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count
        if share_count is not UNSET:
            field_dict["shareCount"] = share_count
        if feedback_id is not UNSET:
            field_dict["feedbackId"] = feedback_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facebook_group_posts_response_200_output_posts_item_author_type_0 import (
            FacebookGroupPostsResponse200OutputPostsItemAuthorType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_author(data: object) -> FacebookGroupPostsResponse200OutputPostsItemAuthorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = FacebookGroupPostsResponse200OutputPostsItemAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FacebookGroupPostsResponse200OutputPostsItemAuthorType0 | None | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_reaction_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reaction_count = _parse_reaction_count(d.pop("reactionCount", UNSET))

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

        def _parse_feedback_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback_id = _parse_feedback_id(d.pop("feedbackId", UNSET))

        facebook_group_posts_response_200_output_posts_item = cls(
            id=id,
            url=url,
            text=text,
            author=author,
            published_at=published_at,
            reaction_count=reaction_count,
            comment_count=comment_count,
            share_count=share_count,
            feedback_id=feedback_id,
        )

        facebook_group_posts_response_200_output_posts_item.additional_properties = d
        return facebook_group_posts_response_200_output_posts_item

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
