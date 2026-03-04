from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_contact_enrichment_response_200_output_profile_status import SyncContactEnrichmentResponse200OutputProfileStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_contact_enrichment_response_200_output_profile_emails_item import SyncContactEnrichmentResponse200OutputProfileEmailsItem
  from ..models.sync_contact_enrichment_response_200_output_profile_phone_numbers_item import SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem





T = TypeVar("T", bound="SyncContactEnrichmentResponse200OutputProfile")



@_attrs_define
class SyncContactEnrichmentResponse200OutputProfile:
    """ 
        Attributes:
            emails (list['SyncContactEnrichmentResponse200OutputProfileEmailsItem']):
            phone_numbers (list['SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem']):
            status (SyncContactEnrichmentResponse200OutputProfileStatus):
            error (Union[Unset, str]):
            exhaustive (Union[None, Unset, bool]):
     """

    emails: list['SyncContactEnrichmentResponse200OutputProfileEmailsItem']
    phone_numbers: list['SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem']
    status: SyncContactEnrichmentResponse200OutputProfileStatus
    error: Union[Unset, str] = UNSET
    exhaustive: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_contact_enrichment_response_200_output_profile_emails_item import SyncContactEnrichmentResponse200OutputProfileEmailsItem
        from ..models.sync_contact_enrichment_response_200_output_profile_phone_numbers_item import SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)



        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)



        status = self.status.value

        error = self.error

        exhaustive: Union[None, Unset, bool]
        if isinstance(self.exhaustive, Unset):
            exhaustive = UNSET
        else:
            exhaustive = self.exhaustive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "emails": emails,
            "phoneNumbers": phone_numbers,
            "status": status,
        })
        if error is not UNSET:
            field_dict["error"] = error
        if exhaustive is not UNSET:
            field_dict["exhaustive"] = exhaustive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_contact_enrichment_response_200_output_profile_emails_item import SyncContactEnrichmentResponse200OutputProfileEmailsItem
        from ..models.sync_contact_enrichment_response_200_output_profile_phone_numbers_item import SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem
        d = dict(src_dict)
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in (_emails):
            emails_item = SyncContactEnrichmentResponse200OutputProfileEmailsItem.from_dict(emails_item_data)



            emails.append(emails_item)


        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in (_phone_numbers):
            phone_numbers_item = SyncContactEnrichmentResponse200OutputProfilePhoneNumbersItem.from_dict(phone_numbers_item_data)



            phone_numbers.append(phone_numbers_item)


        status = SyncContactEnrichmentResponse200OutputProfileStatus(d.pop("status"))




        error = d.pop("error", UNSET)

        def _parse_exhaustive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        exhaustive = _parse_exhaustive(d.pop("exhaustive", UNSET))


        sync_contact_enrichment_response_200_output_profile = cls(
            emails=emails,
            phone_numbers=phone_numbers,
            status=status,
            error=error,
            exhaustive=exhaustive,
        )


        sync_contact_enrichment_response_200_output_profile.additional_properties = d
        return sync_contact_enrichment_response_200_output_profile

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
