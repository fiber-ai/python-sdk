from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokCommentRepliesBody")


@_attrs_define
class TiktokCommentRepliesBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        comment_id (str): Unique comment ID to fetch replies for.
        video_url (str): Full TikTok video URL the comment belongs to (e.g.
            'https://www.tiktok.com/@therock/video/1234567890').
        next_page_token (None | str | Unset): Pagination token from a previous response to retrieve the next page. Omit
            for the first page.
    """

    api_key: str
    comment_id: str
    video_url: str
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        comment_id = self.comment_id

        video_url = self.video_url

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "commentId": comment_id,
                "videoUrl": video_url,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        comment_id = d.pop("commentId")

        video_url = d.pop("videoUrl")

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        tiktok_comment_replies_body = cls(
            api_key=api_key,
            comment_id=comment_id,
            video_url=video_url,
            next_page_token=next_page_token,
        )

        tiktok_comment_replies_body.additional_properties = d
        return tiktok_comment_replies_body

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
