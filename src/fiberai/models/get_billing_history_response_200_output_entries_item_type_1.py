from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_billing_history_response_200_output_entries_item_type_1_credit_status import (
    GetBillingHistoryResponse200OutputEntriesItemType1CreditStatus,
)
from ..models.get_billing_history_response_200_output_entries_item_type_1_payment_status import (
    GetBillingHistoryResponse200OutputEntriesItemType1PaymentStatus,
)
from ..models.get_billing_history_response_200_output_entries_item_type_1_price_paid_cents import (
    GetBillingHistoryResponse200OutputEntriesItemType1PricePaidCents,
)
from ..models.get_billing_history_response_200_output_entries_item_type_1_purchase_type import (
    GetBillingHistoryResponse200OutputEntriesItemType1PurchaseType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBillingHistoryResponse200OutputEntriesItemType1")


@_attrs_define
class GetBillingHistoryResponse200OutputEntriesItemType1:
    """
    Attributes:
        success (bool): Whether the purchase succeeded. Failed purchases carry `failureReason` and the amount they
            attempted to charge instead of the payment IDs.
        purchased_at (str): When the purchase was recorded (ISO 8601, UTC).
        purchase_type (GetBillingHistoryResponse200OutputEntriesItemType1PurchaseType): What kind of purchase this was.
        credits_added (int): The credits this purchase granted. Usually 0 for a failed purchase — `creditStatus` tells
            you whether credits were still granted.
        attempted_price_cents (int): The amount this purchase attempted to charge, in US cents (USD). Nothing was
            charged.
        price_paid_cents (GetBillingHistoryResponse200OutputEntriesItemType1PricePaidCents): A failed purchase moves no
            money.
        payment_status (GetBillingHistoryResponse200OutputEntriesItemType1PaymentStatus): The charge failed; see
            `failureReason`.
        credit_status (GetBillingHistoryResponse200OutputEntriesItemType1CreditStatus): Whether credits from this failed
            purchase were granted.
        failure_reason (None | str | Unset): Why the payment failed, as a short machine-readable code (for example
            'card_declined', 'insufficient_funds', or 'all_methods_failed'). Null when no reason was recorded.
    """

    success: bool
    purchased_at: str
    purchase_type: GetBillingHistoryResponse200OutputEntriesItemType1PurchaseType
    credits_added: int
    attempted_price_cents: int
    price_paid_cents: GetBillingHistoryResponse200OutputEntriesItemType1PricePaidCents
    payment_status: GetBillingHistoryResponse200OutputEntriesItemType1PaymentStatus
    credit_status: GetBillingHistoryResponse200OutputEntriesItemType1CreditStatus
    failure_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        purchased_at = self.purchased_at

        purchase_type = self.purchase_type.value

        credits_added = self.credits_added

        attempted_price_cents = self.attempted_price_cents

        price_paid_cents = self.price_paid_cents.value

        payment_status = self.payment_status.value

        credit_status = self.credit_status.value

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "purchasedAt": purchased_at,
                "purchaseType": purchase_type,
                "creditsAdded": credits_added,
                "attemptedPriceCents": attempted_price_cents,
                "pricePaidCents": price_paid_cents,
                "paymentStatus": payment_status,
                "creditStatus": credit_status,
            }
        )
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        purchased_at = d.pop("purchasedAt")

        purchase_type = GetBillingHistoryResponse200OutputEntriesItemType1PurchaseType(d.pop("purchaseType"))

        credits_added = d.pop("creditsAdded")

        attempted_price_cents = d.pop("attemptedPriceCents")

        price_paid_cents = GetBillingHistoryResponse200OutputEntriesItemType1PricePaidCents(d.pop("pricePaidCents"))

        payment_status = GetBillingHistoryResponse200OutputEntriesItemType1PaymentStatus(d.pop("paymentStatus"))

        credit_status = GetBillingHistoryResponse200OutputEntriesItemType1CreditStatus(d.pop("creditStatus"))

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failureReason", UNSET))

        get_billing_history_response_200_output_entries_item_type_1 = cls(
            success=success,
            purchased_at=purchased_at,
            purchase_type=purchase_type,
            credits_added=credits_added,
            attempted_price_cents=attempted_price_cents,
            price_paid_cents=price_paid_cents,
            payment_status=payment_status,
            credit_status=credit_status,
            failure_reason=failure_reason,
        )

        get_billing_history_response_200_output_entries_item_type_1.additional_properties = d
        return get_billing_history_response_200_output_entries_item_type_1

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
