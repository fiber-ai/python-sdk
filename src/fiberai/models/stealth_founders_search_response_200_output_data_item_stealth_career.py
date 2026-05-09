from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item import (
        StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem,
    )


T = TypeVar("T", bound="StealthFoundersSearchResponse200OutputDataItemStealthCareer")


@_attrs_define
class StealthFoundersSearchResponse200OutputDataItemStealthCareer:
    """
    Attributes:
        transitions (list[StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem]): Signals job-
            listing changes across adjacent snapshots (older -> newer). These changes can provide useful clues while someone
            is in stealth, such as a role shifting from 'Founder @ Stealth Startup' to a more specific label like 'CTO @
            Stealth Fintech Startup'.
        entered_stealth_at (None | str | Unset): When we first observed this person in stealth.
        last_confirmed_in_stealth_at (None | str | Unset): Most recent date where we confirmed that they were still in
            stealth.
        left_stealth_at (None | str | Unset): When we first observed this person no longer in stealth. Null if still in
            stealth.
        days_in_stealth (int | None | Unset): Days spent in stealth. If still in stealth, days from entry to today. If
            left, days from entry to exit.
    """

    transitions: list[StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem]
    entered_stealth_at: None | str | Unset = UNSET
    last_confirmed_in_stealth_at: None | str | Unset = UNSET
    left_stealth_at: None | str | Unset = UNSET
    days_in_stealth: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transitions = []
        for transitions_item_data in self.transitions:
            transitions_item = transitions_item_data.to_dict()
            transitions.append(transitions_item)

        entered_stealth_at: None | str | Unset
        if isinstance(self.entered_stealth_at, Unset):
            entered_stealth_at = UNSET
        else:
            entered_stealth_at = self.entered_stealth_at

        last_confirmed_in_stealth_at: None | str | Unset
        if isinstance(self.last_confirmed_in_stealth_at, Unset):
            last_confirmed_in_stealth_at = UNSET
        else:
            last_confirmed_in_stealth_at = self.last_confirmed_in_stealth_at

        left_stealth_at: None | str | Unset
        if isinstance(self.left_stealth_at, Unset):
            left_stealth_at = UNSET
        else:
            left_stealth_at = self.left_stealth_at

        days_in_stealth: int | None | Unset
        if isinstance(self.days_in_stealth, Unset):
            days_in_stealth = UNSET
        else:
            days_in_stealth = self.days_in_stealth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transitions": transitions,
            }
        )
        if entered_stealth_at is not UNSET:
            field_dict["enteredStealthAt"] = entered_stealth_at
        if last_confirmed_in_stealth_at is not UNSET:
            field_dict["lastConfirmedInStealthAt"] = last_confirmed_in_stealth_at
        if left_stealth_at is not UNSET:
            field_dict["leftStealthAt"] = left_stealth_at
        if days_in_stealth is not UNSET:
            field_dict["daysInStealth"] = days_in_stealth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item import (
            StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem,
        )

        d = dict(src_dict)
        transitions = []
        _transitions = d.pop("transitions")
        for transitions_item_data in _transitions:
            transitions_item = StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem.from_dict(
                transitions_item_data
            )

            transitions.append(transitions_item)

        def _parse_entered_stealth_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entered_stealth_at = _parse_entered_stealth_at(d.pop("enteredStealthAt", UNSET))

        def _parse_last_confirmed_in_stealth_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_confirmed_in_stealth_at = _parse_last_confirmed_in_stealth_at(d.pop("lastConfirmedInStealthAt", UNSET))

        def _parse_left_stealth_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        left_stealth_at = _parse_left_stealth_at(d.pop("leftStealthAt", UNSET))

        def _parse_days_in_stealth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_in_stealth = _parse_days_in_stealth(d.pop("daysInStealth", UNSET))

        stealth_founders_search_response_200_output_data_item_stealth_career = cls(
            transitions=transitions,
            entered_stealth_at=entered_stealth_at,
            last_confirmed_in_stealth_at=last_confirmed_in_stealth_at,
            left_stealth_at=left_stealth_at,
            days_in_stealth=days_in_stealth,
        )

        stealth_founders_search_response_200_output_data_item_stealth_career.additional_properties = d
        return stealth_founders_search_response_200_output_data_item_stealth_career

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
