from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0abw import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0afg import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ago import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aia import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ala import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0alb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0and import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ant import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0are import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0arg import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0arm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0asm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ata import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0atf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0atg import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aus import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aut import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aze import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bdi import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bel import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ben import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bes import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bfa import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bgd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bgr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bhr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bhs import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bih import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blz import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bmu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bol import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bra import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0brb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0brn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0btn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bvt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bwa import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0caf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0can import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cck import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0che import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0chl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0chn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0civ import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cmr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cod import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cog import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cok import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0col import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0com import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cpv import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cri import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cub import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cuw import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cxr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cym import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cyp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cze import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0deu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dji import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dma import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dnk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dom import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dza import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ecu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0egy import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0eri import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0esh import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0esp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0est import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0eth import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fin import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fji import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0flk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fra import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fro import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fsm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gab import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gbr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0geo import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ggy import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gha import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gib import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gin import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0glp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gmb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gnb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gnq import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grc import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gtm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0guf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gum import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0guy import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hkg import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hmd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hnd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0per import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0png import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0som import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB,
    )
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE,
    )


T = TypeVar(
    "T", bound="QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0"
)


@_attrs_define
class QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0:
    """
    Attributes:
        usa (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA |
            Unset):
        gbr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR |
            Unset):
        fra (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA |
            Unset):
        ind (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND |
            Unset):
        bra (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA |
            Unset):
        deu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU |
            Unset):
        esp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP |
            Unset):
        can (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN |
            Unset):
        aus (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS |
            Unset):
        nld (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD |
            Unset):
        ita (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA |
            Unset):
        zaf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF |
            Unset):
        bel (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL |
            Unset):
        chn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN |
            Unset):
        tur (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR |
            Unset):
        mex (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX |
            Unset):
        che (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE |
            Unset):
        nor (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR |
            Unset):
        are (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE |
            Unset):
        swe (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE |
            Unset):
        pol (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL |
            Unset):
        idn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN |
            Unset):
        arg (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG |
            Unset):
        prt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT |
            Unset):
        col (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL |
            Unset):
        chl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL |
            Unset):
        pak (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK |
            Unset):
        dnk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK |
            Unset):
        jpn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN |
            Unset):
        nga (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA |
            Unset):
        sgp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP |
            Unset):
        per (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER |
            Unset):
        nzl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL |
            Unset):
        aut (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT |
            Unset):
        irl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL |
            Unset):
        mys (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS |
            Unset):
        bgd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD |
            Unset):
        egy (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY |
            Unset):
        isr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR |
            Unset):
        sau (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU |
            Unset):
        phl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL |
            Unset):
        fin (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN |
            Unset):
        irn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN |
            Unset):
        rou (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU |
            Unset):
        cze (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE |
            Unset):
        grc (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC |
            Unset):
        hkg (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG |
            Unset):
        hun (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN |
            Unset):
        ken (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN |
            Unset):
        mar (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR |
            Unset):
        vnm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM |
            Unset):
        rus (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS |
            Unset):
        ukr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR |
            Unset):
        ecu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU |
            Unset):
        tha (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA |
            Unset):
        lka (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA |
            Unset):
        kor (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR |
            Unset):
        bgr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR |
            Unset):
        gha (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA |
            Unset):
        srb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB |
            Unset):
        twn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN |
            Unset):
        hrv (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV |
            Unset):
        ltu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU |
            Unset):
        pri (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI |
            Unset):
        svk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK |
            Unset):
        tun (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN |
            Unset):
        est (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST |
            Unset):
        ven (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN |
            Unset):
        cri (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI |
            Unset):
        pan (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN |
            Unset):
        ury (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY |
            Unset):
        lbn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN |
            Unset):
        lux (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX |
            Unset):
        cyp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP |
            Unset):
        npl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL |
            Unset):
        jor (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR |
            Unset):
        svn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN |
            Unset):
        mtq (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ |
            Unset):
        qat (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT |
            Unset):
        glp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP |
            Unset):
        uga (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA |
            Unset):
        dza (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA |
            Unset):
        gtm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM |
            Unset):
        cmr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR |
            Unset):
        lva (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA |
            Unset):
        dom (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM |
            Unset):
        aze (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE |
            Unset):
        geo (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO |
            Unset):
        sen (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN |
            Unset):
        tza (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA |
            Unset):
        zwe (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE |
            Unset):
        kwt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT |
            Unset):
        mlt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT |
            Unset):
        omn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN |
            Unset):
        bol (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL |
            Unset):
        slv (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV |
            Unset):
        arm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM |
            Unset):
        pry (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY |
            Unset):
        irq (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ |
            Unset):
        khm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM |
            Unset):
        bih (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH |
            Unset):
        ago (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO |
            Unset):
        bhr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR |
            Unset):
        alb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB |
            Unset):
        kaz (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ |
            Unset):
        civ (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV |
            Unset):
        eth (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH |
            Unset):
        mus (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS |
            Unset):
        zmb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB |
            Unset):
        mkd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD |
            Unset):
        cod (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD |
            Unset):
        blr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR |
            Unset):
        moz (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ |
            Unset):
        reu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU |
            Unset):
        tto (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO |
            Unset):
        guf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF |
            Unset):
        isl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL |
            Unset):
        mmr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR |
            Unset):
        hnd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND |
            Unset):
        rwa (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA |
            Unset):
        mdg (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG |
            Unset):
        ben (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN |
            Unset):
        uzb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB |
            Unset):
        nam (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM |
            Unset):
        bwa (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA |
            Unset):
        mda (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA |
            Unset):
        jey (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY |
            Unset):
        nic (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC |
            Unset):
        sdn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN |
            Unset):
        jam (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM |
            Unset):
        imn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN |
            Unset):
        bfa (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA |
            Unset):
        mng (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG |
            Unset):
        mne (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE |
            Unset):
        mco (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO |
            Unset):
        tgo (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO |
            Unset):
        afg (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG |
            Unset):
        lby (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY |
            Unset):
        xkx (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX |
            Unset):
        cym (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM |
            Unset):
        mwi (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI |
            Unset):
        som (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM |
            Unset):
        png (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG |
            Unset):
        mdv (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV |
            Unset):
        mli (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI |
            Unset):
        gin (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN |
            Unset):
        pse (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE |
            Unset):
        gab (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB |
            Unset):
        lie (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE |
            Unset):
        hti (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI |
            Unset):
        syr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR |
            Unset):
        brb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB |
            Unset):
        yem (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM |
            Unset):
        ggy (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY |
            Unset):
        ncl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL |
            Unset):
        and_ (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND |
            Unset):
        sur (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR |
            Unset):
        myt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT |
            Unset):
        kgz (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ |
            Unset):
        bhs (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS |
            Unset):
        gib (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB |
            Unset):
        cog (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG |
            Unset):
        fji (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI |
            Unset):
        blm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM |
            Unset):
        cuw (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW |
            Unset):
        cub (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB |
            Unset):
        sle (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE |
            Unset):
        blz (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ |
            Unset):
        ner (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER |
            Unset):
        lbr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR |
            Unset):
        vir (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR |
            Unset):
        pyf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF |
            Unset):
        gum (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM |
            Unset):
        mrt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT |
            Unset):
        abw (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW |
            Unset):
        syc (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC |
            Unset):
        guy (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY |
            Unset):
        lso (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO |
            Unset):
        swz (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ |
            Unset):
        ssd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD |
            Unset):
        lca (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA |
            Unset):
        mac (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC |
            Unset):
        smr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR |
            Unset):
        lao (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO |
            Unset):
        brn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN |
            Unset):
        tcd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD |
            Unset):
        bmu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU |
            Unset):
        vgb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB |
            Unset):
        prk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK |
            Unset):
        btn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN |
            Unset):
        bdi (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI |
            Unset):
        fro (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO |
            Unset):
        tjk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK |
            Unset):
        gmb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB |
            Unset):
        stp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP |
            Unset):
        ant (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT |
            Unset):
        vct (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT |
            Unset):
        dji (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI |
            Unset):
        cpv (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV |
            Unset):
        tkm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM |
            Unset):
        atg (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG |
            Unset):
        tca (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA |
            Unset):
        kna (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA |
            Unset):
        grd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD |
            Unset):
        asm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM |
            Unset):
        vut (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT |
            Unset):
        gnq (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ |
            Unset):
        grl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL |
            Unset):
        sxm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM |
            Unset):
        mnp (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP |
            Unset):
        com (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM |
            Unset):
        tls (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS |
            Unset):
        sjm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM |
            Unset):
        caf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF |
            Unset):
        dma (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA |
            Unset):
        maf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF |
            Unset):
        wsm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM |
            Unset):
        bes (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES |
            Unset):
        mhl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL |
            Unset):
        aia (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA |
            Unset):
        ton (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON |
            Unset):
        cok (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK |
            Unset):
        slb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB |
            Unset):
        spm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM |
            Unset):
        gnb (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB |
            Unset):
        ata (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA |
            Unset):
        tuv (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV |
            Unset):
        ala (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA |
            Unset):
        iot (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT |
            Unset):
        eri (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI |
            Unset):
        plw (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW |
            Unset):
        fsm (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM |
            Unset):
        nru (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU |
            Unset):
        pcn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN |
            Unset):
        flk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK |
            Unset):
        msr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR |
            Unset):
        vat (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT |
            Unset):
        kir (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR |
            Unset):
        shn (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN |
            Unset):
        niu (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU |
            Unset):
        wlf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF |
            Unset):
        hmd (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD |
            Unset):
        cxr (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR |
            Unset):
        nfk (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK |
            Unset):
        atf (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF |
            Unset):
        cck (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK |
            Unset):
        sgs (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS |
            Unset):
        bvt (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT |
            Unset):
        umi (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI |
            Unset):
        esh (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH |
            Unset):
        tkl (QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL |
            Unset):
    """

    usa: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA | Unset
    ) = UNSET
    gbr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR | Unset
    ) = UNSET
    fra: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA | Unset
    ) = UNSET
    ind: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND | Unset
    ) = UNSET
    bra: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA | Unset
    ) = UNSET
    deu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU | Unset
    ) = UNSET
    esp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP | Unset
    ) = UNSET
    can: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN | Unset
    ) = UNSET
    aus: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS | Unset
    ) = UNSET
    nld: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD | Unset
    ) = UNSET
    ita: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA | Unset
    ) = UNSET
    zaf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF | Unset
    ) = UNSET
    bel: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL | Unset
    ) = UNSET
    chn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN | Unset
    ) = UNSET
    tur: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR | Unset
    ) = UNSET
    mex: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX | Unset
    ) = UNSET
    che: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE | Unset
    ) = UNSET
    nor: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR | Unset
    ) = UNSET
    are: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE | Unset
    ) = UNSET
    swe: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE | Unset
    ) = UNSET
    pol: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL | Unset
    ) = UNSET
    idn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN | Unset
    ) = UNSET
    arg: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG | Unset
    ) = UNSET
    prt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT | Unset
    ) = UNSET
    col: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL | Unset
    ) = UNSET
    chl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL | Unset
    ) = UNSET
    pak: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK | Unset
    ) = UNSET
    dnk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK | Unset
    ) = UNSET
    jpn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN | Unset
    ) = UNSET
    nga: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA | Unset
    ) = UNSET
    sgp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP | Unset
    ) = UNSET
    per: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER | Unset
    ) = UNSET
    nzl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL | Unset
    ) = UNSET
    aut: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT | Unset
    ) = UNSET
    irl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL | Unset
    ) = UNSET
    mys: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS | Unset
    ) = UNSET
    bgd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD | Unset
    ) = UNSET
    egy: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY | Unset
    ) = UNSET
    isr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR | Unset
    ) = UNSET
    sau: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU | Unset
    ) = UNSET
    phl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL | Unset
    ) = UNSET
    fin: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN | Unset
    ) = UNSET
    irn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN | Unset
    ) = UNSET
    rou: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU | Unset
    ) = UNSET
    cze: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE | Unset
    ) = UNSET
    grc: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC | Unset
    ) = UNSET
    hkg: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG | Unset
    ) = UNSET
    hun: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN | Unset
    ) = UNSET
    ken: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN | Unset
    ) = UNSET
    mar: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR | Unset
    ) = UNSET
    vnm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM | Unset
    ) = UNSET
    rus: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS | Unset
    ) = UNSET
    ukr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR | Unset
    ) = UNSET
    ecu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU | Unset
    ) = UNSET
    tha: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA | Unset
    ) = UNSET
    lka: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA | Unset
    ) = UNSET
    kor: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR | Unset
    ) = UNSET
    bgr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR | Unset
    ) = UNSET
    gha: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA | Unset
    ) = UNSET
    srb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB | Unset
    ) = UNSET
    twn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN | Unset
    ) = UNSET
    hrv: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV | Unset
    ) = UNSET
    ltu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU | Unset
    ) = UNSET
    pri: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI | Unset
    ) = UNSET
    svk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK | Unset
    ) = UNSET
    tun: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN | Unset
    ) = UNSET
    est: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST | Unset
    ) = UNSET
    ven: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN | Unset
    ) = UNSET
    cri: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI | Unset
    ) = UNSET
    pan: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN | Unset
    ) = UNSET
    ury: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY | Unset
    ) = UNSET
    lbn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN | Unset
    ) = UNSET
    lux: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX | Unset
    ) = UNSET
    cyp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP | Unset
    ) = UNSET
    npl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL | Unset
    ) = UNSET
    jor: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR | Unset
    ) = UNSET
    svn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN | Unset
    ) = UNSET
    mtq: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ | Unset
    ) = UNSET
    qat: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT | Unset
    ) = UNSET
    glp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP | Unset
    ) = UNSET
    uga: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA | Unset
    ) = UNSET
    dza: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA | Unset
    ) = UNSET
    gtm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM | Unset
    ) = UNSET
    cmr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR | Unset
    ) = UNSET
    lva: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA | Unset
    ) = UNSET
    dom: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM | Unset
    ) = UNSET
    aze: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE | Unset
    ) = UNSET
    geo: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO | Unset
    ) = UNSET
    sen: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN | Unset
    ) = UNSET
    tza: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA | Unset
    ) = UNSET
    zwe: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE | Unset
    ) = UNSET
    kwt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT | Unset
    ) = UNSET
    mlt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT | Unset
    ) = UNSET
    omn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN | Unset
    ) = UNSET
    bol: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL | Unset
    ) = UNSET
    slv: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV | Unset
    ) = UNSET
    arm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM | Unset
    ) = UNSET
    pry: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY | Unset
    ) = UNSET
    irq: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ | Unset
    ) = UNSET
    khm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM | Unset
    ) = UNSET
    bih: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH | Unset
    ) = UNSET
    ago: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO | Unset
    ) = UNSET
    bhr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR | Unset
    ) = UNSET
    alb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB | Unset
    ) = UNSET
    kaz: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ | Unset
    ) = UNSET
    civ: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV | Unset
    ) = UNSET
    eth: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH | Unset
    ) = UNSET
    mus: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS | Unset
    ) = UNSET
    zmb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB | Unset
    ) = UNSET
    mkd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD | Unset
    ) = UNSET
    cod: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD | Unset
    ) = UNSET
    blr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR | Unset
    ) = UNSET
    moz: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ | Unset
    ) = UNSET
    reu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU | Unset
    ) = UNSET
    tto: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO | Unset
    ) = UNSET
    guf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF | Unset
    ) = UNSET
    isl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL | Unset
    ) = UNSET
    mmr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR | Unset
    ) = UNSET
    hnd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND | Unset
    ) = UNSET
    rwa: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA | Unset
    ) = UNSET
    mdg: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG | Unset
    ) = UNSET
    ben: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN | Unset
    ) = UNSET
    uzb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB | Unset
    ) = UNSET
    nam: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM | Unset
    ) = UNSET
    bwa: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA | Unset
    ) = UNSET
    mda: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA | Unset
    ) = UNSET
    jey: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY | Unset
    ) = UNSET
    nic: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC | Unset
    ) = UNSET
    sdn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN | Unset
    ) = UNSET
    jam: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM | Unset
    ) = UNSET
    imn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN | Unset
    ) = UNSET
    bfa: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA | Unset
    ) = UNSET
    mng: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG | Unset
    ) = UNSET
    mne: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE | Unset
    ) = UNSET
    mco: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO | Unset
    ) = UNSET
    tgo: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO | Unset
    ) = UNSET
    afg: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG | Unset
    ) = UNSET
    lby: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY | Unset
    ) = UNSET
    xkx: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX | Unset
    ) = UNSET
    cym: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM | Unset
    ) = UNSET
    mwi: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI | Unset
    ) = UNSET
    som: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM | Unset
    ) = UNSET
    png: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG | Unset
    ) = UNSET
    mdv: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV | Unset
    ) = UNSET
    mli: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI | Unset
    ) = UNSET
    gin: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN | Unset
    ) = UNSET
    pse: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE | Unset
    ) = UNSET
    gab: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB | Unset
    ) = UNSET
    lie: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE | Unset
    ) = UNSET
    hti: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI | Unset
    ) = UNSET
    syr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR | Unset
    ) = UNSET
    brb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB | Unset
    ) = UNSET
    yem: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM | Unset
    ) = UNSET
    ggy: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY | Unset
    ) = UNSET
    ncl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL | Unset
    ) = UNSET
    and_: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND | Unset
    ) = UNSET
    sur: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR | Unset
    ) = UNSET
    myt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT | Unset
    ) = UNSET
    kgz: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ | Unset
    ) = UNSET
    bhs: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS | Unset
    ) = UNSET
    gib: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB | Unset
    ) = UNSET
    cog: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG | Unset
    ) = UNSET
    fji: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI | Unset
    ) = UNSET
    blm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM | Unset
    ) = UNSET
    cuw: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW | Unset
    ) = UNSET
    cub: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB | Unset
    ) = UNSET
    sle: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE | Unset
    ) = UNSET
    blz: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ | Unset
    ) = UNSET
    ner: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER | Unset
    ) = UNSET
    lbr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR | Unset
    ) = UNSET
    vir: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR | Unset
    ) = UNSET
    pyf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF | Unset
    ) = UNSET
    gum: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM | Unset
    ) = UNSET
    mrt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT | Unset
    ) = UNSET
    abw: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW | Unset
    ) = UNSET
    syc: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC | Unset
    ) = UNSET
    guy: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY | Unset
    ) = UNSET
    lso: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO | Unset
    ) = UNSET
    swz: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ | Unset
    ) = UNSET
    ssd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD | Unset
    ) = UNSET
    lca: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA | Unset
    ) = UNSET
    mac: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC | Unset
    ) = UNSET
    smr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR | Unset
    ) = UNSET
    lao: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO | Unset
    ) = UNSET
    brn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN | Unset
    ) = UNSET
    tcd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD | Unset
    ) = UNSET
    bmu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU | Unset
    ) = UNSET
    vgb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB | Unset
    ) = UNSET
    prk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK | Unset
    ) = UNSET
    btn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN | Unset
    ) = UNSET
    bdi: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI | Unset
    ) = UNSET
    fro: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO | Unset
    ) = UNSET
    tjk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK | Unset
    ) = UNSET
    gmb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB | Unset
    ) = UNSET
    stp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP | Unset
    ) = UNSET
    ant: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT | Unset
    ) = UNSET
    vct: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT | Unset
    ) = UNSET
    dji: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI | Unset
    ) = UNSET
    cpv: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV | Unset
    ) = UNSET
    tkm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM | Unset
    ) = UNSET
    atg: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG | Unset
    ) = UNSET
    tca: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA | Unset
    ) = UNSET
    kna: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA | Unset
    ) = UNSET
    grd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD | Unset
    ) = UNSET
    asm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM | Unset
    ) = UNSET
    vut: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT | Unset
    ) = UNSET
    gnq: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ | Unset
    ) = UNSET
    grl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL | Unset
    ) = UNSET
    sxm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM | Unset
    ) = UNSET
    mnp: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP | Unset
    ) = UNSET
    com: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM | Unset
    ) = UNSET
    tls: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS | Unset
    ) = UNSET
    sjm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM | Unset
    ) = UNSET
    caf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF | Unset
    ) = UNSET
    dma: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA | Unset
    ) = UNSET
    maf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF | Unset
    ) = UNSET
    wsm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM | Unset
    ) = UNSET
    bes: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES | Unset
    ) = UNSET
    mhl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL | Unset
    ) = UNSET
    aia: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA | Unset
    ) = UNSET
    ton: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON | Unset
    ) = UNSET
    cok: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK | Unset
    ) = UNSET
    slb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB | Unset
    ) = UNSET
    spm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM | Unset
    ) = UNSET
    gnb: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB | Unset
    ) = UNSET
    ata: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA | Unset
    ) = UNSET
    tuv: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV | Unset
    ) = UNSET
    ala: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA | Unset
    ) = UNSET
    iot: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT | Unset
    ) = UNSET
    eri: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI | Unset
    ) = UNSET
    plw: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW | Unset
    ) = UNSET
    fsm: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM | Unset
    ) = UNSET
    nru: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU | Unset
    ) = UNSET
    pcn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN | Unset
    ) = UNSET
    flk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK | Unset
    ) = UNSET
    msr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR | Unset
    ) = UNSET
    vat: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT | Unset
    ) = UNSET
    kir: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR | Unset
    ) = UNSET
    shn: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN | Unset
    ) = UNSET
    niu: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU | Unset
    ) = UNSET
    wlf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF | Unset
    ) = UNSET
    hmd: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD | Unset
    ) = UNSET
    cxr: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR | Unset
    ) = UNSET
    nfk: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK | Unset
    ) = UNSET
    atf: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF | Unset
    ) = UNSET
    cck: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK | Unset
    ) = UNSET
    sgs: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS | Unset
    ) = UNSET
    bvt: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT | Unset
    ) = UNSET
    umi: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI | Unset
    ) = UNSET
    esh: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH | Unset
    ) = UNSET
    tkl: (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0per import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0png import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0som import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB,
        )  # noqa: PLC0415
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE,
        )  # noqa: PLC0415

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
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0abw import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0afg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ago import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aia import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ala import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0alb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0and import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ant import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0are import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0arg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0arm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0asm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ata import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0atf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0atg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aus import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aut import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0aze import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bdi import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bel import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ben import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bes import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bfa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bgd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bgr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bhr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bhs import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bih import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0blz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bmu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bol import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bra import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0brb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0brn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0btn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bvt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0bwa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0caf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0can import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cck import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0che import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0chl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0chn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0civ import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cmr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cod import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cog import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cok import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0col import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0com import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cpv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cri import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cub import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cuw import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cxr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cym import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cyp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0cze import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0deu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dji import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dma import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dnk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dom import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0dza import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ecu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0egy import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0eri import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0esh import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0esp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0est import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0eth import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fin import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fji import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0flk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fra import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fro import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0fsm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gab import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gbr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0geo import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ggy import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gha import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gib import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gin import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0glp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gmb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gnb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gnq import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grc import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0grl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gtm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0guf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0gum import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0guy import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hkg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hmd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hnd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hrv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hti import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0hun import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0idn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0imn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ind import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0iot import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0irq import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0isr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ita import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jam import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jey import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0jpn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kaz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ken import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kgz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0khm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kir import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kna import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0kwt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lao import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lbr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lby import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lca import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lie import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lka import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lso import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ltu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lux import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0lva import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mac import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0maf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mar import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mco import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mda import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdg import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mdv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mex import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mhl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mkd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mli import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mlt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mmr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mne import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mng import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mnp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0moz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mrt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0msr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mtq import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mus import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mwi import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0mys import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0myt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nam import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ncl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ner import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nfk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nga import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nic import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0niu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nld import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nor import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0npl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nru import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0nzl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0omn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pak import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pan import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pcn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0per import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0phl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0plw import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0png import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pol import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pri import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0prt import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pry import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pse import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0pyf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0qat import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0reu import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rou import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rus import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0rwa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sau import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sdn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sen import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sgs import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0shn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sjm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sle import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0slv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0smr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0som import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0spm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0srb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ssd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0stp import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sur import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0svn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swe import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0swz import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0sxm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syc import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0syr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tca import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tcd import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tgo import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tha import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tjk import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkl import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tkm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tls import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ton import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tto import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tun import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tur import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tuv import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0twn import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0tza import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uga import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ukr import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0umi import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ury import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0usa import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0uzb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vat import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vct import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0ven import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vgb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vir import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vnm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0vut import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wlf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0wsm import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0xkx import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0yem import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zaf import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zmb import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0zwe import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _usa = d.pop("USA", UNSET)
        usa: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA
            | Unset
        )
        if isinstance(_usa, Unset):
            usa = UNSET
        else:
            usa = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0USA.from_dict(
                _usa
            )

        _gbr = d.pop("GBR", UNSET)
        gbr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR
            | Unset
        )
        if isinstance(_gbr, Unset):
            gbr = UNSET
        else:
            gbr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GBR.from_dict(
                _gbr
            )

        _fra = d.pop("FRA", UNSET)
        fra: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA
            | Unset
        )
        if isinstance(_fra, Unset):
            fra = UNSET
        else:
            fra = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRA.from_dict(
                _fra
            )

        _ind = d.pop("IND", UNSET)
        ind: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND
            | Unset
        )
        if isinstance(_ind, Unset):
            ind = UNSET
        else:
            ind = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IND.from_dict(
                _ind
            )

        _bra = d.pop("BRA", UNSET)
        bra: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA
            | Unset
        )
        if isinstance(_bra, Unset):
            bra = UNSET
        else:
            bra = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRA.from_dict(
                _bra
            )

        _deu = d.pop("DEU", UNSET)
        deu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU
            | Unset
        )
        if isinstance(_deu, Unset):
            deu = UNSET
        else:
            deu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DEU.from_dict(
                _deu
            )

        _esp = d.pop("ESP", UNSET)
        esp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP
            | Unset
        )
        if isinstance(_esp, Unset):
            esp = UNSET
        else:
            esp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESP.from_dict(
                _esp
            )

        _can = d.pop("CAN", UNSET)
        can: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN
            | Unset
        )
        if isinstance(_can, Unset):
            can = UNSET
        else:
            can = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAN.from_dict(
                _can
            )

        _aus = d.pop("AUS", UNSET)
        aus: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS
            | Unset
        )
        if isinstance(_aus, Unset):
            aus = UNSET
        else:
            aus = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUS.from_dict(
                _aus
            )

        _nld = d.pop("NLD", UNSET)
        nld: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD
            | Unset
        )
        if isinstance(_nld, Unset):
            nld = UNSET
        else:
            nld = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NLD.from_dict(
                _nld
            )

        _ita = d.pop("ITA", UNSET)
        ita: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA
            | Unset
        )
        if isinstance(_ita, Unset):
            ita = UNSET
        else:
            ita = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ITA.from_dict(
                _ita
            )

        _zaf = d.pop("ZAF", UNSET)
        zaf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF
            | Unset
        )
        if isinstance(_zaf, Unset):
            zaf = UNSET
        else:
            zaf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZAF.from_dict(
                _zaf
            )

        _bel = d.pop("BEL", UNSET)
        bel: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL
            | Unset
        )
        if isinstance(_bel, Unset):
            bel = UNSET
        else:
            bel = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEL.from_dict(
                _bel
            )

        _chn = d.pop("CHN", UNSET)
        chn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN
            | Unset
        )
        if isinstance(_chn, Unset):
            chn = UNSET
        else:
            chn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHN.from_dict(
                _chn
            )

        _tur = d.pop("TUR", UNSET)
        tur: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR
            | Unset
        )
        if isinstance(_tur, Unset):
            tur = UNSET
        else:
            tur = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUR.from_dict(
                _tur
            )

        _mex = d.pop("MEX", UNSET)
        mex: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX
            | Unset
        )
        if isinstance(_mex, Unset):
            mex = UNSET
        else:
            mex = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MEX.from_dict(
                _mex
            )

        _che = d.pop("CHE", UNSET)
        che: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE
            | Unset
        )
        if isinstance(_che, Unset):
            che = UNSET
        else:
            che = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHE.from_dict(
                _che
            )

        _nor = d.pop("NOR", UNSET)
        nor: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR
            | Unset
        )
        if isinstance(_nor, Unset):
            nor = UNSET
        else:
            nor = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NOR.from_dict(
                _nor
            )

        _are = d.pop("ARE", UNSET)
        are: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE
            | Unset
        )
        if isinstance(_are, Unset):
            are = UNSET
        else:
            are = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARE.from_dict(
                _are
            )

        _swe = d.pop("SWE", UNSET)
        swe: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE
            | Unset
        )
        if isinstance(_swe, Unset):
            swe = UNSET
        else:
            swe = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWE.from_dict(
                _swe
            )

        _pol = d.pop("POL", UNSET)
        pol: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL
            | Unset
        )
        if isinstance(_pol, Unset):
            pol = UNSET
        else:
            pol = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0POL.from_dict(
                _pol
            )

        _idn = d.pop("IDN", UNSET)
        idn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN
            | Unset
        )
        if isinstance(_idn, Unset):
            idn = UNSET
        else:
            idn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IDN.from_dict(
                _idn
            )

        _arg = d.pop("ARG", UNSET)
        arg: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG
            | Unset
        )
        if isinstance(_arg, Unset):
            arg = UNSET
        else:
            arg = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARG.from_dict(
                _arg
            )

        _prt = d.pop("PRT", UNSET)
        prt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT
            | Unset
        )
        if isinstance(_prt, Unset):
            prt = UNSET
        else:
            prt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRT.from_dict(
                _prt
            )

        _col = d.pop("COL", UNSET)
        col: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL
            | Unset
        )
        if isinstance(_col, Unset):
            col = UNSET
        else:
            col = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COL.from_dict(
                _col
            )

        _chl = d.pop("CHL", UNSET)
        chl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL
            | Unset
        )
        if isinstance(_chl, Unset):
            chl = UNSET
        else:
            chl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CHL.from_dict(
                _chl
            )

        _pak = d.pop("PAK", UNSET)
        pak: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK
            | Unset
        )
        if isinstance(_pak, Unset):
            pak = UNSET
        else:
            pak = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAK.from_dict(
                _pak
            )

        _dnk = d.pop("DNK", UNSET)
        dnk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK
            | Unset
        )
        if isinstance(_dnk, Unset):
            dnk = UNSET
        else:
            dnk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DNK.from_dict(
                _dnk
            )

        _jpn = d.pop("JPN", UNSET)
        jpn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN
            | Unset
        )
        if isinstance(_jpn, Unset):
            jpn = UNSET
        else:
            jpn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JPN.from_dict(
                _jpn
            )

        _nga = d.pop("NGA", UNSET)
        nga: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA
            | Unset
        )
        if isinstance(_nga, Unset):
            nga = UNSET
        else:
            nga = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NGA.from_dict(
                _nga
            )

        _sgp = d.pop("SGP", UNSET)
        sgp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP
            | Unset
        )
        if isinstance(_sgp, Unset):
            sgp = UNSET
        else:
            sgp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGP.from_dict(
                _sgp
            )

        _per = d.pop("PER", UNSET)
        per: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER
            | Unset
        )
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PER.from_dict(
                _per
            )

        _nzl = d.pop("NZL", UNSET)
        nzl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL
            | Unset
        )
        if isinstance(_nzl, Unset):
            nzl = UNSET
        else:
            nzl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NZL.from_dict(
                _nzl
            )

        _aut = d.pop("AUT", UNSET)
        aut: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT
            | Unset
        )
        if isinstance(_aut, Unset):
            aut = UNSET
        else:
            aut = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AUT.from_dict(
                _aut
            )

        _irl = d.pop("IRL", UNSET)
        irl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL
            | Unset
        )
        if isinstance(_irl, Unset):
            irl = UNSET
        else:
            irl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRL.from_dict(
                _irl
            )

        _mys = d.pop("MYS", UNSET)
        mys: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS
            | Unset
        )
        if isinstance(_mys, Unset):
            mys = UNSET
        else:
            mys = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYS.from_dict(
                _mys
            )

        _bgd = d.pop("BGD", UNSET)
        bgd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD
            | Unset
        )
        if isinstance(_bgd, Unset):
            bgd = UNSET
        else:
            bgd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGD.from_dict(
                _bgd
            )

        _egy = d.pop("EGY", UNSET)
        egy: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY
            | Unset
        )
        if isinstance(_egy, Unset):
            egy = UNSET
        else:
            egy = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EGY.from_dict(
                _egy
            )

        _isr = d.pop("ISR", UNSET)
        isr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR
            | Unset
        )
        if isinstance(_isr, Unset):
            isr = UNSET
        else:
            isr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISR.from_dict(
                _isr
            )

        _sau = d.pop("SAU", UNSET)
        sau: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU
            | Unset
        )
        if isinstance(_sau, Unset):
            sau = UNSET
        else:
            sau = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SAU.from_dict(
                _sau
            )

        _phl = d.pop("PHL", UNSET)
        phl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL
            | Unset
        )
        if isinstance(_phl, Unset):
            phl = UNSET
        else:
            phl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PHL.from_dict(
                _phl
            )

        _fin = d.pop("FIN", UNSET)
        fin: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN
            | Unset
        )
        if isinstance(_fin, Unset):
            fin = UNSET
        else:
            fin = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FIN.from_dict(
                _fin
            )

        _irn = d.pop("IRN", UNSET)
        irn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN
            | Unset
        )
        if isinstance(_irn, Unset):
            irn = UNSET
        else:
            irn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRN.from_dict(
                _irn
            )

        _rou = d.pop("ROU", UNSET)
        rou: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU
            | Unset
        )
        if isinstance(_rou, Unset):
            rou = UNSET
        else:
            rou = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ROU.from_dict(
                _rou
            )

        _cze = d.pop("CZE", UNSET)
        cze: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE
            | Unset
        )
        if isinstance(_cze, Unset):
            cze = UNSET
        else:
            cze = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CZE.from_dict(
                _cze
            )

        _grc = d.pop("GRC", UNSET)
        grc: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC
            | Unset
        )
        if isinstance(_grc, Unset):
            grc = UNSET
        else:
            grc = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRC.from_dict(
                _grc
            )

        _hkg = d.pop("HKG", UNSET)
        hkg: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG
            | Unset
        )
        if isinstance(_hkg, Unset):
            hkg = UNSET
        else:
            hkg = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HKG.from_dict(
                _hkg
            )

        _hun = d.pop("HUN", UNSET)
        hun: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN
            | Unset
        )
        if isinstance(_hun, Unset):
            hun = UNSET
        else:
            hun = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HUN.from_dict(
                _hun
            )

        _ken = d.pop("KEN", UNSET)
        ken: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN
            | Unset
        )
        if isinstance(_ken, Unset):
            ken = UNSET
        else:
            ken = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KEN.from_dict(
                _ken
            )

        _mar = d.pop("MAR", UNSET)
        mar: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR
            | Unset
        )
        if isinstance(_mar, Unset):
            mar = UNSET
        else:
            mar = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAR.from_dict(
                _mar
            )

        _vnm = d.pop("VNM", UNSET)
        vnm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM
            | Unset
        )
        if isinstance(_vnm, Unset):
            vnm = UNSET
        else:
            vnm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VNM.from_dict(
                _vnm
            )

        _rus = d.pop("RUS", UNSET)
        rus: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS
            | Unset
        )
        if isinstance(_rus, Unset):
            rus = UNSET
        else:
            rus = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RUS.from_dict(
                _rus
            )

        _ukr = d.pop("UKR", UNSET)
        ukr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR
            | Unset
        )
        if isinstance(_ukr, Unset):
            ukr = UNSET
        else:
            ukr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UKR.from_dict(
                _ukr
            )

        _ecu = d.pop("ECU", UNSET)
        ecu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU
            | Unset
        )
        if isinstance(_ecu, Unset):
            ecu = UNSET
        else:
            ecu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ECU.from_dict(
                _ecu
            )

        _tha = d.pop("THA", UNSET)
        tha: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA
            | Unset
        )
        if isinstance(_tha, Unset):
            tha = UNSET
        else:
            tha = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0THA.from_dict(
                _tha
            )

        _lka = d.pop("LKA", UNSET)
        lka: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA
            | Unset
        )
        if isinstance(_lka, Unset):
            lka = UNSET
        else:
            lka = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LKA.from_dict(
                _lka
            )

        _kor = d.pop("KOR", UNSET)
        kor: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR
            | Unset
        )
        if isinstance(_kor, Unset):
            kor = UNSET
        else:
            kor = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KOR.from_dict(
                _kor
            )

        _bgr = d.pop("BGR", UNSET)
        bgr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR
            | Unset
        )
        if isinstance(_bgr, Unset):
            bgr = UNSET
        else:
            bgr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BGR.from_dict(
                _bgr
            )

        _gha = d.pop("GHA", UNSET)
        gha: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA
            | Unset
        )
        if isinstance(_gha, Unset):
            gha = UNSET
        else:
            gha = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GHA.from_dict(
                _gha
            )

        _srb = d.pop("SRB", UNSET)
        srb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB
            | Unset
        )
        if isinstance(_srb, Unset):
            srb = UNSET
        else:
            srb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SRB.from_dict(
                _srb
            )

        _twn = d.pop("TWN", UNSET)
        twn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN
            | Unset
        )
        if isinstance(_twn, Unset):
            twn = UNSET
        else:
            twn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TWN.from_dict(
                _twn
            )

        _hrv = d.pop("HRV", UNSET)
        hrv: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV
            | Unset
        )
        if isinstance(_hrv, Unset):
            hrv = UNSET
        else:
            hrv = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HRV.from_dict(
                _hrv
            )

        _ltu = d.pop("LTU", UNSET)
        ltu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU
            | Unset
        )
        if isinstance(_ltu, Unset):
            ltu = UNSET
        else:
            ltu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LTU.from_dict(
                _ltu
            )

        _pri = d.pop("PRI", UNSET)
        pri: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI
            | Unset
        )
        if isinstance(_pri, Unset):
            pri = UNSET
        else:
            pri = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRI.from_dict(
                _pri
            )

        _svk = d.pop("SVK", UNSET)
        svk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK
            | Unset
        )
        if isinstance(_svk, Unset):
            svk = UNSET
        else:
            svk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVK.from_dict(
                _svk
            )

        _tun = d.pop("TUN", UNSET)
        tun: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN
            | Unset
        )
        if isinstance(_tun, Unset):
            tun = UNSET
        else:
            tun = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUN.from_dict(
                _tun
            )

        _est = d.pop("EST", UNSET)
        est: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST
            | Unset
        )
        if isinstance(_est, Unset):
            est = UNSET
        else:
            est = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0EST.from_dict(
                _est
            )

        _ven = d.pop("VEN", UNSET)
        ven: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN
            | Unset
        )
        if isinstance(_ven, Unset):
            ven = UNSET
        else:
            ven = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VEN.from_dict(
                _ven
            )

        _cri = d.pop("CRI", UNSET)
        cri: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI
            | Unset
        )
        if isinstance(_cri, Unset):
            cri = UNSET
        else:
            cri = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CRI.from_dict(
                _cri
            )

        _pan = d.pop("PAN", UNSET)
        pan: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN
            | Unset
        )
        if isinstance(_pan, Unset):
            pan = UNSET
        else:
            pan = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PAN.from_dict(
                _pan
            )

        _ury = d.pop("URY", UNSET)
        ury: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY
            | Unset
        )
        if isinstance(_ury, Unset):
            ury = UNSET
        else:
            ury = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0URY.from_dict(
                _ury
            )

        _lbn = d.pop("LBN", UNSET)
        lbn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN
            | Unset
        )
        if isinstance(_lbn, Unset):
            lbn = UNSET
        else:
            lbn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBN.from_dict(
                _lbn
            )

        _lux = d.pop("LUX", UNSET)
        lux: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX
            | Unset
        )
        if isinstance(_lux, Unset):
            lux = UNSET
        else:
            lux = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LUX.from_dict(
                _lux
            )

        _cyp = d.pop("CYP", UNSET)
        cyp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP
            | Unset
        )
        if isinstance(_cyp, Unset):
            cyp = UNSET
        else:
            cyp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYP.from_dict(
                _cyp
            )

        _npl = d.pop("NPL", UNSET)
        npl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL
            | Unset
        )
        if isinstance(_npl, Unset):
            npl = UNSET
        else:
            npl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NPL.from_dict(
                _npl
            )

        _jor = d.pop("JOR", UNSET)
        jor: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR
            | Unset
        )
        if isinstance(_jor, Unset):
            jor = UNSET
        else:
            jor = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JOR.from_dict(
                _jor
            )

        _svn = d.pop("SVN", UNSET)
        svn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN
            | Unset
        )
        if isinstance(_svn, Unset):
            svn = UNSET
        else:
            svn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SVN.from_dict(
                _svn
            )

        _mtq = d.pop("MTQ", UNSET)
        mtq: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ
            | Unset
        )
        if isinstance(_mtq, Unset):
            mtq = UNSET
        else:
            mtq = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MTQ.from_dict(
                _mtq
            )

        _qat = d.pop("QAT", UNSET)
        qat: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT
            | Unset
        )
        if isinstance(_qat, Unset):
            qat = UNSET
        else:
            qat = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0QAT.from_dict(
                _qat
            )

        _glp = d.pop("GLP", UNSET)
        glp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP
            | Unset
        )
        if isinstance(_glp, Unset):
            glp = UNSET
        else:
            glp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GLP.from_dict(
                _glp
            )

        _uga = d.pop("UGA", UNSET)
        uga: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA
            | Unset
        )
        if isinstance(_uga, Unset):
            uga = UNSET
        else:
            uga = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UGA.from_dict(
                _uga
            )

        _dza = d.pop("DZA", UNSET)
        dza: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA
            | Unset
        )
        if isinstance(_dza, Unset):
            dza = UNSET
        else:
            dza = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DZA.from_dict(
                _dza
            )

        _gtm = d.pop("GTM", UNSET)
        gtm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM
            | Unset
        )
        if isinstance(_gtm, Unset):
            gtm = UNSET
        else:
            gtm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GTM.from_dict(
                _gtm
            )

        _cmr = d.pop("CMR", UNSET)
        cmr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR
            | Unset
        )
        if isinstance(_cmr, Unset):
            cmr = UNSET
        else:
            cmr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CMR.from_dict(
                _cmr
            )

        _lva = d.pop("LVA", UNSET)
        lva: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA
            | Unset
        )
        if isinstance(_lva, Unset):
            lva = UNSET
        else:
            lva = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LVA.from_dict(
                _lva
            )

        _dom = d.pop("DOM", UNSET)
        dom: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM
            | Unset
        )
        if isinstance(_dom, Unset):
            dom = UNSET
        else:
            dom = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DOM.from_dict(
                _dom
            )

        _aze = d.pop("AZE", UNSET)
        aze: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE
            | Unset
        )
        if isinstance(_aze, Unset):
            aze = UNSET
        else:
            aze = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AZE.from_dict(
                _aze
            )

        _geo = d.pop("GEO", UNSET)
        geo: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO
            | Unset
        )
        if isinstance(_geo, Unset):
            geo = UNSET
        else:
            geo = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GEO.from_dict(
                _geo
            )

        _sen = d.pop("SEN", UNSET)
        sen: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN
            | Unset
        )
        if isinstance(_sen, Unset):
            sen = UNSET
        else:
            sen = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SEN.from_dict(
                _sen
            )

        _tza = d.pop("TZA", UNSET)
        tza: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA
            | Unset
        )
        if isinstance(_tza, Unset):
            tza = UNSET
        else:
            tza = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TZA.from_dict(
                _tza
            )

        _zwe = d.pop("ZWE", UNSET)
        zwe: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE
            | Unset
        )
        if isinstance(_zwe, Unset):
            zwe = UNSET
        else:
            zwe = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZWE.from_dict(
                _zwe
            )

        _kwt = d.pop("KWT", UNSET)
        kwt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT
            | Unset
        )
        if isinstance(_kwt, Unset):
            kwt = UNSET
        else:
            kwt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KWT.from_dict(
                _kwt
            )

        _mlt = d.pop("MLT", UNSET)
        mlt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT
            | Unset
        )
        if isinstance(_mlt, Unset):
            mlt = UNSET
        else:
            mlt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLT.from_dict(
                _mlt
            )

        _omn = d.pop("OMN", UNSET)
        omn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN
            | Unset
        )
        if isinstance(_omn, Unset):
            omn = UNSET
        else:
            omn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0OMN.from_dict(
                _omn
            )

        _bol = d.pop("BOL", UNSET)
        bol: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL
            | Unset
        )
        if isinstance(_bol, Unset):
            bol = UNSET
        else:
            bol = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BOL.from_dict(
                _bol
            )

        _slv = d.pop("SLV", UNSET)
        slv: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV
            | Unset
        )
        if isinstance(_slv, Unset):
            slv = UNSET
        else:
            slv = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLV.from_dict(
                _slv
            )

        _arm = d.pop("ARM", UNSET)
        arm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM
            | Unset
        )
        if isinstance(_arm, Unset):
            arm = UNSET
        else:
            arm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ARM.from_dict(
                _arm
            )

        _pry = d.pop("PRY", UNSET)
        pry: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY
            | Unset
        )
        if isinstance(_pry, Unset):
            pry = UNSET
        else:
            pry = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRY.from_dict(
                _pry
            )

        _irq = d.pop("IRQ", UNSET)
        irq: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ
            | Unset
        )
        if isinstance(_irq, Unset):
            irq = UNSET
        else:
            irq = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IRQ.from_dict(
                _irq
            )

        _khm = d.pop("KHM", UNSET)
        khm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM
            | Unset
        )
        if isinstance(_khm, Unset):
            khm = UNSET
        else:
            khm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KHM.from_dict(
                _khm
            )

        _bih = d.pop("BIH", UNSET)
        bih: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH
            | Unset
        )
        if isinstance(_bih, Unset):
            bih = UNSET
        else:
            bih = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BIH.from_dict(
                _bih
            )

        _ago = d.pop("AGO", UNSET)
        ago: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO
            | Unset
        )
        if isinstance(_ago, Unset):
            ago = UNSET
        else:
            ago = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AGO.from_dict(
                _ago
            )

        _bhr = d.pop("BHR", UNSET)
        bhr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR
            | Unset
        )
        if isinstance(_bhr, Unset):
            bhr = UNSET
        else:
            bhr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHR.from_dict(
                _bhr
            )

        _alb = d.pop("ALB", UNSET)
        alb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB
            | Unset
        )
        if isinstance(_alb, Unset):
            alb = UNSET
        else:
            alb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALB.from_dict(
                _alb
            )

        _kaz = d.pop("KAZ", UNSET)
        kaz: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ
            | Unset
        )
        if isinstance(_kaz, Unset):
            kaz = UNSET
        else:
            kaz = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KAZ.from_dict(
                _kaz
            )

        _civ = d.pop("CIV", UNSET)
        civ: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV
            | Unset
        )
        if isinstance(_civ, Unset):
            civ = UNSET
        else:
            civ = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CIV.from_dict(
                _civ
            )

        _eth = d.pop("ETH", UNSET)
        eth: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH
            | Unset
        )
        if isinstance(_eth, Unset):
            eth = UNSET
        else:
            eth = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ETH.from_dict(
                _eth
            )

        _mus = d.pop("MUS", UNSET)
        mus: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS
            | Unset
        )
        if isinstance(_mus, Unset):
            mus = UNSET
        else:
            mus = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MUS.from_dict(
                _mus
            )

        _zmb = d.pop("ZMB", UNSET)
        zmb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB
            | Unset
        )
        if isinstance(_zmb, Unset):
            zmb = UNSET
        else:
            zmb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ZMB.from_dict(
                _zmb
            )

        _mkd = d.pop("MKD", UNSET)
        mkd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD
            | Unset
        )
        if isinstance(_mkd, Unset):
            mkd = UNSET
        else:
            mkd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MKD.from_dict(
                _mkd
            )

        _cod = d.pop("COD", UNSET)
        cod: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD
            | Unset
        )
        if isinstance(_cod, Unset):
            cod = UNSET
        else:
            cod = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COD.from_dict(
                _cod
            )

        _blr = d.pop("BLR", UNSET)
        blr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR
            | Unset
        )
        if isinstance(_blr, Unset):
            blr = UNSET
        else:
            blr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLR.from_dict(
                _blr
            )

        _moz = d.pop("MOZ", UNSET)
        moz: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ
            | Unset
        )
        if isinstance(_moz, Unset):
            moz = UNSET
        else:
            moz = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MOZ.from_dict(
                _moz
            )

        _reu = d.pop("REU", UNSET)
        reu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU
            | Unset
        )
        if isinstance(_reu, Unset):
            reu = UNSET
        else:
            reu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0REU.from_dict(
                _reu
            )

        _tto = d.pop("TTO", UNSET)
        tto: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO
            | Unset
        )
        if isinstance(_tto, Unset):
            tto = UNSET
        else:
            tto = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TTO.from_dict(
                _tto
            )

        _guf = d.pop("GUF", UNSET)
        guf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF
            | Unset
        )
        if isinstance(_guf, Unset):
            guf = UNSET
        else:
            guf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUF.from_dict(
                _guf
            )

        _isl = d.pop("ISL", UNSET)
        isl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL
            | Unset
        )
        if isinstance(_isl, Unset):
            isl = UNSET
        else:
            isl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ISL.from_dict(
                _isl
            )

        _mmr = d.pop("MMR", UNSET)
        mmr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR
            | Unset
        )
        if isinstance(_mmr, Unset):
            mmr = UNSET
        else:
            mmr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MMR.from_dict(
                _mmr
            )

        _hnd = d.pop("HND", UNSET)
        hnd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND
            | Unset
        )
        if isinstance(_hnd, Unset):
            hnd = UNSET
        else:
            hnd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HND.from_dict(
                _hnd
            )

        _rwa = d.pop("RWA", UNSET)
        rwa: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA
            | Unset
        )
        if isinstance(_rwa, Unset):
            rwa = UNSET
        else:
            rwa = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0RWA.from_dict(
                _rwa
            )

        _mdg = d.pop("MDG", UNSET)
        mdg: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG
            | Unset
        )
        if isinstance(_mdg, Unset):
            mdg = UNSET
        else:
            mdg = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDG.from_dict(
                _mdg
            )

        _ben = d.pop("BEN", UNSET)
        ben: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN
            | Unset
        )
        if isinstance(_ben, Unset):
            ben = UNSET
        else:
            ben = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BEN.from_dict(
                _ben
            )

        _uzb = d.pop("UZB", UNSET)
        uzb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB
            | Unset
        )
        if isinstance(_uzb, Unset):
            uzb = UNSET
        else:
            uzb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UZB.from_dict(
                _uzb
            )

        _nam = d.pop("NAM", UNSET)
        nam: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM
            | Unset
        )
        if isinstance(_nam, Unset):
            nam = UNSET
        else:
            nam = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NAM.from_dict(
                _nam
            )

        _bwa = d.pop("BWA", UNSET)
        bwa: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA
            | Unset
        )
        if isinstance(_bwa, Unset):
            bwa = UNSET
        else:
            bwa = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BWA.from_dict(
                _bwa
            )

        _mda = d.pop("MDA", UNSET)
        mda: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA
            | Unset
        )
        if isinstance(_mda, Unset):
            mda = UNSET
        else:
            mda = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDA.from_dict(
                _mda
            )

        _jey = d.pop("JEY", UNSET)
        jey: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY
            | Unset
        )
        if isinstance(_jey, Unset):
            jey = UNSET
        else:
            jey = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JEY.from_dict(
                _jey
            )

        _nic = d.pop("NIC", UNSET)
        nic: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC
            | Unset
        )
        if isinstance(_nic, Unset):
            nic = UNSET
        else:
            nic = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIC.from_dict(
                _nic
            )

        _sdn = d.pop("SDN", UNSET)
        sdn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN
            | Unset
        )
        if isinstance(_sdn, Unset):
            sdn = UNSET
        else:
            sdn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SDN.from_dict(
                _sdn
            )

        _jam = d.pop("JAM", UNSET)
        jam: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM
            | Unset
        )
        if isinstance(_jam, Unset):
            jam = UNSET
        else:
            jam = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0JAM.from_dict(
                _jam
            )

        _imn = d.pop("IMN", UNSET)
        imn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN
            | Unset
        )
        if isinstance(_imn, Unset):
            imn = UNSET
        else:
            imn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IMN.from_dict(
                _imn
            )

        _bfa = d.pop("BFA", UNSET)
        bfa: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA
            | Unset
        )
        if isinstance(_bfa, Unset):
            bfa = UNSET
        else:
            bfa = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BFA.from_dict(
                _bfa
            )

        _mng = d.pop("MNG", UNSET)
        mng: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG
            | Unset
        )
        if isinstance(_mng, Unset):
            mng = UNSET
        else:
            mng = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNG.from_dict(
                _mng
            )

        _mne = d.pop("MNE", UNSET)
        mne: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE
            | Unset
        )
        if isinstance(_mne, Unset):
            mne = UNSET
        else:
            mne = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNE.from_dict(
                _mne
            )

        _mco = d.pop("MCO", UNSET)
        mco: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO
            | Unset
        )
        if isinstance(_mco, Unset):
            mco = UNSET
        else:
            mco = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MCO.from_dict(
                _mco
            )

        _tgo = d.pop("TGO", UNSET)
        tgo: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO
            | Unset
        )
        if isinstance(_tgo, Unset):
            tgo = UNSET
        else:
            tgo = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TGO.from_dict(
                _tgo
            )

        _afg = d.pop("AFG", UNSET)
        afg: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG
            | Unset
        )
        if isinstance(_afg, Unset):
            afg = UNSET
        else:
            afg = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AFG.from_dict(
                _afg
            )

        _lby = d.pop("LBY", UNSET)
        lby: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY
            | Unset
        )
        if isinstance(_lby, Unset):
            lby = UNSET
        else:
            lby = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBY.from_dict(
                _lby
            )

        _xkx = d.pop("XKX", UNSET)
        xkx: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX
            | Unset
        )
        if isinstance(_xkx, Unset):
            xkx = UNSET
        else:
            xkx = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0XKX.from_dict(
                _xkx
            )

        _cym = d.pop("CYM", UNSET)
        cym: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM
            | Unset
        )
        if isinstance(_cym, Unset):
            cym = UNSET
        else:
            cym = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CYM.from_dict(
                _cym
            )

        _mwi = d.pop("MWI", UNSET)
        mwi: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI
            | Unset
        )
        if isinstance(_mwi, Unset):
            mwi = UNSET
        else:
            mwi = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MWI.from_dict(
                _mwi
            )

        _som = d.pop("SOM", UNSET)
        som: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM
            | Unset
        )
        if isinstance(_som, Unset):
            som = UNSET
        else:
            som = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SOM.from_dict(
                _som
            )

        _png = d.pop("PNG", UNSET)
        png: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG
            | Unset
        )
        if isinstance(_png, Unset):
            png = UNSET
        else:
            png = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PNG.from_dict(
                _png
            )

        _mdv = d.pop("MDV", UNSET)
        mdv: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV
            | Unset
        )
        if isinstance(_mdv, Unset):
            mdv = UNSET
        else:
            mdv = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MDV.from_dict(
                _mdv
            )

        _mli = d.pop("MLI", UNSET)
        mli: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI
            | Unset
        )
        if isinstance(_mli, Unset):
            mli = UNSET
        else:
            mli = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MLI.from_dict(
                _mli
            )

        _gin = d.pop("GIN", UNSET)
        gin: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN
            | Unset
        )
        if isinstance(_gin, Unset):
            gin = UNSET
        else:
            gin = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIN.from_dict(
                _gin
            )

        _pse = d.pop("PSE", UNSET)
        pse: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE
            | Unset
        )
        if isinstance(_pse, Unset):
            pse = UNSET
        else:
            pse = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PSE.from_dict(
                _pse
            )

        _gab = d.pop("GAB", UNSET)
        gab: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB
            | Unset
        )
        if isinstance(_gab, Unset):
            gab = UNSET
        else:
            gab = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GAB.from_dict(
                _gab
            )

        _lie = d.pop("LIE", UNSET)
        lie: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE
            | Unset
        )
        if isinstance(_lie, Unset):
            lie = UNSET
        else:
            lie = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LIE.from_dict(
                _lie
            )

        _hti = d.pop("HTI", UNSET)
        hti: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI
            | Unset
        )
        if isinstance(_hti, Unset):
            hti = UNSET
        else:
            hti = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HTI.from_dict(
                _hti
            )

        _syr = d.pop("SYR", UNSET)
        syr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR
            | Unset
        )
        if isinstance(_syr, Unset):
            syr = UNSET
        else:
            syr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYR.from_dict(
                _syr
            )

        _brb = d.pop("BRB", UNSET)
        brb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB
            | Unset
        )
        if isinstance(_brb, Unset):
            brb = UNSET
        else:
            brb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRB.from_dict(
                _brb
            )

        _yem = d.pop("YEM", UNSET)
        yem: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM
            | Unset
        )
        if isinstance(_yem, Unset):
            yem = UNSET
        else:
            yem = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0YEM.from_dict(
                _yem
            )

        _ggy = d.pop("GGY", UNSET)
        ggy: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY
            | Unset
        )
        if isinstance(_ggy, Unset):
            ggy = UNSET
        else:
            ggy = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GGY.from_dict(
                _ggy
            )

        _ncl = d.pop("NCL", UNSET)
        ncl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL
            | Unset
        )
        if isinstance(_ncl, Unset):
            ncl = UNSET
        else:
            ncl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NCL.from_dict(
                _ncl
            )

        _and_ = d.pop("AND", UNSET)
        and_: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND
            | Unset
        )
        if isinstance(_and_, Unset):
            and_ = UNSET
        else:
            and_ = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AND.from_dict(
                _and_
            )

        _sur = d.pop("SUR", UNSET)
        sur: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR
            | Unset
        )
        if isinstance(_sur, Unset):
            sur = UNSET
        else:
            sur = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SUR.from_dict(
                _sur
            )

        _myt = d.pop("MYT", UNSET)
        myt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT
            | Unset
        )
        if isinstance(_myt, Unset):
            myt = UNSET
        else:
            myt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MYT.from_dict(
                _myt
            )

        _kgz = d.pop("KGZ", UNSET)
        kgz: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ
            | Unset
        )
        if isinstance(_kgz, Unset):
            kgz = UNSET
        else:
            kgz = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KGZ.from_dict(
                _kgz
            )

        _bhs = d.pop("BHS", UNSET)
        bhs: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS
            | Unset
        )
        if isinstance(_bhs, Unset):
            bhs = UNSET
        else:
            bhs = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BHS.from_dict(
                _bhs
            )

        _gib = d.pop("GIB", UNSET)
        gib: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB
            | Unset
        )
        if isinstance(_gib, Unset):
            gib = UNSET
        else:
            gib = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GIB.from_dict(
                _gib
            )

        _cog = d.pop("COG", UNSET)
        cog: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG
            | Unset
        )
        if isinstance(_cog, Unset):
            cog = UNSET
        else:
            cog = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COG.from_dict(
                _cog
            )

        _fji = d.pop("FJI", UNSET)
        fji: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI
            | Unset
        )
        if isinstance(_fji, Unset):
            fji = UNSET
        else:
            fji = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FJI.from_dict(
                _fji
            )

        _blm = d.pop("BLM", UNSET)
        blm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM
            | Unset
        )
        if isinstance(_blm, Unset):
            blm = UNSET
        else:
            blm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLM.from_dict(
                _blm
            )

        _cuw = d.pop("CUW", UNSET)
        cuw: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW
            | Unset
        )
        if isinstance(_cuw, Unset):
            cuw = UNSET
        else:
            cuw = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUW.from_dict(
                _cuw
            )

        _cub = d.pop("CUB", UNSET)
        cub: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB
            | Unset
        )
        if isinstance(_cub, Unset):
            cub = UNSET
        else:
            cub = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CUB.from_dict(
                _cub
            )

        _sle = d.pop("SLE", UNSET)
        sle: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE
            | Unset
        )
        if isinstance(_sle, Unset):
            sle = UNSET
        else:
            sle = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLE.from_dict(
                _sle
            )

        _blz = d.pop("BLZ", UNSET)
        blz: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ
            | Unset
        )
        if isinstance(_blz, Unset):
            blz = UNSET
        else:
            blz = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BLZ.from_dict(
                _blz
            )

        _ner = d.pop("NER", UNSET)
        ner: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER
            | Unset
        )
        if isinstance(_ner, Unset):
            ner = UNSET
        else:
            ner = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NER.from_dict(
                _ner
            )

        _lbr = d.pop("LBR", UNSET)
        lbr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR
            | Unset
        )
        if isinstance(_lbr, Unset):
            lbr = UNSET
        else:
            lbr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LBR.from_dict(
                _lbr
            )

        _vir = d.pop("VIR", UNSET)
        vir: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR
            | Unset
        )
        if isinstance(_vir, Unset):
            vir = UNSET
        else:
            vir = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VIR.from_dict(
                _vir
            )

        _pyf = d.pop("PYF", UNSET)
        pyf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF
            | Unset
        )
        if isinstance(_pyf, Unset):
            pyf = UNSET
        else:
            pyf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PYF.from_dict(
                _pyf
            )

        _gum = d.pop("GUM", UNSET)
        gum: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM
            | Unset
        )
        if isinstance(_gum, Unset):
            gum = UNSET
        else:
            gum = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUM.from_dict(
                _gum
            )

        _mrt = d.pop("MRT", UNSET)
        mrt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT
            | Unset
        )
        if isinstance(_mrt, Unset):
            mrt = UNSET
        else:
            mrt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MRT.from_dict(
                _mrt
            )

        _abw = d.pop("ABW", UNSET)
        abw: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW
            | Unset
        )
        if isinstance(_abw, Unset):
            abw = UNSET
        else:
            abw = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ABW.from_dict(
                _abw
            )

        _syc = d.pop("SYC", UNSET)
        syc: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC
            | Unset
        )
        if isinstance(_syc, Unset):
            syc = UNSET
        else:
            syc = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SYC.from_dict(
                _syc
            )

        _guy = d.pop("GUY", UNSET)
        guy: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY
            | Unset
        )
        if isinstance(_guy, Unset):
            guy = UNSET
        else:
            guy = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GUY.from_dict(
                _guy
            )

        _lso = d.pop("LSO", UNSET)
        lso: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO
            | Unset
        )
        if isinstance(_lso, Unset):
            lso = UNSET
        else:
            lso = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LSO.from_dict(
                _lso
            )

        _swz = d.pop("SWZ", UNSET)
        swz: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ
            | Unset
        )
        if isinstance(_swz, Unset):
            swz = UNSET
        else:
            swz = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SWZ.from_dict(
                _swz
            )

        _ssd = d.pop("SSD", UNSET)
        ssd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD
            | Unset
        )
        if isinstance(_ssd, Unset):
            ssd = UNSET
        else:
            ssd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SSD.from_dict(
                _ssd
            )

        _lca = d.pop("LCA", UNSET)
        lca: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA
            | Unset
        )
        if isinstance(_lca, Unset):
            lca = UNSET
        else:
            lca = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LCA.from_dict(
                _lca
            )

        _mac = d.pop("MAC", UNSET)
        mac: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC
            | Unset
        )
        if isinstance(_mac, Unset):
            mac = UNSET
        else:
            mac = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAC.from_dict(
                _mac
            )

        _smr = d.pop("SMR", UNSET)
        smr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR
            | Unset
        )
        if isinstance(_smr, Unset):
            smr = UNSET
        else:
            smr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SMR.from_dict(
                _smr
            )

        _lao = d.pop("LAO", UNSET)
        lao: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO
            | Unset
        )
        if isinstance(_lao, Unset):
            lao = UNSET
        else:
            lao = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0LAO.from_dict(
                _lao
            )

        _brn = d.pop("BRN", UNSET)
        brn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN
            | Unset
        )
        if isinstance(_brn, Unset):
            brn = UNSET
        else:
            brn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BRN.from_dict(
                _brn
            )

        _tcd = d.pop("TCD", UNSET)
        tcd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD
            | Unset
        )
        if isinstance(_tcd, Unset):
            tcd = UNSET
        else:
            tcd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCD.from_dict(
                _tcd
            )

        _bmu = d.pop("BMU", UNSET)
        bmu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU
            | Unset
        )
        if isinstance(_bmu, Unset):
            bmu = UNSET
        else:
            bmu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BMU.from_dict(
                _bmu
            )

        _vgb = d.pop("VGB", UNSET)
        vgb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB
            | Unset
        )
        if isinstance(_vgb, Unset):
            vgb = UNSET
        else:
            vgb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VGB.from_dict(
                _vgb
            )

        _prk = d.pop("PRK", UNSET)
        prk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK
            | Unset
        )
        if isinstance(_prk, Unset):
            prk = UNSET
        else:
            prk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PRK.from_dict(
                _prk
            )

        _btn = d.pop("BTN", UNSET)
        btn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN
            | Unset
        )
        if isinstance(_btn, Unset):
            btn = UNSET
        else:
            btn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BTN.from_dict(
                _btn
            )

        _bdi = d.pop("BDI", UNSET)
        bdi: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI
            | Unset
        )
        if isinstance(_bdi, Unset):
            bdi = UNSET
        else:
            bdi = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BDI.from_dict(
                _bdi
            )

        _fro = d.pop("FRO", UNSET)
        fro: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO
            | Unset
        )
        if isinstance(_fro, Unset):
            fro = UNSET
        else:
            fro = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FRO.from_dict(
                _fro
            )

        _tjk = d.pop("TJK", UNSET)
        tjk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK
            | Unset
        )
        if isinstance(_tjk, Unset):
            tjk = UNSET
        else:
            tjk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TJK.from_dict(
                _tjk
            )

        _gmb = d.pop("GMB", UNSET)
        gmb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB
            | Unset
        )
        if isinstance(_gmb, Unset):
            gmb = UNSET
        else:
            gmb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GMB.from_dict(
                _gmb
            )

        _stp = d.pop("STP", UNSET)
        stp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP
            | Unset
        )
        if isinstance(_stp, Unset):
            stp = UNSET
        else:
            stp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0STP.from_dict(
                _stp
            )

        _ant = d.pop("ANT", UNSET)
        ant: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT
            | Unset
        )
        if isinstance(_ant, Unset):
            ant = UNSET
        else:
            ant = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ANT.from_dict(
                _ant
            )

        _vct = d.pop("VCT", UNSET)
        vct: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT
            | Unset
        )
        if isinstance(_vct, Unset):
            vct = UNSET
        else:
            vct = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VCT.from_dict(
                _vct
            )

        _dji = d.pop("DJI", UNSET)
        dji: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI
            | Unset
        )
        if isinstance(_dji, Unset):
            dji = UNSET
        else:
            dji = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DJI.from_dict(
                _dji
            )

        _cpv = d.pop("CPV", UNSET)
        cpv: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV
            | Unset
        )
        if isinstance(_cpv, Unset):
            cpv = UNSET
        else:
            cpv = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CPV.from_dict(
                _cpv
            )

        _tkm = d.pop("TKM", UNSET)
        tkm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM
            | Unset
        )
        if isinstance(_tkm, Unset):
            tkm = UNSET
        else:
            tkm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKM.from_dict(
                _tkm
            )

        _atg = d.pop("ATG", UNSET)
        atg: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG
            | Unset
        )
        if isinstance(_atg, Unset):
            atg = UNSET
        else:
            atg = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATG.from_dict(
                _atg
            )

        _tca = d.pop("TCA", UNSET)
        tca: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA
            | Unset
        )
        if isinstance(_tca, Unset):
            tca = UNSET
        else:
            tca = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TCA.from_dict(
                _tca
            )

        _kna = d.pop("KNA", UNSET)
        kna: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA
            | Unset
        )
        if isinstance(_kna, Unset):
            kna = UNSET
        else:
            kna = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KNA.from_dict(
                _kna
            )

        _grd = d.pop("GRD", UNSET)
        grd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD
            | Unset
        )
        if isinstance(_grd, Unset):
            grd = UNSET
        else:
            grd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRD.from_dict(
                _grd
            )

        _asm = d.pop("ASM", UNSET)
        asm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM
            | Unset
        )
        if isinstance(_asm, Unset):
            asm = UNSET
        else:
            asm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ASM.from_dict(
                _asm
            )

        _vut = d.pop("VUT", UNSET)
        vut: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT
            | Unset
        )
        if isinstance(_vut, Unset):
            vut = UNSET
        else:
            vut = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VUT.from_dict(
                _vut
            )

        _gnq = d.pop("GNQ", UNSET)
        gnq: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ
            | Unset
        )
        if isinstance(_gnq, Unset):
            gnq = UNSET
        else:
            gnq = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNQ.from_dict(
                _gnq
            )

        _grl = d.pop("GRL", UNSET)
        grl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL
            | Unset
        )
        if isinstance(_grl, Unset):
            grl = UNSET
        else:
            grl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GRL.from_dict(
                _grl
            )

        _sxm = d.pop("SXM", UNSET)
        sxm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM
            | Unset
        )
        if isinstance(_sxm, Unset):
            sxm = UNSET
        else:
            sxm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SXM.from_dict(
                _sxm
            )

        _mnp = d.pop("MNP", UNSET)
        mnp: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP
            | Unset
        )
        if isinstance(_mnp, Unset):
            mnp = UNSET
        else:
            mnp = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MNP.from_dict(
                _mnp
            )

        _com = d.pop("COM", UNSET)
        com: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM
            | Unset
        )
        if isinstance(_com, Unset):
            com = UNSET
        else:
            com = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COM.from_dict(
                _com
            )

        _tls = d.pop("TLS", UNSET)
        tls: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS
            | Unset
        )
        if isinstance(_tls, Unset):
            tls = UNSET
        else:
            tls = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TLS.from_dict(
                _tls
            )

        _sjm = d.pop("SJM", UNSET)
        sjm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM
            | Unset
        )
        if isinstance(_sjm, Unset):
            sjm = UNSET
        else:
            sjm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SJM.from_dict(
                _sjm
            )

        _caf = d.pop("CAF", UNSET)
        caf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF
            | Unset
        )
        if isinstance(_caf, Unset):
            caf = UNSET
        else:
            caf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CAF.from_dict(
                _caf
            )

        _dma = d.pop("DMA", UNSET)
        dma: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA
            | Unset
        )
        if isinstance(_dma, Unset):
            dma = UNSET
        else:
            dma = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0DMA.from_dict(
                _dma
            )

        _maf = d.pop("MAF", UNSET)
        maf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF
            | Unset
        )
        if isinstance(_maf, Unset):
            maf = UNSET
        else:
            maf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MAF.from_dict(
                _maf
            )

        _wsm = d.pop("WSM", UNSET)
        wsm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM
            | Unset
        )
        if isinstance(_wsm, Unset):
            wsm = UNSET
        else:
            wsm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WSM.from_dict(
                _wsm
            )

        _bes = d.pop("BES", UNSET)
        bes: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES
            | Unset
        )
        if isinstance(_bes, Unset):
            bes = UNSET
        else:
            bes = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BES.from_dict(
                _bes
            )

        _mhl = d.pop("MHL", UNSET)
        mhl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL
            | Unset
        )
        if isinstance(_mhl, Unset):
            mhl = UNSET
        else:
            mhl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MHL.from_dict(
                _mhl
            )

        _aia = d.pop("AIA", UNSET)
        aia: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA
            | Unset
        )
        if isinstance(_aia, Unset):
            aia = UNSET
        else:
            aia = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0AIA.from_dict(
                _aia
            )

        _ton = d.pop("TON", UNSET)
        ton: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON
            | Unset
        )
        if isinstance(_ton, Unset):
            ton = UNSET
        else:
            ton = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TON.from_dict(
                _ton
            )

        _cok = d.pop("COK", UNSET)
        cok: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK
            | Unset
        )
        if isinstance(_cok, Unset):
            cok = UNSET
        else:
            cok = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0COK.from_dict(
                _cok
            )

        _slb = d.pop("SLB", UNSET)
        slb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB
            | Unset
        )
        if isinstance(_slb, Unset):
            slb = UNSET
        else:
            slb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SLB.from_dict(
                _slb
            )

        _spm = d.pop("SPM", UNSET)
        spm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM
            | Unset
        )
        if isinstance(_spm, Unset):
            spm = UNSET
        else:
            spm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SPM.from_dict(
                _spm
            )

        _gnb = d.pop("GNB", UNSET)
        gnb: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB
            | Unset
        )
        if isinstance(_gnb, Unset):
            gnb = UNSET
        else:
            gnb = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0GNB.from_dict(
                _gnb
            )

        _ata = d.pop("ATA", UNSET)
        ata: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA
            | Unset
        )
        if isinstance(_ata, Unset):
            ata = UNSET
        else:
            ata = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATA.from_dict(
                _ata
            )

        _tuv = d.pop("TUV", UNSET)
        tuv: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV
            | Unset
        )
        if isinstance(_tuv, Unset):
            tuv = UNSET
        else:
            tuv = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TUV.from_dict(
                _tuv
            )

        _ala = d.pop("ALA", UNSET)
        ala: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA
            | Unset
        )
        if isinstance(_ala, Unset):
            ala = UNSET
        else:
            ala = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ALA.from_dict(
                _ala
            )

        _iot = d.pop("IOT", UNSET)
        iot: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT
            | Unset
        )
        if isinstance(_iot, Unset):
            iot = UNSET
        else:
            iot = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0IOT.from_dict(
                _iot
            )

        _eri = d.pop("ERI", UNSET)
        eri: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI
            | Unset
        )
        if isinstance(_eri, Unset):
            eri = UNSET
        else:
            eri = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ERI.from_dict(
                _eri
            )

        _plw = d.pop("PLW", UNSET)
        plw: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW
            | Unset
        )
        if isinstance(_plw, Unset):
            plw = UNSET
        else:
            plw = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PLW.from_dict(
                _plw
            )

        _fsm = d.pop("FSM", UNSET)
        fsm: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM
            | Unset
        )
        if isinstance(_fsm, Unset):
            fsm = UNSET
        else:
            fsm = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FSM.from_dict(
                _fsm
            )

        _nru = d.pop("NRU", UNSET)
        nru: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU
            | Unset
        )
        if isinstance(_nru, Unset):
            nru = UNSET
        else:
            nru = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NRU.from_dict(
                _nru
            )

        _pcn = d.pop("PCN", UNSET)
        pcn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN
            | Unset
        )
        if isinstance(_pcn, Unset):
            pcn = UNSET
        else:
            pcn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0PCN.from_dict(
                _pcn
            )

        _flk = d.pop("FLK", UNSET)
        flk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK
            | Unset
        )
        if isinstance(_flk, Unset):
            flk = UNSET
        else:
            flk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0FLK.from_dict(
                _flk
            )

        _msr = d.pop("MSR", UNSET)
        msr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR
            | Unset
        )
        if isinstance(_msr, Unset):
            msr = UNSET
        else:
            msr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0MSR.from_dict(
                _msr
            )

        _vat = d.pop("VAT", UNSET)
        vat: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT
            | Unset
        )
        if isinstance(_vat, Unset):
            vat = UNSET
        else:
            vat = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0VAT.from_dict(
                _vat
            )

        _kir = d.pop("KIR", UNSET)
        kir: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR
            | Unset
        )
        if isinstance(_kir, Unset):
            kir = UNSET
        else:
            kir = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0KIR.from_dict(
                _kir
            )

        _shn = d.pop("SHN", UNSET)
        shn: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN
            | Unset
        )
        if isinstance(_shn, Unset):
            shn = UNSET
        else:
            shn = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SHN.from_dict(
                _shn
            )

        _niu = d.pop("NIU", UNSET)
        niu: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU
            | Unset
        )
        if isinstance(_niu, Unset):
            niu = UNSET
        else:
            niu = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NIU.from_dict(
                _niu
            )

        _wlf = d.pop("WLF", UNSET)
        wlf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF
            | Unset
        )
        if isinstance(_wlf, Unset):
            wlf = UNSET
        else:
            wlf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0WLF.from_dict(
                _wlf
            )

        _hmd = d.pop("HMD", UNSET)
        hmd: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD
            | Unset
        )
        if isinstance(_hmd, Unset):
            hmd = UNSET
        else:
            hmd = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0HMD.from_dict(
                _hmd
            )

        _cxr = d.pop("CXR", UNSET)
        cxr: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR
            | Unset
        )
        if isinstance(_cxr, Unset):
            cxr = UNSET
        else:
            cxr = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CXR.from_dict(
                _cxr
            )

        _nfk = d.pop("NFK", UNSET)
        nfk: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK
            | Unset
        )
        if isinstance(_nfk, Unset):
            nfk = UNSET
        else:
            nfk = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0NFK.from_dict(
                _nfk
            )

        _atf = d.pop("ATF", UNSET)
        atf: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF
            | Unset
        )
        if isinstance(_atf, Unset):
            atf = UNSET
        else:
            atf = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ATF.from_dict(
                _atf
            )

        _cck = d.pop("CCK", UNSET)
        cck: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK
            | Unset
        )
        if isinstance(_cck, Unset):
            cck = UNSET
        else:
            cck = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0CCK.from_dict(
                _cck
            )

        _sgs = d.pop("SGS", UNSET)
        sgs: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS
            | Unset
        )
        if isinstance(_sgs, Unset):
            sgs = UNSET
        else:
            sgs = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0SGS.from_dict(
                _sgs
            )

        _bvt = d.pop("BVT", UNSET)
        bvt: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT
            | Unset
        )
        if isinstance(_bvt, Unset):
            bvt = UNSET
        else:
            bvt = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0BVT.from_dict(
                _bvt
            )

        _umi = d.pop("UMI", UNSET)
        umi: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI
            | Unset
        )
        if isinstance(_umi, Unset):
            umi = UNSET
        else:
            umi = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0UMI.from_dict(
                _umi
            )

        _esh = d.pop("ESH", UNSET)
        esh: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH
            | Unset
        )
        if isinstance(_esh, Unset):
            esh = UNSET
        else:
            esh = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0ESH.from_dict(
                _esh
            )

        _tkl = d.pop("TKL", UNSET)
        tkl: (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL
            | Unset
        )
        if isinstance(_tkl, Unset):
            tkl = UNSET
        else:
            tkl = QuickCompanyResolveResponse200OutputDataItemCompanyType0LiJobPostsStatsType0CountryLocationStatsType0TKL.from_dict(
                _tkl
            )

        quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0 = cls(
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

        return quick_company_resolve_response_200_output_data_item_company_type_0_li_job_posts_stats_type_0_country_location_stats_type_0
