from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.premium_phone_reveal_response_200_output_phone_numbers_item import (
        PremiumPhoneRevealResponse200OutputPhoneNumbersItem,
    )


T = TypeVar("T", bound="PremiumPhoneRevealResponse200Output")


@_attrs_define
class PremiumPhoneRevealResponse200Output:
    """
    Attributes:
        linkedin_url (str): Resolved LinkedIn profile URL.
        phone_numbers (list[PremiumPhoneRevealResponse200OutputPhoneNumbersItem]): Phone numbers found for this person,
            annotated with identity verification when available.
    """

    linkedin_url: str
    phone_numbers: list[PremiumPhoneRevealResponse200OutputPhoneNumbersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "phoneNumbers": phone_numbers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.premium_phone_reveal_response_200_output_phone_numbers_item import (
            PremiumPhoneRevealResponse200OutputPhoneNumbersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = PremiumPhoneRevealResponse200OutputPhoneNumbersItem.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        premium_phone_reveal_response_200_output = cls(
            linkedin_url=linkedin_url,
            phone_numbers=phone_numbers,
        )

        premium_phone_reveal_response_200_output.additional_properties = d
        return premium_phone_reveal_response_200_output

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
