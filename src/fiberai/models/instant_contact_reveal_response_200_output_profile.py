from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.instant_contact_reveal_response_200_output_profile_emails_item import (
        InstantContactRevealResponse200OutputProfileEmailsItem,
    )
    from ..models.instant_contact_reveal_response_200_output_profile_phone_numbers_item import (
        InstantContactRevealResponse200OutputProfilePhoneNumbersItem,
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
    """

    emails: list[InstantContactRevealResponse200OutputProfileEmailsItem]
    phone_numbers: list[InstantContactRevealResponse200OutputProfilePhoneNumbersItem]
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "phoneNumbers": phone_numbers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_contact_reveal_response_200_output_profile_emails_item import (
            InstantContactRevealResponse200OutputProfileEmailsItem,  # noqa: PLC0415
        )
        from ..models.instant_contact_reveal_response_200_output_profile_phone_numbers_item import (
            InstantContactRevealResponse200OutputProfilePhoneNumbersItem,  # noqa: PLC0415
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

        instant_contact_reveal_response_200_output_profile = cls(
            emails=emails,
            phone_numbers=phone_numbers,
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
