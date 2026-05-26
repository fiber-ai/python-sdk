from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_accelerators_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_categories_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_category_groups_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_count_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_fortune_rankings_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_country_code_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_location_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_state_name_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_industries_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_postings_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_keywords_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funding_usd_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_linkedin_industries_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_naics_codes_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_name_like_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_num_words_in_name_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_revenue_range_usd_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_sort_type_0_item import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_special_flags_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_stage_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_status_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_tags_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_v2_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_tlds_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_total_funding_usd_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParams")


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParams:
    """The company search parameters. Prospects are found from companies matching these filters.

    Attributes:
        exact_company_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0 | Unset):
        domains (list[str] | None | Unset):
        headquarters_country_code (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0 | Unset):
        headquarters_state_name (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0 | Unset):
        employee_count_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0 |
            Unset):
        keywords (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0 | Unset):
        industries_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0 | Unset):
        stage (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0 | Unset):
        total_funding_usd (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0 |
            Unset):
        last_funding_usd (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0 | Unset):
        last_funded_on (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1 | Unset):
        founded_on (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1 | Unset):
        name_like (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0 | Unset):
        exact_company (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0 | Unset):
        accelerators_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0 | Unset):
        headquarters_location (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0
            | Unset):
        linkedin_slugs (list[str] | None | Unset):
        special_flags (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0 | Unset):
        employees (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0 | Unset):
        naics_codes (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0 | Unset):
        fortune_rankings (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0 | Unset):
        job_postings_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0 | Unset):
        job_posting_stats (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0 |
            Unset):
        office_locations_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0 |
            Unset):
        tlds (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0 | Unset):
        num_words_in_name (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0 | Unset):
        status (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0 | Unset):
        technologies (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0 | Unset):
        crunchbase_categories (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0
            | Unset):
        crunchbase_category_groups (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0 | Unset):
        crunchbase_slugs (list[str] | None | Unset):
        investors_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0 | Unset):
        technologies_v2 (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0 | Unset):
        revenue_range_usd (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0 |
            Unset):
        tags (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0 | Unset):
        linkedin_industries (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0 |
            Unset):
        sort (list[PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item] | None | Unset): Sort order
            for company results. Clauses are applied in order. Omit to use the default ranking. Note: changing the sort
            invalidates any existing cursor — start a new pagination run when the sort changes.
    """

    exact_company_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0 | Unset = (
        UNSET
    )
    domains: list[str] | None | Unset = UNSET
    headquarters_country_code: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0 | Unset
    ) = UNSET
    headquarters_state_name: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0 | Unset
    ) = UNSET
    employee_count_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0 | Unset = (
        UNSET
    )
    keywords: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0 | Unset = UNSET
    industries_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0 | Unset = UNSET
    stage: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0 | Unset = UNSET
    total_funding_usd: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0 | Unset = (
        UNSET
    )
    last_funding_usd: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0 | Unset = (
        UNSET
    )
    last_funded_on: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1
        | Unset
    ) = UNSET
    founded_on: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1
        | Unset
    ) = UNSET
    name_like: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0 | Unset = UNSET
    exact_company: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0 | Unset = UNSET
    accelerators_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0 | Unset = UNSET
    headquarters_location: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0 | Unset
    ) = UNSET
    linkedin_slugs: list[str] | None | Unset = UNSET
    special_flags: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0 | Unset = UNSET
    employees: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0 | Unset = UNSET
    naics_codes: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0 | Unset = UNSET
    fortune_rankings: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0 | Unset = (
        UNSET
    )
    job_postings_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0 | Unset = UNSET
    job_posting_stats: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0 | Unset = (
        UNSET
    )
    office_locations_v2: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0 | Unset
    ) = UNSET
    tlds: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0 | Unset = UNSET
    num_words_in_name: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0 | Unset = (
        UNSET
    )
    status: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0 | Unset = UNSET
    technologies: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0 | Unset = UNSET
    crunchbase_categories: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0 | Unset
    ) = UNSET
    crunchbase_category_groups: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0 | Unset
    ) = UNSET
    crunchbase_slugs: list[str] | None | Unset = UNSET
    investors_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0 | Unset = UNSET
    technologies_v2: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0 | Unset = UNSET
    revenue_range_usd: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0 | Unset = (
        UNSET
    )
    tags: None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0 | Unset = UNSET
    linkedin_industries: (
        None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0 | Unset
    ) = UNSET
    sort: list[PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_accelerators_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_categories_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_category_groups_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_count_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_fortune_rankings_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_country_code_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_location_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_state_name_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_industries_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_postings_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_keywords_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funding_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_linkedin_industries_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_naics_codes_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_name_like_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_num_words_in_name_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_revenue_range_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_special_flags_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_stage_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_status_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_tags_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_tlds_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_total_funding_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0,
        )

        exact_company_v2: dict[str, Any] | None | Unset
        if isinstance(self.exact_company_v2, Unset):
            exact_company_v2 = UNSET
        elif isinstance(
            self.exact_company_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0
        ):
            exact_company_v2 = self.exact_company_v2.to_dict()
        else:
            exact_company_v2 = self.exact_company_v2

        domains: list[str] | None | Unset
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains

        else:
            domains = self.domains

        headquarters_country_code: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_country_code, Unset):
            headquarters_country_code = UNSET
        elif isinstance(
            self.headquarters_country_code,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0,
        ):
            headquarters_country_code = self.headquarters_country_code.to_dict()
        else:
            headquarters_country_code = self.headquarters_country_code

        headquarters_state_name: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_state_name, Unset):
            headquarters_state_name = UNSET
        elif isinstance(
            self.headquarters_state_name,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0,
        ):
            headquarters_state_name = self.headquarters_state_name.to_dict()
        else:
            headquarters_state_name = self.headquarters_state_name

        employee_count_v2: dict[str, Any] | None | Unset
        if isinstance(self.employee_count_v2, Unset):
            employee_count_v2 = UNSET
        elif isinstance(
            self.employee_count_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0
        ):
            employee_count_v2 = self.employee_count_v2.to_dict()
        else:
            employee_count_v2 = self.employee_count_v2

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        industries_v2: dict[str, Any] | None | Unset
        if isinstance(self.industries_v2, Unset):
            industries_v2 = UNSET
        elif isinstance(self.industries_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0):
            industries_v2 = self.industries_v2.to_dict()
        else:
            industries_v2 = self.industries_v2

        stage: dict[str, Any] | None | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0):
            stage = self.stage.to_dict()
        else:
            stage = self.stage

        total_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        elif isinstance(
            self.total_funding_usd, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0
        ):
            total_funding_usd = self.total_funding_usd.to_dict()
        else:
            total_funding_usd = self.total_funding_usd

        last_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.last_funding_usd, Unset):
            last_funding_usd = UNSET
        elif isinstance(
            self.last_funding_usd, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0
        ):
            last_funding_usd = self.last_funding_usd.to_dict()
        else:
            last_funding_usd = self.last_funding_usd

        last_funded_on: dict[str, Any] | None | Unset
        if isinstance(self.last_funded_on, Unset):
            last_funded_on = UNSET
        elif isinstance(
            self.last_funded_on, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0
        ):
            last_funded_on = self.last_funded_on.to_dict()
        elif isinstance(
            self.last_funded_on, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1
        ):
            last_funded_on = self.last_funded_on.to_dict()
        else:
            last_funded_on = self.last_funded_on

        founded_on: dict[str, Any] | None | Unset
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        name_like: dict[str, Any] | None | Unset
        if isinstance(self.name_like, Unset):
            name_like = UNSET
        elif isinstance(self.name_like, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0):
            name_like = self.name_like.to_dict()
        else:
            name_like = self.name_like

        exact_company: dict[str, Any] | None | Unset
        if isinstance(self.exact_company, Unset):
            exact_company = UNSET
        elif isinstance(self.exact_company, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0):
            exact_company = self.exact_company.to_dict()
        else:
            exact_company = self.exact_company

        accelerators_v2: dict[str, Any] | None | Unset
        if isinstance(self.accelerators_v2, Unset):
            accelerators_v2 = UNSET
        elif isinstance(
            self.accelerators_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0
        ):
            accelerators_v2 = self.accelerators_v2.to_dict()
        else:
            accelerators_v2 = self.accelerators_v2

        headquarters_location: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_location, Unset):
            headquarters_location = UNSET
        elif isinstance(
            self.headquarters_location,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0,
        ):
            headquarters_location = self.headquarters_location.to_dict()
        else:
            headquarters_location = self.headquarters_location

        linkedin_slugs: list[str] | None | Unset
        if isinstance(self.linkedin_slugs, Unset):
            linkedin_slugs = UNSET
        elif isinstance(self.linkedin_slugs, list):
            linkedin_slugs = self.linkedin_slugs

        else:
            linkedin_slugs = self.linkedin_slugs

        special_flags: dict[str, Any] | None | Unset
        if isinstance(self.special_flags, Unset):
            special_flags = UNSET
        elif isinstance(self.special_flags, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0):
            special_flags = self.special_flags.to_dict()
        else:
            special_flags = self.special_flags

        employees: dict[str, Any] | None | Unset
        if isinstance(self.employees, Unset):
            employees = UNSET
        elif isinstance(self.employees, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0):
            employees = self.employees.to_dict()
        else:
            employees = self.employees

        naics_codes: dict[str, Any] | None | Unset
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0):
            naics_codes = self.naics_codes.to_dict()
        else:
            naics_codes = self.naics_codes

        fortune_rankings: dict[str, Any] | None | Unset
        if isinstance(self.fortune_rankings, Unset):
            fortune_rankings = UNSET
        elif isinstance(
            self.fortune_rankings, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0
        ):
            fortune_rankings = self.fortune_rankings.to_dict()
        else:
            fortune_rankings = self.fortune_rankings

        job_postings_v2: dict[str, Any] | None | Unset
        if isinstance(self.job_postings_v2, Unset):
            job_postings_v2 = UNSET
        elif isinstance(
            self.job_postings_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0
        ):
            job_postings_v2 = self.job_postings_v2.to_dict()
        else:
            job_postings_v2 = self.job_postings_v2

        job_posting_stats: dict[str, Any] | None | Unset
        if isinstance(self.job_posting_stats, Unset):
            job_posting_stats = UNSET
        elif isinstance(
            self.job_posting_stats, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0
        ):
            job_posting_stats = self.job_posting_stats.to_dict()
        else:
            job_posting_stats = self.job_posting_stats

        office_locations_v2: dict[str, Any] | None | Unset
        if isinstance(self.office_locations_v2, Unset):
            office_locations_v2 = UNSET
        elif isinstance(
            self.office_locations_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0
        ):
            office_locations_v2 = self.office_locations_v2.to_dict()
        else:
            office_locations_v2 = self.office_locations_v2

        tlds: dict[str, Any] | None | Unset
        if isinstance(self.tlds, Unset):
            tlds = UNSET
        elif isinstance(self.tlds, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0):
            tlds = self.tlds.to_dict()
        else:
            tlds = self.tlds

        num_words_in_name: dict[str, Any] | None | Unset
        if isinstance(self.num_words_in_name, Unset):
            num_words_in_name = UNSET
        elif isinstance(
            self.num_words_in_name, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0
        ):
            num_words_in_name = self.num_words_in_name.to_dict()
        else:
            num_words_in_name = self.num_words_in_name

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        technologies: dict[str, Any] | None | Unset
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0):
            technologies = self.technologies.to_dict()
        else:
            technologies = self.technologies

        crunchbase_categories: dict[str, Any] | None | Unset
        if isinstance(self.crunchbase_categories, Unset):
            crunchbase_categories = UNSET
        elif isinstance(
            self.crunchbase_categories,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0,
        ):
            crunchbase_categories = self.crunchbase_categories.to_dict()
        else:
            crunchbase_categories = self.crunchbase_categories

        crunchbase_category_groups: dict[str, Any] | None | Unset
        if isinstance(self.crunchbase_category_groups, Unset):
            crunchbase_category_groups = UNSET
        elif isinstance(
            self.crunchbase_category_groups,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0,
        ):
            crunchbase_category_groups = self.crunchbase_category_groups.to_dict()
        else:
            crunchbase_category_groups = self.crunchbase_category_groups

        crunchbase_slugs: list[str] | None | Unset
        if isinstance(self.crunchbase_slugs, Unset):
            crunchbase_slugs = UNSET
        elif isinstance(self.crunchbase_slugs, list):
            crunchbase_slugs = self.crunchbase_slugs

        else:
            crunchbase_slugs = self.crunchbase_slugs

        investors_v2: dict[str, Any] | None | Unset
        if isinstance(self.investors_v2, Unset):
            investors_v2 = UNSET
        elif isinstance(self.investors_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0):
            investors_v2 = self.investors_v2.to_dict()
        else:
            investors_v2 = self.investors_v2

        technologies_v2: dict[str, Any] | None | Unset
        if isinstance(self.technologies_v2, Unset):
            technologies_v2 = UNSET
        elif isinstance(
            self.technologies_v2, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0
        ):
            technologies_v2 = self.technologies_v2.to_dict()
        else:
            technologies_v2 = self.technologies_v2

        revenue_range_usd: dict[str, Any] | None | Unset
        if isinstance(self.revenue_range_usd, Unset):
            revenue_range_usd = UNSET
        elif isinstance(
            self.revenue_range_usd, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0
        ):
            revenue_range_usd = self.revenue_range_usd.to_dict()
        else:
            revenue_range_usd = self.revenue_range_usd

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        linkedin_industries: dict[str, Any] | None | Unset
        if isinstance(self.linkedin_industries, Unset):
            linkedin_industries = UNSET
        elif isinstance(
            self.linkedin_industries, PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0
        ):
            linkedin_industries = self.linkedin_industries.to_dict()
        else:
            linkedin_industries = self.linkedin_industries

        sort: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, list):
            sort = []
            for sort_type_0_item_data in self.sort:
                sort_type_0_item = sort_type_0_item_data.to_dict()
                sort.append(sort_type_0_item)

        else:
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exact_company_v2 is not UNSET:
            field_dict["exactCompanyV2"] = exact_company_v2
        if domains is not UNSET:
            field_dict["domains"] = domains
        if headquarters_country_code is not UNSET:
            field_dict["headquartersCountryCode"] = headquarters_country_code
        if headquarters_state_name is not UNSET:
            field_dict["headquartersStateName"] = headquarters_state_name
        if employee_count_v2 is not UNSET:
            field_dict["employeeCountV2"] = employee_count_v2
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if industries_v2 is not UNSET:
            field_dict["industriesV2"] = industries_v2
        if stage is not UNSET:
            field_dict["stage"] = stage
        if total_funding_usd is not UNSET:
            field_dict["totalFundingUSD"] = total_funding_usd
        if last_funding_usd is not UNSET:
            field_dict["lastFundingUSD"] = last_funding_usd
        if last_funded_on is not UNSET:
            field_dict["lastFundedOn"] = last_funded_on
        if founded_on is not UNSET:
            field_dict["foundedOn"] = founded_on
        if name_like is not UNSET:
            field_dict["nameLike"] = name_like
        if exact_company is not UNSET:
            field_dict["exactCompany"] = exact_company
        if accelerators_v2 is not UNSET:
            field_dict["acceleratorsV2"] = accelerators_v2
        if headquarters_location is not UNSET:
            field_dict["headquartersLocation"] = headquarters_location
        if linkedin_slugs is not UNSET:
            field_dict["linkedinSlugs"] = linkedin_slugs
        if special_flags is not UNSET:
            field_dict["specialFlags"] = special_flags
        if employees is not UNSET:
            field_dict["employees"] = employees
        if naics_codes is not UNSET:
            field_dict["naicsCodes"] = naics_codes
        if fortune_rankings is not UNSET:
            field_dict["fortuneRankings"] = fortune_rankings
        if job_postings_v2 is not UNSET:
            field_dict["jobPostingsV2"] = job_postings_v2
        if job_posting_stats is not UNSET:
            field_dict["jobPostingStats"] = job_posting_stats
        if office_locations_v2 is not UNSET:
            field_dict["officeLocationsV2"] = office_locations_v2
        if tlds is not UNSET:
            field_dict["tlds"] = tlds
        if num_words_in_name is not UNSET:
            field_dict["numWordsInName"] = num_words_in_name
        if status is not UNSET:
            field_dict["status"] = status
        if technologies is not UNSET:
            field_dict["technologies"] = technologies
        if crunchbase_categories is not UNSET:
            field_dict["crunchbaseCategories"] = crunchbase_categories
        if crunchbase_category_groups is not UNSET:
            field_dict["crunchbaseCategoryGroups"] = crunchbase_category_groups
        if crunchbase_slugs is not UNSET:
            field_dict["crunchbaseSlugs"] = crunchbase_slugs
        if investors_v2 is not UNSET:
            field_dict["investorsV2"] = investors_v2
        if technologies_v2 is not UNSET:
            field_dict["technologiesV2"] = technologies_v2
        if revenue_range_usd is not UNSET:
            field_dict["revenueRangeUSD"] = revenue_range_usd
        if tags is not UNSET:
            field_dict["tags"] = tags
        if linkedin_industries is not UNSET:
            field_dict["linkedinIndustries"] = linkedin_industries
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_accelerators_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_categories_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_crunchbase_category_groups_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_count_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_exact_company_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_fortune_rankings_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_founded_on_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_country_code_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_location_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_headquarters_state_name_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_industries_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_postings_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_keywords_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funded_on_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_last_funding_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_linkedin_industries_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_naics_codes_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_name_like_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_num_words_in_name_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_revenue_range_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_sort_type_0_item import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_special_flags_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_stage_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_status_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_tags_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_technologies_v2_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_tlds_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0,
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_total_funding_usd_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0,
        )

        d = dict(src_dict)

        def _parse_exact_company_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0.from_dict(data)
                )

                return exact_company_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyV2Type0 | Unset, data
            )

        exact_company_v2 = _parse_exact_company_v2(d.pop("exactCompanyV2", UNSET))

        def _parse_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        domains = _parse_domains(d.pop("domains", UNSET))

        def _parse_headquarters_country_code(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_country_code_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0.from_dict(
                        data
                    )
                )

                return headquarters_country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersCountryCodeType0 | Unset,
                data,
            )

        headquarters_country_code = _parse_headquarters_country_code(d.pop("headquartersCountryCode", UNSET))

        def _parse_headquarters_state_name(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_state_name_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0.from_dict(data)
                )

                return headquarters_state_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersStateNameType0 | Unset, data
            )

        headquarters_state_name = _parse_headquarters_state_name(d.pop("headquartersStateName", UNSET))

        def _parse_employee_count_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0.from_dict(data)
                )

                return employee_count_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeCountV2Type0 | Unset, data
            )

        employee_count_v2 = _parse_employee_count_v2(d.pop("employeeCountV2", UNSET))

        def _parse_keywords(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0.from_dict(data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsKeywordsType0 | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_industries_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industries_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0.from_dict(data)
                )

                return industries_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsIndustriesV2Type0 | Unset, data)

        industries_v2 = _parse_industries_v2(d.pop("industriesV2", UNSET))

        def _parse_stage(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stage_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0.from_dict(data)

                return stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStageType0 | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_total_funding_usd(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_funding_usd_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0.from_dict(data)
                )

                return total_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTotalFundingUSDType0 | Unset, data
            )

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUSD", UNSET))

        def _parse_last_funding_usd(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funding_usd_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0.from_dict(data)
                )

                return last_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundingUSDType0 | Unset, data
            )

        last_funding_usd = _parse_last_funding_usd(d.pop("lastFundingUSD", UNSET))

        def _parse_last_funded_on(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0.from_dict(data)
                )

                return last_funded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_1 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1.from_dict(data)
                )

                return last_funded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType0
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLastFundedOnType1
                | Unset,
                data,
            )

        last_funded_on = _parse_last_funded_on(d.pop("lastFundedOn", UNSET))

        def _parse_founded_on(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0.from_dict(
                    data
                )

                return founded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1.from_dict(
                    data
                )

                return founded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType0
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFoundedOnType1
                | Unset,
                data,
            )

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))

        def _parse_name_like(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_like_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0.from_dict(
                    data
                )

                return name_like_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNameLikeType0 | Unset, data)

        name_like = _parse_name_like(d.pop("nameLike", UNSET))

        def _parse_exact_company(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0.from_dict(data)
                )

                return exact_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsExactCompanyType0 | Unset, data)

        exact_company = _parse_exact_company(d.pop("exactCompany", UNSET))

        def _parse_accelerators_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accelerators_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0.from_dict(data)
                )

                return accelerators_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsAcceleratorsV2Type0 | Unset, data
            )

        accelerators_v2 = _parse_accelerators_v2(d.pop("acceleratorsV2", UNSET))

        def _parse_headquarters_location(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_location_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0.from_dict(data)
                )

                return headquarters_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsHeadquartersLocationType0 | Unset, data
            )

        headquarters_location = _parse_headquarters_location(d.pop("headquartersLocation", UNSET))

        def _parse_linkedin_slugs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_slugs_type_0 = cast(list[str], data)

                return linkedin_slugs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        linkedin_slugs = _parse_linkedin_slugs(d.pop("linkedinSlugs", UNSET))

        def _parse_special_flags(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                special_flags_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0.from_dict(data)
                )

                return special_flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSpecialFlagsType0 | Unset, data)

        special_flags = _parse_special_flags(d.pop("specialFlags", UNSET))

        def _parse_employees(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employees_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0.from_dict(
                    data
                )

                return employees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0 | Unset, data)

        employees = _parse_employees(d.pop("employees", UNSET))

        def _parse_naics_codes(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                naics_codes_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0.from_dict(
                    data
                )

                return naics_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNaicsCodesType0 | Unset, data)

        naics_codes = _parse_naics_codes(d.pop("naicsCodes", UNSET))

        def _parse_fortune_rankings(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fortune_rankings_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0.from_dict(data)
                )

                return fortune_rankings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFortuneRankingsType0 | Unset, data
            )

        fortune_rankings = _parse_fortune_rankings(d.pop("fortuneRankings", UNSET))

        def _parse_job_postings_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0.from_dict(data)
                )

                return job_postings_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0 | Unset, data
            )

        job_postings_v2 = _parse_job_postings_v2(d.pop("jobPostingsV2", UNSET))

        def _parse_job_posting_stats(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_posting_stats_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0.from_dict(data)
                )

                return job_posting_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0 | Unset, data
            )

        job_posting_stats = _parse_job_posting_stats(d.pop("jobPostingStats", UNSET))

        def _parse_office_locations_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                office_locations_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0.from_dict(data)
                )

                return office_locations_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0 | Unset, data
            )

        office_locations_v2 = _parse_office_locations_v2(d.pop("officeLocationsV2", UNSET))

        def _parse_tlds(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tlds_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0.from_dict(data)

                return tlds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTldsType0 | Unset, data)

        tlds = _parse_tlds(d.pop("tlds", UNSET))

        def _parse_num_words_in_name(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_words_in_name_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0.from_dict(data)
                )

                return num_words_in_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsNumWordsInNameType0 | Unset, data
            )

        num_words_in_name = _parse_num_words_in_name(d.pop("numWordsInName", UNSET))

        def _parse_status(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0.from_dict(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsStatusType0 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_technologies(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0.from_dict(data)
                )

                return technologies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesType0 | Unset, data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))

        def _parse_crunchbase_categories(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_categories_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0.from_dict(data)
                )

                return crunchbase_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoriesType0 | Unset, data
            )

        crunchbase_categories = _parse_crunchbase_categories(d.pop("crunchbaseCategories", UNSET))

        def _parse_crunchbase_category_groups(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_category_groups_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0.from_dict(
                        data
                    )
                )

                return crunchbase_category_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsCrunchbaseCategoryGroupsType0 | Unset,
                data,
            )

        crunchbase_category_groups = _parse_crunchbase_category_groups(d.pop("crunchbaseCategoryGroups", UNSET))

        def _parse_crunchbase_slugs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crunchbase_slugs_type_0 = cast(list[str], data)

                return crunchbase_slugs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        crunchbase_slugs = _parse_crunchbase_slugs(d.pop("crunchbaseSlugs", UNSET))

        def _parse_investors_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0.from_dict(data)
                )

                return investors_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0 | Unset, data)

        investors_v2 = _parse_investors_v2(d.pop("investorsV2", UNSET))

        def _parse_technologies_v2(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_v2_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0.from_dict(data)
                )

                return technologies_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTechnologiesV2Type0 | Unset, data
            )

        technologies_v2 = _parse_technologies_v2(d.pop("technologiesV2", UNSET))

        def _parse_revenue_range_usd(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_range_usd_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0.from_dict(data)
                )

                return revenue_range_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsRevenueRangeUSDType0 | Unset, data
            )

        revenue_range_usd = _parse_revenue_range_usd(d.pop("revenueRangeUSD", UNSET))

        def _parse_tags(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsTagsType0 | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_linkedin_industries(
            data: object,
        ) -> None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linkedin_industries_type_0 = (
                    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0.from_dict(data)
                )

                return linkedin_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsLinkedinIndustriesType0 | Unset, data
            )

        linkedin_industries = _parse_linkedin_industries(d.pop("linkedinIndustries", UNSET))

        def _parse_sort(
            data: object,
        ) -> list[PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_type_0 = []
                _sort_type_0 = data
                for sort_type_0_item_data in _sort_type_0:
                    sort_type_0_item = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item.from_dict(
                        sort_type_0_item_data
                    )

                    sort_type_0.append(sort_type_0_item)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsSortType0Item] | None | Unset, data
            )

        sort = _parse_sort(d.pop("sort", UNSET))

        paginated_combined_search_body_company_config_type_0_search_params = cls(
            exact_company_v2=exact_company_v2,
            domains=domains,
            headquarters_country_code=headquarters_country_code,
            headquarters_state_name=headquarters_state_name,
            employee_count_v2=employee_count_v2,
            keywords=keywords,
            industries_v2=industries_v2,
            stage=stage,
            total_funding_usd=total_funding_usd,
            last_funding_usd=last_funding_usd,
            last_funded_on=last_funded_on,
            founded_on=founded_on,
            name_like=name_like,
            exact_company=exact_company,
            accelerators_v2=accelerators_v2,
            headquarters_location=headquarters_location,
            linkedin_slugs=linkedin_slugs,
            special_flags=special_flags,
            employees=employees,
            naics_codes=naics_codes,
            fortune_rankings=fortune_rankings,
            job_postings_v2=job_postings_v2,
            job_posting_stats=job_posting_stats,
            office_locations_v2=office_locations_v2,
            tlds=tlds,
            num_words_in_name=num_words_in_name,
            status=status,
            technologies=technologies,
            crunchbase_categories=crunchbase_categories,
            crunchbase_category_groups=crunchbase_category_groups,
            crunchbase_slugs=crunchbase_slugs,
            investors_v2=investors_v2,
            technologies_v2=technologies_v2,
            revenue_range_usd=revenue_range_usd,
            tags=tags,
            linkedin_industries=linkedin_industries,
            sort=sort,
        )

        paginated_combined_search_body_company_config_type_0_search_params.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params

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
