from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonCommentChange")


@_attrs_define
class PersonCommentChange:
    """
    Attributes:
        comment_id (str): Unique comment identifier (dedup key)
        content (None | str): Content of the comment
        post_content (None | str): Content of the original post
        post_url (None | str): URL to the LinkedIn post
        post_author_name (None | str): Name of the post author
        commented_ago (None | str): Relative time since the comment
    """

    comment_id: str
    content: None | str
    post_content: None | str
    post_url: None | str
    post_author_name: None | str
    commented_ago: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        content: None | str
        content = self.content

        post_content: None | str
        post_content = self.post_content

        post_url: None | str
        post_url = self.post_url

        post_author_name: None | str
        post_author_name = self.post_author_name

        commented_ago: None | str
        commented_ago = self.commented_ago

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "content": content,
                "postContent": post_content,
                "postUrl": post_url,
                "postAuthorName": post_author_name,
                "commentedAgo": commented_ago,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("commentId")

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

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

        def _parse_commented_ago(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commented_ago = _parse_commented_ago(d.pop("commentedAgo"))

        person_comment_change = cls(
            comment_id=comment_id,
            content=content,
            post_content=post_content,
            post_url=post_url,
            post_author_name=post_author_name,
            commented_ago=commented_ago,
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
