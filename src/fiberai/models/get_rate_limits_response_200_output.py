from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_rate_limits_response_200_output_rate_limits_item import (
        GetRateLimitsResponse200OutputRateLimitsItem,
    )


T = TypeVar("T", bound="GetRateLimitsResponse200Output")


@_attrs_define
class GetRateLimitsResponse200Output:
    """
    Attributes:
        rate_limits (list[GetRateLimitsResponse200OutputRateLimitsItem]): Rate limits for all available API endpoints
    """

    rate_limits: list[GetRateLimitsResponse200OutputRateLimitsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_limits = []
        for rate_limits_item_data in self.rate_limits:
            rate_limits_item = rate_limits_item_data.to_dict()
            rate_limits.append(rate_limits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rateLimits": rate_limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_rate_limits_response_200_output_rate_limits_item import (
            GetRateLimitsResponse200OutputRateLimitsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        rate_limits = []
        _rate_limits = d.pop("rateLimits")
        for rate_limits_item_data in _rate_limits:
            rate_limits_item = GetRateLimitsResponse200OutputRateLimitsItem.from_dict(rate_limits_item_data)

            rate_limits.append(rate_limits_item)

        get_rate_limits_response_200_output = cls(
            rate_limits=rate_limits,
        )

        get_rate_limits_response_200_output.additional_properties = d
        return get_rate_limits_response_200_output

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
