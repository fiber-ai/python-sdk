from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokSongDetailsResponse200Output")


@_attrs_define
class TiktokSongDetailsResponse200Output:
    """
    Attributes:
        id (None | str | Unset): Unique song identifier.
        title (None | str | Unset): Song title.
        artist (None | str | Unset): Artist or creator name.
        duration_seconds (float | None | Unset): Song duration in seconds.
        cover_image_url (None | str | Unset): URL of the song cover image.
        video_count (float | None | Unset): Number of TikTok videos that use this song as audio.
    """

    id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    artist: None | str | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    cover_image_url: None | str | Unset = UNSET
    video_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        artist: None | str | Unset
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        cover_image_url: None | str | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        else:
            cover_image_url = self.cover_image_url

        video_count: float | None | Unset
        if isinstance(self.video_count, Unset):
            video_count = UNSET
        else:
            video_count = self.video_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if artist is not UNSET:
            field_dict["artist"] = artist
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if cover_image_url is not UNSET:
            field_dict["coverImageUrl"] = cover_image_url
        if video_count is not UNSET:
            field_dict["videoCount"] = video_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_artist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artist = _parse_artist(d.pop("artist", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds", UNSET))

        def _parse_cover_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("coverImageUrl", UNSET))

        def _parse_video_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_count = _parse_video_count(d.pop("videoCount", UNSET))

        tiktok_song_details_response_200_output = cls(
            id=id,
            title=title,
            artist=artist,
            duration_seconds=duration_seconds,
            cover_image_url=cover_image_url,
            video_count=video_count,
        )

        tiktok_song_details_response_200_output.additional_properties = d
        return tiktok_song_details_response_200_output

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
