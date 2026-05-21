from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CancelBatchContactDetailsResponse200Output")


@_attrs_define
class CancelBatchContactDetailsResponse200Output:
    """
    Attributes:
        cancelled_count (int): The number of profiles cancelled.
        credits_refunded (float): The number of credits refunded for cancelled profiles.
        message (str): A human-readable summary of the cancellation result.
    """

    cancelled_count: int
    credits_refunded: float
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelled_count = self.cancelled_count

        credits_refunded = self.credits_refunded

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cancelledCount": cancelled_count,
                "creditsRefunded": credits_refunded,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancelled_count = d.pop("cancelledCount")

        credits_refunded = d.pop("creditsRefunded")

        message = d.pop("message")

        cancel_batch_contact_details_response_200_output = cls(
            cancelled_count=cancelled_count,
            credits_refunded=credits_refunded,
            message=message,
        )

        cancel_batch_contact_details_response_200_output.additional_properties = d
        return cancel_batch_contact_details_response_200_output

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
