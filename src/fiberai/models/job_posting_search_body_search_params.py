from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_posting_search_body_search_params_country_or_region_code_type_0_item import JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item
from ..models.job_posting_search_body_search_params_employment_type_type_0_item import JobPostingSearchBodySearchParamsEmploymentTypeType0Item
from ..models.job_posting_search_body_search_params_industries_type_0_item import JobPostingSearchBodySearchParamsIndustriesType0Item
from ..models.job_posting_search_body_search_params_is_active_type_1 import JobPostingSearchBodySearchParamsIsActiveType1
from ..models.job_posting_search_body_search_params_is_active_type_2_type_1 import JobPostingSearchBodySearchParamsIsActiveType2Type1
from ..models.job_posting_search_body_search_params_is_active_type_3_type_1 import JobPostingSearchBodySearchParamsIsActiveType3Type1
from ..models.job_posting_search_body_search_params_job_functions_type_0_item import JobPostingSearchBodySearchParamsJobFunctionsType0Item
from ..models.job_posting_search_body_search_params_job_location_type_type_0_item import JobPostingSearchBodySearchParamsJobLocationTypeType0Item
from ..models.job_posting_search_body_search_params_seniority_level_type_0_item import JobPostingSearchBodySearchParamsSeniorityLevelType0Item
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.job_posting_search_body_search_params_num_applicants_type_0 import JobPostingSearchBodySearchParamsNumApplicantsType0
  from ..models.job_posting_search_body_search_params_posted_at_type_0 import JobPostingSearchBodySearchParamsPostedAtType0
  from ..models.job_posting_search_body_search_params_companies_type_3 import JobPostingSearchBodySearchParamsCompaniesType3
  from ..models.job_posting_search_body_search_params_annual_salary_usd_type_0 import JobPostingSearchBodySearchParamsAnnualSalaryUsdType0
  from ..models.job_posting_search_body_search_params_posted_at_type_1 import JobPostingSearchBodySearchParamsPostedAtType1
  from ..models.job_posting_search_body_search_params_companies_type_2 import JobPostingSearchBodySearchParamsCompaniesType2
  from ..models.job_posting_search_body_search_params_years_of_experience_type_0 import JobPostingSearchBodySearchParamsYearsOfExperienceType0
  from ..models.job_posting_search_body_search_params_companies_type_1 import JobPostingSearchBodySearchParamsCompaniesType1
  from ..models.job_posting_search_body_search_params_companies_type_0 import JobPostingSearchBodySearchParamsCompaniesType0





T = TypeVar("T", bound="JobPostingSearchBodySearchParams")



