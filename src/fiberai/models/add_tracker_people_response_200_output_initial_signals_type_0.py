from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddTrackerPeopleResponse200OutputInitialSignalsType0")


@_attrs_define
class AddTrackerPeopleResponse200OutputInitialSignalsType0:
    """
    Attributes:
        triggered (bool):
        people_queued (int): Number of people queued for initial signal processing.
    """

    triggered: bool
    people_queued: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        triggered = self.triggered

        people_queued = self.people_queued

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "triggered": triggered,
                "peopleQueued": people_queued,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        triggered = d.pop("triggered")

        people_queued = d.pop("peopleQueued")

        add_tracker_people_response_200_output_initial_signals_type_0 = cls(
            triggered=triggered,
            people_queued=people_queued,
        )

        add_tracker_people_response_200_output_initial_signals_type_0.additional_properties = d
        return add_tracker_people_response_200_output_initial_signals_type_0

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
