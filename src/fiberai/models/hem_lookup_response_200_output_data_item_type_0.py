from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hem_lookup_response_200_output_data_item_type_0_status import (
    HemLookupResponse200OutputDataItemType0Status,
)

T = TypeVar("T", bound="HemLookupResponse200OutputDataItemType0")


@_attrs_define
class HemLookupResponse200OutputDataItemType0:
    """
    Attributes:
        status (HemLookupResponse200OutputDataItemType0Status):
        hashed_email (str): The digest exactly as you supplied it, for correlation.
        original_email (str): The email address this digest resolves to — the original address that was hashed to
            produce it.
        linkedin_url (None | str): The person's LinkedIn profile URL, like 'https://www.linkedin.com/in/jane-doe', when
            we have one linked to this address.
        linkedin_user_id (None | str): LinkedIn member id for the person, when known.
    """

    status: HemLookupResponse200OutputDataItemType0Status
    hashed_email: str
    original_email: str
    linkedin_url: None | str
    linkedin_user_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        hashed_email = self.hashed_email

        original_email = self.original_email

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        linkedin_user_id: None | str
        linkedin_user_id = self.linkedin_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "hashedEmail": hashed_email,
                "originalEmail": original_email,
                "linkedinUrl": linkedin_url,
                "linkedinUserID": linkedin_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = HemLookupResponse200OutputDataItemType0Status(d.pop("status"))

        hashed_email = d.pop("hashedEmail")

        original_email = d.pop("originalEmail")

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_linkedin_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_user_id = _parse_linkedin_user_id(d.pop("linkedinUserID"))

        hem_lookup_response_200_output_data_item_type_0 = cls(
            status=status,
            hashed_email=hashed_email,
            original_email=original_email,
            linkedin_url=linkedin_url,
            linkedin_user_id=linkedin_user_id,
        )

        hem_lookup_response_200_output_data_item_type_0.additional_properties = d
        return hem_lookup_response_200_output_data_item_type_0

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
