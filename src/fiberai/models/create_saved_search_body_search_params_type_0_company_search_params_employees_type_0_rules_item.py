from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employees_to_match_type_1 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItem:
    """
    Attributes:
        employees_to_match
            (CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0 |
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1):
        employee_filters
            (CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0 | None |
            Unset):
    """

    employees_to_match: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0
        | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1
    )
    employee_filters: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        )

        employees_to_match: dict[str, Any]
        if isinstance(
            self.employees_to_match,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        ):
            employees_to_match = self.employees_to_match.to_dict()
        else:
            employees_to_match = self.employees_to_match.to_dict()

        employee_filters: dict[str, Any] | None | Unset
        if isinstance(self.employee_filters, Unset):
            employee_filters = UNSET
        elif isinstance(
            self.employee_filters,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        ):
            employee_filters = self.employee_filters.to_dict()
        else:
            employee_filters = self.employee_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employeesToMatch": employees_to_match,
            }
        )
        if employee_filters is not UNSET:
            field_dict["employeeFilters"] = employee_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employees_to_match_type_1 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1,
        )

        d = dict(src_dict)

        def _parse_employees_to_match(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0
            | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employees_to_match_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType0.from_dict(
                    data
                )

                return employees_to_match_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            employees_to_match_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeesToMatchType1.from_dict(
                data
            )

            return employees_to_match_type_1

        employees_to_match = _parse_employees_to_match(d.pop("employeesToMatch"))

        def _parse_employee_filters(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_filters_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0.from_dict(
                    data
                )

                return employee_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0
                | None
                | Unset,
                data,
            )

        employee_filters = _parse_employee_filters(d.pop("employeeFilters", UNSET))

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item = cls(
            employees_to_match=employees_to_match,
            employee_filters=employee_filters,
        )

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item

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
