from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instant_contact_reveal_response_200_output_profile_emails_item import (
        InstantContactRevealResponse200OutputProfileEmailsItem,
    )
    from ..models.instant_contact_reveal_response_200_output_profile_phone_numbers_item import (
        InstantContactRevealResponse200OutputProfilePhoneNumbersItem,
    )
    from ..models.instant_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
        InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,
    )


T = TypeVar("T", bound="InstantContactRevealResponse200OutputProfile")


@_attrs_define
class InstantContactRevealResponse200OutputProfile:
    """
    Attributes:
        emails (list[InstantContactRevealResponse200OutputProfileEmailsItem]): All emails found for this profile,
            ordered by priority.
        phone_numbers (list[InstantContactRevealResponse200OutputProfilePhoneNumbersItem]): All phone numbers found for
            this profile.
        unmatched_work_emails (list[InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset): Work
            emails found for this person whose domain does not match the person's current company (or the company you
            specified). These are not included in emails. Present only when at least one such email was found.
    """

    emails: list[InstantContactRevealResponse200OutputProfileEmailsItem]
    phone_numbers: list[InstantContactRevealResponse200OutputProfilePhoneNumbersItem]
    unmatched_work_emails: list[InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset = UNSET
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

        unmatched_work_emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unmatched_work_emails, Unset):
            unmatched_work_emails = []
            for unmatched_work_emails_item_data in self.unmatched_work_emails:
                unmatched_work_emails_item = unmatched_work_emails_item_data.to_dict()
                unmatched_work_emails.append(unmatched_work_emails_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "phoneNumbers": phone_numbers,
            }
        )
        if unmatched_work_emails is not UNSET:
            field_dict["unmatchedWorkEmails"] = unmatched_work_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_contact_reveal_response_200_output_profile_emails_item import (
            InstantContactRevealResponse200OutputProfileEmailsItem,  # noqa: PLC0415
        )
        from ..models.instant_contact_reveal_response_200_output_profile_phone_numbers_item import (
            InstantContactRevealResponse200OutputProfilePhoneNumbersItem,  # noqa: PLC0415
        )
        from ..models.instant_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
            InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = InstantContactRevealResponse200OutputProfileEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = InstantContactRevealResponse200OutputProfilePhoneNumbersItem.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        _unmatched_work_emails = d.pop("unmatchedWorkEmails", UNSET)
        unmatched_work_emails: list[InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset = UNSET
        if _unmatched_work_emails is not UNSET:
            unmatched_work_emails = []
            for unmatched_work_emails_item_data in _unmatched_work_emails:
                unmatched_work_emails_item = (
                    InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem.from_dict(
                        unmatched_work_emails_item_data
                    )
                )

                unmatched_work_emails.append(unmatched_work_emails_item)

        instant_contact_reveal_response_200_output_profile = cls(
            emails=emails,
            phone_numbers=phone_numbers,
            unmatched_work_emails=unmatched_work_emails,
        )

        instant_contact_reveal_response_200_output_profile.additional_properties = d
        return instant_contact_reveal_response_200_output_profile

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
