from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_verify_otp_response_200_output_status import AccountVerifyOtpResponse200OutputStatus

T = TypeVar("T", bound="AccountVerifyOtpResponse200Output")


@_attrs_define
class AccountVerifyOtpResponse200Output:
    """
    Attributes:
        status (AccountVerifyOtpResponse200OutputStatus):
        api_key (str): The API key for the new trial organization. Store it securely — it cannot be retrieved later.
        credits_awarded (int): Number of credits granted with this trial.
        organization_id (str):
        message (str):
    """

    status: AccountVerifyOtpResponse200OutputStatus
    api_key: str
    credits_awarded: int
    organization_id: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        api_key = self.api_key

        credits_awarded = self.credits_awarded

        organization_id = self.organization_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "apiKey": api_key,
                "creditsAwarded": credits_awarded,
                "organizationId": organization_id,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = AccountVerifyOtpResponse200OutputStatus(d.pop("status"))

        api_key = d.pop("apiKey")

        credits_awarded = d.pop("creditsAwarded")

        organization_id = d.pop("organizationId")

        message = d.pop("message")

        account_verify_otp_response_200_output = cls(
            status=status,
            api_key=api_key,
            credits_awarded=credits_awarded,
            organization_id=organization_id,
            message=message,
        )

        account_verify_otp_response_200_output.additional_properties = d
        return account_verify_otp_response_200_output

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
