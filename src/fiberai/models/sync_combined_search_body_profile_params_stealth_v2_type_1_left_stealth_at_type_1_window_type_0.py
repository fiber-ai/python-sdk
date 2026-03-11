from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_profile_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0_method import (
    SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Method,
)
from ..models.sync_combined_search_body_profile_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0_period import (
    SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Period,
)

T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0:
    """
    Attributes:
        method (SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Method):
        period (SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Period):
        quantity (float):
    """

    method: SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Method
    period: SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Period
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        period = self.period.value

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "period": period,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Method(d.pop("method"))

        period = SyncCombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType0Period(d.pop("period"))

        quantity = d.pop("quantity")

        sync_combined_search_body_profile_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0 = cls(
            method=method,
            period=period,
            quantity=quantity,
        )

        sync_combined_search_body_profile_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0

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
