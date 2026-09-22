from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_quick_contact_reveal_response_200_output_profile_status import (
    SyncQuickContactRevealResponse200OutputProfileStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_quick_contact_reveal_response_200_output_profile_emails_item import (
        SyncQuickContactRevealResponse200OutputProfileEmailsItem,
    )
    from ..models.sync_quick_contact_reveal_response_200_output_profile_phone_numbers_item import (
        SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem,
    )
    from ..models.sync_quick_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
        SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,
    )


T = TypeVar("T", bound="SyncQuickContactRevealResponse200OutputProfile")


@_attrs_define
class SyncQuickContactRevealResponse200OutputProfile:
    """
    Attributes:
        status (SyncQuickContactRevealResponse200OutputProfileStatus):
        emails (list[SyncQuickContactRevealResponse200OutputProfileEmailsItem]):
        phone_numbers (list[SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem]):
        success (bool):
        task_id (str):
        linkedin_url (str):
        name (None | str | Unset): The person's full name. Null when no resolved name is available.
        unmatched_work_emails (list[SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset):
            Work emails found for this person whose domain does not match the person's current company (or the company you
            specified). These are not included in emails. Present only when at least one such email was found.
    """

    status: SyncQuickContactRevealResponse200OutputProfileStatus
    emails: list[SyncQuickContactRevealResponse200OutputProfileEmailsItem]
    phone_numbers: list[SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem]
    success: bool
    task_id: str
    linkedin_url: str
    name: None | str | Unset = UNSET
    unmatched_work_emails: list[SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        success = self.success

        task_id = self.task_id

        linkedin_url = self.linkedin_url

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "emails": emails,
                "phoneNumbers": phone_numbers,
                "success": success,
                "task_id": task_id,
                "linkedin_url": linkedin_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if unmatched_work_emails is not UNSET:
            field_dict["unmatchedWorkEmails"] = unmatched_work_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_quick_contact_reveal_response_200_output_profile_emails_item import (
            SyncQuickContactRevealResponse200OutputProfileEmailsItem,  # noqa: PLC0415
        )
        from ..models.sync_quick_contact_reveal_response_200_output_profile_phone_numbers_item import (
            SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem,  # noqa: PLC0415
        )
        from ..models.sync_quick_contact_reveal_response_200_output_profile_unmatched_work_emails_item import (
            SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = SyncQuickContactRevealResponse200OutputProfileStatus(d.pop("status"))

        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = SyncQuickContactRevealResponse200OutputProfileEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        success = d.pop("success")

        task_id = d.pop("task_id")

        linkedin_url = d.pop("linkedin_url")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _unmatched_work_emails = d.pop("unmatchedWorkEmails", UNSET)
        unmatched_work_emails: list[SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem] | Unset = (
            UNSET
        )
        if _unmatched_work_emails is not UNSET:
            unmatched_work_emails = []
            for unmatched_work_emails_item_data in _unmatched_work_emails:
                unmatched_work_emails_item = (
                    SyncQuickContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem.from_dict(
                        unmatched_work_emails_item_data
                    )
                )

                unmatched_work_emails.append(unmatched_work_emails_item)

        sync_quick_contact_reveal_response_200_output_profile = cls(
            status=status,
            emails=emails,
            phone_numbers=phone_numbers,
            success=success,
            task_id=task_id,
            linkedin_url=linkedin_url,
            name=name,
            unmatched_work_emails=unmatched_work_emails,
        )

        sync_quick_contact_reveal_response_200_output_profile.additional_properties = d
        return sync_quick_contact_reveal_response_200_output_profile

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
