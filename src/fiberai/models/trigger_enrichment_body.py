from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_enrichment_body_enrichment_type import TriggerEnrichmentBodyEnrichmentType


T = TypeVar("T", bound="TriggerEnrichmentBody")


@_attrs_define
class TriggerEnrichmentBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        max_prospects_to_enrich (int): Maximum number of prospects to enrich for this run (must be a positive integer;
            very large values may be rejected by internal safety limits).
        enrichment_type (TriggerEnrichmentBodyEnrichmentType): Enrichment types to request. Credits are charged only for
            selected types.
        run_company_live_enrichment (bool | Unset): Whether to run live enrichment for companies Default: True.
        run_profile_live_enrichment (bool | Unset): Whether to run live enrichment for profiles Default: True.
        run_profile_sales_nav (bool | Unset): Whether to run Sales Navigator profile enrichment Default: True.
        run_contact_enrichment (bool | Unset): Whether to run contact enrichment (emails/phones) Default: True.
        user_email (None | str | Unset): Optional email address to receive completion notifications. If not provided, no
            email will be sent.
    """

    api_key: str
    max_prospects_to_enrich: int
    enrichment_type: TriggerEnrichmentBodyEnrichmentType
    run_company_live_enrichment: bool | Unset = True
    run_profile_live_enrichment: bool | Unset = True
    run_profile_sales_nav: bool | Unset = True
    run_contact_enrichment: bool | Unset = True
    user_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        max_prospects_to_enrich = self.max_prospects_to_enrich

        enrichment_type = self.enrichment_type.to_dict()

        run_company_live_enrichment = self.run_company_live_enrichment

        run_profile_live_enrichment = self.run_profile_live_enrichment

        run_profile_sales_nav = self.run_profile_sales_nav

        run_contact_enrichment = self.run_contact_enrichment

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

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
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_enrichment_body_enrichment_type import TriggerEnrichmentBodyEnrichmentType

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        max_prospects_to_enrich = d.pop("maxProspectsToEnrich")

        enrichment_type = TriggerEnrichmentBodyEnrichmentType.from_dict(d.pop("enrichmentType"))

        run_company_live_enrichment = d.pop("runCompanyLiveEnrichment", UNSET)

        run_profile_live_enrichment = d.pop("runProfileLiveEnrichment", UNSET)

        run_profile_sales_nav = d.pop("runProfileSalesNav", UNSET)

        run_contact_enrichment = d.pop("runContactEnrichment", UNSET)

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("userEmail", UNSET))

        trigger_enrichment_body = cls(
            api_key=api_key,
            max_prospects_to_enrich=max_prospects_to_enrich,
            enrichment_type=enrichment_type,
            run_company_live_enrichment=run_company_live_enrichment,
            run_profile_live_enrichment=run_profile_live_enrichment,
            run_profile_sales_nav=run_profile_sales_nav,
            run_contact_enrichment=run_contact_enrichment,
            user_email=user_email,
        )

        trigger_enrichment_body.additional_properties = d
        return trigger_enrichment_body

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
