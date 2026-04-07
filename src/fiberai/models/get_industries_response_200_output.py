from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_industries_response_200_output_crunchbase_industry_groups import (
        GetIndustriesResponse200OutputCrunchbaseIndustryGroups,
    )


T = TypeVar("T", bound="GetIndustriesResponse200Output")


@_attrs_define
class GetIndustriesResponse200Output:
    """
    Attributes:
        fiber_industries (list[str]): Fiber's standardized list of industries
        crunchbase_industries (list[str]): Crunchbase's list of industries
        crunchbase_industry_groups (GetIndustriesResponse200OutputCrunchbaseIndustryGroups): Crunchbase's industry
            groups mapped to their constituent industries. Keys are industry group names, values are arrays of industry
            names belonging to that group.
        linkedin_industries (list[str]): LinkedIn's list of industries
    """

    fiber_industries: list[str]
    crunchbase_industries: list[str]
    crunchbase_industry_groups: GetIndustriesResponse200OutputCrunchbaseIndustryGroups
    linkedin_industries: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fiber_industries = self.fiber_industries

        crunchbase_industries = self.crunchbase_industries

        crunchbase_industry_groups = self.crunchbase_industry_groups.to_dict()

        linkedin_industries = self.linkedin_industries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fiberIndustries": fiber_industries,
                "crunchbaseIndustries": crunchbase_industries,
                "crunchbaseIndustryGroups": crunchbase_industry_groups,
                "linkedinIndustries": linkedin_industries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_industries_response_200_output_crunchbase_industry_groups import (
            GetIndustriesResponse200OutputCrunchbaseIndustryGroups,
        )

        d = dict(src_dict)
        fiber_industries = cast(list[str], d.pop("fiberIndustries"))

        crunchbase_industries = cast(list[str], d.pop("crunchbaseIndustries"))

        crunchbase_industry_groups = GetIndustriesResponse200OutputCrunchbaseIndustryGroups.from_dict(
            d.pop("crunchbaseIndustryGroups")
        )

        linkedin_industries = cast(list[str], d.pop("linkedinIndustries"))

        get_industries_response_200_output = cls(
            fiber_industries=fiber_industries,
            crunchbase_industries=crunchbase_industries,
            crunchbase_industry_groups=crunchbase_industry_groups,
            linkedin_industries=linkedin_industries,
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
