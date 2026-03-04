from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.people_search_response_200_output_data_item_current_job_type_0_academic_qualification_type_0_item import PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item
from ..models.people_search_response_200_output_data_item_current_job_type_0_employment_type_type_0_item import PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item
from ..models.people_search_response_200_output_data_item_current_job_type_0_job_function_type_0_item import PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item
from ..models.people_search_response_200_output_data_item_current_job_type_0_seniority_type_1 import PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1
from ..models.people_search_response_200_output_data_item_current_job_type_0_seniority_type_2_type_1 import PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1
from ..models.people_search_response_200_output_data_item_current_job_type_0_seniority_type_3_type_1 import PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PeopleSearchResponse200OutputDataItemCurrentJobType0")



@_attrs_define
class PeopleSearchResponse200OutputDataItemCurrentJobType0:
    """ 
        Attributes:
            linkedin_company_id (Union[None, Unset, str]):
            is_current (Union[None, Unset, bool]):
            company_name (Union[None, Unset, str]):
            locality (Union[None, Unset, str]):
            start_date (Union[None, Unset, str]):
            end_date (Union[None, Unset, str]):
            summary (Union[None, Unset, str]):
            title (Union[None, Unset, str]):
            seniority (Union[None, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1,
                PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1,
                PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1, Unset]):
            job_function (Union[None, Unset,
                list[PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item]]):
            employment_type (Union[None, Unset,
                list[PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item]]):
            academic_qualification (Union[None, Unset,
                list[PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item]]):
            company_start_date (Union[None, Unset, str]):
            company_end_date (Union[None, Unset, str]):
     """

    linkedin_company_id: Union[None, Unset, str] = UNSET
    is_current: Union[None, Unset, bool] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    locality: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    seniority: Union[None, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1, Unset] = UNSET
    job_function: Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item]] = UNSET
    employment_type: Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item]] = UNSET
    academic_qualification: Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item]] = UNSET
    company_start_date: Union[None, Unset, str] = UNSET
    company_end_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        linkedin_company_id: Union[None, Unset, str]
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        is_current: Union[None, Unset, bool]
        if isinstance(self.is_current, Unset):
            is_current = UNSET
        else:
            is_current = self.is_current

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        locality: Union[None, Unset, str]
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        seniority: Union[None, Unset, str]
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        elif isinstance(self.seniority, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1):
            seniority = self.seniority.value
        elif isinstance(self.seniority, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1):
            seniority = self.seniority.value
        elif isinstance(self.seniority, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1):
            seniority = self.seniority.value
        else:
            seniority = self.seniority

        job_function: Union[None, Unset, list[str]]
        if isinstance(self.job_function, Unset):
            job_function = UNSET
        elif isinstance(self.job_function, list):
            job_function = []
            for job_function_type_0_item_data in self.job_function:
                job_function_type_0_item = job_function_type_0_item_data.value
                job_function.append(job_function_type_0_item)


        else:
            job_function = self.job_function

        employment_type: Union[None, Unset, list[str]]
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        elif isinstance(self.employment_type, list):
            employment_type = []
            for employment_type_type_0_item_data in self.employment_type:
                employment_type_type_0_item = employment_type_type_0_item_data.value
                employment_type.append(employment_type_type_0_item)


        else:
            employment_type = self.employment_type

        academic_qualification: Union[None, Unset, list[str]]
        if isinstance(self.academic_qualification, Unset):
            academic_qualification = UNSET
        elif isinstance(self.academic_qualification, list):
            academic_qualification = []
            for academic_qualification_type_0_item_data in self.academic_qualification:
                academic_qualification_type_0_item = academic_qualification_type_0_item_data.value
                academic_qualification.append(academic_qualification_type_0_item)


        else:
            academic_qualification = self.academic_qualification

        company_start_date: Union[None, Unset, str]
        if isinstance(self.company_start_date, Unset):
            company_start_date = UNSET
        else:
            company_start_date = self.company_start_date

        company_end_date: Union[None, Unset, str]
        if isinstance(self.company_end_date, Unset):
            company_end_date = UNSET
        else:
            company_end_date = self.company_end_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if locality is not UNSET:
            field_dict["locality"] = locality
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if job_function is not UNSET:
            field_dict["job_function"] = job_function
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if academic_qualification is not UNSET:
            field_dict["academic_qualification"] = academic_qualification
        if company_start_date is not UNSET:
            field_dict["company_start_date"] = company_start_date
        if company_end_date is not UNSET:
            field_dict["company_end_date"] = company_end_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_linkedin_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))


        def _parse_is_current(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_current = _parse_is_current(d.pop("is_current", UNSET))


        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))


        def _parse_locality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        locality = _parse_locality(d.pop("locality", UNSET))


        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))


        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_seniority(data: object) -> Union[None, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_1 = PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1(data)



                return seniority_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_2_type_1 = PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1(data)



                return seniority_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_3_type_1 = PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1(data)



                return seniority_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType2Type1, PeopleSearchResponse200OutputDataItemCurrentJobType0SeniorityType3Type1, Unset], data)

        seniority = _parse_seniority(d.pop("seniority", UNSET))


        def _parse_job_function(data: object) -> Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_function_type_0 = []
                _job_function_type_0 = data
                for job_function_type_0_item_data in (_job_function_type_0):
                    job_function_type_0_item = PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item(job_function_type_0_item_data)



                    job_function_type_0.append(job_function_type_0_item)

                return job_function_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0JobFunctionType0Item]], data)

        job_function = _parse_job_function(d.pop("job_function", UNSET))


        def _parse_employment_type(data: object) -> Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employment_type_type_0 = []
                _employment_type_type_0 = data
                for employment_type_type_0_item_data in (_employment_type_type_0):
                    employment_type_type_0_item = PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item(employment_type_type_0_item_data)



                    employment_type_type_0.append(employment_type_type_0_item)

                return employment_type_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0EmploymentTypeType0Item]], data)

        employment_type = _parse_employment_type(d.pop("employment_type", UNSET))


        def _parse_academic_qualification(data: object) -> Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                academic_qualification_type_0 = []
                _academic_qualification_type_0 = data
                for academic_qualification_type_0_item_data in (_academic_qualification_type_0):
                    academic_qualification_type_0_item = PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item(academic_qualification_type_0_item_data)



                    academic_qualification_type_0.append(academic_qualification_type_0_item)

                return academic_qualification_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[PeopleSearchResponse200OutputDataItemCurrentJobType0AcademicQualificationType0Item]], data)

        academic_qualification = _parse_academic_qualification(d.pop("academic_qualification", UNSET))


        def _parse_company_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_start_date = _parse_company_start_date(d.pop("company_start_date", UNSET))


        def _parse_company_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_end_date = _parse_company_end_date(d.pop("company_end_date", UNSET))


        people_search_response_200_output_data_item_current_job_type_0 = cls(
            linkedin_company_id=linkedin_company_id,
            is_current=is_current,
            company_name=company_name,
            locality=locality,
            start_date=start_date,
            end_date=end_date,
            summary=summary,
            title=title,
            seniority=seniority,
            job_function=job_function,
            employment_type=employment_type,
            academic_qualification=academic_qualification,
            company_start_date=company_start_date,
            company_end_date=company_end_date,
        )


        people_search_response_200_output_data_item_current_job_type_0.additional_properties = d
        return people_search_response_200_output_data_item_current_job_type_0

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
