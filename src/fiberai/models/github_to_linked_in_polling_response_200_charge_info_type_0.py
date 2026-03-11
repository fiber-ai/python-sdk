from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linked_in_polling_response_200_charge_info_type_0_method import (
    GithubToLinkedInPollingResponse200ChargeInfoType0Method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_to_linked_in_polling_response_200_charge_info_type_0_low_credit_alert_type_0 import (
        GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0,
    )


T = TypeVar("T", bound="GithubToLinkedInPollingResponse200ChargeInfoType0")


@_attrs_define
class GithubToLinkedInPollingResponse200ChargeInfoType0:
    """Credits were charged immediately for this operation

    Attributes:
        method (GithubToLinkedInPollingResponse200ChargeInfoType0Method):
        credits_charged (float):
        low_credit_alert (GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0 | None | Unset): Contains
            a link to get more credits, a warning message, and the remaining credit count.
    """

    method: GithubToLinkedInPollingResponse200ChargeInfoType0Method
    credits_charged: float
    low_credit_alert: GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_to_linked_in_polling_response_200_charge_info_type_0_low_credit_alert_type_0 import (
            GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0,
        )

        method = self.method.value

        credits_charged = self.credits_charged

        low_credit_alert: dict[str, Any] | None | Unset
        if isinstance(self.low_credit_alert, Unset):
            low_credit_alert = UNSET
        elif isinstance(self.low_credit_alert, GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0):
            low_credit_alert = self.low_credit_alert.to_dict()
        else:
            low_credit_alert = self.low_credit_alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "creditsCharged": credits_charged,
            }
        )
        if low_credit_alert is not UNSET:
            field_dict["lowCreditAlert"] = low_credit_alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linked_in_polling_response_200_charge_info_type_0_low_credit_alert_type_0 import (
            GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0,
        )

        d = dict(src_dict)
        method = GithubToLinkedInPollingResponse200ChargeInfoType0Method(d.pop("method"))

        credits_charged = d.pop("creditsCharged")

        def _parse_low_credit_alert(
            data: object,
        ) -> GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                low_credit_alert_type_0 = (
                    GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0.from_dict(data)
                )

                return low_credit_alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GithubToLinkedInPollingResponse200ChargeInfoType0LowCreditAlertType0 | None | Unset, data)

        low_credit_alert = _parse_low_credit_alert(d.pop("lowCreditAlert", UNSET))

        github_to_linked_in_polling_response_200_charge_info_type_0 = cls(
            method=method,
            credits_charged=credits_charged,
            low_credit_alert=low_credit_alert,
        )

        github_to_linked_in_polling_response_200_charge_info_type_0.additional_properties = d
        return github_to_linked_in_polling_response_200_charge_info_type_0

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
