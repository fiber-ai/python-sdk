from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_company_rankings_body_rankings_list import ListCompanyRankingsBodyRankingsList
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_company_rankings_body_rankings_rank_range import ListCompanyRankingsBodyRankingsRankRange


T = TypeVar("T", bound="ListCompanyRankingsBodyRankings")


@_attrs_define
class ListCompanyRankingsBodyRankings:
    """
    Attributes:
        list_ (ListCompanyRankingsBodyRankingsList):
        rank_range (ListCompanyRankingsBodyRankingsRankRange): Inclusive rank range of companies to download. Note: the
            Fortune 500 edition actually holds the top 1000 companies, so you can request ranks past 500 (e.g. up to 1000).
        year (int | None | Unset): Edition year of the list. Omit to get the most recent year available.
    """

    list_: ListCompanyRankingsBodyRankingsList
    rank_range: ListCompanyRankingsBodyRankingsRankRange
    year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_ = self.list_.value

        rank_range = self.rank_range.to_dict()

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list": list_,
                "rankRange": rank_range,
            }
        )
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_company_rankings_body_rankings_rank_range import (
            ListCompanyRankingsBodyRankingsRankRange,  # noqa: PLC0415
        )

        d = dict(src_dict)
        list_ = ListCompanyRankingsBodyRankingsList(d.pop("list"))

        rank_range = ListCompanyRankingsBodyRankingsRankRange.from_dict(d.pop("rankRange"))

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        list_company_rankings_body_rankings = cls(
            list_=list_,
            rank_range=rank_range,
            year=year,
        )

        list_company_rankings_body_rankings.additional_properties = d
        return list_company_rankings_body_rankings

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
