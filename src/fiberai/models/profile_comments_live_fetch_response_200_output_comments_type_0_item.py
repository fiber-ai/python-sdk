from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import (
        ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0,
    )
    from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import (
        ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0,
    )


T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200OutputCommentsType0Item")


@_attrs_define
class ProfileCommentsLiveFetchResponse200OutputCommentsType0Item:
    """
    Attributes:
        comment_id (None | str | Unset):
        content (None | str | Unset):
        commented_ago (None | str | Unset):
        commenter (None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0 | Unset):
        post (None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0 | Unset):
    """

    comment_id: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    commented_ago: None | str | Unset = UNSET
    commenter: None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0 | Unset = UNSET
    post: None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import (
            ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0,
        )
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import (
            ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0,
        )

        comment_id: None | str | Unset
        if isinstance(self.comment_id, Unset):
            comment_id = UNSET
        else:
            comment_id = self.comment_id

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        commented_ago: None | str | Unset
        if isinstance(self.commented_ago, Unset):
            commented_ago = UNSET
        else:
            commented_ago = self.commented_ago

        commenter: dict[str, Any] | None | Unset
        if isinstance(self.commenter, Unset):
            commenter = UNSET
        elif isinstance(self.commenter, ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0):
            commenter = self.commenter.to_dict()
        else:
            commenter = self.commenter

        post: dict[str, Any] | None | Unset
        if isinstance(self.post, Unset):
            post = UNSET
        elif isinstance(self.post, ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0):
            post = self.post.to_dict()
        else:
            post = self.post

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_id is not UNSET:
            field_dict["commentId"] = comment_id
        if content is not UNSET:
            field_dict["content"] = content
        if commented_ago is not UNSET:
            field_dict["commentedAgo"] = commented_ago
        if commenter is not UNSET:
            field_dict["commenter"] = commenter
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import (
            ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0,
        )
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import (
            ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0,
        )

        d = dict(src_dict)

        def _parse_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_id = _parse_comment_id(d.pop("commentId", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_commented_ago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commented_ago = _parse_commented_ago(d.pop("commentedAgo", UNSET))

        def _parse_commenter(
            data: object,
        ) -> None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commenter_type_0 = ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0.from_dict(
                    data
                )

                return commenter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0 | Unset, data)

        commenter = _parse_commenter(d.pop("commenter", UNSET))

        def _parse_post(
            data: object,
        ) -> None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_type_0 = ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0.from_dict(data)

                return post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0 | Unset, data)

        post = _parse_post(d.pop("post", UNSET))

        profile_comments_live_fetch_response_200_output_comments_type_0_item = cls(
            comment_id=comment_id,
            content=content,
            commented_ago=commented_ago,
            commenter=commenter,
            post=post,
        )

        profile_comments_live_fetch_response_200_output_comments_type_0_item.additional_properties = d
        return profile_comments_live_fetch_response_200_output_comments_type_0_item

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
