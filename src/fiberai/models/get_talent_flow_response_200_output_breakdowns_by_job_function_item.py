from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem")


@_attrs_define
class GetTalentFlowResponse200OutputBreakdownsByJobFunctionItem:
    """
    Attributes:
        job_function (str): Job function label.
        count (int): Number of people in this function.
        percent (float): Percentage of total people (0-100).
    """

    job_function: str
    count: int
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_function = self.job_function

        count = self.count

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobFunction": job_function,
                "count": count,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_function = d.pop("jobFunction")

        count = d.pop("count")

        percent = d.pop("percent")

        get_talent_flow_response_200_output_breakdowns_by_job_function_item = cls(
            job_function=job_function,
            count=count,
            percent=percent,
        )

        get_talent_flow_response_200_output_breakdowns_by_job_function_item.additional_properties = d
        return get_talent_flow_response_200_output_breakdowns_by_job_function_item

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
