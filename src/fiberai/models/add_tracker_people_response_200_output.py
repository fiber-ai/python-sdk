from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_tracker_people_response_200_output_initial_signals_type_0 import (
        AddTrackerPeopleResponse200OutputInitialSignalsType0,
    )
    from ..models.add_tracker_people_response_200_output_initial_signals_type_1 import (
        AddTrackerPeopleResponse200OutputInitialSignalsType1,
    )
    from ..models.add_tracker_people_response_200_output_invalid_people_item import (
        AddTrackerPeopleResponse200OutputInvalidPeopleItem,
    )


T = TypeVar("T", bound="AddTrackerPeopleResponse200Output")


@_attrs_define
class AddTrackerPeopleResponse200Output:
    """
    Attributes:
        added (int): Number of people fully resolved and added to the list.
        pending (int): Number of people accepted and added to the list but whose profile is still being resolved in the
            background. They become fully tracked once resolution finishes (usually within minutes); a profile that turns
            out not to exist is dropped automatically.
        skipped (int): Number of people not added because they were already in the list or appeared more than once in
            this request. People that could not be resolved are reported in invalidPeople, not here.
        invalid_people (list[AddTrackerPeopleResponse200OutputInvalidPeopleItem]): Details on any people that could not
            be added.
        initial_signals (AddTrackerPeopleResponse200OutputInitialSignalsType0 |
            AddTrackerPeopleResponse200OutputInitialSignalsType1): Status of the initial signals request.
        next_refresh_at (datetime.datetime | None | Unset): When the list is next scheduled to refresh — the first check
            that can produce signals for the entities you just added. Null for a list that has not been scheduled yet; its
            first check runs within about an hour and sets the schedule.
    """

    added: int
    pending: int
    skipped: int
    invalid_people: list[AddTrackerPeopleResponse200OutputInvalidPeopleItem]
    initial_signals: (
        AddTrackerPeopleResponse200OutputInitialSignalsType0 | AddTrackerPeopleResponse200OutputInitialSignalsType1
    )
    next_refresh_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_tracker_people_response_200_output_initial_signals_type_0 import (
            AddTrackerPeopleResponse200OutputInitialSignalsType0,  # noqa: PLC0415
        )

        added = self.added

        pending = self.pending

        skipped = self.skipped

        invalid_people = []
        for invalid_people_item_data in self.invalid_people:
            invalid_people_item = invalid_people_item_data.to_dict()
            invalid_people.append(invalid_people_item)

        initial_signals: dict[str, Any]
        if isinstance(self.initial_signals, AddTrackerPeopleResponse200OutputInitialSignalsType0):
            initial_signals = self.initial_signals.to_dict()
        else:
            initial_signals = self.initial_signals.to_dict()

        next_refresh_at: None | str | Unset
        if isinstance(self.next_refresh_at, Unset):
            next_refresh_at = UNSET
        elif isinstance(self.next_refresh_at, datetime.datetime):
            next_refresh_at = self.next_refresh_at.isoformat()
        else:
            next_refresh_at = self.next_refresh_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "pending": pending,
                "skipped": skipped,
                "invalidPeople": invalid_people,
                "initialSignals": initial_signals,
            }
        )
        if next_refresh_at is not UNSET:
            field_dict["nextRefreshAt"] = next_refresh_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_tracker_people_response_200_output_initial_signals_type_0 import (
            AddTrackerPeopleResponse200OutputInitialSignalsType0,  # noqa: PLC0415
        )
        from ..models.add_tracker_people_response_200_output_initial_signals_type_1 import (
            AddTrackerPeopleResponse200OutputInitialSignalsType1,  # noqa: PLC0415
        )
        from ..models.add_tracker_people_response_200_output_invalid_people_item import (
            AddTrackerPeopleResponse200OutputInvalidPeopleItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        added = d.pop("added")

        pending = d.pop("pending")

        skipped = d.pop("skipped")

        invalid_people = []
        _invalid_people = d.pop("invalidPeople")
        for invalid_people_item_data in _invalid_people:
            invalid_people_item = AddTrackerPeopleResponse200OutputInvalidPeopleItem.from_dict(invalid_people_item_data)

            invalid_people.append(invalid_people_item)

        def _parse_initial_signals(
            data: object,
        ) -> (
            AddTrackerPeopleResponse200OutputInitialSignalsType0 | AddTrackerPeopleResponse200OutputInitialSignalsType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_signals_type_0 = AddTrackerPeopleResponse200OutputInitialSignalsType0.from_dict(data)

                return initial_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            initial_signals_type_1 = AddTrackerPeopleResponse200OutputInitialSignalsType1.from_dict(data)

            return initial_signals_type_1

        initial_signals = _parse_initial_signals(d.pop("initialSignals"))

        def _parse_next_refresh_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_refresh_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_refresh_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_refresh_at = _parse_next_refresh_at(d.pop("nextRefreshAt", UNSET))

        add_tracker_people_response_200_output = cls(
            added=added,
            pending=pending,
            skipped=skipped,
            invalid_people=invalid_people,
            initial_signals=initial_signals,
            next_refresh_at=next_refresh_at,
        )

        add_tracker_people_response_200_output.additional_properties = d
        return add_tracker_people_response_200_output

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
