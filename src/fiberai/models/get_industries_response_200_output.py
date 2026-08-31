from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_industries_response_200_output_company_counts_type_0 import (
        GetIndustriesResponse200OutputCompanyCountsType0,
    )
    from ..models.get_industries_response_200_output_crunchbase_industry_groups import (
        GetIndustriesResponse200OutputCrunchbaseIndustryGroups,
    )


T = TypeVar("T", bound="GetIndustriesResponse200Output")


@_attrs_define
class GetIndustriesResponse200Output:
    """
    Attributes:
        fiber_industries (list[str]): Fiber's standardized list of industries.
        linkedin_industries (list[str]): LinkedIn's list of industries.
        crunchbase_industries (list[str]): Crunchbase's list of industries (a.k.a. Crunchbase categories). Use these
            values to populate the `crunchbaseCategories` filter on the company-search API.
        crunchbase_industry_groups (GetIndustriesResponse200OutputCrunchbaseIndustryGroups): Crunchbase's industry
            groups mapped to their constituent industries. Keys are industry group names, values are arrays of industry
            names belonging to that group. Use the keys to populate the `crunchbaseCategoryGroups` filter on the company-
            search API.
        company_counts (GetIndustriesResponse200OutputCompanyCountsType0 | None | Unset): Shows the number of companies
            in each industry.
    """

    fiber_industries: list[str]
    linkedin_industries: list[str]
    crunchbase_industries: list[str]
    crunchbase_industry_groups: GetIndustriesResponse200OutputCrunchbaseIndustryGroups
    company_counts: GetIndustriesResponse200OutputCompanyCountsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_industries_response_200_output_company_counts_type_0 import (
            GetIndustriesResponse200OutputCompanyCountsType0,  # noqa: PLC0415
        )

        fiber_industries = self.fiber_industries

        linkedin_industries = self.linkedin_industries

        crunchbase_industries = self.crunchbase_industries

        crunchbase_industry_groups = self.crunchbase_industry_groups.to_dict()

        company_counts: dict[str, Any] | None | Unset
        if isinstance(self.company_counts, Unset):
            company_counts = UNSET
        elif isinstance(self.company_counts, GetIndustriesResponse200OutputCompanyCountsType0):
            company_counts = self.company_counts.to_dict()
        else:
            company_counts = self.company_counts

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
        if company_counts is not UNSET:
            field_dict["companyCounts"] = company_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_industries_response_200_output_company_counts_type_0 import (
            GetIndustriesResponse200OutputCompanyCountsType0,  # noqa: PLC0415
        )
        from ..models.get_industries_response_200_output_crunchbase_industry_groups import (
            GetIndustriesResponse200OutputCrunchbaseIndustryGroups,  # noqa: PLC0415
        )

        d = dict(src_dict)
        fiber_industries = cast(list[str], d.pop("fiberIndustries"))

        linkedin_industries = cast(list[str], d.pop("linkedinIndustries"))

        crunchbase_industries = cast(list[str], d.pop("crunchbaseIndustries"))

        crunchbase_industry_groups = GetIndustriesResponse200OutputCrunchbaseIndustryGroups.from_dict(
            d.pop("crunchbaseIndustryGroups")
        )

        def _parse_company_counts(data: object) -> GetIndustriesResponse200OutputCompanyCountsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_counts_type_0 = GetIndustriesResponse200OutputCompanyCountsType0.from_dict(data)

                return company_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetIndustriesResponse200OutputCompanyCountsType0 | None | Unset, data)

        company_counts = _parse_company_counts(d.pop("companyCounts", UNSET))

        get_industries_response_200_output = cls(
            fiber_industries=fiber_industries,
            linkedin_industries=linkedin_industries,
            crunchbase_industries=crunchbase_industries,
            crunchbase_industry_groups=crunchbase_industry_groups,
            company_counts=company_counts,
        )

        get_industries_response_200_output.additional_properties = d
        return get_industries_response_200_output

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
