from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.premium_phone_reveal_body_patience_type_1 import PremiumPhoneRevealBodyPatienceType1
from ..models.premium_phone_reveal_body_patience_type_2_type_1 import PremiumPhoneRevealBodyPatienceType2Type1
from ..models.premium_phone_reveal_body_patience_type_3_type_1 import PremiumPhoneRevealBodyPatienceType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PremiumPhoneRevealBody")


@_attrs_define
class PremiumPhoneRevealBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        linkedin_url (str): LinkedIn profile identifier. Accepts a full URL, a bare slug, or a LinkedIn entity URN.
        patience (None | PremiumPhoneRevealBodyPatienceType1 | PremiumPhoneRevealBodyPatienceType2Type1 |
            PremiumPhoneRevealBodyPatienceType3Type1 | Unset): How long to wait for phone-number verification after a number
            is found. Higher patience increases average response time but improves identity and reachability accuracy.
            MINIMUM is the least thorough verification option.
    """

    api_key: str
    linkedin_url: str
    patience: (
        None
        | PremiumPhoneRevealBodyPatienceType1
        | PremiumPhoneRevealBodyPatienceType2Type1
        | PremiumPhoneRevealBodyPatienceType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        linkedin_url = self.linkedin_url

        patience: None | str | Unset
        if isinstance(self.patience, Unset):
            patience = UNSET
        elif isinstance(self.patience, PremiumPhoneRevealBodyPatienceType1):
            patience = self.patience.value
        elif isinstance(self.patience, PremiumPhoneRevealBodyPatienceType2Type1):
            patience = self.patience.value
        elif isinstance(self.patience, PremiumPhoneRevealBodyPatienceType3Type1):
            patience = self.patience.value
        else:
            patience = self.patience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "linkedinUrl": linkedin_url,
            }
        )
        if patience is not UNSET:
            field_dict["patience"] = patience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = d.pop("linkedinUrl")

        def _parse_patience(
            data: object,
        ) -> (
            None
            | PremiumPhoneRevealBodyPatienceType1
            | PremiumPhoneRevealBodyPatienceType2Type1
            | PremiumPhoneRevealBodyPatienceType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_1 = PremiumPhoneRevealBodyPatienceType1(data)

                return patience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_2_type_1 = PremiumPhoneRevealBodyPatienceType2Type1(data)

                return patience_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_3_type_1 = PremiumPhoneRevealBodyPatienceType3Type1(data)

                return patience_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PremiumPhoneRevealBodyPatienceType1
                | PremiumPhoneRevealBodyPatienceType2Type1
                | PremiumPhoneRevealBodyPatienceType3Type1
                | Unset,
                data,
            )

        patience = _parse_patience(d.pop("patience", UNSET))

        premium_phone_reveal_body = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            patience=patience,
        )

        premium_phone_reveal_body.additional_properties = d
        return premium_phone_reveal_body

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
