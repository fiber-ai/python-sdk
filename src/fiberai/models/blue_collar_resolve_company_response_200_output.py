from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlueCollarResolveCompanyResponse200Output")


@_attrs_define
class BlueCollarResolveCompanyResponse200Output:
    """
    Attributes:
        slug (str): Company identifier to use in the companySlug field of the search endpoint.
        company_name (str): Resolved company display name.
        job_count (float | None | Unset): Approximate number of currently open job listings.
    """

    slug: str
    company_name: str
    job_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        company_name = self.company_name

        job_count: float | None | Unset
        if isinstance(self.job_count, Unset):
            job_count = UNSET
        else:
            job_count = self.job_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "companyName": company_name,
            }
        )
        if job_count is not UNSET:
            field_dict["jobCount"] = job_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        company_name = d.pop("companyName")

        def _parse_job_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        job_count = _parse_job_count(d.pop("jobCount", UNSET))

        blue_collar_resolve_company_response_200_output = cls(
            slug=slug,
            company_name=company_name,
            job_count=job_count,
        )

        blue_collar_resolve_company_response_200_output.additional_properties = d
        return blue_collar_resolve_company_response_200_output

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
