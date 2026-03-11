from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_combined_search_response_200_output_data_type_1_type import (
    PollCombinedSearchResponse200OutputDataType1Type,
)

if TYPE_CHECKING:
    from ..models.poll_combined_search_response_200_output_data_type_1_items_item import (
        PollCombinedSearchResponse200OutputDataType1ItemsItem,
    )


T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType1")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType1:
    """
    Attributes:
        type_ (PollCombinedSearchResponse200OutputDataType1Type):
        items (list[PollCombinedSearchResponse200OutputDataType1ItemsItem]):
    """

    type_: PollCombinedSearchResponse200OutputDataType1Type
    items: list[PollCombinedSearchResponse200OutputDataType1ItemsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_combined_search_response_200_output_data_type_1_items_item import (
            PollCombinedSearchResponse200OutputDataType1ItemsItem,
        )

        d = dict(src_dict)
        type_ = PollCombinedSearchResponse200OutputDataType1Type(d.pop("type"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PollCombinedSearchResponse200OutputDataType1ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        poll_combined_search_response_200_output_data_type_1 = cls(
            type_=type_,
            items=items,
        )

        poll_combined_search_response_200_output_data_type_1.additional_properties = d
        return poll_combined_search_response_200_output_data_type_1

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
