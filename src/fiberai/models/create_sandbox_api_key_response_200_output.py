from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateSandboxApiKeyResponse200Output")


@_attrs_define
class CreateSandboxApiKeyResponse200Output:
    """
    Attributes:
        id (str): id of your api key. This or prefix can be used to identify the key.
        name (str): Name of your api key.
        prefix (str): Non secret prefix of your api key. Used for identification.
        expires_at (datetime.datetime | None): When the key expires. Null implies key never expires.
        max_credits (float | None): The lifetime credit ceiling for this key. Null implies key has no per-key credit
            limit.
        credits_used (float): Credits consumed by this key so far over its lifetime.
        created_at (datetime.datetime): When the key was created, as an ISO 8601 timestamp.
        is_revoked (bool): Whether the key has been revoked. Revoked keys can no longer authenticate. Only ever true in
            listings that include revoked keys.
        api_key (str): The plaintext sandbox API key (starts with sk_test_). Shown once — store it securely, it cannot
            be retrieved later.
    """

    id: str
    name: str
    prefix: str
    expires_at: datetime.datetime | None
    max_credits: float | None
    credits_used: float
    created_at: datetime.datetime
    is_revoked: bool
    api_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        max_credits: float | None
        max_credits = self.max_credits

        credits_used = self.credits_used

        created_at = self.created_at.isoformat()

        is_revoked = self.is_revoked

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "expiresAt": expires_at,
                "maxCredits": max_credits,
                "creditsUsed": credits_used,
                "createdAt": created_at,
                "isRevoked": is_revoked,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_max_credits(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        max_credits = _parse_max_credits(d.pop("maxCredits"))

        credits_used = d.pop("creditsUsed")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        is_revoked = d.pop("isRevoked")

        api_key = d.pop("apiKey")

        create_sandbox_api_key_response_200_output = cls(
            id=id,
            name=name,
            prefix=prefix,
            expires_at=expires_at,
            max_credits=max_credits,
            credits_used=credits_used,
            created_at=created_at,
            is_revoked=is_revoked,
            api_key=api_key,
        )

        create_sandbox_api_key_response_200_output.additional_properties = d
        return create_sandbox_api_key_response_200_output

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
