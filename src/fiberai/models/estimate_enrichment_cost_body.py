from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimate_enrichment_cost_body_enrichment_type import EstimateEnrichmentCostBodyEnrichmentType


T = TypeVar("T", bound="EstimateEnrichmentCostBody")


@_attrs_define
class EstimateEnrichmentCostBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        max_prospects_to_enrich (int): Maximum number of prospects to include when estimating enrichment cost (must be a
            positive integer; very large values may be rejected by internal safety limits).
        enrichment_type (EstimateEnrichmentCostBodyEnrichmentType): Enrichment types to estimate costs for
        run_company_live_enrichment (bool | Unset): Whether to include company live enrichment in estimate Default:
            True.
        run_profile_live_enrichment (bool | Unset): Whether to include profile live enrichment in estimate Default:
            True.
        run_profile_sales_nav (bool | Unset): Whether to include Sales Navigator enrichment in estimate Default: True.
        run_contact_enrichment (bool | Unset): Whether to include contact enrichment in estimate Default: True.
    """

    api_key: str
    max_prospects_to_enrich: int
    enrichment_type: EstimateEnrichmentCostBodyEnrichmentType
    run_company_live_enrichment: bool | Unset = True
    run_profile_live_enrichment: bool | Unset = True
    run_profile_sales_nav: bool | Unset = True
    run_contact_enrichment: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        max_prospects_to_enrich = self.max_prospects_to_enrich

        enrichment_type = self.enrichment_type.to_dict()

        run_company_live_enrichment = self.run_company_live_enrichment

        run_profile_live_enrichment = self.run_profile_live_enrichment

        run_profile_sales_nav = self.run_profile_sales_nav

        run_contact_enrichment = self.run_contact_enrichment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "maxProspectsToEnrich": max_prospects_to_enrich,
                "enrichmentType": enrichment_type,
            }
        )
        if run_company_live_enrichment is not UNSET:
            field_dict["runCompanyLiveEnrichment"] = run_company_live_enrichment
        if run_profile_live_enrichment is not UNSET:
            field_dict["runProfileLiveEnrichment"] = run_profile_live_enrichment
        if run_profile_sales_nav is not UNSET:
            field_dict["runProfileSalesNav"] = run_profile_sales_nav
        if run_contact_enrichment is not UNSET:
            field_dict["runContactEnrichment"] = run_contact_enrichment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimate_enrichment_cost_body_enrichment_type import EstimateEnrichmentCostBodyEnrichmentType

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        max_prospects_to_enrich = d.pop("maxProspectsToEnrich")

        enrichment_type = EstimateEnrichmentCostBodyEnrichmentType.from_dict(d.pop("enrichmentType"))

        run_company_live_enrichment = d.pop("runCompanyLiveEnrichment", UNSET)

        run_profile_live_enrichment = d.pop("runProfileLiveEnrichment", UNSET)

        run_profile_sales_nav = d.pop("runProfileSalesNav", UNSET)

        run_contact_enrichment = d.pop("runContactEnrichment", UNSET)

        estimate_enrichment_cost_body = cls(
            api_key=api_key,
            max_prospects_to_enrich=max_prospects_to_enrich,
            enrichment_type=enrichment_type,
            run_company_live_enrichment=run_company_live_enrichment,
            run_profile_live_enrichment=run_profile_live_enrichment,
            run_profile_sales_nav=run_profile_sales_nav,
            run_contact_enrichment=run_contact_enrichment,
        )

        estimate_enrichment_cost_body.additional_properties = d
        return estimate_enrichment_cost_body

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
