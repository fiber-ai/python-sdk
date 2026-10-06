from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RescheduleTrackerPersonListResponse200Output")


@_attrs_define
class RescheduleTrackerPersonListResponse200Output:
    """
    Attributes:
        new_next_refresh_at (str): When the next refresh is now scheduled to run.
        message (str): Human-readable confirmation of the new schedule.
        previous_next_refresh_at (None | str | Unset): When the next refresh was scheduled before this call. Null if the
            list had no refresh scheduled yet.
    """

    new_next_refresh_at: str
    message: str
    previous_next_refresh_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_next_refresh_at = self.new_next_refresh_at

        message = self.message

        previous_next_refresh_at: None | str | Unset
        if isinstance(self.previous_next_refresh_at, Unset):
            previous_next_refresh_at = UNSET
        else:
            previous_next_refresh_at = self.previous_next_refresh_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newNextRefreshAt": new_next_refresh_at,
                "message": message,
            }
        )
        if previous_next_refresh_at is not UNSET:
            field_dict["previousNextRefreshAt"] = previous_next_refresh_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_next_refresh_at = d.pop("newNextRefreshAt")

        message = d.pop("message")

        def _parse_previous_next_refresh_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_next_refresh_at = _parse_previous_next_refresh_at(d.pop("previousNextRefreshAt", UNSET))

        reschedule_tracker_person_list_response_200_output = cls(
            new_next_refresh_at=new_next_refresh_at,
            message=message,
            previous_next_refresh_at=previous_next_refresh_at,
        )

        reschedule_tracker_person_list_response_200_output.additional_properties = d
        return reschedule_tracker_person_list_response_200_output

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
