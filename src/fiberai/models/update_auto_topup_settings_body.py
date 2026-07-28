from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAutoTopupSettingsBody")


@_attrs_define
class UpdateAutoTopupSettingsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        subscription_id (str): The subscription to configure auto top-up for. An organization can have multiple
            subscriptions, each with its own auto top-up settings.
        is_enabled (bool): Whether auto top-up is enabled
        credit_threshold (int | None | Unset): Credit balance threshold below which auto top-up triggers. Required when
            isEnabled is true.
        credits_to_buy (int | None | Unset): Number of credits to purchase when auto top-up triggers. Required when
            isEnabled is true.
        max_per_day (int | None | Unset): Maximum number of auto top-ups allowed in a rolling 24-hour window. Set to
            null to remove the daily limit.
        max_per_month (int | None | Unset): Maximum number of auto top-ups allowed per calendar month (UTC). When
            reached, auto top-up pauses until the next calendar month. Set to null to remove the monthly limit.
    """

    api_key: str
    subscription_id: str
    is_enabled: bool
    credit_threshold: int | None | Unset = UNSET
    credits_to_buy: int | None | Unset = UNSET
    max_per_day: int | None | Unset = UNSET
    max_per_month: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        subscription_id = self.subscription_id

        is_enabled = self.is_enabled

        credit_threshold: int | None | Unset
        if isinstance(self.credit_threshold, Unset):
            credit_threshold = UNSET
        else:
            credit_threshold = self.credit_threshold

        credits_to_buy: int | None | Unset
        if isinstance(self.credits_to_buy, Unset):
            credits_to_buy = UNSET
        else:
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
                "apiKey": api_key,
                "subscriptionId": subscription_id,
                "isEnabled": is_enabled,
            }
        )
        if credit_threshold is not UNSET:
            field_dict["creditThreshold"] = credit_threshold
        if credits_to_buy is not UNSET:
            field_dict["creditsToBuy"] = credits_to_buy
        if max_per_day is not UNSET:
            field_dict["maxPerDay"] = max_per_day
        if max_per_month is not UNSET:
            field_dict["maxPerMonth"] = max_per_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        subscription_id = d.pop("subscriptionId")

        is_enabled = d.pop("isEnabled")

        def _parse_credit_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credit_threshold = _parse_credit_threshold(d.pop("creditThreshold", UNSET))

        def _parse_credits_to_buy(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_to_buy = _parse_credits_to_buy(d.pop("creditsToBuy", UNSET))

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

        update_auto_topup_settings_body = cls(
            api_key=api_key,
            subscription_id=subscription_id,
            is_enabled=is_enabled,
            credit_threshold=credit_threshold,
            credits_to_buy=credits_to_buy,
            max_per_day=max_per_day,
            max_per_month=max_per_month,
        )

        update_auto_topup_settings_body.additional_properties = d
        return update_auto_topup_settings_body

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
