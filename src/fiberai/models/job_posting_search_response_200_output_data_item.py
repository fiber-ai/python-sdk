from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_posting_search_response_200_output_data_item_job_function_type_0_item import JobPostingSearchResponse200OutputDataItemJobFunctionType0Item
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_1 import JobPostingSearchResponse200OutputDataItemJobLocationTypeType1
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_2_type_1 import JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_3_type_1 import JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1
from ..models.job_posting_search_response_200_output_data_item_standard_industries_type_0_item import JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item
from ..models.job_posting_search_response_200_output_data_item_status import JobPostingSearchResponse200OutputDataItemStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0
  from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import JobPostingSearchResponse200OutputDataItemApplicantRangeType0
  from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import JobPostingSearchResponse200OutputDataItemStandardizedLocationType0
  from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0
  from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0





T = TypeVar("T", bound="JobPostingSearchResponse200OutputDataItem")



@_attrs_define
class JobPostingSearchResponse200OutputDataItem:
    """ 
        Attributes:
            job_id (str): Unique job identifier
            status (JobPostingSearchResponse200OutputDataItemStatus): Job status
            title (Union[None, Unset, str]): Job title/position
            company_name (Union[None, Unset, str]): Company name
            company_logo_url (Union[None, Unset, str]): Company logo URL
            posted_at (Union[None, Unset, str]): When the job was posted
            job_url (Union[None, Unset, str]): LinkedIn job URL
            applicant_range (Union['JobPostingSearchResponse200OutputDataItemApplicantRangeType0', None, Unset]): Applicant
                count range
            description (Union[None, Unset, str]): Job description text
            seniority_level (Union[None, Unset, str]): Seniority level (e.g., 'Entry level', 'Senior level')
            employment_type (Union[None, Unset, str]): Employment type (e.g., 'Full-time', 'Part-time')
            job_function (Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item]]): Job
                function categories
            raw_industries (Union[None, Unset, str]): Raw industries string from LinkedIn
            standard_industries (Union[None, Unset,
                list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item]]): Standardized industry categories
            compensation_range (Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0', None, Unset]):
                Structured compensation range with currency and period
            annual_salary_usd (Union['JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0', None, Unset]): Annual
                salary approximation in USD
            years_of_experience (Union['JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0', None, Unset]):
                Years of experience required
            standardized_location (Union['JobPostingSearchResponse200OutputDataItemStandardizedLocationType0', None,
                Unset]): Standardized location with geo data including lat/lon
            job_location_type (Union[JobPostingSearchResponse200OutputDataItemJobLocationTypeType1,
                JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1,
                JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1, None, Unset]): Work location type
     """

    job_id: str
    status: JobPostingSearchResponse200OutputDataItemStatus
    title: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    company_logo_url: Union[None, Unset, str] = UNSET
    posted_at: Union[None, Unset, str] = UNSET
    job_url: Union[None, Unset, str] = UNSET
    applicant_range: Union['JobPostingSearchResponse200OutputDataItemApplicantRangeType0', None, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    seniority_level: Union[None, Unset, str] = UNSET
    employment_type: Union[None, Unset, str] = UNSET
    job_function: Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item]] = UNSET
    raw_industries: Union[None, Unset, str] = UNSET
    standard_industries: Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item]] = UNSET
    compensation_range: Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0', None, Unset] = UNSET
    annual_salary_usd: Union['JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0', None, Unset] = UNSET
    years_of_experience: Union['JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0', None, Unset] = UNSET
    standardized_location: Union['JobPostingSearchResponse200OutputDataItemStandardizedLocationType0', None, Unset] = UNSET
    job_location_type: Union[JobPostingSearchResponse200OutputDataItemJobLocationTypeType1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0
        from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import JobPostingSearchResponse200OutputDataItemApplicantRangeType0
        from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import JobPostingSearchResponse200OutputDataItemStandardizedLocationType0
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0
        from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0
        job_id = self.job_id

        status = self.status.value

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_logo_url: Union[None, Unset, str]
        if isinstance(self.company_logo_url, Unset):
            company_logo_url = UNSET
        else:
            company_logo_url = self.company_logo_url

        posted_at: Union[None, Unset, str]
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = self.posted_at

        job_url: Union[None, Unset, str]
        if isinstance(self.job_url, Unset):
            job_url = UNSET
        else:
            job_url = self.job_url

        applicant_range: Union[None, Unset, dict[str, Any]]
        if isinstance(self.applicant_range, Unset):
            applicant_range = UNSET
        elif isinstance(self.applicant_range, JobPostingSearchResponse200OutputDataItemApplicantRangeType0):
            applicant_range = self.applicant_range.to_dict()
        else:
            applicant_range = self.applicant_range

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        seniority_level: Union[None, Unset, str]
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        else:
            seniority_level = self.seniority_level

        employment_type: Union[None, Unset, str]
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = self.employment_type

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

        raw_industries: Union[None, Unset, str]
        if isinstance(self.raw_industries, Unset):
            raw_industries = UNSET
        else:
            raw_industries = self.raw_industries

        standard_industries: Union[None, Unset, list[str]]
        if isinstance(self.standard_industries, Unset):
            standard_industries = UNSET
        elif isinstance(self.standard_industries, list):
            standard_industries = []
            for standard_industries_type_0_item_data in self.standard_industries:
                standard_industries_type_0_item = standard_industries_type_0_item_data.value
                standard_industries.append(standard_industries_type_0_item)


        else:
            standard_industries = self.standard_industries

        compensation_range: Union[None, Unset, dict[str, Any]]
        if isinstance(self.compensation_range, Unset):
            compensation_range = UNSET
        elif isinstance(self.compensation_range, JobPostingSearchResponse200OutputDataItemCompensationRangeType0):
            compensation_range = self.compensation_range.to_dict()
        else:
            compensation_range = self.compensation_range

        annual_salary_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.annual_salary_usd, Unset):
            annual_salary_usd = UNSET
        elif isinstance(self.annual_salary_usd, JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0):
            annual_salary_usd = self.annual_salary_usd.to_dict()
        else:
            annual_salary_usd = self.annual_salary_usd

        years_of_experience: Union[None, Unset, dict[str, Any]]
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        standardized_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.standardized_location, Unset):
            standardized_location = UNSET
        elif isinstance(self.standardized_location, JobPostingSearchResponse200OutputDataItemStandardizedLocationType0):
            standardized_location = self.standardized_location.to_dict()
        else:
            standardized_location = self.standardized_location

        job_location_type: Union[None, Unset, str]
        if isinstance(self.job_location_type, Unset):
            job_location_type = UNSET
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType1):
            job_location_type = self.job_location_type.value
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1):
            job_location_type = self.job_location_type.value
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1):
            job_location_type = self.job_location_type.value
        else:
            job_location_type = self.job_location_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "job_id": job_id,
            "status": status,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_logo_url is not UNSET:
            field_dict["company_logo_url"] = company_logo_url
        if posted_at is not UNSET:
            field_dict["posted_at"] = posted_at
        if job_url is not UNSET:
            field_dict["job_url"] = job_url
        if applicant_range is not UNSET:
            field_dict["applicant_range"] = applicant_range
        if description is not UNSET:
            field_dict["description"] = description
        if seniority_level is not UNSET:
            field_dict["seniority_level"] = seniority_level
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if job_function is not UNSET:
            field_dict["job_function"] = job_function
        if raw_industries is not UNSET:
            field_dict["raw_industries"] = raw_industries
        if standard_industries is not UNSET:
            field_dict["standard_industries"] = standard_industries
        if compensation_range is not UNSET:
            field_dict["compensation_range"] = compensation_range
        if annual_salary_usd is not UNSET:
            field_dict["annual_salary_usd"] = annual_salary_usd
        if years_of_experience is not UNSET:
            field_dict["years_of_experience"] = years_of_experience
        if standardized_location is not UNSET:
            field_dict["standardized_location"] = standardized_location
        if job_location_type is not UNSET:
            field_dict["job_location_type"] = job_location_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0
        from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import JobPostingSearchResponse200OutputDataItemApplicantRangeType0
        from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import JobPostingSearchResponse200OutputDataItemStandardizedLocationType0
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0
        from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0
        d = dict(src_dict)
        job_id = d.pop("job_id")

        status = JobPostingSearchResponse200OutputDataItemStatus(d.pop("status"))




        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))


        def _parse_company_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_logo_url = _parse_company_logo_url(d.pop("company_logo_url", UNSET))


        def _parse_posted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        posted_at = _parse_posted_at(d.pop("posted_at", UNSET))


        def _parse_job_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_url = _parse_job_url(d.pop("job_url", UNSET))


        def _parse_applicant_range(data: object) -> Union['JobPostingSearchResponse200OutputDataItemApplicantRangeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applicant_range_type_0 = JobPostingSearchResponse200OutputDataItemApplicantRangeType0.from_dict(data)



                return applicant_range_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemApplicantRangeType0', None, Unset], data)

        applicant_range = _parse_applicant_range(d.pop("applicant_range", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_seniority_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        seniority_level = _parse_seniority_level(d.pop("seniority_level", UNSET))


        def _parse_employment_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        employment_type = _parse_employment_type(d.pop("employment_type", UNSET))


        def _parse_job_function(data: object) -> Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item]]:
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
                    job_function_type_0_item = JobPostingSearchResponse200OutputDataItemJobFunctionType0Item(job_function_type_0_item_data)



                    job_function_type_0.append(job_function_type_0_item)

                return job_function_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item]], data)

        job_function = _parse_job_function(d.pop("job_function", UNSET))


        def _parse_raw_industries(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        raw_industries = _parse_raw_industries(d.pop("raw_industries", UNSET))


        def _parse_standard_industries(data: object) -> Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standard_industries_type_0 = []
                _standard_industries_type_0 = data
                for standard_industries_type_0_item_data in (_standard_industries_type_0):
                    standard_industries_type_0_item = JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item(standard_industries_type_0_item_data)



                    standard_industries_type_0.append(standard_industries_type_0_item)

                return standard_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item]], data)

        standard_industries = _parse_standard_industries(d.pop("standard_industries", UNSET))


        def _parse_compensation_range(data: object) -> Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compensation_range_type_0 = JobPostingSearchResponse200OutputDataItemCompensationRangeType0.from_dict(data)



                return compensation_range_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0', None, Unset], data)

        compensation_range = _parse_compensation_range(d.pop("compensation_range", UNSET))


        def _parse_annual_salary_usd(data: object) -> Union['JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annual_salary_usd_type_0 = JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0.from_dict(data)



                return annual_salary_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0', None, Unset], data)

        annual_salary_usd = _parse_annual_salary_usd(d.pop("annual_salary_usd", UNSET))


        def _parse_years_of_experience(data: object) -> Union['JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0.from_dict(data)



                return years_of_experience_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0', None, Unset], data)

        years_of_experience = _parse_years_of_experience(d.pop("years_of_experience", UNSET))


        def _parse_standardized_location(data: object) -> Union['JobPostingSearchResponse200OutputDataItemStandardizedLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                standardized_location_type_0 = JobPostingSearchResponse200OutputDataItemStandardizedLocationType0.from_dict(data)



                return standardized_location_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemStandardizedLocationType0', None, Unset], data)

        standardized_location = _parse_standardized_location(d.pop("standardized_location", UNSET))


        def _parse_job_location_type(data: object) -> Union[JobPostingSearchResponse200OutputDataItemJobLocationTypeType1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_location_type_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType1(data)



                return job_location_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_location_type_type_2_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1(data)



                return job_location_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_location_type_type_3_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1(data)



                return job_location_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[JobPostingSearchResponse200OutputDataItemJobLocationTypeType1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1, JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1, None, Unset], data)

        job_location_type = _parse_job_location_type(d.pop("job_location_type", UNSET))


        job_posting_search_response_200_output_data_item = cls(
            job_id=job_id,
            status=status,
            title=title,
            company_name=company_name,
            company_logo_url=company_logo_url,
            posted_at=posted_at,
            job_url=job_url,
            applicant_range=applicant_range,
            description=description,
            seniority_level=seniority_level,
            employment_type=employment_type,
            job_function=job_function,
            raw_industries=raw_industries,
            standard_industries=standard_industries,
            compensation_range=compensation_range,
            annual_salary_usd=annual_salary_usd,
            years_of_experience=years_of_experience,
            standardized_location=standardized_location,
            job_location_type=job_location_type,
        )


        job_posting_search_response_200_output_data_item.additional_properties = d
        return job_posting_search_response_200_output_data_item

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
