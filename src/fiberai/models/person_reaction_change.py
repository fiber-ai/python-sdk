from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonReactionChange")


@_attrs_define
class PersonReactionChange:
    """
    Attributes:
        reaction_id (str): Unique reaction identifier (dedup key)
        type_ (None | str): Reaction type (LIKE, LOVE, INSIGHTFUL, CELEBRATE, SUPPORT, FUNNY)
        post_content (None | str): Content of the reacted post
        post_url (None | str): URL to the LinkedIn post
        post_author_name (None | str): Name of the post author
        reacted_ago (None | str): Relative time since the reaction
    """

    reaction_id: str
    type_: None | str
    post_content: None | str
    post_url: None | str
    post_author_name: None | str
    reacted_ago: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction_id = self.reaction_id

        type_: None | str
        type_ = self.type_

        post_content: None | str
        post_content = self.post_content

        post_url: None | str
        post_url = self.post_url

        post_author_name: None | str
        post_author_name = self.post_author_name

        reacted_ago: None | str
        reacted_ago = self.reacted_ago

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reactionId": reaction_id,
                "type": type_,
                "postContent": post_content,
                "postUrl": post_url,
                "postAuthorName": post_author_name,
                "reactedAgo": reacted_ago,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction_id = d.pop("reactionId")

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_post_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_content = _parse_post_content(d.pop("postContent"))

        def _parse_post_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_url = _parse_post_url(d.pop("postUrl"))

        def _parse_post_author_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_author_name = _parse_post_author_name(d.pop("postAuthorName"))

        def _parse_reacted_ago(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reacted_ago = _parse_reacted_ago(d.pop("reactedAgo"))

        person_reaction_change = cls(
            reaction_id=reaction_id,
            type_=type_,
            post_content=post_content,
            post_url=post_url,
            post_author_name=post_author_name,
            reacted_ago=reacted_ago,
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
