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
  from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_location_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_years_of_experience_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_languages_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1
  from ..models.text_to_profile_search_params_response_200_output_search_params_num_followers_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_tags_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_keyword_search_options_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0
  from ..models.text_to_profile_search_params_response_200_output_search_params_time_zone_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1
  from ..models.text_to_profile_search_params_response_200_output_search_params_num_connections_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_fuzzy_name_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1
  from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1
  from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2
  from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_job_title_v3_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0
  from ..models.text_to_profile_search_params_response_200_output_search_params_keywords_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_country_3_letter_code_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0
  from ..models.text_to_profile_search_params_response_200_output_search_params_approx_age_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0





T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParams")



@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParams:
    """ 
        Attributes:
            job_title_v3 (Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0', None, Unset]):
            job_status (Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0',
                'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1',
                'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2', None, Unset]):
            approx_age (Union['TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0', None, Unset]):
            started_in_role (Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0',
                'TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1', None, Unset]):
            started_at_company (Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0',
                'TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1', None, Unset]):
            years_of_experience (Union['TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0', None,
                Unset]):
            keywords (Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0', None, Unset]):
            keyword_search_options (Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0',
                None, Unset]):
            fuzzy_name (Union['TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0', None, Unset]):
            tags (Union['TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0', None, Unset]):
            stealth_v2 (Union['TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0',
                'TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1', None, Unset]):
            country_3_letter_code (Union['TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0',
                None, Unset]):
            location (Union['TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0', None, Unset]):
            time_zone (Union['TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0', None, Unset]):
            education (Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0', None, Unset]):
            languages (Union['TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0', None, Unset]):
            past_jobs (Union['TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0', None, Unset]):
            num_connections (Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0', None,
                Unset]):
            num_followers (Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0', None, Unset]):
            max_people_per_company (Union[None, Unset, float]):
     """

    job_title_v3: Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0', None, Unset] = UNSET
    job_status: Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2', None, Unset] = UNSET
    approx_age: Union['TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0', None, Unset] = UNSET
    started_in_role: Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1', None, Unset] = UNSET
    started_at_company: Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1', None, Unset] = UNSET
    years_of_experience: Union['TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0', None, Unset] = UNSET
    keywords: Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0', None, Unset] = UNSET
    keyword_search_options: Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0', None, Unset] = UNSET
    fuzzy_name: Union['TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0', None, Unset] = UNSET
    tags: Union['TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0', None, Unset] = UNSET
    stealth_v2: Union['TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1', None, Unset] = UNSET
    country_3_letter_code: Union['TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0', None, Unset] = UNSET
    location: Union['TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0', None, Unset] = UNSET
    time_zone: Union['TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0', None, Unset] = UNSET
    education: Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0', None, Unset] = UNSET
    languages: Union['TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0', None, Unset] = UNSET
    past_jobs: Union['TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0', None, Unset] = UNSET
    num_connections: Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0', None, Unset] = UNSET
    num_followers: Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0', None, Unset] = UNSET
    max_people_per_company: Union[None, Unset, float] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_location_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_years_of_experience_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_languages_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_num_followers_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_tags_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_keyword_search_options_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0
        from ..models.text_to_profile_search_params_response_200_output_search_params_time_zone_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_num_connections_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_fuzzy_name_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1
        from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_title_v3_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0
        from ..models.text_to_profile_search_params_response_200_output_search_params_keywords_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_country_3_letter_code_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_approx_age_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0
        job_title_v3: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        job_status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        approx_age: Union[None, Unset, dict[str, Any]]
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        started_in_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(self.started_in_role, TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(self.started_in_role, TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(self.started_at_company, TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(self.started_at_company, TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        years_of_experience: Union[None, Unset, dict[str, Any]]
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(self.keyword_search_options, TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        fuzzy_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        tags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        stealth_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(self.stealth_v2, TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        country_3_letter_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(self.country_3_letter_code, TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        time_zone: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        education: Union[None, Unset, dict[str, Any]]
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0):
            education = self.education.to_dict()
        else:
            education = self.education

        languages: Union[None, Unset, dict[str, Any]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        past_jobs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        num_connections: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(self.num_connections, TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(self.num_followers, TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0):
            num_followers = self.num_followers.to_dict()
        else:
            num_followers = self.num_followers

        max_people_per_company: Union[None, Unset, float]
        if isinstance(self.max_people_per_company, Unset):
            max_people_per_company = UNSET
        else:
            max_people_per_company = self.max_people_per_company


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if job_title_v3 is not UNSET:
            field_dict["jobTitleV3"] = job_title_v3
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if approx_age is not UNSET:
            field_dict["approxAge"] = approx_age
        if started_in_role is not UNSET:
            field_dict["startedInRole"] = started_in_role
        if started_at_company is not UNSET:
            field_dict["startedAtCompany"] = started_at_company
        if years_of_experience is not UNSET:
            field_dict["yearsOfExperience"] = years_of_experience
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if keyword_search_options is not UNSET:
            field_dict["keywordSearchOptions"] = keyword_search_options
        if fuzzy_name is not UNSET:
            field_dict["fuzzyName"] = fuzzy_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if stealth_v2 is not UNSET:
            field_dict["stealthV2"] = stealth_v2
        if country_3_letter_code is not UNSET:
            field_dict["country3LetterCode"] = country_3_letter_code
        if location is not UNSET:
            field_dict["location"] = location
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if education is not UNSET:
            field_dict["education"] = education
        if languages is not UNSET:
            field_dict["languages"] = languages
        if past_jobs is not UNSET:
            field_dict["pastJobs"] = past_jobs
        if num_connections is not UNSET:
            field_dict["numConnections"] = num_connections
        if num_followers is not UNSET:
            field_dict["numFollowers"] = num_followers
        if max_people_per_company is not UNSET:
            field_dict["maxPeoplePerCompany"] = max_people_per_company

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_location_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_years_of_experience_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_languages_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_num_followers_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_tags_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_keyword_search_options_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0
        from ..models.text_to_profile_search_params_response_200_output_search_params_time_zone_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_at_company_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_num_connections_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_fuzzy_name_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_stealth_v2_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1
        from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_started_in_role_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_status_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_job_title_v3_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0
        from ..models.text_to_profile_search_params_response_200_output_search_params_keywords_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_country_3_letter_code_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0
        from ..models.text_to_profile_search_params_response_200_output_search_params_approx_age_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0
        d = dict(src_dict)
        def _parse_job_title_v3(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0.from_dict(data)



                return job_title_v3_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobTitleV3Type0', None, Unset], data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))


        def _parse_job_status(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0.from_dict(data)



                return job_status_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1.from_dict(data)



                return job_status_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2.from_dict(data)



                return job_status_type_2
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsJobStatusType2', None, Unset], data)

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))


        def _parse_approx_age(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0.from_dict(data)



                return approx_age_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsApproxAgeType0', None, Unset], data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))


        def _parse_started_in_role(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0.from_dict(data)



                return started_in_role_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1.from_dict(data)



                return started_in_role_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedInRoleType1', None, Unset], data)

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))


        def _parse_started_at_company(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0.from_dict(data)



                return started_at_company_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1.from_dict(data)



                return started_at_company_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStartedAtCompanyType1', None, Unset], data)

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))


        def _parse_years_of_experience(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0.from_dict(data)



                return years_of_experience_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsYearsOfExperienceType0', None, Unset], data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))


        def _parse_keywords(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_keyword_search_options(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0.from_dict(data)



                return keyword_search_options_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsKeywordSearchOptionsType0', None, Unset], data)

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))


        def _parse_fuzzy_name(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0.from_dict(data)



                return fuzzy_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsFuzzyNameType0', None, Unset], data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))


        def _parse_tags(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0.from_dict(data)



                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0', None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_stealth_v2(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0.from_dict(data)



                return stealth_v2_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1.from_dict(data)



                return stealth_v2_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type0', 'TextToProfileSearchParamsResponse200OutputSearchParamsStealthV2Type1', None, Unset], data)

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))


        def _parse_country_3_letter_code(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0.from_dict(data)



                return country_3_letter_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsCountry3LetterCodeType0', None, Unset], data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))


        def _parse_location(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0.from_dict(data)



                return location_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsLocationType0', None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_time_zone(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0.from_dict(data)



                return time_zone_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsTimeZoneType0', None, Unset], data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_education(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0.from_dict(data)



                return education_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0', None, Unset], data)

        education = _parse_education(d.pop("education", UNSET))


        def _parse_languages(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0.from_dict(data)



                return languages_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsLanguagesType0', None, Unset], data)

        languages = _parse_languages(d.pop("languages", UNSET))


        def _parse_past_jobs(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0.from_dict(data)



                return past_jobs_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0', None, Unset], data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))


        def _parse_num_connections(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0.from_dict(data)



                return num_connections_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumConnectionsType0', None, Unset], data)

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))


        def _parse_num_followers(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0.from_dict(data)



                return num_followers_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsNumFollowersType0', None, Unset], data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))


        def _parse_max_people_per_company(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_people_per_company = _parse_max_people_per_company(d.pop("maxPeoplePerCompany", UNSET))


        text_to_profile_search_params_response_200_output_search_params = cls(
            job_title_v3=job_title_v3,
            job_status=job_status,
            approx_age=approx_age,
            started_in_role=started_in_role,
            started_at_company=started_at_company,
            years_of_experience=years_of_experience,
            keywords=keywords,
            keyword_search_options=keyword_search_options,
            fuzzy_name=fuzzy_name,
            tags=tags,
            stealth_v2=stealth_v2,
            country_3_letter_code=country_3_letter_code,
            location=location,
            time_zone=time_zone,
            education=education,
            languages=languages,
            past_jobs=past_jobs,
            num_connections=num_connections,
            num_followers=num_followers,
            max_people_per_company=max_people_per_company,
        )

        return text_to_profile_search_params_response_200_output_search_params

