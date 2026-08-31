from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_talent_flow_response_200_output_direction import GetTalentFlowResponse200OutputDirection

if TYPE_CHECKING:
    from ..models.get_talent_flow_response_200_output_breakdowns import GetTalentFlowResponse200OutputBreakdowns
    from ..models.get_talent_flow_response_200_output_company import GetTalentFlowResponse200OutputCompany
    from ..models.get_talent_flow_response_200_output_company_buckets_item import (
        GetTalentFlowResponse200OutputCompanyBucketsItem,
    )
    from ..models.get_talent_flow_response_200_output_tenure_months import GetTalentFlowResponse200OutputTenureMonths
    from ..models.get_talent_flow_response_200_output_window import GetTalentFlowResponse200OutputWindow
    from ..models.get_talent_flow_response_200_output_years_of_experience import (
        GetTalentFlowResponse200OutputYearsOfExperience,
    )


T = TypeVar("T", bound="GetTalentFlowResponse200Output")


@_attrs_define
class GetTalentFlowResponse200Output:
    """
    Attributes:
        direction (GetTalentFlowResponse200OutputDirection): Direction of the analysis.
        company (GetTalentFlowResponse200OutputCompany): Company that was analyzed.
        window (GetTalentFlowResponse200OutputWindow): Time window for the analysis.
        people_count (int): Number of people who joined (joiners) or left (leavers) the company within the analysis
            window.
        company_buckets (list[GetTalentFlowResponse200OutputCompanyBucketsItem]): Where people came from (joiners) or
            went to (leavers), sorted by count descending.
        years_of_experience (GetTalentFlowResponse200OutputYearsOfExperience): Years of experience at the time of the
            join or leave event.
        tenure_months (GetTalentFlowResponse200OutputTenureMonths): Tenure at the analyzed company, in months.
        breakdowns (GetTalentFlowResponse200OutputBreakdowns): Categorical breakdowns of the analyzed population.
        generated_at (str): ISO 8601 timestamp when the report was generated.
        markdown_summary (str): Human-readable markdown summary of the report, including tables and charts.
    """

    direction: GetTalentFlowResponse200OutputDirection
    company: GetTalentFlowResponse200OutputCompany
    window: GetTalentFlowResponse200OutputWindow
    people_count: int
    company_buckets: list[GetTalentFlowResponse200OutputCompanyBucketsItem]
    years_of_experience: GetTalentFlowResponse200OutputYearsOfExperience
    tenure_months: GetTalentFlowResponse200OutputTenureMonths
    breakdowns: GetTalentFlowResponse200OutputBreakdowns
    generated_at: str
    markdown_summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        company = self.company.to_dict()

        window = self.window.to_dict()

        people_count = self.people_count

        company_buckets = []
        for company_buckets_item_data in self.company_buckets:
            company_buckets_item = company_buckets_item_data.to_dict()
            company_buckets.append(company_buckets_item)

        years_of_experience = self.years_of_experience.to_dict()

        tenure_months = self.tenure_months.to_dict()

        breakdowns = self.breakdowns.to_dict()

        generated_at = self.generated_at

        markdown_summary = self.markdown_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "company": company,
                "window": window,
                "peopleCount": people_count,
                "companyBuckets": company_buckets,
                "yearsOfExperience": years_of_experience,
                "tenureMonths": tenure_months,
                "breakdowns": breakdowns,
                "generatedAt": generated_at,
                "markdownSummary": markdown_summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_response_200_output_breakdowns import (
            GetTalentFlowResponse200OutputBreakdowns,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_response_200_output_company import (
            GetTalentFlowResponse200OutputCompany,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_response_200_output_company_buckets_item import (
            GetTalentFlowResponse200OutputCompanyBucketsItem,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_response_200_output_tenure_months import (
            GetTalentFlowResponse200OutputTenureMonths,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_response_200_output_window import (
            GetTalentFlowResponse200OutputWindow,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_response_200_output_years_of_experience import (
            GetTalentFlowResponse200OutputYearsOfExperience,  # noqa: PLC0415
        )

        d = dict(src_dict)
        direction = GetTalentFlowResponse200OutputDirection(d.pop("direction"))

        company = GetTalentFlowResponse200OutputCompany.from_dict(d.pop("company"))

        window = GetTalentFlowResponse200OutputWindow.from_dict(d.pop("window"))

        people_count = d.pop("peopleCount")

        company_buckets = []
        _company_buckets = d.pop("companyBuckets")
        for company_buckets_item_data in _company_buckets:
            company_buckets_item = GetTalentFlowResponse200OutputCompanyBucketsItem.from_dict(company_buckets_item_data)

            company_buckets.append(company_buckets_item)

        years_of_experience = GetTalentFlowResponse200OutputYearsOfExperience.from_dict(d.pop("yearsOfExperience"))

        tenure_months = GetTalentFlowResponse200OutputTenureMonths.from_dict(d.pop("tenureMonths"))

        breakdowns = GetTalentFlowResponse200OutputBreakdowns.from_dict(d.pop("breakdowns"))

        generated_at = d.pop("generatedAt")

        markdown_summary = d.pop("markdownSummary")

        get_talent_flow_response_200_output = cls(
            direction=direction,
            company=company,
            window=window,
            people_count=people_count,
            company_buckets=company_buckets,
            years_of_experience=years_of_experience,
            tenure_months=tenure_months,
            breakdowns=breakdowns,
            generated_at=generated_at,
            markdown_summary=markdown_summary,
        )

        get_talent_flow_response_200_output.additional_properties = d
        return get_talent_flow_response_200_output

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
