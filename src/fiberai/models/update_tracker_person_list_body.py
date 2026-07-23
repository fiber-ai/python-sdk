from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
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
    from ..models.update_tracker_person_list_body_initial_signals_type_0 import (
        UpdateTrackerPersonListBodyInitialSignalsType0,
    )
    from ..models.update_tracker_person_list_body_update_rule_flags_type_0_item import (
        UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item,
    )


T = TypeVar("T", bound="UpdateTrackerPersonListBody")


@_attrs_define
class UpdateTrackerPersonListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (None | str | Unset): New name for the list.
        refresh_interval_days (int | None | Unset): New check interval in days.
        is_active (bool | None | Unset): Pause or resume monitoring on the list.
        tracking_rules (list[PersonBecameInfluencer | PersonBecamePremium | PersonBecameTopVoice | PersonBecameVerified
            | PersonChangedCompany | PersonCommentedOnPost | PersonConnectionsMilestone | PersonEmploymentTypeChanged |
            PersonFollowerMilestone | PersonGotDemoted | PersonGotPromoted | PersonHeadlineChanged | PersonIsHiring |
            PersonLocationChanged | PersonNewCertification | PersonOpenToWork | PersonPosted | PersonPostedWithKeyword |
            PersonReactedToPost | PersonSkillsAdded | PersonStartedCompany | PersonStealthChanged | PersonStuckInRole |
            PersonSummaryChanged | PersonTagGained | PersonTenureMilestone | PersonTitleChanged] | None | Unset): Replace
            ALL existing rules with this set. Pass empty array to clear all rules. Omit to leave unchanged. Cannot be used
            with `addRules`/`removeRuleIds`.
        add_rules (list[PersonBecameInfluencer | PersonBecamePremium | PersonBecameTopVoice | PersonBecameVerified |
            PersonChangedCompany | PersonCommentedOnPost | PersonConnectionsMilestone | PersonEmploymentTypeChanged |
            PersonFollowerMilestone | PersonGotDemoted | PersonGotPromoted | PersonHeadlineChanged | PersonIsHiring |
            PersonLocationChanged | PersonNewCertification | PersonOpenToWork | PersonPosted | PersonPostedWithKeyword |
            PersonReactedToPost | PersonSkillsAdded | PersonStartedCompany | PersonStealthChanged | PersonStuckInRole |
            PersonSummaryChanged | PersonTagGained | PersonTenureMilestone | PersonTitleChanged] | None | Unset): Add rules
            to the existing set without removing others. The total active rules on the list (existing + added) must not
            exceed the per-list cap. Cannot be used with `trackingRules`.
        remove_rule_ids (list[str] | None | Unset): Rule IDs to remove. Cannot be used with `trackingRules`.
        update_rule_flags (list[UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item] | None | Unset): Toggle `isDummy`
            on existing rules by ID. Use this to convert a real rule into a dummy rule (or vice versa) without recreating
            it.
        initial_signals (None | Unset | UpdateTrackerPersonListBodyInitialSignalsType0): When provided, generates
            signals immediately for recent events (funding rounds, news, job postings, social posts) without waiting for the
            first tracking cycle. Only certain rule types support initial signals.
    """

    api_key: str
    name: None | str | Unset = UNSET
    refresh_interval_days: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    tracking_rules: (
        list[
            PersonBecameInfluencer
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
        ]
        | None
        | Unset
    ) = UNSET
    add_rules: (
        list[
            PersonBecameInfluencer
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
        ]
        | None
        | Unset
    ) = UNSET
    remove_rule_ids: list[str] | None | Unset = UNSET
    update_rule_flags: list[UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item] | None | Unset = UNSET
    initial_signals: None | Unset | UpdateTrackerPersonListBodyInitialSignalsType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.person_title_changed import PersonTitleChanged
        from ..models.update_tracker_person_list_body_initial_signals_type_0 import (
            UpdateTrackerPersonListBodyInitialSignalsType0,
        )

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
                if isinstance(tracking_rules_type_0_item_data, PersonChangedCompany):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonTitleChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonStealthChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonOpenToWork):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonIsHiring):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonHeadlineChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonLocationChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonTagGained):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonPosted):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonPostedWithKeyword):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonReactedToPost):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonCommentedOnPost):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonSkillsAdded):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonGotPromoted):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonStartedCompany):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonEmploymentTypeChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonConnectionsMilestone):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonFollowerMilestone):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonSummaryChanged):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonNewCertification):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonBecameVerified):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonBecamePremium):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonBecameInfluencer):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonBecameTopVoice):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonGotDemoted):
                    tracking_rules_type_0_item = tracking_rules_type_0_item_data.to_dict()
                elif isinstance(tracking_rules_type_0_item_data, PersonStuckInRole):
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
                if isinstance(add_rules_type_0_item_data, PersonChangedCompany):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonTitleChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonStealthChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonOpenToWork):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonIsHiring):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonHeadlineChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonLocationChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonTagGained):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonPosted):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonPostedWithKeyword):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonReactedToPost):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonCommentedOnPost):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonSkillsAdded):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonGotPromoted):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonStartedCompany):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonEmploymentTypeChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonConnectionsMilestone):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonFollowerMilestone):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonSummaryChanged):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonNewCertification):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonBecameVerified):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonBecamePremium):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonBecameInfluencer):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonBecameTopVoice):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonGotDemoted):
                    add_rules_type_0_item = add_rules_type_0_item_data.to_dict()
                elif isinstance(add_rules_type_0_item_data, PersonStuckInRole):
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

        initial_signals: dict[str, Any] | None | Unset
        if isinstance(self.initial_signals, Unset):
            initial_signals = UNSET
        elif isinstance(self.initial_signals, UpdateTrackerPersonListBodyInitialSignalsType0):
            initial_signals = self.initial_signals.to_dict()
        else:
            initial_signals = self.initial_signals

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
        if initial_signals is not UNSET:
            field_dict["initialSignals"] = initial_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        from ..models.update_tracker_person_list_body_initial_signals_type_0 import (
            UpdateTrackerPersonListBodyInitialSignalsType0,
        )
        from ..models.update_tracker_person_list_body_update_rule_flags_type_0_item import (
            UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item,
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
                PersonBecameInfluencer
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
                        PersonBecameInfluencer
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
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_0 = PersonChangedCompany.from_dict(data)

                            return tracking_rules_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_1 = PersonTitleChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_2 = PersonStealthChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_3 = PersonOpenToWork.from_dict(data)

                            return tracking_rules_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_4 = PersonIsHiring.from_dict(data)

                            return tracking_rules_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_5 = PersonHeadlineChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_6 = PersonLocationChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_7 = PersonTagGained.from_dict(data)

                            return tracking_rules_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_8 = PersonPosted.from_dict(data)

                            return tracking_rules_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_9 = PersonPostedWithKeyword.from_dict(data)

                            return tracking_rules_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_10 = PersonReactedToPost.from_dict(data)

                            return tracking_rules_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_11 = PersonCommentedOnPost.from_dict(data)

                            return tracking_rules_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_12 = PersonSkillsAdded.from_dict(data)

                            return tracking_rules_type_0_item_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_13 = PersonGotPromoted.from_dict(data)

                            return tracking_rules_type_0_item_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_14 = PersonStartedCompany.from_dict(data)

                            return tracking_rules_type_0_item_type_14
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_15 = PersonEmploymentTypeChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_15
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_16 = PersonConnectionsMilestone.from_dict(data)

                            return tracking_rules_type_0_item_type_16
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_17 = PersonFollowerMilestone.from_dict(data)

                            return tracking_rules_type_0_item_type_17
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_18 = PersonSummaryChanged.from_dict(data)

                            return tracking_rules_type_0_item_type_18
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_19 = PersonNewCertification.from_dict(data)

                            return tracking_rules_type_0_item_type_19
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_20 = PersonBecameVerified.from_dict(data)

                            return tracking_rules_type_0_item_type_20
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_21 = PersonBecamePremium.from_dict(data)

                            return tracking_rules_type_0_item_type_21
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_22 = PersonBecameInfluencer.from_dict(data)

                            return tracking_rules_type_0_item_type_22
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_23 = PersonBecameTopVoice.from_dict(data)

                            return tracking_rules_type_0_item_type_23
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_24 = PersonGotDemoted.from_dict(data)

                            return tracking_rules_type_0_item_type_24
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            tracking_rules_type_0_item_type_25 = PersonStuckInRole.from_dict(data)

                            return tracking_rules_type_0_item_type_25
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        tracking_rules_type_0_item_type_26 = PersonTenureMilestone.from_dict(data)

                        return tracking_rules_type_0_item_type_26

                    tracking_rules_type_0_item = _parse_tracking_rules_type_0_item(tracking_rules_type_0_item_data)

                    tracking_rules_type_0.append(tracking_rules_type_0_item)

                return tracking_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    PersonBecameInfluencer
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
                PersonBecameInfluencer
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
                        PersonBecameInfluencer
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
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_0 = PersonChangedCompany.from_dict(data)

                            return add_rules_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_1 = PersonTitleChanged.from_dict(data)

                            return add_rules_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_2 = PersonStealthChanged.from_dict(data)

                            return add_rules_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_3 = PersonOpenToWork.from_dict(data)

                            return add_rules_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_4 = PersonIsHiring.from_dict(data)

                            return add_rules_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_5 = PersonHeadlineChanged.from_dict(data)

                            return add_rules_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_6 = PersonLocationChanged.from_dict(data)

                            return add_rules_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_7 = PersonTagGained.from_dict(data)

                            return add_rules_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_8 = PersonPosted.from_dict(data)

                            return add_rules_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_9 = PersonPostedWithKeyword.from_dict(data)

                            return add_rules_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_10 = PersonReactedToPost.from_dict(data)

                            return add_rules_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_11 = PersonCommentedOnPost.from_dict(data)

                            return add_rules_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_12 = PersonSkillsAdded.from_dict(data)

                            return add_rules_type_0_item_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_13 = PersonGotPromoted.from_dict(data)

                            return add_rules_type_0_item_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_14 = PersonStartedCompany.from_dict(data)

                            return add_rules_type_0_item_type_14
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_15 = PersonEmploymentTypeChanged.from_dict(data)

                            return add_rules_type_0_item_type_15
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_16 = PersonConnectionsMilestone.from_dict(data)

                            return add_rules_type_0_item_type_16
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_17 = PersonFollowerMilestone.from_dict(data)

                            return add_rules_type_0_item_type_17
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_18 = PersonSummaryChanged.from_dict(data)

                            return add_rules_type_0_item_type_18
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_19 = PersonNewCertification.from_dict(data)

                            return add_rules_type_0_item_type_19
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_20 = PersonBecameVerified.from_dict(data)

                            return add_rules_type_0_item_type_20
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_21 = PersonBecamePremium.from_dict(data)

                            return add_rules_type_0_item_type_21
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_22 = PersonBecameInfluencer.from_dict(data)

                            return add_rules_type_0_item_type_22
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_23 = PersonBecameTopVoice.from_dict(data)

                            return add_rules_type_0_item_type_23
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_24 = PersonGotDemoted.from_dict(data)

                            return add_rules_type_0_item_type_24
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            add_rules_type_0_item_type_25 = PersonStuckInRole.from_dict(data)

                            return add_rules_type_0_item_type_25
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        add_rules_type_0_item_type_26 = PersonTenureMilestone.from_dict(data)

                        return add_rules_type_0_item_type_26

                    add_rules_type_0_item = _parse_add_rules_type_0_item(add_rules_type_0_item_data)

                    add_rules_type_0.append(add_rules_type_0_item)

                return add_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    PersonBecameInfluencer
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
        ) -> list[UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item] | None | Unset:
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
                    update_rule_flags_type_0_item = UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item.from_dict(
                        update_rule_flags_type_0_item_data
                    )

                    update_rule_flags_type_0.append(update_rule_flags_type_0_item)

                return update_rule_flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateTrackerPersonListBodyUpdateRuleFlagsType0Item] | None | Unset, data)

        update_rule_flags = _parse_update_rule_flags(d.pop("updateRuleFlags", UNSET))

        def _parse_initial_signals(data: object) -> None | Unset | UpdateTrackerPersonListBodyInitialSignalsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_signals_type_0 = UpdateTrackerPersonListBodyInitialSignalsType0.from_dict(data)

                return initial_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTrackerPersonListBodyInitialSignalsType0, data)

        initial_signals = _parse_initial_signals(d.pop("initialSignals", UNSET))

        update_tracker_person_list_body = cls(
            api_key=api_key,
            name=name,
            refresh_interval_days=refresh_interval_days,
            is_active=is_active,
            tracking_rules=tracking_rules,
            add_rules=add_rules,
            remove_rule_ids=remove_rule_ids,
            update_rule_flags=update_rule_flags,
            initial_signals=initial_signals,
        )

        update_tracker_person_list_body.additional_properties = d
        return update_tracker_person_list_body

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
