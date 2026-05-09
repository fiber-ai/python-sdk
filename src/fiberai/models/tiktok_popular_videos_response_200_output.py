from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tiktok_popular_videos_response_200_output_videos_item import (
        TiktokPopularVideosResponse200OutputVideosItem,
    )


T = TypeVar("T", bound="TiktokPopularVideosResponse200Output")


@_attrs_define
class TiktokPopularVideosResponse200Output:
    """
    Attributes:
        videos (list[TiktokPopularVideosResponse200OutputVideosItem]): List of popular videos.
    """

    videos: list[TiktokPopularVideosResponse200OutputVideosItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_popular_videos_response_200_output_videos_item import (
            TiktokPopularVideosResponse200OutputVideosItem,
        )

        d = dict(src_dict)
        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = TiktokPopularVideosResponse200OutputVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        tiktok_popular_videos_response_200_output = cls(
            videos=videos,
        )

        tiktok_popular_videos_response_200_output.additional_properties = d
        return tiktok_popular_videos_response_200_output

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
