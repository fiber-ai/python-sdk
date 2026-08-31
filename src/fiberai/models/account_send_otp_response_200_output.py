from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_send_otp_response_200_output_status import AccountSendOtpResponse200OutputStatus

if TYPE_CHECKING:
    from ..models.account_send_otp_response_200_output_next import AccountSendOtpResponse200OutputNext


T = TypeVar("T", bound="AccountSendOtpResponse200Output")


@_attrs_define
class AccountSendOtpResponse200Output:
    """
    Attributes:
        status (AccountSendOtpResponse200OutputStatus):
        verification_id (str): Pass this unchanged to POST /v1/account/verify-otp.
        message (str):
        next_ (AccountSendOtpResponse200OutputNext): Next request an agent or client should make after reading the OTP
            from email.
    """

    status: AccountSendOtpResponse200OutputStatus
    verification_id: str
    message: str
    next_: AccountSendOtpResponse200OutputNext
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        verification_id = self.verification_id

        message = self.message

        next_ = self.next_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "verificationId": verification_id,
                "message": message,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_send_otp_response_200_output_next import (
            AccountSendOtpResponse200OutputNext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = AccountSendOtpResponse200OutputStatus(d.pop("status"))

        verification_id = d.pop("verificationId")

        message = d.pop("message")

        next_ = AccountSendOtpResponse200OutputNext.from_dict(d.pop("next"))

        account_send_otp_response_200_output = cls(
            status=status,
            verification_id=verification_id,
            message=message,
            next_=next_,
        )

        account_send_otp_response_200_output.additional_properties = d
        return account_send_otp_response_200_output

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
