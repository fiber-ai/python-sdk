from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.youtube_transcript_response_200_output_available_languages_item import (
        YoutubeTranscriptResponse200OutputAvailableLanguagesItem,
    )
    from ..models.youtube_transcript_response_200_output_segments_type_0_item import (
        YoutubeTranscriptResponse200OutputSegmentsType0Item,
    )


T = TypeVar("T", bound="YoutubeTranscriptResponse200Output")


@_attrs_define
class YoutubeTranscriptResponse200Output:
    """
    Attributes:
        segments (list[YoutubeTranscriptResponse200OutputSegmentsType0Item] | None): Ordered list of transcript segments
            with timestamps.
        available_languages (list[YoutubeTranscriptResponse200OutputAvailableLanguagesItem]): All languages for which a
            transcript is available for this video.
    """

    segments: list[YoutubeTranscriptResponse200OutputSegmentsType0Item] | None
    available_languages: list[YoutubeTranscriptResponse200OutputAvailableLanguagesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments: list[dict[str, Any]] | None
        if isinstance(self.segments, list):
            segments = []
            for segments_type_0_item_data in self.segments:
                segments_type_0_item = segments_type_0_item_data.to_dict()
                segments.append(segments_type_0_item)

        else:
            segments = self.segments

        available_languages = []
        for available_languages_item_data in self.available_languages:
            available_languages_item = available_languages_item_data.to_dict()
            available_languages.append(available_languages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "availableLanguages": available_languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_transcript_response_200_output_available_languages_item import (
            YoutubeTranscriptResponse200OutputAvailableLanguagesItem,  # noqa: PLC0415
        )
        from ..models.youtube_transcript_response_200_output_segments_type_0_item import (
            YoutubeTranscriptResponse200OutputSegmentsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_segments(data: object) -> list[YoutubeTranscriptResponse200OutputSegmentsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segments_type_0 = []
                _segments_type_0 = data
                for segments_type_0_item_data in _segments_type_0:
                    segments_type_0_item = YoutubeTranscriptResponse200OutputSegmentsType0Item.from_dict(
                        segments_type_0_item_data
                    )

                    segments_type_0.append(segments_type_0_item)

                return segments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[YoutubeTranscriptResponse200OutputSegmentsType0Item] | None, data)

        segments = _parse_segments(d.pop("segments"))

        available_languages = []
        _available_languages = d.pop("availableLanguages")
        for available_languages_item_data in _available_languages:
            available_languages_item = YoutubeTranscriptResponse200OutputAvailableLanguagesItem.from_dict(
                available_languages_item_data
            )

            available_languages.append(available_languages_item)

        youtube_transcript_response_200_output = cls(
            segments=segments,
            available_languages=available_languages,
        )

        youtube_transcript_response_200_output.additional_properties = d
        return youtube_transcript_response_200_output

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
