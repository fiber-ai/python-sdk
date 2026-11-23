from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReverseEmailLookupBody")


@_attrs_define
class ReverseEmailLookupBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        email (str): The email address of a person whose LinkedIn profile you want to find.
        refresh_not_found_results (bool | None | Unset): When true, an email we recently found no profile for is
            searched again instead of returning the saved not-found result. A retry takes as long as a first lookup and, if
            it still finds nothing, is billed as a miss; the saved not-found result is free. Omit for the normal behaviour.
    """

    api_key: str
    email: str
    refresh_not_found_results: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        email = self.email

        refresh_not_found_results: bool | None | Unset
        if isinstance(self.refresh_not_found_results, Unset):
            refresh_not_found_results = UNSET
        else:
            refresh_not_found_results = self.refresh_not_found_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "email": email,
            }
        )
        if refresh_not_found_results is not UNSET:
            field_dict["refreshNotFoundResults"] = refresh_not_found_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        email = d.pop("email")

        def _parse_refresh_not_found_results(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        refresh_not_found_results = _parse_refresh_not_found_results(d.pop("refreshNotFoundResults", UNSET))

        reverse_email_lookup_body = cls(
            api_key=api_key,
            email=email,
            refresh_not_found_results=refresh_not_found_results,
        )

        reverse_email_lookup_body.additional_properties = d
        return reverse_email_lookup_body

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
