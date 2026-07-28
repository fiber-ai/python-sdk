from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAutoTopupSettingsResponse200OutputSettingsItemType0")


@_attrs_define
class GetAutoTopupSettingsResponse200OutputSettingsItemType0:
    """
    Attributes:
        configured (bool):
        subscription_id (str): The subscription these auto top-up settings belong to
        is_enabled (bool): Whether auto top-up is currently enabled for this organization
        credit_threshold (int): Credit balance threshold below which auto top-up triggers
        credits_to_buy (int): Number of credits purchased when auto top-up triggers
        max_per_day (int | None | Unset): Maximum number of auto top-ups allowed in a rolling 24-hour window. When
            reached, auto top-up pauses until the window passes. Leave as null to not enforce daily limit.
        max_per_month (int | None | Unset): Maximum number of auto top-ups allowed per calendar month (UTC). When
            reached, auto top-up pauses until the next calendar month. Leave as null to not enforce monthly limit.
    """

    configured: bool
    subscription_id: str
    is_enabled: bool
    credit_threshold: int
    credits_to_buy: int
    max_per_day: int | None | Unset = UNSET
    max_per_month: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        subscription_id = self.subscription_id

        is_enabled = self.is_enabled

        credit_threshold = self.credit_threshold

        credits_to_buy = self.credits_to_buy

        max_per_day: int | None | Unset
        if isinstance(self.max_per_day, Unset):
            max_per_day = UNSET
        else:
            max_per_day = self.max_per_day

        max_per_month: int | None | Unset
        if isinstance(self.max_per_month, Unset):
            max_per_month = UNSET
        else:
            max_per_month = self.max_per_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configured": configured,
                "subscriptionId": subscription_id,
                "isEnabled": is_enabled,
                "creditThreshold": credit_threshold,
                "creditsToBuy": credits_to_buy,
            }
        )
        if max_per_day is not UNSET:
            field_dict["maxPerDay"] = max_per_day
        if max_per_month is not UNSET:
            field_dict["maxPerMonth"] = max_per_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured")

        subscription_id = d.pop("subscriptionId")

        is_enabled = d.pop("isEnabled")

        credit_threshold = d.pop("creditThreshold")

        credits_to_buy = d.pop("creditsToBuy")

        def _parse_max_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_per_day = _parse_max_per_day(d.pop("maxPerDay", UNSET))

        def _parse_max_per_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_per_month = _parse_max_per_month(d.pop("maxPerMonth", UNSET))

        get_auto_topup_settings_response_200_output_settings_item_type_0 = cls(
            configured=configured,
            subscription_id=subscription_id,
            is_enabled=is_enabled,
            credit_threshold=credit_threshold,
            credits_to_buy=credits_to_buy,
            max_per_day=max_per_day,
            max_per_month=max_per_month,
        )

        get_auto_topup_settings_response_200_output_settings_item_type_0.additional_properties = d
        return get_auto_topup_settings_response_200_output_settings_item_type_0

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
