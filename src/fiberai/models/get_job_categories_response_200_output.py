from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_job_categories_response_200_output_seniorities_item import (
    GetJobCategoriesResponse200OutputSenioritiesItem,
)

if TYPE_CHECKING:
    from ..models.get_job_categories_response_200_output_job_functions_item import (
        GetJobCategoriesResponse200OutputJobFunctionsItem,
    )


T = TypeVar("T", bound="GetJobCategoriesResponse200Output")


@_attrs_define
class GetJobCategoriesResponse200Output:
    """
    Attributes:
        job_functions (list[GetJobCategoriesResponse200OutputJobFunctionsItem]): All job functions with their
            specialties nested under them — the full two-tier taxonomy behind the `jobCategories` people-search filter.
        seniorities (list[GetJobCategoriesResponse200OutputSenioritiesItem]): Every value the `seniority` people-search
            filter accepts.
    """

    job_functions: list[GetJobCategoriesResponse200OutputJobFunctionsItem]
    seniorities: list[GetJobCategoriesResponse200OutputSenioritiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_functions = []
        for job_functions_item_data in self.job_functions:
            job_functions_item = job_functions_item_data.to_dict()
            job_functions.append(job_functions_item)

        seniorities = []
        for seniorities_item_data in self.seniorities:
            seniorities_item = seniorities_item_data.value
            seniorities.append(seniorities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobFunctions": job_functions,
                "seniorities": seniorities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_job_categories_response_200_output_job_functions_item import (
            GetJobCategoriesResponse200OutputJobFunctionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        job_functions = []
        _job_functions = d.pop("jobFunctions")
        for job_functions_item_data in _job_functions:
            job_functions_item = GetJobCategoriesResponse200OutputJobFunctionsItem.from_dict(job_functions_item_data)

            job_functions.append(job_functions_item)

        seniorities = []
        _seniorities = d.pop("seniorities")
        for seniorities_item_data in _seniorities:
            seniorities_item = GetJobCategoriesResponse200OutputSenioritiesItem(seniorities_item_data)

            seniorities.append(seniorities_item)

        get_job_categories_response_200_output = cls(
            job_functions=job_functions,
            seniorities=seniorities,
        )

        get_job_categories_response_200_output.additional_properties = d
        return get_job_categories_response_200_output

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
