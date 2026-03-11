from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_contact_enrichment_body_enrichment_type import TriggerContactEnrichmentBodyEnrichmentType
    from ..models.trigger_contact_enrichment_body_linkedin_url import TriggerContactEnrichmentBodyLinkedinUrl


T = TypeVar("T", bound="TriggerContactEnrichmentBody")


@_attrs_define
class TriggerContactEnrichmentBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        linkedin_url (TriggerContactEnrichmentBodyLinkedinUrl):
        enrichment_type (TriggerContactEnrichmentBodyEnrichmentType | Unset): Enrichment types to be requested. Include
            the ones you want to look for, we will charge credits for the ones you request. For example, { getWorkEmails:
            true, getPersonalEmails: true, getPhoneNumbers: true }
        exhaustive (bool | Unset): If true, we exhaustively fetch all emails and phones for the person. This can be
            slower and charge more credits. Default: False.
    """

    api_key: str
    linkedin_url: TriggerContactEnrichmentBodyLinkedinUrl
    enrichment_type: TriggerContactEnrichmentBodyEnrichmentType | Unset = UNSET
    exhaustive: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        linkedin_url = self.linkedin_url.to_dict()

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        exhaustive = self.exhaustive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "linkedinUrl": linkedin_url,
            }
        )
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type
        if exhaustive is not UNSET:
            field_dict["exhaustive"] = exhaustive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_contact_enrichment_body_enrichment_type import TriggerContactEnrichmentBodyEnrichmentType
        from ..models.trigger_contact_enrichment_body_linkedin_url import TriggerContactEnrichmentBodyLinkedinUrl

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = TriggerContactEnrichmentBodyLinkedinUrl.from_dict(d.pop("linkedinUrl"))

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: TriggerContactEnrichmentBodyEnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = TriggerContactEnrichmentBodyEnrichmentType.from_dict(_enrichment_type)

        exhaustive = d.pop("exhaustive", UNSET)

        trigger_contact_enrichment_body = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            enrichment_type=enrichment_type,
            exhaustive=exhaustive,
        )

        trigger_contact_enrichment_body.additional_properties = d
        return trigger_contact_enrichment_body

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
