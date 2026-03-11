from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.build_audience_response_200_output_status import BuildAudienceResponse200OutputStatus

T = TypeVar("T", bound="BuildAudienceResponse200Output")


@_attrs_define
class BuildAudienceResponse200Output:
    """
    Attributes:
        audience_id (str): Unique ID of the audience
        status (BuildAudienceResponse200OutputStatus): Status indicating the build has started
        message (str): Details about the build status
    """

    audience_id: str
    status: BuildAudienceResponse200OutputStatus
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_id = self.audience_id

        status = self.status.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceId": audience_id,
                "status": status,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        status = BuildAudienceResponse200OutputStatus(d.pop("status"))

        message = d.pop("message")

        build_audience_response_200_output = cls(
            audience_id=audience_id,
            status=status,
            message=message,
        )

        build_audience_response_200_output.additional_properties = d
        return build_audience_response_200_output

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
