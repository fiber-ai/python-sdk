from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_body_search_params_approx_age_type_0 import PeopleSearchBodySearchParamsApproxAgeType0
    from ..models.people_search_body_search_params_company_match_mode_type_0 import (
        PeopleSearchBodySearchParamsCompanyMatchModeType0,
    )
    from ..models.people_search_body_search_params_company_match_mode_type_1 import (
        PeopleSearchBodySearchParamsCompanyMatchModeType1,
    )
    from ..models.people_search_body_search_params_country_3_letter_code_type_0 import (
        PeopleSearchBodySearchParamsCountry3LetterCodeType0,
    )
    from ..models.people_search_body_search_params_education_type_0 import PeopleSearchBodySearchParamsEducationType0
    from ..models.people_search_body_search_params_exact_profile_type_0 import (
        PeopleSearchBodySearchParamsExactProfileType0,
    )
    from ..models.people_search_body_search_params_fuzzy_name_type_0 import PeopleSearchBodySearchParamsFuzzyNameType0
    from ..models.people_search_body_search_params_job_status_type_0 import PeopleSearchBodySearchParamsJobStatusType0
    from ..models.people_search_body_search_params_job_status_type_1 import PeopleSearchBodySearchParamsJobStatusType1
    from ..models.people_search_body_search_params_job_status_type_2 import PeopleSearchBodySearchParamsJobStatusType2
    from ..models.people_search_body_search_params_job_title_v2_type_0 import (
        PeopleSearchBodySearchParamsJobTitleV2Type0,
    )
    from ..models.people_search_body_search_params_job_title_v3_type_0 import (
        PeopleSearchBodySearchParamsJobTitleV3Type0,
    )
    from ..models.people_search_body_search_params_keyword_search_options_type_0 import (
        PeopleSearchBodySearchParamsKeywordSearchOptionsType0,
    )
    from ..models.people_search_body_search_params_keywords_type_0 import PeopleSearchBodySearchParamsKeywordsType0
    from ..models.people_search_body_search_params_languages_type_0 import PeopleSearchBodySearchParamsLanguagesType0
    from ..models.people_search_body_search_params_left_stealth_at_type_0 import (
        PeopleSearchBodySearchParamsLeftStealthAtType0,
    )
    from ..models.people_search_body_search_params_left_stealth_at_type_1 import (
        PeopleSearchBodySearchParamsLeftStealthAtType1,
    )
    from ..models.people_search_body_search_params_location_type_0 import PeopleSearchBodySearchParamsLocationType0
    from ..models.people_search_body_search_params_num_connections_type_0 import (
        PeopleSearchBodySearchParamsNumConnectionsType0,
    )
    from ..models.people_search_body_search_params_num_followers_type_0 import (
        PeopleSearchBodySearchParamsNumFollowersType0,
    )
    from ..models.people_search_body_search_params_past_job_text_type_0 import (
        PeopleSearchBodySearchParamsPastJobTextType0,
    )
    from ..models.people_search_body_search_params_past_jobs_type_0 import PeopleSearchBodySearchParamsPastJobsType0
    from ..models.people_search_body_search_params_started_at_company_type_0 import (
        PeopleSearchBodySearchParamsStartedAtCompanyType0,
    )
    from ..models.people_search_body_search_params_started_at_company_type_1 import (
        PeopleSearchBodySearchParamsStartedAtCompanyType1,
    )
    from ..models.people_search_body_search_params_started_in_role_type_0 import (
        PeopleSearchBodySearchParamsStartedInRoleType0,
    )
    from ..models.people_search_body_search_params_started_in_role_type_1 import (
        PeopleSearchBodySearchParamsStartedInRoleType1,
    )
    from ..models.people_search_body_search_params_state_type_0 import PeopleSearchBodySearchParamsStateType0
    from ..models.people_search_body_search_params_stealth_v2_type_0 import PeopleSearchBodySearchParamsStealthV2Type0
    from ..models.people_search_body_search_params_stealth_v2_type_1 import PeopleSearchBodySearchParamsStealthV2Type1
    from ..models.people_search_body_search_params_tags_type_0 import PeopleSearchBodySearchParamsTagsType0
    from ..models.people_search_body_search_params_time_zone_type_0 import PeopleSearchBodySearchParamsTimeZoneType0
    from ..models.people_search_body_search_params_years_of_experience_type_0 import (
        PeopleSearchBodySearchParamsYearsOfExperienceType0,
    )


