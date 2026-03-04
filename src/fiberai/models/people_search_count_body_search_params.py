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
  from ..models.people_search_count_body_search_params_approx_age_type_0 import PeopleSearchCountBodySearchParamsApproxAgeType0
  from ..models.people_search_count_body_search_params_keywords_type_0 import PeopleSearchCountBodySearchParamsKeywordsType0
  from ..models.people_search_count_body_search_params_started_in_role_type_0 import PeopleSearchCountBodySearchParamsStartedInRoleType0
  from ..models.people_search_count_body_search_params_stealth_v2_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1
  from ..models.people_search_count_body_search_params_started_at_company_type_0 import PeopleSearchCountBodySearchParamsStartedAtCompanyType0
  from ..models.people_search_count_body_search_params_past_job_text_type_0 import PeopleSearchCountBodySearchParamsPastJobTextType0
  from ..models.people_search_count_body_search_params_years_of_experience_type_0 import PeopleSearchCountBodySearchParamsYearsOfExperienceType0
  from ..models.people_search_count_body_search_params_education_type_0 import PeopleSearchCountBodySearchParamsEducationType0
  from ..models.people_search_count_body_search_params_left_stealth_at_type_1 import PeopleSearchCountBodySearchParamsLeftStealthAtType1
  from ..models.people_search_count_body_search_params_keyword_search_options_type_0 import PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0
  from ..models.people_search_count_body_search_params_left_stealth_at_type_0 import PeopleSearchCountBodySearchParamsLeftStealthAtType0
  from ..models.people_search_count_body_search_params_job_status_type_0 import PeopleSearchCountBodySearchParamsJobStatusType0
  from ..models.people_search_count_body_search_params_country_3_letter_code_type_0 import PeopleSearchCountBodySearchParamsCountry3LetterCodeType0
  from ..models.people_search_count_body_search_params_job_status_type_2 import PeopleSearchCountBodySearchParamsJobStatusType2
  from ..models.people_search_count_body_search_params_time_zone_type_0 import PeopleSearchCountBodySearchParamsTimeZoneType0
  from ..models.people_search_count_body_search_params_company_match_mode_type_1 import PeopleSearchCountBodySearchParamsCompanyMatchModeType1
  from ..models.people_search_count_body_search_params_languages_type_0 import PeopleSearchCountBodySearchParamsLanguagesType0
  from ..models.people_search_count_body_search_params_started_in_role_type_1 import PeopleSearchCountBodySearchParamsStartedInRoleType1
  from ..models.people_search_count_body_search_params_fuzzy_name_type_0 import PeopleSearchCountBodySearchParamsFuzzyNameType0
  from ..models.people_search_count_body_search_params_company_match_mode_type_0 import PeopleSearchCountBodySearchParamsCompanyMatchModeType0
  from ..models.people_search_count_body_search_params_job_status_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1
  from ..models.people_search_count_body_search_params_past_jobs_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0
  from ..models.people_search_count_body_search_params_stealth_v2_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type0
  from ..models.people_search_count_body_search_params_job_title_v3_type_0 import PeopleSearchCountBodySearchParamsJobTitleV3Type0
  from ..models.people_search_count_body_search_params_state_type_0 import PeopleSearchCountBodySearchParamsStateType0
  from ..models.people_search_count_body_search_params_started_at_company_type_1 import PeopleSearchCountBodySearchParamsStartedAtCompanyType1
  from ..models.people_search_count_body_search_params_tags_type_0 import PeopleSearchCountBodySearchParamsTagsType0
  from ..models.people_search_count_body_search_params_exact_profile_type_0 import PeopleSearchCountBodySearchParamsExactProfileType0
  from ..models.people_search_count_body_search_params_num_followers_type_0 import PeopleSearchCountBodySearchParamsNumFollowersType0
  from ..models.people_search_count_body_search_params_num_connections_type_0 import PeopleSearchCountBodySearchParamsNumConnectionsType0
  from ..models.people_search_count_body_search_params_location_type_0 import PeopleSearchCountBodySearchParamsLocationType0
  from ..models.people_search_count_body_search_params_job_title_v2_type_0 import PeopleSearchCountBodySearchParamsJobTitleV2Type0





T = TypeVar("T", bound="PeopleSearchCountBodySearchParams")



