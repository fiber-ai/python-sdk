from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_depth_chart_response_200_output_type_1_report_buckets_item import (
        PollDepthChartResponse200OutputType1ReportBucketsItem,
    )
    from ..models.poll_depth_chart_response_200_output_type_1_report_company_info import (
        PollDepthChartResponse200OutputType1ReportCompanyInfo,
    )
    from ..models.poll_depth_chart_response_200_output_type_1_report_function_stats_item import (
        PollDepthChartResponse200OutputType1ReportFunctionStatsItem,
    )
    from ..models.poll_depth_chart_response_200_output_type_1_report_seniority_stats_item import (
        PollDepthChartResponse200OutputType1ReportSeniorityStatsItem,
    )


T = TypeVar("T", bound="PollDepthChartResponse200OutputType1Report")


@_attrs_define
class PollDepthChartResponse200OutputType1Report:
    """The completed depth chart report

    Attributes:
        report_id (str): Unique identifier for this report
        company_info (PollDepthChartResponse200OutputType1ReportCompanyInfo): Company identification details
        total_employees (float): Total number of classified employees in the depth chart
        average_tenure_months (float | None): Overall average tenure in months across all employees
        buckets (list[PollDepthChartResponse200OutputType1ReportBucketsItem]): One entry per function x seniority
            combination with headcount and average tenure. Includes summary stats for each bucket, but does not list the
            people in each bucket.
        seniority_stats (list[PollDepthChartResponse200OutputType1ReportSeniorityStatsItem]): Aggregated headcount and
            tenure per seniority level
        function_stats (list[PollDepthChartResponse200OutputType1ReportFunctionStatsItem]): Aggregated headcount and
            tenure per functional area
        markdown_summary (str): Human-readable markdown summary of the depth chart, including a grid table of employee
            counts by function and seniority
    """

    report_id: str
    company_info: PollDepthChartResponse200OutputType1ReportCompanyInfo
    total_employees: float
    average_tenure_months: float | None
    buckets: list[PollDepthChartResponse200OutputType1ReportBucketsItem]
    seniority_stats: list[PollDepthChartResponse200OutputType1ReportSeniorityStatsItem]
    function_stats: list[PollDepthChartResponse200OutputType1ReportFunctionStatsItem]
    markdown_summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        company_info = self.company_info.to_dict()

        total_employees = self.total_employees

        average_tenure_months: float | None
        average_tenure_months = self.average_tenure_months

        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        seniority_stats = []
        for seniority_stats_item_data in self.seniority_stats:
            seniority_stats_item = seniority_stats_item_data.to_dict()
            seniority_stats.append(seniority_stats_item)

        function_stats = []
        for function_stats_item_data in self.function_stats:
            function_stats_item = function_stats_item_data.to_dict()
            function_stats.append(function_stats_item)

        markdown_summary = self.markdown_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "companyInfo": company_info,
                "totalEmployees": total_employees,
                "averageTenureMonths": average_tenure_months,
                "buckets": buckets,
                "seniorityStats": seniority_stats,
                "functionStats": function_stats,
                "markdownSummary": markdown_summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_depth_chart_response_200_output_type_1_report_buckets_item import (
            PollDepthChartResponse200OutputType1ReportBucketsItem,
        )
        from ..models.poll_depth_chart_response_200_output_type_1_report_company_info import (
            PollDepthChartResponse200OutputType1ReportCompanyInfo,
        )
        from ..models.poll_depth_chart_response_200_output_type_1_report_function_stats_item import (
            PollDepthChartResponse200OutputType1ReportFunctionStatsItem,
        )
        from ..models.poll_depth_chart_response_200_output_type_1_report_seniority_stats_item import (
            PollDepthChartResponse200OutputType1ReportSeniorityStatsItem,
        )

        d = dict(src_dict)
        report_id = d.pop("reportId")

        company_info = PollDepthChartResponse200OutputType1ReportCompanyInfo.from_dict(d.pop("companyInfo"))

        total_employees = d.pop("totalEmployees")

        def _parse_average_tenure_months(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_tenure_months = _parse_average_tenure_months(d.pop("averageTenureMonths"))

        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = PollDepthChartResponse200OutputType1ReportBucketsItem.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        seniority_stats = []
        _seniority_stats = d.pop("seniorityStats")
        for seniority_stats_item_data in _seniority_stats:
            seniority_stats_item = PollDepthChartResponse200OutputType1ReportSeniorityStatsItem.from_dict(
                seniority_stats_item_data
            )

            seniority_stats.append(seniority_stats_item)

        function_stats = []
        _function_stats = d.pop("functionStats")
        for function_stats_item_data in _function_stats:
            function_stats_item = PollDepthChartResponse200OutputType1ReportFunctionStatsItem.from_dict(
                function_stats_item_data
            )

            function_stats.append(function_stats_item)

        markdown_summary = d.pop("markdownSummary")

        poll_depth_chart_response_200_output_type_1_report = cls(
            report_id=report_id,
            company_info=company_info,
            total_employees=total_employees,
            average_tenure_months=average_tenure_months,
            buckets=buckets,
            seniority_stats=seniority_stats,
            function_stats=function_stats,
            markdown_summary=markdown_summary,
        )

        poll_depth_chart_response_200_output_type_1_report.additional_properties = d
        return poll_depth_chart_response_200_output_type_1_report

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
