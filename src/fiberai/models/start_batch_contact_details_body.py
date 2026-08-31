from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_batch_contact_details_body_enrichment_types import StartBatchContactDetailsBodyEnrichmentTypes
    from ..models.start_batch_contact_details_body_person_details_item import (
        StartBatchContactDetailsBodyPersonDetailsItem,
    )


T = TypeVar("T", bound="StartBatchContactDetailsBody")


@_attrs_define
class StartBatchContactDetailsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        person_details (list[StartBatchContactDetailsBodyPersonDetailsItem]):
        enrichment_types (StartBatchContactDetailsBodyEnrichmentTypes | Unset): The types of contact information to
            request for each person. Credits are charged per selected type.
    """

    api_key: str
    person_details: list[StartBatchContactDetailsBodyPersonDetailsItem]
    enrichment_types: StartBatchContactDetailsBodyEnrichmentTypes | Unset = UNSET
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
        from ..models.start_batch_contact_details_body_enrichment_types import (
            StartBatchContactDetailsBodyEnrichmentTypes,  # noqa: PLC0415
        )
        from ..models.start_batch_contact_details_body_person_details_item import (
            StartBatchContactDetailsBodyPersonDetailsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        person_details = []
        _person_details = d.pop("personDetails")
        for person_details_item_data in _person_details:
            person_details_item = StartBatchContactDetailsBodyPersonDetailsItem.from_dict(person_details_item_data)

            person_details.append(person_details_item)

        _enrichment_types = d.pop("enrichmentTypes", UNSET)
        enrichment_types: StartBatchContactDetailsBodyEnrichmentTypes | Unset
        if isinstance(_enrichment_types, Unset):
            enrichment_types = UNSET
        else:
            enrichment_types = StartBatchContactDetailsBodyEnrichmentTypes.from_dict(_enrichment_types)

        start_batch_contact_details_body = cls(
            api_key=api_key,
            person_details=person_details,
            enrichment_types=enrichment_types,
        )

        start_batch_contact_details_body.additional_properties = d
        return start_batch_contact_details_body

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
