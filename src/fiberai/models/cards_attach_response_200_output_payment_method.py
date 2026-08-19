from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardsAttachResponse200OutputPaymentMethod")


@_attrs_define
class CardsAttachResponse200OutputPaymentMethod:
    """Display-only metadata for the card that was verified in this call. This is not a saved payment method — future paid
    top-ups must submit a freshly-minted shared payment token.

        Attributes:
            brand (None | str | Unset): Card network (e.g. 'visa', 'mastercard'). Null when unavailable.
            last4 (None | str | Unset): Last four digits of the card. Null when unavailable.
    """

    brand: None | str | Unset = UNSET
    last4: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand: None | str | Unset
        if isinstance(self.brand, Unset):
            brand = UNSET
        else:
            brand = self.brand

        last4: None | str | Unset
        if isinstance(self.last4, Unset):
            last4 = UNSET
        else:
            last4 = self.last4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand is not UNSET:
            field_dict["brand"] = brand
        if last4 is not UNSET:
            field_dict["last4"] = last4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_brand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand = _parse_brand(d.pop("brand", UNSET))

        def _parse_last4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last4 = _parse_last4(d.pop("last4", UNSET))

        cards_attach_response_200_output_payment_method = cls(
            brand=brand,
            last4=last4,
        )

        cards_attach_response_200_output_payment_method.additional_properties = d
        return cards_attach_response_200_output_payment_method

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
