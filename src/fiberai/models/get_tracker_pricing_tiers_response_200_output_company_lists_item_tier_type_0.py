from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_pricing_tiers_response_200_output_company_lists_item_tier_type_0_tier import (
    GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0Tier,
)

T = TypeVar("T", bound="GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0")


@_attrs_define
class GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0:
    """The tier the list's next scheduled refresh will be billed at, with its per-entity cost and when the tier applies.
    Null when your organization has a negotiated rate instead of the standard tiers.

        Attributes:
            tier (GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0Tier):
            credits_per_entity_per_refresh (float): Credits charged per tracked company or person each time the list
                refreshes.
            description (str): When this tier applies.
    """

    tier: GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0Tier
    credits_per_entity_per_refresh: float
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier.value

        credits_per_entity_per_refresh = self.credits_per_entity_per_refresh

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "creditsPerEntityPerRefresh": credits_per_entity_per_refresh,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0Tier(d.pop("tier"))

        credits_per_entity_per_refresh = d.pop("creditsPerEntityPerRefresh")

        description = d.pop("description")

        get_tracker_pricing_tiers_response_200_output_company_lists_item_tier_type_0 = cls(
            tier=tier,
            credits_per_entity_per_refresh=credits_per_entity_per_refresh,
            description=description,
        )

        get_tracker_pricing_tiers_response_200_output_company_lists_item_tier_type_0.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output_company_lists_item_tier_type_0

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
