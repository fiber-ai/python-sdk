from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_verify_otp_response_200_output_status import AccountVerifyOtpResponse200OutputStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountVerifyOtpResponse200Output")


@_attrs_define
class AccountVerifyOtpResponse200Output:
    """
    Attributes:
        status (AccountVerifyOtpResponse200OutputStatus):
        api_key (str): The live API key for the new trial organization (starts with sk_live_). Store it securely — it
            cannot be retrieved later.
        credits_awarded (int): Number of credits granted with this trial.
        organization_id (str):
        message (str):
        sandbox_api_key (None | str | Unset): Companion sandbox API key (starts with sk_test_...) for local development
            and integration tests. Null if it was not minted at signup — create one via POST /v1/api-keys/create-sandbox.
    """

    status: AccountVerifyOtpResponse200OutputStatus
    api_key: str
    credits_awarded: int
    organization_id: str
    message: str
    sandbox_api_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        api_key = self.api_key

        credits_awarded = self.credits_awarded

        organization_id = self.organization_id

        message = self.message

        sandbox_api_key: None | str | Unset
        if isinstance(self.sandbox_api_key, Unset):
            sandbox_api_key = UNSET
        else:
            sandbox_api_key = self.sandbox_api_key

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
        if sandbox_api_key is not UNSET:
            field_dict["sandboxApiKey"] = sandbox_api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = AccountVerifyOtpResponse200OutputStatus(d.pop("status"))

        api_key = d.pop("apiKey")

        credits_awarded = d.pop("creditsAwarded")

        organization_id = d.pop("organizationId")

        message = d.pop("message")

        def _parse_sandbox_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sandbox_api_key = _parse_sandbox_api_key(d.pop("sandboxApiKey", UNSET))

        account_verify_otp_response_200_output = cls(
            status=status,
            api_key=api_key,
            credits_awarded=credits_awarded,
            organization_id=organization_id,
            message=message,
            sandbox_api_key=sandbox_api_key,
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
