from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_change_location_type_type_1 import JobPostingChangeLocationTypeType1
from ..models.job_posting_change_location_type_type_2_type_1 import JobPostingChangeLocationTypeType2Type1
from ..models.job_posting_change_location_type_type_3_type_1 import JobPostingChangeLocationTypeType3Type1
from ..models.job_posting_change_status import JobPostingChangeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobPostingChange")


@_attrs_define
class JobPostingChange:
    """
    Attributes:
        job_id (str): LinkedIn job ID
        title (str): Job title
        status (JobPostingChangeStatus): Job posting status
        job_url (None | str | Unset): URL to the job posting
        location (None | str | Unset): Job location
        location_type (JobPostingChangeLocationTypeType1 | JobPostingChangeLocationTypeType2Type1 |
            JobPostingChangeLocationTypeType3Type1 | None | Unset): Location type
        seniority_level (None | str | Unset): Seniority level
        job_function (None | str | Unset): Department or function
        job_functions (list[str] | None | Unset): All job functions this posting belongs to
        posted_at (None | str | Unset): ISO date when posted
    """

    job_id: str
    title: str
    status: JobPostingChangeStatus
    job_url: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    location_type: (
        JobPostingChangeLocationTypeType1
        | JobPostingChangeLocationTypeType2Type1
        | JobPostingChangeLocationTypeType3Type1
        | None
        | Unset
    ) = UNSET
    seniority_level: None | str | Unset = UNSET
    job_function: None | str | Unset = UNSET
    job_functions: list[str] | None | Unset = UNSET
    posted_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        title = self.title

        status = self.status.value

        job_url: None | str | Unset
        if isinstance(self.job_url, Unset):
            job_url = UNSET
        else:
            job_url = self.job_url

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_type: None | str | Unset
        if isinstance(self.location_type, Unset):
            location_type = UNSET
        elif isinstance(self.location_type, JobPostingChangeLocationTypeType1):
            location_type = self.location_type.value
        elif isinstance(self.location_type, JobPostingChangeLocationTypeType2Type1):
            location_type = self.location_type.value
        elif isinstance(self.location_type, JobPostingChangeLocationTypeType3Type1):
            location_type = self.location_type.value
        else:
            location_type = self.location_type

        seniority_level: None | str | Unset
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        else:
            seniority_level = self.seniority_level

        job_function: None | str | Unset
        if isinstance(self.job_function, Unset):
            job_function = UNSET
        else:
            job_function = self.job_function

        job_functions: list[str] | None | Unset
        if isinstance(self.job_functions, Unset):
            job_functions = UNSET
        elif isinstance(self.job_functions, list):
            job_functions = self.job_functions

        else:
            job_functions = self.job_functions

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = self.posted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
                "title": title,
                "status": status,
            }
        )
        if job_url is not UNSET:
            field_dict["jobUrl"] = job_url
        if location is not UNSET:
            field_dict["location"] = location
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if seniority_level is not UNSET:
            field_dict["seniorityLevel"] = seniority_level
        if job_function is not UNSET:
            field_dict["jobFunction"] = job_function
        if job_functions is not UNSET:
            field_dict["jobFunctions"] = job_functions
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        title = d.pop("title")

        status = JobPostingChangeStatus(d.pop("status"))

        def _parse_job_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_url = _parse_job_url(d.pop("jobUrl", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_location_type(
            data: object,
        ) -> (
            JobPostingChangeLocationTypeType1
            | JobPostingChangeLocationTypeType2Type1
            | JobPostingChangeLocationTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_type_type_1 = JobPostingChangeLocationTypeType1(data)

                return location_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_type_type_2_type_1 = JobPostingChangeLocationTypeType2Type1(data)

                return location_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_type_type_3_type_1 = JobPostingChangeLocationTypeType3Type1(data)

                return location_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JobPostingChangeLocationTypeType1
                | JobPostingChangeLocationTypeType2Type1
                | JobPostingChangeLocationTypeType3Type1
                | None
                | Unset,
                data,
            )

        location_type = _parse_location_type(d.pop("locationType", UNSET))

        def _parse_seniority_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority_level = _parse_seniority_level(d.pop("seniorityLevel", UNSET))

        def _parse_job_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_function = _parse_job_function(d.pop("jobFunction", UNSET))

        def _parse_job_functions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_functions_type_0 = cast(list[str], data)

                return job_functions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_functions = _parse_job_functions(d.pop("jobFunctions", UNSET))

        def _parse_posted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

        job_posting_change = cls(
            job_id=job_id,
            title=title,
            status=status,
            job_url=job_url,
            location=location,
            location_type=location_type,
            seniority_level=seniority_level,
            job_function=job_function,
            job_functions=job_functions,
            posted_at=posted_at,
        )

        job_posting_change.additional_properties = d
        return job_posting_change

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
