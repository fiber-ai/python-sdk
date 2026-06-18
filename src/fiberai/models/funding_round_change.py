from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FundingRoundChange")


@_attrs_define
class FundingRoundChange:
    """
    Attributes:
        type_ (str): Funding round type
        amount_usd (float | None): Amount raised in USD
        date (None | str): ISO date of the round
        investors (list[str]): Investor names
    """

    type_: str
    amount_usd: float | None
    date: None | str
    investors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        amount_usd: float | None
        amount_usd = self.amount_usd

        date: None | str
        date = self.date

        investors = self.investors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "amountUsd": amount_usd,
                "date": date,
                "investors": investors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_amount_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        amount_usd = _parse_amount_usd(d.pop("amountUsd"))

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        investors = cast(list[str], d.pop("investors"))

        funding_round_change = cls(
            type_=type_,
            amount_usd=amount_usd,
            date=date,
            investors=investors,
        )

        funding_round_change.additional_properties = d
        return funding_round_change

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
