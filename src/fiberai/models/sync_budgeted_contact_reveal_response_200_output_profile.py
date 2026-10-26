from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_budgeted_contact_reveal_response_200_output_profile_emails_item import (
        SyncBudgetedContactRevealResponse200OutputProfileEmailsItem,
    )
    from ..models.sync_budgeted_contact_reveal_response_200_output_profile_phone_numbers_item import (
        SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItem,
    )
    from ..models.sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
        SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,
    )


T = TypeVar("T", bound="SyncBudgetedContactRevealResponse200OutputProfile")


@_attrs_define
class SyncBudgetedContactRevealResponse200OutputProfile:
    """
    Attributes:
        emails (list[SyncBudgetedContactRevealResponse200OutputProfileEmailsItem]):
        phone_numbers (list[SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItem]):
        name (None | str | Unset): The person's full name. Null when unavailable.
        unmatched_work_emails (list[SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset):
            Work emails whose domain does not match the person's current company (or the company you specified). Not
            included in emails; present only when at least one was found.
        linkedin_url (None | str | Unset): Public LinkedIn profile URL. Null when none is available.
    """

    emails: list[SyncBudgetedContactRevealResponse200OutputProfileEmailsItem]
    phone_numbers: list[SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItem]
    name: None | str | Unset = UNSET
    unmatched_work_emails: list[SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset = (
        UNSET
    )
    linkedin_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        unmatched_work_emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unmatched_work_emails, Unset):
            unmatched_work_emails = []
            for unmatched_work_emails_item_data in self.unmatched_work_emails:
                unmatched_work_emails_item = unmatched_work_emails_item_data.to_dict()
                unmatched_work_emails.append(unmatched_work_emails_item)

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "phoneNumbers": phone_numbers,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if unmatched_work_emails is not UNSET:
            field_dict["unmatchedWorkEmails"] = unmatched_work_emails
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_budgeted_contact_reveal_response_200_output_profile_emails_item import (
            SyncBudgetedContactRevealResponse200OutputProfileEmailsItem,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_response_200_output_profile_phone_numbers_item import (
            SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItem,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
            SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = SyncBudgetedContactRevealResponse200OutputProfileEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItem.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _unmatched_work_emails = d.pop("unmatchedWorkEmails", UNSET)
        unmatched_work_emails: (
            list[SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset
        ) = UNSET
        if _unmatched_work_emails is not UNSET:
            unmatched_work_emails = []
            for unmatched_work_emails_item_data in _unmatched_work_emails:
                unmatched_work_emails_item = (
                    SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem.from_dict(
                        unmatched_work_emails_item_data
                    )
                )

                unmatched_work_emails.append(unmatched_work_emails_item)

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        sync_budgeted_contact_reveal_response_200_output_profile = cls(
            emails=emails,
            phone_numbers=phone_numbers,
            name=name,
            unmatched_work_emails=unmatched_work_emails,
            linkedin_url=linkedin_url,
        )

        sync_budgeted_contact_reveal_response_200_output_profile.additional_properties = d
        return sync_budgeted_contact_reveal_response_200_output_profile

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
