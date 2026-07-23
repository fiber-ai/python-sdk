from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTrackerPersonListBodyInitialSignalsType0")


@_attrs_define
class UpdateTrackerPersonListBodyInitialSignalsType0:
    """When provided, generates signals immediately for recent events (funding rounds, news, job postings, social posts)
    without waiting for the first tracking cycle. Only certain rule types support initial signals.

        Attributes:
            lookback_period_days (int | None | Unset): How many days back from today to search for recent events. Useful for
                bootstrapping a new list without waiting for the first scheduled refresh. Defaults to the list's refresh
                interval if not provided.
    """

    lookback_period_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookback_period_days: int | None | Unset
        if isinstance(self.lookback_period_days, Unset):
            lookback_period_days = UNSET
        else:
            lookback_period_days = self.lookback_period_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookback_period_days is not UNSET:
            field_dict["lookbackPeriodDays"] = lookback_period_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lookback_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_period_days = _parse_lookback_period_days(d.pop("lookbackPeriodDays", UNSET))

        update_tracker_person_list_body_initial_signals_type_0 = cls(
            lookback_period_days=lookback_period_days,
        )

        update_tracker_person_list_body_initial_signals_type_0.additional_properties = d
        return update_tracker_person_list_body_initial_signals_type_0

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
