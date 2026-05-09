from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokSearchHashtagResponse200OutputHashtagType0")


@_attrs_define
class TiktokSearchHashtagResponse200OutputHashtagType0:
    """Metadata about the hashtag.

    Attributes:
        id (None | str | Unset): Unique hashtag identifier.
        name (None | str | Unset): Hashtag name (without '#').
        total_view_count (float | None | Unset): Total number of views across all videos with this hashtag.
        video_count (float | None | Unset): Total number of videos using this hashtag.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    total_view_count: float | None | Unset = UNSET
    video_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        total_view_count: float | None | Unset
        if isinstance(self.total_view_count, Unset):
            total_view_count = UNSET
        else:
            total_view_count = self.total_view_count

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
        if name is not UNSET:
            field_dict["name"] = name
        if total_view_count is not UNSET:
            field_dict["totalViewCount"] = total_view_count
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_total_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_view_count = _parse_total_view_count(d.pop("totalViewCount", UNSET))

        def _parse_video_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_count = _parse_video_count(d.pop("videoCount", UNSET))

        tiktok_search_hashtag_response_200_output_hashtag_type_0 = cls(
            id=id,
            name=name,
            total_view_count=total_view_count,
            video_count=video_count,
        )

        tiktok_search_hashtag_response_200_output_hashtag_type_0.additional_properties = d
        return tiktok_search_hashtag_response_200_output_hashtag_type_0

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
