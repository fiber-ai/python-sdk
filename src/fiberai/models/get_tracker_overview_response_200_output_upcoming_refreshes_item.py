from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_overview_response_200_output_upcoming_refreshes_item_entity_type import (
    GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType,
)

T = TypeVar("T", bound="GetTrackerOverviewResponse200OutputUpcomingRefreshesItem")


@_attrs_define
class GetTrackerOverviewResponse200OutputUpcomingRefreshesItem:
    """
    Attributes:
        list_id (str): Tracker list ID.
        list_name (str): List name.
        entity_type (GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType): Entity type tracked by this
            list.
        refresh_at (datetime.datetime): ISO timestamp when the next refresh of this list will run.
        entity_count (int): Number of entities in the list that will be refreshed.
        estimated_credits (float): Credits that will be charged for this refresh.
    """

    list_id: str
    list_name: str
    entity_type: GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType
    refresh_at: datetime.datetime
    entity_count: int
    estimated_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        list_name = self.list_name

        entity_type = self.entity_type.value

        refresh_at = self.refresh_at.isoformat()

        entity_count = self.entity_count

        estimated_credits = self.estimated_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "listName": list_name,
                "entityType": entity_type,
                "refreshAt": refresh_at,
                "entityCount": entity_count,
                "estimatedCredits": estimated_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("listId")

        list_name = d.pop("listName")

        entity_type = GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType(d.pop("entityType"))

        refresh_at = datetime.datetime.fromisoformat(d.pop("refreshAt"))

        entity_count = d.pop("entityCount")

        estimated_credits = d.pop("estimatedCredits")

        get_tracker_overview_response_200_output_upcoming_refreshes_item = cls(
            list_id=list_id,
            list_name=list_name,
            entity_type=entity_type,
            refresh_at=refresh_at,
            entity_count=entity_count,
            estimated_credits=estimated_credits,
        )

        get_tracker_overview_response_200_output_upcoming_refreshes_item.additional_properties = d
        return get_tracker_overview_response_200_output_upcoming_refreshes_item

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
