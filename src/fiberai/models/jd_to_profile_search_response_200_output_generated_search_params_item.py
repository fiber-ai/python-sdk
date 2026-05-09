from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_approx_age_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_country_3_letter_code_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_education_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_fuzzy_name_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_1 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_2 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_title_v3_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keyword_search_options_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_languages_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_location_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_connections_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_followers_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_past_jobs_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_1 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_1 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_state_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_1 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_tags_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_time_zone_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_years_of_experience_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0,
    )


T = TypeVar("T", bound="JdToProfileSearchResponse200OutputGeneratedSearchParamsItem")


@_attrs_define
class JdToProfileSearchResponse200OutputGeneratedSearchParamsItem:
    """
    Attributes:
        job_title_v3 (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0 | None | Unset):
        job_status (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0 |
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1 |
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2 | None | Unset):
        approx_age (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0 | None | Unset):
        started_in_role (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0 |
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1 | None | Unset):
        started_at_company (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0 |
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1 | None | Unset):
        years_of_experience (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0 | None |
            Unset):
        keywords (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0 | None | Unset):
        keyword_search_options (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0 |
            None | Unset):
        fuzzy_name (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0 | None | Unset):
        tags (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0 | None | Unset):
        stealth_v2 (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0 |
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1 | None | Unset):
        country_3_letter_code (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0 | None
            | Unset):
        location (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0 | None | Unset):
        time_zone (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0 | None | Unset):
        education (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0 | None | Unset):
        languages (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0 | None | Unset):
        past_jobs (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0 | None | Unset):
        num_connections (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0 | None | Unset):
        num_followers (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0 | None | Unset):
        max_people_per_company (float | None | Unset):
        state (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0 | None | Unset):
        keywords_v2 (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0 | None | Unset):
    """

    job_title_v3: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0 | None | Unset = UNSET
    job_status: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0
        | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1
        | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2
        | None
        | Unset
    ) = UNSET
    approx_age: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0 | None | Unset = UNSET
    started_in_role: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0
        | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1
        | None
        | Unset
    ) = UNSET
    started_at_company: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0
        | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1
        | None
        | Unset
    ) = UNSET
    years_of_experience: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0 | None | Unset
    ) = UNSET
    keywords: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0 | None | Unset = UNSET
    keyword_search_options: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0 | None | Unset
    ) = UNSET
    fuzzy_name: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0 | None | Unset = UNSET
    tags: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0 | None | Unset = UNSET
    stealth_v2: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0
        | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1
        | None
        | Unset
    ) = UNSET
    country_3_letter_code: (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0 | None | Unset
    ) = UNSET
    location: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0 | None | Unset = UNSET
    time_zone: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0 | None | Unset = UNSET
    education: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0 | None | Unset = UNSET
    languages: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0 | None | Unset = UNSET
    past_jobs: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0 | None | Unset = UNSET
    num_connections: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0 | None | Unset = (
        UNSET
    )
    num_followers: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0 | None | Unset = UNSET
    max_people_per_company: float | None | Unset = UNSET
    state: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0 | None | Unset = UNSET
    keywords_v2: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_approx_age_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_country_3_letter_code_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_education_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_fuzzy_name_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_2 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_title_v3_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keyword_search_options_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_languages_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_location_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_connections_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_followers_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_past_jobs_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_state_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_tags_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_time_zone_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_years_of_experience_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0,
        )

        job_title_v3: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(self.job_title_v3, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        job_status: dict[str, Any] | None | Unset
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(self.job_status, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1):
            job_status = self.job_status.to_dict()
        elif isinstance(self.job_status, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        approx_age: dict[str, Any] | None | Unset
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(self.approx_age, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        started_in_role: dict[str, Any] | None | Unset
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(
            self.started_in_role, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0
        ):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(
            self.started_in_role, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1
        ):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: dict[str, Any] | None | Unset
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(
            self.started_at_company, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0
        ):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(
            self.started_at_company, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1
        ):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(
            self.years_of_experience, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0
        ):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: dict[str, Any] | None | Unset
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(
            self.keyword_search_options,
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0,
        ):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        fuzzy_name: dict[str, Any] | None | Unset
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(self.fuzzy_name, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        stealth_v2: dict[str, Any] | None | Unset
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(self.stealth_v2, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(self.stealth_v2, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        country_3_letter_code: dict[str, Any] | None | Unset
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(
            self.country_3_letter_code,
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0,
        ):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        time_zone: dict[str, Any] | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        education: dict[str, Any] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0):
            education = self.education.to_dict()
        else:
            education = self.education

        languages: dict[str, Any] | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        past_jobs: dict[str, Any] | None | Unset
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(self.past_jobs, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        num_connections: dict[str, Any] | None | Unset
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(
            self.num_connections, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0
        ):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: dict[str, Any] | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(
            self.num_followers, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0
        ):
            num_followers = self.num_followers.to_dict()
        else:
            num_followers = self.num_followers

        max_people_per_company: float | None | Unset
        if isinstance(self.max_people_per_company, Unset):
            max_people_per_company = UNSET
        else:
            max_people_per_company = self.max_people_per_company

        state: dict[str, Any] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        keywords_v2: dict[str, Any] | None | Unset
        if isinstance(self.keywords_v2, Unset):
            keywords_v2 = UNSET
        elif isinstance(self.keywords_v2, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0):
            keywords_v2 = self.keywords_v2.to_dict()
        else:
            keywords_v2 = self.keywords_v2

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        if state is not UNSET:
            field_dict["state"] = state
        if keywords_v2 is not UNSET:
            field_dict["keywordsV2"] = keywords_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_approx_age_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_country_3_letter_code_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_education_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_fuzzy_name_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_status_type_2 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_job_title_v3_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keyword_search_options_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_languages_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_location_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_connections_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_num_followers_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_past_jobs_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_at_company_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_started_in_role_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_state_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_stealth_v2_type_1 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_tags_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_time_zone_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_years_of_experience_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0,
        )

        d = dict(src_dict)

        def _parse_job_title_v3(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0.from_dict(data)
                )

                return job_title_v3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobTitleV3Type0 | None | Unset, data)

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))

        def _parse_job_status(
            data: object,
        ) -> (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0
            | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1
            | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2
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
                job_status_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0.from_dict(
                    data
                )

                return job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1.from_dict(
                    data
                )

                return job_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2.from_dict(
                    data
                )

                return job_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType0
                | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType1
                | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemJobStatusType2
                | None
                | Unset,
                data,
            )

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))

        def _parse_approx_age(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0.from_dict(
                    data
                )

                return approx_age_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemApproxAgeType0 | None | Unset, data)

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))

        def _parse_started_in_role(
            data: object,
        ) -> (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0
            | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1
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
                started_in_role_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0.from_dict(data)
                )

                return started_in_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1.from_dict(data)
                )

                return started_in_role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType0
                | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedInRoleType1
                | None
                | Unset,
                data,
            )

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))

        def _parse_started_at_company(
            data: object,
        ) -> (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0
            | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1
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
                started_at_company_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0.from_dict(data)
                )

                return started_at_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1.from_dict(data)
                )

                return started_at_company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType0
                | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStartedAtCompanyType1
                | None
                | Unset,
                data,
            )

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0.from_dict(data)
                )

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemYearsOfExperienceType0 | None | Unset, data
            )

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))

        def _parse_keywords(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0.from_dict(
                    data
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsType0 | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_keyword_search_options(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0.from_dict(data)
                )

                return keyword_search_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordSearchOptionsType0 | None | Unset,
                data,
            )

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))

        def _parse_fuzzy_name(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0.from_dict(
                    data
                )

                return fuzzy_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemFuzzyNameType0 | None | Unset, data)

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))

        def _parse_tags(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_stealth_v2(
            data: object,
        ) -> (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0
            | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1
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
                stealth_v2_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0.from_dict(
                    data
                )

                return stealth_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1.from_dict(
                    data
                )

                return stealth_v2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type0
                | JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStealthV2Type1
                | None
                | Unset,
                data,
            )

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))

        def _parse_country_3_letter_code(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0.from_dict(data)
                )

                return country_3_letter_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemCountry3LetterCodeType0 | None | Unset, data
            )

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))

        def _parse_location(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0.from_dict(
                    data
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLocationType0 | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_time_zone(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0.from_dict(
                    data
                )

                return time_zone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemTimeZoneType0 | None | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        def _parse_education(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0.from_dict(
                    data
                )

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemEducationType0 | None | Unset, data)

        education = _parse_education(d.pop("education", UNSET))

        def _parse_languages(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0.from_dict(
                    data
                )

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemLanguagesType0 | None | Unset, data)

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_past_jobs(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0.from_dict(
                    data
                )

                return past_jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemPastJobsType0 | None | Unset, data)

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))

        def _parse_num_connections(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0.from_dict(data)
                )

                return num_connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumConnectionsType0 | None | Unset, data
            )

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))

        def _parse_num_followers(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0.from_dict(data)
                )

                return num_followers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemNumFollowersType0 | None | Unset, data
            )

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))

        def _parse_max_people_per_company(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_people_per_company = _parse_max_people_per_company(d.pop("maxPeoplePerCompany", UNSET))

        def _parse_state(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0.from_dict(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemStateType0 | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_keywords_v2(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_v2_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0.from_dict(data)
                )

                return keywords_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0 | None | Unset, data)

        keywords_v2 = _parse_keywords_v2(d.pop("keywordsV2", UNSET))

        jd_to_profile_search_response_200_output_generated_search_params_item = cls(
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
            state=state,
            keywords_v2=keywords_v2,
        )

        return jd_to_profile_search_response_200_output_generated_search_params_item
