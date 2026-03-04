from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_real_estate import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_accounting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_purchasing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_writing_editing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_administrative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_human_resources import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_information_technology import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_sales import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_program_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_distribution import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_production import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_supply_chain import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_support import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_entrepreneurship import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_finance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_advertising import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_healthcare_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_science import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_art_creative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_marketing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_project_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_research import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_operations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_military_protective_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_other import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_customer_service import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_arts_and_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_training import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_strategy_planning import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_manufacturing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_engineering import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_legal import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_business_development import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_analyst import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_quality_assurance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_education import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_general_business import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_community_social_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_health_care_provider import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_public_relations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_consulting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting





T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0")



@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0:
    """ 
        Attributes:
            arts_and_design (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign]):
            business_development (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobF
                unctionsStatsType0BusinessDevelopment]):
            community_social_services (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Pure
                eJobFunctionsStatsType0CommunitySocialServices]):
            consulting (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting]):
            education (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education]):
            engineering (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering]):
            entrepreneurship (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunct
                ionsStatsType0Entrepreneurship]):
            healthcare_services (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFu
                nctionsStatsType0HealthcareServices]):
            human_resources (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources]):
            information_technology (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJo
                bFunctionsStatsType0InformationTechnology]):
            legal (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal]):
            military_protective_services (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0P
                ureeJobFunctionsStatsType0MilitaryProtectiveServices]):
            operations (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations]):
            program_product_management (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Pur
                eeJobFunctionsStatsType0ProgramProductManagement]):
            real_estate (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate]):
            sales (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales]):
            support (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support]):
            administrative (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative]):
            finance (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance]):
            marketing (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing]):
            purchasing (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing]):
            product_management (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFun
                ctionsStatsType0ProductManagement]):
            advertising (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising]):
            analyst (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst]):
            customer_service (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunct
                ionsStatsType0CustomerService]):
            distribution (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution]):
            design (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design]):
            general_business (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunct
                ionsStatsType0GeneralBusiness]):
            management (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management]):
            manufacturing (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing]):
            other (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other]):
            public_relations (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunct
                ionsStatsType0PublicRelations]):
            project_management (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFun
                ctionsStatsType0ProjectManagement]):
            production (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production]):
            quality_assurance (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunc
                tionsStatsType0QualityAssurance]):
            research (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research]):
            science (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science]):
            supply_chain (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain]):
            training (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training]):
            health_care_provider (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobF
                unctionsStatsType0HealthCareProvider]):
            accounting (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting]):
            art_creative (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative]):
            strategy_planning (Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunc
                tionsStatsType0StrategyPlanning]):
            writing_editing (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing]):
     """

    arts_and_design: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign'] = UNSET
    business_development: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment'] = UNSET
    community_social_services: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices'] = UNSET
    consulting: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting'] = UNSET
    education: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education'] = UNSET
    engineering: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering'] = UNSET
    entrepreneurship: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship'] = UNSET
    healthcare_services: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices'] = UNSET
    human_resources: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources'] = UNSET
    information_technology: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology'] = UNSET
    legal: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal'] = UNSET
    military_protective_services: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices'] = UNSET
    operations: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations'] = UNSET
    program_product_management: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement'] = UNSET
    real_estate: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate'] = UNSET
    sales: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales'] = UNSET
    support: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support'] = UNSET
    administrative: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative'] = UNSET
    finance: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance'] = UNSET
    marketing: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing'] = UNSET
    purchasing: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing'] = UNSET
    product_management: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement'] = UNSET
    advertising: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising'] = UNSET
    analyst: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst'] = UNSET
    customer_service: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService'] = UNSET
    distribution: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution'] = UNSET
    design: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design'] = UNSET
    general_business: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness'] = UNSET
    management: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management'] = UNSET
    manufacturing: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing'] = UNSET
    other: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other'] = UNSET
    public_relations: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations'] = UNSET
    project_management: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement'] = UNSET
    production: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production'] = UNSET
    quality_assurance: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance'] = UNSET
    research: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research'] = UNSET
    science: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science'] = UNSET
    supply_chain: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain'] = UNSET
    training: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training'] = UNSET
    health_care_provider: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider'] = UNSET
    accounting: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting'] = UNSET
    art_creative: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative'] = UNSET
    strategy_planning: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning'] = UNSET
    writing_editing: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing'] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_real_estate import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_accounting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_purchasing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_writing_editing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_administrative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_human_resources import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_information_technology import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_sales import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_program_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_distribution import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_production import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_supply_chain import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_support import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_entrepreneurship import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_finance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_advertising import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_healthcare_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_science import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_art_creative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_marketing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_project_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_research import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_operations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_military_protective_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_other import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_customer_service import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_arts_and_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_training import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_strategy_planning import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_manufacturing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_engineering import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_legal import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_business_development import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_analyst import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_quality_assurance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_education import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_general_business import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_community_social_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_health_care_provider import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_public_relations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_consulting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting
        arts_and_design: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.arts_and_design, Unset):
            arts_and_design = self.arts_and_design.to_dict()

        business_development: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business_development, Unset):
            business_development = self.business_development.to_dict()

        community_social_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.community_social_services, Unset):
            community_social_services = self.community_social_services.to_dict()

        consulting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.consulting, Unset):
            consulting = self.consulting.to_dict()

        education: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.education, Unset):
            education = self.education.to_dict()

        engineering: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.engineering, Unset):
            engineering = self.engineering.to_dict()

        entrepreneurship: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entrepreneurship, Unset):
            entrepreneurship = self.entrepreneurship.to_dict()

        healthcare_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.healthcare_services, Unset):
            healthcare_services = self.healthcare_services.to_dict()

        human_resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.human_resources, Unset):
            human_resources = self.human_resources.to_dict()

        information_technology: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.information_technology, Unset):
            information_technology = self.information_technology.to_dict()

        legal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        military_protective_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.military_protective_services, Unset):
            military_protective_services = self.military_protective_services.to_dict()

        operations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations.to_dict()

        program_product_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_product_management, Unset):
            program_product_management = self.program_product_management.to_dict()

        real_estate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.real_estate, Unset):
            real_estate = self.real_estate.to_dict()

        sales: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        support: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.support, Unset):
            support = self.support.to_dict()

        administrative: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.administrative, Unset):
            administrative = self.administrative.to_dict()

        finance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        marketing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.marketing, Unset):
            marketing = self.marketing.to_dict()

        purchasing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchasing, Unset):
            purchasing = self.purchasing.to_dict()

        product_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_management, Unset):
            product_management = self.product_management.to_dict()

        advertising: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advertising, Unset):
            advertising = self.advertising.to_dict()

        analyst: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analyst, Unset):
            analyst = self.analyst.to_dict()

        customer_service: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer_service, Unset):
            customer_service = self.customer_service.to_dict()

        distribution: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        design: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.design, Unset):
            design = self.design.to_dict()

        general_business: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.general_business, Unset):
            general_business = self.general_business.to_dict()

        management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.management, Unset):
            management = self.management.to_dict()

        manufacturing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.manufacturing, Unset):
            manufacturing = self.manufacturing.to_dict()

        other: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        public_relations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_relations, Unset):
            public_relations = self.public_relations.to_dict()

        project_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.project_management, Unset):
            project_management = self.project_management.to_dict()

        production: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        quality_assurance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality_assurance, Unset):
            quality_assurance = self.quality_assurance.to_dict()

        research: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.research, Unset):
            research = self.research.to_dict()

        science: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.science, Unset):
            science = self.science.to_dict()

        supply_chain: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.supply_chain, Unset):
            supply_chain = self.supply_chain.to_dict()

        training: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.training, Unset):
            training = self.training.to_dict()

        health_care_provider: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.health_care_provider, Unset):
            health_care_provider = self.health_care_provider.to_dict()

        accounting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = self.accounting.to_dict()

        art_creative: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.art_creative, Unset):
            art_creative = self.art_creative.to_dict()

        strategy_planning: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.strategy_planning, Unset):
            strategy_planning = self.strategy_planning.to_dict()

        writing_editing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.writing_editing, Unset):
            writing_editing = self.writing_editing.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_real_estate import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_accounting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_purchasing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_writing_editing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_administrative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_human_resources import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_information_technology import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_sales import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_program_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_distribution import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_production import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_supply_chain import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_support import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_entrepreneurship import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_finance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_advertising import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_healthcare_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_science import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_art_creative import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_marketing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_project_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_research import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_operations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_military_protective_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_other import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_customer_service import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_arts_and_design import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_training import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_strategy_planning import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_manufacturing import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_engineering import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_legal import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_business_development import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_analyst import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_quality_assurance import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_education import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_general_business import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_product_management import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_community_social_services import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_health_care_provider import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_public_relations import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0_consulting import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting
        d = dict(src_dict)
        _arts_and_design = d.pop("Arts and Design", UNSET)
        arts_and_design: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign]
        if isinstance(_arts_and_design,  Unset):
            arts_and_design = UNSET
        else:
            arts_and_design = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtsAndDesign.from_dict(_arts_and_design)




        _business_development = d.pop("Business Development", UNSET)
        business_development: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment]
        if isinstance(_business_development,  Unset):
            business_development = UNSET
        else:
            business_development = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0BusinessDevelopment.from_dict(_business_development)




        _community_social_services = d.pop("Community & Social Services", UNSET)
        community_social_services: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices]
        if isinstance(_community_social_services,  Unset):
            community_social_services = UNSET
        else:
            community_social_services = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CommunitySocialServices.from_dict(_community_social_services)




        _consulting = d.pop("Consulting", UNSET)
        consulting: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting]
        if isinstance(_consulting,  Unset):
            consulting = UNSET
        else:
            consulting = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Consulting.from_dict(_consulting)




        _education = d.pop("Education", UNSET)
        education: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education]
        if isinstance(_education,  Unset):
            education = UNSET
        else:
            education = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Education.from_dict(_education)




        _engineering = d.pop("Engineering", UNSET)
        engineering: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering]
        if isinstance(_engineering,  Unset):
            engineering = UNSET
        else:
            engineering = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Engineering.from_dict(_engineering)




        _entrepreneurship = d.pop("Entrepreneurship", UNSET)
        entrepreneurship: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship]
        if isinstance(_entrepreneurship,  Unset):
            entrepreneurship = UNSET
        else:
            entrepreneurship = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Entrepreneurship.from_dict(_entrepreneurship)




        _healthcare_services = d.pop("Healthcare Services", UNSET)
        healthcare_services: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices]
        if isinstance(_healthcare_services,  Unset):
            healthcare_services = UNSET
        else:
            healthcare_services = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthcareServices.from_dict(_healthcare_services)




        _human_resources = d.pop("Human Resources", UNSET)
        human_resources: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources]
        if isinstance(_human_resources,  Unset):
            human_resources = UNSET
        else:
            human_resources = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HumanResources.from_dict(_human_resources)




        _information_technology = d.pop("Information Technology", UNSET)
        information_technology: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology]
        if isinstance(_information_technology,  Unset):
            information_technology = UNSET
        else:
            information_technology = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0InformationTechnology.from_dict(_information_technology)




        _legal = d.pop("Legal", UNSET)
        legal: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal]
        if isinstance(_legal,  Unset):
            legal = UNSET
        else:
            legal = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Legal.from_dict(_legal)




        _military_protective_services = d.pop("Military & Protective Services", UNSET)
        military_protective_services: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices]
        if isinstance(_military_protective_services,  Unset):
            military_protective_services = UNSET
        else:
            military_protective_services = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0MilitaryProtectiveServices.from_dict(_military_protective_services)




        _operations = d.pop("Operations", UNSET)
        operations: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations]
        if isinstance(_operations,  Unset):
            operations = UNSET
        else:
            operations = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Operations.from_dict(_operations)




        _program_product_management = d.pop("Program & Product Management", UNSET)
        program_product_management: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement]
        if isinstance(_program_product_management,  Unset):
            program_product_management = UNSET
        else:
            program_product_management = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProgramProductManagement.from_dict(_program_product_management)




        _real_estate = d.pop("Real Estate", UNSET)
        real_estate: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate]
        if isinstance(_real_estate,  Unset):
            real_estate = UNSET
        else:
            real_estate = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0RealEstate.from_dict(_real_estate)




        _sales = d.pop("Sales", UNSET)
        sales: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales]
        if isinstance(_sales,  Unset):
            sales = UNSET
        else:
            sales = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Sales.from_dict(_sales)




        _support = d.pop("Support", UNSET)
        support: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support]
        if isinstance(_support,  Unset):
            support = UNSET
        else:
            support = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Support.from_dict(_support)




        _administrative = d.pop("Administrative", UNSET)
        administrative: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative]
        if isinstance(_administrative,  Unset):
            administrative = UNSET
        else:
            administrative = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Administrative.from_dict(_administrative)




        _finance = d.pop("Finance", UNSET)
        finance: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance]
        if isinstance(_finance,  Unset):
            finance = UNSET
        else:
            finance = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Finance.from_dict(_finance)




        _marketing = d.pop("Marketing", UNSET)
        marketing: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing]
        if isinstance(_marketing,  Unset):
            marketing = UNSET
        else:
            marketing = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Marketing.from_dict(_marketing)




        _purchasing = d.pop("Purchasing", UNSET)
        purchasing: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing]
        if isinstance(_purchasing,  Unset):
            purchasing = UNSET
        else:
            purchasing = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Purchasing.from_dict(_purchasing)




        _product_management = d.pop("Product Management", UNSET)
        product_management: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement]
        if isinstance(_product_management,  Unset):
            product_management = UNSET
        else:
            product_management = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProductManagement.from_dict(_product_management)




        _advertising = d.pop("Advertising", UNSET)
        advertising: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising]
        if isinstance(_advertising,  Unset):
            advertising = UNSET
        else:
            advertising = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Advertising.from_dict(_advertising)




        _analyst = d.pop("Analyst", UNSET)
        analyst: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst]
        if isinstance(_analyst,  Unset):
            analyst = UNSET
        else:
            analyst = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Analyst.from_dict(_analyst)




        _customer_service = d.pop("Customer Service", UNSET)
        customer_service: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService]
        if isinstance(_customer_service,  Unset):
            customer_service = UNSET
        else:
            customer_service = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0CustomerService.from_dict(_customer_service)




        _distribution = d.pop("Distribution", UNSET)
        distribution: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution]
        if isinstance(_distribution,  Unset):
            distribution = UNSET
        else:
            distribution = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Distribution.from_dict(_distribution)




        _design = d.pop("Design", UNSET)
        design: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design]
        if isinstance(_design,  Unset):
            design = UNSET
        else:
            design = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Design.from_dict(_design)




        _general_business = d.pop("General Business", UNSET)
        general_business: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness]
        if isinstance(_general_business,  Unset):
            general_business = UNSET
        else:
            general_business = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0GeneralBusiness.from_dict(_general_business)




        _management = d.pop("Management", UNSET)
        management: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management]
        if isinstance(_management,  Unset):
            management = UNSET
        else:
            management = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Management.from_dict(_management)




        _manufacturing = d.pop("Manufacturing", UNSET)
        manufacturing: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing]
        if isinstance(_manufacturing,  Unset):
            manufacturing = UNSET
        else:
            manufacturing = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Manufacturing.from_dict(_manufacturing)




        _other = d.pop("Other", UNSET)
        other: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other]
        if isinstance(_other,  Unset):
            other = UNSET
        else:
            other = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Other.from_dict(_other)




        _public_relations = d.pop("Public Relations", UNSET)
        public_relations: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations]
        if isinstance(_public_relations,  Unset):
            public_relations = UNSET
        else:
            public_relations = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0PublicRelations.from_dict(_public_relations)




        _project_management = d.pop("Project Management", UNSET)
        project_management: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement]
        if isinstance(_project_management,  Unset):
            project_management = UNSET
        else:
            project_management = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ProjectManagement.from_dict(_project_management)




        _production = d.pop("Production", UNSET)
        production: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production]
        if isinstance(_production,  Unset):
            production = UNSET
        else:
            production = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Production.from_dict(_production)




        _quality_assurance = d.pop("Quality Assurance", UNSET)
        quality_assurance: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance]
        if isinstance(_quality_assurance,  Unset):
            quality_assurance = UNSET
        else:
            quality_assurance = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0QualityAssurance.from_dict(_quality_assurance)




        _research = d.pop("Research", UNSET)
        research: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research]
        if isinstance(_research,  Unset):
            research = UNSET
        else:
            research = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Research.from_dict(_research)




        _science = d.pop("Science", UNSET)
        science: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science]
        if isinstance(_science,  Unset):
            science = UNSET
        else:
            science = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Science.from_dict(_science)




        _supply_chain = d.pop("Supply Chain", UNSET)
        supply_chain: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain]
        if isinstance(_supply_chain,  Unset):
            supply_chain = UNSET
        else:
            supply_chain = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0SupplyChain.from_dict(_supply_chain)




        _training = d.pop("Training", UNSET)
        training: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training]
        if isinstance(_training,  Unset):
            training = UNSET
        else:
            training = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Training.from_dict(_training)




        _health_care_provider = d.pop("Health Care Provider", UNSET)
        health_care_provider: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider]
        if isinstance(_health_care_provider,  Unset):
            health_care_provider = UNSET
        else:
            health_care_provider = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0HealthCareProvider.from_dict(_health_care_provider)




        _accounting = d.pop("Accounting", UNSET)
        accounting: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting]
        if isinstance(_accounting,  Unset):
            accounting = UNSET
        else:
            accounting = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0Accounting.from_dict(_accounting)




        _art_creative = d.pop("Art / Creative", UNSET)
        art_creative: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative]
        if isinstance(_art_creative,  Unset):
            art_creative = UNSET
        else:
            art_creative = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0ArtCreative.from_dict(_art_creative)




        _strategy_planning = d.pop("Strategy / Planning", UNSET)
        strategy_planning: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning]
        if isinstance(_strategy_planning,  Unset):
            strategy_planning = UNSET
        else:
            strategy_planning = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0StrategyPlanning.from_dict(_strategy_planning)




        _writing_editing = d.pop("Writing / Editing", UNSET)
        writing_editing: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing]
        if isinstance(_writing_editing,  Unset):
            writing_editing = UNSET
        else:
            writing_editing = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0PureeJobFunctionsStatsType0WritingEditing.from_dict(_writing_editing)




        sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0 = cls(
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

        return sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0

