from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_tracker_pricing_tiers_response_200_output_company_lists_item import (
        GetTrackerPricingTiersResponse200OutputCompanyListsItem,
    )
    from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item import (
        GetTrackerPricingTiersResponse200OutputPersonListsItem,
    )
    from ..models.get_tracker_pricing_tiers_response_200_output_tiers_item import (
        GetTrackerPricingTiersResponse200OutputTiersItem,
    )


T = TypeVar("T", bound="GetTrackerPricingTiersResponse200Output")


@_attrs_define
class GetTrackerPricingTiersResponse200Output:
    """
    Attributes:
        tracked_entity_count (int): Active companies and people tracked across all of your lists, summed org-wide. This
            total decides tier eligibility for every list.
        uses_custom_pricing (bool): True when your organization has a negotiated per-entity rate that replaces the
            standard tiers. Most organizations are on the standard tiers (false).
        tiers (list[GetTrackerPricingTiersResponse200OutputTiersItem]): The standard tiers, from the standard rate to
            the cheapest.
        company_lists (list[GetTrackerPricingTiersResponse200OutputCompanyListsItem]): All non-archived company tracker
            lists with the tier their next refresh is billed at, and what would move each to a cheaper tier. May include
            paused lists.
        person_lists (list[GetTrackerPricingTiersResponse200OutputPersonListsItem]): All non-archived person tracker
            lists with the tier their next refresh is billed at, and what would move each to a cheaper tier. May include
            paused lists.
    """

    tracked_entity_count: int
    uses_custom_pricing: bool
    tiers: list[GetTrackerPricingTiersResponse200OutputTiersItem]
    company_lists: list[GetTrackerPricingTiersResponse200OutputCompanyListsItem]
    person_lists: list[GetTrackerPricingTiersResponse200OutputPersonListsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracked_entity_count = self.tracked_entity_count

        uses_custom_pricing = self.uses_custom_pricing

        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        company_lists = []
        for company_lists_item_data in self.company_lists:
            company_lists_item = company_lists_item_data.to_dict()
            company_lists.append(company_lists_item)

        person_lists = []
        for person_lists_item_data in self.person_lists:
            person_lists_item = person_lists_item_data.to_dict()
            person_lists.append(person_lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trackedEntityCount": tracked_entity_count,
                "usesCustomPricing": uses_custom_pricing,
                "tiers": tiers,
                "companyLists": company_lists,
                "personLists": person_lists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tracker_pricing_tiers_response_200_output_company_lists_item import (
            GetTrackerPricingTiersResponse200OutputCompanyListsItem,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_person_lists_item import (
            GetTrackerPricingTiersResponse200OutputPersonListsItem,  # noqa: PLC0415
        )
        from ..models.get_tracker_pricing_tiers_response_200_output_tiers_item import (
            GetTrackerPricingTiersResponse200OutputTiersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        tracked_entity_count = d.pop("trackedEntityCount")

        uses_custom_pricing = d.pop("usesCustomPricing")

        tiers = []
        _tiers = d.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = GetTrackerPricingTiersResponse200OutputTiersItem.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        company_lists = []
        _company_lists = d.pop("companyLists")
        for company_lists_item_data in _company_lists:
            company_lists_item = GetTrackerPricingTiersResponse200OutputCompanyListsItem.from_dict(
                company_lists_item_data
            )

            company_lists.append(company_lists_item)

        person_lists = []
        _person_lists = d.pop("personLists")
        for person_lists_item_data in _person_lists:
            person_lists_item = GetTrackerPricingTiersResponse200OutputPersonListsItem.from_dict(person_lists_item_data)

            person_lists.append(person_lists_item)

        get_tracker_pricing_tiers_response_200_output = cls(
            tracked_entity_count=tracked_entity_count,
            uses_custom_pricing=uses_custom_pricing,
            tiers=tiers,
            company_lists=company_lists,
            person_lists=person_lists,
        )

        get_tracker_pricing_tiers_response_200_output.additional_properties = d
        return get_tracker_pricing_tiers_response_200_output

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
