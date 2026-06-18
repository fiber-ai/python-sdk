from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lite_contact_reveal_response_200_output_profile_phone_numbers_item_type_type_1 import (
    LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1,
)
from ..models.lite_contact_reveal_response_200_output_profile_phone_numbers_item_type_type_2_type_1 import (
    LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1,
)
from ..models.lite_contact_reveal_response_200_output_profile_phone_numbers_item_type_type_3_type_1 import (
    LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiteContactRevealResponse200OutputProfilePhoneNumbersItem")


@_attrs_define
class LiteContactRevealResponse200OutputProfilePhoneNumbersItem:
    """
    Attributes:
        phone_number (None | str | Unset): Phone number for the person.
        type_ (LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1 |
            LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1 |
            LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1 | None | Unset): Classification of the
            phone number.
    """

    phone_number: None | str | Unset = UNSET
    type_: (
        LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1
        | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1
        | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_type_(
            data: object,
        ) -> (
            LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1
            | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1
            | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1
                | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType2Type1
                | LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType3Type1
                | None
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        lite_contact_reveal_response_200_output_profile_phone_numbers_item = cls(
            phone_number=phone_number,
            type_=type_,
        )

        lite_contact_reveal_response_200_output_profile_phone_numbers_item.additional_properties = d
        return lite_contact_reveal_response_200_output_profile_phone_numbers_item

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
