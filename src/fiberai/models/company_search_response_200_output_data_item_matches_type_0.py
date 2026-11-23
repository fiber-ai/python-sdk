from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item import (
        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item,
    )
    from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0 import (
        CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0,
    )


T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0:
    """The people and job postings that made this company match. Only returned when `includeMatches` is true.

    Attributes:
        employee_rules (list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item] | None | Unset):
            One entry per rule in `searchParams.employees.rules`, in the same order. Null when the search has no employees
            filter.
        job_postings (CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0 | None | Unset): The postings
            behind `searchParams.jobPostingsV2`. Null when the search has no job postings filter.
    """

    employee_rules: list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item] | None | Unset = (
        UNSET
    )
    job_postings: CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0 import (
            CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0,  # noqa: PLC0415
        )

        employee_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.employee_rules, Unset):
            employee_rules = UNSET
        elif isinstance(self.employee_rules, list):
            employee_rules = []
            for employee_rules_type_0_item_data in self.employee_rules:
                employee_rules_type_0_item = employee_rules_type_0_item_data.to_dict()
                employee_rules.append(employee_rules_type_0_item)

        else:
            employee_rules = self.employee_rules

        job_postings: dict[str, Any] | None | Unset
        if isinstance(self.job_postings, Unset):
            job_postings = UNSET
        elif isinstance(self.job_postings, CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0):
            job_postings = self.job_postings.to_dict()
        else:
            job_postings = self.job_postings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_rules is not UNSET:
            field_dict["employee_rules"] = employee_rules
        if job_postings is not UNSET:
            field_dict["job_postings"] = job_postings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item import (
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item,  # noqa: PLC0415
        )
        from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0 import (
            CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_employee_rules(
            data: object,
        ) -> list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employee_rules_type_0 = []
                _employee_rules_type_0 = data
                for employee_rules_type_0_item_data in _employee_rules_type_0:
                    employee_rules_type_0_item = (
                        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item.from_dict(
                            employee_rules_type_0_item_data
                        )
                    )

                    employee_rules_type_0.append(employee_rules_type_0_item)

                return employee_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item] | None | Unset, data
            )

        employee_rules = _parse_employee_rules(d.pop("employee_rules", UNSET))

        def _parse_job_postings(
            data: object,
        ) -> CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_type_0 = CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0.from_dict(data)

                return job_postings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0 | None | Unset, data)

        job_postings = _parse_job_postings(d.pop("job_postings", UNSET))

        company_search_response_200_output_data_item_matches_type_0 = cls(
            employee_rules=employee_rules,
            job_postings=job_postings,
        )

        company_search_response_200_output_data_item_matches_type_0.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0

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
