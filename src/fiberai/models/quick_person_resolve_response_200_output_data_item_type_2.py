from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quick_person_resolve_response_200_output_data_item_type_2_identifier import (
    QuickPersonResolveResponse200OutputDataItemType2Identifier,
)
from ..models.quick_person_resolve_response_200_output_data_item_type_2_status import (
    QuickPersonResolveResponse200OutputDataItemType2Status,
)

T = TypeVar("T", bound="QuickPersonResolveResponse200OutputDataItemType2")


@_attrs_define
class QuickPersonResolveResponse200OutputDataItemType2:
    """The person opted out of data processing.

    Attributes:
        identifier (QuickPersonResolveResponse200OutputDataItemType2Identifier): The identifier type you supplied,
            echoed back.
        value (str): The identifier value you supplied, echoed back.
        status (QuickPersonResolveResponse200OutputDataItemType2Status): The person asked to be erased. No data is
            returned and you are not charged for this row.
        found (bool): True when `status` is `found`. Kept for compatibility with earlier versions of this endpoint —
            branch on `status` instead.
        person (None):
        opted_out (bool): True when this person has opted out of data processing. No data is returned for them and you
            are not charged for this row.
    """

    identifier: QuickPersonResolveResponse200OutputDataItemType2Identifier
    value: str
    status: QuickPersonResolveResponse200OutputDataItemType2Status
    found: bool
    person: None
    opted_out: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value

        status = self.status.value

        found = self.found

        person = self.person

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
                "optedOut": opted_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = QuickPersonResolveResponse200OutputDataItemType2Identifier(d.pop("identifier"))

        value = d.pop("value")

        status = QuickPersonResolveResponse200OutputDataItemType2Status(d.pop("status"))

        found = d.pop("found")

        person = d.pop("person")

        opted_out = d.pop("optedOut")

        quick_person_resolve_response_200_output_data_item_type_2 = cls(
            identifier=identifier,
            value=value,
            status=status,
            found=found,
            person=person,
            opted_out=opted_out,
        )

        quick_person_resolve_response_200_output_data_item_type_2.additional_properties = d
        return quick_person_resolve_response_200_output_data_item_type_2

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
