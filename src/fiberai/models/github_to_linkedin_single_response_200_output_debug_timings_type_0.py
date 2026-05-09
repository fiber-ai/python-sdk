from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item import (
        GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem,
    )


T = TypeVar("T", bound="GithubToLinkedinSingleResponse200OutputDebugTimingsType0")


@_attrs_define
class GithubToLinkedinSingleResponse200OutputDebugTimingsType0:
    """Optional resolver timing metadata. Present only when requested for diagnostics.

    Attributes:
        lookup_duration_ms (int): Lookup runtime measured inside the single-lookup worker.
        bootstrap_duration_ms (int): Duration of cache/bootstrap loading before resolver execution.
        resolver_duration_ms (int): Total resolver duration for this lookup.
        resolver_step_durations_sum_ms (int): Sum of explicitly instrumented resolver step durations.
        resolver_uninstrumented_duration_ms (int): Resolver duration not covered by step-level instrumentation.
        resolver_steps (list[GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem]): Step-level
            resolver timings for troubleshooting and profiling.
        credit_charge_duration_ms (int | None | Unset): Duration spent charging credits for this request.
        route_duration_ms (int | None | Unset): End-to-end route handler duration for this request.
    """

    lookup_duration_ms: int
    bootstrap_duration_ms: int
    resolver_duration_ms: int
    resolver_step_durations_sum_ms: int
    resolver_uninstrumented_duration_ms: int
    resolver_steps: list[GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem]
    credit_charge_duration_ms: int | None | Unset = UNSET
    route_duration_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookup_duration_ms = self.lookup_duration_ms

        bootstrap_duration_ms = self.bootstrap_duration_ms

        resolver_duration_ms = self.resolver_duration_ms

        resolver_step_durations_sum_ms = self.resolver_step_durations_sum_ms

        resolver_uninstrumented_duration_ms = self.resolver_uninstrumented_duration_ms

        resolver_steps = []
        for resolver_steps_item_data in self.resolver_steps:
            resolver_steps_item = resolver_steps_item_data.to_dict()
            resolver_steps.append(resolver_steps_item)

        credit_charge_duration_ms: int | None | Unset
        if isinstance(self.credit_charge_duration_ms, Unset):
            credit_charge_duration_ms = UNSET
        else:
            credit_charge_duration_ms = self.credit_charge_duration_ms

        route_duration_ms: int | None | Unset
        if isinstance(self.route_duration_ms, Unset):
            route_duration_ms = UNSET
        else:
            route_duration_ms = self.route_duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lookupDurationMs": lookup_duration_ms,
                "bootstrapDurationMs": bootstrap_duration_ms,
                "resolverDurationMs": resolver_duration_ms,
                "resolverStepDurationsSumMs": resolver_step_durations_sum_ms,
                "resolverUninstrumentedDurationMs": resolver_uninstrumented_duration_ms,
                "resolverSteps": resolver_steps,
            }
        )
        if credit_charge_duration_ms is not UNSET:
            field_dict["creditChargeDurationMs"] = credit_charge_duration_ms
        if route_duration_ms is not UNSET:
            field_dict["routeDurationMs"] = route_duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item import (
            GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem,
        )

        d = dict(src_dict)
        lookup_duration_ms = d.pop("lookupDurationMs")

        bootstrap_duration_ms = d.pop("bootstrapDurationMs")

        resolver_duration_ms = d.pop("resolverDurationMs")

        resolver_step_durations_sum_ms = d.pop("resolverStepDurationsSumMs")

        resolver_uninstrumented_duration_ms = d.pop("resolverUninstrumentedDurationMs")

        resolver_steps = []
        _resolver_steps = d.pop("resolverSteps")
        for resolver_steps_item_data in _resolver_steps:
            resolver_steps_item = GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem.from_dict(
                resolver_steps_item_data
            )

            resolver_steps.append(resolver_steps_item)

        def _parse_credit_charge_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credit_charge_duration_ms = _parse_credit_charge_duration_ms(d.pop("creditChargeDurationMs", UNSET))

        def _parse_route_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        route_duration_ms = _parse_route_duration_ms(d.pop("routeDurationMs", UNSET))

        github_to_linkedin_single_response_200_output_debug_timings_type_0 = cls(
            lookup_duration_ms=lookup_duration_ms,
            bootstrap_duration_ms=bootstrap_duration_ms,
            resolver_duration_ms=resolver_duration_ms,
            resolver_step_durations_sum_ms=resolver_step_durations_sum_ms,
            resolver_uninstrumented_duration_ms=resolver_uninstrumented_duration_ms,
            resolver_steps=resolver_steps,
            credit_charge_duration_ms=credit_charge_duration_ms,
            route_duration_ms=route_duration_ms,
        )

        github_to_linkedin_single_response_200_output_debug_timings_type_0.additional_properties = d
        return github_to_linkedin_single_response_200_output_debug_timings_type_0

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
