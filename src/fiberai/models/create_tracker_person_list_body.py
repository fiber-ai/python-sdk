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


T = TypeVar("T", bound="CreateTrackerPersonListBody")


@_attrs_define
class CreateTrackerPersonListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (str): Human-readable name for the tracker list.
        refresh_interval_days (int): How often to check tracked people for changes, in days.
        tracking_rules (list[PersonBecameInfluencer | PersonBecamePremium | PersonBecameTopVoice | PersonBecameVerified
            | PersonChangedCompany | PersonCommentedOnPost | PersonConnectionsMilestone | PersonEmploymentTypeChanged |
            PersonFollowerMilestone | PersonGotDemoted | PersonGotPromoted | PersonHeadlineChanged | PersonIsHiring |
            PersonLocationChanged | PersonNewCertification | PersonOpenToWork | PersonPosted | PersonPostedWithKeyword |
            PersonReactedToPost | PersonSkillsAdded | PersonStartedCompany | PersonStealthChanged | PersonStuckInRole |
            PersonSummaryChanged | PersonTagGained | PersonTenureMilestone | PersonTitleChanged] | None | Unset): Tracking
            rules to evaluate against this list's entities. Multiple rules can be active simultaneously.
    """

    api_key: str
    name: str
    refresh_interval_days: int
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

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        name = d.pop("name")

        refresh_interval_days = d.pop("refreshIntervalDays")

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

        create_tracker_person_list_body = cls(
            api_key=api_key,
            name=name,
            refresh_interval_days=refresh_interval_days,
            tracking_rules=tracking_rules,
        )

        create_tracker_person_list_body.additional_properties = d
        return create_tracker_person_list_body

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
