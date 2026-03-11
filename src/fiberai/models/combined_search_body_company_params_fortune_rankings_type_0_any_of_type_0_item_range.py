from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange")


@_attrs_define
class CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange:
    """
    Attributes:
        low (float):
        high (float):
        name (None | str | Unset):
    """

    low: float
    high: float
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low = self.low

        high = self.high

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "low": low,
                "high": high,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low = d.pop("low")

        high = d.pop("high")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range = cls(
            low=low,
            high=high,
            name=name,
        )

        combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range.additional_properties = d
        return combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range

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
