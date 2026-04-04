from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_company_params_investors_v2_type_0_all_of_type_0_item_investor_identifier_type_3_type import (
    CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3Type,
)

T = TypeVar("T", bound="CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3")


@_attrs_define
class CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3:
    """
    Attributes:
        type_ (CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3Type):
        org_id (str):
    """

    type_: CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3Type
    org_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "org_id": org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestorIdentifierType3Type(
            d.pop("type")
        )

        org_id = d.pop("org_id")

        combined_search_count_body_company_params_investors_v2_type_0_all_of_type_0_item_investor_identifier_type_3 = (
            cls(
                type_=type_,
                org_id=org_id,
            )
        )

        combined_search_count_body_company_params_investors_v2_type_0_all_of_type_0_item_investor_identifier_type_3.additional_properties = d
        return (
            combined_search_count_body_company_params_investors_v2_type_0_all_of_type_0_item_investor_identifier_type_3
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
