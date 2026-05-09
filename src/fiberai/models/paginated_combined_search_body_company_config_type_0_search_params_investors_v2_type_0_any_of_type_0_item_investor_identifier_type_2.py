from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_2_type import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType2Type,
)

T = TypeVar(
    "T",
    bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType2",
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType2:
    """
    Attributes:
        type_ (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifier
            Type2Type):
        linkedin_slug (str):
    """

    type_: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType2Type
    linkedin_slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        linkedin_slug = self.linkedin_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "linkedin_slug": linkedin_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AnyOfType0ItemInvestorIdentifierType2Type(
            d.pop("type")
        )

        linkedin_slug = d.pop("linkedin_slug")

        paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_2 = cls(
            type_=type_,
            linkedin_slug=linkedin_slug,
        )

        paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_2.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_any_of_type_0_item_investor_identifier_type_2

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
