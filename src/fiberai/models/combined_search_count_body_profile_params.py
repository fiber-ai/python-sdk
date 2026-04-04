from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_count_body_profile_params_approx_age_type_0 import (
        CombinedSearchCountBodyProfileParamsApproxAgeType0,
    )
    from ..models.combined_search_count_body_profile_params_certifications_type_0 import (
        CombinedSearchCountBodyProfileParamsCertificationsType0,
    )
    from ..models.combined_search_count_body_profile_params_company_match_mode_type_0 import (
        CombinedSearchCountBodyProfileParamsCompanyMatchModeType0,
    )
    from ..models.combined_search_count_body_profile_params_company_match_mode_type_1 import (
        CombinedSearchCountBodyProfileParamsCompanyMatchModeType1,
    )
    from ..models.combined_search_count_body_profile_params_country_3_letter_code_type_0 import (
        CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0,
    )
    from ..models.combined_search_count_body_profile_params_education_type_0 import (
        CombinedSearchCountBodyProfileParamsEducationType0,
    )
    from ..models.combined_search_count_body_profile_params_employment_type_type_0 import (
        CombinedSearchCountBodyProfileParamsEmploymentTypeType0,
    )
    from ..models.combined_search_count_body_profile_params_exact_profile_type_0 import (
        CombinedSearchCountBodyProfileParamsExactProfileType0,
    )
    from ..models.combined_search_count_body_profile_params_fuzzy_name_type_0 import (
        CombinedSearchCountBodyProfileParamsFuzzyNameType0,
    )
    from ..models.combined_search_count_body_profile_params_job_status_type_0 import (
        CombinedSearchCountBodyProfileParamsJobStatusType0,
    )
    from ..models.combined_search_count_body_profile_params_job_status_type_1 import (
        CombinedSearchCountBodyProfileParamsJobStatusType1,
    )
    from ..models.combined_search_count_body_profile_params_job_status_type_2 import (
        CombinedSearchCountBodyProfileParamsJobStatusType2,
    )
    from ..models.combined_search_count_body_profile_params_job_title_v2_type_0 import (
        CombinedSearchCountBodyProfileParamsJobTitleV2Type0,
    )
    from ..models.combined_search_count_body_profile_params_job_title_v3_type_0 import (
        CombinedSearchCountBodyProfileParamsJobTitleV3Type0,
    )
    from ..models.combined_search_count_body_profile_params_keyword_search_options_type_0 import (
        CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0,
    )
    from ..models.combined_search_count_body_profile_params_keywords_type_0 import (
        CombinedSearchCountBodyProfileParamsKeywordsType0,
    )
    from ..models.combined_search_count_body_profile_params_keywords_v2_type_0 import (
        CombinedSearchCountBodyProfileParamsKeywordsV2Type0,
    )
    from ..models.combined_search_count_body_profile_params_languages_type_0 import (
        CombinedSearchCountBodyProfileParamsLanguagesType0,
    )
    from ..models.combined_search_count_body_profile_params_left_stealth_at_type_0 import (
        CombinedSearchCountBodyProfileParamsLeftStealthAtType0,
    )
    from ..models.combined_search_count_body_profile_params_left_stealth_at_type_1 import (
        CombinedSearchCountBodyProfileParamsLeftStealthAtType1,
    )
    from ..models.combined_search_count_body_profile_params_location_type_0 import (
        CombinedSearchCountBodyProfileParamsLocationType0,
    )
    from ..models.combined_search_count_body_profile_params_num_connections_type_0 import (
        CombinedSearchCountBodyProfileParamsNumConnectionsType0,
    )
    from ..models.combined_search_count_body_profile_params_num_followers_type_0 import (
        CombinedSearchCountBodyProfileParamsNumFollowersType0,
    )
    from ..models.combined_search_count_body_profile_params_past_job_text_type_0 import (
        CombinedSearchCountBodyProfileParamsPastJobTextType0,
    )
    from ..models.combined_search_count_body_profile_params_past_jobs_type_0 import (
        CombinedSearchCountBodyProfileParamsPastJobsType0,
    )
    from ..models.combined_search_count_body_profile_params_publications_type_0 import (
        CombinedSearchCountBodyProfileParamsPublicationsType0,
    )
    from ..models.combined_search_count_body_profile_params_started_at_company_type_0 import (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType0,
    )
    from ..models.combined_search_count_body_profile_params_started_at_company_type_1 import (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType1,
    )
    from ..models.combined_search_count_body_profile_params_started_in_role_type_0 import (
        CombinedSearchCountBodyProfileParamsStartedInRoleType0,
    )
    from ..models.combined_search_count_body_profile_params_started_in_role_type_1 import (
        CombinedSearchCountBodyProfileParamsStartedInRoleType1,
    )
    from ..models.combined_search_count_body_profile_params_state_type_0 import (
        CombinedSearchCountBodyProfileParamsStateType0,
    )
    from ..models.combined_search_count_body_profile_params_stealth_v2_type_0 import (
        CombinedSearchCountBodyProfileParamsStealthV2Type0,
    )
    from ..models.combined_search_count_body_profile_params_stealth_v2_type_1 import (
        CombinedSearchCountBodyProfileParamsStealthV2Type1,
    )
    from ..models.combined_search_count_body_profile_params_tags_type_0 import (
        CombinedSearchCountBodyProfileParamsTagsType0,
    )
    from ..models.combined_search_count_body_profile_params_time_zone_type_0 import (
        CombinedSearchCountBodyProfileParamsTimeZoneType0,
    )
    from ..models.combined_search_count_body_profile_params_years_of_experience_type_0 import (
        CombinedSearchCountBodyProfileParamsYearsOfExperienceType0,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyProfileParams")


@_attrs_define
class CombinedSearchCountBodyProfileParams:
    """The profile search parameters. Returns profiles matching these filters who work/used to work at companies satisfying
    companyParams.

        Attributes:
            country_3_letter_code (CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0 | None | Unset):
            num_connections (CombinedSearchCountBodyProfileParamsNumConnectionsType0 | None | Unset):
            num_followers (CombinedSearchCountBodyProfileParamsNumFollowersType0 | None | Unset):
            approx_age (CombinedSearchCountBodyProfileParamsApproxAgeType0 | None | Unset):
            keywords (CombinedSearchCountBodyProfileParamsKeywordsType0 | None | Unset):
            keywords_v2 (CombinedSearchCountBodyProfileParamsKeywordsV2Type0 | None | Unset):
            keyword_search_options (CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0 | None | Unset):
            job_title_v2 (CombinedSearchCountBodyProfileParamsJobTitleV2Type0 | None | Unset):
            exact_profile (CombinedSearchCountBodyProfileParamsExactProfileType0 | None | Unset):
            started_in_role (CombinedSearchCountBodyProfileParamsStartedInRoleType0 |
                CombinedSearchCountBodyProfileParamsStartedInRoleType1 | None | Unset):
            started_at_company (CombinedSearchCountBodyProfileParamsStartedAtCompanyType0 |
                CombinedSearchCountBodyProfileParamsStartedAtCompanyType1 | None | Unset):
            location (CombinedSearchCountBodyProfileParamsLocationType0 | None | Unset):
            past_jobs (CombinedSearchCountBodyProfileParamsPastJobsType0 | None | Unset):
            languages (CombinedSearchCountBodyProfileParamsLanguagesType0 | None | Unset):
            left_stealth_at (CombinedSearchCountBodyProfileParamsLeftStealthAtType0 |
                CombinedSearchCountBodyProfileParamsLeftStealthAtType1 | None | Unset):
            is_in_stealth (bool | None | Unset):
            stealth_v2 (CombinedSearchCountBodyProfileParamsStealthV2Type0 |
                CombinedSearchCountBodyProfileParamsStealthV2Type1 | None | Unset):
            job_status (CombinedSearchCountBodyProfileParamsJobStatusType0 |
                CombinedSearchCountBodyProfileParamsJobStatusType1 | CombinedSearchCountBodyProfileParamsJobStatusType2 | None |
                Unset):
            time_zone (CombinedSearchCountBodyProfileParamsTimeZoneType0 | None | Unset):
            past_job_text (CombinedSearchCountBodyProfileParamsPastJobTextType0 | None | Unset):
            fuzzy_name (CombinedSearchCountBodyProfileParamsFuzzyNameType0 | None | Unset):
            company_match_mode (CombinedSearchCountBodyProfileParamsCompanyMatchModeType0 |
                CombinedSearchCountBodyProfileParamsCompanyMatchModeType1 | None | Unset):
            years_of_experience (CombinedSearchCountBodyProfileParamsYearsOfExperienceType0 | None | Unset):
            job_title_v3 (CombinedSearchCountBodyProfileParamsJobTitleV3Type0 | None | Unset):
            has_profile_picture (bool | None | Unset):
            state (CombinedSearchCountBodyProfileParamsStateType0 | None | Unset):
            certifications (CombinedSearchCountBodyProfileParamsCertificationsType0 | None | Unset):
            publications (CombinedSearchCountBodyProfileParamsPublicationsType0 | None | Unset):
            has_no_education (bool | None | Unset):
            employment_type (CombinedSearchCountBodyProfileParamsEmploymentTypeType0 | None | Unset):
            get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
                the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
                down the API call, so only enable this if you need it. Default: False.
            get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
                item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
                array. This slows down the API call, so only enable this if you need it. Default: False.
            tags (CombinedSearchCountBodyProfileParamsTagsType0 | None | Unset):
            education (CombinedSearchCountBodyProfileParamsEducationType0 | None | Unset):
    """

    country_3_letter_code: CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0 | None | Unset = UNSET
    num_connections: CombinedSearchCountBodyProfileParamsNumConnectionsType0 | None | Unset = UNSET
    num_followers: CombinedSearchCountBodyProfileParamsNumFollowersType0 | None | Unset = UNSET
    approx_age: CombinedSearchCountBodyProfileParamsApproxAgeType0 | None | Unset = UNSET
    keywords: CombinedSearchCountBodyProfileParamsKeywordsType0 | None | Unset = UNSET
    keywords_v2: CombinedSearchCountBodyProfileParamsKeywordsV2Type0 | None | Unset = UNSET
    keyword_search_options: CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0 | None | Unset = UNSET
    job_title_v2: CombinedSearchCountBodyProfileParamsJobTitleV2Type0 | None | Unset = UNSET
    exact_profile: CombinedSearchCountBodyProfileParamsExactProfileType0 | None | Unset = UNSET
    started_in_role: (
        CombinedSearchCountBodyProfileParamsStartedInRoleType0
        | CombinedSearchCountBodyProfileParamsStartedInRoleType1
        | None
        | Unset
    ) = UNSET
    started_at_company: (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType0
        | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1
        | None
        | Unset
    ) = UNSET
    location: CombinedSearchCountBodyProfileParamsLocationType0 | None | Unset = UNSET
    past_jobs: CombinedSearchCountBodyProfileParamsPastJobsType0 | None | Unset = UNSET
    languages: CombinedSearchCountBodyProfileParamsLanguagesType0 | None | Unset = UNSET
    left_stealth_at: (
        CombinedSearchCountBodyProfileParamsLeftStealthAtType0
        | CombinedSearchCountBodyProfileParamsLeftStealthAtType1
        | None
        | Unset
    ) = UNSET
    is_in_stealth: bool | None | Unset = UNSET
    stealth_v2: (
        CombinedSearchCountBodyProfileParamsStealthV2Type0
        | CombinedSearchCountBodyProfileParamsStealthV2Type1
        | None
        | Unset
    ) = UNSET
    job_status: (
        CombinedSearchCountBodyProfileParamsJobStatusType0
        | CombinedSearchCountBodyProfileParamsJobStatusType1
        | CombinedSearchCountBodyProfileParamsJobStatusType2
        | None
        | Unset
    ) = UNSET
    time_zone: CombinedSearchCountBodyProfileParamsTimeZoneType0 | None | Unset = UNSET
    past_job_text: CombinedSearchCountBodyProfileParamsPastJobTextType0 | None | Unset = UNSET
    fuzzy_name: CombinedSearchCountBodyProfileParamsFuzzyNameType0 | None | Unset = UNSET
    company_match_mode: (
        CombinedSearchCountBodyProfileParamsCompanyMatchModeType0
        | CombinedSearchCountBodyProfileParamsCompanyMatchModeType1
        | None
        | Unset
    ) = UNSET
    years_of_experience: CombinedSearchCountBodyProfileParamsYearsOfExperienceType0 | None | Unset = UNSET
    job_title_v3: CombinedSearchCountBodyProfileParamsJobTitleV3Type0 | None | Unset = UNSET
    has_profile_picture: bool | None | Unset = UNSET
    state: CombinedSearchCountBodyProfileParamsStateType0 | None | Unset = UNSET
    certifications: CombinedSearchCountBodyProfileParamsCertificationsType0 | None | Unset = UNSET
    publications: CombinedSearchCountBodyProfileParamsPublicationsType0 | None | Unset = UNSET
    has_no_education: bool | None | Unset = UNSET
    employment_type: CombinedSearchCountBodyProfileParamsEmploymentTypeType0 | None | Unset = UNSET
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    tags: CombinedSearchCountBodyProfileParamsTagsType0 | None | Unset = UNSET
    education: CombinedSearchCountBodyProfileParamsEducationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_count_body_profile_params_approx_age_type_0 import (
            CombinedSearchCountBodyProfileParamsApproxAgeType0,
        )
        from ..models.combined_search_count_body_profile_params_certifications_type_0 import (
            CombinedSearchCountBodyProfileParamsCertificationsType0,
        )
        from ..models.combined_search_count_body_profile_params_company_match_mode_type_0 import (
            CombinedSearchCountBodyProfileParamsCompanyMatchModeType0,
        )
        from ..models.combined_search_count_body_profile_params_company_match_mode_type_1 import (
            CombinedSearchCountBodyProfileParamsCompanyMatchModeType1,
        )
        from ..models.combined_search_count_body_profile_params_country_3_letter_code_type_0 import (
            CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0,
        )
        from ..models.combined_search_count_body_profile_params_education_type_0 import (
            CombinedSearchCountBodyProfileParamsEducationType0,
        )
        from ..models.combined_search_count_body_profile_params_employment_type_type_0 import (
            CombinedSearchCountBodyProfileParamsEmploymentTypeType0,
        )
        from ..models.combined_search_count_body_profile_params_exact_profile_type_0 import (
            CombinedSearchCountBodyProfileParamsExactProfileType0,
        )
        from ..models.combined_search_count_body_profile_params_fuzzy_name_type_0 import (
            CombinedSearchCountBodyProfileParamsFuzzyNameType0,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_0 import (
            CombinedSearchCountBodyProfileParamsJobStatusType0,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_1 import (
            CombinedSearchCountBodyProfileParamsJobStatusType1,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_2 import (
            CombinedSearchCountBodyProfileParamsJobStatusType2,
        )
        from ..models.combined_search_count_body_profile_params_job_title_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsJobTitleV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_job_title_v3_type_0 import (
            CombinedSearchCountBodyProfileParamsJobTitleV3Type0,
        )
        from ..models.combined_search_count_body_profile_params_keyword_search_options_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0,
        )
        from ..models.combined_search_count_body_profile_params_keywords_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsType0,
        )
        from ..models.combined_search_count_body_profile_params_keywords_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_languages_type_0 import (
            CombinedSearchCountBodyProfileParamsLanguagesType0,
        )
        from ..models.combined_search_count_body_profile_params_left_stealth_at_type_0 import (
            CombinedSearchCountBodyProfileParamsLeftStealthAtType0,
        )
        from ..models.combined_search_count_body_profile_params_left_stealth_at_type_1 import (
            CombinedSearchCountBodyProfileParamsLeftStealthAtType1,
        )
        from ..models.combined_search_count_body_profile_params_location_type_0 import (
            CombinedSearchCountBodyProfileParamsLocationType0,
        )
        from ..models.combined_search_count_body_profile_params_num_connections_type_0 import (
            CombinedSearchCountBodyProfileParamsNumConnectionsType0,
        )
        from ..models.combined_search_count_body_profile_params_num_followers_type_0 import (
            CombinedSearchCountBodyProfileParamsNumFollowersType0,
        )
        from ..models.combined_search_count_body_profile_params_past_job_text_type_0 import (
            CombinedSearchCountBodyProfileParamsPastJobTextType0,
        )
        from ..models.combined_search_count_body_profile_params_past_jobs_type_0 import (
            CombinedSearchCountBodyProfileParamsPastJobsType0,
        )
        from ..models.combined_search_count_body_profile_params_publications_type_0 import (
            CombinedSearchCountBodyProfileParamsPublicationsType0,
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType0,
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1,
        )
        from ..models.combined_search_count_body_profile_params_started_in_role_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedInRoleType0,
        )
        from ..models.combined_search_count_body_profile_params_started_in_role_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedInRoleType1,
        )
        from ..models.combined_search_count_body_profile_params_state_type_0 import (
            CombinedSearchCountBodyProfileParamsStateType0,
        )
        from ..models.combined_search_count_body_profile_params_stealth_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsStealthV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_stealth_v2_type_1 import (
            CombinedSearchCountBodyProfileParamsStealthV2Type1,
        )
        from ..models.combined_search_count_body_profile_params_tags_type_0 import (
            CombinedSearchCountBodyProfileParamsTagsType0,
        )
        from ..models.combined_search_count_body_profile_params_time_zone_type_0 import (
            CombinedSearchCountBodyProfileParamsTimeZoneType0,
        )
        from ..models.combined_search_count_body_profile_params_years_of_experience_type_0 import (
            CombinedSearchCountBodyProfileParamsYearsOfExperienceType0,
        )

        country_3_letter_code: dict[str, Any] | None | Unset
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(self.country_3_letter_code, CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        num_connections: dict[str, Any] | None | Unset
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(self.num_connections, CombinedSearchCountBodyProfileParamsNumConnectionsType0):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: dict[str, Any] | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(self.num_followers, CombinedSearchCountBodyProfileParamsNumFollowersType0):
            num_followers = self.num_followers.to_dict()
        else:
            num_followers = self.num_followers

        approx_age: dict[str, Any] | None | Unset
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, CombinedSearchCountBodyProfileParamsApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, CombinedSearchCountBodyProfileParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keywords_v2: dict[str, Any] | None | Unset
        if isinstance(self.keywords_v2, Unset):
            keywords_v2 = UNSET
        elif isinstance(self.keywords_v2, CombinedSearchCountBodyProfileParamsKeywordsV2Type0):
            keywords_v2 = self.keywords_v2.to_dict()
        else:
            keywords_v2 = self.keywords_v2

        keyword_search_options: dict[str, Any] | None | Unset
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(self.keyword_search_options, CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        job_title_v2: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v2, Unset):
            job_title_v2 = UNSET
        elif isinstance(self.job_title_v2, CombinedSearchCountBodyProfileParamsJobTitleV2Type0):
            job_title_v2 = self.job_title_v2.to_dict()
        else:
            job_title_v2 = self.job_title_v2

        exact_profile: dict[str, Any] | None | Unset
        if isinstance(self.exact_profile, Unset):
            exact_profile = UNSET
        elif isinstance(self.exact_profile, CombinedSearchCountBodyProfileParamsExactProfileType0):
            exact_profile = self.exact_profile.to_dict()
        else:
            exact_profile = self.exact_profile

        started_in_role: dict[str, Any] | None | Unset
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(self.started_in_role, CombinedSearchCountBodyProfileParamsStartedInRoleType0):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(self.started_in_role, CombinedSearchCountBodyProfileParamsStartedInRoleType1):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: dict[str, Any] | None | Unset
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(self.started_at_company, CombinedSearchCountBodyProfileParamsStartedAtCompanyType0):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(self.started_at_company, CombinedSearchCountBodyProfileParamsStartedAtCompanyType1):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, CombinedSearchCountBodyProfileParamsLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        past_jobs: dict[str, Any] | None | Unset
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, CombinedSearchCountBodyProfileParamsPastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        languages: dict[str, Any] | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, CombinedSearchCountBodyProfileParamsLanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        left_stealth_at: dict[str, Any] | None | Unset
        if isinstance(self.left_stealth_at, Unset):
            left_stealth_at = UNSET
        elif isinstance(self.left_stealth_at, CombinedSearchCountBodyProfileParamsLeftStealthAtType0):
            left_stealth_at = self.left_stealth_at.to_dict()
        elif isinstance(self.left_stealth_at, CombinedSearchCountBodyProfileParamsLeftStealthAtType1):
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
        elif isinstance(self.stealth_v2, CombinedSearchCountBodyProfileParamsStealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, CombinedSearchCountBodyProfileParamsStealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        job_status: dict[str, Any] | None | Unset
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, CombinedSearchCountBodyProfileParamsJobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, CombinedSearchCountBodyProfileParamsJobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, CombinedSearchCountBodyProfileParamsJobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        time_zone: dict[str, Any] | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, CombinedSearchCountBodyProfileParamsTimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        past_job_text: dict[str, Any] | None | Unset
        if isinstance(self.past_job_text, Unset):
            past_job_text = UNSET
        elif isinstance(self.past_job_text, CombinedSearchCountBodyProfileParamsPastJobTextType0):
            past_job_text = self.past_job_text.to_dict()
        else:
            past_job_text = self.past_job_text

        fuzzy_name: dict[str, Any] | None | Unset
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, CombinedSearchCountBodyProfileParamsFuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        company_match_mode: dict[str, Any] | None | Unset
        if isinstance(self.company_match_mode, Unset):
            company_match_mode = UNSET
        elif isinstance(self.company_match_mode, CombinedSearchCountBodyProfileParamsCompanyMatchModeType0):
            company_match_mode = self.company_match_mode.to_dict()
        elif isinstance(self.company_match_mode, CombinedSearchCountBodyProfileParamsCompanyMatchModeType1):
            company_match_mode = self.company_match_mode.to_dict()
        else:
            company_match_mode = self.company_match_mode

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, CombinedSearchCountBodyProfileParamsYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        job_title_v3: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, CombinedSearchCountBodyProfileParamsJobTitleV3Type0):
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
        elif isinstance(self.state, CombinedSearchCountBodyProfileParamsStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        certifications: dict[str, Any] | None | Unset
        if isinstance(self.certifications, Unset):
            certifications = UNSET
        elif isinstance(self.certifications, CombinedSearchCountBodyProfileParamsCertificationsType0):
            certifications = self.certifications.to_dict()
        else:
            certifications = self.certifications

        publications: dict[str, Any] | None | Unset
        if isinstance(self.publications, Unset):
            publications = UNSET
        elif isinstance(self.publications, CombinedSearchCountBodyProfileParamsPublicationsType0):
            publications = self.publications.to_dict()
        else:
            publications = self.publications

        has_no_education: bool | None | Unset
        if isinstance(self.has_no_education, Unset):
            has_no_education = UNSET
        else:
            has_no_education = self.has_no_education

        employment_type: dict[str, Any] | None | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        elif isinstance(self.employment_type, CombinedSearchCountBodyProfileParamsEmploymentTypeType0):
            employment_type = self.employment_type.to_dict()
        else:
            employment_type = self.employment_type

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
        elif isinstance(self.tags, CombinedSearchCountBodyProfileParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        education: dict[str, Any] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, CombinedSearchCountBodyProfileParamsEducationType0):
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
        if keywords_v2 is not UNSET:
            field_dict["keywordsV2"] = keywords_v2
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
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if publications is not UNSET:
            field_dict["publications"] = publications
        if has_no_education is not UNSET:
            field_dict["hasNoEducation"] = has_no_education
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
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
        from ..models.combined_search_count_body_profile_params_approx_age_type_0 import (
            CombinedSearchCountBodyProfileParamsApproxAgeType0,
        )
        from ..models.combined_search_count_body_profile_params_certifications_type_0 import (
            CombinedSearchCountBodyProfileParamsCertificationsType0,
        )
        from ..models.combined_search_count_body_profile_params_company_match_mode_type_0 import (
            CombinedSearchCountBodyProfileParamsCompanyMatchModeType0,
        )
        from ..models.combined_search_count_body_profile_params_company_match_mode_type_1 import (
            CombinedSearchCountBodyProfileParamsCompanyMatchModeType1,
        )
        from ..models.combined_search_count_body_profile_params_country_3_letter_code_type_0 import (
            CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0,
        )
        from ..models.combined_search_count_body_profile_params_education_type_0 import (
            CombinedSearchCountBodyProfileParamsEducationType0,
        )
        from ..models.combined_search_count_body_profile_params_employment_type_type_0 import (
            CombinedSearchCountBodyProfileParamsEmploymentTypeType0,
        )
        from ..models.combined_search_count_body_profile_params_exact_profile_type_0 import (
            CombinedSearchCountBodyProfileParamsExactProfileType0,
        )
        from ..models.combined_search_count_body_profile_params_fuzzy_name_type_0 import (
            CombinedSearchCountBodyProfileParamsFuzzyNameType0,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_0 import (
            CombinedSearchCountBodyProfileParamsJobStatusType0,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_1 import (
            CombinedSearchCountBodyProfileParamsJobStatusType1,
        )
        from ..models.combined_search_count_body_profile_params_job_status_type_2 import (
            CombinedSearchCountBodyProfileParamsJobStatusType2,
        )
        from ..models.combined_search_count_body_profile_params_job_title_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsJobTitleV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_job_title_v3_type_0 import (
            CombinedSearchCountBodyProfileParamsJobTitleV3Type0,
        )
        from ..models.combined_search_count_body_profile_params_keyword_search_options_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0,
        )
        from ..models.combined_search_count_body_profile_params_keywords_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsType0,
        )
        from ..models.combined_search_count_body_profile_params_keywords_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_languages_type_0 import (
            CombinedSearchCountBodyProfileParamsLanguagesType0,
        )
        from ..models.combined_search_count_body_profile_params_left_stealth_at_type_0 import (
            CombinedSearchCountBodyProfileParamsLeftStealthAtType0,
        )
        from ..models.combined_search_count_body_profile_params_left_stealth_at_type_1 import (
            CombinedSearchCountBodyProfileParamsLeftStealthAtType1,
        )
        from ..models.combined_search_count_body_profile_params_location_type_0 import (
            CombinedSearchCountBodyProfileParamsLocationType0,
        )
        from ..models.combined_search_count_body_profile_params_num_connections_type_0 import (
            CombinedSearchCountBodyProfileParamsNumConnectionsType0,
        )
        from ..models.combined_search_count_body_profile_params_num_followers_type_0 import (
            CombinedSearchCountBodyProfileParamsNumFollowersType0,
        )
        from ..models.combined_search_count_body_profile_params_past_job_text_type_0 import (
            CombinedSearchCountBodyProfileParamsPastJobTextType0,
        )
        from ..models.combined_search_count_body_profile_params_past_jobs_type_0 import (
            CombinedSearchCountBodyProfileParamsPastJobsType0,
        )
        from ..models.combined_search_count_body_profile_params_publications_type_0 import (
            CombinedSearchCountBodyProfileParamsPublicationsType0,
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType0,
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1,
        )
        from ..models.combined_search_count_body_profile_params_started_in_role_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedInRoleType0,
        )
        from ..models.combined_search_count_body_profile_params_started_in_role_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedInRoleType1,
        )
        from ..models.combined_search_count_body_profile_params_state_type_0 import (
            CombinedSearchCountBodyProfileParamsStateType0,
        )
        from ..models.combined_search_count_body_profile_params_stealth_v2_type_0 import (
            CombinedSearchCountBodyProfileParamsStealthV2Type0,
        )
        from ..models.combined_search_count_body_profile_params_stealth_v2_type_1 import (
            CombinedSearchCountBodyProfileParamsStealthV2Type1,
        )
        from ..models.combined_search_count_body_profile_params_tags_type_0 import (
            CombinedSearchCountBodyProfileParamsTagsType0,
        )
        from ..models.combined_search_count_body_profile_params_time_zone_type_0 import (
            CombinedSearchCountBodyProfileParamsTimeZoneType0,
        )
        from ..models.combined_search_count_body_profile_params_years_of_experience_type_0 import (
            CombinedSearchCountBodyProfileParamsYearsOfExperienceType0,
        )

        d = dict(src_dict)

        def _parse_country_3_letter_code(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0.from_dict(
                    data
                )

                return country_3_letter_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsCountry3LetterCodeType0 | None | Unset, data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))

        def _parse_num_connections(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsNumConnectionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = CombinedSearchCountBodyProfileParamsNumConnectionsType0.from_dict(data)

                return num_connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsNumConnectionsType0 | None | Unset, data)

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))

        def _parse_num_followers(data: object) -> CombinedSearchCountBodyProfileParamsNumFollowersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = CombinedSearchCountBodyProfileParamsNumFollowersType0.from_dict(data)

                return num_followers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsNumFollowersType0 | None | Unset, data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))

        def _parse_approx_age(data: object) -> CombinedSearchCountBodyProfileParamsApproxAgeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = CombinedSearchCountBodyProfileParamsApproxAgeType0.from_dict(data)

                return approx_age_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsApproxAgeType0 | None | Unset, data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))

        def _parse_keywords(data: object) -> CombinedSearchCountBodyProfileParamsKeywordsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = CombinedSearchCountBodyProfileParamsKeywordsType0.from_dict(data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsKeywordsType0 | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_keywords_v2(data: object) -> CombinedSearchCountBodyProfileParamsKeywordsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_v2_type_0 = CombinedSearchCountBodyProfileParamsKeywordsV2Type0.from_dict(data)

                return keywords_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsKeywordsV2Type0 | None | Unset, data)

        keywords_v2 = _parse_keywords_v2(d.pop("keywordsV2", UNSET))

        def _parse_keyword_search_options(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0.from_dict(
                    data
                )

                return keyword_search_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsKeywordSearchOptionsType0 | None | Unset, data)

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))

        def _parse_job_title_v2(data: object) -> CombinedSearchCountBodyProfileParamsJobTitleV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v2_type_0 = CombinedSearchCountBodyProfileParamsJobTitleV2Type0.from_dict(data)

                return job_title_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsJobTitleV2Type0 | None | Unset, data)

        job_title_v2 = _parse_job_title_v2(d.pop("jobTitleV2", UNSET))

        def _parse_exact_profile(data: object) -> CombinedSearchCountBodyProfileParamsExactProfileType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_profile_type_0 = CombinedSearchCountBodyProfileParamsExactProfileType0.from_dict(data)

                return exact_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsExactProfileType0 | None | Unset, data)

        exact_profile = _parse_exact_profile(d.pop("exactProfile", UNSET))

        def _parse_started_in_role(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsStartedInRoleType0
            | CombinedSearchCountBodyProfileParamsStartedInRoleType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_0 = CombinedSearchCountBodyProfileParamsStartedInRoleType0.from_dict(data)

                return started_in_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = CombinedSearchCountBodyProfileParamsStartedInRoleType1.from_dict(data)

                return started_in_role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsStartedInRoleType0
                | CombinedSearchCountBodyProfileParamsStartedInRoleType1
                | None
                | Unset,
                data,
            )

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))

        def _parse_started_at_company(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType0
            | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_0 = CombinedSearchCountBodyProfileParamsStartedAtCompanyType0.from_dict(data)

                return started_at_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = CombinedSearchCountBodyProfileParamsStartedAtCompanyType1.from_dict(data)

                return started_at_company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsStartedAtCompanyType0
                | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1
                | None
                | Unset,
                data,
            )

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))

        def _parse_location(data: object) -> CombinedSearchCountBodyProfileParamsLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = CombinedSearchCountBodyProfileParamsLocationType0.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsLocationType0 | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_past_jobs(data: object) -> CombinedSearchCountBodyProfileParamsPastJobsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = CombinedSearchCountBodyProfileParamsPastJobsType0.from_dict(data)

                return past_jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsPastJobsType0 | None | Unset, data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))

        def _parse_languages(data: object) -> CombinedSearchCountBodyProfileParamsLanguagesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = CombinedSearchCountBodyProfileParamsLanguagesType0.from_dict(data)

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsLanguagesType0 | None | Unset, data)

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_left_stealth_at(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsLeftStealthAtType0
            | CombinedSearchCountBodyProfileParamsLeftStealthAtType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_0 = CombinedSearchCountBodyProfileParamsLeftStealthAtType0.from_dict(data)

                return left_stealth_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_1 = CombinedSearchCountBodyProfileParamsLeftStealthAtType1.from_dict(data)

                return left_stealth_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsLeftStealthAtType0
                | CombinedSearchCountBodyProfileParamsLeftStealthAtType1
                | None
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
        ) -> (
            CombinedSearchCountBodyProfileParamsStealthV2Type0
            | CombinedSearchCountBodyProfileParamsStealthV2Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = CombinedSearchCountBodyProfileParamsStealthV2Type0.from_dict(data)

                return stealth_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = CombinedSearchCountBodyProfileParamsStealthV2Type1.from_dict(data)

                return stealth_v2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsStealthV2Type0
                | CombinedSearchCountBodyProfileParamsStealthV2Type1
                | None
                | Unset,
                data,
            )

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))

        def _parse_job_status(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsJobStatusType0
            | CombinedSearchCountBodyProfileParamsJobStatusType1
            | CombinedSearchCountBodyProfileParamsJobStatusType2
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = CombinedSearchCountBodyProfileParamsJobStatusType0.from_dict(data)

                return job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = CombinedSearchCountBodyProfileParamsJobStatusType1.from_dict(data)

                return job_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = CombinedSearchCountBodyProfileParamsJobStatusType2.from_dict(data)

                return job_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsJobStatusType0
                | CombinedSearchCountBodyProfileParamsJobStatusType1
                | CombinedSearchCountBodyProfileParamsJobStatusType2
                | None
                | Unset,
                data,
            )

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))

        def _parse_time_zone(data: object) -> CombinedSearchCountBodyProfileParamsTimeZoneType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = CombinedSearchCountBodyProfileParamsTimeZoneType0.from_dict(data)

                return time_zone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsTimeZoneType0 | None | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        def _parse_past_job_text(data: object) -> CombinedSearchCountBodyProfileParamsPastJobTextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_job_text_type_0 = CombinedSearchCountBodyProfileParamsPastJobTextType0.from_dict(data)

                return past_job_text_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsPastJobTextType0 | None | Unset, data)

        past_job_text = _parse_past_job_text(d.pop("pastJobText", UNSET))

        def _parse_fuzzy_name(data: object) -> CombinedSearchCountBodyProfileParamsFuzzyNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = CombinedSearchCountBodyProfileParamsFuzzyNameType0.from_dict(data)

                return fuzzy_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsFuzzyNameType0 | None | Unset, data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))

        def _parse_company_match_mode(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsCompanyMatchModeType0
            | CombinedSearchCountBodyProfileParamsCompanyMatchModeType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_0 = CombinedSearchCountBodyProfileParamsCompanyMatchModeType0.from_dict(data)

                return company_match_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_match_mode_type_1 = CombinedSearchCountBodyProfileParamsCompanyMatchModeType1.from_dict(data)

                return company_match_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsCompanyMatchModeType0
                | CombinedSearchCountBodyProfileParamsCompanyMatchModeType1
                | None
                | Unset,
                data,
            )

        company_match_mode = _parse_company_match_mode(d.pop("companyMatchMode", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsYearsOfExperienceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = CombinedSearchCountBodyProfileParamsYearsOfExperienceType0.from_dict(data)

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsYearsOfExperienceType0 | None | Unset, data)

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))

        def _parse_job_title_v3(data: object) -> CombinedSearchCountBodyProfileParamsJobTitleV3Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = CombinedSearchCountBodyProfileParamsJobTitleV3Type0.from_dict(data)

                return job_title_v3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsJobTitleV3Type0 | None | Unset, data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))

        def _parse_has_profile_picture(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_profile_picture = _parse_has_profile_picture(d.pop("hasProfilePicture", UNSET))

        def _parse_state(data: object) -> CombinedSearchCountBodyProfileParamsStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = CombinedSearchCountBodyProfileParamsStateType0.from_dict(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsStateType0 | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_certifications(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsCertificationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                certifications_type_0 = CombinedSearchCountBodyProfileParamsCertificationsType0.from_dict(data)

                return certifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsCertificationsType0 | None | Unset, data)

        certifications = _parse_certifications(d.pop("certifications", UNSET))

        def _parse_publications(data: object) -> CombinedSearchCountBodyProfileParamsPublicationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                publications_type_0 = CombinedSearchCountBodyProfileParamsPublicationsType0.from_dict(data)

                return publications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsPublicationsType0 | None | Unset, data)

        publications = _parse_publications(d.pop("publications", UNSET))

        def _parse_has_no_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_no_education = _parse_has_no_education(d.pop("hasNoEducation", UNSET))

        def _parse_employment_type(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsEmploymentTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employment_type_type_0 = CombinedSearchCountBodyProfileParamsEmploymentTypeType0.from_dict(data)

                return employment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsEmploymentTypeType0 | None | Unset, data)

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))

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

        def _parse_tags(data: object) -> CombinedSearchCountBodyProfileParamsTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = CombinedSearchCountBodyProfileParamsTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsTagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_education(data: object) -> CombinedSearchCountBodyProfileParamsEducationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = CombinedSearchCountBodyProfileParamsEducationType0.from_dict(data)

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchCountBodyProfileParamsEducationType0 | None | Unset, data)

        education = _parse_education(d.pop("education", UNSET))

        combined_search_count_body_profile_params = cls(
            country_3_letter_code=country_3_letter_code,
            num_connections=num_connections,
            num_followers=num_followers,
            approx_age=approx_age,
            keywords=keywords,
            keywords_v2=keywords_v2,
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
            certifications=certifications,
            publications=publications,
            has_no_education=has_no_education,
            employment_type=employment_type,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
            tags=tags,
            education=education,
        )

        return combined_search_count_body_profile_params
