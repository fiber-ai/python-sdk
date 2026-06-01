from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tracker_company_list_response_200_output_tracking_rules_type_0_item import (
        GetTrackerCompanyListResponse200OutputTrackingRulesType0Item,
    )


T = TypeVar("T", bound="GetTrackerCompanyListResponse200Output")


@_attrs_define
class GetTrackerCompanyListResponse200Output:
    """
    Attributes:
        id (str): Tracker list ID
        name (str): Name of the list
        refresh_interval_days (int): Check interval in days
        is_active (bool): Whether the list is actively being checked
        is_archived (bool): Whether the list is archived
        company_count (int): Number of companies in this list
        created_at (datetime.datetime): When the list was created
        tracking_rules (list[GetTrackerCompanyListResponse200OutputTrackingRulesType0Item] | None | Unset): Active
            tracking rules on this list, with IDs for granular management
    """

    id: str
    name: str
    refresh_interval_days: int
    is_active: bool
    is_archived: bool
    company_count: int
    created_at: datetime.datetime
    tracking_rules: list[GetTrackerCompanyListResponse200OutputTrackingRulesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        refresh_interval_days = self.refresh_interval_days

        is_active = self.is_active

        is_archived = self.is_archived

        company_count = self.company_count

        created_at = self.created_at.isoformat()

        tracking_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.tracking_rules, Unset):
            tracking_rules = UNSET
        elif isinstance(self.tracking_rules, list):
            tracking_rules = []
            for tracking_rules_type_0_item_data in self.tracking_rules:
                tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                tracking_rules.append(tracking_rules_type_0_item)

        else:
            tracking_rules = self.tracking_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "refreshIntervalDays": refresh_interval_days,
                "isActive": is_active,
                "isArchived": is_archived,
                "companyCount": company_count,
                "createdAt": created_at,
            }
        )
        if tracking_rules is not UNSET:
            field_dict["trackingRules"] = tracking_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tracker_company_list_response_200_output_tracking_rules_type_0_item import (
            GetTrackerCompanyListResponse200OutputTrackingRulesType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        refresh_interval_days = d.pop("refreshIntervalDays")

        is_active = d.pop("isActive")

        is_archived = d.pop("isArchived")

        company_count = d.pop("companyCount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_tracking_rules(
            data: object,
        ) -> list[GetTrackerCompanyListResponse200OutputTrackingRulesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tracking_rules_type_0 = []
                _tracking_rules_type_0 = data
                for tracking_rules_type_0_item_data in _tracking_rules_type_0:
                    tracking_rules_type_0_item = GetTrackerCompanyListResponse200OutputTrackingRulesType0Item.from_dict(
                        tracking_rules_type_0_item_data
                    )

                    tracking_rules_type_0.append(tracking_rules_type_0_item)

                return tracking_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetTrackerCompanyListResponse200OutputTrackingRulesType0Item] | None | Unset, data)

        tracking_rules = _parse_tracking_rules(d.pop("trackingRules", UNSET))

        get_tracker_company_list_response_200_output = cls(
            id=id,
            name=name,
            refresh_interval_days=refresh_interval_days,
            is_active=is_active,
            is_archived=is_archived,
            company_count=company_count,
            created_at=created_at,
            tracking_rules=tracking_rules,
        )

        get_tracker_company_list_response_200_output.additional_properties = d
        return get_tracker_company_list_response_200_output

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
