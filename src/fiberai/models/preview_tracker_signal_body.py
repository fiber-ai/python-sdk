from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.acquired_company import AcquiredCompany
    from ..models.company_description_changed import CompanyDescriptionChanged
    from ..models.company_logo_changed import CompanyLogoChanged
    from ..models.company_name_changed import CompanyNameChanged
    from ..models.company_news import CompanyNews
    from ..models.company_posted import CompanyPosted
    from ..models.company_posted_with_keyword import CompanyPostedWithKeyword
    from ..models.company_status_changed import CompanyStatusChanged
    from ..models.company_went_inactive import CompanyWentInactive
    from ..models.department_size_threshold import DepartmentSizeThreshold
    from ..models.employee_count_milestone import EmployeeCountMilestone
    from ..models.follower_count_growth import FollowerCountGrowth
    from ..models.funding_stage_changed import FundingStageChanged
    from ..models.headcount_crossed_threshold import HeadcountCrossedThreshold
    from ..models.headcount_growth_percent import HeadcountGrowthPercent
    from ..models.hq_location_changed import HQLocationChanged
    from ..models.job_posting_in_function import JobPostingInFunction
    from ..models.job_posting_with_keyword import JobPostingWithKeyword
    from ..models.new_funding_round import NewFundingRound
    from ..models.new_investor import NewInvestor
    from ..models.new_office_location import NewOfficeLocation
    from ..models.news_with_keyword import NewsWithKeyword
    from ..models.person_became_influencer import PersonBecameInfluencer
    from ..models.person_became_premium import PersonBecamePremium
    from ..models.person_became_top_voice import PersonBecameTopVoice
    from ..models.person_became_verified import PersonBecameVerified
    from ..models.person_changed_company import PersonChangedCompany
    from ..models.person_commented_on_post import PersonCommentedOnPost
    from ..models.person_connections_milestone import PersonConnectionsMilestone
    from ..models.person_employment_type_changed import PersonEmploymentTypeChanged
    from ..models.person_follower_milestone import PersonFollowerMilestone
    from ..models.person_got_demoted import PersonGotDemoted
    from ..models.person_got_promoted import PersonGotPromoted
    from ..models.person_headline_changed import PersonHeadlineChanged
    from ..models.person_is_hiring import PersonIsHiring
    from ..models.person_location_changed import PersonLocationChanged
    from ..models.person_new_certification import PersonNewCertification
    from ..models.person_open_to_work import PersonOpenToWork
    from ..models.person_posted import PersonPosted
    from ..models.person_posted_with_keyword import PersonPostedWithKeyword
    from ..models.person_reacted_to_post import PersonReactedToPost
    from ..models.person_skills_added import PersonSkillsAdded
    from ..models.person_started_company import PersonStartedCompany
    from ..models.person_stealth_changed import PersonStealthChanged
    from ..models.person_stuck_in_role import PersonStuckInRole
    from ..models.person_summary_changed import PersonSummaryChanged
    from ..models.person_tag_gained import PersonTagGained
    from ..models.person_tenure_milestone import PersonTenureMilestone
    from ..models.person_title_changed import PersonTitleChanged
    from ..models.recent_layoffs import RecentLayoffs
    from ..models.recently_hired_with_title import RecentlyHiredWithTitle
    from ..models.technology_added import TechnologyAdded


T = TypeVar("T", bound="PreviewTrackerSignalBody")


