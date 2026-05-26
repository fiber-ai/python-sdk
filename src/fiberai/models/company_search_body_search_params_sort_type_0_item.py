from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_sort_type_0_item_direction import (
    CompanySearchBodySearchParamsSortType0ItemDirection,
)
from ..models.company_search_body_search_params_sort_type_0_item_field import (
    CompanySearchBodySearchParamsSortType0ItemField,
)

T = TypeVar("T", bound="CompanySearchBodySearchParamsSortType0Item")


@_attrs_define
class CompanySearchBodySearchParamsSortType0Item:
    """
    Attributes:
        field (CompanySearchBodySearchParamsSortType0ItemField):
        direction (CompanySearchBodySearchParamsSortType0ItemDirection):
    """

    field: CompanySearchBodySearchParamsSortType0ItemField
    direction: CompanySearchBodySearchParamsSortType0ItemDirection
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "direction": direction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = CompanySearchBodySearchParamsSortType0ItemField(d.pop("field"))

        direction = CompanySearchBodySearchParamsSortType0ItemDirection(d.pop("direction"))

        company_search_body_search_params_sort_type_0_item = cls(
            field=field,
            direction=direction,
        )

        company_search_body_search_params_sort_type_0_item.additional_properties = d
        return company_search_body_search_params_sort_type_0_item

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
