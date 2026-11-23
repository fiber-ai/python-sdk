from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item_status import (
    CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem:
    """A job posting that satisfied the job postings filter.

    Attributes:
        job_id (str): Unique job identifier
        status (CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItemStatus): Job status
        title (None | str | Unset): Job title/position
        posted_at (None | str | Unset): When the job was posted
        job_url (None | str | Unset): LinkedIn job URL
    """

    job_id: str
    status: CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItemStatus
    title: None | str | Unset = UNSET
    posted_at: None | str | Unset = UNSET
    job_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status = self.status.value

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = self.posted_at

        job_url: None | str | Unset
        if isinstance(self.job_url, Unset):
            job_url = UNSET
        else:
            job_url = self.job_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "status": status,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if posted_at is not UNSET:
            field_dict["posted_at"] = posted_at
        if job_url is not UNSET:
            field_dict["job_url"] = job_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        status = CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItemStatus(d.pop("status"))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_posted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        posted_at = _parse_posted_at(d.pop("posted_at", UNSET))

        def _parse_job_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_url = _parse_job_url(d.pop("job_url", UNSET))

        company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item = cls(
            job_id=job_id,
            status=status,
            title=title,
            posted_at=posted_at,
            job_url=job_url,
        )

        company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item

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
