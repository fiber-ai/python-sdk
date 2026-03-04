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
  from ..models.sync_combined_search_body_company_params_last_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0
  from ..models.sync_combined_search_body_company_params_headquarters_country_code_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0
  from ..models.sync_combined_search_body_company_params_num_words_in_name_type_0 import SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0
  from ..models.sync_combined_search_body_company_params_naics_codes_type_0 import SyncCombinedSearchBodyCompanyParamsNaicsCodesType0
  from ..models.sync_combined_search_body_company_params_tlds_type_0 import SyncCombinedSearchBodyCompanyParamsTldsType0
  from ..models.sync_combined_search_body_company_params_founded_on_type_1 import SyncCombinedSearchBodyCompanyParamsFoundedOnType1
  from ..models.sync_combined_search_body_company_params_name_like_type_0 import SyncCombinedSearchBodyCompanyParamsNameLikeType0
  from ..models.sync_combined_search_body_company_params_revenue_usd_type_0 import SyncCombinedSearchBodyCompanyParamsRevenueUSDType0
  from ..models.sync_combined_search_body_company_params_status_type_0 import SyncCombinedSearchBodyCompanyParamsStatusType0
  from ..models.sync_combined_search_body_company_params_fortune_rankings_type_0 import SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0
  from ..models.sync_combined_search_body_company_params_exact_company_v2_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0
  from ..models.sync_combined_search_body_company_params_industries_v2_type_0 import SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0
  from ..models.sync_combined_search_body_company_params_keywords_type_0 import SyncCombinedSearchBodyCompanyParamsKeywordsType0
  from ..models.sync_combined_search_body_company_params_exact_company_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyType0
  from ..models.sync_combined_search_body_company_params_special_flags_type_0 import SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0
  from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0 import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0
  from ..models.sync_combined_search_body_company_params_tags_type_0 import SyncCombinedSearchBodyCompanyParamsTagsType0
  from ..models.sync_combined_search_body_company_params_investors_type_0 import SyncCombinedSearchBodyCompanyParamsInvestorsType0
  from ..models.sync_combined_search_body_company_params_founded_on_type_0 import SyncCombinedSearchBodyCompanyParamsFoundedOnType0
  from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0
  from ..models.sync_combined_search_body_company_params_total_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0
  from ..models.sync_combined_search_body_company_params_headquarters_state_name_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0
  from ..models.sync_combined_search_body_company_params_crunchbase_categories_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0
  from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0
  from ..models.sync_combined_search_body_company_params_employees_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeesType0
  from ..models.sync_combined_search_body_company_params_crunchbase_category_groups_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0
  from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0
  from ..models.sync_combined_search_body_company_params_last_funded_on_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType0
  from ..models.sync_combined_search_body_company_params_technologies_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0
  from ..models.sync_combined_search_body_company_params_stage_type_0 import SyncCombinedSearchBodyCompanyParamsStageType0
  from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0 import SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0
  from ..models.sync_combined_search_body_company_params_headquarters_location_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0
  from ..models.sync_combined_search_body_company_params_linkedin_industries_type_0 import SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0
  from ..models.sync_combined_search_body_company_params_last_funded_on_type_1 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType1





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParams")



