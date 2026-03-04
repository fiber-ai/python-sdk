from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_on_site import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_remote import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote
  from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_hybrid import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid





T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0")



@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0:
    """ 
        Attributes:
            on_site (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite]):
            remote (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote]):
            hybrid (Union[Unset,
                SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid]):
     """

    on_site: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite'] = UNSET
    remote: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote'] = UNSET
    hybrid: Union[Unset, 'SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid'] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_on_site import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_remote import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_hybrid import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid
        on_site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.on_site, Unset):
            on_site = self.on_site.to_dict()

        remote: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remote, Unset):
            remote = self.remote.to_dict()

        hybrid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hybrid, Unset):
            hybrid = self.hybrid.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if on_site is not UNSET:
            field_dict["On-site"] = on_site
        if remote is not UNSET:
            field_dict["Remote"] = remote
        if hybrid is not UNSET:
            field_dict["Hybrid"] = hybrid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_on_site import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_remote import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_hybrid import SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid
        d = dict(src_dict)
        _on_site = d.pop("On-site", UNSET)
        on_site: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite]
        if isinstance(_on_site,  Unset):
            on_site = UNSET
        else:
            on_site = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite.from_dict(_on_site)




        _remote = d.pop("Remote", UNSET)
        remote: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote]
        if isinstance(_remote,  Unset):
            remote = UNSET
        else:
            remote = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote.from_dict(_remote)




        _hybrid = d.pop("Hybrid", UNSET)
        hybrid: Union[Unset, SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid]
        if isinstance(_hybrid,  Unset):
            hybrid = UNSET
        else:
            hybrid = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid.from_dict(_hybrid)




        sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0 = cls(
            on_site=on_site,
            remote=remote,
            hybrid=hybrid,
        )

        return sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_job_location_type_stats_type_0

