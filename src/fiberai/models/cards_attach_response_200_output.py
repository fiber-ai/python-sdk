from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cards_attach_response_200_output_status import CardsAttachResponse200OutputStatus

if TYPE_CHECKING:
    from ..models.cards_attach_response_200_output_payment_method import CardsAttachResponse200OutputPaymentMethod


T = TypeVar("T", bound="CardsAttachResponse200Output")


@_attrs_define
class CardsAttachResponse200Output:
    """
    Attributes:
        status (CardsAttachResponse200OutputStatus):
        credits_granted (int): Additional free trial credits granted by this call. Zero when the organization was
            already at its trial credit ceiling (e.g. re-attaching after the ceiling was already reached).
        total_credits_unlocked (int): Free trial credit ceiling after this call — the maximum credits the organization
            can spend on the trial before it needs a paid top-up.
        payment_method (CardsAttachResponse200OutputPaymentMethod): Display-only metadata for the card that was verified
            in this call. This is not a saved payment method — future paid top-ups must submit a freshly-minted shared
            payment token.
    """

    status: CardsAttachResponse200OutputStatus
    credits_granted: int
    total_credits_unlocked: int
    payment_method: CardsAttachResponse200OutputPaymentMethod
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        credits_granted = self.credits_granted

        total_credits_unlocked = self.total_credits_unlocked

        payment_method = self.payment_method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "creditsGranted": credits_granted,
                "totalCreditsUnlocked": total_credits_unlocked,
                "paymentMethod": payment_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cards_attach_response_200_output_payment_method import (
            CardsAttachResponse200OutputPaymentMethod,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = CardsAttachResponse200OutputStatus(d.pop("status"))

        credits_granted = d.pop("creditsGranted")

        total_credits_unlocked = d.pop("totalCreditsUnlocked")

        payment_method = CardsAttachResponse200OutputPaymentMethod.from_dict(d.pop("paymentMethod"))

        cards_attach_response_200_output = cls(
            status=status,
            credits_granted=credits_granted,
            total_credits_unlocked=total_credits_unlocked,
            payment_method=payment_method,
        )

        cards_attach_response_200_output.additional_properties = d
        return cards_attach_response_200_output

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
