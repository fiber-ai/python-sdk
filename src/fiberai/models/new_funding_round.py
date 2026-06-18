from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_funding_round_round_types_type_0_item import NewFundingRoundRoundTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewFundingRound")


@_attrs_define
class NewFundingRound:
    """
    Attributes:
        type_ (Literal['new_funding_round']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        min_amount_usd (float | None | Unset): Only alert for rounds above this amount. Omit for any amount.
        round_types (list[NewFundingRoundRoundTypesType0Item] | None | Unset): Round types to alert on. Defaults to
            equity-focused types when omitted. Set explicitly to include debt/grant types.
    """

    type_: Literal["new_funding_round"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    min_amount_usd: float | None | Unset = UNSET
    round_types: list[NewFundingRoundRoundTypesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        min_amount_usd: float | None | Unset
        if isinstance(self.min_amount_usd, Unset):
            min_amount_usd = UNSET
        else:
            min_amount_usd = self.min_amount_usd

        round_types: list[str] | None | Unset
        if isinstance(self.round_types, Unset):
            round_types = UNSET
        elif isinstance(self.round_types, list):
            round_types = []
            for round_types_type_0_item_data in self.round_types:
                round_types_type_0_item = round_types_type_0_item_data.value
                round_types.append(round_types_type_0_item)

        else:
            round_types = self.round_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if min_amount_usd is not UNSET:
            field_dict["minAmountUsd"] = min_amount_usd
        if round_types is not UNSET:
            field_dict["roundTypes"] = round_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["new_funding_round"], d.pop("type"))
        if type_ != "new_funding_round":
            raise ValueError(f"type must match const 'new_funding_round', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_min_amount_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_amount_usd = _parse_min_amount_usd(d.pop("minAmountUsd", UNSET))

        def _parse_round_types(data: object) -> list[NewFundingRoundRoundTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                round_types_type_0 = []
                _round_types_type_0 = data
                for round_types_type_0_item_data in _round_types_type_0:
                    round_types_type_0_item = NewFundingRoundRoundTypesType0Item(round_types_type_0_item_data)

                    round_types_type_0.append(round_types_type_0_item)

                return round_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewFundingRoundRoundTypesType0Item] | None | Unset, data)

        round_types = _parse_round_types(d.pop("roundTypes", UNSET))

        new_funding_round = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            min_amount_usd=min_amount_usd,
            round_types=round_types,
        )

        new_funding_round.additional_properties = d
        return new_funding_round

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
