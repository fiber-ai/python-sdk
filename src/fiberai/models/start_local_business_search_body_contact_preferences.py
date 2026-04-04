from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartLocalBusinessSearchBodyContactPreferences")


@_attrs_define
class StartLocalBusinessSearchBodyContactPreferences:
    """Controls which contact data to fetch for all companies in this payload.

    Attributes:
        company_emails (bool | Unset): Fetch emails found on the company website Default: True.
        company_phones (bool | Unset): Fetch phone numbers found on the company website Default: True.
        person_emails (bool | Unset): Fetch work/personal emails of people found via job title search Default: True.
        person_phones (bool | Unset): Fetch phone numbers of people found via job title search Default: True.
    """

    company_emails: bool | Unset = True
    company_phones: bool | Unset = True
    person_emails: bool | Unset = True
    person_phones: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_emails = self.company_emails

        company_phones = self.company_phones

        person_emails = self.person_emails

        person_phones = self.person_phones

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_emails is not UNSET:
            field_dict["companyEmails"] = company_emails
        if company_phones is not UNSET:
            field_dict["companyPhones"] = company_phones
        if person_emails is not UNSET:
            field_dict["personEmails"] = person_emails
        if person_phones is not UNSET:
            field_dict["personPhones"] = person_phones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_emails = d.pop("companyEmails", UNSET)

        company_phones = d.pop("companyPhones", UNSET)

        person_emails = d.pop("personEmails", UNSET)

        person_phones = d.pop("personPhones", UNSET)

        start_local_business_search_body_contact_preferences = cls(
            company_emails=company_emails,
            company_phones=company_phones,
            person_emails=person_emails,
            person_phones=person_phones,
        )

        start_local_business_search_body_contact_preferences.additional_properties = d
        return start_local_business_search_body_contact_preferences

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
