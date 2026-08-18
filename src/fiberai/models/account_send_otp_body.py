from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_send_otp_body_purpose import AccountSendOtpBodyPurpose
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountSendOtpBody")


@_attrs_define
class AccountSendOtpBody:
    """
    Attributes:
        email (str): Work email address to send the verification code to.
        purpose (AccountSendOtpBodyPurpose | Unset): Which product surface this trial is for. Defaults to agent-api for
            backward compatibility. Default: AccountSendOtpBodyPurpose.AGENT_API.
        first_name (None | str | Unset): Optional first name for the account. When omitted, derived from the email
            local-part.
        last_name (None | str | Unset): Optional last name for the account. When omitted, a default value is used.
        company_name (None | str | Unset): Optional organization display name. When omitted, derived from the email
            local-part.
    """

    email: str
    purpose: AccountSendOtpBodyPurpose | Unset = AccountSendOtpBodyPurpose.AGENT_API
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _purpose = d.pop("purpose", UNSET)
        purpose: AccountSendOtpBodyPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = AccountSendOtpBodyPurpose(_purpose)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        account_send_otp_body = cls(
            email=email,
            purpose=purpose,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
        )

        account_send_otp_body.additional_properties = d
        return account_send_otp_body

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
