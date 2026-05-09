from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_depth_chart_response_200_output_type_1_status import PollDepthChartResponse200OutputType1Status

if TYPE_CHECKING:
    from ..models.poll_depth_chart_response_200_output_type_1_report import PollDepthChartResponse200OutputType1Report


T = TypeVar("T", bound="PollDepthChartResponse200OutputType1")


@_attrs_define
class PollDepthChartResponse200OutputType1:
    """
    Attributes:
        status (PollDepthChartResponse200OutputType1Status): Report generation succeeded
        report (PollDepthChartResponse200OutputType1Report): The completed depth chart report
    """

    status: PollDepthChartResponse200OutputType1Status
    report: PollDepthChartResponse200OutputType1Report
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        report = self.report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "report": report,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_depth_chart_response_200_output_type_1_report import (
            PollDepthChartResponse200OutputType1Report,
        )

        d = dict(src_dict)
        status = PollDepthChartResponse200OutputType1Status(d.pop("status"))

        report = PollDepthChartResponse200OutputType1Report.from_dict(d.pop("report"))

        poll_depth_chart_response_200_output_type_1 = cls(
            status=status,
            report=report,
        )

        poll_depth_chart_response_200_output_type_1.additional_properties = d
        return poll_depth_chart_response_200_output_type_1

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
