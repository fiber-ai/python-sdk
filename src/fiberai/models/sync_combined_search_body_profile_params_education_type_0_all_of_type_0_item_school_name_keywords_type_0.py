from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsEducationType0AllOfType0ItemSchoolNameKeywordsType0")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsEducationType0AllOfType0ItemSchoolNameKeywordsType0:
    """
    Attributes:
        any_of (list[str] | None | Unset):
        none_of (list[str] | None | Unset):
    """

    any_of: list[str] | None | Unset = UNSET
    none_of: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_of: list[str] | None | Unset
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = self.any_of

        else:
            any_of = self.any_of

        none_of: list[str] | None | Unset
        if isinstance(self.none_of, Unset):
            none_of = UNSET
        elif isinstance(self.none_of, list):
            none_of = self.none_of

        else:
            none_of = self.none_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if none_of is not UNSET:
            field_dict["noneOf"] = none_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_any_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_of_type_0 = cast(list[str], data)

                return any_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        any_of = _parse_any_of(d.pop("anyOf", UNSET))

        def _parse_none_of(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                none_of_type_0 = cast(list[str], data)

                return none_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        none_of = _parse_none_of(d.pop("noneOf", UNSET))

        sync_combined_search_body_profile_params_education_type_0_all_of_type_0_item_school_name_keywords_type_0 = cls(
            any_of=any_of,
            none_of=none_of,
        )

        sync_combined_search_body_profile_params_education_type_0_all_of_type_0_item_school_name_keywords_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_education_type_0_all_of_type_0_item_school_name_keywords_type_0

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