@_attrs_define
class SyncCombinedSearchBodyCompanyParams:
    """ Company search params. We would find prospects who are currently working in the companies that satisfy these search
    params. Make sure that the search scope of companies is small, else we truncate it to the top 1000 companies.

        Attributes:
            exact_company_v2 (Union['SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0', None, Unset]):
            domains (Union[None, Unset, list[str]]):
            headquarters_country_code (Union['SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0', None,
                Unset]):
            headquarters_state_name (Union['SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0', None, Unset]):
            employee_count_v2 (Union['SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0', None, Unset]):
            keywords (Union['SyncCombinedSearchBodyCompanyParamsKeywordsType0', None, Unset]):
            industries_v2 (Union['SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0', None, Unset]):
            stage (Union['SyncCombinedSearchBodyCompanyParamsStageType0', None, Unset]):
            total_funding_usd (Union['SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0', None, Unset]):
            last_funding_usd (Union['SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0', None, Unset]):
            last_funded_on (Union['SyncCombinedSearchBodyCompanyParamsLastFundedOnType0',
                'SyncCombinedSearchBodyCompanyParamsLastFundedOnType1', None, Unset]):
            founded_on (Union['SyncCombinedSearchBodyCompanyParamsFoundedOnType0',
                'SyncCombinedSearchBodyCompanyParamsFoundedOnType1', None, Unset]):
            name_like (Union['SyncCombinedSearchBodyCompanyParamsNameLikeType0', None, Unset]):
            exact_company (Union['SyncCombinedSearchBodyCompanyParamsExactCompanyType0', None, Unset]):
            accelerators_v2 (Union['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0', None, Unset]):
            employee_trends (Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0', None, Unset]):
            headquarters_location (Union['SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0', None, Unset]):
            linkedin_slugs (Union[None, Unset, list[str]]):
            special_flags (Union['SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0', None, Unset]):
            employees (Union['SyncCombinedSearchBodyCompanyParamsEmployeesType0', None, Unset]):
            revenue_usd (Union['SyncCombinedSearchBodyCompanyParamsRevenueUSDType0', None, Unset]):
            naics_codes (Union['SyncCombinedSearchBodyCompanyParamsNaicsCodesType0', None, Unset]):
            fortune_rankings (Union['SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0', None, Unset]):
            job_postings_v2 (Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0', None, Unset]):
            job_posting_stats (Union['SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0', None, Unset]):
            office_locations_v2 (Union['SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0', None, Unset]):
            tlds (Union['SyncCombinedSearchBodyCompanyParamsTldsType0', None, Unset]):
            num_words_in_name (Union['SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0', None, Unset]):
            status (Union['SyncCombinedSearchBodyCompanyParamsStatusType0', None, Unset]):
            technologies (Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0', None, Unset]):
            investors (Union['SyncCombinedSearchBodyCompanyParamsInvestorsType0', None, Unset]):
            tags (Union['SyncCombinedSearchBodyCompanyParamsTagsType0', None, Unset]):
            crunchbase_categories (Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0', None, Unset]):
            crunchbase_category_groups (Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0', None,
                Unset]):
            linkedin_industries (Union['SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0', None, Unset]):
            crunchbase_slugs (Union[None, Unset, list[str]]):
     """

    exact_company_v2: Union['SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0', None, Unset] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    headquarters_country_code: Union['SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0', None, Unset] = UNSET
    headquarters_state_name: Union['SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0', None, Unset] = UNSET
    employee_count_v2: Union['SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0', None, Unset] = UNSET
    keywords: Union['SyncCombinedSearchBodyCompanyParamsKeywordsType0', None, Unset] = UNSET
    industries_v2: Union['SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0', None, Unset] = UNSET
    stage: Union['SyncCombinedSearchBodyCompanyParamsStageType0', None, Unset] = UNSET
    total_funding_usd: Union['SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0', None, Unset] = UNSET
    last_funding_usd: Union['SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0', None, Unset] = UNSET
    last_funded_on: Union['SyncCombinedSearchBodyCompanyParamsLastFundedOnType0', 'SyncCombinedSearchBodyCompanyParamsLastFundedOnType1', None, Unset] = UNSET
    founded_on: Union['SyncCombinedSearchBodyCompanyParamsFoundedOnType0', 'SyncCombinedSearchBodyCompanyParamsFoundedOnType1', None, Unset] = UNSET
    name_like: Union['SyncCombinedSearchBodyCompanyParamsNameLikeType0', None, Unset] = UNSET
    exact_company: Union['SyncCombinedSearchBodyCompanyParamsExactCompanyType0', None, Unset] = UNSET
    accelerators_v2: Union['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0', None, Unset] = UNSET
    employee_trends: Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0', None, Unset] = UNSET
    headquarters_location: Union['SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0', None, Unset] = UNSET
    linkedin_slugs: Union[None, Unset, list[str]] = UNSET
    special_flags: Union['SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0', None, Unset] = UNSET
    employees: Union['SyncCombinedSearchBodyCompanyParamsEmployeesType0', None, Unset] = UNSET
    revenue_usd: Union['SyncCombinedSearchBodyCompanyParamsRevenueUSDType0', None, Unset] = UNSET
    naics_codes: Union['SyncCombinedSearchBodyCompanyParamsNaicsCodesType0', None, Unset] = UNSET
    fortune_rankings: Union['SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0', None, Unset] = UNSET
    job_postings_v2: Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0', None, Unset] = UNSET
    job_posting_stats: Union['SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0', None, Unset] = UNSET
    office_locations_v2: Union['SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0', None, Unset] = UNSET
    tlds: Union['SyncCombinedSearchBodyCompanyParamsTldsType0', None, Unset] = UNSET
    num_words_in_name: Union['SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0', None, Unset] = UNSET
    status: Union['SyncCombinedSearchBodyCompanyParamsStatusType0', None, Unset] = UNSET
    technologies: Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0', None, Unset] = UNSET
    investors: Union['SyncCombinedSearchBodyCompanyParamsInvestorsType0', None, Unset] = UNSET
    tags: Union['SyncCombinedSearchBodyCompanyParamsTagsType0', None, Unset] = UNSET
    crunchbase_categories: Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0', None, Unset] = UNSET
    crunchbase_category_groups: Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0', None, Unset] = UNSET
    linkedin_industries: Union['SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0', None, Unset] = UNSET
    crunchbase_slugs: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_last_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0
        from ..models.sync_combined_search_body_company_params_headquarters_country_code_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0
        from ..models.sync_combined_search_body_company_params_num_words_in_name_type_0 import SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0
        from ..models.sync_combined_search_body_company_params_naics_codes_type_0 import SyncCombinedSearchBodyCompanyParamsNaicsCodesType0
        from ..models.sync_combined_search_body_company_params_tlds_type_0 import SyncCombinedSearchBodyCompanyParamsTldsType0
        from ..models.sync_combined_search_body_company_params_founded_on_type_1 import SyncCombinedSearchBodyCompanyParamsFoundedOnType1
        from ..models.sync_combined_search_body_company_params_name_like_type_0 import SyncCombinedSearchBodyCompanyParamsNameLikeType0
        from ..models.sync_combined_search_body_company_params_revenue_usd_type_0 import SyncCombinedSearchBodyCompanyParamsRevenueUSDType0
        from ..models.sync_combined_search_body_company_params_status_type_0 import SyncCombinedSearchBodyCompanyParamsStatusType0
        from ..models.sync_combined_search_body_company_params_fortune_rankings_type_0 import SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0
        from ..models.sync_combined_search_body_company_params_exact_company_v2_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0
        from ..models.sync_combined_search_body_company_params_industries_v2_type_0 import SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0
        from ..models.sync_combined_search_body_company_params_keywords_type_0 import SyncCombinedSearchBodyCompanyParamsKeywordsType0
        from ..models.sync_combined_search_body_company_params_exact_company_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyType0
        from ..models.sync_combined_search_body_company_params_special_flags_type_0 import SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0 import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0
        from ..models.sync_combined_search_body_company_params_tags_type_0 import SyncCombinedSearchBodyCompanyParamsTagsType0
        from ..models.sync_combined_search_body_company_params_investors_type_0 import SyncCombinedSearchBodyCompanyParamsInvestorsType0
        from ..models.sync_combined_search_body_company_params_founded_on_type_0 import SyncCombinedSearchBodyCompanyParamsFoundedOnType0
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0
        from ..models.sync_combined_search_body_company_params_total_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0
        from ..models.sync_combined_search_body_company_params_headquarters_state_name_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0
        from ..models.sync_combined_search_body_company_params_crunchbase_categories_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0
        from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0
        from ..models.sync_combined_search_body_company_params_employees_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeesType0
        from ..models.sync_combined_search_body_company_params_crunchbase_category_groups_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0
        from ..models.sync_combined_search_body_company_params_last_funded_on_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0
        from ..models.sync_combined_search_body_company_params_stage_type_0 import SyncCombinedSearchBodyCompanyParamsStageType0
        from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0 import SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0
        from ..models.sync_combined_search_body_company_params_headquarters_location_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0
        from ..models.sync_combined_search_body_company_params_linkedin_industries_type_0 import SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0
        from ..models.sync_combined_search_body_company_params_last_funded_on_type_1 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType1
        exact_company_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.exact_company_v2, Unset):
            exact_company_v2 = UNSET
        elif isinstance(self.exact_company_v2, SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0):
            exact_company_v2 = self.exact_company_v2.to_dict()
        else:
            exact_company_v2 = self.exact_company_v2

        domains: Union[None, Unset, list[str]]
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains


        else:
            domains = self.domains

        headquarters_country_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_country_code, Unset):
            headquarters_country_code = UNSET
        elif isinstance(self.headquarters_country_code, SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0):
            headquarters_country_code = self.headquarters_country_code.to_dict()
        else:
            headquarters_country_code = self.headquarters_country_code

        headquarters_state_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_state_name, Unset):
            headquarters_state_name = UNSET
        elif isinstance(self.headquarters_state_name, SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0):
            headquarters_state_name = self.headquarters_state_name.to_dict()
        else:
            headquarters_state_name = self.headquarters_state_name

        employee_count_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employee_count_v2, Unset):
            employee_count_v2 = UNSET
        elif isinstance(self.employee_count_v2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0):
            employee_count_v2 = self.employee_count_v2.to_dict()
        else:
            employee_count_v2 = self.employee_count_v2

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, SyncCombinedSearchBodyCompanyParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        industries_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.industries_v2, Unset):
            industries_v2 = UNSET
        elif isinstance(self.industries_v2, SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0):
            industries_v2 = self.industries_v2.to_dict()
        else:
            industries_v2 = self.industries_v2

        stage: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, SyncCombinedSearchBodyCompanyParamsStageType0):
            stage = self.stage.to_dict()
        else:
            stage = self.stage

        total_funding_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        elif isinstance(self.total_funding_usd, SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0):
            total_funding_usd = self.total_funding_usd.to_dict()
        else:
            total_funding_usd = self.total_funding_usd

        last_funding_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_funding_usd, Unset):
            last_funding_usd = UNSET
        elif isinstance(self.last_funding_usd, SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0):
            last_funding_usd = self.last_funding_usd.to_dict()
        else:
            last_funding_usd = self.last_funding_usd

        last_funded_on: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_funded_on, Unset):
            last_funded_on = UNSET
        elif isinstance(self.last_funded_on, SyncCombinedSearchBodyCompanyParamsLastFundedOnType0):
            last_funded_on = self.last_funded_on.to_dict()
        elif isinstance(self.last_funded_on, SyncCombinedSearchBodyCompanyParamsLastFundedOnType1):
            last_funded_on = self.last_funded_on.to_dict()
        else:
            last_funded_on = self.last_funded_on

        founded_on: Union[None, Unset, dict[str, Any]]
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, SyncCombinedSearchBodyCompanyParamsFoundedOnType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, SyncCombinedSearchBodyCompanyParamsFoundedOnType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        name_like: Union[None, Unset, dict[str, Any]]
        if isinstance(self.name_like, Unset):
            name_like = UNSET
        elif isinstance(self.name_like, SyncCombinedSearchBodyCompanyParamsNameLikeType0):
            name_like = self.name_like.to_dict()
        else:
            name_like = self.name_like

        exact_company: Union[None, Unset, dict[str, Any]]
        if isinstance(self.exact_company, Unset):
            exact_company = UNSET
        elif isinstance(self.exact_company, SyncCombinedSearchBodyCompanyParamsExactCompanyType0):
            exact_company = self.exact_company.to_dict()
        else:
            exact_company = self.exact_company

        accelerators_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.accelerators_v2, Unset):
            accelerators_v2 = UNSET
        elif isinstance(self.accelerators_v2, SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0):
            accelerators_v2 = self.accelerators_v2.to_dict()
        else:
            accelerators_v2 = self.accelerators_v2

        employee_trends: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employee_trends, Unset):
            employee_trends = UNSET
        elif isinstance(self.employee_trends, SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0):
            employee_trends = self.employee_trends.to_dict()
        else:
            employee_trends = self.employee_trends

        headquarters_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_location, Unset):
            headquarters_location = UNSET
        elif isinstance(self.headquarters_location, SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0):
            headquarters_location = self.headquarters_location.to_dict()
        else:
            headquarters_location = self.headquarters_location

        linkedin_slugs: Union[None, Unset, list[str]]
        if isinstance(self.linkedin_slugs, Unset):
            linkedin_slugs = UNSET
        elif isinstance(self.linkedin_slugs, list):
            linkedin_slugs = self.linkedin_slugs


        else:
            linkedin_slugs = self.linkedin_slugs

        special_flags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.special_flags, Unset):
            special_flags = UNSET
        elif isinstance(self.special_flags, SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0):
            special_flags = self.special_flags.to_dict()
        else:
            special_flags = self.special_flags

        employees: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employees, Unset):
            employees = UNSET
        elif isinstance(self.employees, SyncCombinedSearchBodyCompanyParamsEmployeesType0):
            employees = self.employees.to_dict()
        else:
            employees = self.employees

        revenue_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        elif isinstance(self.revenue_usd, SyncCombinedSearchBodyCompanyParamsRevenueUSDType0):
            revenue_usd = self.revenue_usd.to_dict()
        else:
            revenue_usd = self.revenue_usd

        naics_codes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, SyncCombinedSearchBodyCompanyParamsNaicsCodesType0):
            naics_codes = self.naics_codes.to_dict()
        else:
            naics_codes = self.naics_codes

        fortune_rankings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fortune_rankings, Unset):
            fortune_rankings = UNSET
        elif isinstance(self.fortune_rankings, SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0):
            fortune_rankings = self.fortune_rankings.to_dict()
        else:
            fortune_rankings = self.fortune_rankings

        job_postings_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_postings_v2, Unset):
            job_postings_v2 = UNSET
        elif isinstance(self.job_postings_v2, SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0):
            job_postings_v2 = self.job_postings_v2.to_dict()
        else:
            job_postings_v2 = self.job_postings_v2

        job_posting_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_posting_stats, Unset):
            job_posting_stats = UNSET
        elif isinstance(self.job_posting_stats, SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0):
            job_posting_stats = self.job_posting_stats.to_dict()
        else:
            job_posting_stats = self.job_posting_stats

        office_locations_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.office_locations_v2, Unset):
            office_locations_v2 = UNSET
        elif isinstance(self.office_locations_v2, SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0):
            office_locations_v2 = self.office_locations_v2.to_dict()
        else:
            office_locations_v2 = self.office_locations_v2

        tlds: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tlds, Unset):
            tlds = UNSET
        elif isinstance(self.tlds, SyncCombinedSearchBodyCompanyParamsTldsType0):
            tlds = self.tlds.to_dict()
        else:
            tlds = self.tlds

        num_words_in_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_words_in_name, Unset):
            num_words_in_name = UNSET
        elif isinstance(self.num_words_in_name, SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0):
            num_words_in_name = self.num_words_in_name.to_dict()
        else:
            num_words_in_name = self.num_words_in_name

        status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SyncCombinedSearchBodyCompanyParamsStatusType0):
            status = self.status.to_dict()
        else:
            status = self.status

        technologies: Union[None, Unset, dict[str, Any]]
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, SyncCombinedSearchBodyCompanyParamsTechnologiesType0):
            technologies = self.technologies.to_dict()
        else:
            technologies = self.technologies

        investors: Union[None, Unset, dict[str, Any]]
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, SyncCombinedSearchBodyCompanyParamsInvestorsType0):
            investors = self.investors.to_dict()
        else:
            investors = self.investors

        tags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, SyncCombinedSearchBodyCompanyParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        crunchbase_categories: Union[None, Unset, dict[str, Any]]
        if isinstance(self.crunchbase_categories, Unset):
            crunchbase_categories = UNSET
        elif isinstance(self.crunchbase_categories, SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0):
            crunchbase_categories = self.crunchbase_categories.to_dict()
        else:
            crunchbase_categories = self.crunchbase_categories

        crunchbase_category_groups: Union[None, Unset, dict[str, Any]]
        if isinstance(self.crunchbase_category_groups, Unset):
            crunchbase_category_groups = UNSET
        elif isinstance(self.crunchbase_category_groups, SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0):
            crunchbase_category_groups = self.crunchbase_category_groups.to_dict()
        else:
            crunchbase_category_groups = self.crunchbase_category_groups

        linkedin_industries: Union[None, Unset, dict[str, Any]]
        if isinstance(self.linkedin_industries, Unset):
            linkedin_industries = UNSET
        elif isinstance(self.linkedin_industries, SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0):
            linkedin_industries = self.linkedin_industries.to_dict()
        else:
            linkedin_industries = self.linkedin_industries

        crunchbase_slugs: Union[None, Unset, list[str]]
        if isinstance(self.crunchbase_slugs, Unset):
            crunchbase_slugs = UNSET
        elif isinstance(self.crunchbase_slugs, list):
            crunchbase_slugs = self.crunchbase_slugs


        else:
            crunchbase_slugs = self.crunchbase_slugs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        if employee_trends is not UNSET:
            field_dict["employeeTrends"] = employee_trends
        if headquarters_location is not UNSET:
            field_dict["headquartersLocation"] = headquarters_location
        if linkedin_slugs is not UNSET:
            field_dict["linkedinSlugs"] = linkedin_slugs
        if special_flags is not UNSET:
            field_dict["specialFlags"] = special_flags
        if employees is not UNSET:
            field_dict["employees"] = employees
        if revenue_usd is not UNSET:
            field_dict["revenueUSD"] = revenue_usd
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
        if investors is not UNSET:
            field_dict["investors"] = investors
        if tags is not UNSET:
            field_dict["tags"] = tags
        if crunchbase_categories is not UNSET:
            field_dict["crunchbaseCategories"] = crunchbase_categories
        if crunchbase_category_groups is not UNSET:
            field_dict["crunchbaseCategoryGroups"] = crunchbase_category_groups
        if linkedin_industries is not UNSET:
            field_dict["linkedinIndustries"] = linkedin_industries
        if crunchbase_slugs is not UNSET:
            field_dict["crunchbaseSlugs"] = crunchbase_slugs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_last_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0
        from ..models.sync_combined_search_body_company_params_headquarters_country_code_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0
        from ..models.sync_combined_search_body_company_params_num_words_in_name_type_0 import SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0
        from ..models.sync_combined_search_body_company_params_naics_codes_type_0 import SyncCombinedSearchBodyCompanyParamsNaicsCodesType0
        from ..models.sync_combined_search_body_company_params_tlds_type_0 import SyncCombinedSearchBodyCompanyParamsTldsType0
        from ..models.sync_combined_search_body_company_params_founded_on_type_1 import SyncCombinedSearchBodyCompanyParamsFoundedOnType1
        from ..models.sync_combined_search_body_company_params_name_like_type_0 import SyncCombinedSearchBodyCompanyParamsNameLikeType0
        from ..models.sync_combined_search_body_company_params_revenue_usd_type_0 import SyncCombinedSearchBodyCompanyParamsRevenueUSDType0
        from ..models.sync_combined_search_body_company_params_status_type_0 import SyncCombinedSearchBodyCompanyParamsStatusType0
        from ..models.sync_combined_search_body_company_params_fortune_rankings_type_0 import SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0
        from ..models.sync_combined_search_body_company_params_exact_company_v2_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0
        from ..models.sync_combined_search_body_company_params_industries_v2_type_0 import SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0
        from ..models.sync_combined_search_body_company_params_keywords_type_0 import SyncCombinedSearchBodyCompanyParamsKeywordsType0
        from ..models.sync_combined_search_body_company_params_exact_company_type_0 import SyncCombinedSearchBodyCompanyParamsExactCompanyType0
        from ..models.sync_combined_search_body_company_params_special_flags_type_0 import SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0 import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0
        from ..models.sync_combined_search_body_company_params_tags_type_0 import SyncCombinedSearchBodyCompanyParamsTagsType0
        from ..models.sync_combined_search_body_company_params_investors_type_0 import SyncCombinedSearchBodyCompanyParamsInvestorsType0
        from ..models.sync_combined_search_body_company_params_founded_on_type_0 import SyncCombinedSearchBodyCompanyParamsFoundedOnType0
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0
        from ..models.sync_combined_search_body_company_params_total_funding_usd_type_0 import SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0
        from ..models.sync_combined_search_body_company_params_headquarters_state_name_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0
        from ..models.sync_combined_search_body_company_params_crunchbase_categories_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0
        from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0
        from ..models.sync_combined_search_body_company_params_employees_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeesType0
        from ..models.sync_combined_search_body_company_params_crunchbase_category_groups_type_0 import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0
        from ..models.sync_combined_search_body_company_params_last_funded_on_type_0 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0
        from ..models.sync_combined_search_body_company_params_stage_type_0 import SyncCombinedSearchBodyCompanyParamsStageType0
        from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0 import SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0
        from ..models.sync_combined_search_body_company_params_headquarters_location_type_0 import SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0
        from ..models.sync_combined_search_body_company_params_linkedin_industries_type_0 import SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0
        from ..models.sync_combined_search_body_company_params_last_funded_on_type_1 import SyncCombinedSearchBodyCompanyParamsLastFundedOnType1
        d = dict(src_dict)
        def _parse_exact_company_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_v2_type_0 = SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0.from_dict(data)



                return exact_company_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsExactCompanyV2Type0', None, Unset], data)

        exact_company_v2 = _parse_exact_company_v2(d.pop("exactCompanyV2", UNSET))


        def _parse_domains(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        domains = _parse_domains(d.pop("domains", UNSET))


        def _parse_headquarters_country_code(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_country_code_type_0 = SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0.from_dict(data)



                return headquarters_country_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsHeadquartersCountryCodeType0', None, Unset], data)

        headquarters_country_code = _parse_headquarters_country_code(d.pop("headquartersCountryCode", UNSET))


        def _parse_headquarters_state_name(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_state_name_type_0 = SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0.from_dict(data)



                return headquarters_state_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsHeadquartersStateNameType0', None, Unset], data)

        headquarters_state_name = _parse_headquarters_state_name(d.pop("headquartersStateName", UNSET))


        def _parse_employee_count_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_v2_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0.from_dict(data)



                return employee_count_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0', None, Unset], data)

        employee_count_v2 = _parse_employee_count_v2(d.pop("employeeCountV2", UNSET))


        def _parse_keywords(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsKeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = SyncCombinedSearchBodyCompanyParamsKeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsKeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_industries_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industries_v2_type_0 = SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0.from_dict(data)



                return industries_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsIndustriesV2Type0', None, Unset], data)

        industries_v2 = _parse_industries_v2(d.pop("industriesV2", UNSET))


        def _parse_stage(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsStageType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stage_type_0 = SyncCombinedSearchBodyCompanyParamsStageType0.from_dict(data)



                return stage_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsStageType0', None, Unset], data)

        stage = _parse_stage(d.pop("stage", UNSET))


        def _parse_total_funding_usd(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_funding_usd_type_0 = SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0.from_dict(data)



                return total_funding_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsTotalFundingUSDType0', None, Unset], data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUSD", UNSET))


        def _parse_last_funding_usd(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funding_usd_type_0 = SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0.from_dict(data)



                return last_funding_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsLastFundingUSDType0', None, Unset], data)

        last_funding_usd = _parse_last_funding_usd(d.pop("lastFundingUSD", UNSET))


        def _parse_last_funded_on(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsLastFundedOnType0', 'SyncCombinedSearchBodyCompanyParamsLastFundedOnType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_0 = SyncCombinedSearchBodyCompanyParamsLastFundedOnType0.from_dict(data)



                return last_funded_on_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_1 = SyncCombinedSearchBodyCompanyParamsLastFundedOnType1.from_dict(data)



                return last_funded_on_type_1
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsLastFundedOnType0', 'SyncCombinedSearchBodyCompanyParamsLastFundedOnType1', None, Unset], data)

        last_funded_on = _parse_last_funded_on(d.pop("lastFundedOn", UNSET))


        def _parse_founded_on(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsFoundedOnType0', 'SyncCombinedSearchBodyCompanyParamsFoundedOnType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_0 = SyncCombinedSearchBodyCompanyParamsFoundedOnType0.from_dict(data)



                return founded_on_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_1 = SyncCombinedSearchBodyCompanyParamsFoundedOnType1.from_dict(data)



                return founded_on_type_1
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsFoundedOnType0', 'SyncCombinedSearchBodyCompanyParamsFoundedOnType1', None, Unset], data)

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))


        def _parse_name_like(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsNameLikeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_like_type_0 = SyncCombinedSearchBodyCompanyParamsNameLikeType0.from_dict(data)



                return name_like_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsNameLikeType0', None, Unset], data)

        name_like = _parse_name_like(d.pop("nameLike", UNSET))


        def _parse_exact_company(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsExactCompanyType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_type_0 = SyncCombinedSearchBodyCompanyParamsExactCompanyType0.from_dict(data)



                return exact_company_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsExactCompanyType0', None, Unset], data)

        exact_company = _parse_exact_company(d.pop("exactCompany", UNSET))


        def _parse_accelerators_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accelerators_v2_type_0 = SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0.from_dict(data)



                return accelerators_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0', None, Unset], data)

        accelerators_v2 = _parse_accelerators_v2(d.pop("acceleratorsV2", UNSET))


        def _parse_employee_trends(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_trends_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0.from_dict(data)



                return employee_trends_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0', None, Unset], data)

        employee_trends = _parse_employee_trends(d.pop("employeeTrends", UNSET))


        def _parse_headquarters_location(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_location_type_0 = SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0.from_dict(data)



                return headquarters_location_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsHeadquartersLocationType0', None, Unset], data)

        headquarters_location = _parse_headquarters_location(d.pop("headquartersLocation", UNSET))


        def _parse_linkedin_slugs(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_slugs_type_0 = cast(list[str], data)

                return linkedin_slugs_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        linkedin_slugs = _parse_linkedin_slugs(d.pop("linkedinSlugs", UNSET))


        def _parse_special_flags(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                special_flags_type_0 = SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0.from_dict(data)



                return special_flags_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsSpecialFlagsType0', None, Unset], data)

        special_flags = _parse_special_flags(d.pop("specialFlags", UNSET))


        def _parse_employees(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsEmployeesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employees_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeesType0.from_dict(data)



                return employees_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsEmployeesType0', None, Unset], data)

        employees = _parse_employees(d.pop("employees", UNSET))


        def _parse_revenue_usd(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsRevenueUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_usd_type_0 = SyncCombinedSearchBodyCompanyParamsRevenueUSDType0.from_dict(data)



                return revenue_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsRevenueUSDType0', None, Unset], data)

        revenue_usd = _parse_revenue_usd(d.pop("revenueUSD", UNSET))


        def _parse_naics_codes(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsNaicsCodesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                naics_codes_type_0 = SyncCombinedSearchBodyCompanyParamsNaicsCodesType0.from_dict(data)



                return naics_codes_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsNaicsCodesType0', None, Unset], data)

        naics_codes = _parse_naics_codes(d.pop("naicsCodes", UNSET))


        def _parse_fortune_rankings(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fortune_rankings_type_0 = SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0.from_dict(data)



                return fortune_rankings_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsFortuneRankingsType0', None, Unset], data)

        fortune_rankings = _parse_fortune_rankings(d.pop("fortuneRankings", UNSET))


        def _parse_job_postings_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_v2_type_0 = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0.from_dict(data)



                return job_postings_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0', None, Unset], data)

        job_postings_v2 = _parse_job_postings_v2(d.pop("jobPostingsV2", UNSET))


        def _parse_job_posting_stats(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_posting_stats_type_0 = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0.from_dict(data)



                return job_posting_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0', None, Unset], data)

        job_posting_stats = _parse_job_posting_stats(d.pop("jobPostingStats", UNSET))


        def _parse_office_locations_v2(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                office_locations_v2_type_0 = SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0.from_dict(data)



                return office_locations_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0', None, Unset], data)

        office_locations_v2 = _parse_office_locations_v2(d.pop("officeLocationsV2", UNSET))


        def _parse_tlds(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTldsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tlds_type_0 = SyncCombinedSearchBodyCompanyParamsTldsType0.from_dict(data)



                return tlds_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsTldsType0', None, Unset], data)

        tlds = _parse_tlds(d.pop("tlds", UNSET))


        def _parse_num_words_in_name(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_words_in_name_type_0 = SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0.from_dict(data)



                return num_words_in_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsNumWordsInNameType0', None, Unset], data)

        num_words_in_name = _parse_num_words_in_name(d.pop("numWordsInName", UNSET))


        def _parse_status(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsStatusType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = SyncCombinedSearchBodyCompanyParamsStatusType0.from_dict(data)



                return status_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsStatusType0', None, Unset], data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_technologies(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_type_0 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0.from_dict(data)



                return technologies_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0', None, Unset], data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))


        def _parse_investors(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsInvestorsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_type_0 = SyncCombinedSearchBodyCompanyParamsInvestorsType0.from_dict(data)



                return investors_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsInvestorsType0', None, Unset], data)

        investors = _parse_investors(d.pop("investors", UNSET))


        def _parse_tags(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = SyncCombinedSearchBodyCompanyParamsTagsType0.from_dict(data)



                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsTagsType0', None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_crunchbase_categories(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_categories_type_0 = SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0.from_dict(data)



                return crunchbase_categories_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0', None, Unset], data)

        crunchbase_categories = _parse_crunchbase_categories(d.pop("crunchbaseCategories", UNSET))


        def _parse_crunchbase_category_groups(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crunchbase_category_groups_type_0 = SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0.from_dict(data)



                return crunchbase_category_groups_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoryGroupsType0', None, Unset], data)

        crunchbase_category_groups = _parse_crunchbase_category_groups(d.pop("crunchbaseCategoryGroups", UNSET))


        def _parse_linkedin_industries(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linkedin_industries_type_0 = SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0.from_dict(data)



                return linkedin_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyCompanyParamsLinkedinIndustriesType0', None, Unset], data)

        linkedin_industries = _parse_linkedin_industries(d.pop("linkedinIndustries", UNSET))


        def _parse_crunchbase_slugs(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crunchbase_slugs_type_0 = cast(list[str], data)

                return crunchbase_slugs_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        crunchbase_slugs = _parse_crunchbase_slugs(d.pop("crunchbaseSlugs", UNSET))


        sync_combined_search_body_company_params = cls(
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
            employee_trends=employee_trends,
            headquarters_location=headquarters_location,
            linkedin_slugs=linkedin_slugs,
            special_flags=special_flags,
            employees=employees,
            revenue_usd=revenue_usd,
            naics_codes=naics_codes,
            fortune_rankings=fortune_rankings,
            job_postings_v2=job_postings_v2,
            job_posting_stats=job_posting_stats,
            office_locations_v2=office_locations_v2,
            tlds=tlds,
            num_words_in_name=num_words_in_name,
            status=status,
            technologies=technologies,
            investors=investors,
            tags=tags,
            crunchbase_categories=crunchbase_categories,
            crunchbase_category_groups=crunchbase_category_groups,
            linkedin_industries=linkedin_industries,
            crunchbase_slugs=crunchbase_slugs,
        )


        sync_combined_search_body_company_params.additional_properties = d
        return sync_combined_search_body_company_params

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
