from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0")


@_attrs_define
class YoutubeVideoCommentsResponse200OutputCommentsItemPublishedAtType0:
    """Publication date. When YouTube only provides approximate time (e.g. '2 years ago'), we estimate the date and set
    `estimated: true`.

        Attributes:
            date (str): ISO 8601 date string (e.g. '2024-03-15T00:00:00.000Z').
            estimated (bool): True when the date was estimated from an approximate time string (e.g. '2 years ago'). False
                when an exact date was available.
    """

    date: str
    estimated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        estimated = self.estimated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "estimated": estimated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        estimated = d.pop("estimated")

        youtube_video_comments_response_200_output_comments_item_published_at_type_0 = cls(
            date=date,
            estimated=estimated,
        )

        youtube_video_comments_response_200_output_comments_item_published_at_type_0.additional_properties = d
        return youtube_video_comments_response_200_output_comments_item_published_at_type_0

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
