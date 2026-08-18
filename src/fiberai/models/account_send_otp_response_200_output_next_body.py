from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountSendOtpResponse200OutputNextBody")


@_attrs_define
class AccountSendOtpResponse200OutputNextBody:
    """
    Attributes:
        verification_id (str): Same verificationId returned in this response.
        otp (str): Replace with the one-time code delivered to the email inbox.
    """

    verification_id: str
    otp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verification_id = self.verification_id

        otp = self.otp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verificationId": verification_id,
                "otp": otp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verification_id = d.pop("verificationId")

        otp = d.pop("otp")

        account_send_otp_response_200_output_next_body = cls(
            verification_id=verification_id,
            otp=otp,
        )

        account_send_otp_response_200_output_next_body.additional_properties = d
        return account_send_otp_response_200_output_next_body

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
