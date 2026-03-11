from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToProfileSearchResponse200OutputSearchParamsStartedAtCompanyType0RangeType0")


@_attrs_define
class TextToProfileSearchResponse200OutputSearchParamsStartedAtCompanyType0RangeType0:
    """
    Attributes:
        lower_bound (None | str | Unset):
        upper_bound (None | str | Unset):
    """

    lower_bound: None | str | Unset = UNSET
    upper_bound: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound: None | str | Unset
        if isinstance(self.lower_bound, Unset):
            lower_bound = UNSET
        else:
            lower_bound = self.lower_bound

        upper_bound: None | str | Unset
        if isinstance(self.upper_bound, Unset):
            upper_bound = UNSET
        else:
            upper_bound = self.upper_bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lower_bound(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lower_bound = _parse_lower_bound(d.pop("lowerBound", UNSET))

        def _parse_upper_bound(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upper_bound = _parse_upper_bound(d.pop("upperBound", UNSET))

        text_to_profile_search_response_200_output_search_params_started_at_company_type_0_range_type_0 = cls(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        text_to_profile_search_response_200_output_search_params_started_at_company_type_0_range_type_0.additional_properties = d
        return text_to_profile_search_response_200_output_search_params_started_at_company_type_0_range_type_0

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
