from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonCommentChange")


@_attrs_define
class PersonCommentChange:
    """
    Attributes:
        comment_id (str): Unique comment identifier (dedup key)
        content (None | str | Unset): Content of the comment
        post_content (None | str | Unset): Content of the original post
        post_url (None | str | Unset): URL to the LinkedIn post
        post_author_name (None | str | Unset): Name of the post author
        commented_ago (None | str | Unset): Relative time since the comment
        commented_at (None | str | Unset): Exact ISO timestamp when the comment was made
    """

    comment_id: str
    content: None | str | Unset = UNSET
    post_content: None | str | Unset = UNSET
    post_url: None | str | Unset = UNSET
    post_author_name: None | str | Unset = UNSET
    commented_ago: None | str | Unset = UNSET
    commented_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

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

        commented_ago: None | str | Unset
        if isinstance(self.commented_ago, Unset):
            commented_ago = UNSET
        else:
            commented_ago = self.commented_ago

        commented_at: None | str | Unset
        if isinstance(self.commented_at, Unset):
            commented_at = UNSET
        else:
            commented_at = self.commented_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if post_content is not UNSET:
            field_dict["postContent"] = post_content
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if post_author_name is not UNSET:
            field_dict["postAuthorName"] = post_author_name
        if commented_ago is not UNSET:
            field_dict["commentedAgo"] = commented_ago
        if commented_at is not UNSET:
            field_dict["commentedAt"] = commented_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("commentId")

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

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

        def _parse_commented_ago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commented_ago = _parse_commented_ago(d.pop("commentedAgo", UNSET))

        def _parse_commented_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commented_at = _parse_commented_at(d.pop("commentedAt", UNSET))

        person_comment_change = cls(
            comment_id=comment_id,
            content=content,
            post_content=post_content,
            post_url=post_url,
            post_author_name=post_author_name,
            commented_ago=commented_ago,
            commented_at=commented_at,
        )

        person_comment_change.additional_properties = d
        return person_comment_change

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
