from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_administrative_services import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AdministrativeServices,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_aerospace_military import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AerospaceMilitary,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_artificial_intelligence import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtificialIntelligence,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_arts_music import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_automotive import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_business_services import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0BusinessServices,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_cloud import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_construction import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Construction,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consulting import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consumer_goods import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerGoods,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consumer_services import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerServices,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_design import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_education import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_energy import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_entertainment import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Entertainment,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_environmental import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Environmental,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_events import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_farming_agriculture import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FarmingAgriculture,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_finance import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_food_beverage import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FoodBeverage,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_gaming import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_government import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_hardware import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_healthcare import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_hospitality import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hospitality,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_industrials import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Industrials,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_information_technology import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0InformationTechnology,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_insurance import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_legal import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_life_sciences import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0LifeSciences,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_logistics import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_manufacturing import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Manufacturing,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_marketing_advertising import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0MarketingAdvertising,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_media import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_mining import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_nonprofit import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_publishing import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_real_estate import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_retail import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_science_engineering import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ScienceEngineering,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_security import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_software import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_sports import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_telecom import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_trade import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_transportation import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Transportation,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_travel_tourism import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0TravelTourism,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_utilities import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities,
    )
    from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_venture_capital import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0VentureCapital,
    )


T = TypeVar(
    "T", bound="PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0"
)


