from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAutoTopupSettingsResponse200OutputType0")


@_attrs_define
class UpdateAutoTopupSettingsResponse200OutputType0:
    """
    Attributes:
        configured (bool):
        is_enabled (bool): Whether auto top-up is currently enabled for this organization
        credit_threshold (int): Credit balance threshold below which auto top-up triggers
        credits_to_buy (int): Number of credits purchased when auto top-up triggers
    """

    configured: bool
    is_enabled: bool
    credit_threshold: int
    credits_to_buy: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        is_enabled = self.is_enabled

        credit_threshold = self.credit_threshold

        credits_to_buy = self.credits_to_buy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configured": configured,
                "isEnabled": is_enabled,
                "creditThreshold": credit_threshold,
                "creditsToBuy": credits_to_buy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured")

        is_enabled = d.pop("isEnabled")

        credit_threshold = d.pop("creditThreshold")

        credits_to_buy = d.pop("creditsToBuy")

        update_auto_topup_settings_response_200_output_type_0 = cls(
            configured=configured,
            is_enabled=is_enabled,
            credit_threshold=credit_threshold,
            credits_to_buy=credits_to_buy,
        )

        update_auto_topup_settings_response_200_output_type_0.additional_properties = d
        return update_auto_topup_settings_response_200_output_type_0

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
