from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hotel_search_response_200_output_brands_item_children_item import (
        HotelSearchResponse200OutputBrandsItemChildrenItem,
    )


T = TypeVar("T", bound="HotelSearchResponse200OutputBrandsItem")


@_attrs_define
class HotelSearchResponse200OutputBrandsItem:
    """
    Attributes:
        id (int): Brand group identifier.
        name (str): Brand group display name.
        children (list[HotelSearchResponse200OutputBrandsItemChildrenItem]): Sub-brands within this group.
    """

    id: int
    name: str
    children: list[HotelSearchResponse200OutputBrandsItemChildrenItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_search_response_200_output_brands_item_children_item import (
            HotelSearchResponse200OutputBrandsItemChildrenItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = HotelSearchResponse200OutputBrandsItemChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        hotel_search_response_200_output_brands_item = cls(
            id=id,
            name=name,
            children=children,
        )

        hotel_search_response_200_output_brands_item.additional_properties = d
        return hotel_search_response_200_output_brands_item

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
