from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_2_status import (
    TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2Status,
)

T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2")


@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2:
    """
    Attributes:
        status (TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2Status):
    """

    status: TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2Status(d.pop("status"))

        text_to_profile_search_params_response_200_output_search_params_job_status_type_2 = cls(
            status=status,
        )

        text_to_profile_search_params_response_200_output_search_params_job_status_type_2.additional_properties = d
        return text_to_profile_search_params_response_200_output_search_params_job_status_type_2

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
