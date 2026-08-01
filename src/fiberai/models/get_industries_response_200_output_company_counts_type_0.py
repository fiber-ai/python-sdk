from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_industries_response_200_output_company_counts_type_0_crunchbase_industries import (
        GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustries,
    )
    from ..models.get_industries_response_200_output_company_counts_type_0_crunchbase_industry_groups import (
        GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustryGroups,
    )
    from ..models.get_industries_response_200_output_company_counts_type_0_fiber_industries import (
        GetIndustriesResponse200OutputCompanyCountsType0FiberIndustries,
    )
    from ..models.get_industries_response_200_output_company_counts_type_0_linkedin_industries import (
        GetIndustriesResponse200OutputCompanyCountsType0LinkedinIndustries,
    )


T = TypeVar("T", bound="GetIndustriesResponse200OutputCompanyCountsType0")


@_attrs_define
class GetIndustriesResponse200OutputCompanyCountsType0:
    """Number of companies matching each value in the lists

    Attributes:
        fiber_industries (GetIndustriesResponse200OutputCompanyCountsType0FiberIndustries):
        linkedin_industries (GetIndustriesResponse200OutputCompanyCountsType0LinkedinIndustries):
        crunchbase_industries (GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustries):
        crunchbase_industry_groups (GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustryGroups):
    """

    fiber_industries: GetIndustriesResponse200OutputCompanyCountsType0FiberIndustries
    linkedin_industries: GetIndustriesResponse200OutputCompanyCountsType0LinkedinIndustries
    crunchbase_industries: GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustries
    crunchbase_industry_groups: GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustryGroups
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fiber_industries = self.fiber_industries.to_dict()

        linkedin_industries = self.linkedin_industries.to_dict()

        crunchbase_industries = self.crunchbase_industries.to_dict()

        crunchbase_industry_groups = self.crunchbase_industry_groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fiberIndustries": fiber_industries,
                "linkedinIndustries": linkedin_industries,
                "crunchbaseIndustries": crunchbase_industries,
                "crunchbaseIndustryGroups": crunchbase_industry_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_industries_response_200_output_company_counts_type_0_crunchbase_industries import (
            GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustries,
        )
        from ..models.get_industries_response_200_output_company_counts_type_0_crunchbase_industry_groups import (
            GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustryGroups,
        )
        from ..models.get_industries_response_200_output_company_counts_type_0_fiber_industries import (
            GetIndustriesResponse200OutputCompanyCountsType0FiberIndustries,
        )
        from ..models.get_industries_response_200_output_company_counts_type_0_linkedin_industries import (
            GetIndustriesResponse200OutputCompanyCountsType0LinkedinIndustries,
        )

        d = dict(src_dict)
        fiber_industries = GetIndustriesResponse200OutputCompanyCountsType0FiberIndustries.from_dict(
            d.pop("fiberIndustries")
        )

        linkedin_industries = GetIndustriesResponse200OutputCompanyCountsType0LinkedinIndustries.from_dict(
            d.pop("linkedinIndustries")
        )

        crunchbase_industries = GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustries.from_dict(
            d.pop("crunchbaseIndustries")
        )

        crunchbase_industry_groups = GetIndustriesResponse200OutputCompanyCountsType0CrunchbaseIndustryGroups.from_dict(
            d.pop("crunchbaseIndustryGroups")
        )

        get_industries_response_200_output_company_counts_type_0 = cls(
            fiber_industries=fiber_industries,
            linkedin_industries=linkedin_industries,
            crunchbase_industries=crunchbase_industries,
            crunchbase_industry_groups=crunchbase_industry_groups,
        )

        get_industries_response_200_output_company_counts_type_0.additional_properties = d
        return get_industries_response_200_output_company_counts_type_0

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
