from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_contact_enrichment_result_response_200_output_profile_phone_numbers_item_type import (
    PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItemType,
)

T = TypeVar("T", bound="PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItem")


@_attrs_define
class PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItem:
    """
    Attributes:
        number (str):
        type_ (PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItemType):
    """

    number: str
    type_: PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        type_ = PollContactEnrichmentResultResponse200OutputProfilePhoneNumbersItemType(d.pop("type"))

        poll_contact_enrichment_result_response_200_output_profile_phone_numbers_item = cls(
            number=number,
            type_=type_,
        )

        poll_contact_enrichment_result_response_200_output_profile_phone_numbers_item.additional_properties = d
        return poll_contact_enrichment_result_response_200_output_profile_phone_numbers_item

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
