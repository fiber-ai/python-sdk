from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_company_revenue_response_200_output_company import GetCompanyRevenueResponse200OutputCompany
    from ..models.get_company_revenue_response_200_output_revenue_info_type_0 import (
        GetCompanyRevenueResponse200OutputRevenueInfoType0,
    )


T = TypeVar("T", bound="GetCompanyRevenueResponse200Output")


@_attrs_define
class GetCompanyRevenueResponse200Output:
    """
    Attributes:
        company (GetCompanyRevenueResponse200OutputCompany):
        revenue_info (GetCompanyRevenueResponse200OutputRevenueInfoType0 | None | Unset): Revenue information. Null
            means the company was found but no public revenue data is available.
    """

    company: GetCompanyRevenueResponse200OutputCompany
    revenue_info: GetCompanyRevenueResponse200OutputRevenueInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_company_revenue_response_200_output_revenue_info_type_0 import (
            GetCompanyRevenueResponse200OutputRevenueInfoType0,
        )

        company = self.company.to_dict()

        revenue_info: dict[str, Any] | None | Unset
        if isinstance(self.revenue_info, Unset):
            revenue_info = UNSET
        elif isinstance(self.revenue_info, GetCompanyRevenueResponse200OutputRevenueInfoType0):
            revenue_info = self.revenue_info.to_dict()
        else:
            revenue_info = self.revenue_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
            }
        )
        if revenue_info is not UNSET:
            field_dict["revenueInfo"] = revenue_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_company_revenue_response_200_output_company import GetCompanyRevenueResponse200OutputCompany
        from ..models.get_company_revenue_response_200_output_revenue_info_type_0 import (
            GetCompanyRevenueResponse200OutputRevenueInfoType0,
        )

        d = dict(src_dict)
        company = GetCompanyRevenueResponse200OutputCompany.from_dict(d.pop("company"))

        def _parse_revenue_info(data: object) -> GetCompanyRevenueResponse200OutputRevenueInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_info_type_0 = GetCompanyRevenueResponse200OutputRevenueInfoType0.from_dict(data)

                return revenue_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCompanyRevenueResponse200OutputRevenueInfoType0 | None | Unset, data)

        revenue_info = _parse_revenue_info(d.pop("revenueInfo", UNSET))

        get_company_revenue_response_200_output = cls(
            company=company,
            revenue_info=revenue_info,
        )

        get_company_revenue_response_200_output.additional_properties = d
        return get_company_revenue_response_200_output

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
