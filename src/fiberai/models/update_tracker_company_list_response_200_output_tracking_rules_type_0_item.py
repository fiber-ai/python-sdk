from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_tracker_company_list_response_200_output_tracking_rules_type_0_item_entity_type import (
    UpdateTrackerCompanyListResponse200OutputTrackingRulesType0ItemEntityType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTrackerCompanyListResponse200OutputTrackingRulesType0Item")


@_attrs_define
class UpdateTrackerCompanyListResponse200OutputTrackingRulesType0Item:
    """A tracking rule with its full configuration. Contains all input fields plus a server-generated id.

    Attributes:
        id (str): Unique rule ID. Use with removeRuleIds to delete a specific rule.
        type_ (str): Rule type slug (e.g. headcount_crossed_threshold, person_changed_company)
        entity_type (UpdateTrackerCompanyListResponse200OutputTrackingRulesType0ItemEntityType): Whether this rule
            applies to company or person entities
        lookback_days (int | None | Unset): If set, compare against a snapshot from approximately N days ago instead of
            the most recent prior snapshot.
    """

    id: str
    type_: str
    entity_type: UpdateTrackerCompanyListResponse200OutputTrackingRulesType0ItemEntityType
    lookback_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        entity_type = self.entity_type.value

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        entity_type = UpdateTrackerCompanyListResponse200OutputTrackingRulesType0ItemEntityType(d.pop("entityType"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        update_tracker_company_list_response_200_output_tracking_rules_type_0_item = cls(
            id=id,
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
        )

        update_tracker_company_list_response_200_output_tracking_rules_type_0_item.additional_properties = d
        return update_tracker_company_list_response_200_output_tracking_rules_type_0_item

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
