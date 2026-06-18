from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item,
    )


T = TypeVar(
    "T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0"
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0:
    """
    Attributes:
        country_code (list[str] | None | Unset):
        job_title (list[str] | None | Unset):
        recently_hired (list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFil
            tersType0RecentlyHiredType0Item] | None | Unset):
    """

    country_code: list[str] | None | Unset = UNSET
    job_title: list[str] | None | Unset = UNSET
    recently_hired: (
        list[
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item
        ]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code: list[str] | None | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, list):
            country_code = self.country_code

        else:
            country_code = self.country_code

        job_title: list[str] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, list):
            job_title = self.job_title

        else:
            job_title = self.job_title

        recently_hired: list[dict[str, Any]] | None | Unset
        if isinstance(self.recently_hired, Unset):
            recently_hired = UNSET
        elif isinstance(self.recently_hired, list):
            recently_hired = []
            for recently_hired_type_0_item_data in self.recently_hired:
                recently_hired_type_0_item = recently_hired_type_0_item_data.to_dict()
                recently_hired.append(recently_hired_type_0_item)

        else:
            recently_hired = self.recently_hired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if recently_hired is not UNSET:
            field_dict["recentlyHired"] = recently_hired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item,
        )

        d = dict(src_dict)

        def _parse_country_code(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                country_code_type_0 = cast(list[str], data)

                return country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

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

        def _parse_recently_hired(
            data: object,
        ) -> (
            list[
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recently_hired_type_0 = []
                _recently_hired_type_0 = data
                for recently_hired_type_0_item_data in _recently_hired_type_0:
                    recently_hired_type_0_item = CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item.from_dict(
                        recently_hired_type_0_item_data
                    )

                    recently_hired_type_0.append(recently_hired_type_0_item)

                return recently_hired_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0Item
                ]
                | None
                | Unset,
                data,
            )

        recently_hired = _parse_recently_hired(d.pop("recentlyHired", UNSET))

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0 = cls(
            country_code=country_code,
            job_title=job_title,
            recently_hired=recently_hired,
        )

        create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_employees_type_0_rules_item_employee_filters_type_0

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
