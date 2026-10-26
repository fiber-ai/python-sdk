from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_pricing_tiers_response_200_output_company_lists_item_to_reach_next_tier_type_1_advice import (
    GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1Advice,
)
from ..models.get_tracker_pricing_tiers_response_200_output_company_lists_item_to_reach_next_tier_type_1_next_tier import (
    GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1NextTier,
)

T = TypeVar("T", bound="GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1")


@_attrs_define
class GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1:
    """
    Attributes:
        next_tier (GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1NextTier): The tier this
            change moves the list to.
        next_tier_credits_per_entity (float): Credits charged per tracked company or person each time the list
            refreshes.
        advice (GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1Advice):
        need_to_add (int): How many more companies and people your organization would need to track, across all lists,
            to meet the volume criterion. Always at least 1.
    """

    next_tier: GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1NextTier
    next_tier_credits_per_entity: float
    advice: GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1Advice
    need_to_add: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_tier = self.next_tier.value

        next_tier_credits_per_entity = self.next_tier_credits_per_entity

        advice = self.advice.value

        need_to_add = self.need_to_add

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextTier": next_tier,
                "nextTierCreditsPerEntity": next_tier_credits_per_entity,
                "advice": advice,
                "needToAdd": need_to_add,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_tier = GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1NextTier(
            d.pop("nextTier")
        )

        next_tier_credits_per_entity = d.pop("nextTierCreditsPerEntity")

        advice = GetTrackerPricingTiersResponse200OutputCompanyListsItemToReachNextTierType1Advice(d.pop("advice"))

        need_to_add = d.pop("needToAdd")

        get_tracker_pricing_tiers_response_200_output_company_lists_item_to_reach_next_tier_type_1 = cls(
            next_tier=next_tier,
            next_tier_credits_per_entity=next_tier_credits_per_entity,
            advice=advice,
            need_to_add=need_to_add,
        )

        get_tracker_pricing_tiers_response_200_output_company_lists_item_to_reach_next_tier_type_1.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output_company_lists_item_to_reach_next_tier_type_1

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
