from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_send_otp_response_200_output_next_method import AccountSendOtpResponse200OutputNextMethod
from ..models.account_send_otp_response_200_output_next_path import AccountSendOtpResponse200OutputNextPath

if TYPE_CHECKING:
    from ..models.account_send_otp_response_200_output_next_body import AccountSendOtpResponse200OutputNextBody


T = TypeVar("T", bound="AccountSendOtpResponse200OutputNext")


@_attrs_define
class AccountSendOtpResponse200OutputNext:
    """Next request an agent or client should make after reading the OTP from email.

    Attributes:
        method (AccountSendOtpResponse200OutputNextMethod):
        path (AccountSendOtpResponse200OutputNextPath): Call this endpoint with the OTP from email to finish signup.
        body (AccountSendOtpResponse200OutputNextBody):
    """

    method: AccountSendOtpResponse200OutputNextMethod
    path: AccountSendOtpResponse200OutputNextPath
    body: AccountSendOtpResponse200OutputNextBody
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        path = self.path.value

        body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "path": path,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_send_otp_response_200_output_next_body import AccountSendOtpResponse200OutputNextBody

        d = dict(src_dict)
        method = AccountSendOtpResponse200OutputNextMethod(d.pop("method"))

        path = AccountSendOtpResponse200OutputNextPath(d.pop("path"))

        body = AccountSendOtpResponse200OutputNextBody.from_dict(d.pop("body"))

        account_send_otp_response_200_output_next = cls(
            method=method,
            path=path,
            body=body,
        )

        account_send_otp_response_200_output_next.additional_properties = d
        return account_send_otp_response_200_output_next

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
