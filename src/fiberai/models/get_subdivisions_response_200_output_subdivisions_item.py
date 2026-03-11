from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_subdivisions_response_200_output_subdivisions_item_alternate_names_item import (
        GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem,
    )


T = TypeVar("T", bound="GetSubdivisionsResponse200OutputSubdivisionsItem")


@_attrs_define
class GetSubdivisionsResponse200OutputSubdivisionsItem:
    """
    Attributes:
        code (str): Subdivision code without the country prefix, e.g. 'CA' for California, 'MH' for Maharashtra
        name (str): Official name of the subdivision
        type_ (str): Type of subdivision, e.g. 'State', 'Province', 'Land'
        alternate_names (list[GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem]): Alternate/local
            names for the subdivision
    """

    code: str
    name: str
    type_: str
    alternate_names: list[GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        type_ = self.type_

        alternate_names = []
        for alternate_names_item_data in self.alternate_names:
            alternate_names_item = alternate_names_item_data.to_dict()
            alternate_names.append(alternate_names_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "type": type_,
                "alternateNames": alternate_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subdivisions_response_200_output_subdivisions_item_alternate_names_item import (
            GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem,
        )

        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        type_ = d.pop("type")

        alternate_names = []
        _alternate_names = d.pop("alternateNames")
        for alternate_names_item_data in _alternate_names:
            alternate_names_item = GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem.from_dict(
                alternate_names_item_data
            )

            alternate_names.append(alternate_names_item)

        get_subdivisions_response_200_output_subdivisions_item = cls(
            code=code,
            name=name,
            type_=type_,
            alternate_names=alternate_names,
        )

        get_subdivisions_response_200_output_subdivisions_item.additional_properties = d
        return get_subdivisions_response_200_output_subdivisions_item

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
