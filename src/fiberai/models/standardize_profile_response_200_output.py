from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandardizeProfileResponse200Output")


@_attrs_define
class StandardizeProfileResponse200Output:
    """
    Attributes:
        linkedin_url (str): The resolved LinkedIn profile URL (e.g., 'https://www.linkedin.com/in/williamhgates')
        full_name (None | str | Unset): The person's full name, if available
    """

    linkedin_url: str
    full_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
            }
        )
        if full_name is not UNSET:
            field_dict["fullName"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))

        standardize_profile_response_200_output = cls(
            linkedin_url=linkedin_url,
            full_name=full_name,
        )

        standardize_profile_response_200_output.additional_properties = d
        return standardize_profile_response_200_output

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
