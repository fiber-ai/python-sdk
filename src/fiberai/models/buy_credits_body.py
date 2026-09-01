from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyCreditsBody")


@_attrs_define
class BuyCreditsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        credits_to_buy (int): Number of credits to purchase. One-time payment authorizations require at least 100
            credits. Saved-card purchases require at least 1,000 credits.
        subscription_id (None | str | Unset): The subscription to add credits to. Required when the organization has
            more than one subscription, or when charging a saved payment method. Must be omitted when paying with a one-time
            payment authorization; sending both is rejected.
        shared_payment_granted_token (None | str | Unset): A one-time payment authorization from your payment provider.
            When set, this purchase charges that authorization instead of a saved card. Each purchase needs a freshly minted
            authorization.
        idempotency_key (None | str | Unset): A unique key to safely retry a purchase. If a request fails or times out,
            resend with the same key to avoid being charged twice. When omitted, each call is a new purchase.
    """

    api_key: str
    credits_to_buy: int
    subscription_id: None | str | Unset = UNSET
    shared_payment_granted_token: None | str | Unset = UNSET
    idempotency_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        credits_to_buy = self.credits_to_buy

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        shared_payment_granted_token: None | str | Unset
        if isinstance(self.shared_payment_granted_token, Unset):
            shared_payment_granted_token = UNSET
        else:
            shared_payment_granted_token = self.shared_payment_granted_token

        idempotency_key: None | str | Unset
        if isinstance(self.idempotency_key, Unset):
            idempotency_key = UNSET
        else:
            idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "creditsToBuy": credits_to_buy,
            }
        )
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if shared_payment_granted_token is not UNSET:
            field_dict["sharedPaymentGrantedToken"] = shared_payment_granted_token
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        credits_to_buy = d.pop("creditsToBuy")

        def _parse_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_shared_payment_granted_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shared_payment_granted_token = _parse_shared_payment_granted_token(d.pop("sharedPaymentGrantedToken", UNSET))

        def _parse_idempotency_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idempotency_key = _parse_idempotency_key(d.pop("idempotencyKey", UNSET))

        buy_credits_body = cls(
            api_key=api_key,
            credits_to_buy=credits_to_buy,
            subscription_id=subscription_id,
            shared_payment_granted_token=shared_payment_granted_token,
            idempotency_key=idempotency_key,
        )

        buy_credits_body.additional_properties = d
        return buy_credits_body

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