@_attrs_define
class PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0:
    """
    Attributes:
        administrative_services (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndust
            riesStatsType0AdministrativeServices | Unset):
        aerospace_military (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesS
            tatsType0AerospaceMilitary | Unset):
        artificial_intelligence (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndust
            riesStatsType0ArtificialIntelligence | Unset):
        arts_music
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic
            | Unset):
        automotive
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive
            | Unset):
        business_services (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesSt
            atsType0BusinessServices | Unset):
        cloud
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud |
            Unset):
        construction (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsTy
            pe0Construction | Unset):
        consulting
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting
            | Unset):
        consumer_goods (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStats
            Type0ConsumerGoods | Unset):
        consumer_services (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesSt
            atsType0ConsumerServices | Unset):
        design
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design |
            Unset):
        education
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education
            | Unset):
        energy
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy |
            Unset):
        entertainment (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsT
            ype0Entertainment | Unset):
        environmental (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsT
            ype0Environmental | Unset):
        events
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events |
            Unset):
        farming_agriculture (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustries
            StatsType0FarmingAgriculture | Unset):
        finance
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance |
            Unset):
        food_beverage (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsT
            ype0FoodBeverage | Unset):
        gaming
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming |
            Unset):
        government
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government
            | Unset):
        hardware
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware |
            Unset):
        healthcare
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare
            | Unset):
        hospitality (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsTyp
            e0Hospitality | Unset):
        industrials (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsTyp
            e0Industrials | Unset):
        information_technology (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustr
            iesStatsType0InformationTechnology | Unset):
        insurance
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance
            | Unset):
        legal
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal |
            Unset):
        life_sciences (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsT
            ype0LifeSciences | Unset):
        logistics
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics
            | Unset):
        manufacturing (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsT
            ype0Manufacturing | Unset):
        marketing_advertising (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustri
            esStatsType0MarketingAdvertising | Unset):
        media
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media |
            Unset):
        mining
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining |
            Unset):
        nonprofit
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit
            | Unset):
        publishing
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing
            | Unset):
        real_estate
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate
            | Unset):
        retail
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail |
            Unset):
        science_engineering (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustries
            StatsType0ScienceEngineering | Unset):
        security
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security |
            Unset):
        software
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software |
            Unset):
        sports
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports |
            Unset):
        telecom
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom |
            Unset):
        trade
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade |
            Unset):
        transportation (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStats
            Type0Transportation | Unset):
        travel_tourism (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStats
            Type0TravelTourism | Unset):
        utilities
            (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities
            | Unset):
        venture_capital (PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStat
            sType0VentureCapital | Unset):
    """

    administrative_services: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AdministrativeServices
        | Unset
    ) = UNSET
    aerospace_military: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AerospaceMilitary
        | Unset
    ) = UNSET
    artificial_intelligence: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtificialIntelligence
        | Unset
    ) = UNSET
    arts_music: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic
        | Unset
    ) = UNSET
    automotive: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive
        | Unset
    ) = UNSET
    business_services: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0BusinessServices
        | Unset
    ) = UNSET
    cloud: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud
        | Unset
    ) = UNSET
    construction: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Construction
        | Unset
    ) = UNSET
    consulting: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting
        | Unset
    ) = UNSET
    consumer_goods: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerGoods
        | Unset
    ) = UNSET
    consumer_services: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerServices
        | Unset
    ) = UNSET
    design: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design
        | Unset
    ) = UNSET
    education: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education
        | Unset
    ) = UNSET
    energy: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy
        | Unset
    ) = UNSET
    entertainment: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Entertainment
        | Unset
    ) = UNSET
    environmental: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Environmental
        | Unset
    ) = UNSET
    events: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events
        | Unset
    ) = UNSET
    farming_agriculture: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FarmingAgriculture
        | Unset
    ) = UNSET
    finance: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance
        | Unset
    ) = UNSET
    food_beverage: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FoodBeverage
        | Unset
    ) = UNSET
    gaming: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming
        | Unset
    ) = UNSET
    government: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government
        | Unset
    ) = UNSET
    hardware: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware
        | Unset
    ) = UNSET
    healthcare: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare
        | Unset
    ) = UNSET
    hospitality: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hospitality
        | Unset
    ) = UNSET
    industrials: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Industrials
        | Unset
    ) = UNSET
    information_technology: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0InformationTechnology
        | Unset
    ) = UNSET
    insurance: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance
        | Unset
    ) = UNSET
    legal: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal
        | Unset
    ) = UNSET
    life_sciences: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0LifeSciences
        | Unset
    ) = UNSET
    logistics: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics
        | Unset
    ) = UNSET
    manufacturing: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Manufacturing
        | Unset
    ) = UNSET
    marketing_advertising: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0MarketingAdvertising
        | Unset
    ) = UNSET
    media: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media
        | Unset
    ) = UNSET
    mining: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining
        | Unset
    ) = UNSET
    nonprofit: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit
        | Unset
    ) = UNSET
    publishing: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing
        | Unset
    ) = UNSET
    real_estate: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate
        | Unset
    ) = UNSET
    retail: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail
        | Unset
    ) = UNSET
    science_engineering: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ScienceEngineering
        | Unset
    ) = UNSET
    security: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security
        | Unset
    ) = UNSET
    software: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software
        | Unset
    ) = UNSET
    sports: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports
        | Unset
    ) = UNSET
    telecom: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom
        | Unset
    ) = UNSET
    trade: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade
        | Unset
    ) = UNSET
    transportation: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Transportation
        | Unset
    ) = UNSET
    travel_tourism: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0TravelTourism
        | Unset
    ) = UNSET
    utilities: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities
        | Unset
    ) = UNSET
    venture_capital: (
        PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0VentureCapital
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        administrative_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.administrative_services, Unset):
            administrative_services = self.administrative_services.to_dict()

        aerospace_military: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aerospace_military, Unset):
            aerospace_military = self.aerospace_military.to_dict()

        artificial_intelligence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.artificial_intelligence, Unset):
            artificial_intelligence = self.artificial_intelligence.to_dict()

        arts_music: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arts_music, Unset):
            arts_music = self.arts_music.to_dict()

        automotive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.automotive, Unset):
            automotive = self.automotive.to_dict()

        business_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_services, Unset):
            business_services = self.business_services.to_dict()

        cloud: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud, Unset):
            cloud = self.cloud.to_dict()

        construction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.construction, Unset):
            construction = self.construction.to_dict()

        consulting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consulting, Unset):
            consulting = self.consulting.to_dict()

        consumer_goods: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consumer_goods, Unset):
            consumer_goods = self.consumer_goods.to_dict()

        consumer_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consumer_services, Unset):
            consumer_services = self.consumer_services.to_dict()

        design: dict[str, Any] | Unset = UNSET
        if not isinstance(self.design, Unset):
            design = self.design.to_dict()

        education: dict[str, Any] | Unset = UNSET
        if not isinstance(self.education, Unset):
            education = self.education.to_dict()

        energy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict()

        entertainment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entertainment, Unset):
            entertainment = self.entertainment.to_dict()

        environmental: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environmental, Unset):
            environmental = self.environmental.to_dict()

        events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        farming_agriculture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.farming_agriculture, Unset):
            farming_agriculture = self.farming_agriculture.to_dict()

        finance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        food_beverage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.food_beverage, Unset):
            food_beverage = self.food_beverage.to_dict()

        gaming: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gaming, Unset):
            gaming = self.gaming.to_dict()

        government: dict[str, Any] | Unset = UNSET
        if not isinstance(self.government, Unset):
            government = self.government.to_dict()

        hardware: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardware, Unset):
            hardware = self.hardware.to_dict()

        healthcare: dict[str, Any] | Unset = UNSET
        if not isinstance(self.healthcare, Unset):
            healthcare = self.healthcare.to_dict()

        hospitality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hospitality, Unset):
            hospitality = self.hospitality.to_dict()

        industrials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.industrials, Unset):
            industrials = self.industrials.to_dict()

        information_technology: dict[str, Any] | Unset = UNSET
        if not isinstance(self.information_technology, Unset):
            information_technology = self.information_technology.to_dict()

        insurance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insurance, Unset):
            insurance = self.insurance.to_dict()

        legal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        life_sciences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.life_sciences, Unset):
            life_sciences = self.life_sciences.to_dict()

        logistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logistics, Unset):
            logistics = self.logistics.to_dict()

        manufacturing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturing, Unset):
            manufacturing = self.manufacturing.to_dict()

        marketing_advertising: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marketing_advertising, Unset):
            marketing_advertising = self.marketing_advertising.to_dict()

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        mining: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mining, Unset):
            mining = self.mining.to_dict()

        nonprofit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nonprofit, Unset):
            nonprofit = self.nonprofit.to_dict()

        publishing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publishing, Unset):
            publishing = self.publishing.to_dict()

        real_estate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real_estate, Unset):
            real_estate = self.real_estate.to_dict()

        retail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retail, Unset):
            retail = self.retail.to_dict()

        science_engineering: dict[str, Any] | Unset = UNSET
        if not isinstance(self.science_engineering, Unset):
            science_engineering = self.science_engineering.to_dict()

        security: dict[str, Any] | Unset = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.to_dict()

        software: dict[str, Any] | Unset = UNSET
        if not isinstance(self.software, Unset):
            software = self.software.to_dict()

        sports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sports, Unset):
            sports = self.sports.to_dict()

        telecom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telecom, Unset):
            telecom = self.telecom.to_dict()

        trade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trade, Unset):
            trade = self.trade.to_dict()

        transportation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation, Unset):
            transportation = self.transportation.to_dict()

        travel_tourism: dict[str, Any] | Unset = UNSET
        if not isinstance(self.travel_tourism, Unset):
            travel_tourism = self.travel_tourism.to_dict()

        utilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utilities, Unset):
            utilities = self.utilities.to_dict()

        venture_capital: dict[str, Any] | Unset = UNSET
        if not isinstance(self.venture_capital, Unset):
            venture_capital = self.venture_capital.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if administrative_services is not UNSET:
            field_dict["Administrative Services"] = administrative_services
        if aerospace_military is not UNSET:
            field_dict["Aerospace & Military"] = aerospace_military
        if artificial_intelligence is not UNSET:
            field_dict["Artificial Intelligence"] = artificial_intelligence
        if arts_music is not UNSET:
            field_dict["Arts & Music"] = arts_music
        if automotive is not UNSET:
            field_dict["Automotive"] = automotive
        if business_services is not UNSET:
            field_dict["Business Services"] = business_services
        if cloud is not UNSET:
            field_dict["Cloud"] = cloud
        if construction is not UNSET:
            field_dict["Construction"] = construction
        if consulting is not UNSET:
            field_dict["Consulting"] = consulting
        if consumer_goods is not UNSET:
            field_dict["Consumer Goods"] = consumer_goods
        if consumer_services is not UNSET:
            field_dict["Consumer Services"] = consumer_services
        if design is not UNSET:
            field_dict["Design"] = design
        if education is not UNSET:
            field_dict["Education"] = education
        if energy is not UNSET:
            field_dict["Energy"] = energy
        if entertainment is not UNSET:
            field_dict["Entertainment"] = entertainment
        if environmental is not UNSET:
            field_dict["Environmental"] = environmental
        if events is not UNSET:
            field_dict["Events"] = events
        if farming_agriculture is not UNSET:
            field_dict["Farming & Agriculture"] = farming_agriculture
        if finance is not UNSET:
            field_dict["Finance"] = finance
        if food_beverage is not UNSET:
            field_dict["Food & Beverage"] = food_beverage
        if gaming is not UNSET:
            field_dict["Gaming"] = gaming
        if government is not UNSET:
            field_dict["Government"] = government
        if hardware is not UNSET:
            field_dict["Hardware"] = hardware
        if healthcare is not UNSET:
            field_dict["Healthcare"] = healthcare
        if hospitality is not UNSET:
            field_dict["Hospitality"] = hospitality
        if industrials is not UNSET:
            field_dict["Industrials"] = industrials
        if information_technology is not UNSET:
            field_dict["Information Technology"] = information_technology
        if insurance is not UNSET:
            field_dict["Insurance"] = insurance
        if legal is not UNSET:
            field_dict["Legal"] = legal
        if life_sciences is not UNSET:
            field_dict["Life Sciences"] = life_sciences
        if logistics is not UNSET:
            field_dict["Logistics"] = logistics
        if manufacturing is not UNSET:
            field_dict["Manufacturing"] = manufacturing
        if marketing_advertising is not UNSET:
            field_dict["Marketing & Advertising"] = marketing_advertising
        if media is not UNSET:
            field_dict["Media"] = media
        if mining is not UNSET:
            field_dict["Mining"] = mining
        if nonprofit is not UNSET:
            field_dict["Nonprofit"] = nonprofit
        if publishing is not UNSET:
            field_dict["Publishing"] = publishing
        if real_estate is not UNSET:
            field_dict["Real Estate"] = real_estate
        if retail is not UNSET:
            field_dict["Retail"] = retail
        if science_engineering is not UNSET:
            field_dict["Science & Engineering"] = science_engineering
        if security is not UNSET:
            field_dict["Security"] = security
        if software is not UNSET:
            field_dict["Software"] = software
        if sports is not UNSET:
            field_dict["Sports"] = sports
        if telecom is not UNSET:
            field_dict["Telecom"] = telecom
        if trade is not UNSET:
            field_dict["Trade"] = trade
        if transportation is not UNSET:
            field_dict["Transportation"] = transportation
        if travel_tourism is not UNSET:
            field_dict["Travel & Tourism"] = travel_tourism
        if utilities is not UNSET:
            field_dict["Utilities"] = utilities
        if venture_capital is not UNSET:
            field_dict["Venture Capital"] = venture_capital

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_administrative_services import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AdministrativeServices,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_aerospace_military import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AerospaceMilitary,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_artificial_intelligence import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtificialIntelligence,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_arts_music import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_automotive import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_business_services import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0BusinessServices,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_cloud import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_construction import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Construction,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consulting import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consumer_goods import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerGoods,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_consumer_services import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerServices,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_design import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_education import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_energy import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_entertainment import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Entertainment,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_environmental import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Environmental,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_events import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_farming_agriculture import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FarmingAgriculture,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_finance import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_food_beverage import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FoodBeverage,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_gaming import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_government import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_hardware import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_healthcare import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_hospitality import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hospitality,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_industrials import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Industrials,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_information_technology import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0InformationTechnology,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_insurance import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_legal import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_life_sciences import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0LifeSciences,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_logistics import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_manufacturing import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Manufacturing,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_marketing_advertising import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0MarketingAdvertising,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_media import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_mining import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_nonprofit import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_publishing import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_real_estate import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_retail import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_science_engineering import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ScienceEngineering,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_security import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_software import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_sports import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_telecom import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_trade import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_transportation import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Transportation,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_travel_tourism import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0TravelTourism,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_utilities import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities,
        )
        from ..models.paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0_venture_capital import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0VentureCapital,
        )

        d = dict(src_dict)
        _administrative_services = d.pop("Administrative Services", UNSET)
        administrative_services: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AdministrativeServices
            | Unset
        )
        if isinstance(_administrative_services, Unset):
            administrative_services = UNSET
        else:
            administrative_services = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AdministrativeServices.from_dict(
                _administrative_services
            )

        _aerospace_military = d.pop("Aerospace & Military", UNSET)
        aerospace_military: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AerospaceMilitary
            | Unset
        )
        if isinstance(_aerospace_military, Unset):
            aerospace_military = UNSET
        else:
            aerospace_military = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0AerospaceMilitary.from_dict(
                _aerospace_military
            )

        _artificial_intelligence = d.pop("Artificial Intelligence", UNSET)
        artificial_intelligence: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtificialIntelligence
            | Unset
        )
        if isinstance(_artificial_intelligence, Unset):
            artificial_intelligence = UNSET
        else:
            artificial_intelligence = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtificialIntelligence.from_dict(
                _artificial_intelligence
            )

        _arts_music = d.pop("Arts & Music", UNSET)
        arts_music: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic
            | Unset
        )
        if isinstance(_arts_music, Unset):
            arts_music = UNSET
        else:
            arts_music = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ArtsMusic.from_dict(
                _arts_music
            )

        _automotive = d.pop("Automotive", UNSET)
        automotive: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive
            | Unset
        )
        if isinstance(_automotive, Unset):
            automotive = UNSET
        else:
            automotive = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Automotive.from_dict(
                _automotive
            )

        _business_services = d.pop("Business Services", UNSET)
        business_services: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0BusinessServices
            | Unset
        )
        if isinstance(_business_services, Unset):
            business_services = UNSET
        else:
            business_services = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0BusinessServices.from_dict(
                _business_services
            )

        _cloud = d.pop("Cloud", UNSET)
        cloud: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud
            | Unset
        )
        if isinstance(_cloud, Unset):
            cloud = UNSET
        else:
            cloud = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Cloud.from_dict(
                _cloud
            )

        _construction = d.pop("Construction", UNSET)
        construction: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Construction
            | Unset
        )
        if isinstance(_construction, Unset):
            construction = UNSET
        else:
            construction = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Construction.from_dict(
                _construction
            )

        _consulting = d.pop("Consulting", UNSET)
        consulting: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting
            | Unset
        )
        if isinstance(_consulting, Unset):
            consulting = UNSET
        else:
            consulting = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Consulting.from_dict(
                _consulting
            )

        _consumer_goods = d.pop("Consumer Goods", UNSET)
        consumer_goods: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerGoods
            | Unset
        )
        if isinstance(_consumer_goods, Unset):
            consumer_goods = UNSET
        else:
            consumer_goods = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerGoods.from_dict(
                _consumer_goods
            )

        _consumer_services = d.pop("Consumer Services", UNSET)
        consumer_services: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerServices
            | Unset
        )
        if isinstance(_consumer_services, Unset):
            consumer_services = UNSET
        else:
            consumer_services = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ConsumerServices.from_dict(
                _consumer_services
            )

        _design = d.pop("Design", UNSET)
        design: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design
            | Unset
        )
        if isinstance(_design, Unset):
            design = UNSET
        else:
            design = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Design.from_dict(
                _design
            )

        _education = d.pop("Education", UNSET)
        education: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education
            | Unset
        )
        if isinstance(_education, Unset):
            education = UNSET
        else:
            education = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Education.from_dict(
                _education
            )

        _energy = d.pop("Energy", UNSET)
        energy: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy
            | Unset
        )
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Energy.from_dict(
                _energy
            )

        _entertainment = d.pop("Entertainment", UNSET)
        entertainment: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Entertainment
            | Unset
        )
        if isinstance(_entertainment, Unset):
            entertainment = UNSET
        else:
            entertainment = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Entertainment.from_dict(
                _entertainment
            )

        _environmental = d.pop("Environmental", UNSET)
        environmental: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Environmental
            | Unset
        )
        if isinstance(_environmental, Unset):
            environmental = UNSET
        else:
            environmental = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Environmental.from_dict(
                _environmental
            )

        _events = d.pop("Events", UNSET)
        events: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events
            | Unset
        )
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Events.from_dict(
                _events
            )

        _farming_agriculture = d.pop("Farming & Agriculture", UNSET)
        farming_agriculture: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FarmingAgriculture
            | Unset
        )
        if isinstance(_farming_agriculture, Unset):
            farming_agriculture = UNSET
        else:
            farming_agriculture = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FarmingAgriculture.from_dict(
                _farming_agriculture
            )

        _finance = d.pop("Finance", UNSET)
        finance: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance
            | Unset
        )
        if isinstance(_finance, Unset):
            finance = UNSET
        else:
            finance = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Finance.from_dict(
                _finance
            )

        _food_beverage = d.pop("Food & Beverage", UNSET)
        food_beverage: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FoodBeverage
            | Unset
        )
        if isinstance(_food_beverage, Unset):
            food_beverage = UNSET
        else:
            food_beverage = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0FoodBeverage.from_dict(
                _food_beverage
            )

        _gaming = d.pop("Gaming", UNSET)
        gaming: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming
            | Unset
        )
        if isinstance(_gaming, Unset):
            gaming = UNSET
        else:
            gaming = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Gaming.from_dict(
                _gaming
            )

        _government = d.pop("Government", UNSET)
        government: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government
            | Unset
        )
        if isinstance(_government, Unset):
            government = UNSET
        else:
            government = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Government.from_dict(
                _government
            )

        _hardware = d.pop("Hardware", UNSET)
        hardware: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware
            | Unset
        )
        if isinstance(_hardware, Unset):
            hardware = UNSET
        else:
            hardware = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hardware.from_dict(
                _hardware
            )

        _healthcare = d.pop("Healthcare", UNSET)
        healthcare: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare
            | Unset
        )
        if isinstance(_healthcare, Unset):
            healthcare = UNSET
        else:
            healthcare = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Healthcare.from_dict(
                _healthcare
            )

        _hospitality = d.pop("Hospitality", UNSET)
        hospitality: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hospitality
            | Unset
        )
        if isinstance(_hospitality, Unset):
            hospitality = UNSET
        else:
            hospitality = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Hospitality.from_dict(
                _hospitality
            )

        _industrials = d.pop("Industrials", UNSET)
        industrials: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Industrials
            | Unset
        )
        if isinstance(_industrials, Unset):
            industrials = UNSET
        else:
            industrials = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Industrials.from_dict(
                _industrials
            )

        _information_technology = d.pop("Information Technology", UNSET)
        information_technology: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0InformationTechnology
            | Unset
        )
        if isinstance(_information_technology, Unset):
            information_technology = UNSET
        else:
            information_technology = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0InformationTechnology.from_dict(
                _information_technology
            )

        _insurance = d.pop("Insurance", UNSET)
        insurance: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance
            | Unset
        )
        if isinstance(_insurance, Unset):
            insurance = UNSET
        else:
            insurance = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Insurance.from_dict(
                _insurance
            )

        _legal = d.pop("Legal", UNSET)
        legal: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal
            | Unset
        )
        if isinstance(_legal, Unset):
            legal = UNSET
        else:
            legal = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Legal.from_dict(
                _legal
            )

        _life_sciences = d.pop("Life Sciences", UNSET)
        life_sciences: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0LifeSciences
            | Unset
        )
        if isinstance(_life_sciences, Unset):
            life_sciences = UNSET
        else:
            life_sciences = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0LifeSciences.from_dict(
                _life_sciences
            )

        _logistics = d.pop("Logistics", UNSET)
        logistics: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics
            | Unset
        )
        if isinstance(_logistics, Unset):
            logistics = UNSET
        else:
            logistics = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Logistics.from_dict(
                _logistics
            )

        _manufacturing = d.pop("Manufacturing", UNSET)
        manufacturing: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Manufacturing
            | Unset
        )
        if isinstance(_manufacturing, Unset):
            manufacturing = UNSET
        else:
            manufacturing = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Manufacturing.from_dict(
                _manufacturing
            )

        _marketing_advertising = d.pop("Marketing & Advertising", UNSET)
        marketing_advertising: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0MarketingAdvertising
            | Unset
        )
        if isinstance(_marketing_advertising, Unset):
            marketing_advertising = UNSET
        else:
            marketing_advertising = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0MarketingAdvertising.from_dict(
                _marketing_advertising
            )

        _media = d.pop("Media", UNSET)
        media: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media
            | Unset
        )
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Media.from_dict(
                _media
            )

        _mining = d.pop("Mining", UNSET)
        mining: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining
            | Unset
        )
        if isinstance(_mining, Unset):
            mining = UNSET
        else:
            mining = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Mining.from_dict(
                _mining
            )

        _nonprofit = d.pop("Nonprofit", UNSET)
        nonprofit: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit
            | Unset
        )
        if isinstance(_nonprofit, Unset):
            nonprofit = UNSET
        else:
            nonprofit = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Nonprofit.from_dict(
                _nonprofit
            )

        _publishing = d.pop("Publishing", UNSET)
        publishing: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing
            | Unset
        )
        if isinstance(_publishing, Unset):
            publishing = UNSET
        else:
            publishing = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Publishing.from_dict(
                _publishing
            )

        _real_estate = d.pop("Real Estate", UNSET)
        real_estate: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate
            | Unset
        )
        if isinstance(_real_estate, Unset):
            real_estate = UNSET
        else:
            real_estate = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0RealEstate.from_dict(
                _real_estate
            )

        _retail = d.pop("Retail", UNSET)
        retail: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail
            | Unset
        )
        if isinstance(_retail, Unset):
            retail = UNSET
        else:
            retail = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Retail.from_dict(
                _retail
            )

        _science_engineering = d.pop("Science & Engineering", UNSET)
        science_engineering: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ScienceEngineering
            | Unset
        )
        if isinstance(_science_engineering, Unset):
            science_engineering = UNSET
        else:
            science_engineering = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0ScienceEngineering.from_dict(
                _science_engineering
            )

        _security = d.pop("Security", UNSET)
        security: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security
            | Unset
        )
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Security.from_dict(
                _security
            )

        _software = d.pop("Software", UNSET)
        software: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software
            | Unset
        )
        if isinstance(_software, Unset):
            software = UNSET
        else:
            software = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Software.from_dict(
                _software
            )

        _sports = d.pop("Sports", UNSET)
        sports: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports
            | Unset
        )
        if isinstance(_sports, Unset):
            sports = UNSET
        else:
            sports = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Sports.from_dict(
                _sports
            )

        _telecom = d.pop("Telecom", UNSET)
        telecom: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom
            | Unset
        )
        if isinstance(_telecom, Unset):
            telecom = UNSET
        else:
            telecom = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Telecom.from_dict(
                _telecom
            )

        _trade = d.pop("Trade", UNSET)
        trade: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade
            | Unset
        )
        if isinstance(_trade, Unset):
            trade = UNSET
        else:
            trade = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Trade.from_dict(
                _trade
            )

        _transportation = d.pop("Transportation", UNSET)
        transportation: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Transportation
            | Unset
        )
        if isinstance(_transportation, Unset):
            transportation = UNSET
        else:
            transportation = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Transportation.from_dict(
                _transportation
            )

        _travel_tourism = d.pop("Travel & Tourism", UNSET)
        travel_tourism: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0TravelTourism
            | Unset
        )
        if isinstance(_travel_tourism, Unset):
            travel_tourism = UNSET
        else:
            travel_tourism = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0TravelTourism.from_dict(
                _travel_tourism
            )

        _utilities = d.pop("Utilities", UNSET)
        utilities: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities
            | Unset
        )
        if isinstance(_utilities, Unset):
            utilities = UNSET
        else:
            utilities = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0Utilities.from_dict(
                _utilities
            )

        _venture_capital = d.pop("Venture Capital", UNSET)
        venture_capital: (
            PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0VentureCapital
            | Unset
        )
        if isinstance(_venture_capital, Unset):
            venture_capital = UNSET
        else:
            venture_capital = PaginatedCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0StandardIndustriesStatsType0VentureCapital.from_dict(
                _venture_capital
            )

        paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0 = cls(
            administrative_services=administrative_services,
            aerospace_military=aerospace_military,
            artificial_intelligence=artificial_intelligence,
            arts_music=arts_music,
            automotive=automotive,
            business_services=business_services,
            cloud=cloud,
            construction=construction,
            consulting=consulting,
            consumer_goods=consumer_goods,
            consumer_services=consumer_services,
            design=design,
            education=education,
            energy=energy,
            entertainment=entertainment,
            environmental=environmental,
            events=events,
            farming_agriculture=farming_agriculture,
            finance=finance,
            food_beverage=food_beverage,
            gaming=gaming,
            government=government,
            hardware=hardware,
            healthcare=healthcare,
            hospitality=hospitality,
            industrials=industrials,
            information_technology=information_technology,
            insurance=insurance,
            legal=legal,
            life_sciences=life_sciences,
            logistics=logistics,
            manufacturing=manufacturing,
            marketing_advertising=marketing_advertising,
            media=media,
            mining=mining,
            nonprofit=nonprofit,
            publishing=publishing,
            real_estate=real_estate,
            retail=retail,
            science_engineering=science_engineering,
            security=security,
            software=software,
            sports=sports,
            telecom=telecom,
            trade=trade,
            transportation=transportation,
            travel_tourism=travel_tourism,
            utilities=utilities,
            venture_capital=venture_capital,
        )

        return paginated_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_standard_industries_stats_type_0
