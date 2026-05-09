from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokVideoTranscriptResponse200OutputSegmentsItem")


@_attrs_define
class TiktokVideoTranscriptResponse200OutputSegmentsItem:
    """
    Attributes:
        text (str): Transcript segment text.
        start_seconds (float | None | Unset): Start time of this segment in seconds from the beginning of the video.
        duration_seconds (float | None | Unset): Duration of this segment in seconds.
    """

    text: str
    start_seconds: float | None | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        start_seconds: float | None | Unset
        if isinstance(self.start_seconds, Unset):
            start_seconds = UNSET
        else:
            start_seconds = self.start_seconds

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if start_seconds is not UNSET:
            field_dict["startSeconds"] = start_seconds
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        def _parse_start_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_seconds = _parse_start_seconds(d.pop("startSeconds", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds", UNSET))

        tiktok_video_transcript_response_200_output_segments_item = cls(
            text=text,
            start_seconds=start_seconds,
            duration_seconds=duration_seconds,
        )

        tiktok_video_transcript_response_200_output_segments_item.additional_properties = d
        return tiktok_video_transcript_response_200_output_segments_item

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
