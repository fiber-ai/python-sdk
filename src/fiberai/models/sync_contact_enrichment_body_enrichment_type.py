from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SyncContactEnrichmentBodyEnrichmentType")



@_attrs_define
class SyncContactEnrichmentBodyEnrichmentType:
    """ Enrichment types to be requested. Include the ones you want to look for, we will charge credits for the ones you
    request. For example, { getWorkEmails: true, getPersonalEmails: true, getPhoneNumbers: true }

        Attributes:
            get_work_emails (Union[Unset, bool]):  Default: True.
            get_personal_emails (Union[Unset, bool]):  Default: True.
            get_phone_numbers (Union[Unset, bool]):  Default: True.
     """

    get_work_emails: Union[Unset, bool] = True
    get_personal_emails: Union[Unset, bool] = True
    get_phone_numbers: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        get_work_emails = self.get_work_emails

        get_personal_emails = self.get_personal_emails

        get_phone_numbers = self.get_phone_numbers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if get_work_emails is not UNSET:
            field_dict["getWorkEmails"] = get_work_emails
        if get_personal_emails is not UNSET:
            field_dict["getPersonalEmails"] = get_personal_emails
        if get_phone_numbers is not UNSET:
            field_dict["getPhoneNumbers"] = get_phone_numbers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_work_emails = d.pop("getWorkEmails", UNSET)

        get_personal_emails = d.pop("getPersonalEmails", UNSET)

        get_phone_numbers = d.pop("getPhoneNumbers", UNSET)

        sync_contact_enrichment_body_enrichment_type = cls(
            get_work_emails=get_work_emails,
            get_personal_emails=get_personal_emails,
            get_phone_numbers=get_phone_numbers,
        )


        sync_contact_enrichment_body_enrichment_type.additional_properties = d
        return sync_contact_enrichment_body_enrichment_type

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
