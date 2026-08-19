from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CardsAttachBody")


@_attrs_define
class CardsAttachBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        shared_payment_granted_token (str): Single-use Stripe shared payment token (`spt_...`) authorizing exactly one
            card handoff. Mint it on the buyer side (see https://docs.stripe.com/agentic-commerce/concepts/shared-payment-
            tokens); each request must submit a freshly-minted token.
    """

    api_key: str
    shared_payment_granted_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        shared_payment_granted_token = self.shared_payment_granted_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "sharedPaymentGrantedToken": shared_payment_granted_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        shared_payment_granted_token = d.pop("sharedPaymentGrantedToken")

        cards_attach_body = cls(
            api_key=api_key,
            shared_payment_granted_token=shared_payment_granted_token,
        )

        cards_attach_body.additional_properties = d
        return cards_attach_body

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