T = TypeVar("T", bound="PeopleSearchBodySearchParams")


@_attrs_define
class PeopleSearchBodySearchParams:
    """Search parameters for people search.

    Attributes:
        country_3_letter_code (None | PeopleSearchBodySearchParamsCountry3LetterCodeType0 | Unset):
        num_connections (None | PeopleSearchBodySearchParamsNumConnectionsType0 | Unset):
        num_followers (None | PeopleSearchBodySearchParamsNumFollowersType0 | Unset):
        approx_age (None | PeopleSearchBodySearchParamsApproxAgeType0 | Unset):
        keywords (None | PeopleSearchBodySearchParamsKeywordsType0 | Unset):
        keyword_search_options (None | PeopleSearchBodySearchParamsKeywordSearchOptionsType0 | Unset):
        job_title_v2 (None | PeopleSearchBodySearchParamsJobTitleV2Type0 | Unset):
        exact_profile (None | PeopleSearchBodySearchParamsExactProfileType0 | Unset):
        started_in_role (None | PeopleSearchBodySearchParamsStartedInRoleType0 |
            PeopleSearchBodySearchParamsStartedInRoleType1 | Unset):
        started_at_company (None | PeopleSearchBodySearchParamsStartedAtCompanyType0 |
            PeopleSearchBodySearchParamsStartedAtCompanyType1 | Unset):
        location (None | PeopleSearchBodySearchParamsLocationType0 | Unset):
        past_jobs (None | PeopleSearchBodySearchParamsPastJobsType0 | Unset):
        languages (None | PeopleSearchBodySearchParamsLanguagesType0 | Unset):
        left_stealth_at (None | PeopleSearchBodySearchParamsLeftStealthAtType0 |
            PeopleSearchBodySearchParamsLeftStealthAtType1 | Unset):
        is_in_stealth (bool | None | Unset):
        stealth_v2 (None | PeopleSearchBodySearchParamsStealthV2Type0 | PeopleSearchBodySearchParamsStealthV2Type1 |
            Unset):
        job_status (None | PeopleSearchBodySearchParamsJobStatusType0 | PeopleSearchBodySearchParamsJobStatusType1 |
            PeopleSearchBodySearchParamsJobStatusType2 | Unset):
        time_zone (None | PeopleSearchBodySearchParamsTimeZoneType0 | Unset):
        past_job_text (None | PeopleSearchBodySearchParamsPastJobTextType0 | Unset):
        fuzzy_name (None | PeopleSearchBodySearchParamsFuzzyNameType0 | Unset):
        company_match_mode (None | PeopleSearchBodySearchParamsCompanyMatchModeType0 |
            PeopleSearchBodySearchParamsCompanyMatchModeType1 | Unset):
        years_of_experience (None | PeopleSearchBodySearchParamsYearsOfExperienceType0 | Unset):
        job_title_v3 (None | PeopleSearchBodySearchParamsJobTitleV3Type0 | Unset):
        has_profile_picture (bool | None | Unset):
        state (None | PeopleSearchBodySearchParamsStateType0 | Unset):
        get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
            the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
            down the API call, so only enable this if you need it. Default: False.
        get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
            item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
            array. This slows down the API call, so only enable this if you need it. Default: False.
        tags (None | PeopleSearchBodySearchParamsTagsType0 | Unset):
        education (None | PeopleSearchBodySearchParamsEducationType0 | Unset):
    """

    country_3_letter_code: None | PeopleSearchBodySearchParamsCountry3LetterCodeType0 | Unset = UNSET
    num_connections: None | PeopleSearchBodySearchParamsNumConnectionsType0 | Unset = UNSET
    num_followers: None | PeopleSearchBodySearchParamsNumFollowersType0 | Unset = UNSET
    approx_age: None | PeopleSearchBodySearchParamsApproxAgeType0 | Unset = UNSET
    keywords: None | PeopleSearchBodySearchParamsKeywordsType0 | Unset = UNSET
    keyword_search_options: None | PeopleSearchBodySearchParamsKeywordSearchOptionsType0 | Unset = UNSET
    job_title_v2: None | PeopleSearchBodySearchParamsJobTitleV2Type0 | Unset = UNSET
    exact_profile: None | PeopleSearchBodySearchParamsExactProfileType0 | Unset = UNSET
    started_in_role: (
        None | PeopleSearchBodySearchParamsStartedInRoleType0 | PeopleSearchBodySearchParamsStartedInRoleType1 | Unset
    ) = UNSET
    started_at_company: (
        None
        | PeopleSearchBodySearchParamsStartedAtCompanyType0
        | PeopleSearchBodySearchParamsStartedAtCompanyType1
        | Unset
    ) = UNSET
    location: None | PeopleSearchBodySearchParamsLocationType0 | Unset = UNSET
    past_jobs: None | PeopleSearchBodySearchParamsPastJobsType0 | Unset = UNSET
    languages: None | PeopleSearchBodySearchParamsLanguagesType0 | Unset = UNSET
    left_stealth_at: (
        None | PeopleSearchBodySearchParamsLeftStealthAtType0 | PeopleSearchBodySearchParamsLeftStealthAtType1 | Unset
    ) = UNSET
    is_in_stealth: bool | None | Unset = UNSET
    stealth_v2: (
        None | PeopleSearchBodySearchParamsStealthV2Type0 | PeopleSearchBodySearchParamsStealthV2Type1 | Unset
    ) = UNSET
    job_status: (
        None
        | PeopleSearchBodySearchParamsJobStatusType0
        | PeopleSearchBodySearchParamsJobStatusType1
        | PeopleSearchBodySearchParamsJobStatusType2
        | Unset
    ) = UNSET
    time_zone: None | PeopleSearchBodySearchParamsTimeZoneType0 | Unset = UNSET
    past_job_text: None | PeopleSearchBodySearchParamsPastJobTextType0 | Unset = UNSET
    fuzzy_name: None | PeopleSearchBodySearchParamsFuzzyNameType0 | Unset = UNSET
    company_match_mode: (
        None
        | PeopleSearchBodySearchParamsCompanyMatchModeType0
        | PeopleSearchBodySearchParamsCompanyMatchModeType1
        | Unset
    ) = UNSET
    years_of_experience: None | PeopleSearchBodySearchParamsYearsOfExperienceType0 | Unset = UNSET
    job_title_v3: None | PeopleSearchBodySearchParamsJobTitleV3Type0 | Unset = UNSET
    has_profile_picture: bool | None | Unset = UNSET
    state: None | PeopleSearchBodySearchParamsStateType0 | Unset = UNSET
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    tags: None | PeopleSearchBodySearchParamsTagsType0 | Unset = UNSET
    education: None | PeopleSearchBodySearchParamsEducationType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_approx_age_type_0 import (
            PeopleSearchBodySearchParamsApproxAgeType0,
        )
        from ..models.people_search_body_search_params_company_match_mode_type_0 import (
            PeopleSearchBodySearchParamsCompanyMatchModeType0,
        )
        from ..models.people_search_body_search_params_company_match_mode_type_1 import (
            PeopleSearchBodySearchParamsCompanyMatchModeType1,
        )
        from ..models.people_search_body_search_params_country_3_letter_code_type_0 import (
            PeopleSearchBodySearchParamsCountry3LetterCodeType0,
        )
        from ..models.people_search_body_search_params_education_type_0 import (
            PeopleSearchBodySearchParamsEducationType0,
        )
        from ..models.people_search_body_search_params_exact_profile_type_0 import (
            PeopleSearchBodySearchParamsExactProfileType0,
        )
        from ..models.people_search_body_search_params_fuzzy_name_type_0 import (
            PeopleSearchBodySearchParamsFuzzyNameType0,
        )
        from ..models.people_search_body_search_params_job_status_type_0 import (
            PeopleSearchBodySearchParamsJobStatusType0,
        )
        from ..models.people_search_body_search_params_job_status_type_1 import (
            PeopleSearchBodySearchParamsJobStatusType1,
        )
        from ..models.people_search_body_search_params_job_status_type_2 import (
            PeopleSearchBodySearchParamsJobStatusType2,
        )
        from ..models.people_search_body_search_params_job_title_v2_type_0 import (
            PeopleSearchBodySearchParamsJobTitleV2Type0,
        )
        from ..models.people_search_body_search_params_job_title_v3_type_0 import (
            PeopleSearchBodySearchParamsJobTitleV3Type0,
        )
        from ..models.people_search_body_search_params_keyword_search_options_type_0 import (
            PeopleSearchBodySearchParamsKeywordSearchOptionsType0,
        )
        from ..models.people_search_body_search_params_keywords_type_0 import PeopleSearchBodySearchParamsKeywordsType0
        from ..models.people_search_body_search_params_languages_type_0 import (
            PeopleSearchBodySearchParamsLanguagesType0,
        )
        from ..models.people_search_body_search_params_left_stealth_at_type_0 import (
            PeopleSearchBodySearchParamsLeftStealthAtType0,
        )
        from ..models.people_search_body_search_params_left_stealth_at_type_1 import (
            PeopleSearchBodySearchParamsLeftStealthAtType1,
        )
        from ..models.people_search_body_search_params_location_type_0 import PeopleSearchBodySearchParamsLocationType0
        from ..models.people_search_body_search_params_num_connections_type_0 import (
            PeopleSearchBodySearchParamsNumConnectionsType0,
        )
        from ..models.people_search_body_search_params_num_followers_type_0 import (
            PeopleSearchBodySearchParamsNumFollowersType0,
        )
        from ..models.people_search_body_search_params_past_job_text_type_0 import (
            PeopleSearchBodySearchParamsPastJobTextType0,
        )
        from ..models.people_search_body_search_params_past_jobs_type_0 import PeopleSearchBodySearchParamsPastJobsType0
        from ..models.people_search_body_search_params_started_at_company_type_0 import (
            PeopleSearchBodySearchParamsStartedAtCompanyType0,
        )
        from ..models.people_search_body_search_params_started_at_company_type_1 import (
            PeopleSearchBodySearchParamsStartedAtCompanyType1,
        )
        from ..models.people_search_body_search_params_started_in_role_type_0 import (
            PeopleSearchBodySearchParamsStartedInRoleType0,
        )
        from ..models.people_search_body_search_params_started_in_role_type_1 import (
            PeopleSearchBodySearchParamsStartedInRoleType1,
        )
        from ..models.people_search_body_search_params_state_type_0 import PeopleSearchBodySearchParamsStateType0
        from ..models.people_search_body_search_params_stealth_v2_type_0 import (
            PeopleSearchBodySearchParamsStealthV2Type0,
        )
        from ..models.people_search_body_search_params_stealth_v2_type_1 import (
            PeopleSearchBodySearchParamsStealthV2Type1,
        )
        from ..models.people_search_body_search_params_tags_type_0 import PeopleSearchBodySearchParamsTagsType0
        from ..models.people_search_body_search_params_time_zone_type_0 import PeopleSearchBodySearchParamsTimeZoneType0
        from ..models.people_search_body_search_params_years_of_experience_type_0 import (
            PeopleSearchBodySearchParamsYearsOfExperienceType0,
        )

        country_3_letter_code: dict[str, Any] | None | Unset
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(self.country_3_letter_code, PeopleSearchBodySearchParamsCountry3LetterCodeType0):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        num_connections: dict[str, Any] | None | Unset
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(self.num_connections, PeopleSearchBodySearchParamsNumConnectionsType0):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: dict[str, Any] | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(self.num_followers, PeopleSearchBodySearchParamsNumFollowersType0):
            num_followers = self.num_followers.to_dict()
        else:
            num_followers = self.num_followers

        approx_age: dict[str, Any] | None | Unset
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, PeopleSearchBodySearchParamsApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, PeopleSearchBodySearchParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: dict[str, Any] | None | Unset
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(self.keyword_search_options, PeopleSearchBodySearchParamsKeywordSearchOptionsType0):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        job_title_v2: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v2, Unset):
            job_title_v2 = UNSET
        elif isinstance(self.job_title_v2, PeopleSearchBodySearchParamsJobTitleV2Type0):
            job_title_v2 = self.job_title_v2.to_dict()
        else:
            job_title_v2 = self.job_title_v2

        exact_profile: dict[str, Any] | None | Unset
        if isinstance(self.exact_profile, Unset):
            exact_profile = UNSET
        elif isinstance(self.exact_profile, PeopleSearchBodySearchParamsExactProfileType0):
            exact_profile = self.exact_profile.to_dict()
        else:
            exact_profile = self.exact_profile

        started_in_role: dict[str, Any] | None | Unset
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(self.started_in_role, PeopleSearchBodySearchParamsStartedInRoleType0):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(self.started_in_role, PeopleSearchBodySearchParamsStartedInRoleType1):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: dict[str, Any] | None | Unset
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(self.started_at_company, PeopleSearchBodySearchParamsStartedAtCompanyType0):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(self.started_at_company, PeopleSearchBodySearchParamsStartedAtCompanyType1):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, PeopleSearchBodySearchParamsLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        past_jobs: dict[str, Any] | None | Unset
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, PeopleSearchBodySearchParamsPastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        languages: dict[str, Any] | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, PeopleSearchBodySearchParamsLanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        left_stealth_at: dict[str, Any] | None | Unset
        if isinstance(self.left_stealth_at, Unset):
            left_stealth_at = UNSET
        elif isinstance(self.left_stealth_at, PeopleSearchBodySearchParamsLeftStealthAtType0):
            left_stealth_at = self.left_stealth_at.to_dict()
        elif isinstance(self.left_stealth_at, PeopleSearchBodySearchParamsLeftStealthAtType1):
            left_stealth_at = self.left_stealth_at.to_dict()
        else:
            left_stealth_at = self.left_stealth_at

        is_in_stealth: bool | None | Unset
        if isinstance(self.is_in_stealth, Unset):
            is_in_stealth = UNSET
        else:
            is_in_stealth = self.is_in_stealth

        stealth_v2: dict[str, Any] | None | Unset
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(self.stealth_v2, PeopleSearchBodySearchParamsStealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, PeopleSearchBodySearchParamsStealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        job_status: dict[str, Any] | None | Unset
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, PeopleSearchBodySearchParamsJobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, PeopleSearchBodySearchParamsJobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, PeopleSearchBodySearchParamsJobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        time_zone: dict[str, Any] | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, PeopleSearchBodySearchParamsTimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        past_job_text: dict[str, Any] | None | Unset
        if isinstance(self.past_job_text, Unset):
            past_job_text = UNSET
        elif isinstance(self.past_job_text, PeopleSearchBodySearchParamsPastJobTextType0):
            past_job_text = self.past_job_text.to_dict()
        else:
            past_job_text = self.past_job_text

        fuzzy_name: dict[str, Any] | None | Unset
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, PeopleSearchBodySearchParamsFuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        company_match_mode: dict[str, Any] | None | Unset
        if isinstance(self.company_match_mode, Unset):
            company_match_mode = UNSET
        elif isinstance(self.company_match_mode, PeopleSearchBodySearchParamsCompanyMatchModeType0):
            company_match_mode = self.company_match_mode.to_dict()
        elif isinstance(self.company_match_mode, PeopleSearchBodySearchParamsCompanyMatchModeType1):
            company_match_mode = self.company_match_mode.to_dict()
        else:
            company_match_mode = self.company_match_mode

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, PeopleSearchBodySearchParamsYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        job_title_v3: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, PeopleSearchBodySearchParamsJobTitleV3Type0):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        has_profile_picture: bool | None | Unset
        if isinstance(self.has_profile_picture, Unset):
            has_profile_picture = UNSET
        else:
            has_profile_picture = self.has_profile_picture

        state: dict[str, Any] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, PeopleSearchBodySearchParamsStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        get_detailed_education: bool | None | Unset
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: bool | None | Unset
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, PeopleSearchBodySearchParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        education: dict[str, Any] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, PeopleSearchBodySearchParamsEducationType0):
            education = self.education.to_dict()
        else:
            education = self.education

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        from ..models.people_search_body_search_params_approx_age_type_0 import (
            PeopleSearchBodySearchParamsApproxAgeType0,
        )
        from ..models.people_search_body_search_params_company_match_mode_type_0 import (
            PeopleSearchBodySearchParamsCompanyMatchModeType0,
        )
        from ..models.people_search_body_search_params_company_match_mode_type_1 import (
            PeopleSearchBodySearchParamsCompanyMatchModeType1,
        )
        from ..models.people_search_body_search_params_country_3_letter_code_type_0 import (
            PeopleSearchBodySearchParamsCountry3LetterCodeType0,
        )
        from ..models.people_search_body_search_params_education_type_0 import (
            PeopleSearchBodySearchParamsEducationType0,
        )
        from ..models.people_search_body_search_params_exact_profile_type_0 import (
            PeopleSearchBodySearchParamsExactProfileType0,
        )
        from ..models.people_search_body_search_params_fuzzy_name_type_0 import (
            PeopleSearchBodySearchParamsFuzzyNameType0,
        )
        from ..models.people_search_body_search_params_job_status_type_0 import (
            PeopleSearchBodySearchParamsJobStatusType0,
        )
        from ..models.people_search_body_search_params_job_status_type_1 import (
            PeopleSearchBodySearchParamsJobStatusType1,
        )
        from ..models.people_search_body_search_params_job_status_type_2 import (
            PeopleSearchBodySearchParamsJobStatusType2,
        )
        from ..models.people_search_body_search_params_job_title_v2_type_0 import (
            PeopleSearchBodySearchParamsJobTitleV2Type0,
        )
        from ..models.people_search_body_search_params_job_title_v3_type_0 import (
            PeopleSearchBodySearchParamsJobTitleV3Type0,
        )
        from ..models.people_search_body_search_params_keyword_search_options_type_0 import (
            PeopleSearchBodySearchParamsKeywordSearchOptionsType0,
        )
        from ..models.people_search_body_search_params_keywords_type_0 import PeopleSearchBodySearchParamsKeywordsType0
        from ..models.people_search_body_search_params_languages_type_0 import (
            PeopleSearchBodySearchParamsLanguagesType0,
        )
        from ..models.people_search_body_search_params_left_stealth_at_type_0 import (
            PeopleSearchBodySearchParamsLeftStealthAtType0,
        )
        from ..models.people_search_body_search_params_left_stealth_at_type_1 import (
            PeopleSearchBodySearchParamsLeftStealthAtType1,
        )
        from ..models.people_search_body_search_params_location_type_0 import PeopleSearchBodySearchParamsLocationType0
        from ..models.people_search_body_search_params_num_connections_type_0 import (
            PeopleSearchBodySearchParamsNumConnectionsType0,
        )
        from ..models.people_search_body_search_params_num_followers_type_0 import (
            PeopleSearchBodySearchParamsNumFollowersType0,
        )
        from ..models.people_search_body_search_params_past_job_text_type_0 import (
            PeopleSearchBodySearchParamsPastJobTextType0,
        )
        from ..models.people_search_body_search_params_past_jobs_type_0 import PeopleSearchBodySearchParamsPastJobsType0
        from ..models.people_search_body_search_params_started_at_company_type_0 import (
            PeopleSearchBodySearchParamsStartedAtCompanyType0,
        )
        from ..models.people_search_body_search_params_started_at_company_type_1 import (
            PeopleSearchBodySearchParamsStartedAtCompanyType1,
        )
        from ..models.people_search_body_search_params_started_in_role_type_0 import (
            PeopleSearchBodySearchParamsStartedInRoleType0,
        )
        from ..models.people_search_body_search_params_started_in_role_type_1 import (
            PeopleSearchBodySearchParamsStartedInRoleType1,
        )
        from ..models.people_search_body_search_params_state_type_0 import PeopleSearchBodySearchParamsStateType0
        from ..models.people_search_body_search_params_stealth_v2_type_0 import (
            PeopleSearchBodySearchParamsStealthV2Type0,
        )
        from ..models.people_search_body_search_params_stealth_v2_type_1 import (
            PeopleSearchBodySearchParamsStealthV2Type1,
        )
        from ..models.people_search_body_search_params_tags_type_0 import PeopleSearchBodySearchParamsTagsType0
        from ..models.people_search_body_search_params_time_zone_type_0 import PeopleSearchBodySearchParamsTimeZoneType0
        from ..models.people_search_body_search_params_years_of_experience_type_0 import (
            PeopleSearchBodySearchParamsYearsOfExperienceType0,
        )

        d = dict(src_dict)

        def _parse_country_3_letter_code(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsCountry3LetterCodeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = PeopleSearchBodySearchParamsCountry3LetterCodeType0.from_dict(data)

                return country_3_letter_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsCountry3LetterCodeType0 | Unset, data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))

        def _parse_num_connections(data: object) -> None | PeopleSearchBodySearchParamsNumConnectionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = PeopleSearchBodySearchParamsNumConnectionsType0.from_dict(data)

                return num_connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsNumConnectionsType0 | Unset, data)

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))

        def _parse_num_followers(data: object) -> None | PeopleSearchBodySearchParamsNumFollowersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = PeopleSearchBodySearchParamsNumFollowersType0.from_dict(data)

                return num_followers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsNumFollowersType0 | Unset, data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))

        def _parse_approx_age(data: object) -> None | PeopleSearchBodySearchParamsApproxAgeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = PeopleSearchBodySearchParamsApproxAgeType0.from_dict(data)

                return approx_age_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsApproxAgeType0 | Unset, data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))

        def _parse_keywords(data: object) -> None | PeopleSearchBodySearchParamsKeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PeopleSearchBodySearchParamsKeywordsType0.from_dict(data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsKeywordsType0 | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_keyword_search_options(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsKeywordSearchOptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = PeopleSearchBodySearchParamsKeywordSearchOptionsType0.from_dict(data)

                return keyword_search_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsKeywordSearchOptionsType0 | Unset, data)

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))

        def _parse_job_title_v2(data: object) -> None | PeopleSearchBodySearchParamsJobTitleV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v2_type_0 = PeopleSearchBodySearchParamsJobTitleV2Type0.from_dict(data)

                return job_title_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsJobTitleV2Type0 | Unset, data)

        job_title_v2 = _parse_job_title_v2(d.pop("jobTitleV2", UNSET))

        def _parse_exact_profile(data: object) -> None | PeopleSearchBodySearchParamsExactProfileType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_profile_type_0 = PeopleSearchBodySearchParamsExactProfileType0.from_dict(data)

                return exact_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsExactProfileType0 | Unset, data)

        exact_profile = _parse_exact_profile(d.pop("exactProfile", UNSET))

        def _parse_started_in_role(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsStartedInRoleType0
            | PeopleSearchBodySearchParamsStartedInRoleType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_0 = PeopleSearchBodySearchParamsStartedInRoleType0.from_dict(data)

                return started_in_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = PeopleSearchBodySearchParamsStartedInRoleType1.from_dict(data)

                return started_in_role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsStartedInRoleType0
                | PeopleSearchBodySearchParamsStartedInRoleType1
                | Unset,
                data,
            )

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))

        def _parse_started_at_company(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsStartedAtCompanyType0
            | PeopleSearchBodySearchParamsStartedAtCompanyType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_0 = PeopleSearchBodySearchParamsStartedAtCompanyType0.from_dict(data)

                return started_at_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = PeopleSearchBodySearchParamsStartedAtCompanyType1.from_dict(data)

                return started_at_company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsStartedAtCompanyType0
                | PeopleSearchBodySearchParamsStartedAtCompanyType1
                | Unset,
                data,
            )

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))

        def _parse_location(data: object) -> None | PeopleSearchBodySearchParamsLocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = PeopleSearchBodySearchParamsLocationType0.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsLocationType0 | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_past_jobs(data: object) -> None | PeopleSearchBodySearchParamsPastJobsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = PeopleSearchBodySearchParamsPastJobsType0.from_dict(data)

                return past_jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsPastJobsType0 | Unset, data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))

        def _parse_languages(data: object) -> None | PeopleSearchBodySearchParamsLanguagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = PeopleSearchBodySearchParamsLanguagesType0.from_dict(data)

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsLanguagesType0 | Unset, data)

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_left_stealth_at(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsLeftStealthAtType0
            | PeopleSearchBodySearchParamsLeftStealthAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_0 = PeopleSearchBodySearchParamsLeftStealthAtType0.from_dict(data)

                return left_stealth_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_1 = PeopleSearchBodySearchParamsLeftStealthAtType1.from_dict(data)

                return left_stealth_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsLeftStealthAtType0
                | PeopleSearchBodySearchParamsLeftStealthAtType1
                | Unset,
                data,
            )

        left_stealth_at = _parse_left_stealth_at(d.pop("leftStealthAt", UNSET))

        def _parse_is_in_stealth(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_in_stealth = _parse_is_in_stealth(d.pop("isInStealth", UNSET))

        def _parse_stealth_v2(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsStealthV2Type0 | PeopleSearchBodySearchParamsStealthV2Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = PeopleSearchBodySearchParamsStealthV2Type0.from_dict(data)

                return stealth_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = PeopleSearchBodySearchParamsStealthV2Type1.from_dict(data)

                return stealth_v2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PeopleSearchBodySearchParamsStealthV2Type0 | PeopleSearchBodySearchParamsStealthV2Type1 | Unset,
                data,
            )

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))

        def _parse_job_status(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsJobStatusType0
            | PeopleSearchBodySearchParamsJobStatusType1
            | PeopleSearchBodySearchParamsJobStatusType2
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = PeopleSearchBodySearchParamsJobStatusType0.from_dict(data)

                return job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = PeopleSearchBodySearchParamsJobStatusType1.from_dict(data)

                return job_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = PeopleSearchBodySearchParamsJobStatusType2.from_dict(data)

                return job_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsJobStatusType0
                | PeopleSearchBodySearchParamsJobStatusType1
                | PeopleSearchBodySearchParamsJobStatusType2
                | Unset,
                data,
            )

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))

        def _parse_time_zone(data: object) -> None | PeopleSearchBodySearchParamsTimeZoneType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = PeopleSearchBodySearchParamsTimeZoneType0.from_dict(data)

                return time_zone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsTimeZoneType0 | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        def _parse_past_job_text(data: object) -> None | PeopleSearchBodySearchParamsPastJobTextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_job_text_type_0 = PeopleSearchBodySearchParamsPastJobTextType0.from_dict(data)

                return past_job_text_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsPastJobTextType0 | Unset, data)

        past_job_text = _parse_past_job_text(d.pop("pastJobText", UNSET))

        def _parse_fuzzy_name(data: object) -> None | PeopleSearchBodySearchParamsFuzzyNameType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = PeopleSearchBodySearchParamsFuzzyNameType0.from_dict(data)

                return fuzzy_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsFuzzyNameType0 | Unset, data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))

        def _parse_company_match_mode(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsCompanyMatchModeType0
            | PeopleSearchBodySearchParamsCompanyMatchModeType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_0 = PeopleSearchBodySearchParamsCompanyMatchModeType0.from_dict(data)

                return company_match_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_1 = PeopleSearchBodySearchParamsCompanyMatchModeType1.from_dict(data)

                return company_match_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsCompanyMatchModeType0
                | PeopleSearchBodySearchParamsCompanyMatchModeType1
                | Unset,
                data,
            )

        company_match_mode = _parse_company_match_mode(d.pop("companyMatchMode", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsYearsOfExperienceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = PeopleSearchBodySearchParamsYearsOfExperienceType0.from_dict(data)

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsYearsOfExperienceType0 | Unset, data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))

        def _parse_job_title_v3(data: object) -> None | PeopleSearchBodySearchParamsJobTitleV3Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = PeopleSearchBodySearchParamsJobTitleV3Type0.from_dict(data)

                return job_title_v3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsJobTitleV3Type0 | Unset, data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))

        def _parse_has_profile_picture(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_profile_picture = _parse_has_profile_picture(d.pop("hasProfilePicture", UNSET))

        def _parse_state(data: object) -> None | PeopleSearchBodySearchParamsStateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = PeopleSearchBodySearchParamsStateType0.from_dict(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsStateType0 | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_get_detailed_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))

        def _parse_get_detailed_work_experience(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))

        def _parse_tags(data: object) -> None | PeopleSearchBodySearchParamsTagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = PeopleSearchBodySearchParamsTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsTagsType0 | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_education(data: object) -> None | PeopleSearchBodySearchParamsEducationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = PeopleSearchBodySearchParamsEducationType0.from_dict(data)

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsEducationType0 | Unset, data)

        education = _parse_education(d.pop("education", UNSET))

        people_search_body_search_params = cls(
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

        return people_search_body_search_params
