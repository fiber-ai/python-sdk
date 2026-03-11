from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_search_by_keywords_response_200_output_posts_item import (
        PostSearchByKeywordsResponse200OutputPostsItem,
    )


T = TypeVar("T", bound="PostSearchByKeywordsResponse200Output")


@_attrs_define
class PostSearchByKeywordsResponse200Output:
    """
    Attributes:
        posts (list[PostSearchByKeywordsResponse200OutputPostsItem]):
        cursor (None | str | Unset):
    """

    posts: list[PostSearchByKeywordsResponse200OutputPostsItem]
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "posts": posts,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_search_by_keywords_response_200_output_posts_item import (
            PostSearchByKeywordsResponse200OutputPostsItem,
        )

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = PostSearchByKeywordsResponse200OutputPostsItem.from_dict(posts_item_data)

            posts.append(posts_item)

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        post_search_by_keywords_response_200_output = cls(
            posts=posts,
            cursor=cursor,
        )

        post_search_by_keywords_response_200_output.additional_properties = d
        return post_search_by_keywords_response_200_output

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
