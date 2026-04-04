from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YoutubeVideoDetailsResponse200OutputChaptersItem")


@_attrs_define
class YoutubeVideoDetailsResponse200OutputChaptersItem:
    """
    Attributes:
        title (str): Chapter title.
        start_seconds (float): Start time of the chapter in seconds.
    """

    title: str
    start_seconds: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        start_seconds = self.start_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "startSeconds": start_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        start_seconds = d.pop("startSeconds")

        youtube_video_details_response_200_output_chapters_item = cls(
            title=title,
            start_seconds=start_seconds,
        )

        youtube_video_details_response_200_output_chapters_item.additional_properties = d
        return youtube_video_details_response_200_output_chapters_item

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
