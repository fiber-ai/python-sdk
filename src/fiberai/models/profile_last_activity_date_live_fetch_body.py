from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProfileLastActivityDateLiveFetchBody")


@_attrs_define
class ProfileLastActivityDateLiveFetchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        identifier (str): LinkedIn profile URL is preferred (for example, 'https://www.linkedin.com/in/williamhgates/').
            A LinkedIn slug ('williamhgates') or Sales Navigator URN is also accepted.
    """

    api_key: str
    identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        identifier = d.pop("identifier")

        profile_last_activity_date_live_fetch_body = cls(
            api_key=api_key,
            identifier=identifier,
        )

        profile_last_activity_date_live_fetch_body.additional_properties = d
        return profile_last_activity_date_live_fetch_body

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
