from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="JobPostingSearchCountResponse200Output")



@_attrs_define
class JobPostingSearchCountResponse200Output:
    """ 
        Attributes:
            total_jobs_found (int): Total number of jobs matching the search criteria
     """

    total_jobs_found: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_jobs_found = self.total_jobs_found


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "totalJobsFound": total_jobs_found,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_jobs_found = d.pop("totalJobsFound")

        job_posting_search_count_response_200_output = cls(
            total_jobs_found=total_jobs_found,
        )


        job_posting_search_count_response_200_output.additional_properties = d
        return job_posting_search_count_response_200_output

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
