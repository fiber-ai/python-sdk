from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tiktok_popular_hashtags_response_200_output_hashtags_item import (
        TiktokPopularHashtagsResponse200OutputHashtagsItem,
    )


T = TypeVar("T", bound="TiktokPopularHashtagsResponse200Output")


@_attrs_define
class TiktokPopularHashtagsResponse200Output:
    """
    Attributes:
        hashtags (list[TiktokPopularHashtagsResponse200OutputHashtagsItem]): List of popular hashtags.
    """

    hashtags: list[TiktokPopularHashtagsResponse200OutputHashtagsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hashtags = []
        for hashtags_item_data in self.hashtags:
            hashtags_item = hashtags_item_data.to_dict()
            hashtags.append(hashtags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hashtags": hashtags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_popular_hashtags_response_200_output_hashtags_item import (
            TiktokPopularHashtagsResponse200OutputHashtagsItem,
        )

        d = dict(src_dict)
        hashtags = []
        _hashtags = d.pop("hashtags")
        for hashtags_item_data in _hashtags:
            hashtags_item = TiktokPopularHashtagsResponse200OutputHashtagsItem.from_dict(hashtags_item_data)

            hashtags.append(hashtags_item)

        tiktok_popular_hashtags_response_200_output = cls(
            hashtags=hashtags,
        )

        tiktok_popular_hashtags_response_200_output.additional_properties = d
        return tiktok_popular_hashtags_response_200_output

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
