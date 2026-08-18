from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_api_key_expiration_body_operation import UpdateApiKeyExpirationBodyOperation
from ..models.update_api_key_expiration_body_target import UpdateApiKeyExpirationBodyTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApiKeyExpirationBody")


@_attrs_define
class UpdateApiKeyExpirationBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        operation (UpdateApiKeyExpirationBodyOperation): set: use an absolute date. extend: push the expiration later by
            a number of days. prepone: pull it earlier by a number of days. remove: make the key never expire.
        target (UpdateApiKeyExpirationBodyTarget | Unset): Which key to act on. SELF acts on the key that authenticates
            this request. OTHER acts on a different key in your organization, supplied in targetApiKey. Default:
            UpdateApiKeyExpirationBodyTarget.SELF.
        target_api_key (None | str | Unset): The key to act on when target is OTHER. Must belong to your organization.
            You can pass prefix, id, or the raw key. Omit when target is SELF.
        expires_at (datetime.datetime | None | Unset): The new absolute expiration timestamp (ISO 8601). Required for
            the set operation and must be in the future; ignored otherwise.
        days (int | None | Unset): How many days to move the expiration by. Required for the extend and prepone
            operations; ignored otherwise.
    """

    api_key: str
    operation: UpdateApiKeyExpirationBodyOperation
    target: UpdateApiKeyExpirationBodyTarget | Unset = UpdateApiKeyExpirationBodyTarget.SELF
    target_api_key: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        operation = self.operation.value

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        target_api_key: None | str | Unset
        if isinstance(self.target_api_key, Unset):
            target_api_key = UNSET
        else:
            target_api_key = self.target_api_key

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        days: int | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        else:
            days = self.days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "operation": operation,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if target_api_key is not UNSET:
            field_dict["targetApiKey"] = target_api_key
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        operation = UpdateApiKeyExpirationBodyOperation(d.pop("operation"))

        _target = d.pop("target", UNSET)
        target: UpdateApiKeyExpirationBodyTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = UpdateApiKeyExpirationBodyTarget(_target)

        def _parse_target_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_api_key = _parse_target_api_key(d.pop("targetApiKey", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))

        update_api_key_expiration_body = cls(
            api_key=api_key,
            operation=operation,
            target=target,
            target_api_key=target_api_key,
            expires_at=expires_at,
            days=days,
        )

        update_api_key_expiration_body.additional_properties = d
        return update_api_key_expiration_body

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
