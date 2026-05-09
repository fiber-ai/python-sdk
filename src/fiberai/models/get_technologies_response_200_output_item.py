from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_technologies_response_200_output_item_type import GetTechnologiesResponse200OutputItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTechnologiesResponse200OutputItem")


@_attrs_define
class GetTechnologiesResponse200OutputItem:
    """
    Attributes:
        technology (str): Canonical slug for this technology or platform
        synonyms (list[str]): Human-readable names and variants
        type_ (GetTechnologiesResponse200OutputItemType): Whether this is a technology or a platform
        category (None | str | Unset): Technology category (e.g. CMS, CRM, Analytics)
    """

    technology: str
    synonyms: list[str]
    type_: GetTechnologiesResponse200OutputItemType
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        technology = self.technology

        synonyms = self.synonyms

        type_ = self.type_.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "technology": technology,
                "synonyms": synonyms,
                "type": type_,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        technology = d.pop("technology")

        synonyms = cast(list[str], d.pop("synonyms"))

        type_ = GetTechnologiesResponse200OutputItemType(d.pop("type"))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        get_technologies_response_200_output_item = cls(
            technology=technology,
            synonyms=synonyms,
            type_=type_,
            category=category,
        )

        get_technologies_response_200_output_item.additional_properties = d
        return get_technologies_response_200_output_item

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
