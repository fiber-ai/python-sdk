from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_company_search_params_response_200_output_search_params_accelerators_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_employee_count_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_1 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_country_code_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_state_name_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_industries_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_investors_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_job_postings_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_keywords_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_1 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_last_funding_usd_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_naics_codes_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_name_like_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_revenue_usd_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_stage_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsStageType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_tags_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_technologies_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_total_funding_usd_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0,
    )


T = TypeVar("T", bound="TextToCompanySearchParamsResponse200OutputSearchParams")


@_attrs_define
class TextToCompanySearchParamsResponse200OutputSearchParams:
    """
    Attributes:
        headquarters_country_code (None |
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0 | Unset):
        headquarters_state_name (None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0
            | Unset):
        employee_count_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0 | Unset):
        keywords (None | TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0 | Unset):
        industries_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0 | Unset):
        stage (None | TextToCompanySearchParamsResponse200OutputSearchParamsStageType0 | Unset):
        total_funding_usd (None | TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0 | Unset):
        last_funding_usd (None | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0 | Unset):
        last_funded_on (None | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0 |
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1 | Unset):
        founded_on (None | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0 |
            TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1 | Unset):
        investors (None | TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0 | Unset):
        name_like (None | TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0 | Unset):
        accelerators_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0 | Unset):
        headquarters_location (None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0 |
            Unset):
        job_postings_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0 | Unset):
        tags (None | TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0 | Unset):
        revenue_usd (None | TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0 | Unset):
        office_locations_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0 |
            Unset):
        naics_codes (None | TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0 | Unset):
        technologies (None | TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0 | Unset):
        exact_company_v2 (None | TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0 | Unset):
    """

    headquarters_country_code: (
        None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0 | Unset
    ) = UNSET
    headquarters_state_name: (
        None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0 | Unset
    ) = UNSET
    employee_count_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0 | Unset = UNSET
    keywords: None | TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0 | Unset = UNSET
    industries_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0 | Unset = UNSET
    stage: None | TextToCompanySearchParamsResponse200OutputSearchParamsStageType0 | Unset = UNSET
    total_funding_usd: None | TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0 | Unset = UNSET
    last_funding_usd: None | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0 | Unset = UNSET
    last_funded_on: (
        None
        | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0
        | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1
        | Unset
    ) = UNSET
    founded_on: (
        None
        | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0
        | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1
        | Unset
    ) = UNSET
    investors: None | TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0 | Unset = UNSET
    name_like: None | TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0 | Unset = UNSET
    accelerators_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0 | Unset = UNSET
    headquarters_location: (
        None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0 | Unset
    ) = UNSET
    job_postings_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0 | Unset = UNSET
    tags: None | TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0 | Unset = UNSET
    revenue_usd: None | TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0 | Unset = UNSET
    office_locations_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0 | Unset = (
        UNSET
    )
    naics_codes: None | TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0 | Unset = UNSET
    technologies: None | TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0 | Unset = UNSET
    exact_company_v2: None | TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_params_response_200_output_search_params_accelerators_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_employee_count_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_1 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_country_code_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_state_name_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_industries_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_investors_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_job_postings_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_keywords_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_1 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funding_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_naics_codes_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_name_like_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_revenue_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_stage_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsStageType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_tags_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_technologies_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_total_funding_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0,
        )

        headquarters_country_code: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_country_code, Unset):
            headquarters_country_code = UNSET
        elif isinstance(
            self.headquarters_country_code,
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0,
        ):
            headquarters_country_code = self.headquarters_country_code.to_dict()
        else:
            headquarters_country_code = self.headquarters_country_code

        headquarters_state_name: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_state_name, Unset):
            headquarters_state_name = UNSET
        elif isinstance(
            self.headquarters_state_name,
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0,
        ):
            headquarters_state_name = self.headquarters_state_name.to_dict()
        else:
            headquarters_state_name = self.headquarters_state_name

        employee_count_v2: dict[str, Any] | None | Unset
        if isinstance(self.employee_count_v2, Unset):
            employee_count_v2 = UNSET
        elif isinstance(
            self.employee_count_v2, TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0
        ):
            employee_count_v2 = self.employee_count_v2.to_dict()
        else:
            employee_count_v2 = self.employee_count_v2

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        industries_v2: dict[str, Any] | None | Unset
        if isinstance(self.industries_v2, Unset):
            industries_v2 = UNSET
        elif isinstance(self.industries_v2, TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0):
            industries_v2 = self.industries_v2.to_dict()
        else:
            industries_v2 = self.industries_v2

        stage: dict[str, Any] | None | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, TextToCompanySearchParamsResponse200OutputSearchParamsStageType0):
            stage = self.stage.to_dict()
        else:
            stage = self.stage

        total_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        elif isinstance(
            self.total_funding_usd, TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0
        ):
            total_funding_usd = self.total_funding_usd.to_dict()
        else:
            total_funding_usd = self.total_funding_usd

        last_funding_usd: dict[str, Any] | None | Unset
        if isinstance(self.last_funding_usd, Unset):
            last_funding_usd = UNSET
        elif isinstance(
            self.last_funding_usd, TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0
        ):
            last_funding_usd = self.last_funding_usd.to_dict()
        else:
            last_funding_usd = self.last_funding_usd

        last_funded_on: dict[str, Any] | None | Unset
        if isinstance(self.last_funded_on, Unset):
            last_funded_on = UNSET
        elif isinstance(self.last_funded_on, TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0):
            last_funded_on = self.last_funded_on.to_dict()
        elif isinstance(self.last_funded_on, TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1):
            last_funded_on = self.last_funded_on.to_dict()
        else:
            last_funded_on = self.last_funded_on

        founded_on: dict[str, Any] | None | Unset
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        investors: dict[str, Any] | None | Unset
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0):
            investors = self.investors.to_dict()
        else:
            investors = self.investors

        name_like: dict[str, Any] | None | Unset
        if isinstance(self.name_like, Unset):
            name_like = UNSET
        elif isinstance(self.name_like, TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0):
            name_like = self.name_like.to_dict()
        else:
            name_like = self.name_like

        accelerators_v2: dict[str, Any] | None | Unset
        if isinstance(self.accelerators_v2, Unset):
            accelerators_v2 = UNSET
        elif isinstance(
            self.accelerators_v2, TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0
        ):
            accelerators_v2 = self.accelerators_v2.to_dict()
        else:
            accelerators_v2 = self.accelerators_v2

        headquarters_location: dict[str, Any] | None | Unset
        if isinstance(self.headquarters_location, Unset):
            headquarters_location = UNSET
        elif isinstance(
            self.headquarters_location, TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0
        ):
            headquarters_location = self.headquarters_location.to_dict()
        else:
            headquarters_location = self.headquarters_location

        job_postings_v2: dict[str, Any] | None | Unset
        if isinstance(self.job_postings_v2, Unset):
            job_postings_v2 = UNSET
        elif isinstance(self.job_postings_v2, TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0):
            job_postings_v2 = self.job_postings_v2.to_dict()
        else:
            job_postings_v2 = self.job_postings_v2

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        revenue_usd: dict[str, Any] | None | Unset
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        elif isinstance(self.revenue_usd, TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0):
            revenue_usd = self.revenue_usd.to_dict()
        else:
            revenue_usd = self.revenue_usd

        office_locations_v2: dict[str, Any] | None | Unset
        if isinstance(self.office_locations_v2, Unset):
            office_locations_v2 = UNSET
        elif isinstance(
            self.office_locations_v2, TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0
        ):
            office_locations_v2 = self.office_locations_v2.to_dict()
        else:
            office_locations_v2 = self.office_locations_v2

        naics_codes: dict[str, Any] | None | Unset
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0):
            naics_codes = self.naics_codes.to_dict()
        else:
            naics_codes = self.naics_codes

        technologies: dict[str, Any] | None | Unset
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0):
            technologies = self.technologies.to_dict()
        else:
            technologies = self.technologies

        exact_company_v2: dict[str, Any] | None | Unset
        if isinstance(self.exact_company_v2, Unset):
            exact_company_v2 = UNSET
        elif isinstance(
            self.exact_company_v2, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0
        ):
            exact_company_v2 = self.exact_company_v2.to_dict()
        else:
            exact_company_v2 = self.exact_company_v2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if investors is not UNSET:
            field_dict["investors"] = investors
        if name_like is not UNSET:
            field_dict["nameLike"] = name_like
        if accelerators_v2 is not UNSET:
            field_dict["acceleratorsV2"] = accelerators_v2
        if headquarters_location is not UNSET:
            field_dict["headquartersLocation"] = headquarters_location
        if job_postings_v2 is not UNSET:
            field_dict["jobPostingsV2"] = job_postings_v2
        if tags is not UNSET:
            field_dict["tags"] = tags
        if revenue_usd is not UNSET:
            field_dict["revenueUSD"] = revenue_usd
        if office_locations_v2 is not UNSET:
            field_dict["officeLocationsV2"] = office_locations_v2
        if naics_codes is not UNSET:
            field_dict["naicsCodes"] = naics_codes
        if technologies is not UNSET:
            field_dict["technologies"] = technologies
        if exact_company_v2 is not UNSET:
            field_dict["exactCompanyV2"] = exact_company_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_params_response_200_output_search_params_accelerators_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_employee_count_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_founded_on_type_1 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_country_code_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_state_name_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_industries_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_investors_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_job_postings_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_keywords_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funded_on_type_1 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_last_funding_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_naics_codes_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_name_like_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_revenue_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_stage_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsStageType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_tags_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_technologies_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_total_funding_usd_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0,
        )

        d = dict(src_dict)

        def _parse_headquarters_country_code(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_country_code_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0.from_dict(data)
                )

                return headquarters_country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersCountryCodeType0 | Unset, data
            )

        headquarters_country_code = _parse_headquarters_country_code(d.pop("headquartersCountryCode", UNSET))

        def _parse_headquarters_state_name(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_state_name_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0.from_dict(data)
                )

                return headquarters_state_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersStateNameType0 | Unset, data
            )

        headquarters_state_name = _parse_headquarters_state_name(d.pop("headquartersStateName", UNSET))

        def _parse_employee_count_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0.from_dict(data)
                )

                return employee_count_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsEmployeeCountV2Type0 | Unset, data)

        employee_count_v2 = _parse_employee_count_v2(d.pop("employeeCountV2", UNSET))

        def _parse_keywords(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0.from_dict(data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsKeywordsType0 | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_industries_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industries_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0.from_dict(data)
                )

                return industries_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsIndustriesV2Type0 | Unset, data)

        industries_v2 = _parse_industries_v2(d.pop("industriesV2", UNSET))

        def _parse_stage(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsStageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stage_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsStageType0.from_dict(data)

                return stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsStageType0 | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_total_funding_usd(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_funding_usd_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0.from_dict(data)
                )

                return total_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsTotalFundingUSDType0 | Unset, data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUSD", UNSET))

        def _parse_last_funding_usd(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funding_usd_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0.from_dict(data)
                )

                return last_funding_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundingUSDType0 | Unset, data)

        last_funding_usd = _parse_last_funding_usd(d.pop("lastFundingUSD", UNSET))

        def _parse_last_funded_on(
            data: object,
        ) -> (
            None
            | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0
            | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1
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
                    TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0.from_dict(data)
                )

                return last_funded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_1 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1.from_dict(data)
                )

                return last_funded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType0
                | TextToCompanySearchParamsResponse200OutputSearchParamsLastFundedOnType1
                | Unset,
                data,
            )

        last_funded_on = _parse_last_funded_on(d.pop("lastFundedOn", UNSET))

        def _parse_founded_on(
            data: object,
        ) -> (
            None
            | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0
            | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0.from_dict(data)

                return founded_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_1 = TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1.from_dict(data)

                return founded_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType0
                | TextToCompanySearchParamsResponse200OutputSearchParamsFoundedOnType1
                | Unset,
                data,
            )

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))

        def _parse_investors(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0.from_dict(data)

                return investors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsInvestorsType0 | Unset, data)

        investors = _parse_investors(d.pop("investors", UNSET))

        def _parse_name_like(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_like_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0.from_dict(data)

                return name_like_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsNameLikeType0 | Unset, data)

        name_like = _parse_name_like(d.pop("nameLike", UNSET))

        def _parse_accelerators_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accelerators_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0.from_dict(data)
                )

                return accelerators_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsAcceleratorsV2Type0 | Unset, data)

        accelerators_v2 = _parse_accelerators_v2(d.pop("acceleratorsV2", UNSET))

        def _parse_headquarters_location(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_location_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0.from_dict(data)
                )

                return headquarters_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0 | Unset, data
            )

        headquarters_location = _parse_headquarters_location(d.pop("headquartersLocation", UNSET))

        def _parse_job_postings_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0.from_dict(data)
                )

                return job_postings_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0 | Unset, data)

        job_postings_v2 = _parse_job_postings_v2(d.pop("jobPostingsV2", UNSET))

        def _parse_tags(data: object) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0.from_dict(data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0 | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_revenue_usd(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_usd_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0.from_dict(
                    data
                )

                return revenue_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsRevenueUSDType0 | Unset, data)

        revenue_usd = _parse_revenue_usd(d.pop("revenueUSD", UNSET))

        def _parse_office_locations_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                office_locations_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0.from_dict(data)
                )

                return office_locations_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0 | Unset, data
            )

        office_locations_v2 = _parse_office_locations_v2(d.pop("officeLocationsV2", UNSET))

        def _parse_naics_codes(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                naics_codes_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0.from_dict(
                    data
                )

                return naics_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsNaicsCodesType0 | Unset, data)

        naics_codes = _parse_naics_codes(d.pop("naicsCodes", UNSET))

        def _parse_technologies(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0.from_dict(
                    data
                )

                return technologies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsTechnologiesType0 | Unset, data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))

        def _parse_exact_company_v2(
            data: object,
        ) -> None | TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_v2_type_0 = (
                    TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0.from_dict(data)
                )

                return exact_company_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0 | Unset, data)

        exact_company_v2 = _parse_exact_company_v2(d.pop("exactCompanyV2", UNSET))

        text_to_company_search_params_response_200_output_search_params = cls(
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
            investors=investors,
            name_like=name_like,
            accelerators_v2=accelerators_v2,
            headquarters_location=headquarters_location,
            job_postings_v2=job_postings_v2,
            tags=tags,
            revenue_usd=revenue_usd,
            office_locations_v2=office_locations_v2,
            naics_codes=naics_codes,
            technologies=technologies,
            exact_company_v2=exact_company_v2,
        )

        text_to_company_search_params_response_200_output_search_params.additional_properties = d
        return text_to_company_search_params_response_200_output_search_params

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
