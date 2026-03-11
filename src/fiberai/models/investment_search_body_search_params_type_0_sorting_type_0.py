from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investment_search_body_search_params_type_0_sorting_type_0_direction import (
    InvestmentSearchBodySearchParamsType0SortingType0Direction,
)
from ..models.investment_search_body_search_params_type_0_sorting_type_0_field import (
    InvestmentSearchBodySearchParamsType0SortingType0Field,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestmentSearchBodySearchParamsType0SortingType0")


@_attrs_define
class InvestmentSearchBodySearchParamsType0SortingType0:
    """Sorting configuration. If provided, field is required. Defaults to round_date DESC if not provided.

    Attributes:
        field (InvestmentSearchBodySearchParamsType0SortingType0Field): Field to sort by. Options: 'round_date'
            (default), 'raised_amount_usd', 'company_name', 'investor_name'
        direction (InvestmentSearchBodySearchParamsType0SortingType0Direction | Unset): Sort order - asc or desc
            (defaults to desc) Default: InvestmentSearchBodySearchParamsType0SortingType0Direction.DESC.
    """

    field: InvestmentSearchBodySearchParamsType0SortingType0Field
    direction: InvestmentSearchBodySearchParamsType0SortingType0Direction | Unset = (
        InvestmentSearchBodySearchParamsType0SortingType0Direction.DESC
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = InvestmentSearchBodySearchParamsType0SortingType0Field(d.pop("field"))

        _direction = d.pop("direction", UNSET)
        direction: InvestmentSearchBodySearchParamsType0SortingType0Direction | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = InvestmentSearchBodySearchParamsType0SortingType0Direction(_direction)

        investment_search_body_search_params_type_0_sorting_type_0 = cls(
            field=field,
            direction=direction,
        )

        investment_search_body_search_params_type_0_sorting_type_0.additional_properties = d
        return investment_search_body_search_params_type_0_sorting_type_0

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
