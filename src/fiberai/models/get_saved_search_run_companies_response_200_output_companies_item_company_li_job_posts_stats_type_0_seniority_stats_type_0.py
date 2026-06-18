from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_associate import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_director import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_entry_level import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0EntryLevel,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_executive import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_internship import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Internship,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_mid_senior_level import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_not_applicable import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0NotApplicable,
    )


T = TypeVar(
    "T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0"
)


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0:
    """
    Attributes:
        entry_level (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsTy
            pe0EntryLevel | Unset):
        director
            (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director
            | Unset):
        associate
            (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate
            | Unset):
        mid_senior_level (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SenioritySt
            atsType0MidSeniorLevel | Unset):
        internship (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsTyp
            e0Internship | Unset):
        executive
            (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive
            | Unset):
        not_applicable (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStat
            sType0NotApplicable | Unset):
    """

    entry_level: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0EntryLevel
        | Unset
    ) = UNSET
    director: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director
        | Unset
    ) = UNSET
    associate: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate
        | Unset
    ) = UNSET
    mid_senior_level: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel
        | Unset
    ) = UNSET
    internship: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Internship
        | Unset
    ) = UNSET
    executive: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive
        | Unset
    ) = UNSET
    not_applicable: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0NotApplicable
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        entry_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entry_level, Unset):
            entry_level = self.entry_level.to_dict()

        director: dict[str, Any] | Unset = UNSET
        if not isinstance(self.director, Unset):
            director = self.director.to_dict()

        associate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.associate, Unset):
            associate = self.associate.to_dict()

        mid_senior_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mid_senior_level, Unset):
            mid_senior_level = self.mid_senior_level.to_dict()

        internship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internship, Unset):
            internship = self.internship.to_dict()

        executive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executive, Unset):
            executive = self.executive.to_dict()

        not_applicable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_applicable, Unset):
            not_applicable = self.not_applicable.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_associate import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_director import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_entry_level import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0EntryLevel,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_executive import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_internship import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Internship,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_mid_senior_level import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel,
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0_not_applicable import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0NotApplicable,
        )

        d = dict(src_dict)
        _entry_level = d.pop("Entry level", UNSET)
        entry_level: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0EntryLevel
            | Unset
        )
        if isinstance(_entry_level, Unset):
            entry_level = UNSET
        else:
            entry_level = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0EntryLevel.from_dict(
                _entry_level
            )

        _director = d.pop("Director", UNSET)
        director: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director
            | Unset
        )
        if isinstance(_director, Unset):
            director = UNSET
        else:
            director = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Director.from_dict(
                _director
            )

        _associate = d.pop("Associate", UNSET)
        associate: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate
            | Unset
        )
        if isinstance(_associate, Unset):
            associate = UNSET
        else:
            associate = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Associate.from_dict(
                _associate
            )

        _mid_senior_level = d.pop("Mid-Senior level", UNSET)
        mid_senior_level: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel
            | Unset
        )
        if isinstance(_mid_senior_level, Unset):
            mid_senior_level = UNSET
        else:
            mid_senior_level = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0MidSeniorLevel.from_dict(
                _mid_senior_level
            )

        _internship = d.pop("Internship", UNSET)
        internship: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Internship
            | Unset
        )
        if isinstance(_internship, Unset):
            internship = UNSET
        else:
            internship = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Internship.from_dict(
                _internship
            )

        _executive = d.pop("Executive", UNSET)
        executive: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive
            | Unset
        )
        if isinstance(_executive, Unset):
            executive = UNSET
        else:
            executive = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0Executive.from_dict(
                _executive
            )

        _not_applicable = d.pop("Not Applicable", UNSET)
        not_applicable: (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0NotApplicable
            | Unset
        )
        if isinstance(_not_applicable, Unset):
            not_applicable = UNSET
        else:
            not_applicable = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiJobPostsStatsType0SeniorityStatsType0NotApplicable.from_dict(
                _not_applicable
            )

        get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0 = cls(
            entry_level=entry_level,
            director=director,
            associate=associate,
            mid_senior_level=mid_senior_level,
            internship=internship,
            executive=executive,
            not_applicable=not_applicable,
        )

        return get_saved_search_run_companies_response_200_output_companies_item_company_li_job_posts_stats_type_0_seniority_stats_type_0
