from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_billing_history_response_200_output_entries_item_type_0_credit_status_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_credit_status_type_2_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_credit_status_type_3_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_payment_status_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_payment_status_type_2_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_payment_status_type_3_type_1 import (
    GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1,
)
from ..models.get_billing_history_response_200_output_entries_item_type_0_purchase_type import (
    GetBillingHistoryResponse200OutputEntriesItemType0PurchaseType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBillingHistoryResponse200OutputEntriesItemType0")


@_attrs_define
class GetBillingHistoryResponse200OutputEntriesItemType0:
    """
    Attributes:
        success (bool): Whether the purchase succeeded. Failed purchases carry `failureReason` and the amount they
            attempted to charge instead of the payment IDs.
        purchased_at (str): When the purchase was recorded (ISO 8601, UTC).
        purchase_type (GetBillingHistoryResponse200OutputEntriesItemType0PurchaseType): What kind of purchase this was.
        credits_added (int): The credits this purchase grants (for a subscription entry, the plan allotment for that
            cycle). Confirm it was granted via `creditStatus`.
        price_paid_cents (int | None | Unset): The amount actually paid, in US cents (USD). Null when the amount could
            not be retrieved for this entry — use the payment IDs to corroborate the exact charge.
        payment_status (GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1 |
            GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1 |
            GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1 | None | Unset): Whether the charge
            has settled ('PAID') or is still in flight ('NOT_STARTED'). Null for subscription cycles, where the charge is
            confirmed by the invoice instead.
        credit_status (GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1 |
            GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1 |
            GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1 | None | Unset): Whether the credits
            from this purchase were granted. Null for subscription cycles, which grant credits at period start.
        stripe_payment_intent_id (None | str | Unset): Payment intent ID for a one-off top-up (starts with 'pi_'). Null
            when the charge has not settled yet.
        stripe_invoice_id (None | str | Unset): Invoice ID for a subscription cycle (starts with 'in_').
        stripe_subscription_id (None | str | Unset): Subscription ID the cycle belongs to (starts with 'sub_').
    """

    success: bool
    purchased_at: str
    purchase_type: GetBillingHistoryResponse200OutputEntriesItemType0PurchaseType
    credits_added: int
    price_paid_cents: int | None | Unset = UNSET
    payment_status: (
        GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1
        | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1
        | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1
        | None
        | Unset
    ) = UNSET
    credit_status: (
        GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1
        | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1
        | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1
        | None
        | Unset
    ) = UNSET
    stripe_payment_intent_id: None | str | Unset = UNSET
    stripe_invoice_id: None | str | Unset = UNSET
    stripe_subscription_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        purchased_at = self.purchased_at

        purchase_type = self.purchase_type.value

        credits_added = self.credits_added

        price_paid_cents: int | None | Unset
        if isinstance(self.price_paid_cents, Unset):
            price_paid_cents = UNSET
        else:
            price_paid_cents = self.price_paid_cents

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        elif isinstance(self.payment_status, GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1):
            payment_status = self.payment_status.value
        elif isinstance(self.payment_status, GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1):
            payment_status = self.payment_status.value
        elif isinstance(self.payment_status, GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1):
            payment_status = self.payment_status.value
        else:
            payment_status = self.payment_status

        credit_status: None | str | Unset
        if isinstance(self.credit_status, Unset):
            credit_status = UNSET
        elif isinstance(self.credit_status, GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1):
            credit_status = self.credit_status.value
        elif isinstance(self.credit_status, GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1):
            credit_status = self.credit_status.value
        elif isinstance(self.credit_status, GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1):
            credit_status = self.credit_status.value
        else:
            credit_status = self.credit_status

        stripe_payment_intent_id: None | str | Unset
        if isinstance(self.stripe_payment_intent_id, Unset):
            stripe_payment_intent_id = UNSET
        else:
            stripe_payment_intent_id = self.stripe_payment_intent_id

        stripe_invoice_id: None | str | Unset
        if isinstance(self.stripe_invoice_id, Unset):
            stripe_invoice_id = UNSET
        else:
            stripe_invoice_id = self.stripe_invoice_id

        stripe_subscription_id: None | str | Unset
        if isinstance(self.stripe_subscription_id, Unset):
            stripe_subscription_id = UNSET
        else:
            stripe_subscription_id = self.stripe_subscription_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "purchasedAt": purchased_at,
                "purchaseType": purchase_type,
                "creditsAdded": credits_added,
            }
        )
        if price_paid_cents is not UNSET:
            field_dict["pricePaidCents"] = price_paid_cents
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if credit_status is not UNSET:
            field_dict["creditStatus"] = credit_status
        if stripe_payment_intent_id is not UNSET:
            field_dict["stripePaymentIntentId"] = stripe_payment_intent_id
        if stripe_invoice_id is not UNSET:
            field_dict["stripeInvoiceId"] = stripe_invoice_id
        if stripe_subscription_id is not UNSET:
            field_dict["stripeSubscriptionId"] = stripe_subscription_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        purchased_at = d.pop("purchasedAt")

        purchase_type = GetBillingHistoryResponse200OutputEntriesItemType0PurchaseType(d.pop("purchaseType"))

        credits_added = d.pop("creditsAdded")

        def _parse_price_paid_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_paid_cents = _parse_price_paid_cents(d.pop("pricePaidCents", UNSET))

        def _parse_payment_status(
            data: object,
        ) -> (
            GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1
            | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1
            | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1
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
                payment_status_type_1 = GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1(data)

                return payment_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_status_type_2_type_1 = (
                    GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1(data)
                )

                return payment_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_status_type_3_type_1 = (
                    GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1(data)
                )

                return payment_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType1
                | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1
                | GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType3Type1
                | None
                | Unset,
                data,
            )

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))

        def _parse_credit_status(
            data: object,
        ) -> (
            GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1
            | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1
            | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1
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
                credit_status_type_1 = GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1(data)

                return credit_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credit_status_type_2_type_1 = GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1(
                    data
                )

                return credit_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credit_status_type_3_type_1 = GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1(
                    data
                )

                return credit_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType1
                | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1
                | GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType3Type1
                | None
                | Unset,
                data,
            )

        credit_status = _parse_credit_status(d.pop("creditStatus", UNSET))

        def _parse_stripe_payment_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_payment_intent_id = _parse_stripe_payment_intent_id(d.pop("stripePaymentIntentId", UNSET))

        def _parse_stripe_invoice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_invoice_id = _parse_stripe_invoice_id(d.pop("stripeInvoiceId", UNSET))

        def _parse_stripe_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_subscription_id = _parse_stripe_subscription_id(d.pop("stripeSubscriptionId", UNSET))

        get_billing_history_response_200_output_entries_item_type_0 = cls(
            success=success,
            purchased_at=purchased_at,
            purchase_type=purchase_type,
            credits_added=credits_added,
            price_paid_cents=price_paid_cents,
            payment_status=payment_status,
            credit_status=credit_status,
            stripe_payment_intent_id=stripe_payment_intent_id,
            stripe_invoice_id=stripe_invoice_id,
            stripe_subscription_id=stripe_subscription_id,
        )

        get_billing_history_response_200_output_entries_item_type_0.additional_properties = d
        return get_billing_history_response_200_output_entries_item_type_0

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
