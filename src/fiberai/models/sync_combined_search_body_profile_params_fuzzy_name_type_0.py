from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_profile_params_fuzzy_name_type_0_any_of_item import (
        SyncCombinedSearchBodyProfileParamsFuzzyNameType0AnyOfItem,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsFuzzyNameType0")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsFuzzyNameType0:
    """
    Attributes:
        any_of (list[SyncCombinedSearchBodyProfileParamsFuzzyNameType0AnyOfItem]):
    """

    any_of: list[SyncCombinedSearchBodyProfileParamsFuzzyNameType0AnyOfItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_of = []
        for any_of_item_data in self.any_of:
            any_of_item = any_of_item_data.to_dict()
            any_of.append(any_of_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anyOf": any_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_profile_params_fuzzy_name_type_0_any_of_item import (
            SyncCombinedSearchBodyProfileParamsFuzzyNameType0AnyOfItem,
        )

        d = dict(src_dict)
        any_of = []
        _any_of = d.pop("anyOf")
        for any_of_item_data in _any_of:
            any_of_item = SyncCombinedSearchBodyProfileParamsFuzzyNameType0AnyOfItem.from_dict(any_of_item_data)

            any_of.append(any_of_item)

        sync_combined_search_body_profile_params_fuzzy_name_type_0 = cls(
            any_of=any_of,
        )

        sync_combined_search_body_profile_params_fuzzy_name_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_fuzzy_name_type_0

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
