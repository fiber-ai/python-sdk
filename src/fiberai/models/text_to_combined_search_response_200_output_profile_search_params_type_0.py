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
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_approx_age_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_past_jobs_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_followers_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_connections_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_languages_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_location_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0:
    """ 
        Attributes:
            job_title_v3 (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0', None,
                Unset]):
            job_status (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2', None, Unset]):
            approx_age (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0', None, Unset]):
            started_in_role (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1', None, Unset]):
            started_at_company (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1', None, Unset]):
            years_of_experience
                (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0', None, Unset]):
            keywords (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0', None, Unset]):
            keyword_search_options
                (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0', None, Unset]):
            fuzzy_name (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0', None, Unset]):
            tags (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0', None, Unset]):
            stealth_v2 (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1', None, Unset]):
            country_3_letter_code
                (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0', None, Unset]):
            location (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0', None, Unset]):
            time_zone (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0', None, Unset]):
            education (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0', None, Unset]):
            languages (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0', None, Unset]):
            past_jobs (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0', None, Unset]):
            num_connections (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0', None,
                Unset]):
            num_followers (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0', None,
                Unset]):
            max_people_per_company (Union[None, Unset, float]):
     """

    job_title_v3: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0', None, Unset] = UNSET
    job_status: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2', None, Unset] = UNSET
    approx_age: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0', None, Unset] = UNSET
    started_in_role: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1', None, Unset] = UNSET
    started_at_company: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1', None, Unset] = UNSET
    years_of_experience: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0', None, Unset] = UNSET
    keywords: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0', None, Unset] = UNSET
    keyword_search_options: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0', None, Unset] = UNSET
    fuzzy_name: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0', None, Unset] = UNSET
    tags: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0', None, Unset] = UNSET
    stealth_v2: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1', None, Unset] = UNSET
    country_3_letter_code: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0', None, Unset] = UNSET
    location: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0', None, Unset] = UNSET
    time_zone: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0', None, Unset] = UNSET
    education: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0', None, Unset] = UNSET
    languages: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0', None, Unset] = UNSET
    past_jobs: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0', None, Unset] = UNSET
    num_connections: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0', None, Unset] = UNSET
    num_followers: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0', None, Unset] = UNSET
    max_people_per_company: Union[None, Unset, float] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_approx_age_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_past_jobs_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_followers_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_connections_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_languages_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_location_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0
        job_title_v3: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        job_status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        approx_age: Union[None, Unset, dict[str, Any]]
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        started_in_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(self.started_in_role, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(self.started_in_role, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(self.started_at_company, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(self.started_at_company, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        years_of_experience: Union[None, Unset, dict[str, Any]]
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(self.keyword_search_options, TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        fuzzy_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        tags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        stealth_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(self.stealth_v2, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        country_3_letter_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(self.country_3_letter_code, TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        time_zone: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        education: Union[None, Unset, dict[str, Any]]
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0):
            education = self.education.to_dict()
        else:
            education = self.education

        languages: Union[None, Unset, dict[str, Any]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        past_jobs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        num_connections: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(self.num_connections, TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(self.num_followers, TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0):
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
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_approx_age_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_at_company_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_past_jobs_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_followers_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_num_connections_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_languages_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_location_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_started_in_role_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0
        d = dict(src_dict)
        def _parse_job_title_v3(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0.from_dict(data)



                return job_title_v3_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0', None, Unset], data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))


        def _parse_job_status(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0.from_dict(data)



                return job_status_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1.from_dict(data)



                return job_status_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2.from_dict(data)



                return job_status_type_2
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2', None, Unset], data)

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))


        def _parse_approx_age(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0.from_dict(data)



                return approx_age_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0ApproxAgeType0', None, Unset], data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))


        def _parse_started_in_role(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0.from_dict(data)



                return started_in_role_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1.from_dict(data)



                return started_in_role_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedInRoleType1', None, Unset], data)

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))


        def _parse_started_at_company(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0.from_dict(data)



                return started_at_company_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1.from_dict(data)



                return started_at_company_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StartedAtCompanyType1', None, Unset], data)

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))


        def _parse_years_of_experience(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0.from_dict(data)



                return years_of_experience_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0YearsOfExperienceType0', None, Unset], data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))


        def _parse_keywords(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_keyword_search_options(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0.from_dict(data)



                return keyword_search_options_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0', None, Unset], data)

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))


        def _parse_fuzzy_name(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0.from_dict(data)



                return fuzzy_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0FuzzyNameType0', None, Unset], data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))


        def _parse_tags(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0.from_dict(data)



                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TagsType0', None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_stealth_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0.from_dict(data)



                return stealth_v2_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1.from_dict(data)



                return stealth_v2_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1', None, Unset], data)

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))


        def _parse_country_3_letter_code(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0.from_dict(data)



                return country_3_letter_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0Country3LetterCodeType0', None, Unset], data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))


        def _parse_location(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0.from_dict(data)



                return location_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LocationType0', None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_time_zone(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0.from_dict(data)



                return time_zone_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0', None, Unset], data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_education(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0.from_dict(data)



                return education_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0', None, Unset], data)

        education = _parse_education(d.pop("education", UNSET))


        def _parse_languages(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0.from_dict(data)



                return languages_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0LanguagesType0', None, Unset], data)

        languages = _parse_languages(d.pop("languages", UNSET))


        def _parse_past_jobs(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0.from_dict(data)



                return past_jobs_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0PastJobsType0', None, Unset], data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))


        def _parse_num_connections(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0.from_dict(data)



                return num_connections_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumConnectionsType0', None, Unset], data)

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))


        def _parse_num_followers(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0.from_dict(data)



                return num_followers_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0NumFollowersType0', None, Unset], data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))


        def _parse_max_people_per_company(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_people_per_company = _parse_max_people_per_company(d.pop("maxPeoplePerCompany", UNSET))


        text_to_combined_search_response_200_output_profile_search_params_type_0 = cls(
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

        return text_to_combined_search_response_200_output_profile_search_params_type_0

