from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_mid_senior_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_director import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_executive import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_not_applicable import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_associate import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_entry_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel
  from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_internship import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0:
    """ 
        Attributes:
            entry_level (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel]):
            director (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director]):
            associate (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate]):
            mid_senior_level (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel]):
            internship (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship]):
            executive (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive]):
            not_applicable (Union[Unset,
                TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable]):
     """

    entry_level: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel'] = UNSET
    director: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director'] = UNSET
    associate: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate'] = UNSET
    mid_senior_level: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel'] = UNSET
    internship: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship'] = UNSET
    executive: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive'] = UNSET
    not_applicable: Union[Unset, 'TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable'] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_mid_senior_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_director import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_executive import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_not_applicable import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_associate import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_entry_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_internship import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship
        entry_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry_level, Unset):
            entry_level = self.entry_level.to_dict()

        director: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.director, Unset):
            director = self.director.to_dict()

        associate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.associate, Unset):
            associate = self.associate.to_dict()

        mid_senior_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mid_senior_level, Unset):
            mid_senior_level = self.mid_senior_level.to_dict()

        internship: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.internship, Unset):
            internship = self.internship.to_dict()

        executive: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.executive, Unset):
            executive = self.executive.to_dict()

        not_applicable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.not_applicable, Unset):
            not_applicable = self.not_applicable.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entry_level is not UNSET:
            field_dict["Entry level"] = entry_level
        if director is not UNSET:
            field_dict["Director"] = director
        if associate is not UNSET:
            field_dict["Associate"] = associate
        if mid_senior_level is not UNSET:
            field_dict["Mid-Senior level"] = mid_senior_level
        if internship is not UNSET:
            field_dict["Internship"] = internship
        if executive is not UNSET:
            field_dict["Executive"] = executive
        if not_applicable is not UNSET:
            field_dict["Not Applicable"] = not_applicable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_mid_senior_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_director import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_executive import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_not_applicable import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_associate import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_entry_level import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel
        from ..models.text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0_internship import TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship
        d = dict(src_dict)
        _entry_level = d.pop("Entry level", UNSET)
        entry_level: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel]
        if isinstance(_entry_level,  Unset):
            entry_level = UNSET
        else:
            entry_level = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0EntryLevel.from_dict(_entry_level)




        _director = d.pop("Director", UNSET)
        director: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director]
        if isinstance(_director,  Unset):
            director = UNSET
        else:
            director = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Director.from_dict(_director)




        _associate = d.pop("Associate", UNSET)
        associate: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate]
        if isinstance(_associate,  Unset):
            associate = UNSET
        else:
            associate = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Associate.from_dict(_associate)




        _mid_senior_level = d.pop("Mid-Senior level", UNSET)
        mid_senior_level: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel]
        if isinstance(_mid_senior_level,  Unset):
            mid_senior_level = UNSET
        else:
            mid_senior_level = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel.from_dict(_mid_senior_level)




        _internship = d.pop("Internship", UNSET)
        internship: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship]
        if isinstance(_internship,  Unset):
            internship = UNSET
        else:
            internship = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Internship.from_dict(_internship)




        _executive = d.pop("Executive", UNSET)
        executive: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive]
        if isinstance(_executive,  Unset):
            executive = UNSET
        else:
            executive = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0Executive.from_dict(_executive)




        _not_applicable = d.pop("Not Applicable", UNSET)
        not_applicable: Union[Unset, TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable]
        if isinstance(_not_applicable,  Unset):
            not_applicable = UNSET
        else:
            not_applicable = TextToCombinedSearchResponse200OutputDataCompaniesItemLiJobPostsStatsType0SeniorityStatsType0NotApplicable.from_dict(_not_applicable)




        text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0 = cls(
            entry_level=entry_level,
            director=director,
            associate=associate,
            mid_senior_level=mid_senior_level,
            internship=internship,
            executive=executive,
            not_applicable=not_applicable,
        )

        return text_to_combined_search_response_200_output_data_companies_item_li_job_posts_stats_type_0_seniority_stats_type_0

