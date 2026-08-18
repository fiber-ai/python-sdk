from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonReactionChange")


@_attrs_define
class PersonReactionChange:
    """
    Attributes:
        reaction_id (str): Unique reaction identifier (dedup key)
        type_ (None | str | Unset): Reaction type (LIKE, LOVE, INSIGHTFUL, CELEBRATE, SUPPORT, FUNNY)
        post_content (None | str | Unset): Content of the reacted post
        post_url (None | str | Unset): URL to the LinkedIn post
        post_author_name (None | str | Unset): Name of the post author
        reacted_ago (None | str | Unset): Relative time since the reaction
        reacted_at (None | str | Unset): Exact ISO timestamp when the reaction occurred
    """

    reaction_id: str
    type_: None | str | Unset = UNSET
    post_content: None | str | Unset = UNSET
    post_url: None | str | Unset = UNSET
    post_author_name: None | str | Unset = UNSET
    reacted_ago: None | str | Unset = UNSET
    reacted_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction_id = self.reaction_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        post_content: None | str | Unset
        if isinstance(self.post_content, Unset):
            post_content = UNSET
        else:
            post_content = self.post_content

        post_url: None | str | Unset
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        post_author_name: None | str | Unset
        if isinstance(self.post_author_name, Unset):
            post_author_name = UNSET
        else:
            post_author_name = self.post_author_name

        reacted_ago: None | str | Unset
        if isinstance(self.reacted_ago, Unset):
            reacted_ago = UNSET
        else:
            reacted_ago = self.reacted_ago

        reacted_at: None | str | Unset
        if isinstance(self.reacted_at, Unset):
            reacted_at = UNSET
        else:
            reacted_at = self.reacted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reactionId": reaction_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if post_content is not UNSET:
            field_dict["postContent"] = post_content
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if post_author_name is not UNSET:
            field_dict["postAuthorName"] = post_author_name
        if reacted_ago is not UNSET:
            field_dict["reactedAgo"] = reacted_ago
        if reacted_at is not UNSET:
            field_dict["reactedAt"] = reacted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction_id = d.pop("reactionId")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_post_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_content = _parse_post_content(d.pop("postContent", UNSET))

        def _parse_post_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))

        def _parse_post_author_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_author_name = _parse_post_author_name(d.pop("postAuthorName", UNSET))

        def _parse_reacted_ago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reacted_ago = _parse_reacted_ago(d.pop("reactedAgo", UNSET))

        def _parse_reacted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reacted_at = _parse_reacted_at(d.pop("reactedAt", UNSET))

        person_reaction_change = cls(
            reaction_id=reaction_id,
            type_=type_,
            post_content=post_content,
            post_url=post_url,
            post_author_name=post_author_name,
            reacted_ago=reacted_ago,
            reacted_at=reacted_at,
        )

        person_reaction_change.additional_properties = d
        return person_reaction_change

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
