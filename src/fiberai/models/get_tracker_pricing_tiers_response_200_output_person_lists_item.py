from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_entity_type import (
    GetTrackerPricingTiersResponse200OutputPersonListsItemEntityType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_criteria import (
        GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria,
    )
    from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_tier_type_0 import (
        GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0,
    )
    from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0 import (
        GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0,
    )
    from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_1 import (
        GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1,
    )


T = TypeVar("T", bound="GetTrackerPricingTiersResponse200OutputPersonListsItem")


@_attrs_define
class GetTrackerPricingTiersResponse200OutputPersonListsItem:
    """
    Attributes:
        id (str): Tracker list ID.
        name (str): List name.
        entity_type (GetTrackerPricingTiersResponse200OutputPersonListsItemEntityType): Entity type tracked by this
            list.
        refresh_interval_days (int): How often the list is checked, in days.
        criteria (GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria): The two criteria that decide the
            tier. The entity-count criterion is judged across ALL of your lists; the refresh-interval criterion is judged on
            this list alone.
        has_premium_rules (bool): True when the list has at least one active premium rule. A list with one or more
            premium rules can never be billed higher than Silver — it cannot be on Gold, even when both criteria are met.
        tier (GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0 | None | Unset): The tier the list's next
            scheduled refresh will be billed at, with its per-entity cost and when the tier applies. Null when your
            organization has a negotiated rate instead of the standard tiers.
        to_reach_next_tier (GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0 |
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1 | None | Unset): The one change that
            would move this list to the next cheaper tier, and that tier's per-entity cost. Null when the list is already on
            Gold, when premium rules block the next tier, or when your organization has a negotiated rate.
    """

    id: str
    name: str
    entity_type: GetTrackerPricingTiersResponse200OutputPersonListsItemEntityType
    refresh_interval_days: int
    criteria: GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria
    has_premium_rules: bool
    tier: GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0 | None | Unset = UNSET
    to_reach_next_tier: (
        GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0
        | GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_tier_type_0 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_1 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1,  # noqa: PLC0415
        )

        id = self.id

        name = self.name

        entity_type = self.entity_type.value

        refresh_interval_days = self.refresh_interval_days

        criteria = self.criteria.to_dict()

        has_premium_rules = self.has_premium_rules

        tier: dict[str, Any] | None | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0):
            tier = self.tier.to_dict()
        else:
            tier = self.tier

        to_reach_next_tier: dict[str, Any] | None | Unset
        if isinstance(self.to_reach_next_tier, Unset):
            to_reach_next_tier = UNSET
        elif isinstance(
            self.to_reach_next_tier, GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0
        ):
            to_reach_next_tier = self.to_reach_next_tier.to_dict()
        elif isinstance(
            self.to_reach_next_tier, GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1
        ):
            to_reach_next_tier = self.to_reach_next_tier.to_dict()
        else:
            to_reach_next_tier = self.to_reach_next_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "entityType": entity_type,
                "refreshIntervalDays": refresh_interval_days,
                "criteria": criteria,
                "hasPremiumRules": has_premium_rules,
            }
        )
        if tier is not UNSET:
            field_dict["tier"] = tier
        if to_reach_next_tier is not UNSET:
            field_dict["toReachNextTier"] = to_reach_next_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_criteria import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_tier_type_0 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_0 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item_to_reach_next_tier_type_1 import (
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        entity_type = GetTrackerPricingTiersResponse200OutputPersonListsItemEntityType(d.pop("entityType"))

        refresh_interval_days = d.pop("refreshIntervalDays")

        criteria = GetTrackerPricingTiersResponse200OutputPersonListsItemCriteria.from_dict(d.pop("criteria"))

        has_premium_rules = d.pop("hasPremiumRules")

        def _parse_tier(data: object) -> GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tier_type_0 = GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0.from_dict(data)

                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTrackerPricingTiersResponse200OutputPersonListsItemTierType0 | None | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_to_reach_next_tier(
            data: object,
        ) -> (
            GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0
            | GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_reach_next_tier_type_0 = (
                    GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0.from_dict(data)
                )

                return to_reach_next_tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_reach_next_tier_type_1 = (
                    GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1.from_dict(data)
                )

                return to_reach_next_tier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0
                | GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1
                | None
                | Unset,
                data,
            )

        to_reach_next_tier = _parse_to_reach_next_tier(d.pop("toReachNextTier", UNSET))

        get_tracker_pricing_tiers_response_200_output_person_lists_item = cls(
            id=id,
            name=name,
            entity_type=entity_type,
            refresh_interval_days=refresh_interval_days,
            criteria=criteria,
            has_premium_rules=has_premium_rules,
            tier=tier,
            to_reach_next_tier=to_reach_next_tier,
        )

        get_tracker_pricing_tiers_response_200_output_person_lists_item.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output_person_lists_item

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
