from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reddit_post_comments_response_200_output_comments_item import (
        RedditPostCommentsResponse200OutputCommentsItem,
    )
    from ..models.reddit_post_comments_response_200_output_post_type_0 import (
        RedditPostCommentsResponse200OutputPostType0,
    )


T = TypeVar("T", bound="RedditPostCommentsResponse200Output")


@_attrs_define
class RedditPostCommentsResponse200Output:
    """
    Attributes:
        comments (list[RedditPostCommentsResponse200OutputCommentsItem]): Flat list of comments returned for the post,
            including replies. Each entry's `parentCommentId` is null for top-level comments and points at the parent
            comment's `id` for replies. The list is depth-first ordered (each top-level comment is followed by its
            descendants), so customers who want a tree can group on `parentCommentId`.
        post (None | RedditPostCommentsResponse200OutputPostType0 | Unset): Post metadata for the requested comment
            thread.
        next_page_token (None | str | Unset): Token to retrieve the next page of top-level comments (their nested
            replies are included automatically). Pass as `nextPageToken` in the next request. Null if no more pages.
    """

    comments: list[RedditPostCommentsResponse200OutputCommentsItem]
    post: None | RedditPostCommentsResponse200OutputPostType0 | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reddit_post_comments_response_200_output_post_type_0 import (
            RedditPostCommentsResponse200OutputPostType0,
        )

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        post: dict[str, Any] | None | Unset
        if isinstance(self.post, Unset):
            post = UNSET
        elif isinstance(self.post, RedditPostCommentsResponse200OutputPostType0):
            post = self.post.to_dict()
        else:
            post = self.post

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
            }
        )
        if post is not UNSET:
            field_dict["post"] = post
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reddit_post_comments_response_200_output_comments_item import (
            RedditPostCommentsResponse200OutputCommentsItem,
        )
        from ..models.reddit_post_comments_response_200_output_post_type_0 import (
            RedditPostCommentsResponse200OutputPostType0,
        )

        d = dict(src_dict)
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = RedditPostCommentsResponse200OutputCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        def _parse_post(data: object) -> None | RedditPostCommentsResponse200OutputPostType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_type_0 = RedditPostCommentsResponse200OutputPostType0.from_dict(data)

                return post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedditPostCommentsResponse200OutputPostType0 | Unset, data)

        post = _parse_post(d.pop("post", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        reddit_post_comments_response_200_output = cls(
            comments=comments,
            post=post,
            next_page_token=next_page_token,
        )

        reddit_post_comments_response_200_output.additional_properties = d
        return reddit_post_comments_response_200_output

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
