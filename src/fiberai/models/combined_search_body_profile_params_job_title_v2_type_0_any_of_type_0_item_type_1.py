from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_1_groups_item import (
    CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem,
)
from ..models.combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_1_type import (
    CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1Type,
)

T = TypeVar("T", bound="CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1")


@_attrs_define
class CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1:
    """
    Attributes:
        type_ (CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1Type):
        groups (list[CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem]):
    """

    type_: CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1Type
    groups: list[CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.value
            groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1Type(d.pop("type"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = CombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem(groups_item_data)

            groups.append(groups_item)

        combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_1 = cls(
            type_=type_,
            groups=groups,
        )

        combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_1.additional_properties = d
        return combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_1

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
