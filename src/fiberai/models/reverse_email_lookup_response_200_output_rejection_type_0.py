from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reverse_email_lookup_response_200_output_rejection_type_0_reason import (
    ReverseEmailLookupResponse200OutputRejectionType0Reason,
)

T = TypeVar("T", bound="ReverseEmailLookupResponse200OutputRejectionType0")


@_attrs_define
class ReverseEmailLookupResponse200OutputRejectionType0:
    """Present when the email is unresolvable (e.g. disposable, anonymous relay, or role-based address). The request
    succeeded but there is no person to find.

        Attributes:
            reason (ReverseEmailLookupResponse200OutputRejectionType0Reason): Machine-readable rejection reason
            message (str): Human-readable explanation
    """

    reason: ReverseEmailLookupResponse200OutputRejectionType0Reason
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = ReverseEmailLookupResponse200OutputRejectionType0Reason(d.pop("reason"))

        message = d.pop("message")

        reverse_email_lookup_response_200_output_rejection_type_0 = cls(
            reason=reason,
            message=message,
        )

        reverse_email_lookup_response_200_output_rejection_type_0.additional_properties = d
        return reverse_email_lookup_response_200_output_rejection_type_0

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
