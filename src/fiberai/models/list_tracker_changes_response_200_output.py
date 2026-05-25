from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tracker_signal import TrackerSignal


T = TypeVar("T", bound="ListTrackerChangesResponse200Output")


@_attrs_define
class ListTrackerChangesResponse200Output:
    """
    Attributes:
        changes (list[TrackerSignal]):
        cursor (None | str): Cursor for next page
        has_more (bool): Whether more results exist
    """

    changes: list[TrackerSignal]
    cursor: None | str
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        cursor: None | str
        cursor = self.cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changes": changes,
                "cursor": cursor,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_signal import TrackerSignal

        d = dict(src_dict)
        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = TrackerSignal.from_dict(changes_item_data)

            changes.append(changes_item)

        def _parse_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cursor = _parse_cursor(d.pop("cursor"))

        has_more = d.pop("hasMore")

        list_tracker_changes_response_200_output = cls(
            changes=changes,
            cursor=cursor,
            has_more=has_more,
        )

        list_tracker_changes_response_200_output.additional_properties = d
        return list_tracker_changes_response_200_output

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
