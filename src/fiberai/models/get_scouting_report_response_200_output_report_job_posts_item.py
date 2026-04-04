from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportJobPostsItem")


@_attrs_define
class GetScoutingReportResponse200OutputReportJobPostsItem:
    """
    Attributes:
        job_id (str):
        title (None | str):
        location (None | str):
        posted_at (None | str):
        job_url (None | str):
        location_type (None | str):
    """

    job_id: str
    title: None | str
    location: None | str
    posted_at: None | str
    job_url: None | str
    location_type: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        title: None | str
        title = self.title

        location: None | str
        location = self.location

        posted_at: None | str
        posted_at = self.posted_at

        job_url: None | str
        job_url = self.job_url

        location_type: None | str
        location_type = self.location_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
                "title": title,
                "location": location,
                "postedAt": posted_at,
                "jobUrl": job_url,
                "locationType": location_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_posted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        posted_at = _parse_posted_at(d.pop("postedAt"))

        def _parse_job_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_url = _parse_job_url(d.pop("jobUrl"))

        def _parse_location_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location_type = _parse_location_type(d.pop("locationType"))

        get_scouting_report_response_200_output_report_job_posts_item = cls(
            job_id=job_id,
            title=title,
            location=location,
            posted_at=posted_at,
            job_url=job_url,
            location_type=location_type,
        )

        get_scouting_report_response_200_output_report_job_posts_item.additional_properties = d
        return get_scouting_report_response_200_output_report_job_posts_item

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
