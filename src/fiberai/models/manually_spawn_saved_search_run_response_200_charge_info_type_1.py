from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.manually_spawn_saved_search_run_response_200_charge_info_type_1_method import (
    ManuallySpawnSavedSearchRunResponse200ChargeInfoType1Method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manually_spawn_saved_search_run_response_200_charge_info_type_1_low_credit_alert_type_0 import (
        ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0,
    )


T = TypeVar("T", bound="ManuallySpawnSavedSearchRunResponse200ChargeInfoType1")


@_attrs_define
class ManuallySpawnSavedSearchRunResponse200ChargeInfoType1:
    """Credits will be charged after the operation completes

    Attributes:
        method (ManuallySpawnSavedSearchRunResponse200ChargeInfoType1Method):
        message (str):
        low_credit_alert (ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0 | None | Unset):
            Contains a link to get more credits, a warning message, and the remaining credit count.
    """

    method: ManuallySpawnSavedSearchRunResponse200ChargeInfoType1Method
    message: str
    low_credit_alert: ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.manually_spawn_saved_search_run_response_200_charge_info_type_1_low_credit_alert_type_0 import (
            ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0,
        )

        method = self.method.value

        message = self.message

        low_credit_alert: dict[str, Any] | None | Unset
        if isinstance(self.low_credit_alert, Unset):
            low_credit_alert = UNSET
        elif isinstance(
            self.low_credit_alert, ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0
        ):
            low_credit_alert = self.low_credit_alert.to_dict()
        else:
            low_credit_alert = self.low_credit_alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "message": message,
            }
        )
        if low_credit_alert is not UNSET:
            field_dict["lowCreditAlert"] = low_credit_alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.manually_spawn_saved_search_run_response_200_charge_info_type_1_low_credit_alert_type_0 import (
            ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0,
        )

        d = dict(src_dict)
        method = ManuallySpawnSavedSearchRunResponse200ChargeInfoType1Method(d.pop("method"))

        message = d.pop("message")

        def _parse_low_credit_alert(
            data: object,
        ) -> ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                low_credit_alert_type_0 = (
                    ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0.from_dict(data)
                )

                return low_credit_alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ManuallySpawnSavedSearchRunResponse200ChargeInfoType1LowCreditAlertType0 | None | Unset, data)

        low_credit_alert = _parse_low_credit_alert(d.pop("lowCreditAlert", UNSET))

        manually_spawn_saved_search_run_response_200_charge_info_type_1 = cls(
            method=method,
            message=message,
            low_credit_alert=low_credit_alert,
        )

        manually_spawn_saved_search_run_response_200_charge_info_type_1.additional_properties = d
        return manually_spawn_saved_search_run_response_200_charge_info_type_1

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
