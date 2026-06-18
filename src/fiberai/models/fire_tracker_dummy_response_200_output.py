from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fire_tracker_dummy_response_200_output_signals_item import (
        FireTrackerDummyResponse200OutputSignalsItem,
    )


T = TypeVar("T", bound="FireTrackerDummyResponse200Output")


@_attrs_define
class FireTrackerDummyResponse200Output:
    """
    Attributes:
        signals (list[FireTrackerDummyResponse200OutputSignalsItem]):
    """

    signals: list[FireTrackerDummyResponse200OutputSignalsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signals": signals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fire_tracker_dummy_response_200_output_signals_item import (
            FireTrackerDummyResponse200OutputSignalsItem,
        )

        d = dict(src_dict)
        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = FireTrackerDummyResponse200OutputSignalsItem.from_dict(signals_item_data)

            signals.append(signals_item)

        fire_tracker_dummy_response_200_output = cls(
            signals=signals,
        )

        fire_tracker_dummy_response_200_output.additional_properties = d
        return fire_tracker_dummy_response_200_output

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
