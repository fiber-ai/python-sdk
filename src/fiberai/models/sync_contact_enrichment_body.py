from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_contact_enrichment_body_enrichment_type import SyncContactEnrichmentBodyEnrichmentType





T = TypeVar("T", bound="SyncContactEnrichmentBody")



@_attrs_define
class SyncContactEnrichmentBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            linkedin_url (str): Person's LinkedIn URL, like 'https://www.linkedin.com/in/william-h-gates'
            enrichment_type (Union[Unset, SyncContactEnrichmentBodyEnrichmentType]): Enrichment types to be requested.
                Include the ones you want to look for, we will charge credits for the ones you request. For example, {
                getWorkEmails: true, getPersonalEmails: true, getPhoneNumbers: true }
     """

    api_key: str
    linkedin_url: str
    enrichment_type: Union[Unset, 'SyncContactEnrichmentBodyEnrichmentType'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_contact_enrichment_body_enrichment_type import SyncContactEnrichmentBodyEnrichmentType
        api_key = self.api_key

        linkedin_url = self.linkedin_url

        enrichment_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "linkedinUrl": linkedin_url,
        })
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_contact_enrichment_body_enrichment_type import SyncContactEnrichmentBodyEnrichmentType
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = d.pop("linkedinUrl")

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: Union[Unset, SyncContactEnrichmentBodyEnrichmentType]
        if isinstance(_enrichment_type,  Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = SyncContactEnrichmentBodyEnrichmentType.from_dict(_enrichment_type)




        sync_contact_enrichment_body = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            enrichment_type=enrichment_type,
        )


        sync_contact_enrichment_body.additional_properties = d
        return sync_contact_enrichment_body

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
