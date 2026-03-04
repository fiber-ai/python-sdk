from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_posting_search_count_body_search_params_companies_type_2_identifier import JobPostingSearchCountBodySearchParamsCompaniesType2Identifier
from typing import cast






T = TypeVar("T", bound="JobPostingSearchCountBodySearchParamsCompaniesType2")



@_attrs_define
class JobPostingSearchCountBodySearchParamsCompaniesType2:
    """ 
        Attributes:
            identifier (JobPostingSearchCountBodySearchParamsCompaniesType2Identifier):
            value (list[str]): Array of LinkedIn company URLs, e.g., https://www.linkedin.com/company/microsoft/
     """

    identifier: JobPostingSearchCountBodySearchParamsCompaniesType2Identifier
    value: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "identifier": identifier,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = JobPostingSearchCountBodySearchParamsCompaniesType2Identifier(d.pop("identifier"))




        value = cast(list[str], d.pop("value"))


        job_posting_search_count_body_search_params_companies_type_2 = cls(
            identifier=identifier,
            value=value,
        )


        job_posting_search_count_body_search_params_companies_type_2.additional_properties = d
        return job_posting_search_count_body_search_params_companies_type_2

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
