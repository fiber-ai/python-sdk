from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_waterfall_operations import (
        EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations,
    )


T = TypeVar("T", bound="EstimateEnrichmentCostResponse200OutputBreakdownWaterfall")


@_attrs_define
class EstimateEnrichmentCostResponse200OutputBreakdownWaterfall:
    """Waterfall pricing for contact enrichment

    Attributes:
        credits_ (float):
        original_credits (float):
        discount (float):
        operations (EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations):
    """

    credits_: float
    original_credits: float
    discount: float
    operations: EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        original_credits = self.original_credits

        discount = self.discount

        operations = self.operations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "originalCredits": original_credits,
                "discount": discount,
                "operations": operations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_waterfall_operations import (
            EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations,
        )

        d = dict(src_dict)
        credits_ = d.pop("credits")

        original_credits = d.pop("originalCredits")

        discount = d.pop("discount")

        operations = EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations.from_dict(d.pop("operations"))

        estimate_enrichment_cost_response_200_output_breakdown_waterfall = cls(
            credits_=credits_,
            original_credits=original_credits,
            discount=discount,
            operations=operations,
        )

        estimate_enrichment_cost_response_200_output_breakdown_waterfall.additional_properties = d
        return estimate_enrichment_cost_response_200_output_breakdown_waterfall

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
