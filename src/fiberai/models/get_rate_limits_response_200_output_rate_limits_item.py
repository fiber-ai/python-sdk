from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetRateLimitsResponse200OutputRateLimitsItem")


@_attrs_define
class GetRateLimitsResponse200OutputRateLimitsItem:
    """
    Attributes:
        method (str): HTTP method (e.g. GET, POST)
        path (str): Route path (e.g. /v1/search/people)
        max_ (float): Maximum number of requests allowed in the window
        window_seconds (float | None): Time window duration in seconds (e.g. 60), or null if unavailable
        is_custom (bool): Whether this rate limit is a custom override for your organization
    """

    method: str
    path: str
    max_: float
    window_seconds: float | None
    is_custom: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        path = self.path

        max_ = self.max_

        window_seconds: float | None
        window_seconds = self.window_seconds

        is_custom = self.is_custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "path": path,
                "max": max_,
                "windowSeconds": window_seconds,
                "isCustom": is_custom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method")

        path = d.pop("path")

        max_ = d.pop("max")

        def _parse_window_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        window_seconds = _parse_window_seconds(d.pop("windowSeconds"))

        is_custom = d.pop("isCustom")

        get_rate_limits_response_200_output_rate_limits_item = cls(
            method=method,
            path=path,
            max_=max_,
            window_seconds=window_seconds,
            is_custom=is_custom,
        )

        get_rate_limits_response_200_output_rate_limits_item.additional_properties = d
        return get_rate_limits_response_200_output_rate_limits_item

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
