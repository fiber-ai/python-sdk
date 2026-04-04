from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeTranscriptBody")


@_attrs_define
class YoutubeTranscriptBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        video_id (str): YouTube video ID or full URL. Accepts a bare 11-character ID (e.g. '094y1Z2wpJg') or a full
            YouTube URL (e.g. 'https://www.youtube.com/watch?v=094y1Z2wpJg').
        language_code (None | str | Unset): Transcript BCP-47 language code (e.g. 'en' for English, 'es' for Spanish,
            'fr' for French, 'pt-BR' for Brazilian Portuguese). Omit to receive the default language transcript.
    """

    api_key: str
    video_id: str
    language_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        video_id = self.video_id

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "videoId": video_id,
            }
        )
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        video_id = d.pop("videoId")

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("languageCode", UNSET))

        youtube_transcript_body = cls(
            api_key=api_key,
            video_id=video_id,
            language_code=language_code,
        )

        youtube_transcript_body.additional_properties = d
        return youtube_transcript_body

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
