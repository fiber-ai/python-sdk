from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsKeywordsType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsKeywordsType0:
    """
    Attributes:
        contains_all (list[str] | None | Unset):
        contains_any (list[str] | None | Unset):
        contains_none (list[str] | None | Unset):
    """

    contains_all: list[str] | None | Unset = UNSET
    contains_any: list[str] | None | Unset = UNSET
    contains_none: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contains_all: list[str] | None | Unset
        if isinstance(self.contains_all, Unset):
            contains_all = UNSET
        elif isinstance(self.contains_all, list):
            contains_all = self.contains_all

        else:
            contains_all = self.contains_all

        contains_any: list[str] | None | Unset
        if isinstance(self.contains_any, Unset):
            contains_any = UNSET
        elif isinstance(self.contains_any, list):
            contains_any = self.contains_any

        else:
            contains_any = self.contains_any

        contains_none: list[str] | None | Unset
        if isinstance(self.contains_none, Unset):
            contains_none = UNSET
        elif isinstance(self.contains_none, list):
            contains_none = self.contains_none

        else:
            contains_none = self.contains_none

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contains_all is not UNSET:
            field_dict["containsAll"] = contains_all
        if contains_any is not UNSET:
            field_dict["containsAny"] = contains_any
        if contains_none is not UNSET:
            field_dict["containsNone"] = contains_none

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_contains_all(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contains_all_type_0 = cast(list[str], data)

                return contains_all_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        contains_all = _parse_contains_all(d.pop("containsAll", UNSET))

        def _parse_contains_any(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contains_any_type_0 = cast(list[str], data)

                return contains_any_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        contains_any = _parse_contains_any(d.pop("containsAny", UNSET))

        def _parse_contains_none(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contains_none_type_0 = cast(list[str], data)

                return contains_none_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        contains_none = _parse_contains_none(d.pop("containsNone", UNSET))

        people_search_count_body_search_params_keywords_type_0 = cls(
            contains_all=contains_all,
            contains_any=contains_any,
            contains_none=contains_none,
        )

        people_search_count_body_search_params_keywords_type_0.additional_properties = d
        return people_search_count_body_search_params_keywords_type_0

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
