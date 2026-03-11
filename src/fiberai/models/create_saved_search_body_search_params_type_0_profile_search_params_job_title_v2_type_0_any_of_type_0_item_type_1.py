from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_title_v2_type_0_any_of_type_0_item_type_1_groups_item import (
    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem,
)
from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_title_v2_type_0_any_of_type_0_item_type_1_type import (
    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1Type,
)

T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1:
    """
    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1Type):
        groups
            (list[CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem]):
    """

    type_: CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1Type
    groups: list[CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem]
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
        type_ = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1Type(
            d.pop("type")
        )

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = (
                CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV2Type0AnyOfType0ItemType1GroupsItem(
                    groups_item_data
                )
            )

            groups.append(groups_item)

        create_saved_search_body_search_params_type_0_profile_search_params_job_title_v2_type_0_any_of_type_0_item_type_1 = cls(
            type_=type_,
            groups=groups,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_job_title_v2_type_0_any_of_type_0_item_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_job_title_v2_type_0_any_of_type_0_item_type_1

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
