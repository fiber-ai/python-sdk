from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListCompanyRankingsBodyRankingsRankRange")


@_attrs_define
class ListCompanyRankingsBodyRankingsRankRange:
    """Inclusive rank range of companies to download. Note: the Fortune 500 edition actually holds the top 1000 companies,
    so you can request ranks past 500 (e.g. up to 1000).

        Attributes:
            low (int): First rank to include, where 1 is the top-ranked company.
            high (int): Last rank to include.
    """

    low: int
    high: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low = self.low

        high = self.high

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "low": low,
                "high": high,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low = d.pop("low")

        high = d.pop("high")

        list_company_rankings_body_rankings_rank_range = cls(
            low=low,
            high=high,
        )

        list_company_rankings_body_rankings_rank_range.additional_properties = d
        return list_company_rankings_body_rankings_rank_range

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
