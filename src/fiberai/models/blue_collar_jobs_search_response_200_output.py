from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blue_collar_jobs_search_response_200_output_jobs_item import (
        BlueCollarJobsSearchResponse200OutputJobsItem,
    )


T = TypeVar("T", bound="BlueCollarJobsSearchResponse200Output")


@_attrs_define
class BlueCollarJobsSearchResponse200Output:
    """
    Attributes:
        jobs (list[BlueCollarJobsSearchResponse200OutputJobsItem]): List of job listings matching the search.
        estimated_job_count (float | None | Unset): Estimated total number of matching jobs across all pages.
        next_page_token (None | str | Unset): Pagination token. Pass in the next request to get more results. Null when
            no more pages are available.
    """

    jobs: list[BlueCollarJobsSearchResponse200OutputJobsItem]
    estimated_job_count: float | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        estimated_job_count: float | None | Unset
        if isinstance(self.estimated_job_count, Unset):
            estimated_job_count = UNSET
        else:
            estimated_job_count = self.estimated_job_count

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
            }
        )
        if estimated_job_count is not UNSET:
            field_dict["estimatedJobCount"] = estimated_job_count
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item import (
            BlueCollarJobsSearchResponse200OutputJobsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = BlueCollarJobsSearchResponse200OutputJobsItem.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        def _parse_estimated_job_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_job_count = _parse_estimated_job_count(d.pop("estimatedJobCount", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        blue_collar_jobs_search_response_200_output = cls(
            jobs=jobs,
            estimated_job_count=estimated_job_count,
            next_page_token=next_page_token,
        )

        blue_collar_jobs_search_response_200_output.additional_properties = d
        return blue_collar_jobs_search_response_200_output

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
