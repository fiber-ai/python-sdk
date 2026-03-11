from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemYearsOfExperienceType0")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemYearsOfExperienceType0:
    """
    Attributes:
        lower_bound (float | None | Unset):
        upper_bound (float | None | Unset):
    """

    lower_bound: float | None | Unset = UNSET
    upper_bound: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound: float | None | Unset
        if isinstance(self.lower_bound, Unset):
            lower_bound = UNSET
        else:
            lower_bound = self.lower_bound

        upper_bound: float | None | Unset
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

        def _parse_lower_bound(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lower_bound = _parse_lower_bound(d.pop("lowerBound", UNSET))

        def _parse_upper_bound(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        upper_bound = _parse_upper_bound(d.pop("upperBound", UNSET))

        sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_years_of_experience_type_0 = cls(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_years_of_experience_type_0.additional_properties = d
        return sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_years_of_experience_type_0

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
