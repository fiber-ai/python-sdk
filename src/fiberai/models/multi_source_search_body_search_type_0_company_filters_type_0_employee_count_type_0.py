from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0")


@_attrs_define
class MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0:
    """Filter by number of employees (inclusive range).

    Attributes:
        min_ (int | None | Unset):
        max_ (int | None | Unset):
    """

    min_: int | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_: int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_min_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0 = cls(
            min_=min_,
            max_=max_,
        )

        multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0.additional_properties = d
        return multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0

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
