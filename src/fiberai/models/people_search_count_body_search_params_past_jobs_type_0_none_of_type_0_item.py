from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item_company_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0





T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0Item")



@_attrs_define
class PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0Item:
    """ 
        Attributes:
            job_title (Union[None, Unset, list[str]]):
            company (Union['PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0', None, Unset]):
     """

    job_title: Union[None, Unset, list[str]] = UNSET
    company: Union['PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item_company_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0
        job_title: Union[None, Unset, list[str]]
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, list):
            job_title = self.job_title


        else:
            job_title = self.job_title

        company: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0):
            company = self.company.to_dict()
        else:
            company = self.company


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item_company_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0
        d = dict(src_dict)
        def _parse_job_title(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_title_type_0 = cast(list[str], data)

                return job_title_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        def _parse_company(data: object) -> Union['PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0.from_dict(data)



                return company_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsPastJobsType0NoneOfType0ItemCompanyType0', None, Unset], data)

        company = _parse_company(d.pop("company", UNSET))


        people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item = cls(
            job_title=job_title,
            company=company,
        )


        people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item.additional_properties = d
        return people_search_count_body_search_params_past_jobs_type_0_none_of_type_0_item

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
