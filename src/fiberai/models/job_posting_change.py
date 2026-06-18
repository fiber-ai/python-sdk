from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_change_location_type_type_1 import JobPostingChangeLocationTypeType1
from ..models.job_posting_change_location_type_type_2_type_1 import JobPostingChangeLocationTypeType2Type1
from ..models.job_posting_change_location_type_type_3_type_1 import JobPostingChangeLocationTypeType3Type1
from ..models.job_posting_change_status import JobPostingChangeStatus

T = TypeVar("T", bound="JobPostingChange")


@_attrs_define
class JobPostingChange:
    """
    Attributes:
        job_id (str): LinkedIn job ID
        title (str): Job title
        job_url (None | str): URL to the job posting
        location (None | str): Job location
        location_type (JobPostingChangeLocationTypeType1 | JobPostingChangeLocationTypeType2Type1 |
            JobPostingChangeLocationTypeType3Type1 | None): Location type
        seniority_level (None | str): Seniority level
        job_function (None | str): Department or function
        posted_at (None | str): ISO date when posted
        status (JobPostingChangeStatus): Job posting status
    """

    job_id: str
    title: str
    job_url: None | str
    location: None | str
    location_type: (
        JobPostingChangeLocationTypeType1
        | JobPostingChangeLocationTypeType2Type1
        | JobPostingChangeLocationTypeType3Type1
        | None
    )
    seniority_level: None | str
    job_function: None | str
    posted_at: None | str
    status: JobPostingChangeStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        title = self.title

        job_url: None | str
        job_url = self.job_url

        location: None | str
        location = self.location

        location_type: None | str
        if isinstance(self.location_type, JobPostingChangeLocationTypeType1):
            location_type = self.location_type.value
        elif isinstance(self.location_type, JobPostingChangeLocationTypeType2Type1):
            location_type = self.location_type.value
        elif isinstance(self.location_type, JobPostingChangeLocationTypeType3Type1):
            location_type = self.location_type.value
        else:
            location_type = self.location_type

        seniority_level: None | str
        seniority_level = self.seniority_level

        job_function: None | str
        job_function = self.job_function

        posted_at: None | str
        posted_at = self.posted_at

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
                "title": title,
                "jobUrl": job_url,
                "location": location,
                "locationType": location_type,
                "seniorityLevel": seniority_level,
                "jobFunction": job_function,
                "postedAt": posted_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        title = d.pop("title")

        def _parse_job_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_url = _parse_job_url(d.pop("jobUrl"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_location_type(
            data: object,
        ) -> (
            JobPostingChangeLocationTypeType1
            | JobPostingChangeLocationTypeType2Type1
            | JobPostingChangeLocationTypeType3Type1
            | None
        ):
            if data is None:
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
                | None,
                data,
            )

        location_type = _parse_location_type(d.pop("locationType"))

        def _parse_seniority_level(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seniority_level = _parse_seniority_level(d.pop("seniorityLevel"))

        def _parse_job_function(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_function = _parse_job_function(d.pop("jobFunction"))

        def _parse_posted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        posted_at = _parse_posted_at(d.pop("postedAt"))

        status = JobPostingChangeStatus(d.pop("status"))

        job_posting_change = cls(
            job_id=job_id,
            title=title,
            job_url=job_url,
            location=location,
            location_type=location_type,
            seniority_level=seniority_level,
            job_function=job_function,
            posted_at=posted_at,
            status=status,
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
