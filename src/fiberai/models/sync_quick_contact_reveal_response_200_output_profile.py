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


T = TypeVar("T", bound="SyncQuickContactRevealResponse200OutputProfile")


@_attrs_define
class SyncQuickContactRevealResponse200OutputProfile:
    """
    Attributes:
        emails (list[SyncQuickContactRevealResponse200OutputProfileEmailsItem]):
        phone_numbers (list[SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem]):
        status (SyncQuickContactRevealResponse200OutputProfileStatus):
        error (str | Unset):
        exhaustive (bool | None | Unset):
    """

    emails: list[SyncQuickContactRevealResponse200OutputProfileEmailsItem]
    phone_numbers: list[SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem]
    status: SyncQuickContactRevealResponse200OutputProfileStatus
    error: str | Unset = UNSET
    exhaustive: bool | None | Unset = UNSET
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

        status = self.status.value

        error = self.error

        exhaustive: bool | None | Unset
        if isinstance(self.exhaustive, Unset):
            exhaustive = UNSET
        else:
            exhaustive = self.exhaustive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "phoneNumbers": phone_numbers,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if exhaustive is not UNSET:
            field_dict["exhaustive"] = exhaustive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_quick_contact_reveal_response_200_output_profile_emails_item import (
            SyncQuickContactRevealResponse200OutputProfileEmailsItem,
        )
        from ..models.sync_quick_contact_reveal_response_200_output_profile_phone_numbers_item import (
            SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItem,
        )

        d = dict(src_dict)
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

        status = SyncQuickContactRevealResponse200OutputProfileStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        def _parse_exhaustive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exhaustive = _parse_exhaustive(d.pop("exhaustive", UNSET))

        sync_quick_contact_reveal_response_200_output_profile = cls(
            emails=emails,
            phone_numbers=phone_numbers,
            status=status,
            error=error,
            exhaustive=exhaustive,
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
