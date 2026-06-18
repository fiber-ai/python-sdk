from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LinkedInPostChange")


@_attrs_define
class LinkedInPostChange:
    """
    Attributes:
        post_id (str): LinkedIn post ID
        post_url (None | str): URL to the post
        caption (None | str): Post content
        posted_at (None | str): ISO date when posted
        num_reactions (float | None): Number of reactions
        num_comments (float | None): Number of comments
        num_shares (float | None): Number of shares
    """

    post_id: str
    post_url: None | str
    caption: None | str
    posted_at: None | str
    num_reactions: float | None
    num_comments: float | None
    num_shares: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        post_url: None | str
        post_url = self.post_url

        caption: None | str
        caption = self.caption

        posted_at: None | str
        posted_at = self.posted_at

        num_reactions: float | None
        num_reactions = self.num_reactions

        num_comments: float | None
        num_comments = self.num_comments

        num_shares: float | None
        num_shares = self.num_shares

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postId": post_id,
                "postUrl": post_url,
                "caption": caption,
                "postedAt": posted_at,
                "numReactions": num_reactions,
                "numComments": num_comments,
                "numShares": num_shares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_id = d.pop("postId")

        def _parse_post_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_url = _parse_post_url(d.pop("postUrl"))

        def _parse_caption(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        caption = _parse_caption(d.pop("caption"))

        def _parse_posted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        posted_at = _parse_posted_at(d.pop("postedAt"))

        def _parse_num_reactions(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        num_reactions = _parse_num_reactions(d.pop("numReactions"))

        def _parse_num_comments(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        num_comments = _parse_num_comments(d.pop("numComments"))

        def _parse_num_shares(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        num_shares = _parse_num_shares(d.pop("numShares"))

        linked_in_post_change = cls(
            post_id=post_id,
            post_url=post_url,
            caption=caption,
            posted_at=posted_at,
            num_reactions=num_reactions,
            num_comments=num_comments,
            num_shares=num_shares,
        )

        linked_in_post_change.additional_properties = d
        return linked_in_post_change

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
