from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0 import (
        BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0,
    )


T = TypeVar("T", bound="BlueCollarJobsSearchResponse200OutputJobsItem")


@_attrs_define
class BlueCollarJobsSearchResponse200OutputJobsItem:
    """
    Attributes:
        id (str): Unique job listing identifier.
        title (str): Job title.
        company_name (str): Name of the company that posted the job listing.
        location (str): Job location (city, state, or region).
        url (str): Direct URL to the full job listing.
        description (None | str | Unset): Brief description or snippet of the job posting.
        salary (BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0 | None | Unset): Compensation information.
            Covers various forms of pay (hourly, daily, monthly, yearly). Null when not listed.
        estimated_posted_at (None | str | Unset): Estimated date the job was posted in ISO 8601 format. Derived from
            approximate relative time.
    """

    id: str
    title: str
    company_name: str
    location: str
    url: str
    description: None | str | Unset = UNSET
    salary: BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0 | None | Unset = UNSET
    estimated_posted_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0,
        )

        id = self.id

        title = self.title

        company_name = self.company_name

        location = self.location

        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        salary: dict[str, Any] | None | Unset
        if isinstance(self.salary, Unset):
            salary = UNSET
        elif isinstance(self.salary, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0):
            salary = self.salary.to_dict()
        else:
            salary = self.salary

        estimated_posted_at: None | str | Unset
        if isinstance(self.estimated_posted_at, Unset):
            estimated_posted_at = UNSET
        else:
            estimated_posted_at = self.estimated_posted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "companyName": company_name,
                "location": location,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if salary is not UNSET:
            field_dict["salary"] = salary
        if estimated_posted_at is not UNSET:
            field_dict["estimatedPostedAt"] = estimated_posted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        company_name = d.pop("companyName")

        location = d.pop("location")

        url = d.pop("url")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_salary(data: object) -> BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                salary_type_0 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0.from_dict(data)

                return salary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0 | None | Unset, data)

        salary = _parse_salary(d.pop("salary", UNSET))

        def _parse_estimated_posted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_posted_at = _parse_estimated_posted_at(d.pop("estimatedPostedAt", UNSET))

        blue_collar_jobs_search_response_200_output_jobs_item = cls(
            id=id,
            title=title,
            company_name=company_name,
            location=location,
            url=url,
            description=description,
            salary=salary,
            estimated_posted_at=estimated_posted_at,
        )

        blue_collar_jobs_search_response_200_output_jobs_item.additional_properties = d
        return blue_collar_jobs_search_response_200_output_jobs_item

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
