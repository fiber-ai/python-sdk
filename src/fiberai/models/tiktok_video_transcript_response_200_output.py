from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiktok_video_transcript_response_200_output_language_type_0 import (
        TiktokVideoTranscriptResponse200OutputLanguageType0,
    )
    from ..models.tiktok_video_transcript_response_200_output_segments_item import (
        TiktokVideoTranscriptResponse200OutputSegmentsItem,
    )


T = TypeVar("T", bound="TiktokVideoTranscriptResponse200Output")


@_attrs_define
class TiktokVideoTranscriptResponse200Output:
    """
    Attributes:
        segments (list[TiktokVideoTranscriptResponse200OutputSegmentsItem]): Ordered list of transcript segments.
        language (None | TiktokVideoTranscriptResponse200OutputLanguageType0 | Unset): Language of the transcript, if
            detected.
    """

    segments: list[TiktokVideoTranscriptResponse200OutputSegmentsItem]
    language: None | TiktokVideoTranscriptResponse200OutputLanguageType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tiktok_video_transcript_response_200_output_language_type_0 import (
            TiktokVideoTranscriptResponse200OutputLanguageType0,  # noqa: PLC0415
        )

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        language: dict[str, Any] | None | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        elif isinstance(self.language, TiktokVideoTranscriptResponse200OutputLanguageType0):
            language = self.language.to_dict()
        else:
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_video_transcript_response_200_output_language_type_0 import (
            TiktokVideoTranscriptResponse200OutputLanguageType0,  # noqa: PLC0415
        )
        from ..models.tiktok_video_transcript_response_200_output_segments_item import (
            TiktokVideoTranscriptResponse200OutputSegmentsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = TiktokVideoTranscriptResponse200OutputSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        def _parse_language(data: object) -> None | TiktokVideoTranscriptResponse200OutputLanguageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                language_type_0 = TiktokVideoTranscriptResponse200OutputLanguageType0.from_dict(data)

                return language_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TiktokVideoTranscriptResponse200OutputLanguageType0 | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        tiktok_video_transcript_response_200_output = cls(
            segments=segments,
            language=language,
        )

        tiktok_video_transcript_response_200_output.additional_properties = d
        return tiktok_video_transcript_response_200_output

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
