from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_live_company import (
        EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany,
    )
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_live_prospect import (
        EstimateEnrichmentCostResponse200OutputBreakdownLiveProspect,
    )
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_sales_nav import (
        EstimateEnrichmentCostResponse200OutputBreakdownSalesNav,
    )
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_validation import (
        EstimateEnrichmentCostResponse200OutputBreakdownValidation,
    )
    from ..models.estimate_enrichment_cost_response_200_output_breakdown_waterfall import (
        EstimateEnrichmentCostResponse200OutputBreakdownWaterfall,
    )


T = TypeVar("T", bound="EstimateEnrichmentCostResponse200OutputBreakdown")


@_attrs_define
class EstimateEnrichmentCostResponse200OutputBreakdown:
    """Detailed cost breakdown by operation type

    Attributes:
        sales_nav (EstimateEnrichmentCostResponse200OutputBreakdownSalesNav): Sales Navigator enrichment cost
        live_company (EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany): Company live enrichment cost
        live_prospect (EstimateEnrichmentCostResponse200OutputBreakdownLiveProspect): Prospect live enrichment cost
        waterfall (EstimateEnrichmentCostResponse200OutputBreakdownWaterfall): Waterfall pricing for contact enrichment
        validation (EstimateEnrichmentCostResponse200OutputBreakdownValidation): Email validation cost
    """

    sales_nav: EstimateEnrichmentCostResponse200OutputBreakdownSalesNav
    live_company: EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany
    live_prospect: EstimateEnrichmentCostResponse200OutputBreakdownLiveProspect
    waterfall: EstimateEnrichmentCostResponse200OutputBreakdownWaterfall
    validation: EstimateEnrichmentCostResponse200OutputBreakdownValidation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sales_nav = self.sales_nav.to_dict()

        live_company = self.live_company.to_dict()

        live_prospect = self.live_prospect.to_dict()

        waterfall = self.waterfall.to_dict()

        validation = self.validation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "salesNav": sales_nav,
                "liveCompany": live_company,
                "liveProspect": live_prospect,
                "waterfall": waterfall,
                "validation": validation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_live_company import (
            EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany,
        )
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_live_prospect import (
            EstimateEnrichmentCostResponse200OutputBreakdownLiveProspect,
        )
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_sales_nav import (
            EstimateEnrichmentCostResponse200OutputBreakdownSalesNav,
        )
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_validation import (
            EstimateEnrichmentCostResponse200OutputBreakdownValidation,
        )
        from ..models.estimate_enrichment_cost_response_200_output_breakdown_waterfall import (
            EstimateEnrichmentCostResponse200OutputBreakdownWaterfall,
        )

        d = dict(src_dict)
        sales_nav = EstimateEnrichmentCostResponse200OutputBreakdownSalesNav.from_dict(d.pop("salesNav"))

        live_company = EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany.from_dict(d.pop("liveCompany"))

        live_prospect = EstimateEnrichmentCostResponse200OutputBreakdownLiveProspect.from_dict(d.pop("liveProspect"))

        waterfall = EstimateEnrichmentCostResponse200OutputBreakdownWaterfall.from_dict(d.pop("waterfall"))

        validation = EstimateEnrichmentCostResponse200OutputBreakdownValidation.from_dict(d.pop("validation"))

        estimate_enrichment_cost_response_200_output_breakdown = cls(
            sales_nav=sales_nav,
            live_company=live_company,
            live_prospect=live_prospect,
            waterfall=waterfall,
            validation=validation,
        )

        estimate_enrichment_cost_response_200_output_breakdown.additional_properties = d
        return estimate_enrichment_cost_response_200_output_breakdown

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
