from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0_technology import (
    SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Technology,
)
from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0_type import (
    SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Type,
)

T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Type):
        technology (SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Technology):
    """

    type_: SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Type
    technology: SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Technology
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        technology = self.technology.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "technology": technology,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Type(d.pop("type"))

        technology = SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0Technology(
            d.pop("technology")
        )

        sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0 = cls(
            type_=type_,
            technology=technology,
        )

        sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0.additional_properties = d
        return sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0

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
