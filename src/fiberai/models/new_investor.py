from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewInvestor")


@_attrs_define
class NewInvestor:
    """
    Attributes:
        type_ (Literal['new_investor']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        investor_types (list[str] | None | Unset): Only alert for these investor types (e.g. 'venture_capital'). Omit
            for any new investor.
    """

    type_: Literal["new_investor"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    investor_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        investor_types: list[str] | None | Unset
        if isinstance(self.investor_types, Unset):
            investor_types = UNSET
        elif isinstance(self.investor_types, list):
            investor_types = self.investor_types

        else:
            investor_types = self.investor_types

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
        if investor_types is not UNSET:
            field_dict["investorTypes"] = investor_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["new_investor"], d.pop("type"))
        if type_ != "new_investor":
            raise ValueError(f"type must match const 'new_investor', got '{type_}'")

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

        def _parse_investor_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_types_type_0 = cast(list[str], data)

                return investor_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        investor_types = _parse_investor_types(d.pop("investorTypes", UNSET))

        new_investor = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            investor_types=investor_types,
        )

        new_investor.additional_properties = d
        return new_investor

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
