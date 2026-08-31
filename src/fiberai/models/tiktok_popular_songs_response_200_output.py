from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tiktok_popular_songs_response_200_output_songs_item import (
        TiktokPopularSongsResponse200OutputSongsItem,
    )


T = TypeVar("T", bound="TiktokPopularSongsResponse200Output")


@_attrs_define
class TiktokPopularSongsResponse200Output:
    """
    Attributes:
        songs (list[TiktokPopularSongsResponse200OutputSongsItem]): List of popular songs.
    """

    songs: list[TiktokPopularSongsResponse200OutputSongsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        songs = []
        for songs_item_data in self.songs:
            songs_item = songs_item_data.to_dict()
            songs.append(songs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "songs": songs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_popular_songs_response_200_output_songs_item import (
            TiktokPopularSongsResponse200OutputSongsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        songs = []
        _songs = d.pop("songs")
        for songs_item_data in _songs:
            songs_item = TiktokPopularSongsResponse200OutputSongsItem.from_dict(songs_item_data)

            songs.append(songs_item)

        tiktok_popular_songs_response_200_output = cls(
            songs=songs,
        )

        tiktok_popular_songs_response_200_output.additional_properties = d
        return tiktok_popular_songs_response_200_output

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
