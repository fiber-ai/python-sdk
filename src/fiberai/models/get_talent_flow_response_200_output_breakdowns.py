from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_talent_flow_response_200_output_breakdowns_by_country_item import (
        GetTalentFlowResponse200OutputBreakdownsByCountryItem,
    )
    from ..models.get_talent_flow_response_200_output_breakdowns_by_job_function_item import (
        GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem,
    )
    from ..models.get_talent_flow_response_200_output_breakdowns_by_metro_item import (
        GetTalentFlowResponse200OutputBreakdownsByMetroItem,
    )
    from ..models.get_talent_flow_response_200_output_breakdowns_by_school_item import (
        GetTalentFlowResponse200OutputBreakdownsBySchoolItem,
    )
    from ..models.get_talent_flow_response_200_output_breakdowns_by_seniority_item import (
        GetTalentFlowResponse200OutputBreakdownsBySeniorityItem,
    )
    from ..models.get_talent_flow_response_200_output_breakdowns_by_years_of_experience_item import (
        GetTalentFlowResponse200OutputBreakdownsByYearsOfExperienceItem,
    )


T = TypeVar("T", bound="GetTalentFlowResponse200OutputBreakdowns")


@_attrs_define
class GetTalentFlowResponse200OutputBreakdowns:
    """Categorical breakdowns of the analyzed population.

    Attributes:
        by_seniority (list[GetTalentFlowResponse200OutputBreakdownsBySeniorityItem]): Breakdown by seniority level.
        by_job_function (list[GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem]): Breakdown by job function.
        by_country (list[GetTalentFlowResponse200OutputBreakdownsByCountryItem]): Breakdown by country.
        by_metro (list[GetTalentFlowResponse200OutputBreakdownsByMetroItem]): Breakdown by metro area.
        by_school (list[GetTalentFlowResponse200OutputBreakdownsBySchoolItem]): Breakdown by school or university.
        by_years_of_experience (list[GetTalentFlowResponse200OutputBreakdownsByYearsOfExperienceItem]): Years of
            experience distribution histogram.
    """

    by_seniority: list[GetTalentFlowResponse200OutputBreakdownsBySeniorityItem]
    by_job_function: list[GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem]
    by_country: list[GetTalentFlowResponse200OutputBreakdownsByCountryItem]
    by_metro: list[GetTalentFlowResponse200OutputBreakdownsByMetroItem]
    by_school: list[GetTalentFlowResponse200OutputBreakdownsBySchoolItem]
    by_years_of_experience: list[GetTalentFlowResponse200OutputBreakdownsByYearsOfExperienceItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_seniority = []
        for by_seniority_item_data in self.by_seniority:
            by_seniority_item = by_seniority_item_data.to_dict()
            by_seniority.append(by_seniority_item)

        by_job_function = []
        for by_job_function_item_data in self.by_job_function:
            by_job_function_item = by_job_function_item_data.to_dict()
            by_job_function.append(by_job_function_item)

        by_country = []
        for by_country_item_data in self.by_country:
            by_country_item = by_country_item_data.to_dict()
            by_country.append(by_country_item)

        by_metro = []
        for by_metro_item_data in self.by_metro:
            by_metro_item = by_metro_item_data.to_dict()
            by_metro.append(by_metro_item)

        by_school = []
        for by_school_item_data in self.by_school:
            by_school_item = by_school_item_data.to_dict()
            by_school.append(by_school_item)

        by_years_of_experience = []
        for by_years_of_experience_item_data in self.by_years_of_experience:
            by_years_of_experience_item = by_years_of_experience_item_data.to_dict()
            by_years_of_experience.append(by_years_of_experience_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bySeniority": by_seniority,
                "byJobFunction": by_job_function,
                "byCountry": by_country,
                "byMetro": by_metro,
                "bySchool": by_school,
                "byYearsOfExperience": by_years_of_experience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_response_200_output_breakdowns_by_country_item import (
            GetTalentFlowResponse200OutputBreakdownsByCountryItem,
        )
        from ..models.get_talent_flow_response_200_output_breakdowns_by_job_function_item import (
            GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem,
        )
        from ..models.get_talent_flow_response_200_output_breakdowns_by_metro_item import (
            GetTalentFlowResponse200OutputBreakdownsByMetroItem,
        )
        from ..models.get_talent_flow_response_200_output_breakdowns_by_school_item import (
            GetTalentFlowResponse200OutputBreakdownsBySchoolItem,
        )
        from ..models.get_talent_flow_response_200_output_breakdowns_by_seniority_item import (
            GetTalentFlowResponse200OutputBreakdownsBySeniorityItem,
        )
        from ..models.get_talent_flow_response_200_output_breakdowns_by_years_of_experience_item import (
            GetTalentFlowResponse200OutputBreakdownsByYearsOfExperienceItem,
        )

        d = dict(src_dict)
        by_seniority = []
        _by_seniority = d.pop("bySeniority")
        for by_seniority_item_data in _by_seniority:
            by_seniority_item = GetTalentFlowResponse200OutputBreakdownsBySeniorityItem.from_dict(
                by_seniority_item_data
            )

            by_seniority.append(by_seniority_item)

        by_job_function = []
        _by_job_function = d.pop("byJobFunction")
        for by_job_function_item_data in _by_job_function:
            by_job_function_item = GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem.from_dict(
                by_job_function_item_data
            )

            by_job_function.append(by_job_function_item)

        by_country = []
        _by_country = d.pop("byCountry")
        for by_country_item_data in _by_country:
            by_country_item = GetTalentFlowResponse200OutputBreakdownsByCountryItem.from_dict(by_country_item_data)

            by_country.append(by_country_item)

        by_metro = []
        _by_metro = d.pop("byMetro")
        for by_metro_item_data in _by_metro:
            by_metro_item = GetTalentFlowResponse200OutputBreakdownsByMetroItem.from_dict(by_metro_item_data)

            by_metro.append(by_metro_item)

        by_school = []
        _by_school = d.pop("bySchool")
        for by_school_item_data in _by_school:
            by_school_item = GetTalentFlowResponse200OutputBreakdownsBySchoolItem.from_dict(by_school_item_data)

            by_school.append(by_school_item)

        by_years_of_experience = []
        _by_years_of_experience = d.pop("byYearsOfExperience")
        for by_years_of_experience_item_data in _by_years_of_experience:
            by_years_of_experience_item = GetTalentFlowResponse200OutputBreakdownsByYearsOfExperienceItem.from_dict(
                by_years_of_experience_item_data
            )

            by_years_of_experience.append(by_years_of_experience_item)

        get_talent_flow_response_200_output_breakdowns = cls(
            by_seniority=by_seniority,
            by_job_function=by_job_function,
            by_country=by_country,
            by_metro=by_metro,
            by_school=by_school,
            by_years_of_experience=by_years_of_experience,
        )

        get_talent_flow_response_200_output_breakdowns.additional_properties = d
        return get_talent_flow_response_200_output_breakdowns

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
