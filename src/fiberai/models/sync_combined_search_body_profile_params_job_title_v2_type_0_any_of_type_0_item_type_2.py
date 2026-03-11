from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_2_groups_item import (
    SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2GroupsItem,
)
from ..models.sync_combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_2_type import (
    SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2Type):
        groups (list[SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2GroupsItem]):
        keywords (list[str] | Unset):
    """

    type_: SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2Type
    groups: list[SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2GroupsItem]
    keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.value
            groups.append(groups_item)

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "groups": groups,
            }
        )
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2Type(d.pop("type"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AnyOfType0ItemType2GroupsItem(
                groups_item_data
            )

            groups.append(groups_item)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        sync_combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_2 = cls(
            type_=type_,
            groups=groups,
            keywords=keywords,
        )

        sync_combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_2.additional_properties = d
        return sync_combined_search_body_profile_params_job_title_v2_type_0_any_of_type_0_item_type_2

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
