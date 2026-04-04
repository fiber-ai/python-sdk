from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YoutubeTranscriptResponse200OutputSegmentsType0Item")


@_attrs_define
class YoutubeTranscriptResponse200OutputSegmentsType0Item:
    """
    Attributes:
        text (str): The transcript text for this segment.
        start_seconds (float): Start time of the segment in seconds.
        duration_seconds (float): Duration of the segment in seconds.
    """

    text: str
    start_seconds: float
    duration_seconds: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        start_seconds = self.start_seconds

        duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "startSeconds": start_seconds,
                "durationSeconds": duration_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        start_seconds = d.pop("startSeconds")

        duration_seconds = d.pop("durationSeconds")

        youtube_transcript_response_200_output_segments_type_0_item = cls(
            text=text,
            start_seconds=start_seconds,
            duration_seconds=duration_seconds,
        )

        youtube_transcript_response_200_output_segments_type_0_item.additional_properties = d
        return youtube_transcript_response_200_output_segments_type_0_item

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
