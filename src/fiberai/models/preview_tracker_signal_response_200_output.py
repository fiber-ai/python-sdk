from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.preview_tracker_signal_response_200_output_signal import PreviewTrackerSignalResponse200OutputSignal


T = TypeVar("T", bound="PreviewTrackerSignalResponse200Output")


@_attrs_define
class PreviewTrackerSignalResponse200Output:
    """
    Attributes:
        signal (PreviewTrackerSignalResponse200OutputSignal):
    """

    signal: PreviewTrackerSignalResponse200OutputSignal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal = self.signal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signal": signal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_tracker_signal_response_200_output_signal import (
            PreviewTrackerSignalResponse200OutputSignal,  # noqa: PLC0415
        )

        d = dict(src_dict)
        signal = PreviewTrackerSignalResponse200OutputSignal.from_dict(d.pop("signal"))

        preview_tracker_signal_response_200_output = cls(
            signal=signal,
        )

        preview_tracker_signal_response_200_output.additional_properties = d
        return preview_tracker_signal_response_200_output

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
