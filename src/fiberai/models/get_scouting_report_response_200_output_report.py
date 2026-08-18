from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_scouting_report_response_200_output_report_blog_posts_item import (
        GetScoutingReportResponse200OutputReportBlogPostsItem,
    )
    from ..models.get_scouting_report_response_200_output_report_company_photos_item import (
        GetScoutingReportResponse200OutputReportCompanyPhotosItem,
    )
    from ..models.get_scouting_report_response_200_output_report_company_profile_type_0 import (
        GetScoutingReportResponse200OutputReportCompanyProfileType0,
    )
    from ..models.get_scouting_report_response_200_output_report_founders_item import (
        GetScoutingReportResponse200OutputReportFoundersItem,
    )
    from ..models.get_scouting_report_response_200_output_report_funding_info_type_0 import (
        GetScoutingReportResponse200OutputReportFundingInfoType0,
    )
    from ..models.get_scouting_report_response_200_output_report_historical_headcount_type_0 import (
        GetScoutingReportResponse200OutputReportHistoricalHeadcountType0,
    )
    from ..models.get_scouting_report_response_200_output_report_job_posts_item import (
        GetScoutingReportResponse200OutputReportJobPostsItem,
    )
    from ..models.get_scouting_report_response_200_output_report_media_links_item import (
        GetScoutingReportResponse200OutputReportMediaLinksItem,
    )
    from ..models.get_scouting_report_response_200_output_report_milestones_item import (
        GetScoutingReportResponse200OutputReportMilestonesItem,
    )
    from ..models.get_scouting_report_response_200_output_report_news_item import (
        GetScoutingReportResponse200OutputReportNewsItem,
    )
    from ..models.get_scouting_report_response_200_output_report_office_locations_item import (
        GetScoutingReportResponse200OutputReportOfficeLocationsItem,
    )


T = TypeVar("T", bound="GetScoutingReportResponse200OutputReport")


