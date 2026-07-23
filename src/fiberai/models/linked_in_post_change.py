from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        poster_name (None | str | Unset): Display name of the person who posted
        poster_slug (None | str | Unset): LinkedIn slug of the poster (e.g. 'williamhgates')
        poster_url (None | str | Unset): Full LinkedIn profile URL of the poster
        poster_profile_picture (None | str | Unset): Profile picture URL of the poster
    """

    post_id: str
    post_url: None | str
    caption: None | str
    posted_at: None | str
    num_reactions: float | None
    num_comments: float | None
    num_shares: float | None
    poster_name: None | str | Unset = UNSET
    poster_slug: None | str | Unset = UNSET
    poster_url: None | str | Unset = UNSET
    poster_profile_picture: None | str | Unset = UNSET
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

        poster_name: None | str | Unset
        if isinstance(self.poster_name, Unset):
            poster_name = UNSET
        else:
            poster_name = self.poster_name

        poster_slug: None | str | Unset
        if isinstance(self.poster_slug, Unset):
            poster_slug = UNSET
        else:
            poster_slug = self.poster_slug

        poster_url: None | str | Unset
        if isinstance(self.poster_url, Unset):
            poster_url = UNSET
        else:
            poster_url = self.poster_url

        poster_profile_picture: None | str | Unset
        if isinstance(self.poster_profile_picture, Unset):
            poster_profile_picture = UNSET
        else:
            poster_profile_picture = self.poster_profile_picture

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
        if poster_name is not UNSET:
            field_dict["posterName"] = poster_name
        if poster_slug is not UNSET:
            field_dict["posterSlug"] = poster_slug
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if poster_profile_picture is not UNSET:
            field_dict["posterProfilePicture"] = poster_profile_picture

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

        def _parse_poster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_name = _parse_poster_name(d.pop("posterName", UNSET))

        def _parse_poster_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_slug = _parse_poster_slug(d.pop("posterSlug", UNSET))

        def _parse_poster_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_url = _parse_poster_url(d.pop("posterUrl", UNSET))

        def _parse_poster_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_profile_picture = _parse_poster_profile_picture(d.pop("posterProfilePicture", UNSET))

        linked_in_post_change = cls(
            post_id=post_id,
            post_url=post_url,
            caption=caption,
            posted_at=posted_at,
            num_reactions=num_reactions,
            num_comments=num_comments,
            num_shares=num_shares,
            poster_name=poster_name,
            poster_slug=poster_slug,
            poster_url=poster_url,
            poster_profile_picture=poster_profile_picture,
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
