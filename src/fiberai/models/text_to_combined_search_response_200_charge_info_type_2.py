from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_charge_info_type_2_method import (
    TextToCombinedSearchResponse200ChargeInfoType2Method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_charge_info_type_2_low_credit_alert_type_0 import (
        TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200ChargeInfoType2")


@_attrs_define
class TextToCombinedSearchResponse200ChargeInfoType2:
    """Credits that were charged for an asynchronous operation

    Attributes:
        method (TextToCombinedSearchResponse200ChargeInfoType2Method):
        credits_charged (float):
        message (str):
        low_credit_alert (None | TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0 | Unset): Contains a
            link to get more credits, a warning message, and the remaining credit count.
    """

    method: TextToCombinedSearchResponse200ChargeInfoType2Method
    credits_charged: float
    message: str
    low_credit_alert: None | TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_charge_info_type_2_low_credit_alert_type_0 import (
            TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0,
        )

        method = self.method.value

        credits_charged = self.credits_charged

        message = self.message

        low_credit_alert: dict[str, Any] | None | Unset
        if isinstance(self.low_credit_alert, Unset):
            low_credit_alert = UNSET
        elif isinstance(self.low_credit_alert, TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0):
            low_credit_alert = self.low_credit_alert.to_dict()
        else:
            low_credit_alert = self.low_credit_alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "creditsCharged": credits_charged,
                "message": message,
            }
        )
        if low_credit_alert is not UNSET:
            field_dict["lowCreditAlert"] = low_credit_alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_charge_info_type_2_low_credit_alert_type_0 import (
            TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0,
        )

        d = dict(src_dict)
        method = TextToCombinedSearchResponse200ChargeInfoType2Method(d.pop("method"))

        credits_charged = d.pop("creditsCharged")

        message = d.pop("message")

        def _parse_low_credit_alert(
            data: object,
        ) -> None | TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                low_credit_alert_type_0 = TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0.from_dict(
                    data
                )

                return low_credit_alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200ChargeInfoType2LowCreditAlertType0 | Unset, data)

        low_credit_alert = _parse_low_credit_alert(d.pop("lowCreditAlert", UNSET))

        text_to_combined_search_response_200_charge_info_type_2 = cls(
            method=method,
            credits_charged=credits_charged,
            message=message,
            low_credit_alert=low_credit_alert,
        )

        text_to_combined_search_response_200_charge_info_type_2.additional_properties = d
        return text_to_combined_search_response_200_charge_info_type_2

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
