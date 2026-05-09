from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tiktok_popular_creators_response_200_output_creators_item import (
        TiktokPopularCreatorsResponse200OutputCreatorsItem,
    )


T = TypeVar("T", bound="TiktokPopularCreatorsResponse200Output")


@_attrs_define
class TiktokPopularCreatorsResponse200Output:
    """
    Attributes:
        creators (list[TiktokPopularCreatorsResponse200OutputCreatorsItem]): List of popular creators.
    """

    creators: list[TiktokPopularCreatorsResponse200OutputCreatorsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creators = []
        for creators_item_data in self.creators:
            creators_item = creators_item_data.to_dict()
            creators.append(creators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creators": creators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_popular_creators_response_200_output_creators_item import (
            TiktokPopularCreatorsResponse200OutputCreatorsItem,
        )

        d = dict(src_dict)
        creators = []
        _creators = d.pop("creators")
        for creators_item_data in _creators:
            creators_item = TiktokPopularCreatorsResponse200OutputCreatorsItem.from_dict(creators_item_data)

            creators.append(creators_item)

        tiktok_popular_creators_response_200_output = cls(
            creators=creators,
        )

        tiktok_popular_creators_response_200_output.additional_properties = d
        return tiktok_popular_creators_response_200_output

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
