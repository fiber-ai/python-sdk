from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2_method import (
    LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Method,
)
from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2_period import (
    LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Period,
)
from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2_which import (
    LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Which,
)

T = TypeVar("T", bound="LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2")


@_attrs_define
class LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2:
    """
    Attributes:
        method (LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Method):
        which (LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Which):
        period (LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Period):
    """

    method: LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Method
    which: LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Which
    period: LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        which = self.which.value

        period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "which": which,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Method(
            d.pop("method")
        )

        which = LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Which(
            d.pop("which")
        )

        period = LookalikesTriggerBodyFiltersType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Period(
            d.pop("period")
        )

        lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2 = cls(
            method=method,
            which=which,
            period=period,
        )

        lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2.additional_properties = d
        return lookalikes_trigger_body_filters_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1_window_type_2

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
