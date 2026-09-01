from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_company_rankings_body_rankings import ListCompanyRankingsBodyRankings


T = TypeVar("T", bound="ListCompanyRankingsBody")


@_attrs_define
class ListCompanyRankingsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        rankings (ListCompanyRankingsBodyRankings):
    """

    api_key: str
    rankings: ListCompanyRankingsBodyRankings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        rankings = self.rankings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "rankings": rankings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_company_rankings_body_rankings import ListCompanyRankingsBodyRankings  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        rankings = ListCompanyRankingsBodyRankings.from_dict(d.pop("rankings"))

        list_company_rankings_body = cls(
            api_key=api_key,
            rankings=rankings,
        )

        list_company_rankings_body.additional_properties = d
        return list_company_rankings_body

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
