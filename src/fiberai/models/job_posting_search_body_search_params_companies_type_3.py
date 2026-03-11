from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_search_body_search_params_companies_type_3_identifier import (
    JobPostingSearchBodySearchParamsCompaniesType3Identifier,
)

T = TypeVar("T", bound="JobPostingSearchBodySearchParamsCompaniesType3")


@_attrs_define
class JobPostingSearchBodySearchParamsCompaniesType3:
    """
    Attributes:
        identifier (JobPostingSearchBodySearchParamsCompaniesType3Identifier):
        value (list[str]): Array of LinkedIn organization IDs (numeric strings), e.g., '1035' for Microsoft
    """

    identifier: JobPostingSearchBodySearchParamsCompaniesType3Identifier
    value: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = JobPostingSearchBodySearchParamsCompaniesType3Identifier(d.pop("identifier"))

        value = cast(list[str], d.pop("value"))

        job_posting_search_body_search_params_companies_type_3 = cls(
            identifier=identifier,
            value=value,
        )

        job_posting_search_body_search_params_companies_type_3.additional_properties = d
        return job_posting_search_body_search_params_companies_type_3

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
