from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tracker_signal_output import TrackerSignalOutput


T = TypeVar("T", bound="ListTrackerSignalsResponse200Output")


@_attrs_define
class ListTrackerSignalsResponse200Output:
    """
    Attributes:
        signals (list[TrackerSignalOutput]):
        next_cursor (None | str): Cursor for fetching the next page. Null when there are no more results.
    """

    signals: list[TrackerSignalOutput]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signals": signals,
                "nextCursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_signal_output import TrackerSignalOutput  # noqa: PLC0415

        d = dict(src_dict)
        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = TrackerSignalOutput.from_dict(signals_item_data)

            signals.append(signals_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        list_tracker_signals_response_200_output = cls(
            signals=signals,
            next_cursor=next_cursor,
        )

        list_tracker_signals_response_200_output.additional_properties = d
        return list_tracker_signals_response_200_output

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
