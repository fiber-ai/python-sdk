from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item import (
        CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem,
    )
    from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_total_count import (
        CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0TotalCount,
    )


T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0:
    """The postings behind `searchParams.jobPostingsV2`. Null when the search has no job postings filter.

    Attributes:
        total_count (CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0TotalCount): How many postings at
            this company satisfy the filter.
        postings (list[CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem]): A capped sample
            of the matching postings, newest first.
    """

    total_count: CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0TotalCount
    postings: list[CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count.to_dict()

        postings = []
        for postings_item_data in self.postings:
            postings_item = postings_item_data.to_dict()
            postings.append(postings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "postings": postings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_postings_item import (
            CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem,  # noqa: PLC0415
        )
        from ..models.company_search_response_200_output_data_item_matches_type_0_job_postings_type_0_total_count import (
            CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0TotalCount,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total_count = CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0TotalCount.from_dict(
            d.pop("total_count")
        )

        postings = []
        _postings = d.pop("postings")
        for postings_item_data in _postings:
            postings_item = CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItem.from_dict(
                postings_item_data
            )

            postings.append(postings_item)

        company_search_response_200_output_data_item_matches_type_0_job_postings_type_0 = cls(
            total_count=total_count,
            postings=postings,
        )

        company_search_response_200_output_data_item_matches_type_0_job_postings_type_0.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0_job_postings_type_0

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
