from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.revoke_current_api_key_body_target import RevokeCurrentApiKeyBodyTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevokeCurrentApiKeyBody")


@_attrs_define
class RevokeCurrentApiKeyBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        target (RevokeCurrentApiKeyBodyTarget | Unset): Which key to act on. SELF acts on the key that authenticates
            this request. OTHER acts on a different key in your organization, supplied in targetApiKey. Default:
            RevokeCurrentApiKeyBodyTarget.SELF.
        target_api_key (None | str | Unset): The key to act on when target is OTHER. Must belong to your organization.
            You can pass prefix, id, or the raw key. Omit when target is SELF.
    """

    api_key: str
    target: RevokeCurrentApiKeyBodyTarget | Unset = RevokeCurrentApiKeyBodyTarget.SELF
    target_api_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        target_api_key: None | str | Unset
        if isinstance(self.target_api_key, Unset):
            target_api_key = UNSET
        else:
            target_api_key = self.target_api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if target_api_key is not UNSET:
            field_dict["targetApiKey"] = target_api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        _target = d.pop("target", UNSET)
        target: RevokeCurrentApiKeyBodyTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = RevokeCurrentApiKeyBodyTarget(_target)

        def _parse_target_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_api_key = _parse_target_api_key(d.pop("targetApiKey", UNSET))

        revoke_current_api_key_body = cls(
            api_key=api_key,
            target=target,
            target_api_key=target_api_key,
        )

        revoke_current_api_key_body.additional_properties = d
        return revoke_current_api_key_body

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