@_attrs_define
class GetScoutingReportResponse200OutputReport:
    """The generated scouting report

    Attributes:
        news (list[GetScoutingReportResponse200OutputReportNewsItem]):
        media_links (list[GetScoutingReportResponse200OutputReportMediaLinksItem]):
        blog_posts (list[GetScoutingReportResponse200OutputReportBlogPostsItem]):
        company_photos (list[GetScoutingReportResponse200OutputReportCompanyPhotosItem]):
        milestones (list[GetScoutingReportResponse200OutputReportMilestonesItem]):
        job_posts (list[GetScoutingReportResponse200OutputReportJobPostsItem]):
        founders (list[GetScoutingReportResponse200OutputReportFoundersItem]):
        historical_headcount (GetScoutingReportResponse200OutputReportHistoricalHeadcountType0 | None):
        company_summary (None | str):
        company_profile (GetScoutingReportResponse200OutputReportCompanyProfileType0 | None):
        office_locations (list[GetScoutingReportResponse200OutputReportOfficeLocationsItem]): Company office locations
            with structured address details and coordinates. Empty when no office data is available.
        about_description (None | str | Unset):
        funding_info (GetScoutingReportResponse200OutputReportFundingInfoType0 | None | Unset):
    """

    news: list[GetScoutingReportResponse200OutputReportNewsItem]
    media_links: list[GetScoutingReportResponse200OutputReportMediaLinksItem]
    blog_posts: list[GetScoutingReportResponse200OutputReportBlogPostsItem]
    company_photos: list[GetScoutingReportResponse200OutputReportCompanyPhotosItem]
    milestones: list[GetScoutingReportResponse200OutputReportMilestonesItem]
    job_posts: list[GetScoutingReportResponse200OutputReportJobPostsItem]
    founders: list[GetScoutingReportResponse200OutputReportFoundersItem]
    historical_headcount: GetScoutingReportResponse200OutputReportHistoricalHeadcountType0 | None
    company_summary: None | str
    company_profile: GetScoutingReportResponse200OutputReportCompanyProfileType0 | None
    office_locations: list[GetScoutingReportResponse200OutputReportOfficeLocationsItem]
    about_description: None | str | Unset = UNSET
    funding_info: GetScoutingReportResponse200OutputReportFundingInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_scouting_report_response_200_output_report_company_profile_type_0 import (
            GetScoutingReportResponse200OutputReportCompanyProfileType0,
        )
        from ..models.get_scouting_report_response_200_output_report_funding_info_type_0 import (
            GetScoutingReportResponse200OutputReportFundingInfoType0,
        )
        from ..models.get_scouting_report_response_200_output_report_historical_headcount_type_0 import (
            GetScoutingReportResponse200OutputReportHistoricalHeadcountType0,
        )

        news = []
        for news_item_data in self.news:
            news_item = news_item_data.to_dict()
            news.append(news_item)

        media_links = []
        for media_links_item_data in self.media_links:
            media_links_item = media_links_item_data.to_dict()
            media_links.append(media_links_item)

        blog_posts = []
        for blog_posts_item_data in self.blog_posts:
            blog_posts_item = blog_posts_item_data.to_dict()
            blog_posts.append(blog_posts_item)

        company_photos = []
        for company_photos_item_data in self.company_photos:
            company_photos_item = company_photos_item_data.to_dict()
            company_photos.append(company_photos_item)

        milestones = []
        for milestones_item_data in self.milestones:
            milestones_item = milestones_item_data.to_dict()
            milestones.append(milestones_item)

        job_posts = []
        for job_posts_item_data in self.job_posts:
            job_posts_item = job_posts_item_data.to_dict()
            job_posts.append(job_posts_item)

        founders = []
        for founders_item_data in self.founders:
            founders_item = founders_item_data.to_dict()
            founders.append(founders_item)

        historical_headcount: dict[str, Any] | None
        if isinstance(self.historical_headcount, GetScoutingReportResponse200OutputReportHistoricalHeadcountType0):
            historical_headcount = self.historical_headcount.to_dict()
        else:
            historical_headcount = self.historical_headcount

        company_summary: None | str
        company_summary = self.company_summary

        company_profile: dict[str, Any] | None
        if isinstance(self.company_profile, GetScoutingReportResponse200OutputReportCompanyProfileType0):
            company_profile = self.company_profile.to_dict()
        else:
            company_profile = self.company_profile

        office_locations = []
        for office_locations_item_data in self.office_locations:
            office_locations_item = office_locations_item_data.to_dict()
            office_locations.append(office_locations_item)

        about_description: None | str | Unset
        if isinstance(self.about_description, Unset):
            about_description = UNSET
        else:
            about_description = self.about_description

        funding_info: dict[str, Any] | None | Unset
        if isinstance(self.funding_info, Unset):
            funding_info = UNSET
        elif isinstance(self.funding_info, GetScoutingReportResponse200OutputReportFundingInfoType0):
            funding_info = self.funding_info.to_dict()
        else:
            funding_info = self.funding_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "news": news,
                "mediaLinks": media_links,
                "blogPosts": blog_posts,
                "companyPhotos": company_photos,
                "milestones": milestones,
                "jobPosts": job_posts,
                "founders": founders,
                "historicalHeadcount": historical_headcount,
                "companySummary": company_summary,
                "companyProfile": company_profile,
                "officeLocations": office_locations,
            }
        )
        if about_description is not UNSET:
            field_dict["aboutDescription"] = about_description
        if funding_info is not UNSET:
            field_dict["fundingInfo"] = funding_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_scouting_report_response_200_output_report_blog_posts_item import (
            GetScoutingReportResponse200OutputReportBlogPostsItem,
        )
        from ..models.get_scouting_report_response_200_output_report_company_photos_item import (
            GetScoutingReportResponse200OutputReportCompanyPhotosItem,
        )
        from ..models.get_scouting_report_response_200_output_report_company_profile_type_0 import (
            GetScoutingReportResponse200OutputReportCompanyProfileType0,
        )
        from ..models.get_scouting_report_response_200_output_report_founders_item import (
            GetScoutingReportResponse200OutputReportFoundersItem,
        )
        from ..models.get_scouting_report_response_200_output_report_funding_info_type_0 import (
            GetScoutingReportResponse200OutputReportFundingInfoType0,
        )
        from ..models.get_scouting_report_response_200_output_report_historical_headcount_type_0 import (
            GetScoutingReportResponse200OutputReportHistoricalHeadcountType0,
        )
        from ..models.get_scouting_report_response_200_output_report_job_posts_item import (
            GetScoutingReportResponse200OutputReportJobPostsItem,
        )
        from ..models.get_scouting_report_response_200_output_report_media_links_item import (
            GetScoutingReportResponse200OutputReportMediaLinksItem,
        )
        from ..models.get_scouting_report_response_200_output_report_milestones_item import (
            GetScoutingReportResponse200OutputReportMilestonesItem,
        )
        from ..models.get_scouting_report_response_200_output_report_news_item import (
            GetScoutingReportResponse200OutputReportNewsItem,
        )
        from ..models.get_scouting_report_response_200_output_report_office_locations_item import (
            GetScoutingReportResponse200OutputReportOfficeLocationsItem,
        )

        d = dict(src_dict)
        news = []
        _news = d.pop("news")
        for news_item_data in _news:
            news_item = GetScoutingReportResponse200OutputReportNewsItem.from_dict(news_item_data)

            news.append(news_item)

        media_links = []
        _media_links = d.pop("mediaLinks")
        for media_links_item_data in _media_links:
            media_links_item = GetScoutingReportResponse200OutputReportMediaLinksItem.from_dict(media_links_item_data)

            media_links.append(media_links_item)

        blog_posts = []
        _blog_posts = d.pop("blogPosts")
        for blog_posts_item_data in _blog_posts:
            blog_posts_item = GetScoutingReportResponse200OutputReportBlogPostsItem.from_dict(blog_posts_item_data)

            blog_posts.append(blog_posts_item)

        company_photos = []
        _company_photos = d.pop("companyPhotos")
        for company_photos_item_data in _company_photos:
            company_photos_item = GetScoutingReportResponse200OutputReportCompanyPhotosItem.from_dict(
                company_photos_item_data
            )

            company_photos.append(company_photos_item)

        milestones = []
        _milestones = d.pop("milestones")
        for milestones_item_data in _milestones:
            milestones_item = GetScoutingReportResponse200OutputReportMilestonesItem.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        job_posts = []
        _job_posts = d.pop("jobPosts")
        for job_posts_item_data in _job_posts:
            job_posts_item = GetScoutingReportResponse200OutputReportJobPostsItem.from_dict(job_posts_item_data)

            job_posts.append(job_posts_item)

        founders = []
        _founders = d.pop("founders")
        for founders_item_data in _founders:
            founders_item = GetScoutingReportResponse200OutputReportFoundersItem.from_dict(founders_item_data)

            founders.append(founders_item)

        def _parse_historical_headcount(
            data: object,
        ) -> GetScoutingReportResponse200OutputReportHistoricalHeadcountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                historical_headcount_type_0 = (
                    GetScoutingReportResponse200OutputReportHistoricalHeadcountType0.from_dict(data)
                )

                return historical_headcount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetScoutingReportResponse200OutputReportHistoricalHeadcountType0 | None, data)

        historical_headcount = _parse_historical_headcount(d.pop("historicalHeadcount"))

        def _parse_company_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_summary = _parse_company_summary(d.pop("companySummary"))

        def _parse_company_profile(data: object) -> GetScoutingReportResponse200OutputReportCompanyProfileType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_profile_type_0 = GetScoutingReportResponse200OutputReportCompanyProfileType0.from_dict(data)

                return company_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetScoutingReportResponse200OutputReportCompanyProfileType0 | None, data)

        company_profile = _parse_company_profile(d.pop("companyProfile"))

        office_locations = []
        _office_locations = d.pop("officeLocations")
        for office_locations_item_data in _office_locations:
            office_locations_item = GetScoutingReportResponse200OutputReportOfficeLocationsItem.from_dict(
                office_locations_item_data
            )

            office_locations.append(office_locations_item)

        def _parse_about_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        about_description = _parse_about_description(d.pop("aboutDescription", UNSET))

        def _parse_funding_info(
            data: object,
        ) -> GetScoutingReportResponse200OutputReportFundingInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                funding_info_type_0 = GetScoutingReportResponse200OutputReportFundingInfoType0.from_dict(data)

                return funding_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetScoutingReportResponse200OutputReportFundingInfoType0 | None | Unset, data)

        funding_info = _parse_funding_info(d.pop("fundingInfo", UNSET))

        get_scouting_report_response_200_output_report = cls(
            news=news,
            media_links=media_links,
            blog_posts=blog_posts,
            company_photos=company_photos,
            milestones=milestones,
            job_posts=job_posts,
            founders=founders,
            historical_headcount=historical_headcount,
            company_summary=company_summary,
            company_profile=company_profile,
            office_locations=office_locations,
            about_description=about_description,
            funding_info=funding_info,
        )

        get_scouting_report_response_200_output_report.additional_properties = d
        return get_scouting_report_response_200_output_report

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
