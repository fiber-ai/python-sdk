from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HemLookupBody")


@_attrs_define
class HemLookupBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        hashed_emails (list[str]): Up to 100 SHA-256, MD5, or SHA-1 digests of lowercased, trimmed email addresses. Each
            hash must be a hexadecimal digest, upper or lower case, of the lowercased and trimmed address — SHA-256 is 64
            characters, MD5 is 32, and SHA-1 is 40. A hash that is not a valid digest is returned as a `rejected` result
            rather than failing the request.
    """

    api_key: str
    hashed_emails: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        hashed_emails = self.hashed_emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "hashedEmails": hashed_emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        hashed_emails = cast(list[str], d.pop("hashedEmails"))

        hem_lookup_body = cls(
            api_key=api_key,
            hashed_emails=hashed_emails,
        )

        hem_lookup_body.additional_properties = d
        return hem_lookup_body

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
