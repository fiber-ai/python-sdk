from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0_advice import (
    GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0Advice,
)
from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0_increase_to import (
    GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0IncreaseTo,
)
from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0_next_tier import (
    GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0NextTier,
)

T = TypeVar("T", bound="GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0")


@_attrs_define
class GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0:
    """
    Attributes:
        next_tier (GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0NextTier): The tier this
            change moves the list to.
        next_tier_credits_per_entity (float): Credits charged per tracked company or person each time the list
            refreshes.
        advice (GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0Advice):
        increase_to (GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0IncreaseTo): The refresh
            cadence to switch this list to.
    """

    next_tier: GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0NextTier
    next_tier_credits_per_entity: float
    advice: GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0Advice
    increase_to: GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0IncreaseTo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_tier = self.next_tier.value

        next_tier_credits_per_entity = self.next_tier_credits_per_entity

        advice = self.advice.value

        increase_to = self.increase_to.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextTier": next_tier,
                "nextTierCreditsPerEntity": next_tier_credits_per_entity,
                "advice": advice,
                "increaseTo": increase_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_tier = GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0NextTier(
            d.pop("nextTier")
        )

        next_tier_credits_per_entity = d.pop("nextTierCreditsPerEntity")

        advice = GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0Advice(d.pop("advice"))

        increase_to = GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0IncreaseTo(
            d.pop("increaseTo")
        )

        get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0 = cls(
            next_tier=next_tier,
            next_tier_credits_per_entity=next_tier_credits_per_entity,
            advice=advice,
            increase_to=increase_to,
        )

        get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0

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
