from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FundingRoundChange")


@_attrs_define
class FundingRoundChange:
    """
    Attributes:
        type_ (str): Funding round type
        investors (list[str]): Investor names
        amount_usd (float | None | Unset): Amount raised in USD
        date (None | str | Unset): ISO date of the round
        crunchbase_url (None | str | Unset): URL to the funding round page on Crunchbase, when available
    """

    type_: str
    investors: list[str]
    amount_usd: float | None | Unset = UNSET
    date: None | str | Unset = UNSET
    crunchbase_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        investors = self.investors

        amount_usd: float | None | Unset
        if isinstance(self.amount_usd, Unset):
            amount_usd = UNSET
        else:
            amount_usd = self.amount_usd

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        crunchbase_url: None | str | Unset
        if isinstance(self.crunchbase_url, Unset):
            crunchbase_url = UNSET
        else:
            crunchbase_url = self.crunchbase_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "investors": investors,
            }
        )
        if amount_usd is not UNSET:
            field_dict["amountUsd"] = amount_usd
        if date is not UNSET:
            field_dict["date"] = date
        if crunchbase_url is not UNSET:
            field_dict["crunchbaseUrl"] = crunchbase_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        investors = cast(list[str], d.pop("investors"))

        def _parse_amount_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_usd = _parse_amount_usd(d.pop("amountUsd", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_crunchbase_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crunchbase_url = _parse_crunchbase_url(d.pop("crunchbaseUrl", UNSET))

        funding_round_change = cls(
            type_=type_,
            investors=investors,
            amount_usd=amount_usd,
            date=date,
            crunchbase_url=crunchbase_url,
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
