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
    from ..models.update_tracker_company_list_body_update_rule_flags_type_0_item import (
        UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item,
    )


T = TypeVar("T", bound="UpdateTrackerCompanyListBody")


@_attrs_define
class UpdateTrackerCompanyListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (None | str | Unset): New name for the list.
        refresh_interval_days (int | None | Unset): New check interval in days.
        is_active (bool | None | Unset): Pause or resume monitoring on the list.
        tracking_rules (list[AcquiredCompany | CompanyDescriptionChanged | CompanyLogoChanged | CompanyNameChanged |
            CompanyNews | CompanyPosted | CompanyPostedWithKeyword | CompanyStatusChanged | CompanyWentInactive |
            DepartmentSizeThreshold | EmployeeCountMilestone | FollowerCountGrowth | FundingStageChanged |
            HeadcountCrossedThreshold | HeadcountGrowthPercent | HQLocationChanged | JobPostingInFunction |
            JobPostingWithKeyword | NewFundingRound | NewInvestor | NewOfficeLocation | NewsWithKeyword | RecentLayoffs |
            RecentlyHiredWithTitle | TechnologyAdded] | None | Unset): Replace ALL existing rules with this set. Pass empty
            array to clear all rules. Omit to leave unchanged. Cannot be used with `addRules`/`removeRuleIds`.
        add_rules (list[AcquiredCompany | CompanyDescriptionChanged | CompanyLogoChanged | CompanyNameChanged |
            CompanyNews | CompanyPosted | CompanyPostedWithKeyword | CompanyStatusChanged | CompanyWentInactive |
            DepartmentSizeThreshold | EmployeeCountMilestone | FollowerCountGrowth | FundingStageChanged |
            HeadcountCrossedThreshold | HeadcountGrowthPercent | HQLocationChanged | JobPostingInFunction |
            JobPostingWithKeyword | NewFundingRound | NewInvestor | NewOfficeLocation | NewsWithKeyword | RecentLayoffs |
            RecentlyHiredWithTitle | TechnologyAdded] | None | Unset): Add rules to the existing set without removing
            others. The total active rules on the list (existing + added) must not exceed the per-list cap. Cannot be used
            with `trackingRules`.
        remove_rule_ids (list[str] | None | Unset): Rule IDs to remove. Cannot be used with `trackingRules`.
        update_rule_flags (list[UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item] | None | Unset): Toggle `isDummy`
            on existing rules by ID. Use this to convert a real rule into a dummy rule (or vice versa) without recreating
            it.
    """

    api_key: str
    name: None | str | Unset = UNSET
    refresh_interval_days: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
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
    add_rules: (
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
    remove_rule_ids: list[str] | None | Unset = UNSET
    update_rule_flags: list[UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle
        from ..models.technology_added import TechnologyAdded

        api_key = self.api_key

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        refresh_interval_days: int | None | Unset
        if isinstance(self.refresh_interval_days, Unset):
            refresh_interval_days = UNSET
        else:
            refresh_interval_days = self.refresh_interval_days

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

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

        add_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.add_rules, Unset):
            add_rules = UNSET
        elif isinstance(self.add_rules, list):
            add_rules = []
            for add_rules_type_0_item_data in self.add_rules:
                add_rules_type_0_item: dict[str, Any]
                if isinstance(add_rules_type_0_item_data, HeadcountCrossedThreshold):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, HeadcountGrowthPercent):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, NewFundingRound):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, FundingStageChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, JobPostingWithKeyword):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, JobPostingInFunction):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, NewsWithKeyword):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyNews):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, HQLocationChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyStatusChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, TechnologyAdded):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyPosted):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyPostedWithKeyword):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, FollowerCountGrowth):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyNameChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyDescriptionChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyWentInactive):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, EmployeeCountMilestone):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, NewOfficeLocation):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, CompanyLogoChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, AcquiredCompany):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, NewInvestor):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, RecentlyHiredWithTitle):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, DepartmentSizeThreshold):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                else:
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()

                add_rules.append(add_rules_type_0_item)

        else:
            add_rules = self.add_rules

        remove_rule_ids: list[str] | None | Unset
        if isinstance(self.remove_rule_ids, Unset):
            remove_rule_ids = UNSET
        elif isinstance(self.remove_rule_ids, list):
            remove_rule_ids = self.remove_rule_ids

        else:
            remove_rule_ids = self.remove_rule_ids

        update_rule_flags: list[dict[str, Any]] | None | Unset
        if isinstance(self.update_rule_flags, Unset):
            update_rule_flags = UNSET
        elif isinstance(self.update_rule_flags, list):
            update_rule_flags = []
            for update_rule_flags_type_0_item_data in self.update_rule_flags:
                update_rule_flags_type_0_item = update_rule_flags_type_0_item_data.to_dict()
                update_rule_flags.append(update_rule_flags_type_0_item)

        else:
            update_rule_flags = self.update_rule_flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if refresh_interval_days is not UNSET:
            field_dict["refreshIntervalDays"] = refresh_interval_days
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if tracking_rules is not UNSET:
            field_dict["trackingRules"] = tracking_rules
        if add_rules is not UNSET:
            field_dict["addRules"] = add_rules
        if remove_rule_ids is not UNSET:
            field_dict["removeRuleIds"] = remove_rule_ids
        if update_rule_flags is not UNSET:
            field_dict["updateRuleFlags"] = update_rule_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        from ..models.recent_layoffs import RecentLayoffs
        from ..models.recently_hired_with_title import RecentlyHiredWithTitle
        from ..models.technology_added import TechnologyAdded
        from ..models.update_tracker_company_list_body_update_rule_flags_type_0_item import (
            UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_refresh_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        refresh_interval_days = _parse_refresh_interval_days(d.pop("refreshIntervalDays", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

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

        def _parse_add_rules(
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
                add_rules_type_0 = []
                _add_rules_type_0 = data
                for add_rules_type_0_item_data in _add_rules_type_0:

                    def _parse_add_rules_type_0_item(
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
                            add_rules_type_0_item_type_0 = HeadcountCrossedThreshold.from_dict(data)

                            return add_rules_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_1 = HeadcountGrowthPercent.from_dict(data)

                            return add_rules_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_2 = NewFundingRound.from_dict(data)

                            return add_rules_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_3 = FundingStageChanged.from_dict(data)

                            return add_rules_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_4 = JobPostingWithKeyword.from_dict(data)

                            return add_rules_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_5 = JobPostingInFunction.from_dict(data)

                            return add_rules_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_6 = NewsWithKeyword.from_dict(data)

                            return add_rules_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_7 = CompanyNews.from_dict(data)

                            return add_rules_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_8 = HQLocationChanged.from_dict(data)

                            return add_rules_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_9 = CompanyStatusChanged.from_dict(data)

                            return add_rules_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_10 = TechnologyAdded.from_dict(data)

                            return add_rules_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_11 = CompanyPosted.from_dict(data)

                            return add_rules_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_12 = CompanyPostedWithKeyword.from_dict(data)

                            return add_rules_type_0_item_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_13 = FollowerCountGrowth.from_dict(data)

                            return add_rules_type_0_item_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_14 = CompanyNameChanged.from_dict(data)

                            return add_rules_type_0_item_type_14
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_15 = CompanyDescriptionChanged.from_dict(data)

                            return add_rules_type_0_item_type_15
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_16 = CompanyWentInactive.from_dict(data)

                            return add_rules_type_0_item_type_16
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_17 = EmployeeCountMilestone.from_dict(data)

                            return add_rules_type_0_item_type_17
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_18 = NewOfficeLocation.from_dict(data)

                            return add_rules_type_0_item_type_18
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_19 = CompanyLogoChanged.from_dict(data)

                            return add_rules_type_0_item_type_19
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_20 = AcquiredCompany.from_dict(data)

                            return add_rules_type_0_item_type_20
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_21 = NewInvestor.from_dict(data)

                            return add_rules_type_0_item_type_21
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_22 = RecentlyHiredWithTitle.from_dict(data)

                            return add_rules_type_0_item_type_22
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_23 = DepartmentSizeThreshold.from_dict(data)

                            return add_rules_type_0_item_type_23
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        add_rules_type_0_item_type_24 = RecentLayoffs.from_dict(data)

                        return add_rules_type_0_item_type_24

                    add_rules_type_0_item = _parse_add_rules_type_0_item(add_rules_type_0_item_data)

                    add_rules_type_0.append(add_rules_type_0_item)

                return add_rules_type_0
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

        add_rules = _parse_add_rules(d.pop("addRules", UNSET))

        def _parse_remove_rule_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                remove_rule_ids_type_0 = cast(list[str], data)

                return remove_rule_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        remove_rule_ids = _parse_remove_rule_ids(d.pop("removeRuleIds", UNSET))

        def _parse_update_rule_flags(
            data: object,
        ) -> list[UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                update_rule_flags_type_0 = []
                _update_rule_flags_type_0 = data
                for update_rule_flags_type_0_item_data in _update_rule_flags_type_0:
                    update_rule_flags_type_0_item = UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item.from_dict(
                        update_rule_flags_type_0_item_data
                    )

                    update_rule_flags_type_0.append(update_rule_flags_type_0_item)

                return update_rule_flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item] | None | Unset, data)

        update_rule_flags = _parse_update_rule_flags(d.pop("updateRuleFlags", UNSET))

        update_tracker_company_list_body = cls(
            api_key=api_key,
            name=name,
            refresh_interval_days=refresh_interval_days,
            is_active=is_active,
            tracking_rules=tracking_rules,
            add_rules=add_rules,
            remove_rule_ids=remove_rule_ids,
            update_rule_flags=update_rule_flags,
        )

        update_tracker_company_list_body.additional_properties = d
        return update_tracker_company_list_body

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
