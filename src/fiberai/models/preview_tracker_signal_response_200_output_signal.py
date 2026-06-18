from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.preview_tracker_signal_response_200_output_signal_change_data_item import (
        PreviewTrackerSignalResponse200OutputSignalChangeDataItem,
    )


T = TypeVar("T", bound="PreviewTrackerSignalResponse200OutputSignal")


@_attrs_define
class PreviewTrackerSignalResponse200OutputSignal:
    """
    Attributes:
        type_ (str): Rule type slug (e.g. person_connections_milestone).
        summary (str): Human-readable description of what changed.
        change_data (list[PreviewTrackerSignalResponse200OutputSignalChangeDataItem]): Structured payload describing
            what changed.
        is_dummy (bool):
    """

    type_: str
    summary: str
    change_data: list[PreviewTrackerSignalResponse200OutputSignalChangeDataItem]
    is_dummy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        summary = self.summary

        change_data = []
        for change_data_item_data in self.change_data:
            change_data_item = change_data_item_data.to_dict()
            change_data.append(change_data_item)

        is_dummy = self.is_dummy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "summary": summary,
                "changeData": change_data,
                "isDummy": is_dummy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_tracker_signal_response_200_output_signal_change_data_item import (
            PreviewTrackerSignalResponse200OutputSignalChangeDataItem,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        summary = d.pop("summary")

        change_data = []
        _change_data = d.pop("changeData")
        for change_data_item_data in _change_data:
            change_data_item = PreviewTrackerSignalResponse200OutputSignalChangeDataItem.from_dict(
                change_data_item_data
            )

            change_data.append(change_data_item)

        is_dummy = d.pop("isDummy")

        preview_tracker_signal_response_200_output_signal = cls(
            type_=type_,
            summary=summary,
            change_data=change_data,
            is_dummy=is_dummy,
        )

        preview_tracker_signal_response_200_output_signal.additional_properties = d
        return preview_tracker_signal_response_200_output_signal

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
