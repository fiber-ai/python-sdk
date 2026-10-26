from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria")


@_attrs_define
class GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria:
    """The two criteria that decide the tier. The entity-count criterion is judged across ALL of your lists; the refresh-
    interval criterion is judged on this list alone.

        Attributes:
            meets_entity_count_criteria (bool): True when your organization's tracked entity total meets the volume
                threshold described in the tiers table.
            meets_refresh_interval_criteria (bool): True when this list refreshes at least once a day (refreshIntervalDays
                of 1 or less).
    """

    meets_entity_count_criteria: bool
    meets_refresh_interval_criteria: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meets_entity_count_criteria = self.meets_entity_count_criteria

        meets_refresh_interval_criteria = self.meets_refresh_interval_criteria

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meetsEntityCountCriteria": meets_entity_count_criteria,
                "meetsRefreshIntervalCriteria": meets_refresh_interval_criteria,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        meets_entity_count_criteria = d.pop("meetsEntityCountCriteria")

        meets_refresh_interval_criteria = d.pop("meetsRefreshIntervalCriteria")

        get_tracker_pricing_tiers_response_200_output_person_lists_item_criteria = cls(
            meets_entity_count_criteria=meets_entity_count_criteria,
            meets_refresh_interval_criteria=meets_refresh_interval_criteria,
        )

        get_tracker_pricing_tiers_response_200_output_person_lists_item_criteria.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output_person_lists_item_criteria

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
