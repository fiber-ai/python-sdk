from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_category_type_1 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_category_type_2_type_1 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_category_type_3_type_1 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_standard_industries_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_tags_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_role_count_matches_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investors_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_industries_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_best_funding_round_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_fortune_rankings_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_stock_info_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_location_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_num_matching_locations_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_custom_data_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_similar_companies_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_locations_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_round_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_acquisitions_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_count_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0





T = TypeVar("T", bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem")



@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItem:
    """ 
        Attributes:
            linkedin_id (Union[None, Unset, str]):
            accelerator_statuses (Union[None, Unset, list[str]]):
            accelerators (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item']]):
            blog_urls (Union[None, Unset, list[str]]):
            custom_data (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0', None,
                Unset]):
            domains (Union[None, Unset, list[str]]):
            emails (Union[None, Unset, list[str]]):
            phone_numbers (Union[None, Unset, list[str]]):
            employee_count_consensus
                (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0', None,
                Unset]):
            facebook_urls (Union[None, Unset, list[str]]):
            fortune_rankings (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item']]):
            founded_on_consensus (Union[None, Unset, str]):
            github_usernames (Union[None, Unset, list[str]]):
            instagram_handles (Union[None, Unset, list[str]]):
            latest_funding_consensus (Union[None, Unset, float]):
            linkedin_slugs (Union[None, Unset, list[str]]):
            linkedin_primary_slug (Union[None, Unset, str]):
            li_org_id (Union[None, Unset, str]):
            li_category (Union[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1,
                GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1,
                GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1, None, Unset]):
            li_job_posts_stats (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0',
                None, Unset]):
            li_description (Union[None, Unset, str]):
            li_follower_count (Union[None, Unset, float]):
            li_headline (Union[None, Unset, str]):
            li_industries (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item']]):
            li_locations (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item']]):
            li_specialties (Union[None, Unset, list[str]]):
            location_consensus
                (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0', None, Unset]):
            market_cap_usd (Union[None, Unset, float]):
            naics_codes (Union[None, Unset, list[str]]):
            names (Union[None, Unset, list[str]]):
            preferred_name (Union[None, Unset, str]):
            revenue_usd (Union[None, Unset, float]):
            standard_industries (Union[None, Unset,
                list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item]]):
            status_consensus (Union[None, Unset, str]):
            stock_info_consensus
                (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0', None, Unset]):
            tags (Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item]]):
            total_funding_consensus (Union[None, Unset, float]):
            twitter_handles (Union[None, Unset, list[str]]):
            websites (Union[None, Unset, list[str]]):
            wellfound_slugs (Union[None, Unset, list[str]]):
            youtube_urls (Union[None, Unset, list[str]]):
            role_count_matches (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item']]):
            num_matching_locations
                (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0', None, Unset]):
            linkedin_ids (Union[None, Unset, list[str]]):
            last_sort_key (Union[None, Unset, str]):
            relevance_score (Union[None, Unset, float]):
            num_li_locations (Union[None, Unset, float]):
            location_name (Union[None, Unset, str]):
            crunchbase_slug (Union[None, Unset, str]):
            crunchbase_rank (Union[None, Unset, float]):
            primary_role (Union[None, Unset, str]):
            roles (Union[None, Unset, list[str]]):
            short_description (Union[None, Unset, str]):
            long_description (Union[None, Unset, str]):
            crunchbase_category_groups (Union[None, Unset, list[str]]):
            crunchbase_categories (Union[None, Unset, list[str]]):
            is_subsidiary (Union[None, Unset, bool]):
            parent (Union[None, Unset, str]):
            num_funding_rounds (Union[None, Unset, float]):
            funding_rounds (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item']]):
            num_exits (Union[None, Unset, float]):
            investors (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item']]):
            acquisitions (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item']]):
            best_funding_round (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0',
                None, Unset]):
            funding_stage (Union[None, Unset, str]):
            alt_industries (Union[None, Unset, list[str]]):
            alt_keywords (Union[None, Unset, list[str]]):
            alt_description (Union[None, Unset, str]):
            employee_trends (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item']]):
            logo_url (Union[None, Unset, str]):
            similar_companies (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item']]):
            full_funding_rounds (Union[None, Unset,
                list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item']]):
            funding_round_stats
                (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0', None, Unset]):
            investment_stats (Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0',
                None, Unset]):
            is_investor (Union[None, Unset, bool]):
            investor_type (Union[None, Unset, str]):
            investor_categories (Union[None, Unset, list[str]]):
     """

    linkedin_id: Union[None, Unset, str] = UNSET
    accelerator_statuses: Union[None, Unset, list[str]] = UNSET
    accelerators: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item']] = UNSET
    blog_urls: Union[None, Unset, list[str]] = UNSET
    custom_data: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0', None, Unset] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    emails: Union[None, Unset, list[str]] = UNSET
    phone_numbers: Union[None, Unset, list[str]] = UNSET
    employee_count_consensus: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0', None, Unset] = UNSET
    facebook_urls: Union[None, Unset, list[str]] = UNSET
    fortune_rankings: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item']] = UNSET
    founded_on_consensus: Union[None, Unset, str] = UNSET
    github_usernames: Union[None, Unset, list[str]] = UNSET
    instagram_handles: Union[None, Unset, list[str]] = UNSET
    latest_funding_consensus: Union[None, Unset, float] = UNSET
    linkedin_slugs: Union[None, Unset, list[str]] = UNSET
    linkedin_primary_slug: Union[None, Unset, str] = UNSET
    li_org_id: Union[None, Unset, str] = UNSET
    li_category: Union[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1, None, Unset] = UNSET
    li_job_posts_stats: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0', None, Unset] = UNSET
    li_description: Union[None, Unset, str] = UNSET
    li_follower_count: Union[None, Unset, float] = UNSET
    li_headline: Union[None, Unset, str] = UNSET
    li_industries: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item']] = UNSET
    li_locations: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item']] = UNSET
    li_specialties: Union[None, Unset, list[str]] = UNSET
    location_consensus: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0', None, Unset] = UNSET
    market_cap_usd: Union[None, Unset, float] = UNSET
    naics_codes: Union[None, Unset, list[str]] = UNSET
    names: Union[None, Unset, list[str]] = UNSET
    preferred_name: Union[None, Unset, str] = UNSET
    revenue_usd: Union[None, Unset, float] = UNSET
    standard_industries: Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item]] = UNSET
    status_consensus: Union[None, Unset, str] = UNSET
    stock_info_consensus: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0', None, Unset] = UNSET
    tags: Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item]] = UNSET
    total_funding_consensus: Union[None, Unset, float] = UNSET
    twitter_handles: Union[None, Unset, list[str]] = UNSET
    websites: Union[None, Unset, list[str]] = UNSET
    wellfound_slugs: Union[None, Unset, list[str]] = UNSET
    youtube_urls: Union[None, Unset, list[str]] = UNSET
    role_count_matches: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item']] = UNSET
    num_matching_locations: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0', None, Unset] = UNSET
    linkedin_ids: Union[None, Unset, list[str]] = UNSET
    last_sort_key: Union[None, Unset, str] = UNSET
    relevance_score: Union[None, Unset, float] = UNSET
    num_li_locations: Union[None, Unset, float] = UNSET
    location_name: Union[None, Unset, str] = UNSET
    crunchbase_slug: Union[None, Unset, str] = UNSET
    crunchbase_rank: Union[None, Unset, float] = UNSET
    primary_role: Union[None, Unset, str] = UNSET
    roles: Union[None, Unset, list[str]] = UNSET
    short_description: Union[None, Unset, str] = UNSET
    long_description: Union[None, Unset, str] = UNSET
    crunchbase_category_groups: Union[None, Unset, list[str]] = UNSET
    crunchbase_categories: Union[None, Unset, list[str]] = UNSET
    is_subsidiary: Union[None, Unset, bool] = UNSET
    parent: Union[None, Unset, str] = UNSET
    num_funding_rounds: Union[None, Unset, float] = UNSET
    funding_rounds: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item']] = UNSET
    num_exits: Union[None, Unset, float] = UNSET
    investors: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item']] = UNSET
    acquisitions: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item']] = UNSET
    best_funding_round: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0', None, Unset] = UNSET
    funding_stage: Union[None, Unset, str] = UNSET
    alt_industries: Union[None, Unset, list[str]] = UNSET
    alt_keywords: Union[None, Unset, list[str]] = UNSET
    alt_description: Union[None, Unset, str] = UNSET
    employee_trends: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item']] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    similar_companies: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item']] = UNSET
    full_funding_rounds: Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item']] = UNSET
    funding_round_stats: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0', None, Unset] = UNSET
    investment_stats: Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0', None, Unset] = UNSET
    is_investor: Union[None, Unset, bool] = UNSET
    investor_type: Union[None, Unset, str] = UNSET
    investor_categories: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_role_count_matches_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investors_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_industries_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_best_funding_round_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_fortune_rankings_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_stock_info_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_location_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_num_matching_locations_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_custom_data_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_similar_companies_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_locations_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_round_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_acquisitions_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_count_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0
        linkedin_id: Union[None, Unset, str]
        if isinstance(self.linkedin_id, Unset):
            linkedin_id = UNSET
        else:
            linkedin_id = self.linkedin_id

        accelerator_statuses: Union[None, Unset, list[str]]
        if isinstance(self.accelerator_statuses, Unset):
            accelerator_statuses = UNSET
        elif isinstance(self.accelerator_statuses, list):
            accelerator_statuses = self.accelerator_statuses


        else:
            accelerator_statuses = self.accelerator_statuses

        accelerators: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.accelerators, Unset):
            accelerators = UNSET
        elif isinstance(self.accelerators, list):
            accelerators = []
            for accelerators_type_0_item_data in self.accelerators:
                accelerators_type_0_item = accelerators_type_0_item_data.to_dict()
                accelerators.append(accelerators_type_0_item)


        else:
            accelerators = self.accelerators

        blog_urls: Union[None, Unset, list[str]]
        if isinstance(self.blog_urls, Unset):
            blog_urls = UNSET
        elif isinstance(self.blog_urls, list):
            blog_urls = self.blog_urls


        else:
            blog_urls = self.blog_urls

        custom_data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_data, Unset):
            custom_data = UNSET
        elif isinstance(self.custom_data, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0):
            custom_data = self.custom_data.to_dict()
        else:
            custom_data = self.custom_data

        domains: Union[None, Unset, list[str]]
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains


        else:
            domains = self.domains

        emails: Union[None, Unset, list[str]]
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = self.emails


        else:
            emails = self.emails

        phone_numbers: Union[None, Unset, list[str]]
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = self.phone_numbers


        else:
            phone_numbers = self.phone_numbers

        employee_count_consensus: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employee_count_consensus, Unset):
            employee_count_consensus = UNSET
        elif isinstance(self.employee_count_consensus, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0):
            employee_count_consensus = self.employee_count_consensus.to_dict()
        else:
            employee_count_consensus = self.employee_count_consensus

        facebook_urls: Union[None, Unset, list[str]]
        if isinstance(self.facebook_urls, Unset):
            facebook_urls = UNSET
        elif isinstance(self.facebook_urls, list):
            facebook_urls = self.facebook_urls


        else:
            facebook_urls = self.facebook_urls

        fortune_rankings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.fortune_rankings, Unset):
            fortune_rankings = UNSET
        elif isinstance(self.fortune_rankings, list):
            fortune_rankings = []
            for fortune_rankings_type_0_item_data in self.fortune_rankings:
                fortune_rankings_type_0_item = fortune_rankings_type_0_item_data.to_dict()
                fortune_rankings.append(fortune_rankings_type_0_item)


        else:
            fortune_rankings = self.fortune_rankings

        founded_on_consensus: Union[None, Unset, str]
        if isinstance(self.founded_on_consensus, Unset):
            founded_on_consensus = UNSET
        else:
            founded_on_consensus = self.founded_on_consensus

        github_usernames: Union[None, Unset, list[str]]
        if isinstance(self.github_usernames, Unset):
            github_usernames = UNSET
        elif isinstance(self.github_usernames, list):
            github_usernames = self.github_usernames


        else:
            github_usernames = self.github_usernames

        instagram_handles: Union[None, Unset, list[str]]
        if isinstance(self.instagram_handles, Unset):
            instagram_handles = UNSET
        elif isinstance(self.instagram_handles, list):
            instagram_handles = self.instagram_handles


        else:
            instagram_handles = self.instagram_handles

        latest_funding_consensus: Union[None, Unset, float]
        if isinstance(self.latest_funding_consensus, Unset):
            latest_funding_consensus = UNSET
        else:
            latest_funding_consensus = self.latest_funding_consensus

        linkedin_slugs: Union[None, Unset, list[str]]
        if isinstance(self.linkedin_slugs, Unset):
            linkedin_slugs = UNSET
        elif isinstance(self.linkedin_slugs, list):
            linkedin_slugs = self.linkedin_slugs


        else:
            linkedin_slugs = self.linkedin_slugs

        linkedin_primary_slug: Union[None, Unset, str]
        if isinstance(self.linkedin_primary_slug, Unset):
            linkedin_primary_slug = UNSET
        else:
            linkedin_primary_slug = self.linkedin_primary_slug

        li_org_id: Union[None, Unset, str]
        if isinstance(self.li_org_id, Unset):
            li_org_id = UNSET
        else:
            li_org_id = self.li_org_id

        li_category: Union[None, Unset, str]
        if isinstance(self.li_category, Unset):
            li_category = UNSET
        elif isinstance(self.li_category, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1):
            li_category = self.li_category.value
        elif isinstance(self.li_category, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1):
            li_category = self.li_category.value
        elif isinstance(self.li_category, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1):
            li_category = self.li_category.value
        else:
            li_category = self.li_category

        li_job_posts_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.li_job_posts_stats, Unset):
            li_job_posts_stats = UNSET
        elif isinstance(self.li_job_posts_stats, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0):
            li_job_posts_stats = self.li_job_posts_stats.to_dict()
        else:
            li_job_posts_stats = self.li_job_posts_stats

        li_description: Union[None, Unset, str]
        if isinstance(self.li_description, Unset):
            li_description = UNSET
        else:
            li_description = self.li_description

        li_follower_count: Union[None, Unset, float]
        if isinstance(self.li_follower_count, Unset):
            li_follower_count = UNSET
        else:
            li_follower_count = self.li_follower_count

        li_headline: Union[None, Unset, str]
        if isinstance(self.li_headline, Unset):
            li_headline = UNSET
        else:
            li_headline = self.li_headline

        li_industries: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.li_industries, Unset):
            li_industries = UNSET
        elif isinstance(self.li_industries, list):
            li_industries = []
            for li_industries_type_0_item_data in self.li_industries:
                li_industries_type_0_item = li_industries_type_0_item_data.to_dict()
                li_industries.append(li_industries_type_0_item)


        else:
            li_industries = self.li_industries

        li_locations: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.li_locations, Unset):
            li_locations = UNSET
        elif isinstance(self.li_locations, list):
            li_locations = []
            for li_locations_type_0_item_data in self.li_locations:
                li_locations_type_0_item = li_locations_type_0_item_data.to_dict()
                li_locations.append(li_locations_type_0_item)


        else:
            li_locations = self.li_locations

        li_specialties: Union[None, Unset, list[str]]
        if isinstance(self.li_specialties, Unset):
            li_specialties = UNSET
        elif isinstance(self.li_specialties, list):
            li_specialties = self.li_specialties


        else:
            li_specialties = self.li_specialties

        location_consensus: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location_consensus, Unset):
            location_consensus = UNSET
        elif isinstance(self.location_consensus, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0):
            location_consensus = self.location_consensus.to_dict()
        else:
            location_consensus = self.location_consensus

        market_cap_usd: Union[None, Unset, float]
        if isinstance(self.market_cap_usd, Unset):
            market_cap_usd = UNSET
        else:
            market_cap_usd = self.market_cap_usd

        naics_codes: Union[None, Unset, list[str]]
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, list):
            naics_codes = self.naics_codes


        else:
            naics_codes = self.naics_codes

        names: Union[None, Unset, list[str]]
        if isinstance(self.names, Unset):
            names = UNSET
        elif isinstance(self.names, list):
            names = self.names


        else:
            names = self.names

        preferred_name: Union[None, Unset, str]
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        revenue_usd: Union[None, Unset, float]
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        else:
            revenue_usd = self.revenue_usd

        standard_industries: Union[None, Unset, list[str]]
        if isinstance(self.standard_industries, Unset):
            standard_industries = UNSET
        elif isinstance(self.standard_industries, list):
            standard_industries = []
            for standard_industries_type_0_item_data in self.standard_industries:
                standard_industries_type_0_item = standard_industries_type_0_item_data.value
                standard_industries.append(standard_industries_type_0_item)


        else:
            standard_industries = self.standard_industries

        status_consensus: Union[None, Unset, str]
        if isinstance(self.status_consensus, Unset):
            status_consensus = UNSET
        else:
            status_consensus = self.status_consensus

        stock_info_consensus: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stock_info_consensus, Unset):
            stock_info_consensus = UNSET
        elif isinstance(self.stock_info_consensus, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0):
            stock_info_consensus = self.stock_info_consensus.to_dict()
        else:
            stock_info_consensus = self.stock_info_consensus

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.value
                tags.append(tags_type_0_item)


        else:
            tags = self.tags

        total_funding_consensus: Union[None, Unset, float]
        if isinstance(self.total_funding_consensus, Unset):
            total_funding_consensus = UNSET
        else:
            total_funding_consensus = self.total_funding_consensus

        twitter_handles: Union[None, Unset, list[str]]
        if isinstance(self.twitter_handles, Unset):
            twitter_handles = UNSET
        elif isinstance(self.twitter_handles, list):
            twitter_handles = self.twitter_handles


        else:
            twitter_handles = self.twitter_handles

        websites: Union[None, Unset, list[str]]
        if isinstance(self.websites, Unset):
            websites = UNSET
        elif isinstance(self.websites, list):
            websites = self.websites


        else:
            websites = self.websites

        wellfound_slugs: Union[None, Unset, list[str]]
        if isinstance(self.wellfound_slugs, Unset):
            wellfound_slugs = UNSET
        elif isinstance(self.wellfound_slugs, list):
            wellfound_slugs = self.wellfound_slugs


        else:
            wellfound_slugs = self.wellfound_slugs

        youtube_urls: Union[None, Unset, list[str]]
        if isinstance(self.youtube_urls, Unset):
            youtube_urls = UNSET
        elif isinstance(self.youtube_urls, list):
            youtube_urls = self.youtube_urls


        else:
            youtube_urls = self.youtube_urls

        role_count_matches: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.role_count_matches, Unset):
            role_count_matches = UNSET
        elif isinstance(self.role_count_matches, list):
            role_count_matches = []
            for role_count_matches_type_0_item_data in self.role_count_matches:
                role_count_matches_type_0_item = role_count_matches_type_0_item_data.to_dict()
                role_count_matches.append(role_count_matches_type_0_item)


        else:
            role_count_matches = self.role_count_matches

        num_matching_locations: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_matching_locations, Unset):
            num_matching_locations = UNSET
        elif isinstance(self.num_matching_locations, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0):
            num_matching_locations = self.num_matching_locations.to_dict()
        else:
            num_matching_locations = self.num_matching_locations

        linkedin_ids: Union[None, Unset, list[str]]
        if isinstance(self.linkedin_ids, Unset):
            linkedin_ids = UNSET
        elif isinstance(self.linkedin_ids, list):
            linkedin_ids = self.linkedin_ids


        else:
            linkedin_ids = self.linkedin_ids

        last_sort_key: Union[None, Unset, str]
        if isinstance(self.last_sort_key, Unset):
            last_sort_key = UNSET
        else:
            last_sort_key = self.last_sort_key

        relevance_score: Union[None, Unset, float]
        if isinstance(self.relevance_score, Unset):
            relevance_score = UNSET
        else:
            relevance_score = self.relevance_score

        num_li_locations: Union[None, Unset, float]
        if isinstance(self.num_li_locations, Unset):
            num_li_locations = UNSET
        else:
            num_li_locations = self.num_li_locations

        location_name: Union[None, Unset, str]
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        crunchbase_slug: Union[None, Unset, str]
        if isinstance(self.crunchbase_slug, Unset):
            crunchbase_slug = UNSET
        else:
            crunchbase_slug = self.crunchbase_slug

        crunchbase_rank: Union[None, Unset, float]
        if isinstance(self.crunchbase_rank, Unset):
            crunchbase_rank = UNSET
        else:
            crunchbase_rank = self.crunchbase_rank

        primary_role: Union[None, Unset, str]
        if isinstance(self.primary_role, Unset):
            primary_role = UNSET
        else:
            primary_role = self.primary_role

        roles: Union[None, Unset, list[str]]
        if isinstance(self.roles, Unset):
            roles = UNSET
        elif isinstance(self.roles, list):
            roles = self.roles


        else:
            roles = self.roles

        short_description: Union[None, Unset, str]
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        long_description: Union[None, Unset, str]
        if isinstance(self.long_description, Unset):
            long_description = UNSET
        else:
            long_description = self.long_description

        crunchbase_category_groups: Union[None, Unset, list[str]]
        if isinstance(self.crunchbase_category_groups, Unset):
            crunchbase_category_groups = UNSET
        elif isinstance(self.crunchbase_category_groups, list):
            crunchbase_category_groups = self.crunchbase_category_groups


        else:
            crunchbase_category_groups = self.crunchbase_category_groups

        crunchbase_categories: Union[None, Unset, list[str]]
        if isinstance(self.crunchbase_categories, Unset):
            crunchbase_categories = UNSET
        elif isinstance(self.crunchbase_categories, list):
            crunchbase_categories = self.crunchbase_categories


        else:
            crunchbase_categories = self.crunchbase_categories

        is_subsidiary: Union[None, Unset, bool]
        if isinstance(self.is_subsidiary, Unset):
            is_subsidiary = UNSET
        else:
            is_subsidiary = self.is_subsidiary

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        num_funding_rounds: Union[None, Unset, float]
        if isinstance(self.num_funding_rounds, Unset):
            num_funding_rounds = UNSET
        else:
            num_funding_rounds = self.num_funding_rounds

        funding_rounds: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.funding_rounds, Unset):
            funding_rounds = UNSET
        elif isinstance(self.funding_rounds, list):
            funding_rounds = []
            for funding_rounds_type_0_item_data in self.funding_rounds:
                funding_rounds_type_0_item = funding_rounds_type_0_item_data.to_dict()
                funding_rounds.append(funding_rounds_type_0_item)


        else:
            funding_rounds = self.funding_rounds

        num_exits: Union[None, Unset, float]
        if isinstance(self.num_exits, Unset):
            num_exits = UNSET
        else:
            num_exits = self.num_exits

        investors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, list):
            investors = []
            for investors_type_0_item_data in self.investors:
                investors_type_0_item = investors_type_0_item_data.to_dict()
                investors.append(investors_type_0_item)


        else:
            investors = self.investors

        acquisitions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.acquisitions, Unset):
            acquisitions = UNSET
        elif isinstance(self.acquisitions, list):
            acquisitions = []
            for acquisitions_type_0_item_data in self.acquisitions:
                acquisitions_type_0_item = acquisitions_type_0_item_data.to_dict()
                acquisitions.append(acquisitions_type_0_item)


        else:
            acquisitions = self.acquisitions

        best_funding_round: Union[None, Unset, dict[str, Any]]
        if isinstance(self.best_funding_round, Unset):
            best_funding_round = UNSET
        elif isinstance(self.best_funding_round, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0):
            best_funding_round = self.best_funding_round.to_dict()
        else:
            best_funding_round = self.best_funding_round

        funding_stage: Union[None, Unset, str]
        if isinstance(self.funding_stage, Unset):
            funding_stage = UNSET
        else:
            funding_stage = self.funding_stage

        alt_industries: Union[None, Unset, list[str]]
        if isinstance(self.alt_industries, Unset):
            alt_industries = UNSET
        elif isinstance(self.alt_industries, list):
            alt_industries = self.alt_industries


        else:
            alt_industries = self.alt_industries

        alt_keywords: Union[None, Unset, list[str]]
        if isinstance(self.alt_keywords, Unset):
            alt_keywords = UNSET
        elif isinstance(self.alt_keywords, list):
            alt_keywords = self.alt_keywords


        else:
            alt_keywords = self.alt_keywords

        alt_description: Union[None, Unset, str]
        if isinstance(self.alt_description, Unset):
            alt_description = UNSET
        else:
            alt_description = self.alt_description

        employee_trends: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.employee_trends, Unset):
            employee_trends = UNSET
        elif isinstance(self.employee_trends, list):
            employee_trends = []
            for employee_trends_type_0_item_data in self.employee_trends:
                employee_trends_type_0_item = employee_trends_type_0_item_data.to_dict()
                employee_trends.append(employee_trends_type_0_item)


        else:
            employee_trends = self.employee_trends

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        similar_companies: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.similar_companies, Unset):
            similar_companies = UNSET
        elif isinstance(self.similar_companies, list):
            similar_companies = []
            for similar_companies_type_0_item_data in self.similar_companies:
                similar_companies_type_0_item = similar_companies_type_0_item_data.to_dict()
                similar_companies.append(similar_companies_type_0_item)


        else:
            similar_companies = self.similar_companies

        full_funding_rounds: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.full_funding_rounds, Unset):
            full_funding_rounds = UNSET
        elif isinstance(self.full_funding_rounds, list):
            full_funding_rounds = []
            for full_funding_rounds_type_0_item_data in self.full_funding_rounds:
                full_funding_rounds_type_0_item = full_funding_rounds_type_0_item_data.to_dict()
                full_funding_rounds.append(full_funding_rounds_type_0_item)


        else:
            full_funding_rounds = self.full_funding_rounds

        funding_round_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.funding_round_stats, Unset):
            funding_round_stats = UNSET
        elif isinstance(self.funding_round_stats, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0):
            funding_round_stats = self.funding_round_stats.to_dict()
        else:
            funding_round_stats = self.funding_round_stats

        investment_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.investment_stats, Unset):
            investment_stats = UNSET
        elif isinstance(self.investment_stats, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0):
            investment_stats = self.investment_stats.to_dict()
        else:
            investment_stats = self.investment_stats

        is_investor: Union[None, Unset, bool]
        if isinstance(self.is_investor, Unset):
            is_investor = UNSET
        else:
            is_investor = self.is_investor

        investor_type: Union[None, Unset, str]
        if isinstance(self.investor_type, Unset):
            investor_type = UNSET
        else:
            investor_type = self.investor_type

        investor_categories: Union[None, Unset, list[str]]
        if isinstance(self.investor_categories, Unset):
            investor_categories = UNSET
        elif isinstance(self.investor_categories, list):
            investor_categories = self.investor_categories


        else:
            investor_categories = self.investor_categories


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linkedin_id is not UNSET:
            field_dict["linkedin_id"] = linkedin_id
        if accelerator_statuses is not UNSET:
            field_dict["accelerator_statuses"] = accelerator_statuses
        if accelerators is not UNSET:
            field_dict["accelerators"] = accelerators
        if blog_urls is not UNSET:
            field_dict["blog_urls"] = blog_urls
        if custom_data is not UNSET:
            field_dict["custom_data"] = custom_data
        if domains is not UNSET:
            field_dict["domains"] = domains
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if employee_count_consensus is not UNSET:
            field_dict["employee_count_consensus"] = employee_count_consensus
        if facebook_urls is not UNSET:
            field_dict["facebook_urls"] = facebook_urls
        if fortune_rankings is not UNSET:
            field_dict["fortune_rankings"] = fortune_rankings
        if founded_on_consensus is not UNSET:
            field_dict["founded_on_consensus"] = founded_on_consensus
        if github_usernames is not UNSET:
            field_dict["github_usernames"] = github_usernames
        if instagram_handles is not UNSET:
            field_dict["instagram_handles"] = instagram_handles
        if latest_funding_consensus is not UNSET:
            field_dict["latest_funding_consensus"] = latest_funding_consensus
        if linkedin_slugs is not UNSET:
            field_dict["linkedin_slugs"] = linkedin_slugs
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if li_org_id is not UNSET:
            field_dict["li_org_id"] = li_org_id
        if li_category is not UNSET:
            field_dict["li_category"] = li_category
        if li_job_posts_stats is not UNSET:
            field_dict["li_job_posts_stats"] = li_job_posts_stats
        if li_description is not UNSET:
            field_dict["li_description"] = li_description
        if li_follower_count is not UNSET:
            field_dict["li_follower_count"] = li_follower_count
        if li_headline is not UNSET:
            field_dict["li_headline"] = li_headline
        if li_industries is not UNSET:
            field_dict["li_industries"] = li_industries
        if li_locations is not UNSET:
            field_dict["li_locations"] = li_locations
        if li_specialties is not UNSET:
            field_dict["li_specialties"] = li_specialties
        if location_consensus is not UNSET:
            field_dict["location_consensus"] = location_consensus
        if market_cap_usd is not UNSET:
            field_dict["market_cap_usd"] = market_cap_usd
        if naics_codes is not UNSET:
            field_dict["naics_codes"] = naics_codes
        if names is not UNSET:
            field_dict["names"] = names
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if revenue_usd is not UNSET:
            field_dict["revenue_usd"] = revenue_usd
        if standard_industries is not UNSET:
            field_dict["standard_industries"] = standard_industries
        if status_consensus is not UNSET:
            field_dict["status_consensus"] = status_consensus
        if stock_info_consensus is not UNSET:
            field_dict["stock_info_consensus"] = stock_info_consensus
        if tags is not UNSET:
            field_dict["tags"] = tags
        if total_funding_consensus is not UNSET:
            field_dict["total_funding_consensus"] = total_funding_consensus
        if twitter_handles is not UNSET:
            field_dict["twitter_handles"] = twitter_handles
        if websites is not UNSET:
            field_dict["websites"] = websites
        if wellfound_slugs is not UNSET:
            field_dict["wellfound_slugs"] = wellfound_slugs
        if youtube_urls is not UNSET:
            field_dict["youtube_urls"] = youtube_urls
        if role_count_matches is not UNSET:
            field_dict["role_count_matches"] = role_count_matches
        if num_matching_locations is not UNSET:
            field_dict["num_matching_locations"] = num_matching_locations
        if linkedin_ids is not UNSET:
            field_dict["linkedin_ids"] = linkedin_ids
        if last_sort_key is not UNSET:
            field_dict["last_sort_key"] = last_sort_key
        if relevance_score is not UNSET:
            field_dict["relevance_score"] = relevance_score
        if num_li_locations is not UNSET:
            field_dict["num_li_locations"] = num_li_locations
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if crunchbase_slug is not UNSET:
            field_dict["crunchbase_slug"] = crunchbase_slug
        if crunchbase_rank is not UNSET:
            field_dict["crunchbase_rank"] = crunchbase_rank
        if primary_role is not UNSET:
            field_dict["primary_role"] = primary_role
        if roles is not UNSET:
            field_dict["roles"] = roles
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if long_description is not UNSET:
            field_dict["long_description"] = long_description
        if crunchbase_category_groups is not UNSET:
            field_dict["crunchbase_category_groups"] = crunchbase_category_groups
        if crunchbase_categories is not UNSET:
            field_dict["crunchbase_categories"] = crunchbase_categories
        if is_subsidiary is not UNSET:
            field_dict["is_subsidiary"] = is_subsidiary
        if parent is not UNSET:
            field_dict["parent"] = parent
        if num_funding_rounds is not UNSET:
            field_dict["num_funding_rounds"] = num_funding_rounds
        if funding_rounds is not UNSET:
            field_dict["funding_rounds"] = funding_rounds
        if num_exits is not UNSET:
            field_dict["num_exits"] = num_exits
        if investors is not UNSET:
            field_dict["investors"] = investors
        if acquisitions is not UNSET:
            field_dict["acquisitions"] = acquisitions
        if best_funding_round is not UNSET:
            field_dict["best_funding_round"] = best_funding_round
        if funding_stage is not UNSET:
            field_dict["funding_stage"] = funding_stage
        if alt_industries is not UNSET:
            field_dict["alt_industries"] = alt_industries
        if alt_keywords is not UNSET:
            field_dict["alt_keywords"] = alt_keywords
        if alt_description is not UNSET:
            field_dict["alt_description"] = alt_description
        if employee_trends is not UNSET:
            field_dict["employee_trends"] = employee_trends
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if similar_companies is not UNSET:
            field_dict["similar_companies"] = similar_companies
        if full_funding_rounds is not UNSET:
            field_dict["full_funding_rounds"] = full_funding_rounds
        if funding_round_stats is not UNSET:
            field_dict["funding_round_stats"] = funding_round_stats
        if investment_stats is not UNSET:
            field_dict["investment_stats"] = investment_stats
        if is_investor is not UNSET:
            field_dict["is_investor"] = is_investor
        if investor_type is not UNSET:
            field_dict["investor_type"] = investor_type
        if investor_categories is not UNSET:
            field_dict["investor_categories"] = investor_categories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_role_count_matches_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investors_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_industries_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_best_funding_round_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_fortune_rankings_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_rounds_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_stock_info_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_location_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_num_matching_locations_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_custom_data_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_similar_companies_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_locations_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_funding_round_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_acquisitions_type_0_item import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_count_consensus_type_0 import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0
        d = dict(src_dict)
        def _parse_linkedin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_id = _parse_linkedin_id(d.pop("linkedin_id", UNSET))


        def _parse_accelerator_statuses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accelerator_statuses_type_0 = cast(list[str], data)

                return accelerator_statuses_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        accelerator_statuses = _parse_accelerator_statuses(d.pop("accelerator_statuses", UNSET))


        def _parse_accelerators(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accelerators_type_0 = []
                _accelerators_type_0 = data
                for accelerators_type_0_item_data in (_accelerators_type_0):
                    accelerators_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item.from_dict(accelerators_type_0_item_data)



                    accelerators_type_0.append(accelerators_type_0_item)

                return accelerators_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0Item']], data)

        accelerators = _parse_accelerators(d.pop("accelerators", UNSET))


        def _parse_blog_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blog_urls_type_0 = cast(list[str], data)

                return blog_urls_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        blog_urls = _parse_blog_urls(d.pop("blog_urls", UNSET))


        def _parse_custom_data(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_data_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0.from_dict(data)



                return custom_data_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemCustomDataType0', None, Unset], data)

        custom_data = _parse_custom_data(d.pop("custom_data", UNSET))


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


        def _parse_emails(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = cast(list[str], data)

                return emails_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        emails = _parse_emails(d.pop("emails", UNSET))


        def _parse_phone_numbers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = cast(list[str], data)

                return phone_numbers_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        phone_numbers = _parse_phone_numbers(d.pop("phone_numbers", UNSET))


        def _parse_employee_count_consensus(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_consensus_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0.from_dict(data)



                return employee_count_consensus_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeCountConsensusType0', None, Unset], data)

        employee_count_consensus = _parse_employee_count_consensus(d.pop("employee_count_consensus", UNSET))


        def _parse_facebook_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facebook_urls_type_0 = cast(list[str], data)

                return facebook_urls_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        facebook_urls = _parse_facebook_urls(d.pop("facebook_urls", UNSET))


        def _parse_fortune_rankings(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fortune_rankings_type_0 = []
                _fortune_rankings_type_0 = data
                for fortune_rankings_type_0_item_data in (_fortune_rankings_type_0):
                    fortune_rankings_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item.from_dict(fortune_rankings_type_0_item_data)



                    fortune_rankings_type_0.append(fortune_rankings_type_0_item)

                return fortune_rankings_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFortuneRankingsType0Item']], data)

        fortune_rankings = _parse_fortune_rankings(d.pop("fortune_rankings", UNSET))


        def _parse_founded_on_consensus(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        founded_on_consensus = _parse_founded_on_consensus(d.pop("founded_on_consensus", UNSET))


        def _parse_github_usernames(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                github_usernames_type_0 = cast(list[str], data)

                return github_usernames_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        github_usernames = _parse_github_usernames(d.pop("github_usernames", UNSET))


        def _parse_instagram_handles(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instagram_handles_type_0 = cast(list[str], data)

                return instagram_handles_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        instagram_handles = _parse_instagram_handles(d.pop("instagram_handles", UNSET))


        def _parse_latest_funding_consensus(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latest_funding_consensus = _parse_latest_funding_consensus(d.pop("latest_funding_consensus", UNSET))


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

        linkedin_slugs = _parse_linkedin_slugs(d.pop("linkedin_slugs", UNSET))


        def _parse_linkedin_primary_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_primary_slug = _parse_linkedin_primary_slug(d.pop("linkedin_primary_slug", UNSET))


        def _parse_li_org_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        li_org_id = _parse_li_org_id(d.pop("li_org_id", UNSET))


        def _parse_li_category(data: object) -> Union[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                li_category_type_1 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1(data)



                return li_category_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                li_category_type_2_type_1 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1(data)



                return li_category_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                li_category_type_3_type_1 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1(data)



                return li_category_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType2Type1, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiCategoryType3Type1, None, Unset], data)

        li_category = _parse_li_category(d.pop("li_category", UNSET))


        def _parse_li_job_posts_stats(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                li_job_posts_stats_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0.from_dict(data)



                return li_job_posts_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0', None, Unset], data)

        li_job_posts_stats = _parse_li_job_posts_stats(d.pop("li_job_posts_stats", UNSET))


        def _parse_li_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        li_description = _parse_li_description(d.pop("li_description", UNSET))


        def _parse_li_follower_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        li_follower_count = _parse_li_follower_count(d.pop("li_follower_count", UNSET))


        def _parse_li_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        li_headline = _parse_li_headline(d.pop("li_headline", UNSET))


        def _parse_li_industries(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                li_industries_type_0 = []
                _li_industries_type_0 = data
                for li_industries_type_0_item_data in (_li_industries_type_0):
                    li_industries_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item.from_dict(li_industries_type_0_item_data)



                    li_industries_type_0.append(li_industries_type_0_item)

                return li_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiIndustriesType0Item']], data)

        li_industries = _parse_li_industries(d.pop("li_industries", UNSET))


        def _parse_li_locations(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                li_locations_type_0 = []
                _li_locations_type_0 = data
                for li_locations_type_0_item_data in (_li_locations_type_0):
                    li_locations_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item.from_dict(li_locations_type_0_item_data)



                    li_locations_type_0.append(li_locations_type_0_item)

                return li_locations_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiLocationsType0Item']], data)

        li_locations = _parse_li_locations(d.pop("li_locations", UNSET))


        def _parse_li_specialties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                li_specialties_type_0 = cast(list[str], data)

                return li_specialties_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        li_specialties = _parse_li_specialties(d.pop("li_specialties", UNSET))


        def _parse_location_consensus(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_consensus_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0.from_dict(data)



                return location_consensus_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLocationConsensusType0', None, Unset], data)

        location_consensus = _parse_location_consensus(d.pop("location_consensus", UNSET))


        def _parse_market_cap_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        market_cap_usd = _parse_market_cap_usd(d.pop("market_cap_usd", UNSET))


        def _parse_naics_codes(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                naics_codes_type_0 = cast(list[str], data)

                return naics_codes_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        naics_codes = _parse_naics_codes(d.pop("naics_codes", UNSET))


        def _parse_names(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                names_type_0 = cast(list[str], data)

                return names_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        names = _parse_names(d.pop("names", UNSET))


        def _parse_preferred_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))


        def _parse_revenue_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        revenue_usd = _parse_revenue_usd(d.pop("revenue_usd", UNSET))


        def _parse_standard_industries(data: object) -> Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standard_industries_type_0 = []
                _standard_industries_type_0 = data
                for standard_industries_type_0_item_data in (_standard_industries_type_0):
                    standard_industries_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item(standard_industries_type_0_item_data)



                    standard_industries_type_0.append(standard_industries_type_0_item)

                return standard_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStandardIndustriesType0Item]], data)

        standard_industries = _parse_standard_industries(d.pop("standard_industries", UNSET))


        def _parse_status_consensus(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_consensus = _parse_status_consensus(d.pop("status_consensus", UNSET))


        def _parse_stock_info_consensus(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stock_info_consensus_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0.from_dict(data)



                return stock_info_consensus_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemStockInfoConsensusType0', None, Unset], data)

        stock_info_consensus = _parse_stock_info_consensus(d.pop("stock_info_consensus", UNSET))


        def _parse_tags(data: object) -> Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemTagsType0Item]], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_total_funding_consensus(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_funding_consensus = _parse_total_funding_consensus(d.pop("total_funding_consensus", UNSET))


        def _parse_twitter_handles(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                twitter_handles_type_0 = cast(list[str], data)

                return twitter_handles_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        twitter_handles = _parse_twitter_handles(d.pop("twitter_handles", UNSET))


        def _parse_websites(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                websites_type_0 = cast(list[str], data)

                return websites_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        websites = _parse_websites(d.pop("websites", UNSET))


        def _parse_wellfound_slugs(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                wellfound_slugs_type_0 = cast(list[str], data)

                return wellfound_slugs_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        wellfound_slugs = _parse_wellfound_slugs(d.pop("wellfound_slugs", UNSET))


        def _parse_youtube_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                youtube_urls_type_0 = cast(list[str], data)

                return youtube_urls_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        youtube_urls = _parse_youtube_urls(d.pop("youtube_urls", UNSET))


        def _parse_role_count_matches(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_count_matches_type_0 = []
                _role_count_matches_type_0 = data
                for role_count_matches_type_0_item_data in (_role_count_matches_type_0):
                    role_count_matches_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item.from_dict(role_count_matches_type_0_item_data)



                    role_count_matches_type_0.append(role_count_matches_type_0_item)

                return role_count_matches_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item']], data)

        role_count_matches = _parse_role_count_matches(d.pop("role_count_matches", UNSET))


        def _parse_num_matching_locations(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_locations_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0.from_dict(data)



                return num_matching_locations_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0', None, Unset], data)

        num_matching_locations = _parse_num_matching_locations(d.pop("num_matching_locations", UNSET))


        def _parse_linkedin_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_ids_type_0 = cast(list[str], data)

                return linkedin_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        linkedin_ids = _parse_linkedin_ids(d.pop("linkedin_ids", UNSET))


        def _parse_last_sort_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_sort_key = _parse_last_sort_key(d.pop("last_sort_key", UNSET))


        def _parse_relevance_score(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        relevance_score = _parse_relevance_score(d.pop("relevance_score", UNSET))


        def _parse_num_li_locations(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_li_locations = _parse_num_li_locations(d.pop("num_li_locations", UNSET))


        def _parse_location_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))


        def _parse_crunchbase_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        crunchbase_slug = _parse_crunchbase_slug(d.pop("crunchbase_slug", UNSET))


        def _parse_crunchbase_rank(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crunchbase_rank = _parse_crunchbase_rank(d.pop("crunchbase_rank", UNSET))


        def _parse_primary_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_role = _parse_primary_role(d.pop("primary_role", UNSET))


        def _parse_roles(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = cast(list[str], data)

                return roles_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        roles = _parse_roles(d.pop("roles", UNSET))


        def _parse_short_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))


        def _parse_long_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        long_description = _parse_long_description(d.pop("long_description", UNSET))


        def _parse_crunchbase_category_groups(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crunchbase_category_groups_type_0 = cast(list[str], data)

                return crunchbase_category_groups_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        crunchbase_category_groups = _parse_crunchbase_category_groups(d.pop("crunchbase_category_groups", UNSET))


        def _parse_crunchbase_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crunchbase_categories_type_0 = cast(list[str], data)

                return crunchbase_categories_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        crunchbase_categories = _parse_crunchbase_categories(d.pop("crunchbase_categories", UNSET))


        def _parse_is_subsidiary(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_subsidiary = _parse_is_subsidiary(d.pop("is_subsidiary", UNSET))


        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))


        def _parse_num_funding_rounds(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_funding_rounds = _parse_num_funding_rounds(d.pop("num_funding_rounds", UNSET))


        def _parse_funding_rounds(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_rounds_type_0 = []
                _funding_rounds_type_0 = data
                for funding_rounds_type_0_item_data in (_funding_rounds_type_0):
                    funding_rounds_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item.from_dict(funding_rounds_type_0_item_data)



                    funding_rounds_type_0.append(funding_rounds_type_0_item)

                return funding_rounds_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundsType0Item']], data)

        funding_rounds = _parse_funding_rounds(d.pop("funding_rounds", UNSET))


        def _parse_num_exits(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_exits = _parse_num_exits(d.pop("num_exits", UNSET))


        def _parse_investors(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investors_type_0 = []
                _investors_type_0 = data
                for investors_type_0_item_data in (_investors_type_0):
                    investors_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item.from_dict(investors_type_0_item_data)



                    investors_type_0.append(investors_type_0_item)

                return investors_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestorsType0Item']], data)

        investors = _parse_investors(d.pop("investors", UNSET))


        def _parse_acquisitions(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                acquisitions_type_0 = []
                _acquisitions_type_0 = data
                for acquisitions_type_0_item_data in (_acquisitions_type_0):
                    acquisitions_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item.from_dict(acquisitions_type_0_item_data)



                    acquisitions_type_0.append(acquisitions_type_0_item)

                return acquisitions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcquisitionsType0Item']], data)

        acquisitions = _parse_acquisitions(d.pop("acquisitions", UNSET))


        def _parse_best_funding_round(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                best_funding_round_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0.from_dict(data)



                return best_funding_round_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemBestFundingRoundType0', None, Unset], data)

        best_funding_round = _parse_best_funding_round(d.pop("best_funding_round", UNSET))


        def _parse_funding_stage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        funding_stage = _parse_funding_stage(d.pop("funding_stage", UNSET))


        def _parse_alt_industries(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alt_industries_type_0 = cast(list[str], data)

                return alt_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        alt_industries = _parse_alt_industries(d.pop("alt_industries", UNSET))


        def _parse_alt_keywords(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alt_keywords_type_0 = cast(list[str], data)

                return alt_keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        alt_keywords = _parse_alt_keywords(d.pop("alt_keywords", UNSET))


        def _parse_alt_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alt_description = _parse_alt_description(d.pop("alt_description", UNSET))


        def _parse_employee_trends(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employee_trends_type_0 = []
                _employee_trends_type_0 = data
                for employee_trends_type_0_item_data in (_employee_trends_type_0):
                    employee_trends_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item.from_dict(employee_trends_type_0_item_data)



                    employee_trends_type_0.append(employee_trends_type_0_item)

                return employee_trends_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item']], data)

        employee_trends = _parse_employee_trends(d.pop("employee_trends", UNSET))


        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_similar_companies(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                similar_companies_type_0 = []
                _similar_companies_type_0 = data
                for similar_companies_type_0_item_data in (_similar_companies_type_0):
                    similar_companies_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item.from_dict(similar_companies_type_0_item_data)



                    similar_companies_type_0.append(similar_companies_type_0_item)

                return similar_companies_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item']], data)

        similar_companies = _parse_similar_companies(d.pop("similar_companies", UNSET))


        def _parse_full_funding_rounds(data: object) -> Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                full_funding_rounds_type_0 = []
                _full_funding_rounds_type_0 = data
                for full_funding_rounds_type_0_item_data in (_full_funding_rounds_type_0):
                    full_funding_rounds_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item.from_dict(full_funding_rounds_type_0_item_data)



                    full_funding_rounds_type_0.append(full_funding_rounds_type_0_item)

                return full_funding_rounds_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0Item']], data)

        full_funding_rounds = _parse_full_funding_rounds(d.pop("full_funding_rounds", UNSET))


        def _parse_funding_round_stats(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                funding_round_stats_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0.from_dict(data)



                return funding_round_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFundingRoundStatsType0', None, Unset], data)

        funding_round_stats = _parse_funding_round_stats(d.pop("funding_round_stats", UNSET))


        def _parse_investment_stats(data: object) -> Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investment_stats_type_0 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0.from_dict(data)



                return investment_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0', None, Unset], data)

        investment_stats = _parse_investment_stats(d.pop("investment_stats", UNSET))


        def _parse_is_investor(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_investor = _parse_is_investor(d.pop("is_investor", UNSET))


        def _parse_investor_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        investor_type = _parse_investor_type(d.pop("investor_type", UNSET))


        def _parse_investor_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_categories_type_0 = cast(list[str], data)

                return investor_categories_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        investor_categories = _parse_investor_categories(d.pop("investor_categories", UNSET))


        get_current_companies_in_saved_search_response_200_output_companies_item = cls(
            linkedin_id=linkedin_id,
            accelerator_statuses=accelerator_statuses,
            accelerators=accelerators,
            blog_urls=blog_urls,
            custom_data=custom_data,
            domains=domains,
            emails=emails,
            phone_numbers=phone_numbers,
            employee_count_consensus=employee_count_consensus,
            facebook_urls=facebook_urls,
            fortune_rankings=fortune_rankings,
            founded_on_consensus=founded_on_consensus,
            github_usernames=github_usernames,
            instagram_handles=instagram_handles,
            latest_funding_consensus=latest_funding_consensus,
            linkedin_slugs=linkedin_slugs,
            linkedin_primary_slug=linkedin_primary_slug,
            li_org_id=li_org_id,
            li_category=li_category,
            li_job_posts_stats=li_job_posts_stats,
            li_description=li_description,
            li_follower_count=li_follower_count,
            li_headline=li_headline,
            li_industries=li_industries,
            li_locations=li_locations,
            li_specialties=li_specialties,
            location_consensus=location_consensus,
            market_cap_usd=market_cap_usd,
            naics_codes=naics_codes,
            names=names,
            preferred_name=preferred_name,
            revenue_usd=revenue_usd,
            standard_industries=standard_industries,
            status_consensus=status_consensus,
            stock_info_consensus=stock_info_consensus,
            tags=tags,
            total_funding_consensus=total_funding_consensus,
            twitter_handles=twitter_handles,
            websites=websites,
            wellfound_slugs=wellfound_slugs,
            youtube_urls=youtube_urls,
            role_count_matches=role_count_matches,
            num_matching_locations=num_matching_locations,
            linkedin_ids=linkedin_ids,
            last_sort_key=last_sort_key,
            relevance_score=relevance_score,
            num_li_locations=num_li_locations,
            location_name=location_name,
            crunchbase_slug=crunchbase_slug,
            crunchbase_rank=crunchbase_rank,
            primary_role=primary_role,
            roles=roles,
            short_description=short_description,
            long_description=long_description,
            crunchbase_category_groups=crunchbase_category_groups,
            crunchbase_categories=crunchbase_categories,
            is_subsidiary=is_subsidiary,
            parent=parent,
            num_funding_rounds=num_funding_rounds,
            funding_rounds=funding_rounds,
            num_exits=num_exits,
            investors=investors,
            acquisitions=acquisitions,
            best_funding_round=best_funding_round,
            funding_stage=funding_stage,
            alt_industries=alt_industries,
            alt_keywords=alt_keywords,
            alt_description=alt_description,
            employee_trends=employee_trends,
            logo_url=logo_url,
            similar_companies=similar_companies,
            full_funding_rounds=full_funding_rounds,
            funding_round_stats=funding_round_stats,
            investment_stats=investment_stats,
            is_investor=is_investor,
            investor_type=investor_type,
            investor_categories=investor_categories,
        )


        get_current_companies_in_saved_search_response_200_output_companies_item.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item

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
