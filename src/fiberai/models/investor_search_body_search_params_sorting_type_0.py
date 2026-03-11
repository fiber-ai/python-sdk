from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investor_search_body_search_params_sorting_type_0_direction import (
    InvestorSearchBodySearchParamsSortingType0Direction,
)
from ..models.investor_search_body_search_params_sorting_type_0_field import (
    InvestorSearchBodySearchParamsSortingType0Field,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestorSearchBodySearchParamsSortingType0")


@_attrs_define
class InvestorSearchBodySearchParamsSortingType0:
    """Sorting configuration. If provided, field is required. Defaults to total_investment_count DESC if not provided.

    Attributes:
        field (InvestorSearchBodySearchParamsSortingType0Field): Field to sort by. For 'importance', higher values
            indicate a more important investor (as determined by our AI). Use DESC direction to start with the most
            important investors.
        direction (InvestorSearchBodySearchParamsSortingType0Direction | Unset): Sort order - asc or desc (defaults to
            desc) Default: InvestorSearchBodySearchParamsSortingType0Direction.DESC.
    """

    field: InvestorSearchBodySearchParamsSortingType0Field
    direction: InvestorSearchBodySearchParamsSortingType0Direction | Unset = (
        InvestorSearchBodySearchParamsSortingType0Direction.DESC
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
        field = InvestorSearchBodySearchParamsSortingType0Field(d.pop("field"))

        _direction = d.pop("direction", UNSET)
        direction: InvestorSearchBodySearchParamsSortingType0Direction | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = InvestorSearchBodySearchParamsSortingType0Direction(_direction)

        investor_search_body_search_params_sorting_type_0 = cls(
            field=field,
            direction=direction,
        )

        investor_search_body_search_params_sorting_type_0.additional_properties = d
        return investor_search_body_search_params_sorting_type_0

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
