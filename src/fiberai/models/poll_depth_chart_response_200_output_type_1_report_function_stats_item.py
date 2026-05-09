from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollDepthChartResponse200OutputType1ReportFunctionStatsItem")


@_attrs_define
class PollDepthChartResponse200OutputType1ReportFunctionStatsItem:
    """
    Attributes:
        function (str): Functional area (e.g. Engineering, Sales/GTM, Marketing)
        total_employees (float): Total employees in this function
        average_tenure_months (float | None): Average tenure in months across all seniority levels in this function
    """

    function: str
    total_employees: float
    average_tenure_months: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function

        total_employees = self.total_employees

        average_tenure_months: float | None
        average_tenure_months = self.average_tenure_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "totalEmployees": total_employees,
                "averageTenureMonths": average_tenure_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function = d.pop("function")

        total_employees = d.pop("totalEmployees")

        def _parse_average_tenure_months(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_tenure_months = _parse_average_tenure_months(d.pop("averageTenureMonths"))

        poll_depth_chart_response_200_output_type_1_report_function_stats_item = cls(
            function=function,
            total_employees=total_employees,
            average_tenure_months=average_tenure_months,
        )

        poll_depth_chart_response_200_output_type_1_report_function_stats_item.additional_properties = d
        return poll_depth_chart_response_200_output_type_1_report_function_stats_item

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
