from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0")


@_attrs_define
class TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0:
    """
    Attributes:
        lower_bound_exclusive (int | None | Unset):
        upper_bound_inclusive (int | None | Unset):
    """

    lower_bound_exclusive: int | None | Unset = UNSET
    upper_bound_inclusive: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound_exclusive: int | None | Unset
        if isinstance(self.lower_bound_exclusive, Unset):
            lower_bound_exclusive = UNSET
        else:
            lower_bound_exclusive = self.lower_bound_exclusive

        upper_bound_inclusive: int | None | Unset
        if isinstance(self.upper_bound_inclusive, Unset):
            upper_bound_inclusive = UNSET
        else:
            upper_bound_inclusive = self.upper_bound_inclusive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_bound_exclusive is not UNSET:
            field_dict["lowerBoundExclusive"] = lower_bound_exclusive
        if upper_bound_inclusive is not UNSET:
            field_dict["upperBoundInclusive"] = upper_bound_inclusive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lower_bound_exclusive(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lower_bound_exclusive = _parse_lower_bound_exclusive(d.pop("lowerBoundExclusive", UNSET))

        def _parse_upper_bound_inclusive(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        upper_bound_inclusive = _parse_upper_bound_inclusive(d.pop("upperBoundInclusive", UNSET))

        text_to_combined_search_param_response_200_output_company_search_params_type_0_employee_count_v2_type_0 = cls(
            lower_bound_exclusive=lower_bound_exclusive,
            upper_bound_inclusive=upper_bound_inclusive,
        )

        text_to_combined_search_param_response_200_output_company_search_params_type_0_employee_count_v2_type_0.additional_properties = d
        return text_to_combined_search_param_response_200_output_company_search_params_type_0_employee_count_v2_type_0

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