@_attrs_define
class PeopleSearchCountBodySearchParams:
    """ Search parameters for people search.

        Attributes:
            country_3_letter_code (Union['PeopleSearchCountBodySearchParamsCountry3LetterCodeType0', None, Unset]):
            num_connections (Union['PeopleSearchCountBodySearchParamsNumConnectionsType0', None, Unset]):
            num_followers (Union['PeopleSearchCountBodySearchParamsNumFollowersType0', None, Unset]):
            approx_age (Union['PeopleSearchCountBodySearchParamsApproxAgeType0', None, Unset]):
            keywords (Union['PeopleSearchCountBodySearchParamsKeywordsType0', None, Unset]):
            keyword_search_options (Union['PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0', None, Unset]):
            job_title_v2 (Union['PeopleSearchCountBodySearchParamsJobTitleV2Type0', None, Unset]):
            exact_profile (Union['PeopleSearchCountBodySearchParamsExactProfileType0', None, Unset]):
            started_in_role (Union['PeopleSearchCountBodySearchParamsStartedInRoleType0',
                'PeopleSearchCountBodySearchParamsStartedInRoleType1', None, Unset]):
            started_at_company (Union['PeopleSearchCountBodySearchParamsStartedAtCompanyType0',
                'PeopleSearchCountBodySearchParamsStartedAtCompanyType1', None, Unset]):
            location (Union['PeopleSearchCountBodySearchParamsLocationType0', None, Unset]):
            past_jobs (Union['PeopleSearchCountBodySearchParamsPastJobsType0', None, Unset]):
            languages (Union['PeopleSearchCountBodySearchParamsLanguagesType0', None, Unset]):
            left_stealth_at (Union['PeopleSearchCountBodySearchParamsLeftStealthAtType0',
                'PeopleSearchCountBodySearchParamsLeftStealthAtType1', None, Unset]):
            is_in_stealth (Union[None, Unset, bool]):
            stealth_v2 (Union['PeopleSearchCountBodySearchParamsStealthV2Type0',
                'PeopleSearchCountBodySearchParamsStealthV2Type1', None, Unset]):
            job_status (Union['PeopleSearchCountBodySearchParamsJobStatusType0',
                'PeopleSearchCountBodySearchParamsJobStatusType1', 'PeopleSearchCountBodySearchParamsJobStatusType2', None,
                Unset]):
            time_zone (Union['PeopleSearchCountBodySearchParamsTimeZoneType0', None, Unset]):
            past_job_text (Union['PeopleSearchCountBodySearchParamsPastJobTextType0', None, Unset]):
            fuzzy_name (Union['PeopleSearchCountBodySearchParamsFuzzyNameType0', None, Unset]):
            company_match_mode (Union['PeopleSearchCountBodySearchParamsCompanyMatchModeType0',
                'PeopleSearchCountBodySearchParamsCompanyMatchModeType1', None, Unset]):
            years_of_experience (Union['PeopleSearchCountBodySearchParamsYearsOfExperienceType0', None, Unset]):
            job_title_v3 (Union['PeopleSearchCountBodySearchParamsJobTitleV3Type0', None, Unset]):
            has_profile_picture (Union[None, Unset, bool]):
            state (Union['PeopleSearchCountBodySearchParamsStateType0', None, Unset]):
            get_detailed_education (Union[None, Unset, bool]): Whether to include deep details about each educational item,
                like the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This
                slows down the API call, so only enable this if you need it. Default: False.
            get_detailed_work_experience (Union[None, Unset, bool]): Whether to include deep details about each work
                experience item, like the company's LinkedIn URL, website, location, etc. That'll be put in the
                detailedWorkExperience array. This slows down the API call, so only enable this if you need it. Default: False.
            tags (Union['PeopleSearchCountBodySearchParamsTagsType0', None, Unset]):
            education (Union['PeopleSearchCountBodySearchParamsEducationType0', None, Unset]):
     """

    country_3_letter_code: Union['PeopleSearchCountBodySearchParamsCountry3LetterCodeType0', None, Unset] = UNSET
    num_connections: Union['PeopleSearchCountBodySearchParamsNumConnectionsType0', None, Unset] = UNSET
    num_followers: Union['PeopleSearchCountBodySearchParamsNumFollowersType0', None, Unset] = UNSET
    approx_age: Union['PeopleSearchCountBodySearchParamsApproxAgeType0', None, Unset] = UNSET
    keywords: Union['PeopleSearchCountBodySearchParamsKeywordsType0', None, Unset] = UNSET
    keyword_search_options: Union['PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0', None, Unset] = UNSET
    job_title_v2: Union['PeopleSearchCountBodySearchParamsJobTitleV2Type0', None, Unset] = UNSET
    exact_profile: Union['PeopleSearchCountBodySearchParamsExactProfileType0', None, Unset] = UNSET
    started_in_role: Union['PeopleSearchCountBodySearchParamsStartedInRoleType0', 'PeopleSearchCountBodySearchParamsStartedInRoleType1', None, Unset] = UNSET
    started_at_company: Union['PeopleSearchCountBodySearchParamsStartedAtCompanyType0', 'PeopleSearchCountBodySearchParamsStartedAtCompanyType1', None, Unset] = UNSET
    location: Union['PeopleSearchCountBodySearchParamsLocationType0', None, Unset] = UNSET
    past_jobs: Union['PeopleSearchCountBodySearchParamsPastJobsType0', None, Unset] = UNSET
    languages: Union['PeopleSearchCountBodySearchParamsLanguagesType0', None, Unset] = UNSET
    left_stealth_at: Union['PeopleSearchCountBodySearchParamsLeftStealthAtType0', 'PeopleSearchCountBodySearchParamsLeftStealthAtType1', None, Unset] = UNSET
    is_in_stealth: Union[None, Unset, bool] = UNSET
    stealth_v2: Union['PeopleSearchCountBodySearchParamsStealthV2Type0', 'PeopleSearchCountBodySearchParamsStealthV2Type1', None, Unset] = UNSET
    job_status: Union['PeopleSearchCountBodySearchParamsJobStatusType0', 'PeopleSearchCountBodySearchParamsJobStatusType1', 'PeopleSearchCountBodySearchParamsJobStatusType2', None, Unset] = UNSET
    time_zone: Union['PeopleSearchCountBodySearchParamsTimeZoneType0', None, Unset] = UNSET
    past_job_text: Union['PeopleSearchCountBodySearchParamsPastJobTextType0', None, Unset] = UNSET
    fuzzy_name: Union['PeopleSearchCountBodySearchParamsFuzzyNameType0', None, Unset] = UNSET
    company_match_mode: Union['PeopleSearchCountBodySearchParamsCompanyMatchModeType0', 'PeopleSearchCountBodySearchParamsCompanyMatchModeType1', None, Unset] = UNSET
    years_of_experience: Union['PeopleSearchCountBodySearchParamsYearsOfExperienceType0', None, Unset] = UNSET
    job_title_v3: Union['PeopleSearchCountBodySearchParamsJobTitleV3Type0', None, Unset] = UNSET
    has_profile_picture: Union[None, Unset, bool] = UNSET
    state: Union['PeopleSearchCountBodySearchParamsStateType0', None, Unset] = UNSET
    get_detailed_education: Union[None, Unset, bool] = False
    get_detailed_work_experience: Union[None, Unset, bool] = False
    tags: Union['PeopleSearchCountBodySearchParamsTagsType0', None, Unset] = UNSET
    education: Union['PeopleSearchCountBodySearchParamsEducationType0', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_approx_age_type_0 import PeopleSearchCountBodySearchParamsApproxAgeType0
        from ..models.people_search_count_body_search_params_keywords_type_0 import PeopleSearchCountBodySearchParamsKeywordsType0
        from ..models.people_search_count_body_search_params_started_in_role_type_0 import PeopleSearchCountBodySearchParamsStartedInRoleType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1
        from ..models.people_search_count_body_search_params_started_at_company_type_0 import PeopleSearchCountBodySearchParamsStartedAtCompanyType0
        from ..models.people_search_count_body_search_params_past_job_text_type_0 import PeopleSearchCountBodySearchParamsPastJobTextType0
        from ..models.people_search_count_body_search_params_years_of_experience_type_0 import PeopleSearchCountBodySearchParamsYearsOfExperienceType0
        from ..models.people_search_count_body_search_params_education_type_0 import PeopleSearchCountBodySearchParamsEducationType0
        from ..models.people_search_count_body_search_params_left_stealth_at_type_1 import PeopleSearchCountBodySearchParamsLeftStealthAtType1
        from ..models.people_search_count_body_search_params_keyword_search_options_type_0 import PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0
        from ..models.people_search_count_body_search_params_left_stealth_at_type_0 import PeopleSearchCountBodySearchParamsLeftStealthAtType0
        from ..models.people_search_count_body_search_params_job_status_type_0 import PeopleSearchCountBodySearchParamsJobStatusType0
        from ..models.people_search_count_body_search_params_country_3_letter_code_type_0 import PeopleSearchCountBodySearchParamsCountry3LetterCodeType0
        from ..models.people_search_count_body_search_params_job_status_type_2 import PeopleSearchCountBodySearchParamsJobStatusType2
        from ..models.people_search_count_body_search_params_time_zone_type_0 import PeopleSearchCountBodySearchParamsTimeZoneType0
        from ..models.people_search_count_body_search_params_company_match_mode_type_1 import PeopleSearchCountBodySearchParamsCompanyMatchModeType1
        from ..models.people_search_count_body_search_params_languages_type_0 import PeopleSearchCountBodySearchParamsLanguagesType0
        from ..models.people_search_count_body_search_params_started_in_role_type_1 import PeopleSearchCountBodySearchParamsStartedInRoleType1
        from ..models.people_search_count_body_search_params_fuzzy_name_type_0 import PeopleSearchCountBodySearchParamsFuzzyNameType0
        from ..models.people_search_count_body_search_params_company_match_mode_type_0 import PeopleSearchCountBodySearchParamsCompanyMatchModeType0
        from ..models.people_search_count_body_search_params_job_status_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1
        from ..models.people_search_count_body_search_params_past_jobs_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type0
        from ..models.people_search_count_body_search_params_job_title_v3_type_0 import PeopleSearchCountBodySearchParamsJobTitleV3Type0
        from ..models.people_search_count_body_search_params_state_type_0 import PeopleSearchCountBodySearchParamsStateType0
        from ..models.people_search_count_body_search_params_started_at_company_type_1 import PeopleSearchCountBodySearchParamsStartedAtCompanyType1
        from ..models.people_search_count_body_search_params_tags_type_0 import PeopleSearchCountBodySearchParamsTagsType0
        from ..models.people_search_count_body_search_params_exact_profile_type_0 import PeopleSearchCountBodySearchParamsExactProfileType0
        from ..models.people_search_count_body_search_params_num_followers_type_0 import PeopleSearchCountBodySearchParamsNumFollowersType0
        from ..models.people_search_count_body_search_params_num_connections_type_0 import PeopleSearchCountBodySearchParamsNumConnectionsType0
        from ..models.people_search_count_body_search_params_location_type_0 import PeopleSearchCountBodySearchParamsLocationType0
        from ..models.people_search_count_body_search_params_job_title_v2_type_0 import PeopleSearchCountBodySearchParamsJobTitleV2Type0
        country_3_letter_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(self.country_3_letter_code, PeopleSearchCountBodySearchParamsCountry3LetterCodeType0):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        num_connections: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(self.num_connections, PeopleSearchCountBodySearchParamsNumConnectionsType0):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(self.num_followers, PeopleSearchCountBodySearchParamsNumFollowersType0):
            num_followers = self.num_followers.to_dict()
        else:
            num_followers = self.num_followers

        approx_age: Union[None, Unset, dict[str, Any]]
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, PeopleSearchCountBodySearchParamsApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, PeopleSearchCountBodySearchParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(self.keyword_search_options, PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        job_title_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_title_v2, Unset):
            job_title_v2 = UNSET
        elif isinstance(self.job_title_v2, PeopleSearchCountBodySearchParamsJobTitleV2Type0):
            job_title_v2 = self.job_title_v2.to_dict()
        else:
            job_title_v2 = self.job_title_v2

        exact_profile: Union[None, Unset, dict[str, Any]]
        if isinstance(self.exact_profile, Unset):
            exact_profile = UNSET
        elif isinstance(self.exact_profile, PeopleSearchCountBodySearchParamsExactProfileType0):
            exact_profile = self.exact_profile.to_dict()
        else:
            exact_profile = self.exact_profile

        started_in_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(self.started_in_role, PeopleSearchCountBodySearchParamsStartedInRoleType0):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(self.started_in_role, PeopleSearchCountBodySearchParamsStartedInRoleType1):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(self.started_at_company, PeopleSearchCountBodySearchParamsStartedAtCompanyType0):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(self.started_at_company, PeopleSearchCountBodySearchParamsStartedAtCompanyType1):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, PeopleSearchCountBodySearchParamsLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        past_jobs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, PeopleSearchCountBodySearchParamsPastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        languages: Union[None, Unset, dict[str, Any]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, PeopleSearchCountBodySearchParamsLanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        left_stealth_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.left_stealth_at, Unset):
            left_stealth_at = UNSET
        elif isinstance(self.left_stealth_at, PeopleSearchCountBodySearchParamsLeftStealthAtType0):
            left_stealth_at = self.left_stealth_at.to_dict()
        elif isinstance(self.left_stealth_at, PeopleSearchCountBodySearchParamsLeftStealthAtType1):
            left_stealth_at = self.left_stealth_at.to_dict()
        else:
            left_stealth_at = self.left_stealth_at

        is_in_stealth: Union[None, Unset, bool]
        if isinstance(self.is_in_stealth, Unset):
            is_in_stealth = UNSET
        else:
            is_in_stealth = self.is_in_stealth

        stealth_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(self.stealth_v2, PeopleSearchCountBodySearchParamsStealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, PeopleSearchCountBodySearchParamsStealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        job_status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, PeopleSearchCountBodySearchParamsJobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, PeopleSearchCountBodySearchParamsJobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, PeopleSearchCountBodySearchParamsJobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        time_zone: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, PeopleSearchCountBodySearchParamsTimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        past_job_text: Union[None, Unset, dict[str, Any]]
        if isinstance(self.past_job_text, Unset):
            past_job_text = UNSET
        elif isinstance(self.past_job_text, PeopleSearchCountBodySearchParamsPastJobTextType0):
            past_job_text = self.past_job_text.to_dict()
        else:
            past_job_text = self.past_job_text

        fuzzy_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, PeopleSearchCountBodySearchParamsFuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        company_match_mode: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_match_mode, Unset):
            company_match_mode = UNSET
        elif isinstance(self.company_match_mode, PeopleSearchCountBodySearchParamsCompanyMatchModeType0):
            company_match_mode = self.company_match_mode.to_dict()
        elif isinstance(self.company_match_mode, PeopleSearchCountBodySearchParamsCompanyMatchModeType1):
            company_match_mode = self.company_match_mode.to_dict()
        else:
            company_match_mode = self.company_match_mode

        years_of_experience: Union[None, Unset, dict[str, Any]]
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, PeopleSearchCountBodySearchParamsYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        job_title_v3: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, PeopleSearchCountBodySearchParamsJobTitleV3Type0):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        has_profile_picture: Union[None, Unset, bool]
        if isinstance(self.has_profile_picture, Unset):
            has_profile_picture = UNSET
        else:
            has_profile_picture = self.has_profile_picture

        state: Union[None, Unset, dict[str, Any]]
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, PeopleSearchCountBodySearchParamsStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        get_detailed_education: Union[None, Unset, bool]
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: Union[None, Unset, bool]
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        tags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, PeopleSearchCountBodySearchParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        education: Union[None, Unset, dict[str, Any]]
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, PeopleSearchCountBodySearchParamsEducationType0):
            education = self.education.to_dict()
        else:
            education = self.education


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if country_3_letter_code is not UNSET:
            field_dict["country3LetterCode"] = country_3_letter_code
        if num_connections is not UNSET:
            field_dict["numConnections"] = num_connections
        if num_followers is not UNSET:
            field_dict["numFollowers"] = num_followers
        if approx_age is not UNSET:
            field_dict["approxAge"] = approx_age
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if keyword_search_options is not UNSET:
            field_dict["keywordSearchOptions"] = keyword_search_options
        if job_title_v2 is not UNSET:
            field_dict["jobTitleV2"] = job_title_v2
        if exact_profile is not UNSET:
            field_dict["exactProfile"] = exact_profile
        if started_in_role is not UNSET:
            field_dict["startedInRole"] = started_in_role
        if started_at_company is not UNSET:
            field_dict["startedAtCompany"] = started_at_company
        if location is not UNSET:
            field_dict["location"] = location
        if past_jobs is not UNSET:
            field_dict["pastJobs"] = past_jobs
        if languages is not UNSET:
            field_dict["languages"] = languages
        if left_stealth_at is not UNSET:
            field_dict["leftStealthAt"] = left_stealth_at
        if is_in_stealth is not UNSET:
            field_dict["isInStealth"] = is_in_stealth
        if stealth_v2 is not UNSET:
            field_dict["stealthV2"] = stealth_v2
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if past_job_text is not UNSET:
            field_dict["pastJobText"] = past_job_text
        if fuzzy_name is not UNSET:
            field_dict["fuzzyName"] = fuzzy_name
        if company_match_mode is not UNSET:
            field_dict["companyMatchMode"] = company_match_mode
        if years_of_experience is not UNSET:
            field_dict["yearsOfExperience"] = years_of_experience
        if job_title_v3 is not UNSET:
            field_dict["jobTitleV3"] = job_title_v3
        if has_profile_picture is not UNSET:
            field_dict["hasProfilePicture"] = has_profile_picture
        if state is not UNSET:
            field_dict["state"] = state
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience
        if tags is not UNSET:
            field_dict["tags"] = tags
        if education is not UNSET:
            field_dict["education"] = education

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_approx_age_type_0 import PeopleSearchCountBodySearchParamsApproxAgeType0
        from ..models.people_search_count_body_search_params_keywords_type_0 import PeopleSearchCountBodySearchParamsKeywordsType0
        from ..models.people_search_count_body_search_params_started_in_role_type_0 import PeopleSearchCountBodySearchParamsStartedInRoleType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1
        from ..models.people_search_count_body_search_params_started_at_company_type_0 import PeopleSearchCountBodySearchParamsStartedAtCompanyType0
        from ..models.people_search_count_body_search_params_past_job_text_type_0 import PeopleSearchCountBodySearchParamsPastJobTextType0
        from ..models.people_search_count_body_search_params_years_of_experience_type_0 import PeopleSearchCountBodySearchParamsYearsOfExperienceType0
        from ..models.people_search_count_body_search_params_education_type_0 import PeopleSearchCountBodySearchParamsEducationType0
        from ..models.people_search_count_body_search_params_left_stealth_at_type_1 import PeopleSearchCountBodySearchParamsLeftStealthAtType1
        from ..models.people_search_count_body_search_params_keyword_search_options_type_0 import PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0
        from ..models.people_search_count_body_search_params_left_stealth_at_type_0 import PeopleSearchCountBodySearchParamsLeftStealthAtType0
        from ..models.people_search_count_body_search_params_job_status_type_0 import PeopleSearchCountBodySearchParamsJobStatusType0
        from ..models.people_search_count_body_search_params_country_3_letter_code_type_0 import PeopleSearchCountBodySearchParamsCountry3LetterCodeType0
        from ..models.people_search_count_body_search_params_job_status_type_2 import PeopleSearchCountBodySearchParamsJobStatusType2
        from ..models.people_search_count_body_search_params_time_zone_type_0 import PeopleSearchCountBodySearchParamsTimeZoneType0
        from ..models.people_search_count_body_search_params_company_match_mode_type_1 import PeopleSearchCountBodySearchParamsCompanyMatchModeType1
        from ..models.people_search_count_body_search_params_languages_type_0 import PeopleSearchCountBodySearchParamsLanguagesType0
        from ..models.people_search_count_body_search_params_started_in_role_type_1 import PeopleSearchCountBodySearchParamsStartedInRoleType1
        from ..models.people_search_count_body_search_params_fuzzy_name_type_0 import PeopleSearchCountBodySearchParamsFuzzyNameType0
        from ..models.people_search_count_body_search_params_company_match_mode_type_0 import PeopleSearchCountBodySearchParamsCompanyMatchModeType0
        from ..models.people_search_count_body_search_params_job_status_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1
        from ..models.people_search_count_body_search_params_past_jobs_type_0 import PeopleSearchCountBodySearchParamsPastJobsType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type0
        from ..models.people_search_count_body_search_params_job_title_v3_type_0 import PeopleSearchCountBodySearchParamsJobTitleV3Type0
        from ..models.people_search_count_body_search_params_state_type_0 import PeopleSearchCountBodySearchParamsStateType0
        from ..models.people_search_count_body_search_params_started_at_company_type_1 import PeopleSearchCountBodySearchParamsStartedAtCompanyType1
        from ..models.people_search_count_body_search_params_tags_type_0 import PeopleSearchCountBodySearchParamsTagsType0
        from ..models.people_search_count_body_search_params_exact_profile_type_0 import PeopleSearchCountBodySearchParamsExactProfileType0
        from ..models.people_search_count_body_search_params_num_followers_type_0 import PeopleSearchCountBodySearchParamsNumFollowersType0
        from ..models.people_search_count_body_search_params_num_connections_type_0 import PeopleSearchCountBodySearchParamsNumConnectionsType0
        from ..models.people_search_count_body_search_params_location_type_0 import PeopleSearchCountBodySearchParamsLocationType0
        from ..models.people_search_count_body_search_params_job_title_v2_type_0 import PeopleSearchCountBodySearchParamsJobTitleV2Type0
        d = dict(src_dict)
        def _parse_country_3_letter_code(data: object) -> Union['PeopleSearchCountBodySearchParamsCountry3LetterCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = PeopleSearchCountBodySearchParamsCountry3LetterCodeType0.from_dict(data)



                return country_3_letter_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsCountry3LetterCodeType0', None, Unset], data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))


        def _parse_num_connections(data: object) -> Union['PeopleSearchCountBodySearchParamsNumConnectionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = PeopleSearchCountBodySearchParamsNumConnectionsType0.from_dict(data)



                return num_connections_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsNumConnectionsType0', None, Unset], data)

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))


        def _parse_num_followers(data: object) -> Union['PeopleSearchCountBodySearchParamsNumFollowersType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = PeopleSearchCountBodySearchParamsNumFollowersType0.from_dict(data)



                return num_followers_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsNumFollowersType0', None, Unset], data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))


        def _parse_approx_age(data: object) -> Union['PeopleSearchCountBodySearchParamsApproxAgeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = PeopleSearchCountBodySearchParamsApproxAgeType0.from_dict(data)



                return approx_age_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsApproxAgeType0', None, Unset], data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))


        def _parse_keywords(data: object) -> Union['PeopleSearchCountBodySearchParamsKeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PeopleSearchCountBodySearchParamsKeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsKeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_keyword_search_options(data: object) -> Union['PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0.from_dict(data)



                return keyword_search_options_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsKeywordSearchOptionsType0', None, Unset], data)

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))


        def _parse_job_title_v2(data: object) -> Union['PeopleSearchCountBodySearchParamsJobTitleV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v2_type_0 = PeopleSearchCountBodySearchParamsJobTitleV2Type0.from_dict(data)



                return job_title_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsJobTitleV2Type0', None, Unset], data)

        job_title_v2 = _parse_job_title_v2(d.pop("jobTitleV2", UNSET))


        def _parse_exact_profile(data: object) -> Union['PeopleSearchCountBodySearchParamsExactProfileType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_profile_type_0 = PeopleSearchCountBodySearchParamsExactProfileType0.from_dict(data)



                return exact_profile_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsExactProfileType0', None, Unset], data)

        exact_profile = _parse_exact_profile(d.pop("exactProfile", UNSET))


        def _parse_started_in_role(data: object) -> Union['PeopleSearchCountBodySearchParamsStartedInRoleType0', 'PeopleSearchCountBodySearchParamsStartedInRoleType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_0 = PeopleSearchCountBodySearchParamsStartedInRoleType0.from_dict(data)



                return started_in_role_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = PeopleSearchCountBodySearchParamsStartedInRoleType1.from_dict(data)



                return started_in_role_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsStartedInRoleType0', 'PeopleSearchCountBodySearchParamsStartedInRoleType1', None, Unset], data)

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))


        def _parse_started_at_company(data: object) -> Union['PeopleSearchCountBodySearchParamsStartedAtCompanyType0', 'PeopleSearchCountBodySearchParamsStartedAtCompanyType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_0 = PeopleSearchCountBodySearchParamsStartedAtCompanyType0.from_dict(data)



                return started_at_company_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = PeopleSearchCountBodySearchParamsStartedAtCompanyType1.from_dict(data)



                return started_at_company_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsStartedAtCompanyType0', 'PeopleSearchCountBodySearchParamsStartedAtCompanyType1', None, Unset], data)

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))


        def _parse_location(data: object) -> Union['PeopleSearchCountBodySearchParamsLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = PeopleSearchCountBodySearchParamsLocationType0.from_dict(data)



                return location_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsLocationType0', None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_past_jobs(data: object) -> Union['PeopleSearchCountBodySearchParamsPastJobsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = PeopleSearchCountBodySearchParamsPastJobsType0.from_dict(data)



                return past_jobs_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsPastJobsType0', None, Unset], data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))


        def _parse_languages(data: object) -> Union['PeopleSearchCountBodySearchParamsLanguagesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = PeopleSearchCountBodySearchParamsLanguagesType0.from_dict(data)



                return languages_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsLanguagesType0', None, Unset], data)

        languages = _parse_languages(d.pop("languages", UNSET))


        def _parse_left_stealth_at(data: object) -> Union['PeopleSearchCountBodySearchParamsLeftStealthAtType0', 'PeopleSearchCountBodySearchParamsLeftStealthAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_0 = PeopleSearchCountBodySearchParamsLeftStealthAtType0.from_dict(data)



                return left_stealth_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_1 = PeopleSearchCountBodySearchParamsLeftStealthAtType1.from_dict(data)



                return left_stealth_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsLeftStealthAtType0', 'PeopleSearchCountBodySearchParamsLeftStealthAtType1', None, Unset], data)

        left_stealth_at = _parse_left_stealth_at(d.pop("leftStealthAt", UNSET))


        def _parse_is_in_stealth(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_in_stealth = _parse_is_in_stealth(d.pop("isInStealth", UNSET))


        def _parse_stealth_v2(data: object) -> Union['PeopleSearchCountBodySearchParamsStealthV2Type0', 'PeopleSearchCountBodySearchParamsStealthV2Type1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = PeopleSearchCountBodySearchParamsStealthV2Type0.from_dict(data)



                return stealth_v2_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = PeopleSearchCountBodySearchParamsStealthV2Type1.from_dict(data)



                return stealth_v2_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsStealthV2Type0', 'PeopleSearchCountBodySearchParamsStealthV2Type1', None, Unset], data)

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))


        def _parse_job_status(data: object) -> Union['PeopleSearchCountBodySearchParamsJobStatusType0', 'PeopleSearchCountBodySearchParamsJobStatusType1', 'PeopleSearchCountBodySearchParamsJobStatusType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = PeopleSearchCountBodySearchParamsJobStatusType0.from_dict(data)



                return job_status_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = PeopleSearchCountBodySearchParamsJobStatusType1.from_dict(data)



                return job_status_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = PeopleSearchCountBodySearchParamsJobStatusType2.from_dict(data)



                return job_status_type_2
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsJobStatusType0', 'PeopleSearchCountBodySearchParamsJobStatusType1', 'PeopleSearchCountBodySearchParamsJobStatusType2', None, Unset], data)

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))


        def _parse_time_zone(data: object) -> Union['PeopleSearchCountBodySearchParamsTimeZoneType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = PeopleSearchCountBodySearchParamsTimeZoneType0.from_dict(data)



                return time_zone_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsTimeZoneType0', None, Unset], data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))


        def _parse_past_job_text(data: object) -> Union['PeopleSearchCountBodySearchParamsPastJobTextType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_job_text_type_0 = PeopleSearchCountBodySearchParamsPastJobTextType0.from_dict(data)



                return past_job_text_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsPastJobTextType0', None, Unset], data)

        past_job_text = _parse_past_job_text(d.pop("pastJobText", UNSET))


        def _parse_fuzzy_name(data: object) -> Union['PeopleSearchCountBodySearchParamsFuzzyNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = PeopleSearchCountBodySearchParamsFuzzyNameType0.from_dict(data)



                return fuzzy_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsFuzzyNameType0', None, Unset], data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))


        def _parse_company_match_mode(data: object) -> Union['PeopleSearchCountBodySearchParamsCompanyMatchModeType0', 'PeopleSearchCountBodySearchParamsCompanyMatchModeType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_0 = PeopleSearchCountBodySearchParamsCompanyMatchModeType0.from_dict(data)



                return company_match_mode_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_1 = PeopleSearchCountBodySearchParamsCompanyMatchModeType1.from_dict(data)



                return company_match_mode_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsCompanyMatchModeType0', 'PeopleSearchCountBodySearchParamsCompanyMatchModeType1', None, Unset], data)

        company_match_mode = _parse_company_match_mode(d.pop("companyMatchMode", UNSET))


        def _parse_years_of_experience(data: object) -> Union['PeopleSearchCountBodySearchParamsYearsOfExperienceType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = PeopleSearchCountBodySearchParamsYearsOfExperienceType0.from_dict(data)



                return years_of_experience_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsYearsOfExperienceType0', None, Unset], data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))


        def _parse_job_title_v3(data: object) -> Union['PeopleSearchCountBodySearchParamsJobTitleV3Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = PeopleSearchCountBodySearchParamsJobTitleV3Type0.from_dict(data)



                return job_title_v3_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsJobTitleV3Type0', None, Unset], data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))


        def _parse_has_profile_picture(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_profile_picture = _parse_has_profile_picture(d.pop("hasProfilePicture", UNSET))


        def _parse_state(data: object) -> Union['PeopleSearchCountBodySearchParamsStateType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = PeopleSearchCountBodySearchParamsStateType0.from_dict(data)



                return state_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsStateType0', None, Unset], data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_get_detailed_education(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))


        def _parse_get_detailed_work_experience(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))


        def _parse_tags(data: object) -> Union['PeopleSearchCountBodySearchParamsTagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = PeopleSearchCountBodySearchParamsTagsType0.from_dict(data)



                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsTagsType0', None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_education(data: object) -> Union['PeopleSearchCountBodySearchParamsEducationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = PeopleSearchCountBodySearchParamsEducationType0.from_dict(data)



                return education_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsEducationType0', None, Unset], data)

        education = _parse_education(d.pop("education", UNSET))


        people_search_count_body_search_params = cls(
            country_3_letter_code=country_3_letter_code,
            num_connections=num_connections,
            num_followers=num_followers,
            approx_age=approx_age,
            keywords=keywords,
            keyword_search_options=keyword_search_options,
            job_title_v2=job_title_v2,
            exact_profile=exact_profile,
            started_in_role=started_in_role,
            started_at_company=started_at_company,
            location=location,
            past_jobs=past_jobs,
            languages=languages,
            left_stealth_at=left_stealth_at,
            is_in_stealth=is_in_stealth,
            stealth_v2=stealth_v2,
            job_status=job_status,
            time_zone=time_zone,
            past_job_text=past_job_text,
            fuzzy_name=fuzzy_name,
            company_match_mode=company_match_mode,
            years_of_experience=years_of_experience,
            job_title_v3=job_title_v3,
            has_profile_picture=has_profile_picture,
            state=state,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
            tags=tags,
            education=education,
        )

        return people_search_count_body_search_params

