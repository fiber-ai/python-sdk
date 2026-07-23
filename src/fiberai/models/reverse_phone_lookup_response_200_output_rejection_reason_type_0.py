from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReversePhoneLookupResponse200OutputRejectionReasonType0")


@_attrs_define
class ReversePhoneLookupResponse200OutputRejectionReasonType0:
    """Present when the phone number is unresolvable (e.g. invalid format, not found).

    Attributes:
        reason (str): Why the phone number couldn't be resolved
    """

    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        reverse_phone_lookup_response_200_output_rejection_reason_type_0 = cls(
            reason=reason,
        )

        reverse_phone_lookup_response_200_output_rejection_reason_type_0.additional_properties = d
        return reverse_phone_lookup_response_200_output_rejection_reason_type_0

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
