from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0_tag import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0Tag,
)

T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0"
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0:
    """
    Attributes:
        tag (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0Tag):
    """

    tag: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0Tag
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0Tag(
            d.pop("tag")
        )

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0 = cls(
            tag=tag,
        )

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0

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
