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
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_country_code_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_state_name_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_location_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_naics_codes_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_industries_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_stage_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_investors_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_technologies_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_employee_count_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_accelerators_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_exact_company_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_name_like_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_total_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_revenue_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_job_postings_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputCompanySearchParamsType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputCompanySearchParamsType0:
    """ 
        Attributes:
            headquarters_country_code
                (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0', None,
                Unset]):
            headquarters_state_name
                (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0', None, Unset]):
            employee_count_v2 (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0',
                None, Unset]):
            keywords (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0', None, Unset]):
            industries_v2 (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0', None,
                Unset]):
            stage (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0', None, Unset]):
            total_funding_usd (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0',
                None, Unset]):
            last_funding_usd (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0',
                None, Unset]):
            last_funded_on (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0',
                'TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1', None, Unset]):
            founded_on (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0',
                'TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1', None, Unset]):
            investors (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0', None, Unset]):
            name_like (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0', None, Unset]):
            accelerators_v2 (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0', None,
                Unset]):
            headquarters_location
                (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0', None, Unset]):
            job_postings_v2 (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0', None,
                Unset]):
            tags (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0', None, Unset]):
            revenue_usd (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0', None,
                Unset]):
            office_locations_v2
                (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0', None, Unset]):
            naics_codes (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0', None,
                Unset]):
            technologies (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0', None,
                Unset]):
            exact_company_v2 (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0',
                None, Unset]):
     """

    headquarters_country_code: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0', None, Unset] = UNSET
    headquarters_state_name: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0', None, Unset] = UNSET
    employee_count_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0', None, Unset] = UNSET
    keywords: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0', None, Unset] = UNSET
    industries_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0', None, Unset] = UNSET
    stage: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0', None, Unset] = UNSET
    total_funding_usd: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0', None, Unset] = UNSET
    last_funding_usd: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0', None, Unset] = UNSET
    last_funded_on: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1', None, Unset] = UNSET
    founded_on: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1', None, Unset] = UNSET
    investors: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0', None, Unset] = UNSET
    name_like: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0', None, Unset] = UNSET
    accelerators_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0', None, Unset] = UNSET
    headquarters_location: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0', None, Unset] = UNSET
    job_postings_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0', None, Unset] = UNSET
    tags: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0', None, Unset] = UNSET
    revenue_usd: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0', None, Unset] = UNSET
    office_locations_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0', None, Unset] = UNSET
    naics_codes: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0', None, Unset] = UNSET
    technologies: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0', None, Unset] = UNSET
    exact_company_v2: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_country_code_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_state_name_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_location_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_naics_codes_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_industries_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_stage_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_investors_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_technologies_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_employee_count_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_accelerators_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_exact_company_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_name_like_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_total_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_revenue_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_job_postings_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0
        headquarters_country_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_country_code, Unset):
            headquarters_country_code = UNSET
        elif isinstance(self.headquarters_country_code, TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0):
            headquarters_country_code = self.headquarters_country_code.to_dict()
        else:
            headquarters_country_code = self.headquarters_country_code

        headquarters_state_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_state_name, Unset):
            headquarters_state_name = UNSET
        elif isinstance(self.headquarters_state_name, TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0):
            headquarters_state_name = self.headquarters_state_name.to_dict()
        else:
            headquarters_state_name = self.headquarters_state_name

        employee_count_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employee_count_v2, Unset):
            employee_count_v2 = UNSET
        elif isinstance(self.employee_count_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0):
            employee_count_v2 = self.employee_count_v2.to_dict()
        else:
            employee_count_v2 = self.employee_count_v2

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        industries_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.industries_v2, Unset):
            industries_v2 = UNSET
        elif isinstance(self.industries_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0):
            industries_v2 = self.industries_v2.to_dict()
        else:
            industries_v2 = self.industries_v2

        stage: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0):
            stage = self.stage.to_dict()
        else:
            stage = self.stage

        total_funding_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        elif isinstance(self.total_funding_usd, TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0):
            total_funding_usd = self.total_funding_usd.to_dict()
        else:
            total_funding_usd = self.total_funding_usd

        last_funding_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_funding_usd, Unset):
            last_funding_usd = UNSET
        elif isinstance(self.last_funding_usd, TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0):
            last_funding_usd = self.last_funding_usd.to_dict()
        else:
            last_funding_usd = self.last_funding_usd

        last_funded_on: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_funded_on, Unset):
            last_funded_on = UNSET
        elif isinstance(self.last_funded_on, TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0):
            last_funded_on = self.last_funded_on.to_dict()
        elif isinstance(self.last_funded_on, TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1):
            last_funded_on = self.last_funded_on.to_dict()
        else:
            last_funded_on = self.last_funded_on

        founded_on: Union[None, Unset, dict[str, Any]]
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        investors: Union[None, Unset, dict[str, Any]]
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0):
            investors = self.investors.to_dict()
        else:
            investors = self.investors

        name_like: Union[None, Unset, dict[str, Any]]
        if isinstance(self.name_like, Unset):
            name_like = UNSET
        elif isinstance(self.name_like, TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0):
            name_like = self.name_like.to_dict()
        else:
            name_like = self.name_like

        accelerators_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.accelerators_v2, Unset):
            accelerators_v2 = UNSET
        elif isinstance(self.accelerators_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0):
            accelerators_v2 = self.accelerators_v2.to_dict()
        else:
            accelerators_v2 = self.accelerators_v2

        headquarters_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.headquarters_location, Unset):
            headquarters_location = UNSET
        elif isinstance(self.headquarters_location, TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0):
            headquarters_location = self.headquarters_location.to_dict()
        else:
            headquarters_location = self.headquarters_location

        job_postings_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_postings_v2, Unset):
            job_postings_v2 = UNSET
        elif isinstance(self.job_postings_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0):
            job_postings_v2 = self.job_postings_v2.to_dict()
        else:
            job_postings_v2 = self.job_postings_v2

        tags: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        revenue_usd: Union[None, Unset, dict[str, Any]]
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        elif isinstance(self.revenue_usd, TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0):
            revenue_usd = self.revenue_usd.to_dict()
        else:
            revenue_usd = self.revenue_usd

        office_locations_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.office_locations_v2, Unset):
            office_locations_v2 = UNSET
        elif isinstance(self.office_locations_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0):
            office_locations_v2 = self.office_locations_v2.to_dict()
        else:
            office_locations_v2 = self.office_locations_v2

        naics_codes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0):
            naics_codes = self.naics_codes.to_dict()
        else:
            naics_codes = self.naics_codes

        technologies: Union[None, Unset, dict[str, Any]]
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0):
            technologies = self.technologies.to_dict()
        else:
            technologies = self.technologies

        exact_company_v2: Union[None, Unset, dict[str, Any]]
        if isinstance(self.exact_company_v2, Unset):
            exact_company_v2 = UNSET
        elif isinstance(self.exact_company_v2, TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0):
            exact_company_v2 = self.exact_company_v2.to_dict()
        else:
            exact_company_v2 = self.exact_company_v2


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_country_code_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_state_name_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_headquarters_location_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_naics_codes_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_tags_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_industries_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_stage_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_investors_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_last_funded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_technologies_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_keywords_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_founded_on_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_employee_count_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_accelerators_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_exact_company_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_name_like_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_total_funding_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_revenue_usd_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_job_postings_v2_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0
        d = dict(src_dict)
        def _parse_headquarters_country_code(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_country_code_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0.from_dict(data)



                return headquarters_country_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersCountryCodeType0', None, Unset], data)

        headquarters_country_code = _parse_headquarters_country_code(d.pop("headquartersCountryCode", UNSET))


        def _parse_headquarters_state_name(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_state_name_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0.from_dict(data)



                return headquarters_state_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersStateNameType0', None, Unset], data)

        headquarters_state_name = _parse_headquarters_state_name(d.pop("headquartersStateName", UNSET))


        def _parse_employee_count_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0.from_dict(data)



                return employee_count_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0EmployeeCountV2Type0', None, Unset], data)

        employee_count_v2 = _parse_employee_count_v2(d.pop("employeeCountV2", UNSET))


        def _parse_keywords(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0KeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_industries_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industries_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0.from_dict(data)



                return industries_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0IndustriesV2Type0', None, Unset], data)

        industries_v2 = _parse_industries_v2(d.pop("industriesV2", UNSET))


        def _parse_stage(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stage_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0.from_dict(data)



                return stage_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0StageType0', None, Unset], data)

        stage = _parse_stage(d.pop("stage", UNSET))


        def _parse_total_funding_usd(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_funding_usd_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0.from_dict(data)



                return total_funding_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TotalFundingUSDType0', None, Unset], data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUSD", UNSET))


        def _parse_last_funding_usd(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funding_usd_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0.from_dict(data)



                return last_funding_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundingUSDType0', None, Unset], data)

        last_funding_usd = _parse_last_funding_usd(d.pop("lastFundingUSD", UNSET))


        def _parse_last_funded_on(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0.from_dict(data)



                return last_funded_on_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_funded_on_type_1 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1.from_dict(data)



                return last_funded_on_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0LastFundedOnType1', None, Unset], data)

        last_funded_on = _parse_last_funded_on(d.pop("lastFundedOn", UNSET))


        def _parse_founded_on(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0.from_dict(data)



                return founded_on_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_1 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1.from_dict(data)



                return founded_on_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0FoundedOnType1', None, Unset], data)

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))


        def _parse_investors(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0.from_dict(data)



                return investors_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsType0', None, Unset], data)

        investors = _parse_investors(d.pop("investors", UNSET))


        def _parse_name_like(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_like_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0.from_dict(data)



                return name_like_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NameLikeType0', None, Unset], data)

        name_like = _parse_name_like(d.pop("nameLike", UNSET))


        def _parse_accelerators_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accelerators_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0.from_dict(data)



                return accelerators_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0AcceleratorsV2Type0', None, Unset], data)

        accelerators_v2 = _parse_accelerators_v2(d.pop("acceleratorsV2", UNSET))


        def _parse_headquarters_location(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_location_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0.from_dict(data)



                return headquarters_location_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0HeadquartersLocationType0', None, Unset], data)

        headquarters_location = _parse_headquarters_location(d.pop("headquartersLocation", UNSET))


        def _parse_job_postings_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_postings_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0.from_dict(data)



                return job_postings_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0JobPostingsV2Type0', None, Unset], data)

        job_postings_v2 = _parse_job_postings_v2(d.pop("jobPostingsV2", UNSET))


        def _parse_tags(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tags_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0.from_dict(data)



                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TagsType0', None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_revenue_usd(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_usd_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0.from_dict(data)



                return revenue_usd_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0RevenueUSDType0', None, Unset], data)

        revenue_usd = _parse_revenue_usd(d.pop("revenueUSD", UNSET))


        def _parse_office_locations_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                office_locations_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0.from_dict(data)



                return office_locations_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0', None, Unset], data)

        office_locations_v2 = _parse_office_locations_v2(d.pop("officeLocationsV2", UNSET))


        def _parse_naics_codes(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                naics_codes_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0.from_dict(data)



                return naics_codes_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0NaicsCodesType0', None, Unset], data)

        naics_codes = _parse_naics_codes(d.pop("naicsCodes", UNSET))


        def _parse_technologies(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technologies_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0.from_dict(data)



                return technologies_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0TechnologiesType0', None, Unset], data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))


        def _parse_exact_company_v2(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_company_v2_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0.from_dict(data)



                return exact_company_v2_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0ExactCompanyV2Type0', None, Unset], data)

        exact_company_v2 = _parse_exact_company_v2(d.pop("exactCompanyV2", UNSET))


        text_to_combined_search_response_200_output_company_search_params_type_0 = cls(
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


        text_to_combined_search_response_200_output_company_search_params_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_company_search_params_type_0

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
