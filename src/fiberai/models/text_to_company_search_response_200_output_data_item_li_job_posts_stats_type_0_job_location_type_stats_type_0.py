from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_hybrid import (
        TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid,
    )
    from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_on_site import (
        TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite,
    )
    from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_remote import (
        TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote,
    )


T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0")


@_attrs_define
class TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0:
    """
    Attributes:
        on_site (TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite |
            Unset):
        remote (TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote |
            Unset):
        hybrid (TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid |
            Unset):
    """

    on_site: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite | Unset = (
        UNSET
    )
    remote: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote | Unset = (
        UNSET
    )
    hybrid: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        on_site: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_site, Unset):
            on_site = self.on_site.to_dict()

        remote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote, Unset):
            remote = self.remote.to_dict()

        hybrid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hybrid, Unset):
            hybrid = self.hybrid.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if on_site is not UNSET:
            field_dict["On-site"] = on_site
        if remote is not UNSET:
            field_dict["Remote"] = remote
        if hybrid is not UNSET:
            field_dict["Hybrid"] = hybrid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_hybrid import (
            TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid,
        )
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_on_site import (
            TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite,
        )
        from ..models.text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0_remote import (
            TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote,
        )

        d = dict(src_dict)
        _on_site = d.pop("On-site", UNSET)
        on_site: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite | Unset
        if isinstance(_on_site, Unset):
            on_site = UNSET
        else:
            on_site = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0OnSite.from_dict(
                _on_site
            )

        _remote = d.pop("Remote", UNSET)
        remote: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote | Unset
        if isinstance(_remote, Unset):
            remote = UNSET
        else:
            remote = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Remote.from_dict(
                _remote
            )

        _hybrid = d.pop("Hybrid", UNSET)
        hybrid: TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid | Unset
        if isinstance(_hybrid, Unset):
            hybrid = UNSET
        else:
            hybrid = TextToCompanySearchResponse200OutputDataItemLiJobPostsStatsType0JobLocationTypeStatsType0Hybrid.from_dict(
                _hybrid
            )

        text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0 = cls(
            on_site=on_site,
            remote=remote,
            hybrid=hybrid,
        )

        return text_to_company_search_response_200_output_data_item_li_job_posts_stats_type_0_job_location_type_stats_type_0
