from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quick_person_resolve_response_200_output_data_item_type_3_identifier import (
    QuickPersonResolveResponse200OutputDataItemType3Identifier,
)
from ..models.quick_person_resolve_response_200_output_data_item_type_3_reason import (
    QuickPersonResolveResponse200OutputDataItemType3Reason,
)
from ..models.quick_person_resolve_response_200_output_data_item_type_3_status import (
    QuickPersonResolveResponse200OutputDataItemType3Status,
)

T = TypeVar("T", bound="QuickPersonResolveResponse200OutputDataItemType3")


@_attrs_define
class QuickPersonResolveResponse200OutputDataItemType3:
    """The value was not a usable identifier.

    Attributes:
        identifier (QuickPersonResolveResponse200OutputDataItemType3Identifier): The identifier type you supplied,
            echoed back.
        value (str): The identifier value you supplied, echoed back.
        status (QuickPersonResolveResponse200OutputDataItemType3Status): The value can never resolve as the identifier
            type you declared. Nothing was looked up and you are not charged for this row.
        found (bool): True when `status` is `found`. Kept for compatibility with earlier versions of this endpoint —
            branch on `status` instead.
        person (None):
        reason (QuickPersonResolveResponse200OutputDataItemType3Reason): What is wrong with this value.
        message (str): How to correct this value.
        opted_out (bool): True when this person has opted out of data processing. No data is returned for them and you
            are not charged for this row.
    """

    identifier: QuickPersonResolveResponse200OutputDataItemType3Identifier
    value: str
    status: QuickPersonResolveResponse200OutputDataItemType3Status
    found: bool
    person: None
    reason: QuickPersonResolveResponse200OutputDataItemType3Reason
    message: str
    opted_out: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value

        status = self.status.value

        found = self.found

        person = self.person

        reason = self.reason.value

        message = self.message

        opted_out = self.opted_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "value": value,
                "status": status,
                "found": found,
                "person": person,
                "reason": reason,
                "message": message,
                "optedOut": opted_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = QuickPersonResolveResponse200OutputDataItemType3Identifier(d.pop("identifier"))

        value = d.pop("value")

        status = QuickPersonResolveResponse200OutputDataItemType3Status(d.pop("status"))

        found = d.pop("found")

        person = d.pop("person")

        reason = QuickPersonResolveResponse200OutputDataItemType3Reason(d.pop("reason"))

        message = d.pop("message")

        opted_out = d.pop("optedOut")

        quick_person_resolve_response_200_output_data_item_type_3 = cls(
            identifier=identifier,
            value=value,
            status=status,
            found=found,
            person=person,
            reason=reason,
            message=message,
            opted_out=opted_out,
        )

        quick_person_resolve_response_200_output_data_item_type_3.additional_properties = d
        return quick_person_resolve_response_200_output_data_item_type_3

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
