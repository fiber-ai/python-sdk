from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
    from ..models.create_tracker_company_list_body_company_search_params_type_0 import (
        CreateTrackerCompanyListBodyCompanySearchParamsType0,
    )
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
    from ..models.recent_layoffs import RecentLayoffs
    from ..models.recently_hired_with_title import RecentlyHiredWithTitle
    from ..models.technology_added import TechnologyAdded


T = TypeVar("T", bound="CreateTrackerCompanyListBody")


@_attrs_define
class CreateTrackerCompanyListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (str): Human-readable name for the tracker list.
        refresh_interval_days (int): How often to check tracked companies for changes, in days.
        tracking_rules (list[AcquiredCompany | CompanyDescriptionChanged | CompanyLogoChanged | CompanyNameChanged |
            CompanyNews | CompanyPosted | CompanyPostedWithKeyword | CompanyStatusChanged | CompanyWentInactive |
            DepartmentSizeThreshold | EmployeeCountMilestone | FollowerCountGrowth | FundingStageChanged |
            HeadcountCrossedThreshold | HeadcountGrowthPercent | HQLocationChanged | JobPostingInFunction |
            JobPostingWithKeyword | NewFundingRound | NewInvestor | NewOfficeLocation | NewsWithKeyword | RecentLayoffs |
            RecentlyHiredWithTitle | TechnologyAdded] | None | Unset): Tracking rules to evaluate against this list's
            entities. Multiple rules can be active simultaneously.
        company_search_params (CreateTrackerCompanyListBodyCompanySearchParamsType0 | None | Unset): If provided, this
            list becomes DYNAMIC: rather than adding companies manually, the list auto-populates with companies matching
            these filters and refreshes over time (new matches are added; companies that no longer match are dropped). Uses
            the same filters as the company search endpoint. Omit to create a static, manually-managed list.
        max_dynamic_members (int | None | Unset): For dynamic lists only: the maximum number of companies to keep in the
            list. Defaults to 10000. Ignored for static lists.
    """

    api_key: str
    name: str
    refresh_interval_days: int
    tracking_rules: (
        list[
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
            | RecentLayoffs
            | RecentlyHiredWithTitle
            | TechnologyAdded
        ]
        | None
        | Unset
    ) = UNSET
    company_search_params: CreateTrackerCompanyListBodyCompanySearchParamsType0 | None | Unset = UNSET
    max_dynamic_members: int | None | Unset = UNSET
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
        from ..models.create_tracker_company_list_body_company_search_params_type_0 import (
            CreateTrackerCompanyListBodyCompanySearchParamsType0,  # noqa: PLC0415
        )
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
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle  # noqa: PLC0415
        from ..models.technology_added import TechnologyAdded  # noqa: PLC0415

        api_key = self.api_key

        name = self.name

        refresh_interval_days = self.refresh_interval_days

        tracking_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.tracking_rules, Unset):
            tracking_rules = UNSET
        elif isinstance(self.tracking_rules, list):
            tracking_rules = []
            for tracking_rules_type_0_item_data in self.tracking_rules:
                tracking_rules_type_0_item: dict[str, Any]
                if isinstance(tracking_rules_type_0_item_data, HeadcountCrossedThreshold):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, HeadcountGrowthPercent):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, NewFundingRound):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, FundingStageChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, JobPostingWithKeyword):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, JobPostingInFunction):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, NewsWithKeyword):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyNews):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, HQLocationChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyStatusChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, TechnologyAdded):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyPosted):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyPostedWithKeyword):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, FollowerCountGrowth):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyNameChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyDescriptionChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyWentInactive):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, EmployeeCountMilestone):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, NewOfficeLocation):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, CompanyLogoChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, AcquiredCompany):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, NewInvestor):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, RecentlyHiredWithTitle):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, DepartmentSizeThreshold):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                else:
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()

                tracking_rules.append(tracking_rules_type_0_item)

        else:
            tracking_rules = self.tracking_rules

        company_search_params: dict[str, Any] | None | Unset
        if isinstance(self.company_search_params, Unset):
            company_search_params = UNSET
        elif isinstance(self.company_search_params, CreateTrackerCompanyListBodyCompanySearchParamsType0):
            company_search_params = self.company_search_params.to_dict()
        else:
            company_search_params = self.company_search_params

        max_dynamic_members: int | None | Unset
        if isinstance(self.max_dynamic_members, Unset):
            max_dynamic_members = UNSET
        else:
            max_dynamic_members = self.max_dynamic_members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "name": name,
                "refreshIntervalDays": refresh_interval_days,
            }
        )
        if tracking_rules is not UNSET:
            field_dict["trackingRules"] = tracking_rules
        if company_search_params is not UNSET:
            field_dict["companySearchParams"] = company_search_params
        if max_dynamic_members is not UNSET:
            field_dict["maxDynamicMembers"] = max_dynamic_members

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
        from ..models.create_tracker_company_list_body_company_search_params_type_0 import (
            CreateTrackerCompanyListBodyCompanySearchParamsType0,  # noqa: PLC0415
        )
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
        from ..models.recent_layoffs import RecentLayoffs  # noqa: PLC0415
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle  # noqa: PLC0415
        from ..models.technology_added import TechnologyAdded  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        name = d.pop("name")

        refresh_interval_days = d.pop("refreshIntervalDays")

        def _parse_tracking_rules(
            data: object,
        ) -> (
            list[
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
                | RecentLayoffs
                | RecentlyHiredWithTitle
                | TechnologyAdded
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tracking_rules_type_0 = []
                _tracking_rules_type_0 = data
                for tracking_rules_type_0_item_data in _tracking_rules_type_0:

                    def _parse_tracking_rules_type_0_item(
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
                        | RecentLayoffs
                        | RecentlyHiredWithTitle
                        | TechnologyAdded
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_0 = HeadcountCrossedThreshold.from_dict(data)

                            return tracking_rules_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_1 = HeadcountGrowthPercent.from_dict(data)

                            return tracking_rules_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_2 = NewFundingRound.from_dict(data)

                            return tracking_rules_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_3 = FundingStageChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_4 = JobPostingWithKeyword.from_dict(data)

                            return tracking_rules_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_5 = JobPostingInFunction.from_dict(data)

                            return tracking_rules_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_6 = NewsWithKeyword.from_dict(data)

                            return tracking_rules_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_7 = CompanyNews.from_dict(data)

                            return tracking_rules_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_8 = HQLocationChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_9 = CompanyStatusChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_10 = TechnologyAdded.from_dict(data)

                            return tracking_rules_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_11 = CompanyPosted.from_dict(data)

                            return tracking_rules_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_12 = CompanyPostedWithKeyword.from_dict(data)

                            return tracking_rules_type_0_item_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_13 = FollowerCountGrowth.from_dict(data)

                            return tracking_rules_type_0_item_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_14 = CompanyNameChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_14
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_15 = CompanyDescriptionChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_15
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_16 = CompanyWentInactive.from_dict(data)

                            return tracking_rules_type_0_item_type_16
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_17 = EmployeeCountMilestone.from_dict(data)

                            return tracking_rules_type_0_item_type_17
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_18 = NewOfficeLocation.from_dict(data)

                            return tracking_rules_type_0_item_type_18
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_19 = CompanyLogoChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_19
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_20 = AcquiredCompany.from_dict(data)

                            return tracking_rules_type_0_item_type_20
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_21 = NewInvestor.from_dict(data)

                            return tracking_rules_type_0_item_type_21
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_22 = RecentlyHiredWithTitle.from_dict(data)

                            return tracking_rules_type_0_item_type_22
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_23 = DepartmentSizeThreshold.from_dict(data)

                            return tracking_rules_type_0_item_type_23
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        tracking_rules_type_0_item_type_24 = RecentLayoffs.from_dict(data)

                        return tracking_rules_type_0_item_type_24

                    tracking_rules_type_0_item = _parse_tracking_rules_type_0_item(tracking_rules_type_0_item_data)

                    tracking_rules_type_0.append(tracking_rules_type_0_item)

                return tracking_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
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
                    | RecentLayoffs
                    | RecentlyHiredWithTitle
                    | TechnologyAdded
                ]
                | None
                | Unset,
                data,
            )

        tracking_rules = _parse_tracking_rules(d.pop("trackingRules", UNSET))

        def _parse_company_search_params(
            data: object,
        ) -> CreateTrackerCompanyListBodyCompanySearchParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_search_params_type_0 = CreateTrackerCompanyListBodyCompanySearchParamsType0.from_dict(data)

                return company_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateTrackerCompanyListBodyCompanySearchParamsType0 | None | Unset, data)

        company_search_params = _parse_company_search_params(d.pop("companySearchParams", UNSET))

        def _parse_max_dynamic_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_dynamic_members = _parse_max_dynamic_members(d.pop("maxDynamicMembers", UNSET))

        create_tracker_company_list_body = cls(
            api_key=api_key,
            name=name,
            refresh_interval_days=refresh_interval_days,
            tracking_rules=tracking_rules,
            company_search_params=company_search_params,
            max_dynamic_members=max_dynamic_members,
        )

        create_tracker_company_list_body.additional_properties = d
        return create_tracker_company_list_body

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
