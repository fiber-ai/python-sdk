from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiktok_comment_replies_response_200_output_comments_item import (
        TiktokCommentRepliesResponse200OutputCommentsItem,
    )


T = TypeVar("T", bound="TiktokCommentRepliesResponse200Output")


@_attrs_define
class TiktokCommentRepliesResponse200Output:
    """
    Attributes:
        comments (list[TiktokCommentRepliesResponse200OutputCommentsItem]): List of replies for this page.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if there are no more pages.
    """

    comments: list[TiktokCommentRepliesResponse200OutputCommentsItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

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
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_comment_replies_response_200_output_comments_item import (
            TiktokCommentRepliesResponse200OutputCommentsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = TiktokCommentRepliesResponse200OutputCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        tiktok_comment_replies_response_200_output = cls(
            comments=comments,
            next_page_token=next_page_token,
        )

        tiktok_comment_replies_response_200_output.additional_properties = d
        return tiktok_comment_replies_response_200_output

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
