from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_closed_job_functions_type_0_item import JobPostingClosedJobFunctionsType0Item
from ..models.job_posting_closed_seniority_levels_type_0_item import JobPostingClosedSeniorityLevelsType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobPostingClosed")


@_attrs_define
class JobPostingClosed:
    """
    Attributes:
        type_ (Literal['job_posting_closed']):
        entity_type (Literal['company']):
        lookback_days (None | Unset): Not used by this rule: each closed job alerts once. Omit.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        keywords (list[str] | None | Unset): Only alert when the closed job's title contains any of these keywords. Omit
            for any title.
        job_functions (list[JobPostingClosedJobFunctionsType0Item] | None | Unset): Only alert when the closed job is in
            any of these departments, such as Engineering or Sales. Omit for any department.
        seniority_levels (list[JobPostingClosedSeniorityLevelsType0Item] | None | Unset): Only alert for these seniority
            levels. Omit for any level.
    """

    type_: Literal["job_posting_closed"]
    entity_type: Literal["company"]
    lookback_days: None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    job_functions: list[JobPostingClosedJobFunctionsType0Item] | None | Unset = UNSET
    seniority_levels: list[JobPostingClosedSeniorityLevelsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        job_functions: list[str] | None | Unset
        if isinstance(self.job_functions, Unset):
            job_functions = UNSET
        elif isinstance(self.job_functions, list):
            job_functions = []
            for job_functions_type_0_item_data in self.job_functions:
                job_functions_type_0_item = job_functions_type_0_item_data.value
                job_functions.append(job_functions_type_0_item)

        else:
            job_functions = self.job_functions

        seniority_levels: list[str] | None | Unset
        if isinstance(self.seniority_levels, Unset):
            seniority_levels = UNSET
        elif isinstance(self.seniority_levels, list):
            seniority_levels = []
            for seniority_levels_type_0_item_data in self.seniority_levels:
                seniority_levels_type_0_item = seniority_levels_type_0_item_data.value
                seniority_levels.append(seniority_levels_type_0_item)

        else:
            seniority_levels = self.seniority_levels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if job_functions is not UNSET:
            field_dict["jobFunctions"] = job_functions
        if seniority_levels is not UNSET:
            field_dict["seniorityLevels"] = seniority_levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["job_posting_closed"], d.pop("type"))
        if type_ != "job_posting_closed":
            raise ValueError(f"type must match const 'job_posting_closed', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_job_functions(data: object) -> list[JobPostingClosedJobFunctionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_functions_type_0 = []
                _job_functions_type_0 = data
                for job_functions_type_0_item_data in _job_functions_type_0:
                    job_functions_type_0_item = JobPostingClosedJobFunctionsType0Item(job_functions_type_0_item_data)

                    job_functions_type_0.append(job_functions_type_0_item)

                return job_functions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingClosedJobFunctionsType0Item] | None | Unset, data)

        job_functions = _parse_job_functions(d.pop("jobFunctions", UNSET))

        def _parse_seniority_levels(data: object) -> list[JobPostingClosedSeniorityLevelsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seniority_levels_type_0 = []
                _seniority_levels_type_0 = data
                for seniority_levels_type_0_item_data in _seniority_levels_type_0:
                    seniority_levels_type_0_item = JobPostingClosedSeniorityLevelsType0Item(
                        seniority_levels_type_0_item_data
                    )

                    seniority_levels_type_0.append(seniority_levels_type_0_item)

                return seniority_levels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingClosedSeniorityLevelsType0Item] | None | Unset, data)

        seniority_levels = _parse_seniority_levels(d.pop("seniorityLevels", UNSET))

        job_posting_closed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            keywords=keywords,
            job_functions=job_functions,
            seniority_levels=seniority_levels,
        )

        job_posting_closed.additional_properties = d
        return job_posting_closed

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
