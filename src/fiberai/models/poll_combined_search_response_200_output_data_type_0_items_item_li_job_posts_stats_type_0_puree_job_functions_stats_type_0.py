from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_accounting import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_administrative import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_advertising import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_analyst import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_art_creative import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_arts_and_design import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_business_development import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_community_social_services import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_consulting import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_customer_service import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_design import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_distribution import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_education import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_engineering import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_entrepreneurship import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_finance import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_general_business import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_health_care_provider import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_healthcare_services import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_human_resources import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_information_technology import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_legal import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_management import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_manufacturing import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_marketing import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_military_protective_services import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_operations import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_other import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_product_management import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_production import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_program_product_management import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_project_management import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_public_relations import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_purchasing import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_quality_assurance import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_real_estate import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_research import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_sales import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_science import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_strategy_planning import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_supply_chain import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_support import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_training import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_writing_editing import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing,
    )


T = TypeVar(
    "T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0"
)


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0:
    """
    Attributes:
        arts_and_design (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStats
            Type0ArtsAndDesign | Unset):
        business_development (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctions
            StatsType0BusinessDevelopment | Unset):
        community_social_services (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunc
            tionsStatsType0CommunitySocialServices | Unset):
        consulting
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting
            | Unset):
        education
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education |
            Unset):
        engineering
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
            | Unset):
        entrepreneurship (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStat
            sType0Entrepreneurship | Unset):
        healthcare_services (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsS
            tatsType0HealthcareServices | Unset):
        human_resources (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStats
            Type0HumanResources | Unset):
        information_technology (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctio
            nsStatsType0InformationTechnology | Unset):
        legal (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
            | Unset):
        military_protective_services (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobF
            unctionsStatsType0MilitaryProtectiveServices | Unset):
        operations
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
            | Unset):
        program_product_management (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFun
            ctionsStatsType0ProgramProductManagement | Unset):
        real_estate
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
            | Unset):
        sales (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
            | Unset):
        support
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support |
            Unset):
        administrative (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsT
            ype0Administrative | Unset):
        finance
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance |
            Unset):
        marketing
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing |
            Unset):
        purchasing
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
            | Unset):
        product_management (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsSt
            atsType0ProductManagement | Unset):
        advertising
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
            | Unset):
        analyst
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst |
            Unset):
        customer_service (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStat
            sType0CustomerService | Unset):
        distribution (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsTyp
            e0Distribution | Unset):
        design
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design |
            Unset):
        general_business (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStat
            sType0GeneralBusiness | Unset):
        management
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
            | Unset):
        manufacturing (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsTy
            pe0Manufacturing | Unset):
        other (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
            | Unset):
        public_relations (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStat
            sType0PublicRelations | Unset):
        project_management (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsSt
            atsType0ProjectManagement | Unset):
        production
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
            | Unset):
        quality_assurance (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsSta
            tsType0QualityAssurance | Unset):
        research
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research |
            Unset):
        science
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science |
            Unset):
        supply_chain
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
            | Unset):
        training
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training |
            Unset):
        health_care_provider (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctions
            StatsType0HealthCareProvider | Unset):
        accounting
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
            | Unset):
        art_creative
            (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
            | Unset):
        strategy_planning (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsSta
            tsType0StrategyPlanning | Unset):
        writing_editing (PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStats
            Type0WritingEditing | Unset):
    """

    arts_and_design: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign
        | Unset
    ) = UNSET
    business_development: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment
        | Unset
    ) = UNSET
    community_social_services: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices
        | Unset
    ) = UNSET
    consulting: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting
        | Unset
    ) = UNSET
    education: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education
        | Unset
    ) = UNSET
    engineering: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
        | Unset
    ) = UNSET
    entrepreneurship: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship
        | Unset
    ) = UNSET
    healthcare_services: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices
        | Unset
    ) = UNSET
    human_resources: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources
        | Unset
    ) = UNSET
    information_technology: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology
        | Unset
    ) = UNSET
    legal: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
        | Unset
    ) = UNSET
    military_protective_services: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices
        | Unset
    ) = UNSET
    operations: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
        | Unset
    ) = UNSET
    program_product_management: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement
        | Unset
    ) = UNSET
    real_estate: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
        | Unset
    ) = UNSET
    sales: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
        | Unset
    ) = UNSET
    support: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support
        | Unset
    ) = UNSET
    administrative: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative
        | Unset
    ) = UNSET
    finance: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance
        | Unset
    ) = UNSET
    marketing: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing
        | Unset
    ) = UNSET
    purchasing: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
        | Unset
    ) = UNSET
    product_management: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement
        | Unset
    ) = UNSET
    advertising: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
        | Unset
    ) = UNSET
    analyst: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst
        | Unset
    ) = UNSET
    customer_service: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService
        | Unset
    ) = UNSET
    distribution: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution
        | Unset
    ) = UNSET
    design: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design
        | Unset
    ) = UNSET
    general_business: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness
        | Unset
    ) = UNSET
    management: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
        | Unset
    ) = UNSET
    manufacturing: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing
        | Unset
    ) = UNSET
    other: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
        | Unset
    ) = UNSET
    public_relations: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations
        | Unset
    ) = UNSET
    project_management: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement
        | Unset
    ) = UNSET
    production: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
        | Unset
    ) = UNSET
    quality_assurance: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance
        | Unset
    ) = UNSET
    research: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research
        | Unset
    ) = UNSET
    science: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science
        | Unset
    ) = UNSET
    supply_chain: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
        | Unset
    ) = UNSET
    training: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training
        | Unset
    ) = UNSET
    health_care_provider: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider
        | Unset
    ) = UNSET
    accounting: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
        | Unset
    ) = UNSET
    art_creative: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
        | Unset
    ) = UNSET
    strategy_planning: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning
        | Unset
    ) = UNSET
    writing_editing: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        arts_and_design: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arts_and_design, Unset):
            arts_and_design = self.arts_and_design.to_dict()

        business_development: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_development, Unset):
            business_development = self.business_development.to_dict()

        community_social_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.community_social_services, Unset):
            community_social_services = self.community_social_services.to_dict()

        consulting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consulting, Unset):
            consulting = self.consulting.to_dict()

        education: dict[str, Any] | Unset = UNSET
        if not isinstance(self.education, Unset):
            education = self.education.to_dict()

        engineering: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engineering, Unset):
            engineering = self.engineering.to_dict()

        entrepreneurship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrepreneurship, Unset):
            entrepreneurship = self.entrepreneurship.to_dict()

        healthcare_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.healthcare_services, Unset):
            healthcare_services = self.healthcare_services.to_dict()

        human_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.human_resources, Unset):
            human_resources = self.human_resources.to_dict()

        information_technology: dict[str, Any] | Unset = UNSET
        if not isinstance(self.information_technology, Unset):
            information_technology = self.information_technology.to_dict()

        legal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        military_protective_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.military_protective_services, Unset):
            military_protective_services = self.military_protective_services.to_dict()

        operations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations.to_dict()

        program_product_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.program_product_management, Unset):
            program_product_management = self.program_product_management.to_dict()

        real_estate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real_estate, Unset):
            real_estate = self.real_estate.to_dict()

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        support: dict[str, Any] | Unset = UNSET
        if not isinstance(self.support, Unset):
            support = self.support.to_dict()

        administrative: dict[str, Any] | Unset = UNSET
        if not isinstance(self.administrative, Unset):
            administrative = self.administrative.to_dict()

        finance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        marketing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marketing, Unset):
            marketing = self.marketing.to_dict()

        purchasing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purchasing, Unset):
            purchasing = self.purchasing.to_dict()

        product_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_management, Unset):
            product_management = self.product_management.to_dict()

        advertising: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advertising, Unset):
            advertising = self.advertising.to_dict()

        analyst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analyst, Unset):
            analyst = self.analyst.to_dict()

        customer_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer_service, Unset):
            customer_service = self.customer_service.to_dict()

        distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        design: dict[str, Any] | Unset = UNSET
        if not isinstance(self.design, Unset):
            design = self.design.to_dict()

        general_business: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general_business, Unset):
            general_business = self.general_business.to_dict()

        management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.management, Unset):
            management = self.management.to_dict()

        manufacturing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturing, Unset):
            manufacturing = self.manufacturing.to_dict()

        other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        public_relations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_relations, Unset):
            public_relations = self.public_relations.to_dict()

        project_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_management, Unset):
            project_management = self.project_management.to_dict()

        production: dict[str, Any] | Unset = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        quality_assurance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quality_assurance, Unset):
            quality_assurance = self.quality_assurance.to_dict()

        research: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research, Unset):
            research = self.research.to_dict()

        science: dict[str, Any] | Unset = UNSET
        if not isinstance(self.science, Unset):
            science = self.science.to_dict()

        supply_chain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supply_chain, Unset):
            supply_chain = self.supply_chain.to_dict()

        training: dict[str, Any] | Unset = UNSET
        if not isinstance(self.training, Unset):
            training = self.training.to_dict()

        health_care_provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_care_provider, Unset):
            health_care_provider = self.health_care_provider.to_dict()

        accounting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = self.accounting.to_dict()

        art_creative: dict[str, Any] | Unset = UNSET
        if not isinstance(self.art_creative, Unset):
            art_creative = self.art_creative.to_dict()

        strategy_planning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_planning, Unset):
            strategy_planning = self.strategy_planning.to_dict()

        writing_editing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.writing_editing, Unset):
            writing_editing = self.writing_editing.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if arts_and_design is not UNSET:
            field_dict["Arts and Design"] = arts_and_design
        if business_development is not UNSET:
            field_dict["Business Development"] = business_development
        if community_social_services is not UNSET:
            field_dict["Community & Social Services"] = community_social_services
        if consulting is not UNSET:
            field_dict["Consulting"] = consulting
        if education is not UNSET:
            field_dict["Education"] = education
        if engineering is not UNSET:
            field_dict["Engineering"] = engineering
        if entrepreneurship is not UNSET:
            field_dict["Entrepreneurship"] = entrepreneurship
        if healthcare_services is not UNSET:
            field_dict["Healthcare Services"] = healthcare_services
        if human_resources is not UNSET:
            field_dict["Human Resources"] = human_resources
        if information_technology is not UNSET:
            field_dict["Information Technology"] = information_technology
        if legal is not UNSET:
            field_dict["Legal"] = legal
        if military_protective_services is not UNSET:
            field_dict["Military & Protective Services"] = military_protective_services
        if operations is not UNSET:
            field_dict["Operations"] = operations
        if program_product_management is not UNSET:
            field_dict["Program & Product Management"] = program_product_management
        if real_estate is not UNSET:
            field_dict["Real Estate"] = real_estate
        if sales is not UNSET:
            field_dict["Sales"] = sales
        if support is not UNSET:
            field_dict["Support"] = support
        if administrative is not UNSET:
            field_dict["Administrative"] = administrative
        if finance is not UNSET:
            field_dict["Finance"] = finance
        if marketing is not UNSET:
            field_dict["Marketing"] = marketing
        if purchasing is not UNSET:
            field_dict["Purchasing"] = purchasing
        if product_management is not UNSET:
            field_dict["Product Management"] = product_management
        if advertising is not UNSET:
            field_dict["Advertising"] = advertising
        if analyst is not UNSET:
            field_dict["Analyst"] = analyst
        if customer_service is not UNSET:
            field_dict["Customer Service"] = customer_service
        if distribution is not UNSET:
            field_dict["Distribution"] = distribution
        if design is not UNSET:
            field_dict["Design"] = design
        if general_business is not UNSET:
            field_dict["General Business"] = general_business
        if management is not UNSET:
            field_dict["Management"] = management
        if manufacturing is not UNSET:
            field_dict["Manufacturing"] = manufacturing
        if other is not UNSET:
            field_dict["Other"] = other
        if public_relations is not UNSET:
            field_dict["Public Relations"] = public_relations
        if project_management is not UNSET:
            field_dict["Project Management"] = project_management
        if production is not UNSET:
            field_dict["Production"] = production
        if quality_assurance is not UNSET:
            field_dict["Quality Assurance"] = quality_assurance
        if research is not UNSET:
            field_dict["Research"] = research
        if science is not UNSET:
            field_dict["Science"] = science
        if supply_chain is not UNSET:
            field_dict["Supply Chain"] = supply_chain
        if training is not UNSET:
            field_dict["Training"] = training
        if health_care_provider is not UNSET:
            field_dict["Health Care Provider"] = health_care_provider
        if accounting is not UNSET:
            field_dict["Accounting"] = accounting
        if art_creative is not UNSET:
            field_dict["Art / Creative"] = art_creative
        if strategy_planning is not UNSET:
            field_dict["Strategy / Planning"] = strategy_planning
        if writing_editing is not UNSET:
            field_dict["Writing / Editing"] = writing_editing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_accounting import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_administrative import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_advertising import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_analyst import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_art_creative import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_arts_and_design import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_business_development import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_community_social_services import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_consulting import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_customer_service import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_design import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_distribution import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_education import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_engineering import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_entrepreneurship import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_finance import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_general_business import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_health_care_provider import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_healthcare_services import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_human_resources import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_information_technology import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_legal import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_management import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_manufacturing import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_marketing import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_military_protective_services import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_operations import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_other import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_product_management import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_production import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_program_product_management import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_project_management import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_public_relations import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_purchasing import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_quality_assurance import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_real_estate import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_research import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_sales import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_science import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_strategy_planning import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_supply_chain import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_support import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_training import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_writing_editing import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing,
        )

        d = dict(src_dict)
        _arts_and_design = d.pop("Arts and Design", UNSET)
        arts_and_design: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign
            | Unset
        )
        if isinstance(_arts_and_design, Unset):
            arts_and_design = UNSET
        else:
            arts_and_design = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign.from_dict(
                _arts_and_design
            )

        _business_development = d.pop("Business Development", UNSET)
        business_development: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment
            | Unset
        )
        if isinstance(_business_development, Unset):
            business_development = UNSET
        else:
            business_development = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment.from_dict(
                _business_development
            )

        _community_social_services = d.pop("Community & Social Services", UNSET)
        community_social_services: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices
            | Unset
        )
        if isinstance(_community_social_services, Unset):
            community_social_services = UNSET
        else:
            community_social_services = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices.from_dict(
                _community_social_services
            )

        _consulting = d.pop("Consulting", UNSET)
        consulting: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting
            | Unset
        )
        if isinstance(_consulting, Unset):
            consulting = UNSET
        else:
            consulting = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting.from_dict(
                _consulting
            )

        _education = d.pop("Education", UNSET)
        education: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education
            | Unset
        )
        if isinstance(_education, Unset):
            education = UNSET
        else:
            education = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education.from_dict(
                _education
            )

        _engineering = d.pop("Engineering", UNSET)
        engineering: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
            | Unset
        )
        if isinstance(_engineering, Unset):
            engineering = UNSET
        else:
            engineering = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering.from_dict(
                _engineering
            )

        _entrepreneurship = d.pop("Entrepreneurship", UNSET)
        entrepreneurship: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship
            | Unset
        )
        if isinstance(_entrepreneurship, Unset):
            entrepreneurship = UNSET
        else:
            entrepreneurship = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship.from_dict(
                _entrepreneurship
            )

        _healthcare_services = d.pop("Healthcare Services", UNSET)
        healthcare_services: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices
            | Unset
        )
        if isinstance(_healthcare_services, Unset):
            healthcare_services = UNSET
        else:
            healthcare_services = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices.from_dict(
                _healthcare_services
            )

        _human_resources = d.pop("Human Resources", UNSET)
        human_resources: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources
            | Unset
        )
        if isinstance(_human_resources, Unset):
            human_resources = UNSET
        else:
            human_resources = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources.from_dict(
                _human_resources
            )

        _information_technology = d.pop("Information Technology", UNSET)
        information_technology: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology
            | Unset
        )
        if isinstance(_information_technology, Unset):
            information_technology = UNSET
        else:
            information_technology = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology.from_dict(
                _information_technology
            )

        _legal = d.pop("Legal", UNSET)
        legal: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
            | Unset
        )
        if isinstance(_legal, Unset):
            legal = UNSET
        else:
            legal = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal.from_dict(
                _legal
            )

        _military_protective_services = d.pop("Military & Protective Services", UNSET)
        military_protective_services: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices
            | Unset
        )
        if isinstance(_military_protective_services, Unset):
            military_protective_services = UNSET
        else:
            military_protective_services = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices.from_dict(
                _military_protective_services
            )

        _operations = d.pop("Operations", UNSET)
        operations: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
            | Unset
        )
        if isinstance(_operations, Unset):
            operations = UNSET
        else:
            operations = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations.from_dict(
                _operations
            )

        _program_product_management = d.pop("Program & Product Management", UNSET)
        program_product_management: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement
            | Unset
        )
        if isinstance(_program_product_management, Unset):
            program_product_management = UNSET
        else:
            program_product_management = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement.from_dict(
                _program_product_management
            )

        _real_estate = d.pop("Real Estate", UNSET)
        real_estate: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
            | Unset
        )
        if isinstance(_real_estate, Unset):
            real_estate = UNSET
        else:
            real_estate = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate.from_dict(
                _real_estate
            )

        _sales = d.pop("Sales", UNSET)
        sales: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
            | Unset
        )
        if isinstance(_sales, Unset):
            sales = UNSET
        else:
            sales = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales.from_dict(
                _sales
            )

        _support = d.pop("Support", UNSET)
        support: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support
            | Unset
        )
        if isinstance(_support, Unset):
            support = UNSET
        else:
            support = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support.from_dict(
                _support
            )

        _administrative = d.pop("Administrative", UNSET)
        administrative: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative
            | Unset
        )
        if isinstance(_administrative, Unset):
            administrative = UNSET
        else:
            administrative = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative.from_dict(
                _administrative
            )

        _finance = d.pop("Finance", UNSET)
        finance: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance
            | Unset
        )
        if isinstance(_finance, Unset):
            finance = UNSET
        else:
            finance = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance.from_dict(
                _finance
            )

        _marketing = d.pop("Marketing", UNSET)
        marketing: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing
            | Unset
        )
        if isinstance(_marketing, Unset):
            marketing = UNSET
        else:
            marketing = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing.from_dict(
                _marketing
            )

        _purchasing = d.pop("Purchasing", UNSET)
        purchasing: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
            | Unset
        )
        if isinstance(_purchasing, Unset):
            purchasing = UNSET
        else:
            purchasing = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing.from_dict(
                _purchasing
            )

        _product_management = d.pop("Product Management", UNSET)
        product_management: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement
            | Unset
        )
        if isinstance(_product_management, Unset):
            product_management = UNSET
        else:
            product_management = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement.from_dict(
                _product_management
            )

        _advertising = d.pop("Advertising", UNSET)
        advertising: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
            | Unset
        )
        if isinstance(_advertising, Unset):
            advertising = UNSET
        else:
            advertising = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising.from_dict(
                _advertising
            )

        _analyst = d.pop("Analyst", UNSET)
        analyst: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst
            | Unset
        )
        if isinstance(_analyst, Unset):
            analyst = UNSET
        else:
            analyst = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst.from_dict(
                _analyst
            )

        _customer_service = d.pop("Customer Service", UNSET)
        customer_service: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService
            | Unset
        )
        if isinstance(_customer_service, Unset):
            customer_service = UNSET
        else:
            customer_service = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService.from_dict(
                _customer_service
            )

        _distribution = d.pop("Distribution", UNSET)
        distribution: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution
            | Unset
        )
        if isinstance(_distribution, Unset):
            distribution = UNSET
        else:
            distribution = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution.from_dict(
                _distribution
            )

        _design = d.pop("Design", UNSET)
        design: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design
            | Unset
        )
        if isinstance(_design, Unset):
            design = UNSET
        else:
            design = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design.from_dict(
                _design
            )

        _general_business = d.pop("General Business", UNSET)
        general_business: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness
            | Unset
        )
        if isinstance(_general_business, Unset):
            general_business = UNSET
        else:
            general_business = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness.from_dict(
                _general_business
            )

        _management = d.pop("Management", UNSET)
        management: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
            | Unset
        )
        if isinstance(_management, Unset):
            management = UNSET
        else:
            management = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management.from_dict(
                _management
            )

        _manufacturing = d.pop("Manufacturing", UNSET)
        manufacturing: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing
            | Unset
        )
        if isinstance(_manufacturing, Unset):
            manufacturing = UNSET
        else:
            manufacturing = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing.from_dict(
                _manufacturing
            )

        _other = d.pop("Other", UNSET)
        other: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
            | Unset
        )
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other.from_dict(
                _other
            )

        _public_relations = d.pop("Public Relations", UNSET)
        public_relations: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations
            | Unset
        )
        if isinstance(_public_relations, Unset):
            public_relations = UNSET
        else:
            public_relations = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations.from_dict(
                _public_relations
            )

        _project_management = d.pop("Project Management", UNSET)
        project_management: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement
            | Unset
        )
        if isinstance(_project_management, Unset):
            project_management = UNSET
        else:
            project_management = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement.from_dict(
                _project_management
            )

        _production = d.pop("Production", UNSET)
        production: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
            | Unset
        )
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production.from_dict(
                _production
            )

        _quality_assurance = d.pop("Quality Assurance", UNSET)
        quality_assurance: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance
            | Unset
        )
        if isinstance(_quality_assurance, Unset):
            quality_assurance = UNSET
        else:
            quality_assurance = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance.from_dict(
                _quality_assurance
            )

        _research = d.pop("Research", UNSET)
        research: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research
            | Unset
        )
        if isinstance(_research, Unset):
            research = UNSET
        else:
            research = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research.from_dict(
                _research
            )

        _science = d.pop("Science", UNSET)
        science: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science
            | Unset
        )
        if isinstance(_science, Unset):
            science = UNSET
        else:
            science = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science.from_dict(
                _science
            )

        _supply_chain = d.pop("Supply Chain", UNSET)
        supply_chain: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
            | Unset
        )
        if isinstance(_supply_chain, Unset):
            supply_chain = UNSET
        else:
            supply_chain = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain.from_dict(
                _supply_chain
            )

        _training = d.pop("Training", UNSET)
        training: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training
            | Unset
        )
        if isinstance(_training, Unset):
            training = UNSET
        else:
            training = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training.from_dict(
                _training
            )

        _health_care_provider = d.pop("Health Care Provider", UNSET)
        health_care_provider: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider
            | Unset
        )
        if isinstance(_health_care_provider, Unset):
            health_care_provider = UNSET
        else:
            health_care_provider = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider.from_dict(
                _health_care_provider
            )

        _accounting = d.pop("Accounting", UNSET)
        accounting: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
            | Unset
        )
        if isinstance(_accounting, Unset):
            accounting = UNSET
        else:
            accounting = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting.from_dict(
                _accounting
            )

        _art_creative = d.pop("Art / Creative", UNSET)
        art_creative: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
            | Unset
        )
        if isinstance(_art_creative, Unset):
            art_creative = UNSET
        else:
            art_creative = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative.from_dict(
                _art_creative
            )

        _strategy_planning = d.pop("Strategy / Planning", UNSET)
        strategy_planning: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning
            | Unset
        )
        if isinstance(_strategy_planning, Unset):
            strategy_planning = UNSET
        else:
            strategy_planning = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning.from_dict(
                _strategy_planning
            )

        _writing_editing = d.pop("Writing / Editing", UNSET)
        writing_editing: (
            PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing
            | Unset
        )
        if isinstance(_writing_editing, Unset):
            writing_editing = UNSET
        else:
            writing_editing = PollCombinedSearchResponse200OutputDataType0ItemsItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing.from_dict(
                _writing_editing
            )

        poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0 = cls(
            arts_and_design=arts_and_design,
            business_development=business_development,
            community_social_services=community_social_services,
            consulting=consulting,
            education=education,
            engineering=engineering,
            entrepreneurship=entrepreneurship,
            healthcare_services=healthcare_services,
            human_resources=human_resources,
            information_technology=information_technology,
            legal=legal,
            military_protective_services=military_protective_services,
            operations=operations,
            program_product_management=program_product_management,
            real_estate=real_estate,
            sales=sales,
            support=support,
            administrative=administrative,
            finance=finance,
            marketing=marketing,
            purchasing=purchasing,
            product_management=product_management,
            advertising=advertising,
            analyst=analyst,
            customer_service=customer_service,
            distribution=distribution,
            design=design,
            general_business=general_business,
            management=management,
            manufacturing=manufacturing,
            other=other,
            public_relations=public_relations,
            project_management=project_management,
            production=production,
            quality_assurance=quality_assurance,
            research=research,
            science=science,
            supply_chain=supply_chain,
            training=training,
            health_care_provider=health_care_provider,
            accounting=accounting,
            art_creative=art_creative,
            strategy_planning=strategy_planning,
            writing_editing=writing_editing,
        )

        return poll_combined_search_response_200_output_data_type_0_items_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0
