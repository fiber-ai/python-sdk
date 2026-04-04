from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeVideoCommentsBody")


@_attrs_define
class YoutubeVideoCommentsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        video_id (str): YouTube video ID or full URL. Accepts a bare 11-character ID (e.g. '094y1Z2wpJg') or a full
            YouTube URL (e.g. 'https://www.youtube.com/watch?v=094y1Z2wpJg').
        next_page_token (None | str | Unset): Pagination token from a previous response to retrieve the next page of
            comments. Omit for the first page.
    """

    api_key: str
    video_id: str
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        video_id = self.video_id

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
                "videoId": video_id,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        video_id = d.pop("videoId")

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        youtube_video_comments_body = cls(
            api_key=api_key,
            video_id=video_id,
            next_page_token=next_page_token,
        )

        youtube_video_comments_body.additional_properties = d
        return youtube_video_comments_body

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
