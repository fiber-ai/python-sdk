from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_depth_chart_response_200_output_type_2_status import PollDepthChartResponse200OutputType2Status

T = TypeVar("T", bound="PollDepthChartResponse200OutputType2")


@_attrs_define
class PollDepthChartResponse200OutputType2:
    """
    Attributes:
        status (PollDepthChartResponse200OutputType2Status): Report generation failed
        error_message (str): Description of why generation failed
    """

    status: PollDepthChartResponse200OutputType2Status
    error_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "errorMessage": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = PollDepthChartResponse200OutputType2Status(d.pop("status"))

        error_message = d.pop("errorMessage")

        poll_depth_chart_response_200_output_type_2 = cls(
            status=status,
            error_message=error_message,
        )

        poll_depth_chart_response_200_output_type_2.additional_properties = d
        return poll_depth_chart_response_200_output_type_2

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
