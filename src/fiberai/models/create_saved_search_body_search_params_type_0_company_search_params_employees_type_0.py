from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_joiner import (
    CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0Joiner,
)

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0:
    """
    Attributes:
        rules (list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem]):
        joiner (CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0Joiner):
    """

    rules: list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem]
    joiner: CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0Joiner
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        joiner = self.joiner.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
                "joiner": joiner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem,
        )

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem.from_dict(
                rules_item_data
            )

            rules.append(rules_item)

        joiner = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0Joiner(d.pop("joiner"))

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0 = cls(
            rules=rules,
            joiner=joiner,
        )

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_employees_type_0

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
