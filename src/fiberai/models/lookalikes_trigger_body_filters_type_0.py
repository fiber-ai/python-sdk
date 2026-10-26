from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_trigger_body_filters_type_0_accelerators_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_categories_type_0 import (
        LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_category_groups_type_0 import (
        LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_employee_count_ranges_type_0 import (
        LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_employee_count_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_employee_trends_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_fortune_rankings_type_0 import (
        LookalikesTriggerBodyFiltersType0FortuneRankingsType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_0 import (
        LookalikesTriggerBodyFiltersType0FoundedOnType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_1 import (
        LookalikesTriggerBodyFiltersType0FoundedOnType1,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_headquarters_country_code_type_0 import (
        LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_headquarters_location_type_0 import (
        LookalikesTriggerBodyFiltersType0HeadquartersLocationType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_headquarters_state_name_type_0 import (
        LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_industries_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0IndustriesV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0InvestorsV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_job_posting_stats_type_0 import (
        LookalikesTriggerBodyFiltersType0JobPostingStatsType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_job_postings_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0JobPostingsV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_keywords_type_0 import (
        LookalikesTriggerBodyFiltersType0KeywordsType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_0 import (
        LookalikesTriggerBodyFiltersType0LastFundedOnType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_1 import (
        LookalikesTriggerBodyFiltersType0LastFundedOnType1,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_last_funding_usd_type_0 import (
        LookalikesTriggerBodyFiltersType0LastFundingUSDType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_linkedin_industries_type_0 import (
        LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_naics_codes_type_0 import (
        LookalikesTriggerBodyFiltersType0NaicsCodesType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_name_like_type_0 import (
        LookalikesTriggerBodyFiltersType0NameLikeType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_num_words_in_name_type_0 import (
        LookalikesTriggerBodyFiltersType0NumWordsInNameType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_office_locations_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_revenue_range_usd_type_0 import (
        LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_revenue_ranges_usd_type_0 import (
        LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_special_flags_type_0 import (
        LookalikesTriggerBodyFiltersType0SpecialFlagsType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_stage_type_0 import LookalikesTriggerBodyFiltersType0StageType0
    from ..models.lookalikes_trigger_body_filters_type_0_status_type_0 import (
        LookalikesTriggerBodyFiltersType0StatusType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_tags_type_0 import LookalikesTriggerBodyFiltersType0TagsType0
    from ..models.lookalikes_trigger_body_filters_type_0_technologies_type_0 import (
        LookalikesTriggerBodyFiltersType0TechnologiesType0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_technologies_v2_type_0 import (
        LookalikesTriggerBodyFiltersType0TechnologiesV2Type0,
    )
    from ..models.lookalikes_trigger_body_filters_type_0_tlds_type_0 import LookalikesTriggerBodyFiltersType0TldsType0
    from ..models.lookalikes_trigger_body_filters_type_0_total_funding_usd_type_0 import (
        LookalikesTriggerBodyFiltersType0TotalFundingUSDType0,
    )


T = TypeVar("T", bound="LookalikesTriggerBodyFiltersType0")


@_attrs_define
class LookalikesTriggerBodyFiltersType0:
    """Only return lookalikes that match these company search filters — the same object company search takes, so you can
    reuse your company search filters as-is. Filters that pick specific companies and employee-based filters are not
    accepted; use exclusion lists to leave companies out. A filter you set replaces that part of each grouping's own
    search (lists you exclude are added to it). Omit to return lookalikes of any kind.

        Attributes:
            headquarters_country_code (LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0 | None | Unset):
            headquarters_state_name (LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0 | None | Unset):
            employee_count_v2 (LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0 | None | Unset):
            employee_count_ranges (LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0 | None | Unset):
            keywords (LookalikesTriggerBodyFiltersType0KeywordsType0 | None | Unset):
            industries_v2 (LookalikesTriggerBodyFiltersType0IndustriesV2Type0 | None | Unset):
            stage (LookalikesTriggerBodyFiltersType0StageType0 | None | Unset):
            total_funding_usd (LookalikesTriggerBodyFiltersType0TotalFundingUSDType0 | None | Unset):
            last_funding_usd (LookalikesTriggerBodyFiltersType0LastFundingUSDType0 | None | Unset):
            last_funded_on (LookalikesTriggerBodyFiltersType0LastFundedOnType0 |
                LookalikesTriggerBodyFiltersType0LastFundedOnType1 | None | Unset):
            founded_on (LookalikesTriggerBodyFiltersType0FoundedOnType0 | LookalikesTriggerBodyFiltersType0FoundedOnType1 |
                None | Unset):
            name_like (LookalikesTriggerBodyFiltersType0NameLikeType0 | None | Unset):
            accelerators_v2 (LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0 | None | Unset):
            headquarters_location (LookalikesTriggerBodyFiltersType0HeadquartersLocationType0 | None | Unset):
            special_flags (LookalikesTriggerBodyFiltersType0SpecialFlagsType0 | None | Unset):
            naics_codes (LookalikesTriggerBodyFiltersType0NaicsCodesType0 | None | Unset):
            fortune_rankings (LookalikesTriggerBodyFiltersType0FortuneRankingsType0 | None | Unset):
            job_postings_v2 (LookalikesTriggerBodyFiltersType0JobPostingsV2Type0 | None | Unset):
            job_posting_stats (LookalikesTriggerBodyFiltersType0JobPostingStatsType0 | None | Unset):
            office_locations_v2 (LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0 | None | Unset):
            tlds (LookalikesTriggerBodyFiltersType0TldsType0 | None | Unset):
            num_words_in_name (LookalikesTriggerBodyFiltersType0NumWordsInNameType0 | None | Unset):
            status (LookalikesTriggerBodyFiltersType0StatusType0 | None | Unset):
            technologies (LookalikesTriggerBodyFiltersType0TechnologiesType0 | None | Unset):
            crunchbase_categories (LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0 | None | Unset):
            crunchbase_category_groups (LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0 | None | Unset):
            investors_v2 (LookalikesTriggerBodyFiltersType0InvestorsV2Type0 | None | Unset):
            technologies_v2 (LookalikesTriggerBodyFiltersType0TechnologiesV2Type0 | None | Unset):
            revenue_range_usd (LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0 | None | Unset):
            revenue_ranges_usd (LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0 | None | Unset):
            employee_trends_v2 (LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0 | None | Unset):
            tags (LookalikesTriggerBodyFiltersType0TagsType0 | None | Unset):
            linkedin_industries (LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0 | None | Unset): Filter companies
                by the industries they are tagged with on LinkedIn. To get the list of valid values, each with its company
                count, use the `getIndustries` endpoint (`GET /v1/enums/industries`), and hide values with very small counts
                from your filter UI, since a value with only a handful of companies behind it is a no-op filter. Values must
                match the enum exactly — a misspelled or retired value returns zero results with no error or warning. This
                filter matches LinkedIn's own industry tags, which are narrow and granular. For broader matching use
                `industriesV2` (Fiber's standardized categories, listed as `fiberIndustries` in the same response) or
                `crunchbaseCategories` / `crunchbaseCategoryGroups` for Crunchbase's taxonomy — the three are separate
                classifications and are not interchangeable.
    """

    headquarters_country_code: LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0 | None | Unset = UNSET
    headquarters_state_name: LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0 | None | Unset = UNSET
    employee_count_v2: LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0 | None | Unset = UNSET
    employee_count_ranges: LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0 | None | Unset = UNSET
    keywords: LookalikesTriggerBodyFiltersType0KeywordsType0 | None | Unset = UNSET
    industries_v2: LookalikesTriggerBodyFiltersType0IndustriesV2Type0 | None | Unset = UNSET
    stage: LookalikesTriggerBodyFiltersType0StageType0 | None | Unset = UNSET
    total_funding_usd: LookalikesTriggerBodyFiltersType0TotalFundingUSDType0 | None | Unset = UNSET
    last_funding_usd: LookalikesTriggerBodyFiltersType0LastFundingUSDType0 | None | Unset = UNSET
    last_funded_on: (
        LookalikesTriggerBodyFiltersType0LastFundedOnType0
        | LookalikesTriggerBodyFiltersType0LastFundedOnType1
        | None
        | Unset
    ) = UNSET
    founded_on: (
        LookalikesTriggerBodyFiltersType0FoundedOnType0 | LookalikesTriggerBodyFiltersType0FoundedOnType1 | None | Unset
    ) = UNSET
    name_like: LookalikesTriggerBodyFiltersType0NameLikeType0 | None | Unset = UNSET
    accelerators_v2: LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0 | None | Unset = UNSET
    headquarters_location: LookalikesTriggerBodyFiltersType0HeadquartersLocationType0 | None | Unset = UNSET
    special_flags: LookalikesTriggerBodyFiltersType0SpecialFlagsType0 | None | Unset = UNSET
    naics_codes: LookalikesTriggerBodyFiltersType0NaicsCodesType0 | None | Unset = UNSET
    fortune_rankings: LookalikesTriggerBodyFiltersType0FortuneRankingsType0 | None | Unset = UNSET
    job_postings_v2: LookalikesTriggerBodyFiltersType0JobPostingsV2Type0 | None | Unset = UNSET
    job_posting_stats: LookalikesTriggerBodyFiltersType0JobPostingStatsType0 | None | Unset = UNSET
    office_locations_v2: LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0 | None | Unset = UNSET
    tlds: LookalikesTriggerBodyFiltersType0TldsType0 | None | Unset = UNSET
    num_words_in_name: LookalikesTriggerBodyFiltersType0NumWordsInNameType0 | None | Unset = UNSET
    status: LookalikesTriggerBodyFiltersType0StatusType0 | None | Unset = UNSET
    technologies: LookalikesTriggerBodyFiltersType0TechnologiesType0 | None | Unset = UNSET
    crunchbase_categories: LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0 | None | Unset = UNSET
    crunchbase_category_groups: LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0 | None | Unset = UNSET
    investors_v2: LookalikesTriggerBodyFiltersType0InvestorsV2Type0 | None | Unset = UNSET
    technologies_v2: LookalikesTriggerBodyFiltersType0TechnologiesV2Type0 | None | Unset = UNSET
    revenue_range_usd: LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0 | None | Unset = UNSET
    revenue_ranges_usd: LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0 | None | Unset = UNSET
    employee_trends_v2: LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0 | None | Unset = UNSET
    tags: LookalikesTriggerBodyFiltersType0TagsType0 | None | Unset = UNSET
    linkedin_industries: LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookalikes_trigger_body_filters_type_0_accelerators_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_categories_type_0 import (
            LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_category_groups_type_0 import (
            LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_count_ranges_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_count_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_trends_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_fortune_rankings_type_0 import (
            LookalikesTriggerBodyFiltersType0FortuneRankingsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_0 import (
            LookalikesTriggerBodyFiltersType0FoundedOnType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_1 import (
            LookalikesTriggerBodyFiltersType0FoundedOnType1,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_country_code_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_location_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersLocationType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_state_name_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_industries_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0IndustriesV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0InvestorsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_job_posting_stats_type_0 import (
            LookalikesTriggerBodyFiltersType0JobPostingStatsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_job_postings_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0JobPostingsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_keywords_type_0 import (
            LookalikesTriggerBodyFiltersType0KeywordsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_0 import (
            LookalikesTriggerBodyFiltersType0LastFundedOnType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_1 import (
            LookalikesTriggerBodyFiltersType0LastFundedOnType1,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funding_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0LastFundingUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_linkedin_industries_type_0 import (
            LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_naics_codes_type_0 import (
            LookalikesTriggerBodyFiltersType0NaicsCodesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_name_like_type_0 import (
            LookalikesTriggerBodyFiltersType0NameLikeType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_num_words_in_name_type_0 import (
            LookalikesTriggerBodyFiltersType0NumWordsInNameType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_office_locations_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_revenue_range_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_revenue_ranges_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_special_flags_type_0 import (
            LookalikesTriggerBodyFiltersType0SpecialFlagsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_stage_type_0 import (
            LookalikesTriggerBodyFiltersType0StageType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_status_type_0 import (
            LookalikesTriggerBodyFiltersType0StatusType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_tags_type_0 import (
            LookalikesTriggerBodyFiltersType0TagsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_technologies_type_0 import (
            LookalikesTriggerBodyFiltersType0TechnologiesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_technologies_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0TechnologiesV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_tlds_type_0 import (
            LookalikesTriggerBodyFiltersType0TldsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_total_funding_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0TotalFundingUSDType0,  # noqa: PLC0415
        )

        headquarters_country_code: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_country_code, Unset):
            headquarters_country_code = UNSET
        elif isinstance(self.headquarters_country_code, LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0):
            headquarters_country_code = self.headquarters_country_code.to_dict()
        else:
            headquarters_country_code = self.headquarters_country_code

        headquarters_state_name: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_state_name, Unset):
            headquarters_state_name = UNSET
        elif isinstance(self.headquarters_state_name, LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0):
            headquarters_state_name = self.headquarters_state_name.to_dict()
        else:
            headquarters_state_name = self.headquarters_state_name

        employee_count_v2: dict[str, Any] | None | Unset
        if isinstance(self.employee_count_v2, Unset):
            employee_count_v2 = UNSET
        elif isinstance(self.employee_count_v2, LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0):
            employee_count_v2 = self.employee_count_v2.to_dict()
        else:
            employee_count_v2 = self.employee_count_v2

        employee_count_ranges: dict[str, Any] | None | Unset
        if isinstance(self.employee_count_ranges, Unset):
            employee_count_ranges = UNSET
        elif isinstance(self.employee_count_ranges, LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0):
            employee_count_ranges = self.employee_count_ranges.to_dict()
        else:
            employee_count_ranges = self.employee_count_ranges

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, LookalikesTriggerBodyFiltersType0KeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        industries_v2: dict[str, Any] | None | Unset
        if isinstance(self.industries_v2, Unset):
            industries_v2 = UNSET
        elif isinstance(self.industries_v2, LookalikesTriggerBodyFiltersType0IndustriesV2Type0):
            industries_v2 = self.industries_v2.to_dict()
        else:
            industries_v2 = self.industries_v2

        stage: dict[str, Any] | None | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, LookalikesTriggerBodyFiltersType0StageType0):
            stage = self.stage.to_dict()
        else:
            stage = self.stage

        total_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        elif isinstance(self.total_funding_usd, LookalikesTriggerBodyFiltersType0TotalFundingUSDType0):
            total_funding_usd = self.total_funding_usd.to_dict()
        else:
            total_funding_usd = self.total_funding_usd

        last_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.last_funding_usd, Unset):
            last_funding_usd = UNSET
        elif isinstance(self.last_funding_usd, LookalikesTriggerBodyFiltersType0LastFundingUSDType0):
            last_funding_usd = self.last_funding_usd.to_dict()
        else:
            last_funding_usd = self.last_funding_usd

        last_funded_on: dict[str, Any] | None | Unset
        if isinstance(self.last_funded_on, Unset):
            last_funded_on = UNSET
        elif isinstance(self.last_funded_on, LookalikesTriggerBodyFiltersType0LastFundedOnType0):
            last_funded_on = self.last_funded_on.to_dict()
        elif isinstance(self.last_funded_on, LookalikesTriggerBodyFiltersType0LastFundedOnType1):
            last_funded_on = self.last_funded_on.to_dict()
        else:
            last_funded_on = self.last_funded_on

        founded_on: dict[str, Any] | None | Unset
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, LookalikesTriggerBodyFiltersType0FoundedOnType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, LookalikesTriggerBodyFiltersType0FoundedOnType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        name_like: dict[str, Any] | None | Unset
        if isinstance(self.name_like, Unset):
            name_like = UNSET
        elif isinstance(self.name_like, LookalikesTriggerBodyFiltersType0NameLikeType0):
            name_like = self.name_like.to_dict()
        else:
            name_like = self.name_like

        accelerators_v2: dict[str, Any] | None | Unset
        if isinstance(self.accelerators_v2, Unset):
            accelerators_v2 = UNSET
        elif isinstance(self.accelerators_v2, LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0):
            accelerators_v2 = self.accelerators_v2.to_dict()
        else:
            accelerators_v2 = self.accelerators_v2

        headquarters_location: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_location, Unset):
            headquarters_location = UNSET
        elif isinstance(self.headquarters_location, LookalikesTriggerBodyFiltersType0HeadquartersLocationType0):
            headquarters_location = self.headquarters_location.to_dict()
        else:
            headquarters_location = self.headquarters_location

        special_flags: dict[str, Any] | None | Unset
        if isinstance(self.special_flags, Unset):
            special_flags = UNSET
        elif isinstance(self.special_flags, LookalikesTriggerBodyFiltersType0SpecialFlagsType0):
            special_flags = self.special_flags.to_dict()
        else:
            special_flags = self.special_flags

        naics_codes: dict[str, Any] | None | Unset
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, LookalikesTriggerBodyFiltersType0NaicsCodesType0):
            naics_codes = self.naics_codes.to_dict()
        else:
            naics_codes = self.naics_codes

        fortune_rankings: dict[str, Any] | None | Unset
        if isinstance(self.fortune_rankings, Unset):
            fortune_rankings = UNSET
        elif isinstance(self.fortune_rankings, LookalikesTriggerBodyFiltersType0FortuneRankingsType0):
            fortune_rankings = self.fortune_rankings.to_dict()
        else:
            fortune_rankings = self.fortune_rankings

        job_postings_v2: dict[str, Any] | None | Unset
        if isinstance(self.job_postings_v2, Unset):
            job_postings_v2 = UNSET
        elif isinstance(self.job_postings_v2, LookalikesTriggerBodyFiltersType0JobPostingsV2Type0):
            job_postings_v2 = self.job_postings_v2.to_dict()
        else:
            job_postings_v2 = self.job_postings_v2

        job_posting_stats: dict[str, Any] | None | Unset
        if isinstance(self.job_posting_stats, Unset):
            job_posting_stats = UNSET
        elif isinstance(self.job_posting_stats, LookalikesTriggerBodyFiltersType0JobPostingStatsType0):
            job_posting_stats = self.job_posting_stats.to_dict()
        else:
            job_posting_stats = self.job_posting_stats

        office_locations_v2: dict[str, Any] | None | Unset
        if isinstance(self.office_locations_v2, Unset):
            office_locations_v2 = UNSET
        elif isinstance(self.office_locations_v2, LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0):
            office_locations_v2 = self.office_locations_v2.to_dict()
        else:
            office_locations_v2 = self.office_locations_v2

        tlds: dict[str, Any] | None | Unset
        if isinstance(self.tlds, Unset):
            tlds = UNSET
        elif isinstance(self.tlds, LookalikesTriggerBodyFiltersType0TldsType0):
            tlds = self.tlds.to_dict()
        else:
            tlds = self.tlds

        num_words_in_name: dict[str, Any] | None | Unset
        if isinstance(self.num_words_in_name, Unset):
            num_words_in_name = UNSET
        elif isinstance(self.num_words_in_name, LookalikesTriggerBodyFiltersType0NumWordsInNameType0):
            num_words_in_name = self.num_words_in_name.to_dict()
        else:
            num_words_in_name = self.num_words_in_name

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, LookalikesTriggerBodyFiltersType0StatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        technologies: dict[str, Any] | None | Unset
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, LookalikesTriggerBodyFiltersType0TechnologiesType0):
            technologies = self.technologies.to_dict()
        else:
            technologies = self.technologies

        crunchbase_categories: dict[str, Any] | None | Unset
        if isinstance(self.crunchbase_categories, Unset):
            crunchbase_categories = UNSET
        elif isinstance(self.crunchbase_categories, LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0):
            crunchbase_categories = self.crunchbase_categories.to_dict()
        else:
            crunchbase_categories = self.crunchbase_categories

        crunchbase_category_groups: dict[str, Any] | None | Unset
        if isinstance(self.crunchbase_category_groups, Unset):
            crunchbase_category_groups = UNSET
        elif isinstance(
            self.crunchbase_category_groups, LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0
        ):
            crunchbase_category_groups = self.crunchbase_category_groups.to_dict()
        else:
            crunchbase_category_groups = self.crunchbase_category_groups

        investors_v2: dict[str, Any] | None | Unset
        if isinstance(self.investors_v2, Unset):
            investors_v2 = UNSET
        elif isinstance(self.investors_v2, LookalikesTriggerBodyFiltersType0InvestorsV2Type0):
            investors_v2 = self.investors_v2.to_dict()
        else:
            investors_v2 = self.investors_v2

        technologies_v2: dict[str, Any] | None | Unset
        if isinstance(self.technologies_v2, Unset):
            technologies_v2 = UNSET
        elif isinstance(self.technologies_v2, LookalikesTriggerBodyFiltersType0TechnologiesV2Type0):
            technologies_v2 = self.technologies_v2.to_dict()
        else:
            technologies_v2 = self.technologies_v2

        revenue_range_usd: dict[str, Any] | None | Unset
        if isinstance(self.revenue_range_usd, Unset):
            revenue_range_usd = UNSET
        elif isinstance(self.revenue_range_usd, LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0):
            revenue_range_usd = self.revenue_range_usd.to_dict()
        else:
            revenue_range_usd = self.revenue_range_usd

        revenue_ranges_usd: dict[str, Any] | None | Unset
        if isinstance(self.revenue_ranges_usd, Unset):
            revenue_ranges_usd = UNSET
        elif isinstance(self.revenue_ranges_usd, LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0):
            revenue_ranges_usd = self.revenue_ranges_usd.to_dict()
        else:
            revenue_ranges_usd = self.revenue_ranges_usd

        employee_trends_v2: dict[str, Any] | None | Unset
        if isinstance(self.employee_trends_v2, Unset):
            employee_trends_v2 = UNSET
        elif isinstance(self.employee_trends_v2, LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0):
            employee_trends_v2 = self.employee_trends_v2.to_dict()
        else:
            employee_trends_v2 = self.employee_trends_v2

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, LookalikesTriggerBodyFiltersType0TagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        linkedin_industries: dict[str, Any] | None | Unset
        if isinstance(self.linkedin_industries, Unset):
            linkedin_industries = UNSET
        elif isinstance(self.linkedin_industries, LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0):
            linkedin_industries = self.linkedin_industries.to_dict()
        else:
            linkedin_industries = self.linkedin_industries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headquarters_country_code is not UNSET:
            field_dict["headquartersCountryCode"] = headquarters_country_code
        if headquarters_state_name is not UNSET:
            field_dict["headquartersStateName"] = headquarters_state_name
        if employee_count_v2 is not UNSET:
            field_dict["employeeCountV2"] = employee_count_v2
        if employee_count_ranges is not UNSET:
            field_dict["employeeCountRanges"] = employee_count_ranges
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
        if accelerators_v2 is not UNSET:
            field_dict["acceleratorsV2"] = accelerators_v2
        if headquarters_location is not UNSET:
            field_dict["headquartersLocation"] = headquarters_location
        if special_flags is not UNSET:
            field_dict["specialFlags"] = special_flags
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
        if investors_v2 is not UNSET:
            field_dict["investorsV2"] = investors_v2
        if technologies_v2 is not UNSET:
            field_dict["technologiesV2"] = technologies_v2
        if revenue_range_usd is not UNSET:
            field_dict["revenueRangeUSD"] = revenue_range_usd
        if revenue_ranges_usd is not UNSET:
            field_dict["revenueRangesUSD"] = revenue_ranges_usd
        if employee_trends_v2 is not UNSET:
            field_dict["employeeTrendsV2"] = employee_trends_v2
        if tags is not UNSET:
            field_dict["tags"] = tags
        if linkedin_industries is not UNSET:
            field_dict["linkedinIndustries"] = linkedin_industries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_trigger_body_filters_type_0_accelerators_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_categories_type_0 import (
            LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_crunchbase_category_groups_type_0 import (
            LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_count_ranges_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_count_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_employee_trends_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_fortune_rankings_type_0 import (
            LookalikesTriggerBodyFiltersType0FortuneRankingsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_0 import (
            LookalikesTriggerBodyFiltersType0FoundedOnType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_founded_on_type_1 import (
            LookalikesTriggerBodyFiltersType0FoundedOnType1,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_country_code_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_location_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersLocationType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_headquarters_state_name_type_0 import (
            LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_industries_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0IndustriesV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_investors_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0InvestorsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_job_posting_stats_type_0 import (
            LookalikesTriggerBodyFiltersType0JobPostingStatsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_job_postings_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0JobPostingsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_keywords_type_0 import (
            LookalikesTriggerBodyFiltersType0KeywordsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_0 import (
            LookalikesTriggerBodyFiltersType0LastFundedOnType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funded_on_type_1 import (
            LookalikesTriggerBodyFiltersType0LastFundedOnType1,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_last_funding_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0LastFundingUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_linkedin_industries_type_0 import (
            LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_naics_codes_type_0 import (
            LookalikesTriggerBodyFiltersType0NaicsCodesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_name_like_type_0 import (
            LookalikesTriggerBodyFiltersType0NameLikeType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_num_words_in_name_type_0 import (
            LookalikesTriggerBodyFiltersType0NumWordsInNameType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_office_locations_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_revenue_range_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_revenue_ranges_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_special_flags_type_0 import (
            LookalikesTriggerBodyFiltersType0SpecialFlagsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_stage_type_0 import (
            LookalikesTriggerBodyFiltersType0StageType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_status_type_0 import (
            LookalikesTriggerBodyFiltersType0StatusType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_tags_type_0 import (
            LookalikesTriggerBodyFiltersType0TagsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_technologies_type_0 import (
            LookalikesTriggerBodyFiltersType0TechnologiesType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_technologies_v2_type_0 import (
            LookalikesTriggerBodyFiltersType0TechnologiesV2Type0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_tlds_type_0 import (
            LookalikesTriggerBodyFiltersType0TldsType0,  # noqa: PLC0415
        )
        from ..models.lookalikes_trigger_body_filters_type_0_total_funding_usd_type_0 import (
            LookalikesTriggerBodyFiltersType0TotalFundingUSDType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_headquarters_country_code(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_country_code_type_0 = (
                    LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0.from_dict(data)
                )

                return headquarters_country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0HeadquartersCountryCodeType0 | None | Unset, data)

        headquarters_country_code = _parse_headquarters_country_code(d.pop("headquartersCountryCode", UNSET))

        def _parse_headquarters_state_name(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_state_name_type_0 = LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0.from_dict(
                    data
                )

                return headquarters_state_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0HeadquartersStateNameType0 | None | Unset, data)

        headquarters_state_name = _parse_headquarters_state_name(d.pop("headquartersStateName", UNSET))

        def _parse_employee_count_v2(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_v2_type_0 = LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0.from_dict(data)

                return employee_count_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0EmployeeCountV2Type0 | None | Unset, data)

        employee_count_v2 = _parse_employee_count_v2(d.pop("employeeCountV2", UNSET))

        def _parse_employee_count_ranges(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_ranges_type_0 = LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0.from_dict(data)

                return employee_count_ranges_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0EmployeeCountRangesType0 | None | Unset, data)

        employee_count_ranges = _parse_employee_count_ranges(d.pop("employeeCountRanges", UNSET))

        def _parse_keywords(data: object) -> LookalikesTriggerBodyFiltersType0KeywordsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = LookalikesTriggerBodyFiltersType0KeywordsType0.from_dict(data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0KeywordsType0 | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_industries_v2(data: object) -> LookalikesTriggerBodyFiltersType0IndustriesV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industries_v2_type_0 = LookalikesTriggerBodyFiltersType0IndustriesV2Type0.from_dict(data)

                return industries_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0IndustriesV2Type0 | None | Unset, data)

        industries_v2 = _parse_industries_v2(d.pop("industriesV2", UNSET))

        def _parse_stage(data: object) -> LookalikesTriggerBodyFiltersType0StageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stage_type_0 = LookalikesTriggerBodyFiltersType0StageType0.from_dict(data)

                return stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0StageType0 | None | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_total_funding_usd(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0TotalFundingUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_funding_usd_type_0 = LookalikesTriggerBodyFiltersType0TotalFundingUSDType0.from_dict(data)

                return total_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0TotalFundingUSDType0 | None | Unset, data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUSD", UNSET))

        def _parse_last_funding_usd(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0LastFundingUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funding_usd_type_0 = LookalikesTriggerBodyFiltersType0LastFundingUSDType0.from_dict(data)

                return last_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0LastFundingUSDType0 | None | Unset, data)

        last_funding_usd = _parse_last_funding_usd(d.pop("lastFundingUSD", UNSET))

        def _parse_last_funded_on(
            data: object,
        ) -> (
            LookalikesTriggerBodyFiltersType0LastFundedOnType0
            | LookalikesTriggerBodyFiltersType0LastFundedOnType1
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
                last_funded_on_type_0 = LookalikesTriggerBodyFiltersType0LastFundedOnType0.from_dict(data)

                return last_funded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_1 = LookalikesTriggerBodyFiltersType0LastFundedOnType1.from_dict(data)

                return last_funded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LookalikesTriggerBodyFiltersType0LastFundedOnType0
                | LookalikesTriggerBodyFiltersType0LastFundedOnType1
                | None
                | Unset,
                data,
            )

        last_funded_on = _parse_last_funded_on(d.pop("lastFundedOn", UNSET))

        def _parse_founded_on(
            data: object,
        ) -> (
            LookalikesTriggerBodyFiltersType0FoundedOnType0
            | LookalikesTriggerBodyFiltersType0FoundedOnType1
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
                founded_on_type_0 = LookalikesTriggerBodyFiltersType0FoundedOnType0.from_dict(data)

                return founded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_1 = LookalikesTriggerBodyFiltersType0FoundedOnType1.from_dict(data)

                return founded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LookalikesTriggerBodyFiltersType0FoundedOnType0
                | LookalikesTriggerBodyFiltersType0FoundedOnType1
                | None
                | Unset,
                data,
            )

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))

        def _parse_name_like(data: object) -> LookalikesTriggerBodyFiltersType0NameLikeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_like_type_0 = LookalikesTriggerBodyFiltersType0NameLikeType0.from_dict(data)

                return name_like_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0NameLikeType0 | None | Unset, data)

        name_like = _parse_name_like(d.pop("nameLike", UNSET))

        def _parse_accelerators_v2(data: object) -> LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accelerators_v2_type_0 = LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0.from_dict(data)

                return accelerators_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0AcceleratorsV2Type0 | None | Unset, data)

        accelerators_v2 = _parse_accelerators_v2(d.pop("acceleratorsV2", UNSET))

        def _parse_headquarters_location(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0HeadquartersLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_location_type_0 = LookalikesTriggerBodyFiltersType0HeadquartersLocationType0.from_dict(
                    data
                )

                return headquarters_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0HeadquartersLocationType0 | None | Unset, data)

        headquarters_location = _parse_headquarters_location(d.pop("headquartersLocation", UNSET))

        def _parse_special_flags(data: object) -> LookalikesTriggerBodyFiltersType0SpecialFlagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                special_flags_type_0 = LookalikesTriggerBodyFiltersType0SpecialFlagsType0.from_dict(data)

                return special_flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0SpecialFlagsType0 | None | Unset, data)

        special_flags = _parse_special_flags(d.pop("specialFlags", UNSET))

        def _parse_naics_codes(data: object) -> LookalikesTriggerBodyFiltersType0NaicsCodesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                naics_codes_type_0 = LookalikesTriggerBodyFiltersType0NaicsCodesType0.from_dict(data)

                return naics_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0NaicsCodesType0 | None | Unset, data)

        naics_codes = _parse_naics_codes(d.pop("naicsCodes", UNSET))

        def _parse_fortune_rankings(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0FortuneRankingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fortune_rankings_type_0 = LookalikesTriggerBodyFiltersType0FortuneRankingsType0.from_dict(data)

                return fortune_rankings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0FortuneRankingsType0 | None | Unset, data)

        fortune_rankings = _parse_fortune_rankings(d.pop("fortuneRankings", UNSET))

        def _parse_job_postings_v2(data: object) -> LookalikesTriggerBodyFiltersType0JobPostingsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_v2_type_0 = LookalikesTriggerBodyFiltersType0JobPostingsV2Type0.from_dict(data)

                return job_postings_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0JobPostingsV2Type0 | None | Unset, data)

        job_postings_v2 = _parse_job_postings_v2(d.pop("jobPostingsV2", UNSET))

        def _parse_job_posting_stats(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0JobPostingStatsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_posting_stats_type_0 = LookalikesTriggerBodyFiltersType0JobPostingStatsType0.from_dict(data)

                return job_posting_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0JobPostingStatsType0 | None | Unset, data)

        job_posting_stats = _parse_job_posting_stats(d.pop("jobPostingStats", UNSET))

        def _parse_office_locations_v2(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                office_locations_v2_type_0 = LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0.from_dict(data)

                return office_locations_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0OfficeLocationsV2Type0 | None | Unset, data)

        office_locations_v2 = _parse_office_locations_v2(d.pop("officeLocationsV2", UNSET))

        def _parse_tlds(data: object) -> LookalikesTriggerBodyFiltersType0TldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tlds_type_0 = LookalikesTriggerBodyFiltersType0TldsType0.from_dict(data)

                return tlds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0TldsType0 | None | Unset, data)

        tlds = _parse_tlds(d.pop("tlds", UNSET))

        def _parse_num_words_in_name(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0NumWordsInNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_words_in_name_type_0 = LookalikesTriggerBodyFiltersType0NumWordsInNameType0.from_dict(data)

                return num_words_in_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0NumWordsInNameType0 | None | Unset, data)

        num_words_in_name = _parse_num_words_in_name(d.pop("numWordsInName", UNSET))

        def _parse_status(data: object) -> LookalikesTriggerBodyFiltersType0StatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = LookalikesTriggerBodyFiltersType0StatusType0.from_dict(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0StatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_technologies(data: object) -> LookalikesTriggerBodyFiltersType0TechnologiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_type_0 = LookalikesTriggerBodyFiltersType0TechnologiesType0.from_dict(data)

                return technologies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0TechnologiesType0 | None | Unset, data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))

        def _parse_crunchbase_categories(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_categories_type_0 = LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0.from_dict(
                    data
                )

                return crunchbase_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0CrunchbaseCategoriesType0 | None | Unset, data)

        crunchbase_categories = _parse_crunchbase_categories(d.pop("crunchbaseCategories", UNSET))

        def _parse_crunchbase_category_groups(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_category_groups_type_0 = (
                    LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0.from_dict(data)
                )

                return crunchbase_category_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0CrunchbaseCategoryGroupsType0 | None | Unset, data)

        crunchbase_category_groups = _parse_crunchbase_category_groups(d.pop("crunchbaseCategoryGroups", UNSET))

        def _parse_investors_v2(data: object) -> LookalikesTriggerBodyFiltersType0InvestorsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_v2_type_0 = LookalikesTriggerBodyFiltersType0InvestorsV2Type0.from_dict(data)

                return investors_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0InvestorsV2Type0 | None | Unset, data)

        investors_v2 = _parse_investors_v2(d.pop("investorsV2", UNSET))

        def _parse_technologies_v2(data: object) -> LookalikesTriggerBodyFiltersType0TechnologiesV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_v2_type_0 = LookalikesTriggerBodyFiltersType0TechnologiesV2Type0.from_dict(data)

                return technologies_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0TechnologiesV2Type0 | None | Unset, data)

        technologies_v2 = _parse_technologies_v2(d.pop("technologiesV2", UNSET))

        def _parse_revenue_range_usd(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_range_usd_type_0 = LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0.from_dict(data)

                return revenue_range_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0RevenueRangeUSDType0 | None | Unset, data)

        revenue_range_usd = _parse_revenue_range_usd(d.pop("revenueRangeUSD", UNSET))

        def _parse_revenue_ranges_usd(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_ranges_usd_type_0 = LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0.from_dict(data)

                return revenue_ranges_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0RevenueRangesUSDType0 | None | Unset, data)

        revenue_ranges_usd = _parse_revenue_ranges_usd(d.pop("revenueRangesUSD", UNSET))

        def _parse_employee_trends_v2(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_trends_v2_type_0 = LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0.from_dict(data)

                return employee_trends_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0EmployeeTrendsV2Type0 | None | Unset, data)

        employee_trends_v2 = _parse_employee_trends_v2(d.pop("employeeTrendsV2", UNSET))

        def _parse_tags(data: object) -> LookalikesTriggerBodyFiltersType0TagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = LookalikesTriggerBodyFiltersType0TagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0TagsType0 | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_linkedin_industries(
            data: object,
        ) -> LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linkedin_industries_type_0 = LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0.from_dict(data)

                return linkedin_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0LinkedinIndustriesType0 | None | Unset, data)

        linkedin_industries = _parse_linkedin_industries(d.pop("linkedinIndustries", UNSET))

        lookalikes_trigger_body_filters_type_0 = cls(
            headquarters_country_code=headquarters_country_code,
            headquarters_state_name=headquarters_state_name,
            employee_count_v2=employee_count_v2,
            employee_count_ranges=employee_count_ranges,
            keywords=keywords,
            industries_v2=industries_v2,
            stage=stage,
            total_funding_usd=total_funding_usd,
            last_funding_usd=last_funding_usd,
            last_funded_on=last_funded_on,
            founded_on=founded_on,
            name_like=name_like,
            accelerators_v2=accelerators_v2,
            headquarters_location=headquarters_location,
            special_flags=special_flags,
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
            investors_v2=investors_v2,
            technologies_v2=technologies_v2,
            revenue_range_usd=revenue_range_usd,
            revenue_ranges_usd=revenue_ranges_usd,
            employee_trends_v2=employee_trends_v2,
            tags=tags,
            linkedin_industries=linkedin_industries,
        )

        lookalikes_trigger_body_filters_type_0.additional_properties = d
        return lookalikes_trigger_body_filters_type_0

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
