from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tracker_overview_response_200_output_entity_limits_type_0_companies import (
        GetTrackerOverviewResponse200OutputEntityLimitsType0Companies,
    )
    from ..models.get_tracker_overview_response_200_output_entity_limits_type_0_people import (
        GetTrackerOverviewResponse200OutputEntityLimitsType0People,
    )


T = TypeVar("T", bound="GetTrackerOverviewResponse200OutputEntityLimitsType0")


@_attrs_define
class GetTrackerOverviewResponse200OutputEntityLimitsType0:
    """Your organization's limits on tracked companies and people, with current usage. Change them with POST
    /v1/tracker/entity-limit.

        Attributes:
            companies (GetTrackerOverviewResponse200OutputEntityLimitsType0Companies): Limit and usage for tracked
                companies.
            people (GetTrackerOverviewResponse200OutputEntityLimitsType0People): Limit and usage for tracked people.
            estimated_credits_per_refresh_at_limits (float | None | Unset): Credits it would cost to refresh every list once
                if both limits were full, at the highest per-entity rate your lists can be billed at for that volume. Null
                unless both limits are set.
    """

    companies: GetTrackerOverviewResponse200OutputEntityLimitsType0Companies
    people: GetTrackerOverviewResponse200OutputEntityLimitsType0People
    estimated_credits_per_refresh_at_limits: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = self.companies.to_dict()

        people = self.people.to_dict()

        estimated_credits_per_refresh_at_limits: float | None | Unset
        if isinstance(self.estimated_credits_per_refresh_at_limits, Unset):
            estimated_credits_per_refresh_at_limits = UNSET
        else:
            estimated_credits_per_refresh_at_limits = self.estimated_credits_per_refresh_at_limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
                "people": people,
            }
        )
        if estimated_credits_per_refresh_at_limits is not UNSET:
            field_dict["estimatedCreditsPerRefreshAtLimits"] = estimated_credits_per_refresh_at_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tracker_overview_response_200_output_entity_limits_type_0_companies import (
            GetTrackerOverviewResponse200OutputEntityLimitsType0Companies,  # noqa: PLC0415
        )
        from ..models.get_tracker_overview_response_200_output_entity_limits_type_0_people import (
            GetTrackerOverviewResponse200OutputEntityLimitsType0People,  # noqa: PLC0415
        )

        d = dict(src_dict)
        companies = GetTrackerOverviewResponse200OutputEntityLimitsType0Companies.from_dict(d.pop("companies"))

        people = GetTrackerOverviewResponse200OutputEntityLimitsType0People.from_dict(d.pop("people"))

        def _parse_estimated_credits_per_refresh_at_limits(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_credits_per_refresh_at_limits = _parse_estimated_credits_per_refresh_at_limits(
            d.pop("estimatedCreditsPerRefreshAtLimits", UNSET)
        )

        get_tracker_overview_response_200_output_entity_limits_type_0 = cls(
            companies=companies,
            people=people,
            estimated_credits_per_refresh_at_limits=estimated_credits_per_refresh_at_limits,
        )

        get_tracker_overview_response_200_output_entity_limits_type_0.additional_properties = d
        return get_tracker_overview_response_200_output_entity_limits_type_0

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
