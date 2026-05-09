from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_2 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItem")


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItem:
    """
    Attributes:
        employees_to_match
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1):
        employee_filters (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0 | Unset):
        job_status (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2 | Unset):
    """

    employees_to_match: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1
    )
    employee_filters: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0
        | Unset
    ) = UNSET
    job_status: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_2 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2,
        )

        employees_to_match: dict[str, Any]
        if isinstance(
            self.employees_to_match,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        ):
            employees_to_match = self.employees_to_match.to_dict()
        else:
            employees_to_match = self.employees_to_match.to_dict()

        employee_filters: dict[str, Any] | None | Unset
        if isinstance(self.employee_filters, Unset):
            employee_filters = UNSET
        elif isinstance(
            self.employee_filters,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        ):
            employee_filters = self.employee_filters.to_dict()
        else:
            employee_filters = self.employee_filters

        job_status: dict[str, Any] | None | Unset
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(
            self.job_status,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0,
        ):
            job_status = self.job_status.to_dict()
        elif isinstance(
            self.job_status,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1,
        ):
            job_status = self.job_status.to_dict()
        elif isinstance(
            self.job_status,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2,
        ):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employeesToMatch": employees_to_match,
            }
        )
        if employee_filters is not UNSET:
            field_dict["employeeFilters"] = employee_filters
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employees_to_match_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_job_status_type_2 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2,
        )

        d = dict(src_dict)

        def _parse_employees_to_match(
            data: object,
        ) -> (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employees_to_match_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType0.from_dict(
                    data
                )

                return employees_to_match_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            employees_to_match_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeesToMatchType1.from_dict(
                data
            )

            return employees_to_match_type_1

        employees_to_match = _parse_employees_to_match(d.pop("employeesToMatch"))

        def _parse_employee_filters(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_filters_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0.from_dict(
                    data
                )

                return employee_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0
                | Unset,
                data,
            )

        employee_filters = _parse_employee_filters(d.pop("employeeFilters", UNSET))

        def _parse_job_status(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0.from_dict(
                    data
                )

                return job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1.from_dict(
                    data
                )

                return job_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2.from_dict(
                    data
                )

                return job_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType0
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType1
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemJobStatusType2
                | Unset,
                data,
            )

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item = cls(
            employees_to_match=employees_to_match,
            employee_filters=employee_filters,
            job_status=job_status,
        )

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item

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
