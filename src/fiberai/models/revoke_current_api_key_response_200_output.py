from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RevokeCurrentApiKeyResponse200Output")


@_attrs_define
class RevokeCurrentApiKeyResponse200Output:
    """
    Attributes:
        revoked (bool): Revocation status of the key.
        id (str): The identifier of the revoked key.
    """

    revoked: bool
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revoked = self.revoked

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revoked": revoked,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revoked = d.pop("revoked")

        id = d.pop("id")

        revoke_current_api_key_response_200_output = cls(
            revoked=revoked,
            id=id,
        )

        revoke_current_api_key_response_200_output.additional_properties = d
        return revoke_current_api_key_response_200_output

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
