from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_sort_type_0_item_direction import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemDirection,
)
from ..models.paginated_combined_search_body_profile_config_type_0_search_params_sort_type_0_item_field import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemField,
)

T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0Item")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0Item:
    """
    Attributes:
        field (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemField):
        direction (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemDirection):
    """

    field: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemField
    direction: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemDirection
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
        field = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemField(d.pop("field"))

        direction = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemDirection(d.pop("direction"))

        paginated_combined_search_body_profile_config_type_0_search_params_sort_type_0_item = cls(
            field=field,
            direction=direction,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_sort_type_0_item.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_sort_type_0_item

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
