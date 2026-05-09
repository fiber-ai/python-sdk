from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokPopularHashtagsResponse200OutputHashtagsItem")


@_attrs_define
class TiktokPopularHashtagsResponse200OutputHashtagsItem:
    """
    Attributes:
        name (None | str | Unset): Hashtag name (without '#').
        video_count (float | None | Unset): Total number of videos using this hashtag.
        total_view_count (float | None | Unset): Total number of views across all videos with this hashtag.
        trend_direction (None | str | Unset): Trend direction indicator (free-form; the value depends on what TikTok
            reports).
    """

    name: None | str | Unset = UNSET
    video_count: float | None | Unset = UNSET
    total_view_count: float | None | Unset = UNSET
    trend_direction: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        video_count: float | None | Unset
        if isinstance(self.video_count, Unset):
            video_count = UNSET
        else:
            video_count = self.video_count

        total_view_count: float | None | Unset
        if isinstance(self.total_view_count, Unset):
            total_view_count = UNSET
        else:
            total_view_count = self.total_view_count

        trend_direction: None | str | Unset
        if isinstance(self.trend_direction, Unset):
            trend_direction = UNSET
        else:
            trend_direction = self.trend_direction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if video_count is not UNSET:
            field_dict["videoCount"] = video_count
        if total_view_count is not UNSET:
            field_dict["totalViewCount"] = total_view_count
        if trend_direction is not UNSET:
            field_dict["trendDirection"] = trend_direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_video_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_count = _parse_video_count(d.pop("videoCount", UNSET))

        def _parse_total_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_view_count = _parse_total_view_count(d.pop("totalViewCount", UNSET))

        def _parse_trend_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trend_direction = _parse_trend_direction(d.pop("trendDirection", UNSET))

        tiktok_popular_hashtags_response_200_output_hashtags_item = cls(
            name=name,
            video_count=video_count,
            total_view_count=total_view_count,
            trend_direction=trend_direction,
        )

        tiktok_popular_hashtags_response_200_output_hashtags_item.additional_properties = d
        return tiktok_popular_hashtags_response_200_output_hashtags_item

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
