from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1_type import (
    SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1Type,
)

T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1Type):
        name (str):
    """

    type_: SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1Type
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1Type(d.pop("type"))

        name = d.pop("name")

        sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1 = cls(
            type_=type_,
            name=name,
        )

        sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1.additional_properties = d
        return sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1

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
