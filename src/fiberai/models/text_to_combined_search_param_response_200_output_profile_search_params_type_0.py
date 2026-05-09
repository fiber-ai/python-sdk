from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_approx_age_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_1 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_2 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_v2_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_languages_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_location_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_connections_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_followers_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_past_jobs_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_1 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_1 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_state_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_tags_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_time_zone_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0")


@_attrs_define
class TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0:
    """
    Attributes:
        job_title_v3 (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0 | Unset):
        job_status (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0 |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1 |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2 | Unset):
        approx_age (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0 | Unset):
        started_in_role (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0 |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1 | Unset):
        started_at_company (None |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0 |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1 | Unset):
        years_of_experience (None |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0 | Unset):
        keywords (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0 | Unset):
        keyword_search_options (None |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0 | Unset):
        fuzzy_name (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0 | Unset):
        tags (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0 | Unset):
        stealth_v2 (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0 |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1 | Unset):
        country_3_letter_code (None |
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0 | Unset):
        location (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0 | Unset):
        time_zone (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0 | Unset):
        education (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0 | Unset):
        languages (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0 | Unset):
        past_jobs (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0 | Unset):
        num_connections (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0 |
            Unset):
        num_followers (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0 |
            Unset):
        max_people_per_company (float | None | Unset):
        state (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0 | Unset):
        keywords_v2 (None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0 | Unset):
    """

    job_title_v3: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0 | Unset = (
        UNSET
    )
    job_status: (
        None
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2
        | Unset
    ) = UNSET
    approx_age: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0 | Unset = UNSET
    started_in_role: (
        None
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1
        | Unset
    ) = UNSET
    started_at_company: (
        None
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
        | Unset
    ) = UNSET
    years_of_experience: (
        None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0 | Unset
    ) = UNSET
    keywords: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0 | Unset = UNSET
    keyword_search_options: (
        None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0 | Unset
    ) = UNSET
    fuzzy_name: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0 | Unset = UNSET
    tags: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0 | Unset = UNSET
    stealth_v2: (
        None
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0
        | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1
        | Unset
    ) = UNSET
    country_3_letter_code: (
        None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0 | Unset
    ) = UNSET
    location: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0 | Unset = UNSET
    time_zone: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0 | Unset = UNSET
    education: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0 | Unset = UNSET
    languages: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0 | Unset = UNSET
    past_jobs: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0 | Unset = UNSET
    num_connections: (
        None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0 | Unset
    ) = UNSET
    num_followers: (
        None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0 | Unset
    ) = UNSET
    max_people_per_company: float | None | Unset = UNSET
    state: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0 | Unset = UNSET
    keywords_v2: None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0 | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_approx_age_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_2 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_v2_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_languages_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_location_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_connections_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_followers_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_past_jobs_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_state_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_tags_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_time_zone_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0,
        )

        job_title_v3: dict[str, Any] | None | Unset
        if isinstance(self.job_title_v3, Unset):
            job_title_v3 = UNSET
        elif isinstance(
            self.job_title_v3, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0
        ):
            job_title_v3 = self.job_title_v3.to_dict()
        else:
            job_title_v3 = self.job_title_v3

        job_status: dict[str, Any] | None | Unset
        if isinstance(self.job_status, Unset):
            job_status = UNSET
        elif isinstance(
            self.job_status, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0
        ):
            job_status = self.job_status.to_dict()
        elif isinstance(
            self.job_status, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1
        ):
            job_status = self.job_status.to_dict()
        elif isinstance(
            self.job_status, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2
        ):
            job_status = self.job_status.to_dict()
        else:
            job_status = self.job_status

        approx_age: dict[str, Any] | None | Unset
        if isinstance(self.approx_age, Unset):
            approx_age = UNSET
        elif isinstance(
            self.approx_age, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0
        ):
            approx_age = self.approx_age.to_dict()
        else:
            approx_age = self.approx_age

        started_in_role: dict[str, Any] | None | Unset
        if isinstance(self.started_in_role, Unset):
            started_in_role = UNSET
        elif isinstance(
            self.started_in_role, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0
        ):
            started_in_role = self.started_in_role.to_dict()
        elif isinstance(
            self.started_in_role, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1
        ):
            started_in_role = self.started_in_role.to_dict()
        else:
            started_in_role = self.started_in_role

        started_at_company: dict[str, Any] | None | Unset
        if isinstance(self.started_at_company, Unset):
            started_at_company = UNSET
        elif isinstance(
            self.started_at_company,
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0,
        ):
            started_at_company = self.started_at_company.to_dict()
        elif isinstance(
            self.started_at_company,
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1,
        ):
            started_at_company = self.started_at_company.to_dict()
        else:
            started_at_company = self.started_at_company

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(
            self.years_of_experience,
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0,
        ):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        keyword_search_options: dict[str, Any] | None | Unset
        if isinstance(self.keyword_search_options, Unset):
            keyword_search_options = UNSET
        elif isinstance(
            self.keyword_search_options,
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0,
        ):
            keyword_search_options = self.keyword_search_options.to_dict()
        else:
            keyword_search_options = self.keyword_search_options

        fuzzy_name: dict[str, Any] | None | Unset
        if isinstance(self.fuzzy_name, Unset):
            fuzzy_name = UNSET
        elif isinstance(
            self.fuzzy_name, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0
        ):
            fuzzy_name = self.fuzzy_name.to_dict()
        else:
            fuzzy_name = self.fuzzy_name

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        stealth_v2: dict[str, Any] | None | Unset
        if isinstance(self.stealth_v2, Unset):
            stealth_v2 = UNSET
        elif isinstance(
            self.stealth_v2, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0
        ):
            stealth_v2 = self.stealth_v2.to_dict()
        elif isinstance(
            self.stealth_v2, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1
        ):
            stealth_v2 = self.stealth_v2.to_dict()
        else:
            stealth_v2 = self.stealth_v2

        country_3_letter_code: dict[str, Any] | None | Unset
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        elif isinstance(
            self.country_3_letter_code,
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0,
        ):
            country_3_letter_code = self.country_3_letter_code.to_dict()
        else:
            country_3_letter_code = self.country_3_letter_code

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        time_zone: dict[str, Any] | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(
            self.time_zone, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0
        ):
            time_zone = self.time_zone.to_dict()
        else:
            time_zone = self.time_zone

        education: dict[str, Any] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(
            self.education, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0
        ):
            education = self.education.to_dict()
        else:
            education = self.education

        languages: dict[str, Any] | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(
            self.languages, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0
        ):
            languages = self.languages.to_dict()
        else:
            languages = self.languages

        past_jobs: dict[str, Any] | None | Unset
        if isinstance(self.past_jobs, Unset):
            past_jobs = UNSET
        elif isinstance(
            self.past_jobs, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0
        ):
            past_jobs = self.past_jobs.to_dict()
        else:
            past_jobs = self.past_jobs

        num_connections: dict[str, Any] | None | Unset
        if isinstance(self.num_connections, Unset):
            num_connections = UNSET
        elif isinstance(
            self.num_connections, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0
        ):
            num_connections = self.num_connections.to_dict()
        else:
            num_connections = self.num_connections

        num_followers: dict[str, Any] | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        elif isinstance(
            self.num_followers, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0
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
        elif isinstance(self.state, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0):
            state = self.state.to_dict()
        else:
            state = self.state

        keywords_v2: dict[str, Any] | None | Unset
        if isinstance(self.keywords_v2, Unset):
            keywords_v2 = UNSET
        elif isinstance(
            self.keywords_v2, TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0
        ):
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
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_approx_age_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_country_3_letter_code_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_fuzzy_name_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_status_type_2 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_job_title_v3_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keyword_search_options_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_keywords_v2_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_languages_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_location_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_connections_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_num_followers_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_past_jobs_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_at_company_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_started_in_role_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_state_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_stealth_v2_type_1 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_tags_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_time_zone_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_years_of_experience_type_0 import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0,
        )

        d = dict(src_dict)

        def _parse_job_title_v3(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_v3_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0.from_dict(data)
                )

                return job_title_v3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobTitleV3Type0 | Unset, data
            )

        job_title_v3 = _parse_job_title_v3(d.pop("jobTitleV3", UNSET))

        def _parse_job_status(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0.from_dict(data)
                )

                return job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_1 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1.from_dict(data)
                )

                return job_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_status_type_2 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2.from_dict(data)
                )

                return job_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType0
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType1
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0JobStatusType2
                | Unset,
                data,
            )

        job_status = _parse_job_status(d.pop("jobStatus", UNSET))

        def _parse_approx_age(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approx_age_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0.from_dict(data)
                )

                return approx_age_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0ApproxAgeType0 | Unset, data
            )

        approx_age = _parse_approx_age(d.pop("approxAge", UNSET))

        def _parse_started_in_role(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1
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
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0.from_dict(data)
                )

                return started_in_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_in_role_type_1 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1.from_dict(data)
                )

                return started_in_role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType0
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedInRoleType1
                | Unset,
                data,
            )

        started_in_role = _parse_started_in_role(d.pop("startedInRole", UNSET))

        def _parse_started_at_company(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
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
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0.from_dict(
                        data
                    )
                )

                return started_at_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_at_company_type_1 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1.from_dict(
                        data
                    )
                )

                return started_at_company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType0
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StartedAtCompanyType1
                | Unset,
                data,
            )

        started_at_company = _parse_started_at_company(d.pop("startedAtCompany", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0.from_dict(
                        data
                    )
                )

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0YearsOfExperienceType0 | Unset,
                data,
            )

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))

        def _parse_keywords(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0.from_dict(data)
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsType0 | Unset, data
            )

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_keyword_search_options(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_search_options_type_0 = TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0.from_dict(
                    data
                )

                return keyword_search_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0
                | Unset,
                data,
            )

        keyword_search_options = _parse_keyword_search_options(d.pop("keywordSearchOptions", UNSET))

        def _parse_fuzzy_name(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fuzzy_name_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0.from_dict(data)
                )

                return fuzzy_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0FuzzyNameType0 | Unset, data
            )

        fuzzy_name = _parse_fuzzy_name(d.pop("fuzzyName", UNSET))

        def _parse_tags(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0.from_dict(
                    data
                )

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TagsType0 | Unset, data
            )

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_stealth_v2(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0
            | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0.from_dict(data)
                )

                return stealth_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_v2_type_1 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1.from_dict(data)
                )

                return stealth_v2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type0
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StealthV2Type1
                | Unset,
                data,
            )

        stealth_v2 = _parse_stealth_v2(d.pop("stealthV2", UNSET))

        def _parse_country_3_letter_code(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_3_letter_code_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0.from_dict(
                        data
                    )
                )

                return country_3_letter_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0Country3LetterCodeType0
                | Unset,
                data,
            )

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))

        def _parse_location(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0.from_dict(data)
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LocationType0 | Unset, data
            )

        location = _parse_location(d.pop("location", UNSET))

        def _parse_time_zone(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_zone_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0.from_dict(data)
                )

                return time_zone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0TimeZoneType0 | Unset, data
            )

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        def _parse_education(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                education_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0.from_dict(data)
                )

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0 | Unset, data
            )

        education = _parse_education(d.pop("education", UNSET))

        def _parse_languages(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                languages_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0.from_dict(data)
                )

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0LanguagesType0 | Unset, data
            )

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_past_jobs(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                past_jobs_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0.from_dict(data)
                )

                return past_jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0PastJobsType0 | Unset, data
            )

        past_jobs = _parse_past_jobs(d.pop("pastJobs", UNSET))

        def _parse_num_connections(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_connections_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0.from_dict(
                        data
                    )
                )

                return num_connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumConnectionsType0 | Unset,
                data,
            )

        num_connections = _parse_num_connections(d.pop("numConnections", UNSET))

        def _parse_num_followers(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_followers_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0.from_dict(data)
                )

                return num_followers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0NumFollowersType0 | Unset, data
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
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0.from_dict(
                    data
                )

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0StateType0 | Unset, data
            )

        state = _parse_state(d.pop("state", UNSET))

        def _parse_keywords_v2(
            data: object,
        ) -> None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_v2_type_0 = (
                    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0.from_dict(data)
                )

                return keywords_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0KeywordsV2Type0 | Unset, data
            )

        keywords_v2 = _parse_keywords_v2(d.pop("keywordsV2", UNSET))

        text_to_combined_search_param_response_200_output_profile_search_params_type_0 = cls(
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

        return text_to_combined_search_param_response_200_output_profile_search_params_type_0
