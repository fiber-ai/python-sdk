from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllApiKeysBody")


@_attrs_define
class GetAllApiKeysBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        include_revoked (bool | Unset): Include revoked keys in the results. Defaults to false, returning only active
            keys. Default: False.
    """

    api_key: str
    include_revoked: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        include_revoked = self.include_revoked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if include_revoked is not UNSET:
            field_dict["includeRevoked"] = include_revoked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        include_revoked = d.pop("includeRevoked", UNSET)

        get_all_api_keys_body = cls(
            api_key=api_key,
            include_revoked=include_revoked,
        )

        get_all_api_keys_body.additional_properties = d
        return get_all_api_keys_body

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
