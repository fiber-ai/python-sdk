from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTalentFlowResponse200OutputBreakdownsBySeniorityItem")


@_attrs_define
class GetTalentFlowResponse200OutputBreakdownsBySeniorityItem:
    """
    Attributes:
        seniority (str): Seniority level label.
        count (int): Number of people at this seniority.
        percent (float): Percentage of total people (0-100).
    """

    seniority: str
    count: int
    percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seniority = self.seniority

        count = self.count

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seniority": seniority,
                "count": count,
                "percent": percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seniority = d.pop("seniority")

        count = d.pop("count")

        percent = d.pop("percent")

        get_talent_flow_response_200_output_breakdowns_by_seniority_item = cls(
            seniority=seniority,
            count=count,
            percent=percent,
        )

        get_talent_flow_response_200_output_breakdowns_by_seniority_item.additional_properties = d
        return get_talent_flow_response_200_output_breakdowns_by_seniority_item

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
