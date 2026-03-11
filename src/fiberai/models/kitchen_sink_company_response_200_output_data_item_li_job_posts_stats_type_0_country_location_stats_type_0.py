from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0abw import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0afg import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ago import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aia import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ala import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0alb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0and import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ant import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0are import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0arg import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0arm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0asm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ata import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0atf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0atg import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aus import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aut import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aze import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bdi import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bel import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ben import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bes import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bfa import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bgd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bgr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bhr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bhs import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bih import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blz import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bmu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bol import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bra import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0brb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0brn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0btn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bvt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bwa import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0caf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0can import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cck import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0che import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0chl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0chn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0civ import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cmr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cod import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cog import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cok import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0col import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0com import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cpv import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cri import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cub import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cuw import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cxr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cym import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cyp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cze import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0deu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dji import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dma import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dnk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dom import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dza import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ecu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0egy import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0eri import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0esh import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0esp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0est import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0eth import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fin import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fji import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0flk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fra import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fro import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fsm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gab import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gbr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0geo import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ggy import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gha import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gib import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gin import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0glp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gmb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gnb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gnq import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grc import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gtm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0guf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gum import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0guy import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hkg import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hmd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hnd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0per import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0png import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0som import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
        KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE,
    )


T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0:
    """
    Attributes:
        usa (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA | Unset):
        gbr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR | Unset):
        fra (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA | Unset):
        ind (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND | Unset):
        bra (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA | Unset):
        deu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU | Unset):
        esp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP | Unset):
        can (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN | Unset):
        aus (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS | Unset):
        nld (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD | Unset):
        ita (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA | Unset):
        zaf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF | Unset):
        bel (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL | Unset):
        chn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN | Unset):
        tur (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR | Unset):
        mex (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX | Unset):
        che (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE | Unset):
        nor (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR | Unset):
        are (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE | Unset):
        swe (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE | Unset):
        pol (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL | Unset):
        idn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN | Unset):
        arg (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG | Unset):
        prt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT | Unset):
        col (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL | Unset):
        chl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL | Unset):
        pak (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK | Unset):
        dnk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK | Unset):
        jpn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN | Unset):
        nga (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA | Unset):
        sgp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP | Unset):
        per (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER | Unset):
        nzl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL | Unset):
        aut (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT | Unset):
        irl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL | Unset):
        mys (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS | Unset):
        bgd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD | Unset):
        egy (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY | Unset):
        isr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR | Unset):
        sau (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU | Unset):
        phl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL | Unset):
        fin (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN | Unset):
        irn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN | Unset):
        rou (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU | Unset):
        cze (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE | Unset):
        grc (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC | Unset):
        hkg (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG | Unset):
        hun (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN | Unset):
        ken (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN | Unset):
        mar (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR | Unset):
        vnm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM | Unset):
        rus (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS | Unset):
        ukr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR | Unset):
        ecu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU | Unset):
        tha (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA | Unset):
        lka (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA | Unset):
        kor (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR | Unset):
        bgr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR | Unset):
        gha (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA | Unset):
        srb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB | Unset):
        twn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN | Unset):
        hrv (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV | Unset):
        ltu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU | Unset):
        pri (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI | Unset):
        svk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK | Unset):
        tun (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN | Unset):
        est (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST | Unset):
        ven (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN | Unset):
        cri (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI | Unset):
        pan (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN | Unset):
        ury (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY | Unset):
        lbn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN | Unset):
        lux (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX | Unset):
        cyp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP | Unset):
        npl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL | Unset):
        jor (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR | Unset):
        svn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN | Unset):
        mtq (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ | Unset):
        qat (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT | Unset):
        glp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP | Unset):
        uga (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA | Unset):
        dza (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA | Unset):
        gtm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM | Unset):
        cmr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR | Unset):
        lva (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA | Unset):
        dom (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM | Unset):
        aze (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE | Unset):
        geo (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO | Unset):
        sen (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN | Unset):
        tza (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA | Unset):
        zwe (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE | Unset):
        kwt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT | Unset):
        mlt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT | Unset):
        omn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN | Unset):
        bol (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL | Unset):
        slv (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV | Unset):
        arm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM | Unset):
        pry (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY | Unset):
        irq (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ | Unset):
        khm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM | Unset):
        bih (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH | Unset):
        ago (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO | Unset):
        bhr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR | Unset):
        alb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB | Unset):
        kaz (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ | Unset):
        civ (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV | Unset):
        eth (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH | Unset):
        mus (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS | Unset):
        zmb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB | Unset):
        mkd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD | Unset):
        cod (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD | Unset):
        blr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR | Unset):
        moz (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ | Unset):
        reu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU | Unset):
        tto (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO | Unset):
        guf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF | Unset):
        isl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL | Unset):
        mmr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR | Unset):
        hnd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND | Unset):
        rwa (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA | Unset):
        mdg (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG | Unset):
        ben (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN | Unset):
        uzb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB | Unset):
        nam (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM | Unset):
        bwa (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA | Unset):
        mda (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA | Unset):
        jey (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY | Unset):
        nic (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC | Unset):
        sdn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN | Unset):
        jam (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM | Unset):
        imn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN | Unset):
        bfa (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA | Unset):
        mng (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG | Unset):
        mne (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE | Unset):
        mco (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO | Unset):
        tgo (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO | Unset):
        afg (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG | Unset):
        lby (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY | Unset):
        xkx (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX | Unset):
        cym (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM | Unset):
        mwi (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI | Unset):
        som (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM | Unset):
        png (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG | Unset):
        mdv (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV | Unset):
        mli (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI | Unset):
        gin (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN | Unset):
        pse (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE | Unset):
        gab (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB | Unset):
        lie (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE | Unset):
        hti (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI | Unset):
        syr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR | Unset):
        brb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB | Unset):
        yem (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM | Unset):
        ggy (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY | Unset):
        ncl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL | Unset):
        and_ (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND | Unset):
        sur (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR | Unset):
        myt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT | Unset):
        kgz (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ | Unset):
        bhs (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS | Unset):
        gib (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB | Unset):
        cog (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG | Unset):
        fji (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI | Unset):
        blm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM | Unset):
        cuw (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW | Unset):
        cub (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB | Unset):
        sle (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE | Unset):
        blz (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ | Unset):
        ner (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER | Unset):
        lbr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR | Unset):
        vir (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR | Unset):
        pyf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF | Unset):
        gum (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM | Unset):
        mrt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT | Unset):
        abw (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW | Unset):
        syc (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC | Unset):
        guy (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY | Unset):
        lso (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO | Unset):
        swz (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ | Unset):
        ssd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD | Unset):
        lca (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA | Unset):
        mac (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC | Unset):
        smr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR | Unset):
        lao (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO | Unset):
        brn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN | Unset):
        tcd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD | Unset):
        bmu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU | Unset):
        vgb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB | Unset):
        prk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK | Unset):
        btn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN | Unset):
        bdi (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI | Unset):
        fro (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO | Unset):
        tjk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK | Unset):
        gmb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB | Unset):
        stp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP | Unset):
        ant (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT | Unset):
        vct (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT | Unset):
        dji (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI | Unset):
        cpv (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV | Unset):
        tkm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM | Unset):
        atg (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG | Unset):
        tca (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA | Unset):
        kna (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA | Unset):
        grd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD | Unset):
        asm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM | Unset):
        vut (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT | Unset):
        gnq (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ | Unset):
        grl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL | Unset):
        sxm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM | Unset):
        mnp (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP | Unset):
        com (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM | Unset):
        tls (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS | Unset):
        sjm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM | Unset):
        caf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF | Unset):
        dma (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA | Unset):
        maf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF | Unset):
        wsm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM | Unset):
        bes (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES | Unset):
        mhl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL | Unset):
        aia (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA | Unset):
        ton (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON | Unset):
        cok (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK | Unset):
        slb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB | Unset):
        spm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM | Unset):
        gnb (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB | Unset):
        ata (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA | Unset):
        tuv (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV | Unset):
        ala (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA | Unset):
        iot (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT | Unset):
        eri (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI | Unset):
        plw (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW | Unset):
        fsm (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM | Unset):
        nru (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU | Unset):
        pcn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN | Unset):
        flk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK | Unset):
        msr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR | Unset):
        vat (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT | Unset):
        kir (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR | Unset):
        shn (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN | Unset):
        niu (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU | Unset):
        wlf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF | Unset):
        hmd (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD | Unset):
        cxr (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR | Unset):
        nfk (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK | Unset):
        atf (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF | Unset):
        cck (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK | Unset):
        sgs (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS | Unset):
        bvt (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT | Unset):
        umi (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI | Unset):
        esh (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH | Unset):
        tkl (KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL | Unset):
    """

    usa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA | Unset = UNSET
    gbr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR | Unset = UNSET
    fra: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA | Unset = UNSET
    ind: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND | Unset = UNSET
    bra: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA | Unset = UNSET
    deu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU | Unset = UNSET
    esp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP | Unset = UNSET
    can: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN | Unset = UNSET
    aus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS | Unset = UNSET
    nld: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD | Unset = UNSET
    ita: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA | Unset = UNSET
    zaf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF | Unset = UNSET
    bel: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL | Unset = UNSET
    chn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN | Unset = UNSET
    tur: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR | Unset = UNSET
    mex: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX | Unset = UNSET
    che: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE | Unset = UNSET
    nor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR | Unset = UNSET
    are: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE | Unset = UNSET
    swe: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE | Unset = UNSET
    pol: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL | Unset = UNSET
    idn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN | Unset = UNSET
    arg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG | Unset = UNSET
    prt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT | Unset = UNSET
    col: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL | Unset = UNSET
    chl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL | Unset = UNSET
    pak: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK | Unset = UNSET
    dnk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK | Unset = UNSET
    jpn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN | Unset = UNSET
    nga: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA | Unset = UNSET
    sgp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP | Unset = UNSET
    per: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER | Unset = UNSET
    nzl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL | Unset = UNSET
    aut: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT | Unset = UNSET
    irl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL | Unset = UNSET
    mys: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS | Unset = UNSET
    bgd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD | Unset = UNSET
    egy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY | Unset = UNSET
    isr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR | Unset = UNSET
    sau: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU | Unset = UNSET
    phl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL | Unset = UNSET
    fin: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN | Unset = UNSET
    irn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN | Unset = UNSET
    rou: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU | Unset = UNSET
    cze: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE | Unset = UNSET
    grc: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC | Unset = UNSET
    hkg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG | Unset = UNSET
    hun: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN | Unset = UNSET
    ken: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN | Unset = UNSET
    mar: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR | Unset = UNSET
    vnm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM | Unset = UNSET
    rus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS | Unset = UNSET
    ukr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR | Unset = UNSET
    ecu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU | Unset = UNSET
    tha: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA | Unset = UNSET
    lka: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA | Unset = UNSET
    kor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR | Unset = UNSET
    bgr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR | Unset = UNSET
    gha: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA | Unset = UNSET
    srb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB | Unset = UNSET
    twn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN | Unset = UNSET
    hrv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV | Unset = UNSET
    ltu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU | Unset = UNSET
    pri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI | Unset = UNSET
    svk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK | Unset = UNSET
    tun: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN | Unset = UNSET
    est: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST | Unset = UNSET
    ven: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN | Unset = UNSET
    cri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI | Unset = UNSET
    pan: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN | Unset = UNSET
    ury: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY | Unset = UNSET
    lbn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN | Unset = UNSET
    lux: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX | Unset = UNSET
    cyp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP | Unset = UNSET
    npl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL | Unset = UNSET
    jor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR | Unset = UNSET
    svn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN | Unset = UNSET
    mtq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ | Unset = UNSET
    qat: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT | Unset = UNSET
    glp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP | Unset = UNSET
    uga: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA | Unset = UNSET
    dza: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA | Unset = UNSET
    gtm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM | Unset = UNSET
    cmr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR | Unset = UNSET
    lva: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA | Unset = UNSET
    dom: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM | Unset = UNSET
    aze: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE | Unset = UNSET
    geo: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO | Unset = UNSET
    sen: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN | Unset = UNSET
    tza: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA | Unset = UNSET
    zwe: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE | Unset = UNSET
    kwt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT | Unset = UNSET
    mlt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT | Unset = UNSET
    omn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN | Unset = UNSET
    bol: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL | Unset = UNSET
    slv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV | Unset = UNSET
    arm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM | Unset = UNSET
    pry: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY | Unset = UNSET
    irq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ | Unset = UNSET
    khm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM | Unset = UNSET
    bih: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH | Unset = UNSET
    ago: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO | Unset = UNSET
    bhr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR | Unset = UNSET
    alb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB | Unset = UNSET
    kaz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ | Unset = UNSET
    civ: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV | Unset = UNSET
    eth: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH | Unset = UNSET
    mus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS | Unset = UNSET
    zmb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB | Unset = UNSET
    mkd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD | Unset = UNSET
    cod: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD | Unset = UNSET
    blr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR | Unset = UNSET
    moz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ | Unset = UNSET
    reu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU | Unset = UNSET
    tto: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO | Unset = UNSET
    guf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF | Unset = UNSET
    isl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL | Unset = UNSET
    mmr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR | Unset = UNSET
    hnd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND | Unset = UNSET
    rwa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA | Unset = UNSET
    mdg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG | Unset = UNSET
    ben: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN | Unset = UNSET
    uzb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB | Unset = UNSET
    nam: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM | Unset = UNSET
    bwa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA | Unset = UNSET
    mda: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA | Unset = UNSET
    jey: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY | Unset = UNSET
    nic: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC | Unset = UNSET
    sdn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN | Unset = UNSET
    jam: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM | Unset = UNSET
    imn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN | Unset = UNSET
    bfa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA | Unset = UNSET
    mng: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG | Unset = UNSET
    mne: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE | Unset = UNSET
    mco: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO | Unset = UNSET
    tgo: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO | Unset = UNSET
    afg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG | Unset = UNSET
    lby: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY | Unset = UNSET
    xkx: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX | Unset = UNSET
    cym: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM | Unset = UNSET
    mwi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI | Unset = UNSET
    som: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM | Unset = UNSET
    png: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG | Unset = UNSET
    mdv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV | Unset = UNSET
    mli: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI | Unset = UNSET
    gin: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN | Unset = UNSET
    pse: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE | Unset = UNSET
    gab: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB | Unset = UNSET
    lie: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE | Unset = UNSET
    hti: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI | Unset = UNSET
    syr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR | Unset = UNSET
    brb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB | Unset = UNSET
    yem: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM | Unset = UNSET
    ggy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY | Unset = UNSET
    ncl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL | Unset = UNSET
    and_: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND | Unset = UNSET
    sur: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR | Unset = UNSET
    myt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT | Unset = UNSET
    kgz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ | Unset = UNSET
    bhs: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS | Unset = UNSET
    gib: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB | Unset = UNSET
    cog: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG | Unset = UNSET
    fji: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI | Unset = UNSET
    blm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM | Unset = UNSET
    cuw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW | Unset = UNSET
    cub: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB | Unset = UNSET
    sle: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE | Unset = UNSET
    blz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ | Unset = UNSET
    ner: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER | Unset = UNSET
    lbr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR | Unset = UNSET
    vir: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR | Unset = UNSET
    pyf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF | Unset = UNSET
    gum: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM | Unset = UNSET
    mrt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT | Unset = UNSET
    abw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW | Unset = UNSET
    syc: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC | Unset = UNSET
    guy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY | Unset = UNSET
    lso: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO | Unset = UNSET
    swz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ | Unset = UNSET
    ssd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD | Unset = UNSET
    lca: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA | Unset = UNSET
    mac: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC | Unset = UNSET
    smr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR | Unset = UNSET
    lao: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO | Unset = UNSET
    brn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN | Unset = UNSET
    tcd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD | Unset = UNSET
    bmu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU | Unset = UNSET
    vgb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB | Unset = UNSET
    prk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK | Unset = UNSET
    btn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN | Unset = UNSET
    bdi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI | Unset = UNSET
    fro: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO | Unset = UNSET
    tjk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK | Unset = UNSET
    gmb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB | Unset = UNSET
    stp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP | Unset = UNSET
    ant: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT | Unset = UNSET
    vct: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT | Unset = UNSET
    dji: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI | Unset = UNSET
    cpv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV | Unset = UNSET
    tkm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM | Unset = UNSET
    atg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG | Unset = UNSET
    tca: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA | Unset = UNSET
    kna: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA | Unset = UNSET
    grd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD | Unset = UNSET
    asm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM | Unset = UNSET
    vut: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT | Unset = UNSET
    gnq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ | Unset = UNSET
    grl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL | Unset = UNSET
    sxm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM | Unset = UNSET
    mnp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP | Unset = UNSET
    com: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM | Unset = UNSET
    tls: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS | Unset = UNSET
    sjm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM | Unset = UNSET
    caf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF | Unset = UNSET
    dma: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA | Unset = UNSET
    maf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF | Unset = UNSET
    wsm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM | Unset = UNSET
    bes: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES | Unset = UNSET
    mhl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL | Unset = UNSET
    aia: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA | Unset = UNSET
    ton: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON | Unset = UNSET
    cok: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK | Unset = UNSET
    slb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB | Unset = UNSET
    spm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM | Unset = UNSET
    gnb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB | Unset = UNSET
    ata: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA | Unset = UNSET
    tuv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV | Unset = UNSET
    ala: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA | Unset = UNSET
    iot: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT | Unset = UNSET
    eri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI | Unset = UNSET
    plw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW | Unset = UNSET
    fsm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM | Unset = UNSET
    nru: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU | Unset = UNSET
    pcn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN | Unset = UNSET
    flk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK | Unset = UNSET
    msr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR | Unset = UNSET
    vat: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT | Unset = UNSET
    kir: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR | Unset = UNSET
    shn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN | Unset = UNSET
    niu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU | Unset = UNSET
    wlf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF | Unset = UNSET
    hmd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD | Unset = UNSET
    cxr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR | Unset = UNSET
    nfk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK | Unset = UNSET
    atf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF | Unset = UNSET
    cck: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK | Unset = UNSET
    sgs: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS | Unset = UNSET
    bvt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT | Unset = UNSET
    umi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI | Unset = UNSET
    esh: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH | Unset = UNSET
    tkl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0per import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0png import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0som import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE,
        )

        usa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usa, Unset):
            usa = self.usa.to_dict()

        gbr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gbr, Unset):
            gbr = self.gbr.to_dict()

        fra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fra, Unset):
            fra = self.fra.to_dict()

        ind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ind, Unset):
            ind = self.ind.to_dict()

        bra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bra, Unset):
            bra = self.bra.to_dict()

        deu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deu, Unset):
            deu = self.deu.to_dict()

        esp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.esp, Unset):
            esp = self.esp.to_dict()

        can: dict[str, Any] | Unset = UNSET
        if not isinstance(self.can, Unset):
            can = self.can.to_dict()

        aus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aus, Unset):
            aus = self.aus.to_dict()

        nld: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nld, Unset):
            nld = self.nld.to_dict()

        ita: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ita, Unset):
            ita = self.ita.to_dict()

        zaf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zaf, Unset):
            zaf = self.zaf.to_dict()

        bel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bel, Unset):
            bel = self.bel.to_dict()

        chn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chn, Unset):
            chn = self.chn.to_dict()

        tur: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tur, Unset):
            tur = self.tur.to_dict()

        mex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mex, Unset):
            mex = self.mex.to_dict()

        che: dict[str, Any] | Unset = UNSET
        if not isinstance(self.che, Unset):
            che = self.che.to_dict()

        nor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nor, Unset):
            nor = self.nor.to_dict()

        are: dict[str, Any] | Unset = UNSET
        if not isinstance(self.are, Unset):
            are = self.are.to_dict()

        swe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.swe, Unset):
            swe = self.swe.to_dict()

        pol: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pol, Unset):
            pol = self.pol.to_dict()

        idn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.idn, Unset):
            idn = self.idn.to_dict()

        arg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arg, Unset):
            arg = self.arg.to_dict()

        prt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prt, Unset):
            prt = self.prt.to_dict()

        col: dict[str, Any] | Unset = UNSET
        if not isinstance(self.col, Unset):
            col = self.col.to_dict()

        chl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chl, Unset):
            chl = self.chl.to_dict()

        pak: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pak, Unset):
            pak = self.pak.to_dict()

        dnk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnk, Unset):
            dnk = self.dnk.to_dict()

        jpn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jpn, Unset):
            jpn = self.jpn.to_dict()

        nga: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nga, Unset):
            nga = self.nga.to_dict()

        sgp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sgp, Unset):
            sgp = self.sgp.to_dict()

        per: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.to_dict()

        nzl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nzl, Unset):
            nzl = self.nzl.to_dict()

        aut: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aut, Unset):
            aut = self.aut.to_dict()

        irl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.irl, Unset):
            irl = self.irl.to_dict()

        mys: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mys, Unset):
            mys = self.mys.to_dict()

        bgd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bgd, Unset):
            bgd = self.bgd.to_dict()

        egy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.egy, Unset):
            egy = self.egy.to_dict()

        isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isr, Unset):
            isr = self.isr.to_dict()

        sau: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sau, Unset):
            sau = self.sau.to_dict()

        phl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phl, Unset):
            phl = self.phl.to_dict()

        fin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fin, Unset):
            fin = self.fin.to_dict()

        irn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.irn, Unset):
            irn = self.irn.to_dict()

        rou: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rou, Unset):
            rou = self.rou.to_dict()

        cze: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cze, Unset):
            cze = self.cze.to_dict()

        grc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grc, Unset):
            grc = self.grc.to_dict()

        hkg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hkg, Unset):
            hkg = self.hkg.to_dict()

        hun: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hun, Unset):
            hun = self.hun.to_dict()

        ken: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ken, Unset):
            ken = self.ken.to_dict()

        mar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mar, Unset):
            mar = self.mar.to_dict()

        vnm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vnm, Unset):
            vnm = self.vnm.to_dict()

        rus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rus, Unset):
            rus = self.rus.to_dict()

        ukr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ukr, Unset):
            ukr = self.ukr.to_dict()

        ecu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ecu, Unset):
            ecu = self.ecu.to_dict()

        tha: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tha, Unset):
            tha = self.tha.to_dict()

        lka: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lka, Unset):
            lka = self.lka.to_dict()

        kor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kor, Unset):
            kor = self.kor.to_dict()

        bgr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bgr, Unset):
            bgr = self.bgr.to_dict()

        gha: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gha, Unset):
            gha = self.gha.to_dict()

        srb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.srb, Unset):
            srb = self.srb.to_dict()

        twn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.twn, Unset):
            twn = self.twn.to_dict()

        hrv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hrv, Unset):
            hrv = self.hrv.to_dict()

        ltu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ltu, Unset):
            ltu = self.ltu.to_dict()

        pri: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pri, Unset):
            pri = self.pri.to_dict()

        svk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.svk, Unset):
            svk = self.svk.to_dict()

        tun: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tun, Unset):
            tun = self.tun.to_dict()

        est: dict[str, Any] | Unset = UNSET
        if not isinstance(self.est, Unset):
            est = self.est.to_dict()

        ven: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ven, Unset):
            ven = self.ven.to_dict()

        cri: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cri, Unset):
            cri = self.cri.to_dict()

        pan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pan, Unset):
            pan = self.pan.to_dict()

        ury: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ury, Unset):
            ury = self.ury.to_dict()

        lbn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lbn, Unset):
            lbn = self.lbn.to_dict()

        lux: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lux, Unset):
            lux = self.lux.to_dict()

        cyp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cyp, Unset):
            cyp = self.cyp.to_dict()

        npl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.npl, Unset):
            npl = self.npl.to_dict()

        jor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jor, Unset):
            jor = self.jor.to_dict()

        svn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.svn, Unset):
            svn = self.svn.to_dict()

        mtq: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mtq, Unset):
            mtq = self.mtq.to_dict()

        qat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qat, Unset):
            qat = self.qat.to_dict()

        glp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.glp, Unset):
            glp = self.glp.to_dict()

        uga: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uga, Unset):
            uga = self.uga.to_dict()

        dza: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dza, Unset):
            dza = self.dza.to_dict()

        gtm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gtm, Unset):
            gtm = self.gtm.to_dict()

        cmr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cmr, Unset):
            cmr = self.cmr.to_dict()

        lva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lva, Unset):
            lva = self.lva.to_dict()

        dom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dom, Unset):
            dom = self.dom.to_dict()

        aze: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aze, Unset):
            aze = self.aze.to_dict()

        geo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geo, Unset):
            geo = self.geo.to_dict()

        sen: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sen, Unset):
            sen = self.sen.to_dict()

        tza: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tza, Unset):
            tza = self.tza.to_dict()

        zwe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zwe, Unset):
            zwe = self.zwe.to_dict()

        kwt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kwt, Unset):
            kwt = self.kwt.to_dict()

        mlt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlt, Unset):
            mlt = self.mlt.to_dict()

        omn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.omn, Unset):
            omn = self.omn.to_dict()

        bol: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bol, Unset):
            bol = self.bol.to_dict()

        slv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slv, Unset):
            slv = self.slv.to_dict()

        arm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arm, Unset):
            arm = self.arm.to_dict()

        pry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pry, Unset):
            pry = self.pry.to_dict()

        irq: dict[str, Any] | Unset = UNSET
        if not isinstance(self.irq, Unset):
            irq = self.irq.to_dict()

        khm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.khm, Unset):
            khm = self.khm.to_dict()

        bih: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bih, Unset):
            bih = self.bih.to_dict()

        ago: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ago, Unset):
            ago = self.ago.to_dict()

        bhr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bhr, Unset):
            bhr = self.bhr.to_dict()

        alb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alb, Unset):
            alb = self.alb.to_dict()

        kaz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kaz, Unset):
            kaz = self.kaz.to_dict()

        civ: dict[str, Any] | Unset = UNSET
        if not isinstance(self.civ, Unset):
            civ = self.civ.to_dict()

        eth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eth, Unset):
            eth = self.eth.to_dict()

        mus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mus, Unset):
            mus = self.mus.to_dict()

        zmb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.zmb, Unset):
            zmb = self.zmb.to_dict()

        mkd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mkd, Unset):
            mkd = self.mkd.to_dict()

        cod: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cod, Unset):
            cod = self.cod.to_dict()

        blr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blr, Unset):
            blr = self.blr.to_dict()

        moz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moz, Unset):
            moz = self.moz.to_dict()

        reu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reu, Unset):
            reu = self.reu.to_dict()

        tto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tto, Unset):
            tto = self.tto.to_dict()

        guf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guf, Unset):
            guf = self.guf.to_dict()

        isl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isl, Unset):
            isl = self.isl.to_dict()

        mmr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mmr, Unset):
            mmr = self.mmr.to_dict()

        hnd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hnd, Unset):
            hnd = self.hnd.to_dict()

        rwa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rwa, Unset):
            rwa = self.rwa.to_dict()

        mdg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mdg, Unset):
            mdg = self.mdg.to_dict()

        ben: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ben, Unset):
            ben = self.ben.to_dict()

        uzb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uzb, Unset):
            uzb = self.uzb.to_dict()

        nam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nam, Unset):
            nam = self.nam.to_dict()

        bwa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bwa, Unset):
            bwa = self.bwa.to_dict()

        mda: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mda, Unset):
            mda = self.mda.to_dict()

        jey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jey, Unset):
            jey = self.jey.to_dict()

        nic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nic, Unset):
            nic = self.nic.to_dict()

        sdn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sdn, Unset):
            sdn = self.sdn.to_dict()

        jam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jam, Unset):
            jam = self.jam.to_dict()

        imn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.imn, Unset):
            imn = self.imn.to_dict()

        bfa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bfa, Unset):
            bfa = self.bfa.to_dict()

        mng: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mng, Unset):
            mng = self.mng.to_dict()

        mne: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mne, Unset):
            mne = self.mne.to_dict()

        mco: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mco, Unset):
            mco = self.mco.to_dict()

        tgo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tgo, Unset):
            tgo = self.tgo.to_dict()

        afg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.afg, Unset):
            afg = self.afg.to_dict()

        lby: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lby, Unset):
            lby = self.lby.to_dict()

        xkx: dict[str, Any] | Unset = UNSET
        if not isinstance(self.xkx, Unset):
            xkx = self.xkx.to_dict()

        cym: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cym, Unset):
            cym = self.cym.to_dict()

        mwi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mwi, Unset):
            mwi = self.mwi.to_dict()

        som: dict[str, Any] | Unset = UNSET
        if not isinstance(self.som, Unset):
            som = self.som.to_dict()

        png: dict[str, Any] | Unset = UNSET
        if not isinstance(self.png, Unset):
            png = self.png.to_dict()

        mdv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mdv, Unset):
            mdv = self.mdv.to_dict()

        mli: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mli, Unset):
            mli = self.mli.to_dict()

        gin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gin, Unset):
            gin = self.gin.to_dict()

        pse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pse, Unset):
            pse = self.pse.to_dict()

        gab: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gab, Unset):
            gab = self.gab.to_dict()

        lie: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lie, Unset):
            lie = self.lie.to_dict()

        hti: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hti, Unset):
            hti = self.hti.to_dict()

        syr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.syr, Unset):
            syr = self.syr.to_dict()

        brb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brb, Unset):
            brb = self.brb.to_dict()

        yem: dict[str, Any] | Unset = UNSET
        if not isinstance(self.yem, Unset):
            yem = self.yem.to_dict()

        ggy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ggy, Unset):
            ggy = self.ggy.to_dict()

        ncl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ncl, Unset):
            ncl = self.ncl.to_dict()

        and_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.and_, Unset):
            and_ = self.and_.to_dict()

        sur: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sur, Unset):
            sur = self.sur.to_dict()

        myt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.myt, Unset):
            myt = self.myt.to_dict()

        kgz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kgz, Unset):
            kgz = self.kgz.to_dict()

        bhs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bhs, Unset):
            bhs = self.bhs.to_dict()

        gib: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gib, Unset):
            gib = self.gib.to_dict()

        cog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cog, Unset):
            cog = self.cog.to_dict()

        fji: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fji, Unset):
            fji = self.fji.to_dict()

        blm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blm, Unset):
            blm = self.blm.to_dict()

        cuw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cuw, Unset):
            cuw = self.cuw.to_dict()

        cub: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cub, Unset):
            cub = self.cub.to_dict()

        sle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sle, Unset):
            sle = self.sle.to_dict()

        blz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blz, Unset):
            blz = self.blz.to_dict()

        ner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ner, Unset):
            ner = self.ner.to_dict()

        lbr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lbr, Unset):
            lbr = self.lbr.to_dict()

        vir: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vir, Unset):
            vir = self.vir.to_dict()

        pyf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pyf, Unset):
            pyf = self.pyf.to_dict()

        gum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gum, Unset):
            gum = self.gum.to_dict()

        mrt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mrt, Unset):
            mrt = self.mrt.to_dict()

        abw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abw, Unset):
            abw = self.abw.to_dict()

        syc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.syc, Unset):
            syc = self.syc.to_dict()

        guy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guy, Unset):
            guy = self.guy.to_dict()

        lso: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lso, Unset):
            lso = self.lso.to_dict()

        swz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.swz, Unset):
            swz = self.swz.to_dict()

        ssd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssd, Unset):
            ssd = self.ssd.to_dict()

        lca: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lca, Unset):
            lca = self.lca.to_dict()

        mac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac, Unset):
            mac = self.mac.to_dict()

        smr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smr, Unset):
            smr = self.smr.to_dict()

        lao: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lao, Unset):
            lao = self.lao.to_dict()

        brn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brn, Unset):
            brn = self.brn.to_dict()

        tcd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcd, Unset):
            tcd = self.tcd.to_dict()

        bmu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bmu, Unset):
            bmu = self.bmu.to_dict()

        vgb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vgb, Unset):
            vgb = self.vgb.to_dict()

        prk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prk, Unset):
            prk = self.prk.to_dict()

        btn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.btn, Unset):
            btn = self.btn.to_dict()

        bdi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bdi, Unset):
            bdi = self.bdi.to_dict()

        fro: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fro, Unset):
            fro = self.fro.to_dict()

        tjk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tjk, Unset):
            tjk = self.tjk.to_dict()

        gmb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmb, Unset):
            gmb = self.gmb.to_dict()

        stp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stp, Unset):
            stp = self.stp.to_dict()

        ant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ant, Unset):
            ant = self.ant.to_dict()

        vct: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vct, Unset):
            vct = self.vct.to_dict()

        dji: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dji, Unset):
            dji = self.dji.to_dict()

        cpv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpv, Unset):
            cpv = self.cpv.to_dict()

        tkm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tkm, Unset):
            tkm = self.tkm.to_dict()

        atg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.atg, Unset):
            atg = self.atg.to_dict()

        tca: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tca, Unset):
            tca = self.tca.to_dict()

        kna: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kna, Unset):
            kna = self.kna.to_dict()

        grd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grd, Unset):
            grd = self.grd.to_dict()

        asm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asm, Unset):
            asm = self.asm.to_dict()

        vut: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vut, Unset):
            vut = self.vut.to_dict()

        gnq: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gnq, Unset):
            gnq = self.gnq.to_dict()

        grl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grl, Unset):
            grl = self.grl.to_dict()

        sxm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sxm, Unset):
            sxm = self.sxm.to_dict()

        mnp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mnp, Unset):
            mnp = self.mnp.to_dict()

        com: dict[str, Any] | Unset = UNSET
        if not isinstance(self.com, Unset):
            com = self.com.to_dict()

        tls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tls, Unset):
            tls = self.tls.to_dict()

        sjm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sjm, Unset):
            sjm = self.sjm.to_dict()

        caf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.caf, Unset):
            caf = self.caf.to_dict()

        dma: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dma, Unset):
            dma = self.dma.to_dict()

        maf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maf, Unset):
            maf = self.maf.to_dict()

        wsm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wsm, Unset):
            wsm = self.wsm.to_dict()

        bes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bes, Unset):
            bes = self.bes.to_dict()

        mhl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mhl, Unset):
            mhl = self.mhl.to_dict()

        aia: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aia, Unset):
            aia = self.aia.to_dict()

        ton: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ton, Unset):
            ton = self.ton.to_dict()

        cok: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cok, Unset):
            cok = self.cok.to_dict()

        slb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slb, Unset):
            slb = self.slb.to_dict()

        spm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spm, Unset):
            spm = self.spm.to_dict()

        gnb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gnb, Unset):
            gnb = self.gnb.to_dict()

        ata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ata, Unset):
            ata = self.ata.to_dict()

        tuv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tuv, Unset):
            tuv = self.tuv.to_dict()

        ala: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ala, Unset):
            ala = self.ala.to_dict()

        iot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.iot, Unset):
            iot = self.iot.to_dict()

        eri: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eri, Unset):
            eri = self.eri.to_dict()

        plw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plw, Unset):
            plw = self.plw.to_dict()

        fsm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fsm, Unset):
            fsm = self.fsm.to_dict()

        nru: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nru, Unset):
            nru = self.nru.to_dict()

        pcn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pcn, Unset):
            pcn = self.pcn.to_dict()

        flk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flk, Unset):
            flk = self.flk.to_dict()

        msr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.msr, Unset):
            msr = self.msr.to_dict()

        vat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vat, Unset):
            vat = self.vat.to_dict()

        kir: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kir, Unset):
            kir = self.kir.to_dict()

        shn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shn, Unset):
            shn = self.shn.to_dict()

        niu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.niu, Unset):
            niu = self.niu.to_dict()

        wlf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlf, Unset):
            wlf = self.wlf.to_dict()

        hmd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hmd, Unset):
            hmd = self.hmd.to_dict()

        cxr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cxr, Unset):
            cxr = self.cxr.to_dict()

        nfk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nfk, Unset):
            nfk = self.nfk.to_dict()

        atf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.atf, Unset):
            atf = self.atf.to_dict()

        cck: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cck, Unset):
            cck = self.cck.to_dict()

        sgs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sgs, Unset):
            sgs = self.sgs.to_dict()

        bvt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bvt, Unset):
            bvt = self.bvt.to_dict()

        umi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.umi, Unset):
            umi = self.umi.to_dict()

        esh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.esh, Unset):
            esh = self.esh.to_dict()

        tkl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tkl, Unset):
            tkl = self.tkl.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if usa is not UNSET:
            field_dict["USA"] = usa
        if gbr is not UNSET:
            field_dict["GBR"] = gbr
        if fra is not UNSET:
            field_dict["FRA"] = fra
        if ind is not UNSET:
            field_dict["IND"] = ind
        if bra is not UNSET:
            field_dict["BRA"] = bra
        if deu is not UNSET:
            field_dict["DEU"] = deu
        if esp is not UNSET:
            field_dict["ESP"] = esp
        if can is not UNSET:
            field_dict["CAN"] = can
        if aus is not UNSET:
            field_dict["AUS"] = aus
        if nld is not UNSET:
            field_dict["NLD"] = nld
        if ita is not UNSET:
            field_dict["ITA"] = ita
        if zaf is not UNSET:
            field_dict["ZAF"] = zaf
        if bel is not UNSET:
            field_dict["BEL"] = bel
        if chn is not UNSET:
            field_dict["CHN"] = chn
        if tur is not UNSET:
            field_dict["TUR"] = tur
        if mex is not UNSET:
            field_dict["MEX"] = mex
        if che is not UNSET:
            field_dict["CHE"] = che
        if nor is not UNSET:
            field_dict["NOR"] = nor
        if are is not UNSET:
            field_dict["ARE"] = are
        if swe is not UNSET:
            field_dict["SWE"] = swe
        if pol is not UNSET:
            field_dict["POL"] = pol
        if idn is not UNSET:
            field_dict["IDN"] = idn
        if arg is not UNSET:
            field_dict["ARG"] = arg
        if prt is not UNSET:
            field_dict["PRT"] = prt
        if col is not UNSET:
            field_dict["COL"] = col
        if chl is not UNSET:
            field_dict["CHL"] = chl
        if pak is not UNSET:
            field_dict["PAK"] = pak
        if dnk is not UNSET:
            field_dict["DNK"] = dnk
        if jpn is not UNSET:
            field_dict["JPN"] = jpn
        if nga is not UNSET:
            field_dict["NGA"] = nga
        if sgp is not UNSET:
            field_dict["SGP"] = sgp
        if per is not UNSET:
            field_dict["PER"] = per
        if nzl is not UNSET:
            field_dict["NZL"] = nzl
        if aut is not UNSET:
            field_dict["AUT"] = aut
        if irl is not UNSET:
            field_dict["IRL"] = irl
        if mys is not UNSET:
            field_dict["MYS"] = mys
        if bgd is not UNSET:
            field_dict["BGD"] = bgd
        if egy is not UNSET:
            field_dict["EGY"] = egy
        if isr is not UNSET:
            field_dict["ISR"] = isr
        if sau is not UNSET:
            field_dict["SAU"] = sau
        if phl is not UNSET:
            field_dict["PHL"] = phl
        if fin is not UNSET:
            field_dict["FIN"] = fin
        if irn is not UNSET:
            field_dict["IRN"] = irn
        if rou is not UNSET:
            field_dict["ROU"] = rou
        if cze is not UNSET:
            field_dict["CZE"] = cze
        if grc is not UNSET:
            field_dict["GRC"] = grc
        if hkg is not UNSET:
            field_dict["HKG"] = hkg
        if hun is not UNSET:
            field_dict["HUN"] = hun
        if ken is not UNSET:
            field_dict["KEN"] = ken
        if mar is not UNSET:
            field_dict["MAR"] = mar
        if vnm is not UNSET:
            field_dict["VNM"] = vnm
        if rus is not UNSET:
            field_dict["RUS"] = rus
        if ukr is not UNSET:
            field_dict["UKR"] = ukr
        if ecu is not UNSET:
            field_dict["ECU"] = ecu
        if tha is not UNSET:
            field_dict["THA"] = tha
        if lka is not UNSET:
            field_dict["LKA"] = lka
        if kor is not UNSET:
            field_dict["KOR"] = kor
        if bgr is not UNSET:
            field_dict["BGR"] = bgr
        if gha is not UNSET:
            field_dict["GHA"] = gha
        if srb is not UNSET:
            field_dict["SRB"] = srb
        if twn is not UNSET:
            field_dict["TWN"] = twn
        if hrv is not UNSET:
            field_dict["HRV"] = hrv
        if ltu is not UNSET:
            field_dict["LTU"] = ltu
        if pri is not UNSET:
            field_dict["PRI"] = pri
        if svk is not UNSET:
            field_dict["SVK"] = svk
        if tun is not UNSET:
            field_dict["TUN"] = tun
        if est is not UNSET:
            field_dict["EST"] = est
        if ven is not UNSET:
            field_dict["VEN"] = ven
        if cri is not UNSET:
            field_dict["CRI"] = cri
        if pan is not UNSET:
            field_dict["PAN"] = pan
        if ury is not UNSET:
            field_dict["URY"] = ury
        if lbn is not UNSET:
            field_dict["LBN"] = lbn
        if lux is not UNSET:
            field_dict["LUX"] = lux
        if cyp is not UNSET:
            field_dict["CYP"] = cyp
        if npl is not UNSET:
            field_dict["NPL"] = npl
        if jor is not UNSET:
            field_dict["JOR"] = jor
        if svn is not UNSET:
            field_dict["SVN"] = svn
        if mtq is not UNSET:
            field_dict["MTQ"] = mtq
        if qat is not UNSET:
            field_dict["QAT"] = qat
        if glp is not UNSET:
            field_dict["GLP"] = glp
        if uga is not UNSET:
            field_dict["UGA"] = uga
        if dza is not UNSET:
            field_dict["DZA"] = dza
        if gtm is not UNSET:
            field_dict["GTM"] = gtm
        if cmr is not UNSET:
            field_dict["CMR"] = cmr
        if lva is not UNSET:
            field_dict["LVA"] = lva
        if dom is not UNSET:
            field_dict["DOM"] = dom
        if aze is not UNSET:
            field_dict["AZE"] = aze
        if geo is not UNSET:
            field_dict["GEO"] = geo
        if sen is not UNSET:
            field_dict["SEN"] = sen
        if tza is not UNSET:
            field_dict["TZA"] = tza
        if zwe is not UNSET:
            field_dict["ZWE"] = zwe
        if kwt is not UNSET:
            field_dict["KWT"] = kwt
        if mlt is not UNSET:
            field_dict["MLT"] = mlt
        if omn is not UNSET:
            field_dict["OMN"] = omn
        if bol is not UNSET:
            field_dict["BOL"] = bol
        if slv is not UNSET:
            field_dict["SLV"] = slv
        if arm is not UNSET:
            field_dict["ARM"] = arm
        if pry is not UNSET:
            field_dict["PRY"] = pry
        if irq is not UNSET:
            field_dict["IRQ"] = irq
        if khm is not UNSET:
            field_dict["KHM"] = khm
        if bih is not UNSET:
            field_dict["BIH"] = bih
        if ago is not UNSET:
            field_dict["AGO"] = ago
        if bhr is not UNSET:
            field_dict["BHR"] = bhr
        if alb is not UNSET:
            field_dict["ALB"] = alb
        if kaz is not UNSET:
            field_dict["KAZ"] = kaz
        if civ is not UNSET:
            field_dict["CIV"] = civ
        if eth is not UNSET:
            field_dict["ETH"] = eth
        if mus is not UNSET:
            field_dict["MUS"] = mus
        if zmb is not UNSET:
            field_dict["ZMB"] = zmb
        if mkd is not UNSET:
            field_dict["MKD"] = mkd
        if cod is not UNSET:
            field_dict["COD"] = cod
        if blr is not UNSET:
            field_dict["BLR"] = blr
        if moz is not UNSET:
            field_dict["MOZ"] = moz
        if reu is not UNSET:
            field_dict["REU"] = reu
        if tto is not UNSET:
            field_dict["TTO"] = tto
        if guf is not UNSET:
            field_dict["GUF"] = guf
        if isl is not UNSET:
            field_dict["ISL"] = isl
        if mmr is not UNSET:
            field_dict["MMR"] = mmr
        if hnd is not UNSET:
            field_dict["HND"] = hnd
        if rwa is not UNSET:
            field_dict["RWA"] = rwa
        if mdg is not UNSET:
            field_dict["MDG"] = mdg
        if ben is not UNSET:
            field_dict["BEN"] = ben
        if uzb is not UNSET:
            field_dict["UZB"] = uzb
        if nam is not UNSET:
            field_dict["NAM"] = nam
        if bwa is not UNSET:
            field_dict["BWA"] = bwa
        if mda is not UNSET:
            field_dict["MDA"] = mda
        if jey is not UNSET:
            field_dict["JEY"] = jey
        if nic is not UNSET:
            field_dict["NIC"] = nic
        if sdn is not UNSET:
            field_dict["SDN"] = sdn
        if jam is not UNSET:
            field_dict["JAM"] = jam
        if imn is not UNSET:
            field_dict["IMN"] = imn
        if bfa is not UNSET:
            field_dict["BFA"] = bfa
        if mng is not UNSET:
            field_dict["MNG"] = mng
        if mne is not UNSET:
            field_dict["MNE"] = mne
        if mco is not UNSET:
            field_dict["MCO"] = mco
        if tgo is not UNSET:
            field_dict["TGO"] = tgo
        if afg is not UNSET:
            field_dict["AFG"] = afg
        if lby is not UNSET:
            field_dict["LBY"] = lby
        if xkx is not UNSET:
            field_dict["XKX"] = xkx
        if cym is not UNSET:
            field_dict["CYM"] = cym
        if mwi is not UNSET:
            field_dict["MWI"] = mwi
        if som is not UNSET:
            field_dict["SOM"] = som
        if png is not UNSET:
            field_dict["PNG"] = png
        if mdv is not UNSET:
            field_dict["MDV"] = mdv
        if mli is not UNSET:
            field_dict["MLI"] = mli
        if gin is not UNSET:
            field_dict["GIN"] = gin
        if pse is not UNSET:
            field_dict["PSE"] = pse
        if gab is not UNSET:
            field_dict["GAB"] = gab
        if lie is not UNSET:
            field_dict["LIE"] = lie
        if hti is not UNSET:
            field_dict["HTI"] = hti
        if syr is not UNSET:
            field_dict["SYR"] = syr
        if brb is not UNSET:
            field_dict["BRB"] = brb
        if yem is not UNSET:
            field_dict["YEM"] = yem
        if ggy is not UNSET:
            field_dict["GGY"] = ggy
        if ncl is not UNSET:
            field_dict["NCL"] = ncl
        if and_ is not UNSET:
            field_dict["AND"] = and_
        if sur is not UNSET:
            field_dict["SUR"] = sur
        if myt is not UNSET:
            field_dict["MYT"] = myt
        if kgz is not UNSET:
            field_dict["KGZ"] = kgz
        if bhs is not UNSET:
            field_dict["BHS"] = bhs
        if gib is not UNSET:
            field_dict["GIB"] = gib
        if cog is not UNSET:
            field_dict["COG"] = cog
        if fji is not UNSET:
            field_dict["FJI"] = fji
        if blm is not UNSET:
            field_dict["BLM"] = blm
        if cuw is not UNSET:
            field_dict["CUW"] = cuw
        if cub is not UNSET:
            field_dict["CUB"] = cub
        if sle is not UNSET:
            field_dict["SLE"] = sle
        if blz is not UNSET:
            field_dict["BLZ"] = blz
        if ner is not UNSET:
            field_dict["NER"] = ner
        if lbr is not UNSET:
            field_dict["LBR"] = lbr
        if vir is not UNSET:
            field_dict["VIR"] = vir
        if pyf is not UNSET:
            field_dict["PYF"] = pyf
        if gum is not UNSET:
            field_dict["GUM"] = gum
        if mrt is not UNSET:
            field_dict["MRT"] = mrt
        if abw is not UNSET:
            field_dict["ABW"] = abw
        if syc is not UNSET:
            field_dict["SYC"] = syc
        if guy is not UNSET:
            field_dict["GUY"] = guy
        if lso is not UNSET:
            field_dict["LSO"] = lso
        if swz is not UNSET:
            field_dict["SWZ"] = swz
        if ssd is not UNSET:
            field_dict["SSD"] = ssd
        if lca is not UNSET:
            field_dict["LCA"] = lca
        if mac is not UNSET:
            field_dict["MAC"] = mac
        if smr is not UNSET:
            field_dict["SMR"] = smr
        if lao is not UNSET:
            field_dict["LAO"] = lao
        if brn is not UNSET:
            field_dict["BRN"] = brn
        if tcd is not UNSET:
            field_dict["TCD"] = tcd
        if bmu is not UNSET:
            field_dict["BMU"] = bmu
        if vgb is not UNSET:
            field_dict["VGB"] = vgb
        if prk is not UNSET:
            field_dict["PRK"] = prk
        if btn is not UNSET:
            field_dict["BTN"] = btn
        if bdi is not UNSET:
            field_dict["BDI"] = bdi
        if fro is not UNSET:
            field_dict["FRO"] = fro
        if tjk is not UNSET:
            field_dict["TJK"] = tjk
        if gmb is not UNSET:
            field_dict["GMB"] = gmb
        if stp is not UNSET:
            field_dict["STP"] = stp
        if ant is not UNSET:
            field_dict["ANT"] = ant
        if vct is not UNSET:
            field_dict["VCT"] = vct
        if dji is not UNSET:
            field_dict["DJI"] = dji
        if cpv is not UNSET:
            field_dict["CPV"] = cpv
        if tkm is not UNSET:
            field_dict["TKM"] = tkm
        if atg is not UNSET:
            field_dict["ATG"] = atg
        if tca is not UNSET:
            field_dict["TCA"] = tca
        if kna is not UNSET:
            field_dict["KNA"] = kna
        if grd is not UNSET:
            field_dict["GRD"] = grd
        if asm is not UNSET:
            field_dict["ASM"] = asm
        if vut is not UNSET:
            field_dict["VUT"] = vut
        if gnq is not UNSET:
            field_dict["GNQ"] = gnq
        if grl is not UNSET:
            field_dict["GRL"] = grl
        if sxm is not UNSET:
            field_dict["SXM"] = sxm
        if mnp is not UNSET:
            field_dict["MNP"] = mnp
        if com is not UNSET:
            field_dict["COM"] = com
        if tls is not UNSET:
            field_dict["TLS"] = tls
        if sjm is not UNSET:
            field_dict["SJM"] = sjm
        if caf is not UNSET:
            field_dict["CAF"] = caf
        if dma is not UNSET:
            field_dict["DMA"] = dma
        if maf is not UNSET:
            field_dict["MAF"] = maf
        if wsm is not UNSET:
            field_dict["WSM"] = wsm
        if bes is not UNSET:
            field_dict["BES"] = bes
        if mhl is not UNSET:
            field_dict["MHL"] = mhl
        if aia is not UNSET:
            field_dict["AIA"] = aia
        if ton is not UNSET:
            field_dict["TON"] = ton
        if cok is not UNSET:
            field_dict["COK"] = cok
        if slb is not UNSET:
            field_dict["SLB"] = slb
        if spm is not UNSET:
            field_dict["SPM"] = spm
        if gnb is not UNSET:
            field_dict["GNB"] = gnb
        if ata is not UNSET:
            field_dict["ATA"] = ata
        if tuv is not UNSET:
            field_dict["TUV"] = tuv
        if ala is not UNSET:
            field_dict["ALA"] = ala
        if iot is not UNSET:
            field_dict["IOT"] = iot
        if eri is not UNSET:
            field_dict["ERI"] = eri
        if plw is not UNSET:
            field_dict["PLW"] = plw
        if fsm is not UNSET:
            field_dict["FSM"] = fsm
        if nru is not UNSET:
            field_dict["NRU"] = nru
        if pcn is not UNSET:
            field_dict["PCN"] = pcn
        if flk is not UNSET:
            field_dict["FLK"] = flk
        if msr is not UNSET:
            field_dict["MSR"] = msr
        if vat is not UNSET:
            field_dict["VAT"] = vat
        if kir is not UNSET:
            field_dict["KIR"] = kir
        if shn is not UNSET:
            field_dict["SHN"] = shn
        if niu is not UNSET:
            field_dict["NIU"] = niu
        if wlf is not UNSET:
            field_dict["WLF"] = wlf
        if hmd is not UNSET:
            field_dict["HMD"] = hmd
        if cxr is not UNSET:
            field_dict["CXR"] = cxr
        if nfk is not UNSET:
            field_dict["NFK"] = nfk
        if atf is not UNSET:
            field_dict["ATF"] = atf
        if cck is not UNSET:
            field_dict["CCK"] = cck
        if sgs is not UNSET:
            field_dict["SGS"] = sgs
        if bvt is not UNSET:
            field_dict["BVT"] = bvt
        if umi is not UNSET:
            field_dict["UMI"] = umi
        if esh is not UNSET:
            field_dict["ESH"] = esh
        if tkl is not UNSET:
            field_dict["TKL"] = tkl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0abw import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0afg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ago import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aia import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ala import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0alb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0and import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ant import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0are import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0arg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0arm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0asm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ata import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0atf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0atg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aus import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aut import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0aze import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bdi import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bel import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ben import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bes import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bfa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bgd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bgr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bhr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bhs import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bih import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0blz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bmu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bol import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bra import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0brb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0brn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0btn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bvt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0bwa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0caf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0can import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cck import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0che import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0chl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0chn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0civ import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cmr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cod import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cog import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cok import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0col import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0com import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cpv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cri import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cub import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cuw import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cxr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cym import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cyp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0cze import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0deu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dji import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dma import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dnk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dom import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0dza import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ecu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0egy import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0eri import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0esh import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0esp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0est import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0eth import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fin import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fji import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0flk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fra import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fro import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0fsm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gab import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gbr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0geo import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ggy import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gha import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gib import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gin import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0glp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gmb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gnb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gnq import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grc import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0grl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gtm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0guf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0gum import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0guy import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hkg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hmd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hnd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0per import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0png import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0som import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
            KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE,
        )

        d = dict(src_dict)
        _usa = d.pop("USA", UNSET)
        usa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA | Unset
        if isinstance(_usa, Unset):
            usa = UNSET
        else:
            usa = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0USA.from_dict(
                _usa
            )

        _gbr = d.pop("GBR", UNSET)
        gbr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR | Unset
        if isinstance(_gbr, Unset):
            gbr = UNSET
        else:
            gbr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GBR.from_dict(
                _gbr
            )

        _fra = d.pop("FRA", UNSET)
        fra: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA | Unset
        if isinstance(_fra, Unset):
            fra = UNSET
        else:
            fra = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRA.from_dict(
                _fra
            )

        _ind = d.pop("IND", UNSET)
        ind: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND | Unset
        if isinstance(_ind, Unset):
            ind = UNSET
        else:
            ind = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IND.from_dict(
                _ind
            )

        _bra = d.pop("BRA", UNSET)
        bra: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA | Unset
        if isinstance(_bra, Unset):
            bra = UNSET
        else:
            bra = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRA.from_dict(
                _bra
            )

        _deu = d.pop("DEU", UNSET)
        deu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU | Unset
        if isinstance(_deu, Unset):
            deu = UNSET
        else:
            deu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DEU.from_dict(
                _deu
            )

        _esp = d.pop("ESP", UNSET)
        esp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP | Unset
        if isinstance(_esp, Unset):
            esp = UNSET
        else:
            esp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESP.from_dict(
                _esp
            )

        _can = d.pop("CAN", UNSET)
        can: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN | Unset
        if isinstance(_can, Unset):
            can = UNSET
        else:
            can = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAN.from_dict(
                _can
            )

        _aus = d.pop("AUS", UNSET)
        aus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS | Unset
        if isinstance(_aus, Unset):
            aus = UNSET
        else:
            aus = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUS.from_dict(
                _aus
            )

        _nld = d.pop("NLD", UNSET)
        nld: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD | Unset
        if isinstance(_nld, Unset):
            nld = UNSET
        else:
            nld = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NLD.from_dict(
                _nld
            )

        _ita = d.pop("ITA", UNSET)
        ita: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA | Unset
        if isinstance(_ita, Unset):
            ita = UNSET
        else:
            ita = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ITA.from_dict(
                _ita
            )

        _zaf = d.pop("ZAF", UNSET)
        zaf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF | Unset
        if isinstance(_zaf, Unset):
            zaf = UNSET
        else:
            zaf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZAF.from_dict(
                _zaf
            )

        _bel = d.pop("BEL", UNSET)
        bel: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL | Unset
        if isinstance(_bel, Unset):
            bel = UNSET
        else:
            bel = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEL.from_dict(
                _bel
            )

        _chn = d.pop("CHN", UNSET)
        chn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN | Unset
        if isinstance(_chn, Unset):
            chn = UNSET
        else:
            chn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHN.from_dict(
                _chn
            )

        _tur = d.pop("TUR", UNSET)
        tur: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR | Unset
        if isinstance(_tur, Unset):
            tur = UNSET
        else:
            tur = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUR.from_dict(
                _tur
            )

        _mex = d.pop("MEX", UNSET)
        mex: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX | Unset
        if isinstance(_mex, Unset):
            mex = UNSET
        else:
            mex = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MEX.from_dict(
                _mex
            )

        _che = d.pop("CHE", UNSET)
        che: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE | Unset
        if isinstance(_che, Unset):
            che = UNSET
        else:
            che = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHE.from_dict(
                _che
            )

        _nor = d.pop("NOR", UNSET)
        nor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR | Unset
        if isinstance(_nor, Unset):
            nor = UNSET
        else:
            nor = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NOR.from_dict(
                _nor
            )

        _are = d.pop("ARE", UNSET)
        are: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE | Unset
        if isinstance(_are, Unset):
            are = UNSET
        else:
            are = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARE.from_dict(
                _are
            )

        _swe = d.pop("SWE", UNSET)
        swe: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE | Unset
        if isinstance(_swe, Unset):
            swe = UNSET
        else:
            swe = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWE.from_dict(
                _swe
            )

        _pol = d.pop("POL", UNSET)
        pol: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL | Unset
        if isinstance(_pol, Unset):
            pol = UNSET
        else:
            pol = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0POL.from_dict(
                _pol
            )

        _idn = d.pop("IDN", UNSET)
        idn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN | Unset
        if isinstance(_idn, Unset):
            idn = UNSET
        else:
            idn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IDN.from_dict(
                _idn
            )

        _arg = d.pop("ARG", UNSET)
        arg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG | Unset
        if isinstance(_arg, Unset):
            arg = UNSET
        else:
            arg = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARG.from_dict(
                _arg
            )

        _prt = d.pop("PRT", UNSET)
        prt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT | Unset
        if isinstance(_prt, Unset):
            prt = UNSET
        else:
            prt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRT.from_dict(
                _prt
            )

        _col = d.pop("COL", UNSET)
        col: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL | Unset
        if isinstance(_col, Unset):
            col = UNSET
        else:
            col = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COL.from_dict(
                _col
            )

        _chl = d.pop("CHL", UNSET)
        chl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL | Unset
        if isinstance(_chl, Unset):
            chl = UNSET
        else:
            chl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CHL.from_dict(
                _chl
            )

        _pak = d.pop("PAK", UNSET)
        pak: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK | Unset
        if isinstance(_pak, Unset):
            pak = UNSET
        else:
            pak = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAK.from_dict(
                _pak
            )

        _dnk = d.pop("DNK", UNSET)
        dnk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK | Unset
        if isinstance(_dnk, Unset):
            dnk = UNSET
        else:
            dnk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DNK.from_dict(
                _dnk
            )

        _jpn = d.pop("JPN", UNSET)
        jpn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN | Unset
        if isinstance(_jpn, Unset):
            jpn = UNSET
        else:
            jpn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JPN.from_dict(
                _jpn
            )

        _nga = d.pop("NGA", UNSET)
        nga: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA | Unset
        if isinstance(_nga, Unset):
            nga = UNSET
        else:
            nga = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NGA.from_dict(
                _nga
            )

        _sgp = d.pop("SGP", UNSET)
        sgp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP | Unset
        if isinstance(_sgp, Unset):
            sgp = UNSET
        else:
            sgp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGP.from_dict(
                _sgp
            )

        _per = d.pop("PER", UNSET)
        per: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PER.from_dict(
                _per
            )

        _nzl = d.pop("NZL", UNSET)
        nzl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL | Unset
        if isinstance(_nzl, Unset):
            nzl = UNSET
        else:
            nzl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NZL.from_dict(
                _nzl
            )

        _aut = d.pop("AUT", UNSET)
        aut: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT | Unset
        if isinstance(_aut, Unset):
            aut = UNSET
        else:
            aut = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AUT.from_dict(
                _aut
            )

        _irl = d.pop("IRL", UNSET)
        irl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL | Unset
        if isinstance(_irl, Unset):
            irl = UNSET
        else:
            irl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRL.from_dict(
                _irl
            )

        _mys = d.pop("MYS", UNSET)
        mys: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS | Unset
        if isinstance(_mys, Unset):
            mys = UNSET
        else:
            mys = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYS.from_dict(
                _mys
            )

        _bgd = d.pop("BGD", UNSET)
        bgd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD | Unset
        if isinstance(_bgd, Unset):
            bgd = UNSET
        else:
            bgd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGD.from_dict(
                _bgd
            )

        _egy = d.pop("EGY", UNSET)
        egy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY | Unset
        if isinstance(_egy, Unset):
            egy = UNSET
        else:
            egy = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EGY.from_dict(
                _egy
            )

        _isr = d.pop("ISR", UNSET)
        isr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR | Unset
        if isinstance(_isr, Unset):
            isr = UNSET
        else:
            isr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISR.from_dict(
                _isr
            )

        _sau = d.pop("SAU", UNSET)
        sau: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU | Unset
        if isinstance(_sau, Unset):
            sau = UNSET
        else:
            sau = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SAU.from_dict(
                _sau
            )

        _phl = d.pop("PHL", UNSET)
        phl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL | Unset
        if isinstance(_phl, Unset):
            phl = UNSET
        else:
            phl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PHL.from_dict(
                _phl
            )

        _fin = d.pop("FIN", UNSET)
        fin: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN | Unset
        if isinstance(_fin, Unset):
            fin = UNSET
        else:
            fin = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FIN.from_dict(
                _fin
            )

        _irn = d.pop("IRN", UNSET)
        irn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN | Unset
        if isinstance(_irn, Unset):
            irn = UNSET
        else:
            irn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRN.from_dict(
                _irn
            )

        _rou = d.pop("ROU", UNSET)
        rou: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU | Unset
        if isinstance(_rou, Unset):
            rou = UNSET
        else:
            rou = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ROU.from_dict(
                _rou
            )

        _cze = d.pop("CZE", UNSET)
        cze: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE | Unset
        if isinstance(_cze, Unset):
            cze = UNSET
        else:
            cze = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CZE.from_dict(
                _cze
            )

        _grc = d.pop("GRC", UNSET)
        grc: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC | Unset
        if isinstance(_grc, Unset):
            grc = UNSET
        else:
            grc = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRC.from_dict(
                _grc
            )

        _hkg = d.pop("HKG", UNSET)
        hkg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG | Unset
        if isinstance(_hkg, Unset):
            hkg = UNSET
        else:
            hkg = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HKG.from_dict(
                _hkg
            )

        _hun = d.pop("HUN", UNSET)
        hun: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN | Unset
        if isinstance(_hun, Unset):
            hun = UNSET
        else:
            hun = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HUN.from_dict(
                _hun
            )

        _ken = d.pop("KEN", UNSET)
        ken: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN | Unset
        if isinstance(_ken, Unset):
            ken = UNSET
        else:
            ken = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KEN.from_dict(
                _ken
            )

        _mar = d.pop("MAR", UNSET)
        mar: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR | Unset
        if isinstance(_mar, Unset):
            mar = UNSET
        else:
            mar = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAR.from_dict(
                _mar
            )

        _vnm = d.pop("VNM", UNSET)
        vnm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM | Unset
        if isinstance(_vnm, Unset):
            vnm = UNSET
        else:
            vnm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VNM.from_dict(
                _vnm
            )

        _rus = d.pop("RUS", UNSET)
        rus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS | Unset
        if isinstance(_rus, Unset):
            rus = UNSET
        else:
            rus = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RUS.from_dict(
                _rus
            )

        _ukr = d.pop("UKR", UNSET)
        ukr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR | Unset
        if isinstance(_ukr, Unset):
            ukr = UNSET
        else:
            ukr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UKR.from_dict(
                _ukr
            )

        _ecu = d.pop("ECU", UNSET)
        ecu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU | Unset
        if isinstance(_ecu, Unset):
            ecu = UNSET
        else:
            ecu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ECU.from_dict(
                _ecu
            )

        _tha = d.pop("THA", UNSET)
        tha: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA | Unset
        if isinstance(_tha, Unset):
            tha = UNSET
        else:
            tha = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0THA.from_dict(
                _tha
            )

        _lka = d.pop("LKA", UNSET)
        lka: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA | Unset
        if isinstance(_lka, Unset):
            lka = UNSET
        else:
            lka = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LKA.from_dict(
                _lka
            )

        _kor = d.pop("KOR", UNSET)
        kor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR | Unset
        if isinstance(_kor, Unset):
            kor = UNSET
        else:
            kor = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KOR.from_dict(
                _kor
            )

        _bgr = d.pop("BGR", UNSET)
        bgr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR | Unset
        if isinstance(_bgr, Unset):
            bgr = UNSET
        else:
            bgr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BGR.from_dict(
                _bgr
            )

        _gha = d.pop("GHA", UNSET)
        gha: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA | Unset
        if isinstance(_gha, Unset):
            gha = UNSET
        else:
            gha = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GHA.from_dict(
                _gha
            )

        _srb = d.pop("SRB", UNSET)
        srb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB | Unset
        if isinstance(_srb, Unset):
            srb = UNSET
        else:
            srb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SRB.from_dict(
                _srb
            )

        _twn = d.pop("TWN", UNSET)
        twn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN | Unset
        if isinstance(_twn, Unset):
            twn = UNSET
        else:
            twn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TWN.from_dict(
                _twn
            )

        _hrv = d.pop("HRV", UNSET)
        hrv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV | Unset
        if isinstance(_hrv, Unset):
            hrv = UNSET
        else:
            hrv = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HRV.from_dict(
                _hrv
            )

        _ltu = d.pop("LTU", UNSET)
        ltu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU | Unset
        if isinstance(_ltu, Unset):
            ltu = UNSET
        else:
            ltu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LTU.from_dict(
                _ltu
            )

        _pri = d.pop("PRI", UNSET)
        pri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI | Unset
        if isinstance(_pri, Unset):
            pri = UNSET
        else:
            pri = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRI.from_dict(
                _pri
            )

        _svk = d.pop("SVK", UNSET)
        svk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK | Unset
        if isinstance(_svk, Unset):
            svk = UNSET
        else:
            svk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVK.from_dict(
                _svk
            )

        _tun = d.pop("TUN", UNSET)
        tun: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN | Unset
        if isinstance(_tun, Unset):
            tun = UNSET
        else:
            tun = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUN.from_dict(
                _tun
            )

        _est = d.pop("EST", UNSET)
        est: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST | Unset
        if isinstance(_est, Unset):
            est = UNSET
        else:
            est = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0EST.from_dict(
                _est
            )

        _ven = d.pop("VEN", UNSET)
        ven: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN | Unset
        if isinstance(_ven, Unset):
            ven = UNSET
        else:
            ven = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VEN.from_dict(
                _ven
            )

        _cri = d.pop("CRI", UNSET)
        cri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI | Unset
        if isinstance(_cri, Unset):
            cri = UNSET
        else:
            cri = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CRI.from_dict(
                _cri
            )

        _pan = d.pop("PAN", UNSET)
        pan: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN | Unset
        if isinstance(_pan, Unset):
            pan = UNSET
        else:
            pan = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PAN.from_dict(
                _pan
            )

        _ury = d.pop("URY", UNSET)
        ury: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY | Unset
        if isinstance(_ury, Unset):
            ury = UNSET
        else:
            ury = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0URY.from_dict(
                _ury
            )

        _lbn = d.pop("LBN", UNSET)
        lbn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN | Unset
        if isinstance(_lbn, Unset):
            lbn = UNSET
        else:
            lbn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBN.from_dict(
                _lbn
            )

        _lux = d.pop("LUX", UNSET)
        lux: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX | Unset
        if isinstance(_lux, Unset):
            lux = UNSET
        else:
            lux = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LUX.from_dict(
                _lux
            )

        _cyp = d.pop("CYP", UNSET)
        cyp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP | Unset
        if isinstance(_cyp, Unset):
            cyp = UNSET
        else:
            cyp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYP.from_dict(
                _cyp
            )

        _npl = d.pop("NPL", UNSET)
        npl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL | Unset
        if isinstance(_npl, Unset):
            npl = UNSET
        else:
            npl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NPL.from_dict(
                _npl
            )

        _jor = d.pop("JOR", UNSET)
        jor: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR | Unset
        if isinstance(_jor, Unset):
            jor = UNSET
        else:
            jor = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JOR.from_dict(
                _jor
            )

        _svn = d.pop("SVN", UNSET)
        svn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN | Unset
        if isinstance(_svn, Unset):
            svn = UNSET
        else:
            svn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SVN.from_dict(
                _svn
            )

        _mtq = d.pop("MTQ", UNSET)
        mtq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ | Unset
        if isinstance(_mtq, Unset):
            mtq = UNSET
        else:
            mtq = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MTQ.from_dict(
                _mtq
            )

        _qat = d.pop("QAT", UNSET)
        qat: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT | Unset
        if isinstance(_qat, Unset):
            qat = UNSET
        else:
            qat = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0QAT.from_dict(
                _qat
            )

        _glp = d.pop("GLP", UNSET)
        glp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP | Unset
        if isinstance(_glp, Unset):
            glp = UNSET
        else:
            glp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GLP.from_dict(
                _glp
            )

        _uga = d.pop("UGA", UNSET)
        uga: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA | Unset
        if isinstance(_uga, Unset):
            uga = UNSET
        else:
            uga = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UGA.from_dict(
                _uga
            )

        _dza = d.pop("DZA", UNSET)
        dza: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA | Unset
        if isinstance(_dza, Unset):
            dza = UNSET
        else:
            dza = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DZA.from_dict(
                _dza
            )

        _gtm = d.pop("GTM", UNSET)
        gtm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM | Unset
        if isinstance(_gtm, Unset):
            gtm = UNSET
        else:
            gtm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GTM.from_dict(
                _gtm
            )

        _cmr = d.pop("CMR", UNSET)
        cmr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR | Unset
        if isinstance(_cmr, Unset):
            cmr = UNSET
        else:
            cmr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CMR.from_dict(
                _cmr
            )

        _lva = d.pop("LVA", UNSET)
        lva: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA | Unset
        if isinstance(_lva, Unset):
            lva = UNSET
        else:
            lva = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LVA.from_dict(
                _lva
            )

        _dom = d.pop("DOM", UNSET)
        dom: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM | Unset
        if isinstance(_dom, Unset):
            dom = UNSET
        else:
            dom = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DOM.from_dict(
                _dom
            )

        _aze = d.pop("AZE", UNSET)
        aze: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE | Unset
        if isinstance(_aze, Unset):
            aze = UNSET
        else:
            aze = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AZE.from_dict(
                _aze
            )

        _geo = d.pop("GEO", UNSET)
        geo: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO | Unset
        if isinstance(_geo, Unset):
            geo = UNSET
        else:
            geo = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GEO.from_dict(
                _geo
            )

        _sen = d.pop("SEN", UNSET)
        sen: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN | Unset
        if isinstance(_sen, Unset):
            sen = UNSET
        else:
            sen = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SEN.from_dict(
                _sen
            )

        _tza = d.pop("TZA", UNSET)
        tza: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA | Unset
        if isinstance(_tza, Unset):
            tza = UNSET
        else:
            tza = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TZA.from_dict(
                _tza
            )

        _zwe = d.pop("ZWE", UNSET)
        zwe: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE | Unset
        if isinstance(_zwe, Unset):
            zwe = UNSET
        else:
            zwe = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZWE.from_dict(
                _zwe
            )

        _kwt = d.pop("KWT", UNSET)
        kwt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT | Unset
        if isinstance(_kwt, Unset):
            kwt = UNSET
        else:
            kwt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KWT.from_dict(
                _kwt
            )

        _mlt = d.pop("MLT", UNSET)
        mlt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT | Unset
        if isinstance(_mlt, Unset):
            mlt = UNSET
        else:
            mlt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLT.from_dict(
                _mlt
            )

        _omn = d.pop("OMN", UNSET)
        omn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN | Unset
        if isinstance(_omn, Unset):
            omn = UNSET
        else:
            omn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0OMN.from_dict(
                _omn
            )

        _bol = d.pop("BOL", UNSET)
        bol: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL | Unset
        if isinstance(_bol, Unset):
            bol = UNSET
        else:
            bol = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BOL.from_dict(
                _bol
            )

        _slv = d.pop("SLV", UNSET)
        slv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV | Unset
        if isinstance(_slv, Unset):
            slv = UNSET
        else:
            slv = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLV.from_dict(
                _slv
            )

        _arm = d.pop("ARM", UNSET)
        arm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM | Unset
        if isinstance(_arm, Unset):
            arm = UNSET
        else:
            arm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ARM.from_dict(
                _arm
            )

        _pry = d.pop("PRY", UNSET)
        pry: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY | Unset
        if isinstance(_pry, Unset):
            pry = UNSET
        else:
            pry = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRY.from_dict(
                _pry
            )

        _irq = d.pop("IRQ", UNSET)
        irq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ | Unset
        if isinstance(_irq, Unset):
            irq = UNSET
        else:
            irq = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IRQ.from_dict(
                _irq
            )

        _khm = d.pop("KHM", UNSET)
        khm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM | Unset
        if isinstance(_khm, Unset):
            khm = UNSET
        else:
            khm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KHM.from_dict(
                _khm
            )

        _bih = d.pop("BIH", UNSET)
        bih: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH | Unset
        if isinstance(_bih, Unset):
            bih = UNSET
        else:
            bih = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BIH.from_dict(
                _bih
            )

        _ago = d.pop("AGO", UNSET)
        ago: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO | Unset
        if isinstance(_ago, Unset):
            ago = UNSET
        else:
            ago = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AGO.from_dict(
                _ago
            )

        _bhr = d.pop("BHR", UNSET)
        bhr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR | Unset
        if isinstance(_bhr, Unset):
            bhr = UNSET
        else:
            bhr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHR.from_dict(
                _bhr
            )

        _alb = d.pop("ALB", UNSET)
        alb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB | Unset
        if isinstance(_alb, Unset):
            alb = UNSET
        else:
            alb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALB.from_dict(
                _alb
            )

        _kaz = d.pop("KAZ", UNSET)
        kaz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ | Unset
        if isinstance(_kaz, Unset):
            kaz = UNSET
        else:
            kaz = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KAZ.from_dict(
                _kaz
            )

        _civ = d.pop("CIV", UNSET)
        civ: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV | Unset
        if isinstance(_civ, Unset):
            civ = UNSET
        else:
            civ = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CIV.from_dict(
                _civ
            )

        _eth = d.pop("ETH", UNSET)
        eth: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH | Unset
        if isinstance(_eth, Unset):
            eth = UNSET
        else:
            eth = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ETH.from_dict(
                _eth
            )

        _mus = d.pop("MUS", UNSET)
        mus: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS | Unset
        if isinstance(_mus, Unset):
            mus = UNSET
        else:
            mus = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MUS.from_dict(
                _mus
            )

        _zmb = d.pop("ZMB", UNSET)
        zmb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB | Unset
        if isinstance(_zmb, Unset):
            zmb = UNSET
        else:
            zmb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ZMB.from_dict(
                _zmb
            )

        _mkd = d.pop("MKD", UNSET)
        mkd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD | Unset
        if isinstance(_mkd, Unset):
            mkd = UNSET
        else:
            mkd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MKD.from_dict(
                _mkd
            )

        _cod = d.pop("COD", UNSET)
        cod: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD | Unset
        if isinstance(_cod, Unset):
            cod = UNSET
        else:
            cod = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COD.from_dict(
                _cod
            )

        _blr = d.pop("BLR", UNSET)
        blr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR | Unset
        if isinstance(_blr, Unset):
            blr = UNSET
        else:
            blr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLR.from_dict(
                _blr
            )

        _moz = d.pop("MOZ", UNSET)
        moz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ | Unset
        if isinstance(_moz, Unset):
            moz = UNSET
        else:
            moz = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MOZ.from_dict(
                _moz
            )

        _reu = d.pop("REU", UNSET)
        reu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU | Unset
        if isinstance(_reu, Unset):
            reu = UNSET
        else:
            reu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0REU.from_dict(
                _reu
            )

        _tto = d.pop("TTO", UNSET)
        tto: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO | Unset
        if isinstance(_tto, Unset):
            tto = UNSET
        else:
            tto = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TTO.from_dict(
                _tto
            )

        _guf = d.pop("GUF", UNSET)
        guf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF | Unset
        if isinstance(_guf, Unset):
            guf = UNSET
        else:
            guf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUF.from_dict(
                _guf
            )

        _isl = d.pop("ISL", UNSET)
        isl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL | Unset
        if isinstance(_isl, Unset):
            isl = UNSET
        else:
            isl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ISL.from_dict(
                _isl
            )

        _mmr = d.pop("MMR", UNSET)
        mmr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR | Unset
        if isinstance(_mmr, Unset):
            mmr = UNSET
        else:
            mmr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MMR.from_dict(
                _mmr
            )

        _hnd = d.pop("HND", UNSET)
        hnd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND | Unset
        if isinstance(_hnd, Unset):
            hnd = UNSET
        else:
            hnd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HND.from_dict(
                _hnd
            )

        _rwa = d.pop("RWA", UNSET)
        rwa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA | Unset
        if isinstance(_rwa, Unset):
            rwa = UNSET
        else:
            rwa = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0RWA.from_dict(
                _rwa
            )

        _mdg = d.pop("MDG", UNSET)
        mdg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG | Unset
        if isinstance(_mdg, Unset):
            mdg = UNSET
        else:
            mdg = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDG.from_dict(
                _mdg
            )

        _ben = d.pop("BEN", UNSET)
        ben: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN | Unset
        if isinstance(_ben, Unset):
            ben = UNSET
        else:
            ben = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BEN.from_dict(
                _ben
            )

        _uzb = d.pop("UZB", UNSET)
        uzb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB | Unset
        if isinstance(_uzb, Unset):
            uzb = UNSET
        else:
            uzb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UZB.from_dict(
                _uzb
            )

        _nam = d.pop("NAM", UNSET)
        nam: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM | Unset
        if isinstance(_nam, Unset):
            nam = UNSET
        else:
            nam = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NAM.from_dict(
                _nam
            )

        _bwa = d.pop("BWA", UNSET)
        bwa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA | Unset
        if isinstance(_bwa, Unset):
            bwa = UNSET
        else:
            bwa = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BWA.from_dict(
                _bwa
            )

        _mda = d.pop("MDA", UNSET)
        mda: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA | Unset
        if isinstance(_mda, Unset):
            mda = UNSET
        else:
            mda = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDA.from_dict(
                _mda
            )

        _jey = d.pop("JEY", UNSET)
        jey: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY | Unset
        if isinstance(_jey, Unset):
            jey = UNSET
        else:
            jey = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JEY.from_dict(
                _jey
            )

        _nic = d.pop("NIC", UNSET)
        nic: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC | Unset
        if isinstance(_nic, Unset):
            nic = UNSET
        else:
            nic = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIC.from_dict(
                _nic
            )

        _sdn = d.pop("SDN", UNSET)
        sdn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN | Unset
        if isinstance(_sdn, Unset):
            sdn = UNSET
        else:
            sdn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SDN.from_dict(
                _sdn
            )

        _jam = d.pop("JAM", UNSET)
        jam: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM | Unset
        if isinstance(_jam, Unset):
            jam = UNSET
        else:
            jam = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0JAM.from_dict(
                _jam
            )

        _imn = d.pop("IMN", UNSET)
        imn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN | Unset
        if isinstance(_imn, Unset):
            imn = UNSET
        else:
            imn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IMN.from_dict(
                _imn
            )

        _bfa = d.pop("BFA", UNSET)
        bfa: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA | Unset
        if isinstance(_bfa, Unset):
            bfa = UNSET
        else:
            bfa = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BFA.from_dict(
                _bfa
            )

        _mng = d.pop("MNG", UNSET)
        mng: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG | Unset
        if isinstance(_mng, Unset):
            mng = UNSET
        else:
            mng = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNG.from_dict(
                _mng
            )

        _mne = d.pop("MNE", UNSET)
        mne: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE | Unset
        if isinstance(_mne, Unset):
            mne = UNSET
        else:
            mne = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNE.from_dict(
                _mne
            )

        _mco = d.pop("MCO", UNSET)
        mco: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO | Unset
        if isinstance(_mco, Unset):
            mco = UNSET
        else:
            mco = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MCO.from_dict(
                _mco
            )

        _tgo = d.pop("TGO", UNSET)
        tgo: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO | Unset
        if isinstance(_tgo, Unset):
            tgo = UNSET
        else:
            tgo = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TGO.from_dict(
                _tgo
            )

        _afg = d.pop("AFG", UNSET)
        afg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG | Unset
        if isinstance(_afg, Unset):
            afg = UNSET
        else:
            afg = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AFG.from_dict(
                _afg
            )

        _lby = d.pop("LBY", UNSET)
        lby: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY | Unset
        if isinstance(_lby, Unset):
            lby = UNSET
        else:
            lby = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBY.from_dict(
                _lby
            )

        _xkx = d.pop("XKX", UNSET)
        xkx: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX | Unset
        if isinstance(_xkx, Unset):
            xkx = UNSET
        else:
            xkx = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0XKX.from_dict(
                _xkx
            )

        _cym = d.pop("CYM", UNSET)
        cym: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM | Unset
        if isinstance(_cym, Unset):
            cym = UNSET
        else:
            cym = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CYM.from_dict(
                _cym
            )

        _mwi = d.pop("MWI", UNSET)
        mwi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI | Unset
        if isinstance(_mwi, Unset):
            mwi = UNSET
        else:
            mwi = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MWI.from_dict(
                _mwi
            )

        _som = d.pop("SOM", UNSET)
        som: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM | Unset
        if isinstance(_som, Unset):
            som = UNSET
        else:
            som = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SOM.from_dict(
                _som
            )

        _png = d.pop("PNG", UNSET)
        png: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG | Unset
        if isinstance(_png, Unset):
            png = UNSET
        else:
            png = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PNG.from_dict(
                _png
            )

        _mdv = d.pop("MDV", UNSET)
        mdv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV | Unset
        if isinstance(_mdv, Unset):
            mdv = UNSET
        else:
            mdv = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MDV.from_dict(
                _mdv
            )

        _mli = d.pop("MLI", UNSET)
        mli: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI | Unset
        if isinstance(_mli, Unset):
            mli = UNSET
        else:
            mli = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MLI.from_dict(
                _mli
            )

        _gin = d.pop("GIN", UNSET)
        gin: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN | Unset
        if isinstance(_gin, Unset):
            gin = UNSET
        else:
            gin = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIN.from_dict(
                _gin
            )

        _pse = d.pop("PSE", UNSET)
        pse: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE | Unset
        if isinstance(_pse, Unset):
            pse = UNSET
        else:
            pse = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PSE.from_dict(
                _pse
            )

        _gab = d.pop("GAB", UNSET)
        gab: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB | Unset
        if isinstance(_gab, Unset):
            gab = UNSET
        else:
            gab = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GAB.from_dict(
                _gab
            )

        _lie = d.pop("LIE", UNSET)
        lie: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE | Unset
        if isinstance(_lie, Unset):
            lie = UNSET
        else:
            lie = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LIE.from_dict(
                _lie
            )

        _hti = d.pop("HTI", UNSET)
        hti: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI | Unset
        if isinstance(_hti, Unset):
            hti = UNSET
        else:
            hti = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HTI.from_dict(
                _hti
            )

        _syr = d.pop("SYR", UNSET)
        syr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR | Unset
        if isinstance(_syr, Unset):
            syr = UNSET
        else:
            syr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYR.from_dict(
                _syr
            )

        _brb = d.pop("BRB", UNSET)
        brb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB | Unset
        if isinstance(_brb, Unset):
            brb = UNSET
        else:
            brb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRB.from_dict(
                _brb
            )

        _yem = d.pop("YEM", UNSET)
        yem: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM | Unset
        if isinstance(_yem, Unset):
            yem = UNSET
        else:
            yem = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0YEM.from_dict(
                _yem
            )

        _ggy = d.pop("GGY", UNSET)
        ggy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY | Unset
        if isinstance(_ggy, Unset):
            ggy = UNSET
        else:
            ggy = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GGY.from_dict(
                _ggy
            )

        _ncl = d.pop("NCL", UNSET)
        ncl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL | Unset
        if isinstance(_ncl, Unset):
            ncl = UNSET
        else:
            ncl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NCL.from_dict(
                _ncl
            )

        _and_ = d.pop("AND", UNSET)
        and_: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND | Unset
        if isinstance(_and_, Unset):
            and_ = UNSET
        else:
            and_ = (
                KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AND.from_dict(
                    _and_
                )
            )

        _sur = d.pop("SUR", UNSET)
        sur: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR | Unset
        if isinstance(_sur, Unset):
            sur = UNSET
        else:
            sur = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SUR.from_dict(
                _sur
            )

        _myt = d.pop("MYT", UNSET)
        myt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT | Unset
        if isinstance(_myt, Unset):
            myt = UNSET
        else:
            myt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MYT.from_dict(
                _myt
            )

        _kgz = d.pop("KGZ", UNSET)
        kgz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ | Unset
        if isinstance(_kgz, Unset):
            kgz = UNSET
        else:
            kgz = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KGZ.from_dict(
                _kgz
            )

        _bhs = d.pop("BHS", UNSET)
        bhs: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS | Unset
        if isinstance(_bhs, Unset):
            bhs = UNSET
        else:
            bhs = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BHS.from_dict(
                _bhs
            )

        _gib = d.pop("GIB", UNSET)
        gib: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB | Unset
        if isinstance(_gib, Unset):
            gib = UNSET
        else:
            gib = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GIB.from_dict(
                _gib
            )

        _cog = d.pop("COG", UNSET)
        cog: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG | Unset
        if isinstance(_cog, Unset):
            cog = UNSET
        else:
            cog = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COG.from_dict(
                _cog
            )

        _fji = d.pop("FJI", UNSET)
        fji: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI | Unset
        if isinstance(_fji, Unset):
            fji = UNSET
        else:
            fji = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FJI.from_dict(
                _fji
            )

        _blm = d.pop("BLM", UNSET)
        blm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM | Unset
        if isinstance(_blm, Unset):
            blm = UNSET
        else:
            blm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLM.from_dict(
                _blm
            )

        _cuw = d.pop("CUW", UNSET)
        cuw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW | Unset
        if isinstance(_cuw, Unset):
            cuw = UNSET
        else:
            cuw = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUW.from_dict(
                _cuw
            )

        _cub = d.pop("CUB", UNSET)
        cub: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB | Unset
        if isinstance(_cub, Unset):
            cub = UNSET
        else:
            cub = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CUB.from_dict(
                _cub
            )

        _sle = d.pop("SLE", UNSET)
        sle: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE | Unset
        if isinstance(_sle, Unset):
            sle = UNSET
        else:
            sle = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLE.from_dict(
                _sle
            )

        _blz = d.pop("BLZ", UNSET)
        blz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ | Unset
        if isinstance(_blz, Unset):
            blz = UNSET
        else:
            blz = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BLZ.from_dict(
                _blz
            )

        _ner = d.pop("NER", UNSET)
        ner: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER | Unset
        if isinstance(_ner, Unset):
            ner = UNSET
        else:
            ner = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NER.from_dict(
                _ner
            )

        _lbr = d.pop("LBR", UNSET)
        lbr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR | Unset
        if isinstance(_lbr, Unset):
            lbr = UNSET
        else:
            lbr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LBR.from_dict(
                _lbr
            )

        _vir = d.pop("VIR", UNSET)
        vir: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR | Unset
        if isinstance(_vir, Unset):
            vir = UNSET
        else:
            vir = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VIR.from_dict(
                _vir
            )

        _pyf = d.pop("PYF", UNSET)
        pyf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF | Unset
        if isinstance(_pyf, Unset):
            pyf = UNSET
        else:
            pyf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PYF.from_dict(
                _pyf
            )

        _gum = d.pop("GUM", UNSET)
        gum: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM | Unset
        if isinstance(_gum, Unset):
            gum = UNSET
        else:
            gum = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUM.from_dict(
                _gum
            )

        _mrt = d.pop("MRT", UNSET)
        mrt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT | Unset
        if isinstance(_mrt, Unset):
            mrt = UNSET
        else:
            mrt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MRT.from_dict(
                _mrt
            )

        _abw = d.pop("ABW", UNSET)
        abw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW | Unset
        if isinstance(_abw, Unset):
            abw = UNSET
        else:
            abw = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ABW.from_dict(
                _abw
            )

        _syc = d.pop("SYC", UNSET)
        syc: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC | Unset
        if isinstance(_syc, Unset):
            syc = UNSET
        else:
            syc = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SYC.from_dict(
                _syc
            )

        _guy = d.pop("GUY", UNSET)
        guy: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY | Unset
        if isinstance(_guy, Unset):
            guy = UNSET
        else:
            guy = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GUY.from_dict(
                _guy
            )

        _lso = d.pop("LSO", UNSET)
        lso: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO | Unset
        if isinstance(_lso, Unset):
            lso = UNSET
        else:
            lso = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LSO.from_dict(
                _lso
            )

        _swz = d.pop("SWZ", UNSET)
        swz: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ | Unset
        if isinstance(_swz, Unset):
            swz = UNSET
        else:
            swz = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SWZ.from_dict(
                _swz
            )

        _ssd = d.pop("SSD", UNSET)
        ssd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD | Unset
        if isinstance(_ssd, Unset):
            ssd = UNSET
        else:
            ssd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SSD.from_dict(
                _ssd
            )

        _lca = d.pop("LCA", UNSET)
        lca: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA | Unset
        if isinstance(_lca, Unset):
            lca = UNSET
        else:
            lca = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LCA.from_dict(
                _lca
            )

        _mac = d.pop("MAC", UNSET)
        mac: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC | Unset
        if isinstance(_mac, Unset):
            mac = UNSET
        else:
            mac = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAC.from_dict(
                _mac
            )

        _smr = d.pop("SMR", UNSET)
        smr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR | Unset
        if isinstance(_smr, Unset):
            smr = UNSET
        else:
            smr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SMR.from_dict(
                _smr
            )

        _lao = d.pop("LAO", UNSET)
        lao: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO | Unset
        if isinstance(_lao, Unset):
            lao = UNSET
        else:
            lao = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0LAO.from_dict(
                _lao
            )

        _brn = d.pop("BRN", UNSET)
        brn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN | Unset
        if isinstance(_brn, Unset):
            brn = UNSET
        else:
            brn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BRN.from_dict(
                _brn
            )

        _tcd = d.pop("TCD", UNSET)
        tcd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD | Unset
        if isinstance(_tcd, Unset):
            tcd = UNSET
        else:
            tcd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCD.from_dict(
                _tcd
            )

        _bmu = d.pop("BMU", UNSET)
        bmu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU | Unset
        if isinstance(_bmu, Unset):
            bmu = UNSET
        else:
            bmu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BMU.from_dict(
                _bmu
            )

        _vgb = d.pop("VGB", UNSET)
        vgb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB | Unset
        if isinstance(_vgb, Unset):
            vgb = UNSET
        else:
            vgb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VGB.from_dict(
                _vgb
            )

        _prk = d.pop("PRK", UNSET)
        prk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK | Unset
        if isinstance(_prk, Unset):
            prk = UNSET
        else:
            prk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PRK.from_dict(
                _prk
            )

        _btn = d.pop("BTN", UNSET)
        btn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN | Unset
        if isinstance(_btn, Unset):
            btn = UNSET
        else:
            btn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BTN.from_dict(
                _btn
            )

        _bdi = d.pop("BDI", UNSET)
        bdi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI | Unset
        if isinstance(_bdi, Unset):
            bdi = UNSET
        else:
            bdi = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BDI.from_dict(
                _bdi
            )

        _fro = d.pop("FRO", UNSET)
        fro: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO | Unset
        if isinstance(_fro, Unset):
            fro = UNSET
        else:
            fro = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FRO.from_dict(
                _fro
            )

        _tjk = d.pop("TJK", UNSET)
        tjk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK | Unset
        if isinstance(_tjk, Unset):
            tjk = UNSET
        else:
            tjk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TJK.from_dict(
                _tjk
            )

        _gmb = d.pop("GMB", UNSET)
        gmb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB | Unset
        if isinstance(_gmb, Unset):
            gmb = UNSET
        else:
            gmb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GMB.from_dict(
                _gmb
            )

        _stp = d.pop("STP", UNSET)
        stp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP | Unset
        if isinstance(_stp, Unset):
            stp = UNSET
        else:
            stp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0STP.from_dict(
                _stp
            )

        _ant = d.pop("ANT", UNSET)
        ant: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT | Unset
        if isinstance(_ant, Unset):
            ant = UNSET
        else:
            ant = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ANT.from_dict(
                _ant
            )

        _vct = d.pop("VCT", UNSET)
        vct: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT | Unset
        if isinstance(_vct, Unset):
            vct = UNSET
        else:
            vct = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VCT.from_dict(
                _vct
            )

        _dji = d.pop("DJI", UNSET)
        dji: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI | Unset
        if isinstance(_dji, Unset):
            dji = UNSET
        else:
            dji = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DJI.from_dict(
                _dji
            )

        _cpv = d.pop("CPV", UNSET)
        cpv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV | Unset
        if isinstance(_cpv, Unset):
            cpv = UNSET
        else:
            cpv = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CPV.from_dict(
                _cpv
            )

        _tkm = d.pop("TKM", UNSET)
        tkm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM | Unset
        if isinstance(_tkm, Unset):
            tkm = UNSET
        else:
            tkm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKM.from_dict(
                _tkm
            )

        _atg = d.pop("ATG", UNSET)
        atg: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG | Unset
        if isinstance(_atg, Unset):
            atg = UNSET
        else:
            atg = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATG.from_dict(
                _atg
            )

        _tca = d.pop("TCA", UNSET)
        tca: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA | Unset
        if isinstance(_tca, Unset):
            tca = UNSET
        else:
            tca = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TCA.from_dict(
                _tca
            )

        _kna = d.pop("KNA", UNSET)
        kna: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA | Unset
        if isinstance(_kna, Unset):
            kna = UNSET
        else:
            kna = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KNA.from_dict(
                _kna
            )

        _grd = d.pop("GRD", UNSET)
        grd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD | Unset
        if isinstance(_grd, Unset):
            grd = UNSET
        else:
            grd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRD.from_dict(
                _grd
            )

        _asm = d.pop("ASM", UNSET)
        asm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM | Unset
        if isinstance(_asm, Unset):
            asm = UNSET
        else:
            asm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ASM.from_dict(
                _asm
            )

        _vut = d.pop("VUT", UNSET)
        vut: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT | Unset
        if isinstance(_vut, Unset):
            vut = UNSET
        else:
            vut = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VUT.from_dict(
                _vut
            )

        _gnq = d.pop("GNQ", UNSET)
        gnq: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ | Unset
        if isinstance(_gnq, Unset):
            gnq = UNSET
        else:
            gnq = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNQ.from_dict(
                _gnq
            )

        _grl = d.pop("GRL", UNSET)
        grl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL | Unset
        if isinstance(_grl, Unset):
            grl = UNSET
        else:
            grl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GRL.from_dict(
                _grl
            )

        _sxm = d.pop("SXM", UNSET)
        sxm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM | Unset
        if isinstance(_sxm, Unset):
            sxm = UNSET
        else:
            sxm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SXM.from_dict(
                _sxm
            )

        _mnp = d.pop("MNP", UNSET)
        mnp: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP | Unset
        if isinstance(_mnp, Unset):
            mnp = UNSET
        else:
            mnp = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MNP.from_dict(
                _mnp
            )

        _com = d.pop("COM", UNSET)
        com: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM | Unset
        if isinstance(_com, Unset):
            com = UNSET
        else:
            com = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COM.from_dict(
                _com
            )

        _tls = d.pop("TLS", UNSET)
        tls: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS | Unset
        if isinstance(_tls, Unset):
            tls = UNSET
        else:
            tls = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TLS.from_dict(
                _tls
            )

        _sjm = d.pop("SJM", UNSET)
        sjm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM | Unset
        if isinstance(_sjm, Unset):
            sjm = UNSET
        else:
            sjm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SJM.from_dict(
                _sjm
            )

        _caf = d.pop("CAF", UNSET)
        caf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF | Unset
        if isinstance(_caf, Unset):
            caf = UNSET
        else:
            caf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CAF.from_dict(
                _caf
            )

        _dma = d.pop("DMA", UNSET)
        dma: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA | Unset
        if isinstance(_dma, Unset):
            dma = UNSET
        else:
            dma = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0DMA.from_dict(
                _dma
            )

        _maf = d.pop("MAF", UNSET)
        maf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF | Unset
        if isinstance(_maf, Unset):
            maf = UNSET
        else:
            maf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MAF.from_dict(
                _maf
            )

        _wsm = d.pop("WSM", UNSET)
        wsm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM | Unset
        if isinstance(_wsm, Unset):
            wsm = UNSET
        else:
            wsm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WSM.from_dict(
                _wsm
            )

        _bes = d.pop("BES", UNSET)
        bes: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES | Unset
        if isinstance(_bes, Unset):
            bes = UNSET
        else:
            bes = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BES.from_dict(
                _bes
            )

        _mhl = d.pop("MHL", UNSET)
        mhl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL | Unset
        if isinstance(_mhl, Unset):
            mhl = UNSET
        else:
            mhl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MHL.from_dict(
                _mhl
            )

        _aia = d.pop("AIA", UNSET)
        aia: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA | Unset
        if isinstance(_aia, Unset):
            aia = UNSET
        else:
            aia = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0AIA.from_dict(
                _aia
            )

        _ton = d.pop("TON", UNSET)
        ton: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON | Unset
        if isinstance(_ton, Unset):
            ton = UNSET
        else:
            ton = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TON.from_dict(
                _ton
            )

        _cok = d.pop("COK", UNSET)
        cok: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK | Unset
        if isinstance(_cok, Unset):
            cok = UNSET
        else:
            cok = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0COK.from_dict(
                _cok
            )

        _slb = d.pop("SLB", UNSET)
        slb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB | Unset
        if isinstance(_slb, Unset):
            slb = UNSET
        else:
            slb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SLB.from_dict(
                _slb
            )

        _spm = d.pop("SPM", UNSET)
        spm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM | Unset
        if isinstance(_spm, Unset):
            spm = UNSET
        else:
            spm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SPM.from_dict(
                _spm
            )

        _gnb = d.pop("GNB", UNSET)
        gnb: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB | Unset
        if isinstance(_gnb, Unset):
            gnb = UNSET
        else:
            gnb = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0GNB.from_dict(
                _gnb
            )

        _ata = d.pop("ATA", UNSET)
        ata: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA | Unset
        if isinstance(_ata, Unset):
            ata = UNSET
        else:
            ata = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATA.from_dict(
                _ata
            )

        _tuv = d.pop("TUV", UNSET)
        tuv: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV | Unset
        if isinstance(_tuv, Unset):
            tuv = UNSET
        else:
            tuv = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TUV.from_dict(
                _tuv
            )

        _ala = d.pop("ALA", UNSET)
        ala: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA | Unset
        if isinstance(_ala, Unset):
            ala = UNSET
        else:
            ala = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ALA.from_dict(
                _ala
            )

        _iot = d.pop("IOT", UNSET)
        iot: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT | Unset
        if isinstance(_iot, Unset):
            iot = UNSET
        else:
            iot = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0IOT.from_dict(
                _iot
            )

        _eri = d.pop("ERI", UNSET)
        eri: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI | Unset
        if isinstance(_eri, Unset):
            eri = UNSET
        else:
            eri = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ERI.from_dict(
                _eri
            )

        _plw = d.pop("PLW", UNSET)
        plw: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW | Unset
        if isinstance(_plw, Unset):
            plw = UNSET
        else:
            plw = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PLW.from_dict(
                _plw
            )

        _fsm = d.pop("FSM", UNSET)
        fsm: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM | Unset
        if isinstance(_fsm, Unset):
            fsm = UNSET
        else:
            fsm = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FSM.from_dict(
                _fsm
            )

        _nru = d.pop("NRU", UNSET)
        nru: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU | Unset
        if isinstance(_nru, Unset):
            nru = UNSET
        else:
            nru = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NRU.from_dict(
                _nru
            )

        _pcn = d.pop("PCN", UNSET)
        pcn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN | Unset
        if isinstance(_pcn, Unset):
            pcn = UNSET
        else:
            pcn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0PCN.from_dict(
                _pcn
            )

        _flk = d.pop("FLK", UNSET)
        flk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK | Unset
        if isinstance(_flk, Unset):
            flk = UNSET
        else:
            flk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0FLK.from_dict(
                _flk
            )

        _msr = d.pop("MSR", UNSET)
        msr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR | Unset
        if isinstance(_msr, Unset):
            msr = UNSET
        else:
            msr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0MSR.from_dict(
                _msr
            )

        _vat = d.pop("VAT", UNSET)
        vat: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT | Unset
        if isinstance(_vat, Unset):
            vat = UNSET
        else:
            vat = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0VAT.from_dict(
                _vat
            )

        _kir = d.pop("KIR", UNSET)
        kir: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR | Unset
        if isinstance(_kir, Unset):
            kir = UNSET
        else:
            kir = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0KIR.from_dict(
                _kir
            )

        _shn = d.pop("SHN", UNSET)
        shn: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN | Unset
        if isinstance(_shn, Unset):
            shn = UNSET
        else:
            shn = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SHN.from_dict(
                _shn
            )

        _niu = d.pop("NIU", UNSET)
        niu: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU | Unset
        if isinstance(_niu, Unset):
            niu = UNSET
        else:
            niu = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NIU.from_dict(
                _niu
            )

        _wlf = d.pop("WLF", UNSET)
        wlf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF | Unset
        if isinstance(_wlf, Unset):
            wlf = UNSET
        else:
            wlf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0WLF.from_dict(
                _wlf
            )

        _hmd = d.pop("HMD", UNSET)
        hmd: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD | Unset
        if isinstance(_hmd, Unset):
            hmd = UNSET
        else:
            hmd = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0HMD.from_dict(
                _hmd
            )

        _cxr = d.pop("CXR", UNSET)
        cxr: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR | Unset
        if isinstance(_cxr, Unset):
            cxr = UNSET
        else:
            cxr = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CXR.from_dict(
                _cxr
            )

        _nfk = d.pop("NFK", UNSET)
        nfk: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK | Unset
        if isinstance(_nfk, Unset):
            nfk = UNSET
        else:
            nfk = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0NFK.from_dict(
                _nfk
            )

        _atf = d.pop("ATF", UNSET)
        atf: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF | Unset
        if isinstance(_atf, Unset):
            atf = UNSET
        else:
            atf = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ATF.from_dict(
                _atf
            )

        _cck = d.pop("CCK", UNSET)
        cck: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK | Unset
        if isinstance(_cck, Unset):
            cck = UNSET
        else:
            cck = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0CCK.from_dict(
                _cck
            )

        _sgs = d.pop("SGS", UNSET)
        sgs: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS | Unset
        if isinstance(_sgs, Unset):
            sgs = UNSET
        else:
            sgs = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0SGS.from_dict(
                _sgs
            )

        _bvt = d.pop("BVT", UNSET)
        bvt: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT | Unset
        if isinstance(_bvt, Unset):
            bvt = UNSET
        else:
            bvt = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0BVT.from_dict(
                _bvt
            )

        _umi = d.pop("UMI", UNSET)
        umi: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI | Unset
        if isinstance(_umi, Unset):
            umi = UNSET
        else:
            umi = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0UMI.from_dict(
                _umi
            )

        _esh = d.pop("ESH", UNSET)
        esh: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH | Unset
        if isinstance(_esh, Unset):
            esh = UNSET
        else:
            esh = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0ESH.from_dict(
                _esh
            )

        _tkl = d.pop("TKL", UNSET)
        tkl: KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL | Unset
        if isinstance(_tkl, Unset):
            tkl = UNSET
        else:
            tkl = KitchenSinkCompanyResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0TKL.from_dict(
                _tkl
            )

        kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0 = (
            cls(
                usa=usa,
                gbr=gbr,
                fra=fra,
                ind=ind,
                bra=bra,
                deu=deu,
                esp=esp,
                can=can,
                aus=aus,
                nld=nld,
                ita=ita,
                zaf=zaf,
                bel=bel,
                chn=chn,
                tur=tur,
                mex=mex,
                che=che,
                nor=nor,
                are=are,
                swe=swe,
                pol=pol,
                idn=idn,
                arg=arg,
                prt=prt,
                col=col,
                chl=chl,
                pak=pak,
                dnk=dnk,
                jpn=jpn,
                nga=nga,
                sgp=sgp,
                per=per,
                nzl=nzl,
                aut=aut,
                irl=irl,
                mys=mys,
                bgd=bgd,
                egy=egy,
                isr=isr,
                sau=sau,
                phl=phl,
                fin=fin,
                irn=irn,
                rou=rou,
                cze=cze,
                grc=grc,
                hkg=hkg,
                hun=hun,
                ken=ken,
                mar=mar,
                vnm=vnm,
                rus=rus,
                ukr=ukr,
                ecu=ecu,
                tha=tha,
                lka=lka,
                kor=kor,
                bgr=bgr,
                gha=gha,
                srb=srb,
                twn=twn,
                hrv=hrv,
                ltu=ltu,
                pri=pri,
                svk=svk,
                tun=tun,
                est=est,
                ven=ven,
                cri=cri,
                pan=pan,
                ury=ury,
                lbn=lbn,
                lux=lux,
                cyp=cyp,
                npl=npl,
                jor=jor,
                svn=svn,
                mtq=mtq,
                qat=qat,
                glp=glp,
                uga=uga,
                dza=dza,
                gtm=gtm,
                cmr=cmr,
                lva=lva,
                dom=dom,
                aze=aze,
                geo=geo,
                sen=sen,
                tza=tza,
                zwe=zwe,
                kwt=kwt,
                mlt=mlt,
                omn=omn,
                bol=bol,
                slv=slv,
                arm=arm,
                pry=pry,
                irq=irq,
                khm=khm,
                bih=bih,
                ago=ago,
                bhr=bhr,
                alb=alb,
                kaz=kaz,
                civ=civ,
                eth=eth,
                mus=mus,
                zmb=zmb,
                mkd=mkd,
                cod=cod,
                blr=blr,
                moz=moz,
                reu=reu,
                tto=tto,
                guf=guf,
                isl=isl,
                mmr=mmr,
                hnd=hnd,
                rwa=rwa,
                mdg=mdg,
                ben=ben,
                uzb=uzb,
                nam=nam,
                bwa=bwa,
                mda=mda,
                jey=jey,
                nic=nic,
                sdn=sdn,
                jam=jam,
                imn=imn,
                bfa=bfa,
                mng=mng,
                mne=mne,
                mco=mco,
                tgo=tgo,
                afg=afg,
                lby=lby,
                xkx=xkx,
                cym=cym,
                mwi=mwi,
                som=som,
                png=png,
                mdv=mdv,
                mli=mli,
                gin=gin,
                pse=pse,
                gab=gab,
                lie=lie,
                hti=hti,
                syr=syr,
                brb=brb,
                yem=yem,
                ggy=ggy,
                ncl=ncl,
                and_=and_,
                sur=sur,
                myt=myt,
                kgz=kgz,
                bhs=bhs,
                gib=gib,
                cog=cog,
                fji=fji,
                blm=blm,
                cuw=cuw,
                cub=cub,
                sle=sle,
                blz=blz,
                ner=ner,
                lbr=lbr,
                vir=vir,
                pyf=pyf,
                gum=gum,
                mrt=mrt,
                abw=abw,
                syc=syc,
                guy=guy,
                lso=lso,
                swz=swz,
                ssd=ssd,
                lca=lca,
                mac=mac,
                smr=smr,
                lao=lao,
                brn=brn,
                tcd=tcd,
                bmu=bmu,
                vgb=vgb,
                prk=prk,
                btn=btn,
                bdi=bdi,
                fro=fro,
                tjk=tjk,
                gmb=gmb,
                stp=stp,
                ant=ant,
                vct=vct,
                dji=dji,
                cpv=cpv,
                tkm=tkm,
                atg=atg,
                tca=tca,
                kna=kna,
                grd=grd,
                asm=asm,
                vut=vut,
                gnq=gnq,
                grl=grl,
                sxm=sxm,
                mnp=mnp,
                com=com,
                tls=tls,
                sjm=sjm,
                caf=caf,
                dma=dma,
                maf=maf,
                wsm=wsm,
                bes=bes,
                mhl=mhl,
                aia=aia,
                ton=ton,
                cok=cok,
                slb=slb,
                spm=spm,
                gnb=gnb,
                ata=ata,
                tuv=tuv,
                ala=ala,
                iot=iot,
                eri=eri,
                plw=plw,
                fsm=fsm,
                nru=nru,
                pcn=pcn,
                flk=flk,
                msr=msr,
                vat=vat,
                kir=kir,
                shn=shn,
                niu=niu,
                wlf=wlf,
                hmd=hmd,
                cxr=cxr,
                nfk=nfk,
                atf=atf,
                cck=cck,
                sgs=sgs,
                bvt=bvt,
                umi=umi,
                esh=esh,
                tkl=tkl,
            )
        )

        return (
            kitchen_sink_company_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0
        )
