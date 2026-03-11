from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAudienceSearchParamsResponse200ChargeInfoType2LowCreditAlertType0")


@_attrs_define
class UpdateAudienceSearchParamsResponse200ChargeInfoType2LowCreditAlertType0:
    """Contains a link to get more credits, a warning message, and the remaining credit count.

    Attributes:
        get_more_credits_url (str): URL to top up credits or restart billing cycle to get fresh credits.
        message (str): Human-readable credits warning.
        available_credits (float): Number of credits remaining in the current billing period.
    """

    get_more_credits_url: str
    message: str
    available_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        get_more_credits_url = self.get_more_credits_url

        message = self.message

        available_credits = self.available_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "getMoreCreditsUrl": get_more_credits_url,
                "message": message,
                "availableCredits": available_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_more_credits_url = d.pop("getMoreCreditsUrl")

        message = d.pop("message")

        available_credits = d.pop("availableCredits")

        update_audience_search_params_response_200_charge_info_type_2_low_credit_alert_type_0 = cls(
            get_more_credits_url=get_more_credits_url,
            message=message,
            available_credits=available_credits,
        )

        update_audience_search_params_response_200_charge_info_type_2_low_credit_alert_type_0.additional_properties = d
        return update_audience_search_params_response_200_charge_info_type_2_low_credit_alert_type_0

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
