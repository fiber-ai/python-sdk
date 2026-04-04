from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_0_type import (
    SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0Type,
)

T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0Type):
        domain (str):
    """

    type_: SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0Type
    domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType0Type(
            d.pop("type")
        )

        domain = d.pop("domain")

        sync_combined_search_body_company_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_0 = (
            cls(
                type_=type_,
                domain=domain,
            )
        )

        sync_combined_search_body_company_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_0.additional_properties = d
        return (
            sync_combined_search_body_company_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_0
        )

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
