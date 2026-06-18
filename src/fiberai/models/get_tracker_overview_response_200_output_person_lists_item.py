from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_overview_response_200_output_person_lists_item_entity_type import (
    GetTrackerOverviewResponse200OutputPersonListsItemEntityType,
)

T = TypeVar("T", bound="GetTrackerOverviewResponse200OutputPersonListsItem")


@_attrs_define
class GetTrackerOverviewResponse200OutputPersonListsItem:
    """
    Attributes:
        id (str): Tracker list ID.
        name (str): List name.
        entity_type (GetTrackerOverviewResponse200OutputPersonListsItemEntityType): Entity type tracked by this list.
        refresh_interval_days (int): How often the list is checked, in days.
        is_active (bool): Whether the list is actively being checked.
        entity_count (int): Number of active entities currently tracked in this list.
        rule_count (int): Number of active tracking rules on this list. Use the GET endpoint for the full rule details.
        next_refresh_at (datetime.datetime | None): ISO timestamp when at least one entity in this list becomes due for
            its next check. Null if the list has no active entities.
        estimated_credits_per_refresh (float): Credits charged for a full refresh of this list at the org's current
            pricing (entityCount × per-entity cost).
    """

    id: str
    name: str
    entity_type: GetTrackerOverviewResponse200OutputPersonListsItemEntityType
    refresh_interval_days: int
    is_active: bool
    entity_count: int
    rule_count: int
    next_refresh_at: datetime.datetime | None
    estimated_credits_per_refresh: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        entity_type = self.entity_type.value

        refresh_interval_days = self.refresh_interval_days

        is_active = self.is_active

        entity_count = self.entity_count

        rule_count = self.rule_count

        next_refresh_at: None | str
        if isinstance(self.next_refresh_at, datetime.datetime):
            next_refresh_at = self.next_refresh_at.isoformat()
        else:
            next_refresh_at = self.next_refresh_at

        estimated_credits_per_refresh = self.estimated_credits_per_refresh

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "entityType": entity_type,
                "refreshIntervalDays": refresh_interval_days,
                "isActive": is_active,
                "entityCount": entity_count,
                "ruleCount": rule_count,
                "nextRefreshAt": next_refresh_at,
                "estimatedCreditsPerRefresh": estimated_credits_per_refresh,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        entity_type = GetTrackerOverviewResponse200OutputPersonListsItemEntityType(d.pop("entityType"))

        refresh_interval_days = d.pop("refreshIntervalDays")

        is_active = d.pop("isActive")

        entity_count = d.pop("entityCount")

        rule_count = d.pop("ruleCount")

        def _parse_next_refresh_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_refresh_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_refresh_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_refresh_at = _parse_next_refresh_at(d.pop("nextRefreshAt"))

        estimated_credits_per_refresh = d.pop("estimatedCreditsPerRefresh")

        get_tracker_overview_response_200_output_person_lists_item = cls(
            id=id,
            name=name,
            entity_type=entity_type,
            refresh_interval_days=refresh_interval_days,
            is_active=is_active,
            entity_count=entity_count,
            rule_count=rule_count,
            next_refresh_at=next_refresh_at,
            estimated_credits_per_refresh=estimated_credits_per_refresh,
        )

        get_tracker_overview_response_200_output_person_lists_item.additional_properties = d
        return get_tracker_overview_response_200_output_person_lists_item

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
