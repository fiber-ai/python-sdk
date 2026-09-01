from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_phone_number_body_patience_type_1 import ValidatePhoneNumberBodyPatienceType1
from ..models.validate_phone_number_body_patience_type_2_type_1 import ValidatePhoneNumberBodyPatienceType2Type1
from ..models.validate_phone_number_body_patience_type_3_type_1 import ValidatePhoneNumberBodyPatienceType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidatePhoneNumberBody")


@_attrs_define
class ValidatePhoneNumberBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        phone_number (str): Phone number to validate. E.164 (e.g. +14155551234) is recommended; other formats with
            spaces, dashes, or parentheses are accepted.
        patience (None | Unset | ValidatePhoneNumberBodyPatienceType1 | ValidatePhoneNumberBodyPatienceType2Type1 |
            ValidatePhoneNumberBodyPatienceType3Type1): How long to wait for phone-number verification after a number is
            found. Higher patience increases average response time but improves identity and reachability accuracy. MINIMUM
            is the least thorough verification option.
    """

    api_key: str
    phone_number: str
    patience: (
        None
        | Unset
        | ValidatePhoneNumberBodyPatienceType1
        | ValidatePhoneNumberBodyPatienceType2Type1
        | ValidatePhoneNumberBodyPatienceType3Type1
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        phone_number = self.phone_number

        patience: None | str | Unset
        if isinstance(self.patience, Unset):
            patience = UNSET
        elif isinstance(self.patience, ValidatePhoneNumberBodyPatienceType1):
            patience = self.patience.value
        elif isinstance(self.patience, ValidatePhoneNumberBodyPatienceType2Type1):
            patience = self.patience.value
        elif isinstance(self.patience, ValidatePhoneNumberBodyPatienceType3Type1):
            patience = self.patience.value
        else:
            patience = self.patience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "phoneNumber": phone_number,
            }
        )
        if patience is not UNSET:
            field_dict["patience"] = patience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        phone_number = d.pop("phoneNumber")

        def _parse_patience(
            data: object,
        ) -> (
            None
            | Unset
            | ValidatePhoneNumberBodyPatienceType1
            | ValidatePhoneNumberBodyPatienceType2Type1
            | ValidatePhoneNumberBodyPatienceType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_1 = ValidatePhoneNumberBodyPatienceType1(data)

                return patience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_2_type_1 = ValidatePhoneNumberBodyPatienceType2Type1(data)

                return patience_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_3_type_1 = ValidatePhoneNumberBodyPatienceType3Type1(data)

                return patience_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | ValidatePhoneNumberBodyPatienceType1
                | ValidatePhoneNumberBodyPatienceType2Type1
                | ValidatePhoneNumberBodyPatienceType3Type1,
                data,
            )

        patience = _parse_patience(d.pop("patience", UNSET))

        validate_phone_number_body = cls(
            api_key=api_key,
            phone_number=phone_number,
            patience=patience,
        )

        validate_phone_number_body.additional_properties = d
        return validate_phone_number_body

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
