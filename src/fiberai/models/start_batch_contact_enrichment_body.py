from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_batch_contact_enrichment_body_enrichment_types import (
        StartBatchContactEnrichmentBodyEnrichmentTypes,
    )
    from ..models.start_batch_contact_enrichment_body_person_details_item import (
        StartBatchContactEnrichmentBodyPersonDetailsItem,
    )


T = TypeVar("T", bound="StartBatchContactEnrichmentBody")


@_attrs_define
class StartBatchContactEnrichmentBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        person_details (list[StartBatchContactEnrichmentBodyPersonDetailsItem]):
        enrichment_types (StartBatchContactEnrichmentBodyEnrichmentTypes | Unset): Types of contact info to be requested
            for each person. Include the ones you want to look for. For example, { getWorkEmails: true, getPersonalEmails:
            true, getPhoneNumbers: true }
    """

    api_key: str
    person_details: list[StartBatchContactEnrichmentBodyPersonDetailsItem]
    enrichment_types: StartBatchContactEnrichmentBodyEnrichmentTypes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        person_details = []
        for person_details_item_data in self.person_details:
            person_details_item = person_details_item_data.to_dict()
            person_details.append(person_details_item)

        enrichment_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_types, Unset):
            enrichment_types = self.enrichment_types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "personDetails": person_details,
            }
        )
        if enrichment_types is not UNSET:
            field_dict["enrichmentTypes"] = enrichment_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_batch_contact_enrichment_body_enrichment_types import (
            StartBatchContactEnrichmentBodyEnrichmentTypes,
        )
        from ..models.start_batch_contact_enrichment_body_person_details_item import (
            StartBatchContactEnrichmentBodyPersonDetailsItem,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        person_details = []
        _person_details = d.pop("personDetails")
        for person_details_item_data in _person_details:
            person_details_item = StartBatchContactEnrichmentBodyPersonDetailsItem.from_dict(person_details_item_data)

            person_details.append(person_details_item)

        _enrichment_types = d.pop("enrichmentTypes", UNSET)
        enrichment_types: StartBatchContactEnrichmentBodyEnrichmentTypes | Unset
        if isinstance(_enrichment_types, Unset):
            enrichment_types = UNSET
        else:
            enrichment_types = StartBatchContactEnrichmentBodyEnrichmentTypes.from_dict(_enrichment_types)

        start_batch_contact_enrichment_body = cls(
            api_key=api_key,
            person_details=person_details,
            enrichment_types=enrichment_types,
        )

        start_batch_contact_enrichment_body.additional_properties = d
        return start_batch_contact_enrichment_body

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
