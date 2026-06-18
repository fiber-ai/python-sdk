from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1,
    )


T = TypeVar(
    "T",
    bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item",
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item:
    """
    Attributes:
        hired_at (CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0Re
            centlyHiredType0ItemHiredAtType0 | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesI
            temEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1 | None | Unset):
        job_title (list[str] | None | Unset):
    """

    hired_at: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0
        | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1
        | None
        | Unset
    ) = UNSET
    job_title: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1,
        )

        hired_at: dict[str, Any] | None | Unset
        if isinstance(self.hired_at, Unset):
            hired_at = UNSET
        elif isinstance(
            self.hired_at,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0,
        ):
            hired_at = self.hired_at.to_dict()
        elif isinstance(
            self.hired_at,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1,
        ):
            hired_at = self.hired_at.to_dict()
        else:
            hired_at = self.hired_at

        job_title: list[str] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, list):
            job_title = self.job_title

        else:
            job_title = self.job_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hired_at is not UNSET:
            field_dict["hiredAt"] = hired_at
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1,
        )

        d = dict(src_dict)

        def _parse_hired_at(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0
            | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1
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
                hired_at_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0.from_dict(
                    data
                )

                return hired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hired_at_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1.from_dict(
                    data
                )

                return hired_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0
                | CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1
                | None
                | Unset,
                data,
            )

        hired_at = _parse_hired_at(d.pop("hiredAt", UNSET))

        def _parse_job_title(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_title_type_0 = cast(list[str], data)

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item = cls(
            hired_at=hired_at,
            job_title=job_title,
        )

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item

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