@_attrs_define
class PreviewTrackerSignalBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        config (AcquiredCompany | CompanyDescriptionChanged | CompanyLogoChanged | CompanyNameChanged | CompanyNews |
            CompanyPosted | CompanyPostedWithKeyword | CompanyStatusChanged | CompanyWentInactive | DepartmentSizeThreshold
            | EmployeeCountMilestone | FollowerCountGrowth | FundingStageChanged | HeadcountCrossedThreshold |
            HeadcountGrowthPercent | HQLocationChanged | JobPostingInFunction | JobPostingWithKeyword | NewFundingRound |
            NewInvestor | NewOfficeLocation | NewsWithKeyword | PersonBecameInfluencer | PersonBecamePremium |
            PersonBecameTopVoice | PersonBecameVerified | PersonChangedCompany | PersonCommentedOnPost |
            PersonConnectionsMilestone | PersonEmploymentTypeChanged | PersonFollowerMilestone | PersonGotDemoted |
            PersonGotPromoted | PersonHeadlineChanged | PersonIsHiring | PersonLocationChanged | PersonNewCertification |
            PersonOpenToWork | PersonPosted | PersonPostedWithKeyword | PersonReactedToPost | PersonSkillsAdded |
            PersonStartedCompany | PersonStealthChanged | PersonStuckInRole | PersonSummaryChanged | PersonTagGained |
            PersonTenureMilestone | PersonTitleChanged | RecentLayoffs | RecentlyHiredWithTitle | TechnologyAdded): Rule
            configuration to preview. Same shape as when creating a rule.
    """

    api_key: str
    config: (
        AcquiredCompany
        | CompanyDescriptionChanged
        | CompanyLogoChanged
        | CompanyNameChanged
        | CompanyNews
        | CompanyPosted
        | CompanyPostedWithKeyword
        | CompanyStatusChanged
        | CompanyWentInactive
        | DepartmentSizeThreshold
        | EmployeeCountMilestone
        | FollowerCountGrowth
        | FundingStageChanged
        | HeadcountCrossedThreshold
        | HeadcountGrowthPercent
        | HQLocationChanged
        | JobPostingInFunction
        | JobPostingWithKeyword
        | NewFundingRound
        | NewInvestor
        | NewOfficeLocation
        | NewsWithKeyword
        | PersonBecameInfluencer
        | PersonBecamePremium
        | PersonBecameTopVoice
        | PersonBecameVerified
        | PersonChangedCompany
        | PersonCommentedOnPost
        | PersonConnectionsMilestone
        | PersonEmploymentTypeChanged
        | PersonFollowerMilestone
        | PersonGotDemoted
        | PersonGotPromoted
        | PersonHeadlineChanged
        | PersonIsHiring
        | PersonLocationChanged
        | PersonNewCertification
        | PersonOpenToWork
        | PersonPosted
        | PersonPostedWithKeyword
        | PersonReactedToPost
        | PersonSkillsAdded
        | PersonStartedCompany
        | PersonStealthChanged
        | PersonStuckInRole
        | PersonSummaryChanged
        | PersonTagGained
        | PersonTenureMilestone
        | PersonTitleChanged
        | RecentLayoffs
        | RecentlyHiredWithTitle
        | TechnologyAdded
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.acquired_company import AcquiredCompany  # noqa: PLC0415
        from ..models.company_description_changed import CompanyDescriptionChanged  # noqa: PLC0415
        from ..models.company_logo_changed import CompanyLogoChanged  # noqa: PLC0415
        from ..models.company_name_changed import CompanyNameChanged  # noqa: PLC0415
        from ..models.company_news import CompanyNews  # noqa: PLC0415
        from ..models.company_posted import CompanyPosted  # noqa: PLC0415
        from ..models.company_posted_with_keyword import CompanyPostedWithKeyword  # noqa: PLC0415
        from ..models.company_status_changed import CompanyStatusChanged  # noqa: PLC0415
        from ..models.company_went_inactive import CompanyWentInactive  # noqa: PLC0415
        from ..models.department_size_threshold import DepartmentSizeThreshold  # noqa: PLC0415
        from ..models.employee_count_milestone import EmployeeCountMilestone  # noqa: PLC0415
        from ..models.follower_count_growth import FollowerCountGrowth  # noqa: PLC0415
        from ..models.funding_stage_changed import FundingStageChanged  # noqa: PLC0415
        from ..models.headcount_crossed_threshold import HeadcountCrossedThreshold  # noqa: PLC0415
        from ..models.headcount_growth_percent import HeadcountGrowthPercent  # noqa: PLC0415
        from ..models.hq_location_changed import HQLocationChanged  # noqa: PLC0415
        from ..models.job_posting_in_function import JobPostingInFunction  # noqa: PLC0415
        from ..models.job_posting_with_keyword import JobPostingWithKeyword  # noqa: PLC0415
        from ..models.new_funding_round import NewFundingRound  # noqa: PLC0415
        from ..models.new_investor import NewInvestor  # noqa: PLC0415
        from ..models.new_office_location import NewOfficeLocation  # noqa: PLC0415
        from ..models.news_with_keyword import NewsWithKeyword  # noqa: PLC0415
        from ..models.person_became_influencer import PersonBecameInfluencer  # noqa: PLC0415
        from ..models.person_became_premium import PersonBecamePremium  # noqa: PLC0415
        from ..models.person_became_top_voice import PersonBecameTopVoice  # noqa: PLC0415
        from ..models.person_became_verified import PersonBecameVerified  # noqa: PLC0415
        from ..models.person_changed_company import PersonChangedCompany  # noqa: PLC0415
        from ..models.person_commented_on_post import PersonCommentedOnPost  # noqa: PLC0415
        from ..models.person_connections_milestone import PersonConnectionsMilestone  # noqa: PLC0415
        from ..models.person_employment_type_changed import PersonEmploymentTypeChanged  # noqa: PLC0415
        from ..models.person_follower_milestone import PersonFollowerMilestone  # noqa: PLC0415
        from ..models.person_got_demoted import PersonGotDemoted  # noqa: PLC0415
        from ..models.person_got_promoted import PersonGotPromoted  # noqa: PLC0415
        from ..models.person_headline_changed import PersonHeadlineChanged  # noqa: PLC0415
        from ..models.person_is_hiring import PersonIsHiring  # noqa: PLC0415
        from ..models.person_location_changed import PersonLocationChanged  # noqa: PLC0415
        from ..models.person_new_certification import PersonNewCertification  # noqa: PLC0415
        from ..models.person_open_to_work import PersonOpenToWork  # noqa: PLC0415
        from ..models.person_posted import PersonPosted  # noqa: PLC0415
        from ..models.person_posted_with_keyword import PersonPostedWithKeyword  # noqa: PLC0415
        from ..models.person_reacted_to_post import PersonReactedToPost  # noqa: PLC0415
        from ..models.person_skills_added import PersonSkillsAdded  # noqa: PLC0415
        from ..models.person_started_company import PersonStartedCompany  # noqa: PLC0415
        from ..models.person_stealth_changed import PersonStealthChanged  # noqa: PLC0415
        from ..models.person_stuck_in_role import PersonStuckInRole  # noqa: PLC0415
        from ..models.person_summary_changed import PersonSummaryChanged  # noqa: PLC0415
        from ..models.person_tag_gained import PersonTagGained  # noqa: PLC0415
        from ..models.person_title_changed import PersonTitleChanged  # noqa: PLC0415
        from ..models.recent_layoffs import RecentLayoffs  # noqa: PLC0415
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle  # noqa: PLC0415
        from ..models.technology_added import TechnologyAdded  # noqa: PLC0415

        api_key = self.api_key

        config: dict[str, Any]
        if isinstance(self.config, HeadcountCrossedThreshold):
            config = self.config.to_dict()
        elif isinstance(self.config, HeadcountGrowthPercent):
            config = self.config.to_dict()
        elif isinstance(self.config, NewFundingRound):
            config = self.config.to_dict()
        elif isinstance(self.config, FundingStageChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, JobPostingWithKeyword):
            config = self.config.to_dict()
        elif isinstance(self.config, JobPostingInFunction):
            config = self.config.to_dict()
        elif isinstance(self.config, NewsWithKeyword):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyNews):
            config = self.config.to_dict()
        elif isinstance(self.config, HQLocationChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyStatusChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, TechnologyAdded):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyPosted):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyPostedWithKeyword):
            config = self.config.to_dict()
        elif isinstance(self.config, FollowerCountGrowth):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyNameChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyDescriptionChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyWentInactive):
            config = self.config.to_dict()
        elif isinstance(self.config, EmployeeCountMilestone):
            config = self.config.to_dict()
        elif isinstance(self.config, NewOfficeLocation):
            config = self.config.to_dict()
        elif isinstance(self.config, CompanyLogoChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, AcquiredCompany):
            config = self.config.to_dict()
        elif isinstance(self.config, NewInvestor):
            config = self.config.to_dict()
        elif isinstance(self.config, RecentlyHiredWithTitle):
            config = self.config.to_dict()
        elif isinstance(self.config, DepartmentSizeThreshold):
            config = self.config.to_dict()
        elif isinstance(self.config, RecentLayoffs):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonChangedCompany):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonTitleChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonStealthChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonOpenToWork):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonIsHiring):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonHeadlineChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonLocationChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonTagGained):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonPosted):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonPostedWithKeyword):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonReactedToPost):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonCommentedOnPost):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonSkillsAdded):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonGotPromoted):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonStartedCompany):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonEmploymentTypeChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonConnectionsMilestone):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonFollowerMilestone):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonSummaryChanged):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonNewCertification):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonBecameVerified):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonBecamePremium):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonBecameInfluencer):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonBecameTopVoice):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonGotDemoted):
            config = self.config.to_dict()
        elif isinstance(self.config, PersonStuckInRole):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acquired_company import AcquiredCompany  # noqa: PLC0415
        from ..models.company_description_changed import CompanyDescriptionChanged  # noqa: PLC0415
        from ..models.company_logo_changed import CompanyLogoChanged  # noqa: PLC0415
        from ..models.company_name_changed import CompanyNameChanged  # noqa: PLC0415
        from ..models.company_news import CompanyNews  # noqa: PLC0415
        from ..models.company_posted import CompanyPosted  # noqa: PLC0415
        from ..models.company_posted_with_keyword import CompanyPostedWithKeyword  # noqa: PLC0415
        from ..models.company_status_changed import CompanyStatusChanged  # noqa: PLC0415
        from ..models.company_went_inactive import CompanyWentInactive  # noqa: PLC0415
        from ..models.department_size_threshold import DepartmentSizeThreshold  # noqa: PLC0415
        from ..models.employee_count_milestone import EmployeeCountMilestone  # noqa: PLC0415
        from ..models.follower_count_growth import FollowerCountGrowth  # noqa: PLC0415
        from ..models.funding_stage_changed import FundingStageChanged  # noqa: PLC0415
        from ..models.headcount_crossed_threshold import HeadcountCrossedThreshold  # noqa: PLC0415
        from ..models.headcount_growth_percent import HeadcountGrowthPercent  # noqa: PLC0415
        from ..models.hq_location_changed import HQLocationChanged  # noqa: PLC0415
        from ..models.job_posting_in_function import JobPostingInFunction  # noqa: PLC0415
        from ..models.job_posting_with_keyword import JobPostingWithKeyword  # noqa: PLC0415
        from ..models.new_funding_round import NewFundingRound  # noqa: PLC0415
        from ..models.new_investor import NewInvestor  # noqa: PLC0415
        from ..models.new_office_location import NewOfficeLocation  # noqa: PLC0415
        from ..models.news_with_keyword import NewsWithKeyword  # noqa: PLC0415
        from ..models.person_became_influencer import PersonBecameInfluencer  # noqa: PLC0415
        from ..models.person_became_premium import PersonBecamePremium  # noqa: PLC0415
        from ..models.person_became_top_voice import PersonBecameTopVoice  # noqa: PLC0415
        from ..models.person_became_verified import PersonBecameVerified  # noqa: PLC0415
        from ..models.person_changed_company import PersonChangedCompany  # noqa: PLC0415
        from ..models.person_commented_on_post import PersonCommentedOnPost  # noqa: PLC0415
        from ..models.person_connections_milestone import PersonConnectionsMilestone  # noqa: PLC0415
        from ..models.person_employment_type_changed import PersonEmploymentTypeChanged  # noqa: PLC0415
        from ..models.person_follower_milestone import PersonFollowerMilestone  # noqa: PLC0415
        from ..models.person_got_demoted import PersonGotDemoted  # noqa: PLC0415
        from ..models.person_got_promoted import PersonGotPromoted  # noqa: PLC0415
        from ..models.person_headline_changed import PersonHeadlineChanged  # noqa: PLC0415
        from ..models.person_is_hiring import PersonIsHiring  # noqa: PLC0415
        from ..models.person_location_changed import PersonLocationChanged  # noqa: PLC0415
        from ..models.person_new_certification import PersonNewCertification  # noqa: PLC0415
        from ..models.person_open_to_work import PersonOpenToWork  # noqa: PLC0415
        from ..models.person_posted import PersonPosted  # noqa: PLC0415
        from ..models.person_posted_with_keyword import PersonPostedWithKeyword  # noqa: PLC0415
        from ..models.person_reacted_to_post import PersonReactedToPost  # noqa: PLC0415
        from ..models.person_skills_added import PersonSkillsAdded  # noqa: PLC0415
        from ..models.person_started_company import PersonStartedCompany  # noqa: PLC0415
        from ..models.person_stealth_changed import PersonStealthChanged  # noqa: PLC0415
        from ..models.person_stuck_in_role import PersonStuckInRole  # noqa: PLC0415
        from ..models.person_summary_changed import PersonSummaryChanged  # noqa: PLC0415
        from ..models.person_tag_gained import PersonTagGained  # noqa: PLC0415
        from ..models.person_tenure_milestone import PersonTenureMilestone  # noqa: PLC0415
        from ..models.person_title_changed import PersonTitleChanged  # noqa: PLC0415
        from ..models.recent_layoffs import RecentLayoffs  # noqa: PLC0415
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle  # noqa: PLC0415
        from ..models.technology_added import TechnologyAdded  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_config(
            data: object,
        ) -> (
            AcquiredCompany
            | CompanyDescriptionChanged
            | CompanyLogoChanged
            | CompanyNameChanged
            | CompanyNews
            | CompanyPosted
            | CompanyPostedWithKeyword
            | CompanyStatusChanged
            | CompanyWentInactive
            | DepartmentSizeThreshold
            | EmployeeCountMilestone
            | FollowerCountGrowth
            | FundingStageChanged
            | HeadcountCrossedThreshold
            | HeadcountGrowthPercent
            | HQLocationChanged
            | JobPostingInFunction
            | JobPostingWithKeyword
            | NewFundingRound
            | NewInvestor
            | NewOfficeLocation
            | NewsWithKeyword
            | PersonBecameInfluencer
            | PersonBecamePremium
            | PersonBecameTopVoice
            | PersonBecameVerified
            | PersonChangedCompany
            | PersonCommentedOnPost
            | PersonConnectionsMilestone
            | PersonEmploymentTypeChanged
            | PersonFollowerMilestone
            | PersonGotDemoted
            | PersonGotPromoted
            | PersonHeadlineChanged
            | PersonIsHiring
            | PersonLocationChanged
            | PersonNewCertification
            | PersonOpenToWork
            | PersonPosted
            | PersonPostedWithKeyword
            | PersonReactedToPost
            | PersonSkillsAdded
            | PersonStartedCompany
            | PersonStealthChanged
            | PersonStuckInRole
            | PersonSummaryChanged
            | PersonTagGained
            | PersonTenureMilestone
            | PersonTitleChanged
            | RecentLayoffs
            | RecentlyHiredWithTitle
            | TechnologyAdded
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = HeadcountCrossedThreshold.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = HeadcountGrowthPercent.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_2 = NewFundingRound.from_dict(data)

                return config_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_3 = FundingStageChanged.from_dict(data)

                return config_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_4 = JobPostingWithKeyword.from_dict(data)

                return config_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_5 = JobPostingInFunction.from_dict(data)

                return config_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_6 = NewsWithKeyword.from_dict(data)

                return config_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_7 = CompanyNews.from_dict(data)

                return config_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_8 = HQLocationChanged.from_dict(data)

                return config_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_9 = CompanyStatusChanged.from_dict(data)

                return config_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_10 = TechnologyAdded.from_dict(data)

                return config_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_11 = CompanyPosted.from_dict(data)

                return config_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_12 = CompanyPostedWithKeyword.from_dict(data)

                return config_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_13 = FollowerCountGrowth.from_dict(data)

                return config_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_14 = CompanyNameChanged.from_dict(data)

                return config_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_15 = CompanyDescriptionChanged.from_dict(data)

                return config_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_16 = CompanyWentInactive.from_dict(data)

                return config_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_17 = EmployeeCountMilestone.from_dict(data)

                return config_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_18 = NewOfficeLocation.from_dict(data)

                return config_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_19 = CompanyLogoChanged.from_dict(data)

                return config_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_20 = AcquiredCompany.from_dict(data)

                return config_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_21 = NewInvestor.from_dict(data)

                return config_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_22 = RecentlyHiredWithTitle.from_dict(data)

                return config_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_23 = DepartmentSizeThreshold.from_dict(data)

                return config_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_24 = RecentLayoffs.from_dict(data)

                return config_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_25 = PersonChangedCompany.from_dict(data)

                return config_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_26 = PersonTitleChanged.from_dict(data)

                return config_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_27 = PersonStealthChanged.from_dict(data)

                return config_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_28 = PersonOpenToWork.from_dict(data)

                return config_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_29 = PersonIsHiring.from_dict(data)

                return config_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_30 = PersonHeadlineChanged.from_dict(data)

                return config_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_31 = PersonLocationChanged.from_dict(data)

                return config_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_32 = PersonTagGained.from_dict(data)

                return config_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_33 = PersonPosted.from_dict(data)

                return config_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_34 = PersonPostedWithKeyword.from_dict(data)

                return config_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_35 = PersonReactedToPost.from_dict(data)

                return config_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_36 = PersonCommentedOnPost.from_dict(data)

                return config_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_37 = PersonSkillsAdded.from_dict(data)

                return config_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_38 = PersonGotPromoted.from_dict(data)

                return config_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_39 = PersonStartedCompany.from_dict(data)

                return config_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_40 = PersonEmploymentTypeChanged.from_dict(data)

                return config_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_41 = PersonConnectionsMilestone.from_dict(data)

                return config_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_42 = PersonFollowerMilestone.from_dict(data)

                return config_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_43 = PersonSummaryChanged.from_dict(data)

                return config_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_44 = PersonNewCertification.from_dict(data)

                return config_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_45 = PersonBecameVerified.from_dict(data)

                return config_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_46 = PersonBecamePremium.from_dict(data)

                return config_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_47 = PersonBecameInfluencer.from_dict(data)

                return config_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_48 = PersonBecameTopVoice.from_dict(data)

                return config_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_49 = PersonGotDemoted.from_dict(data)

                return config_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_50 = PersonStuckInRole.from_dict(data)

                return config_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_51 = PersonTenureMilestone.from_dict(data)

            return config_type_51

        config = _parse_config(d.pop("config"))

        preview_tracker_signal_body = cls(
            api_key=api_key,
            config=config,
        )

        preview_tracker_signal_body.additional_properties = d
        return preview_tracker_signal_body

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
