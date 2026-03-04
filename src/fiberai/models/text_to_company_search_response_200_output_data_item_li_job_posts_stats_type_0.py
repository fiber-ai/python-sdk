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
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_seniority_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_standard_industries_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0
  from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_employment_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0





T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0")



@_attrs_define
class TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0:
    """ 
        Attributes:
            total_count (float):
            seniority_stats (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0',
                None, Unset]):
            employment_type_stats
                (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0', None,
                Unset]):
            country_location_stats
                (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0', None,
                Unset]):
            puree_job_functions_stats
                (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0', None,
                Unset]):
            standard_industries_stats
                (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0', None,
                Unset]):
            job_location_type_stats
                (Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0', None,
                Unset]):
     """

    total_count: float
    seniority_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0', None, Unset] = UNSET
    employment_type_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0', None, Unset] = UNSET
    country_location_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0', None, Unset] = UNSET
    puree_job_functions_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0', None, Unset] = UNSET
    standard_industries_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0', None, Unset] = UNSET
    job_location_type_stats: Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_seniority_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_standard_industries_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_employment_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0
        total_count = self.total_count

        seniority_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.seniority_stats, Unset):
            seniority_stats = UNSET
        elif isinstance(self.seniority_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0):
            seniority_stats = self.seniority_stats.to_dict()
        else:
            seniority_stats = self.seniority_stats

        employment_type_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.employment_type_stats, Unset):
            employment_type_stats = UNSET
        elif isinstance(self.employment_type_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0):
            employment_type_stats = self.employment_type_stats.to_dict()
        else:
            employment_type_stats = self.employment_type_stats

        country_location_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.country_location_stats, Unset):
            country_location_stats = UNSET
        elif isinstance(self.country_location_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0):
            country_location_stats = self.country_location_stats.to_dict()
        else:
            country_location_stats = self.country_location_stats

        puree_job_functions_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.puree_job_functions_stats, Unset):
            puree_job_functions_stats = UNSET
        elif isinstance(self.puree_job_functions_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0):
            puree_job_functions_stats = self.puree_job_functions_stats.to_dict()
        else:
            puree_job_functions_stats = self.puree_job_functions_stats

        standard_industries_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.standard_industries_stats, Unset):
            standard_industries_stats = UNSET
        elif isinstance(self.standard_industries_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0):
            standard_industries_stats = self.standard_industries_stats.to_dict()
        else:
            standard_industries_stats = self.standard_industries_stats

        job_location_type_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_location_type_stats, Unset):
            job_location_type_stats = UNSET
        elif isinstance(self.job_location_type_stats, TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0):
            job_location_type_stats = self.job_location_type_stats.to_dict()
        else:
            job_location_type_stats = self.job_location_type_stats


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_count": total_count,
        })
        if seniority_stats is not UNSET:
            field_dict["seniority_stats"] = seniority_stats
        if employment_type_stats is not UNSET:
            field_dict["employment_type_stats"] = employment_type_stats
        if country_location_stats is not UNSET:
            field_dict["country_location_stats"] = country_location_stats
        if puree_job_functions_stats is not UNSET:
            field_dict["puree_job_functions_stats"] = puree_job_functions_stats
        if standard_industries_stats is not UNSET:
            field_dict["standard_industries_stats"] = standard_industries_stats
        if job_location_type_stats is not UNSET:
            field_dict["job_location_type_stats"] = job_location_type_stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_puree_job_functions_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_seniority_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_standard_industries_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_country_location_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_employment_type_stats_type_0 import TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0
        d = dict(src_dict)
        total_count = d.pop("total_count")

        def _parse_seniority_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                seniority_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0.from_dict(data)



                return seniority_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0SeniorityStatsType0', None, Unset], data)

        seniority_stats = _parse_seniority_stats(d.pop("seniority_stats", UNSET))


        def _parse_employment_type_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employment_type_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0.from_dict(data)



                return employment_type_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0EmploymentTypeStatsType0', None, Unset], data)

        employment_type_stats = _parse_employment_type_stats(d.pop("employment_type_stats", UNSET))


        def _parse_country_location_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_location_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0.from_dict(data)



                return country_location_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0CountryLocationStatsType0', None, Unset], data)

        country_location_stats = _parse_country_location_stats(d.pop("country_location_stats", UNSET))


        def _parse_puree_job_functions_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                puree_job_functions_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0.from_dict(data)



                return puree_job_functions_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0PureeJobFunctionsStatsType0', None, Unset], data)

        puree_job_functions_stats = _parse_puree_job_functions_stats(d.pop("puree_job_functions_stats", UNSET))


        def _parse_standard_industries_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                standard_industries_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0.from_dict(data)



                return standard_industries_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0StandardIndustriesStatsType0', None, Unset], data)

        standard_industries_stats = _parse_standard_industries_stats(d.pop("standard_industries_stats", UNSET))


        def _parse_job_location_type_stats(data: object) -> Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_location_type_stats_type_0 = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0.from_dict(data)



                return job_location_type_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0', None, Unset], data)

        job_location_type_stats = _parse_job_location_type_stats(d.pop("job_location_type_stats", UNSET))


        text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0 = cls(
            total_count=total_count,
            seniority_stats=seniority_stats,
            employment_type_stats=employment_type_stats,
            country_location_stats=country_location_stats,
            puree_job_functions_stats=puree_job_functions_stats,
            standard_industries_stats=standard_industries_stats,
            job_location_type_stats=job_location_type_stats,
        )


        text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0.additional_properties = d
        return text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0

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
