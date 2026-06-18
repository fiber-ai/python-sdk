from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_in_function_job_functions_type_0_item import JobPostingInFunctionJobFunctionsType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobPostingInFunction")


@_attrs_define
class JobPostingInFunction:
    """
    Attributes:
        type_ (Literal['job_posting_in_function']):
        entity_type (Literal['company']):
        job_functions (list[JobPostingInFunctionJobFunctionsType0Item] | None): Alert when a job posting is in any of
            these departments/functions.
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        min_postings (int | None | Unset): Only alert if at least this many NEW matching postings are detected in a
            single check cycle. Omit for 1 (any new match).
    """

    type_: Literal["job_posting_in_function"]
    entity_type: Literal["company"]
    job_functions: list[JobPostingInFunctionJobFunctionsType0Item] | None
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    min_postings: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        job_functions: list[str] | None
        if isinstance(self.job_functions, list):
            job_functions = []
            for job_functions_type_0_item_data in self.job_functions:
                job_functions_type_0_item = job_functions_type_0_item_data.value
                job_functions.append(job_functions_type_0_item)

        else:
            job_functions = self.job_functions

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        min_postings: int | None | Unset
        if isinstance(self.min_postings, Unset):
            min_postings = UNSET
        else:
            min_postings = self.min_postings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "jobFunctions": job_functions,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if min_postings is not UNSET:
            field_dict["minPostings"] = min_postings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["job_posting_in_function"], d.pop("type"))
        if type_ != "job_posting_in_function":
            raise ValueError(f"type must match const 'job_posting_in_function', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_job_functions(data: object) -> list[JobPostingInFunctionJobFunctionsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_functions_type_0 = []
                _job_functions_type_0 = data
                for job_functions_type_0_item_data in _job_functions_type_0:
                    job_functions_type_0_item = JobPostingInFunctionJobFunctionsType0Item(
                        job_functions_type_0_item_data
                    )

                    job_functions_type_0.append(job_functions_type_0_item)

                return job_functions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingInFunctionJobFunctionsType0Item] | None, data)

        job_functions = _parse_job_functions(d.pop("jobFunctions"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_min_postings(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_postings = _parse_min_postings(d.pop("minPostings", UNSET))

        job_posting_in_function = cls(
            type_=type_,
            entity_type=entity_type,
            job_functions=job_functions,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            min_postings=min_postings,
        )

        job_posting_in_function.additional_properties = d
        return job_posting_in_function

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
