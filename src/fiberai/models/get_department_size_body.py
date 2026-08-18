from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_department_size_body_company_type_0 import GetDepartmentSizeBodyCompanyType0
    from ..models.get_department_size_body_company_type_1 import GetDepartmentSizeBodyCompanyType1
    from ..models.get_department_size_body_company_type_2 import GetDepartmentSizeBodyCompanyType2
    from ..models.get_department_size_body_company_type_3 import GetDepartmentSizeBodyCompanyType3
    from ..models.get_department_size_body_departments_item import GetDepartmentSizeBodyDepartmentsItem


T = TypeVar("T", bound="GetDepartmentSizeBody")


@_attrs_define
class GetDepartmentSizeBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company (GetDepartmentSizeBodyCompanyType0 | GetDepartmentSizeBodyCompanyType1 |
            GetDepartmentSizeBodyCompanyType2 | GetDepartmentSizeBodyCompanyType3): Company identifier. Set identifier to
            'linkedinUrl', 'linkedinSlug', 'linkedinOrgId', or 'domain' and provide the corresponding value.
        departments (list[GetDepartmentSizeBodyDepartmentsItem]): Departments to size. Each is counted independently
            against ALL current employees, so overlapping definitions may count the same person in more than one department.
    """

    api_key: str
    company: (
        GetDepartmentSizeBodyCompanyType0
        | GetDepartmentSizeBodyCompanyType1
        | GetDepartmentSizeBodyCompanyType2
        | GetDepartmentSizeBodyCompanyType3
    )
    departments: list[GetDepartmentSizeBodyDepartmentsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_department_size_body_company_type_0 import GetDepartmentSizeBodyCompanyType0
        from ..models.get_department_size_body_company_type_1 import GetDepartmentSizeBodyCompanyType1
        from ..models.get_department_size_body_company_type_2 import GetDepartmentSizeBodyCompanyType2

        api_key = self.api_key

        company: dict[str, Any]
        if isinstance(self.company, GetDepartmentSizeBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, GetDepartmentSizeBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, GetDepartmentSizeBodyCompanyType2):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        departments = []
        for departments_item_data in self.departments:
            departments_item = departments_item_data.to_dict()
            departments.append(departments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "company": company,
                "departments": departments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_department_size_body_company_type_0 import GetDepartmentSizeBodyCompanyType0
        from ..models.get_department_size_body_company_type_1 import GetDepartmentSizeBodyCompanyType1
        from ..models.get_department_size_body_company_type_2 import GetDepartmentSizeBodyCompanyType2
        from ..models.get_department_size_body_company_type_3 import GetDepartmentSizeBodyCompanyType3
        from ..models.get_department_size_body_departments_item import GetDepartmentSizeBodyDepartmentsItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company(
            data: object,
        ) -> (
            GetDepartmentSizeBodyCompanyType0
            | GetDepartmentSizeBodyCompanyType1
            | GetDepartmentSizeBodyCompanyType2
            | GetDepartmentSizeBodyCompanyType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = GetDepartmentSizeBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = GetDepartmentSizeBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = GetDepartmentSizeBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_3 = GetDepartmentSizeBodyCompanyType3.from_dict(data)

            return company_type_3

        company = _parse_company(d.pop("company"))

        departments = []
        _departments = d.pop("departments")
        for departments_item_data in _departments:
            departments_item = GetDepartmentSizeBodyDepartmentsItem.from_dict(departments_item_data)

            departments.append(departments_item)

        get_department_size_body = cls(
            api_key=api_key,
            company=company,
            departments=departments,
        )

        get_department_size_body.additional_properties = d
        return get_department_size_body

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
