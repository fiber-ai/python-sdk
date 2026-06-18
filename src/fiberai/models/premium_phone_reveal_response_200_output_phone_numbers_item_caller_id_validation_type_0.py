from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.premium_phone_reveal_response_200_output_phone_numbers_item_caller_id_validation_type_0_category import (
    PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0Category,
)

T = TypeVar("T", bound="PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0")


@_attrs_define
class PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0:
    """Result for attempted phone number verification.

    Attributes:
        category (PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0Category): How confidently
            this phone number is associated with the person.
        reasoning (str): Brief explanation for the confidence level.
        caller_id_name (str): The registered name for this phone number.
    """

    category: PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0Category
    reasoning: str
    caller_id_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        reasoning = self.reasoning

        caller_id_name = self.caller_id_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "reasoning": reasoning,
                "callerIdName": caller_id_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0Category(d.pop("category"))

        reasoning = d.pop("reasoning")

        caller_id_name = d.pop("callerIdName")

        premium_phone_reveal_response_200_output_phone_numbers_item_caller_id_validation_type_0 = cls(
            category=category,
            reasoning=reasoning,
            caller_id_name=caller_id_name,
        )

        premium_phone_reveal_response_200_output_phone_numbers_item_caller_id_validation_type_0.additional_properties = d
        return premium_phone_reveal_response_200_output_phone_numbers_item_caller_id_validation_type_0

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
