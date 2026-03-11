from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_combined_search_response_200_output_data_type_0_items_item_fortune_rankings_type_0_item_list import (
    PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0ItemList,
)

T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0Item")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0Item:
    """
    Attributes:
        list_ (PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0ItemList):
        year (float):
        rank (float):
    """

    list_: PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0ItemList
    year: float
    rank: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_ = self.list_.value

        year = self.year

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list": list_,
                "year": year,
                "rank": rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_ = PollCombinedSearchResponse200OutputDataType0ItemsItemFortuneRankingsType0ItemList(d.pop("list"))

        year = d.pop("year")

        rank = d.pop("rank")

        poll_combined_search_response_200_output_data_type_0_items_item_fortune_rankings_type_0_item = cls(
            list_=list_,
            year=year,
            rank=rank,
        )

        poll_combined_search_response_200_output_data_type_0_items_item_fortune_rankings_type_0_item.additional_properties = d
        return poll_combined_search_response_200_output_data_type_0_items_item_fortune_rankings_type_0_item

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
