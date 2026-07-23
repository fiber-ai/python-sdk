from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_hotel_brands_response_200_output_brands_item_children_item import (
        GetHotelBrandsResponse200OutputBrandsItemChildrenItem,
    )


T = TypeVar("T", bound="GetHotelBrandsResponse200OutputBrandsItem")


@_attrs_define
class GetHotelBrandsResponse200OutputBrandsItem:
    """A supported hotel brand filter value.

    Attributes:
        id (int): Brand group identifier for search filters.
        name (str): Brand group display name.
        children (list[GetHotelBrandsResponse200OutputBrandsItemChildrenItem]): Sub-brands within this group.
    """

    id: int
    name: str
    children: list[GetHotelBrandsResponse200OutputBrandsItemChildrenItem]
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
        from ..models.get_hotel_brands_response_200_output_brands_item_children_item import (
            GetHotelBrandsResponse200OutputBrandsItemChildrenItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = GetHotelBrandsResponse200OutputBrandsItemChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        get_hotel_brands_response_200_output_brands_item = cls(
            id=id,
            name=name,
            children=children,
        )

        get_hotel_brands_response_200_output_brands_item.additional_properties = d
        return get_hotel_brands_response_200_output_brands_item

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