@_attrs_define
class JobPostingSearchBodySearchParams:
    """ Job search filter parameters

        Attributes:
            companies (Union['JobPostingSearchBodySearchParamsCompaniesType0',
                'JobPostingSearchBodySearchParamsCompaniesType1', 'JobPostingSearchBodySearchParamsCompaniesType2',
                'JobPostingSearchBodySearchParamsCompaniesType3', None, Unset]): Filter jobs by one type of company identifier
                with array values
            title (Union[None, Unset, list[str]]): Array of job titles for partial match (e.g., 'Software Engineer',
                'Manager')
            is_active (Union[JobPostingSearchBodySearchParamsIsActiveType1,
                JobPostingSearchBodySearchParamsIsActiveType2Type1, JobPostingSearchBodySearchParamsIsActiveType3Type1, None,
                Unset]): Filter by job status: true=active, false=closed, no_preference=both
            posted_at (Union['JobPostingSearchBodySearchParamsPostedAtType0',
                'JobPostingSearchBodySearchParamsPostedAtType1', None, Unset]): Filter by job posting date (supports relative
                and absolute dates)
            num_applicants (Union['JobPostingSearchBodySearchParamsNumApplicantsType0', None, Unset]): Filter by number of
                applicants (range)
            job_functions (Union[None, Unset, list[JobPostingSearchBodySearchParamsJobFunctionsType0Item]]): Array of job
                functions
            industries (Union[None, Unset, list[JobPostingSearchBodySearchParamsIndustriesType0Item]]): Array of industries
            annual_salary_usd (Union['JobPostingSearchBodySearchParamsAnnualSalaryUsdType0', None, Unset]): Filter by annual
                salary range in USD
            years_of_experience (Union['JobPostingSearchBodySearchParamsYearsOfExperienceType0', None, Unset]): Filter by
                years of experience required
            job_location_type (Union[None, Unset, list[JobPostingSearchBodySearchParamsJobLocationTypeType0Item]]): Array of
                work location types
            employment_type (Union[None, Unset, list[JobPostingSearchBodySearchParamsEmploymentTypeType0Item]]): Array of
                employment types (e.g., Full-time, Part-time, Contract, Internship)
            seniority_level (Union[None, Unset, list[JobPostingSearchBodySearchParamsSeniorityLevelType0Item]]): Array of
                seniority levels (e.g., Entry level, Mid-Senior level, Director)
            country_or_region_code (Union[None, Unset, list[JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item]]):
                Array of country or region codes (e.g., USA, IND, X-ANGLOSPHERE)
     """

    companies: Union['JobPostingSearchBodySearchParamsCompaniesType0', 'JobPostingSearchBodySearchParamsCompaniesType1', 'JobPostingSearchBodySearchParamsCompaniesType2', 'JobPostingSearchBodySearchParamsCompaniesType3', None, Unset] = UNSET
    title: Union[None, Unset, list[str]] = UNSET
    is_active: Union[JobPostingSearchBodySearchParamsIsActiveType1, JobPostingSearchBodySearchParamsIsActiveType2Type1, JobPostingSearchBodySearchParamsIsActiveType3Type1, None, Unset] = UNSET
    posted_at: Union['JobPostingSearchBodySearchParamsPostedAtType0', 'JobPostingSearchBodySearchParamsPostedAtType1', None, Unset] = UNSET
    num_applicants: Union['JobPostingSearchBodySearchParamsNumApplicantsType0', None, Unset] = UNSET
    job_functions: Union[None, Unset, list[JobPostingSearchBodySearchParamsJobFunctionsType0Item]] = UNSET
    industries: Union[None, Unset, list[JobPostingSearchBodySearchParamsIndustriesType0Item]] = UNSET
    annual_salary_usd: Union['JobPostingSearchBodySearchParamsAnnualSalaryUsdType0', None, Unset] = UNSET
    years_of_experience: Union['JobPostingSearchBodySearchParamsYearsOfExperienceType0', None, Unset] = UNSET
    job_location_type: Union[None, Unset, list[JobPostingSearchBodySearchParamsJobLocationTypeType0Item]] = UNSET
    employment_type: Union[None, Unset, list[JobPostingSearchBodySearchParamsEmploymentTypeType0Item]] = UNSET
    seniority_level: Union[None, Unset, list[JobPostingSearchBodySearchParamsSeniorityLevelType0Item]] = UNSET
    country_or_region_code: Union[None, Unset, list[JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.job_posting_search_body_search_params_num_applicants_type_0 import JobPostingSearchBodySearchParamsNumApplicantsType0
        from ..models.job_posting_search_body_search_params_posted_at_type_0 import JobPostingSearchBodySearchParamsPostedAtType0
        from ..models.job_posting_search_body_search_params_companies_type_3 import JobPostingSearchBodySearchParamsCompaniesType3
        from ..models.job_posting_search_body_search_params_annual_salary_usd_type_0 import JobPostingSearchBodySearchParamsAnnualSalaryUsdType0
        from ..models.job_posting_search_body_search_params_posted_at_type_1 import JobPostingSearchBodySearchParamsPostedAtType1
        from ..models.job_posting_search_body_search_params_companies_type_2 import JobPostingSearchBodySearchParamsCompaniesType2
        from ..models.job_posting_search_body_search_params_years_of_experience_type_0 import JobPostingSearchBodySearchParamsYearsOfExperienceType0
        from ..models.job_posting_search_body_search_params_companies_type_1 import JobPostingSearchBodySearchParamsCompaniesType1
        from ..models.job_posting_search_body_search_params_companies_type_0 import JobPostingSearchBodySearchParamsCompaniesType0
        companies: Union[None, Unset, dict[str, Any]]
        if isinstance(self.companies, Unset):
            companies = UNSET
        elif isinstance(self.companies, JobPostingSearchBodySearchParamsCompaniesType0):
            companies = self.companies.to_dict()
        elif isinstance(self.companies, JobPostingSearchBodySearchParamsCompaniesType1):
            companies = self.companies.to_dict()
        elif isinstance(self.companies, JobPostingSearchBodySearchParamsCompaniesType2):
            companies = self.companies.to_dict()
        elif isinstance(self.companies, JobPostingSearchBodySearchParamsCompaniesType3):
            companies = self.companies.to_dict()
        else:
            companies = self.companies

        title: Union[None, Unset, list[str]]
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, list):
            title = self.title


        else:
            title = self.title

        is_active: Union[None, Unset, str]
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        elif isinstance(self.is_active, JobPostingSearchBodySearchParamsIsActiveType1):
            is_active = self.is_active.value
        elif isinstance(self.is_active, JobPostingSearchBodySearchParamsIsActiveType2Type1):
            is_active = self.is_active.value
        elif isinstance(self.is_active, JobPostingSearchBodySearchParamsIsActiveType3Type1):
            is_active = self.is_active.value
        else:
            is_active = self.is_active

        posted_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, JobPostingSearchBodySearchParamsPostedAtType0):
            posted_at = self.posted_at.to_dict()
        elif isinstance(self.posted_at, JobPostingSearchBodySearchParamsPostedAtType1):
            posted_at = self.posted_at.to_dict()
        else:
            posted_at = self.posted_at

        num_applicants: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_applicants, Unset):
            num_applicants = UNSET
        elif isinstance(self.num_applicants, JobPostingSearchBodySearchParamsNumApplicantsType0):
            num_applicants = self.num_applicants.to_dict()
        else:
            num_applicants = self.num_applicants

        job_functions: Union[None, Unset, list[str]]
        if isinstance(self.job_functions, Unset):
            job_functions = UNSET
        elif isinstance(self.job_functions, list):
            job_functions = []
            for job_functions_type_0_item_data in self.job_functions:
                job_functions_type_0_item = job_functions_type_0_item_data.value
                job_functions.append(job_functions_type_0_item)


        else:
            job_functions = self.job_functions

        industries: Union[None, Unset, list[str]]
        if isinstance(self.industries, Unset):
            industries = UNSET
        elif isinstance(self.industries, list):
            industries = []
            for industries_type_0_item_data in self.industries:
                industries_type_0_item = industries_type_0_item_data.value
                industries.append(industries_type_0_item)


        else:
            industries = self.industries

        annual_salary_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.annual_salary_usd, Unset):
            annual_salary_usd = UNSET
        elif isinstance(self.annual_salary_usd, JobPostingSearchBodySearchParamsAnnualSalaryUsdType0):
            annual_salary_usd = self.annual_salary_usd.to_dict()
        else:
            annual_salary_usd = self.annual_salary_usd

        years_of_experience: Union[None, Unset, dict[str, Any]]
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, JobPostingSearchBodySearchParamsYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        job_location_type: Union[None, Unset, list[str]]
        if isinstance(self.job_location_type, Unset):
            job_location_type = UNSET
        elif isinstance(self.job_location_type, list):
            job_location_type = []
            for job_location_type_type_0_item_data in self.job_location_type:
                job_location_type_type_0_item = job_location_type_type_0_item_data.value
                job_location_type.append(job_location_type_type_0_item)


        else:
            job_location_type = self.job_location_type

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

        seniority_level: Union[None, Unset, list[str]]
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        elif isinstance(self.seniority_level, list):
            seniority_level = []
            for seniority_level_type_0_item_data in self.seniority_level:
                seniority_level_type_0_item = seniority_level_type_0_item_data.value
                seniority_level.append(seniority_level_type_0_item)


        else:
            seniority_level = self.seniority_level

        country_or_region_code: Union[None, Unset, list[str]]
        if isinstance(self.country_or_region_code, Unset):
            country_or_region_code = UNSET
        elif isinstance(self.country_or_region_code, list):
            country_or_region_code = []
            for country_or_region_code_type_0_item_data in self.country_or_region_code:
                country_or_region_code_type_0_item = country_or_region_code_type_0_item_data.value
                country_or_region_code.append(country_or_region_code_type_0_item)


        else:
            country_or_region_code = self.country_or_region_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if companies is not UNSET:
            field_dict["companies"] = companies
        if title is not UNSET:
            field_dict["title"] = title
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if num_applicants is not UNSET:
            field_dict["numApplicants"] = num_applicants
        if job_functions is not UNSET:
            field_dict["jobFunctions"] = job_functions
        if industries is not UNSET:
            field_dict["industries"] = industries
        if annual_salary_usd is not UNSET:
            field_dict["annualSalaryUsd"] = annual_salary_usd
        if years_of_experience is not UNSET:
            field_dict["yearsOfExperience"] = years_of_experience
        if job_location_type is not UNSET:
            field_dict["jobLocationType"] = job_location_type
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if seniority_level is not UNSET:
            field_dict["seniorityLevel"] = seniority_level
        if country_or_region_code is not UNSET:
            field_dict["countryOrRegionCode"] = country_or_region_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_posting_search_body_search_params_num_applicants_type_0 import JobPostingSearchBodySearchParamsNumApplicantsType0
        from ..models.job_posting_search_body_search_params_posted_at_type_0 import JobPostingSearchBodySearchParamsPostedAtType0
        from ..models.job_posting_search_body_search_params_companies_type_3 import JobPostingSearchBodySearchParamsCompaniesType3
        from ..models.job_posting_search_body_search_params_annual_salary_usd_type_0 import JobPostingSearchBodySearchParamsAnnualSalaryUsdType0
        from ..models.job_posting_search_body_search_params_posted_at_type_1 import JobPostingSearchBodySearchParamsPostedAtType1
        from ..models.job_posting_search_body_search_params_companies_type_2 import JobPostingSearchBodySearchParamsCompaniesType2
        from ..models.job_posting_search_body_search_params_years_of_experience_type_0 import JobPostingSearchBodySearchParamsYearsOfExperienceType0
        from ..models.job_posting_search_body_search_params_companies_type_1 import JobPostingSearchBodySearchParamsCompaniesType1
        from ..models.job_posting_search_body_search_params_companies_type_0 import JobPostingSearchBodySearchParamsCompaniesType0
        d = dict(src_dict)
        def _parse_companies(data: object) -> Union['JobPostingSearchBodySearchParamsCompaniesType0', 'JobPostingSearchBodySearchParamsCompaniesType1', 'JobPostingSearchBodySearchParamsCompaniesType2', 'JobPostingSearchBodySearchParamsCompaniesType3', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_type_0 = JobPostingSearchBodySearchParamsCompaniesType0.from_dict(data)



                return companies_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_type_1 = JobPostingSearchBodySearchParamsCompaniesType1.from_dict(data)



                return companies_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_type_2 = JobPostingSearchBodySearchParamsCompaniesType2.from_dict(data)



                return companies_type_2
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_type_3 = JobPostingSearchBodySearchParamsCompaniesType3.from_dict(data)



                return companies_type_3
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchBodySearchParamsCompaniesType0', 'JobPostingSearchBodySearchParamsCompaniesType1', 'JobPostingSearchBodySearchParamsCompaniesType2', 'JobPostingSearchBodySearchParamsCompaniesType3', None, Unset], data)

        companies = _parse_companies(d.pop("companies", UNSET))


        def _parse_title(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                title_type_0 = cast(list[str], data)

                return title_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_is_active(data: object) -> Union[JobPostingSearchBodySearchParamsIsActiveType1, JobPostingSearchBodySearchParamsIsActiveType2Type1, JobPostingSearchBodySearchParamsIsActiveType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                is_active_type_1 = JobPostingSearchBodySearchParamsIsActiveType1(data)



                return is_active_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                is_active_type_2_type_1 = JobPostingSearchBodySearchParamsIsActiveType2Type1(data)



                return is_active_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                is_active_type_3_type_1 = JobPostingSearchBodySearchParamsIsActiveType3Type1(data)



                return is_active_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[JobPostingSearchBodySearchParamsIsActiveType1, JobPostingSearchBodySearchParamsIsActiveType2Type1, JobPostingSearchBodySearchParamsIsActiveType3Type1, None, Unset], data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))


        def _parse_posted_at(data: object) -> Union['JobPostingSearchBodySearchParamsPostedAtType0', 'JobPostingSearchBodySearchParamsPostedAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_0 = JobPostingSearchBodySearchParamsPostedAtType0.from_dict(data)



                return posted_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_1 = JobPostingSearchBodySearchParamsPostedAtType1.from_dict(data)



                return posted_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchBodySearchParamsPostedAtType0', 'JobPostingSearchBodySearchParamsPostedAtType1', None, Unset], data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))


        def _parse_num_applicants(data: object) -> Union['JobPostingSearchBodySearchParamsNumApplicantsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_applicants_type_0 = JobPostingSearchBodySearchParamsNumApplicantsType0.from_dict(data)



                return num_applicants_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchBodySearchParamsNumApplicantsType0', None, Unset], data)

        num_applicants = _parse_num_applicants(d.pop("numApplicants", UNSET))


        def _parse_job_functions(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsJobFunctionsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_functions_type_0 = []
                _job_functions_type_0 = data
                for job_functions_type_0_item_data in (_job_functions_type_0):
                    job_functions_type_0_item = JobPostingSearchBodySearchParamsJobFunctionsType0Item(job_functions_type_0_item_data)



                    job_functions_type_0.append(job_functions_type_0_item)

                return job_functions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsJobFunctionsType0Item]], data)

        job_functions = _parse_job_functions(d.pop("jobFunctions", UNSET))


        def _parse_industries(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsIndustriesType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = []
                _industries_type_0 = data
                for industries_type_0_item_data in (_industries_type_0):
                    industries_type_0_item = JobPostingSearchBodySearchParamsIndustriesType0Item(industries_type_0_item_data)



                    industries_type_0.append(industries_type_0_item)

                return industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsIndustriesType0Item]], data)

        industries = _parse_industries(d.pop("industries", UNSET))


        def _parse_annual_salary_usd(data: object) -> Union['JobPostingSearchBodySearchParamsAnnualSalaryUsdType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annual_salary_usd_type_0 = JobPostingSearchBodySearchParamsAnnualSalaryUsdType0.from_dict(data)



                return annual_salary_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchBodySearchParamsAnnualSalaryUsdType0', None, Unset], data)

        annual_salary_usd = _parse_annual_salary_usd(d.pop("annualSalaryUsd", UNSET))


        def _parse_years_of_experience(data: object) -> Union['JobPostingSearchBodySearchParamsYearsOfExperienceType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = JobPostingSearchBodySearchParamsYearsOfExperienceType0.from_dict(data)



                return years_of_experience_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchBodySearchParamsYearsOfExperienceType0', None, Unset], data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))


        def _parse_job_location_type(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsJobLocationTypeType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_location_type_type_0 = []
                _job_location_type_type_0 = data
                for job_location_type_type_0_item_data in (_job_location_type_type_0):
                    job_location_type_type_0_item = JobPostingSearchBodySearchParamsJobLocationTypeType0Item(job_location_type_type_0_item_data)



                    job_location_type_type_0.append(job_location_type_type_0_item)

                return job_location_type_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsJobLocationTypeType0Item]], data)

        job_location_type = _parse_job_location_type(d.pop("jobLocationType", UNSET))


        def _parse_employment_type(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsEmploymentTypeType0Item]]:
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
                    employment_type_type_0_item = JobPostingSearchBodySearchParamsEmploymentTypeType0Item(employment_type_type_0_item_data)



                    employment_type_type_0.append(employment_type_type_0_item)

                return employment_type_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsEmploymentTypeType0Item]], data)

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))


        def _parse_seniority_level(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsSeniorityLevelType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seniority_level_type_0 = []
                _seniority_level_type_0 = data
                for seniority_level_type_0_item_data in (_seniority_level_type_0):
                    seniority_level_type_0_item = JobPostingSearchBodySearchParamsSeniorityLevelType0Item(seniority_level_type_0_item_data)



                    seniority_level_type_0.append(seniority_level_type_0_item)

                return seniority_level_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsSeniorityLevelType0Item]], data)

        seniority_level = _parse_seniority_level(d.pop("seniorityLevel", UNSET))


        def _parse_country_or_region_code(data: object) -> Union[None, Unset, list[JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                country_or_region_code_type_0 = []
                _country_or_region_code_type_0 = data
                for country_or_region_code_type_0_item_data in (_country_or_region_code_type_0):
                    country_or_region_code_type_0_item = JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item(country_or_region_code_type_0_item_data)



                    country_or_region_code_type_0.append(country_or_region_code_type_0_item)

                return country_or_region_code_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[JobPostingSearchBodySearchParamsCountryOrRegionCodeType0Item]], data)

        country_or_region_code = _parse_country_or_region_code(d.pop("countryOrRegionCode", UNSET))


        job_posting_search_body_search_params = cls(
            companies=companies,
            title=title,
            is_active=is_active,
            posted_at=posted_at,
            num_applicants=num_applicants,
            job_functions=job_functions,
            industries=industries,
            annual_salary_usd=annual_salary_usd,
            years_of_experience=years_of_experience,
            job_location_type=job_location_type,
            employment_type=employment_type,
            seniority_level=seniority_level,
            country_or_region_code=country_or_region_code,
        )

        return job_posting_search_body_search_params

