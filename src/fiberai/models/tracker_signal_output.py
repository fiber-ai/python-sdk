from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_signal_output_entity_type import TrackerSignalOutputEntityType

if TYPE_CHECKING:
    from ..models.acquisition_change import AcquisitionChange
    from ..models.certification_change import CertificationChange
    from ..models.company_location_change import CompanyLocationChange
    from ..models.departed_from_list_change import DepartedFromListChange
    from ..models.department_size_change import DepartmentSizeChange
    from ..models.funding_round_change import FundingRoundChange
    from ..models.funding_stage_change import FundingStageChange
    from ..models.investor_change import InvestorChange
    from ..models.job_posting_change import JobPostingChange
    from ..models.layoff_event_change import LayoffEventChange
    from ..models.linked_in_post_change import LinkedInPostChange
    from ..models.location_delta_change import LocationDeltaChange
    from ..models.named_item_change import NamedItemChange
    from ..models.news_article_change import NewsArticleChange
    from ..models.numeric_delta_change import NumericDeltaChange
    from ..models.person_comment_change import PersonCommentChange
    from ..models.person_experience_change import PersonExperienceChange
    from ..models.person_reaction_change import PersonReactionChange
    from ..models.scalar_delta_change import ScalarDeltaChange
    from ..models.tenure_change import TenureChange
    from ..models.tracked_employee_change import TrackedEmployeeChange


T = TypeVar("T", bound="TrackerSignalOutput")


@_attrs_define
class TrackerSignalOutput:
    """
    Attributes:
        id (str): Signal ID.
        entity_id (str): Tracked entity ID.
        entity_type (TrackerSignalOutputEntityType): Entity type.
        linkedin_identifier (str): LinkedIn org ID or user ID.
        linkedin_slug (None | str): The identifying part of a person or company's LinkedIn URL, such as `williamhgates`
            for `https://www.linkedin.com/in/williamhgates/` or `google` for `https://www.linkedin.com/company/google`.
        linkedin_url (None | str): Full LinkedIn URL for the tracked entity, like
            `https://www.linkedin.com/company/google` for companies or `https://www.linkedin.com/in/williamhgates` for
            people.
        type_ (str): Signal type (e.g. headcount_crossed_threshold).
        summary (None | str): Human-readable description of what changed.
        change_data (list[AcquisitionChange | CertificationChange | CompanyLocationChange | DepartedFromListChange |
            DepartmentSizeChange | FundingRoundChange | FundingStageChange | InvestorChange | JobPostingChange |
            LayoffEventChange | LinkedInPostChange | LocationDeltaChange | NamedItemChange | NewsArticleChange |
            NumericDeltaChange | PersonCommentChange | PersonExperienceChange | PersonReactionChange | ScalarDeltaChange |
            TenureChange | TrackedEmployeeChange]): Array of objects describing what changed. Shape depends on signal type.
        sources (list[str]): URLs providing proof or more information about this signal.
        methodology (str): Explanation of how this signal was detected and verified.
        observed_at (datetime.datetime): When the signal was detected.
        centi_credits_charged (int): Credits charged for the tracker check that produced this signal, in centi-credits
            (100 = 1 credit).
        is_dummy (bool): When true, this signal was generated synthetically via the `fire-dummy` endpoint.
    """

    id: str
    entity_id: str
    entity_type: TrackerSignalOutputEntityType
    linkedin_identifier: str
    linkedin_slug: None | str
    linkedin_url: None | str
    type_: str
    summary: None | str
    change_data: list[
        AcquisitionChange
        | CertificationChange
        | CompanyLocationChange
        | DepartedFromListChange
        | DepartmentSizeChange
        | FundingRoundChange
        | FundingStageChange
        | InvestorChange
        | JobPostingChange
        | LayoffEventChange
        | LinkedInPostChange
        | LocationDeltaChange
        | NamedItemChange
        | NewsArticleChange
        | NumericDeltaChange
        | PersonCommentChange
        | PersonExperienceChange
        | PersonReactionChange
        | ScalarDeltaChange
        | TenureChange
        | TrackedEmployeeChange
    ]
    sources: list[str]
    methodology: str
    observed_at: datetime.datetime
    centi_credits_charged: int
    is_dummy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.acquisition_change import AcquisitionChange  # noqa: PLC0415
        from ..models.certification_change import CertificationChange  # noqa: PLC0415
        from ..models.company_location_change import CompanyLocationChange  # noqa: PLC0415
        from ..models.departed_from_list_change import DepartedFromListChange  # noqa: PLC0415
        from ..models.department_size_change import DepartmentSizeChange  # noqa: PLC0415
        from ..models.funding_round_change import FundingRoundChange  # noqa: PLC0415
        from ..models.funding_stage_change import FundingStageChange  # noqa: PLC0415
        from ..models.investor_change import InvestorChange  # noqa: PLC0415
        from ..models.job_posting_change import JobPostingChange  # noqa: PLC0415
        from ..models.layoff_event_change import LayoffEventChange  # noqa: PLC0415
        from ..models.linked_in_post_change import LinkedInPostChange  # noqa: PLC0415
        from ..models.location_delta_change import LocationDeltaChange  # noqa: PLC0415
        from ..models.news_article_change import NewsArticleChange  # noqa: PLC0415
        from ..models.numeric_delta_change import NumericDeltaChange  # noqa: PLC0415
        from ..models.person_comment_change import PersonCommentChange  # noqa: PLC0415
        from ..models.person_experience_change import PersonExperienceChange  # noqa: PLC0415
        from ..models.person_reaction_change import PersonReactionChange  # noqa: PLC0415
        from ..models.scalar_delta_change import ScalarDeltaChange  # noqa: PLC0415
        from ..models.tenure_change import TenureChange  # noqa: PLC0415
        from ..models.tracked_employee_change import TrackedEmployeeChange  # noqa: PLC0415

        id = self.id

        entity_id = self.entity_id

        entity_type = self.entity_type.value

        linkedin_identifier = self.linkedin_identifier

        linkedin_slug: None | str
        linkedin_slug = self.linkedin_slug

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        type_ = self.type_

        summary: None | str
        summary = self.summary

        change_data = []
        for change_data_item_data in self.change_data:
            change_data_item: dict[str, Any]
            if isinstance(change_data_item_data, FundingStageChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, LocationDeltaChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, CompanyLocationChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, FundingRoundChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, JobPostingChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, NewsArticleChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, LinkedInPostChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, PersonExperienceChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, TenureChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, LayoffEventChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, TrackedEmployeeChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, InvestorChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, AcquisitionChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, CertificationChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, DepartmentSizeChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, PersonReactionChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, PersonCommentChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, DepartedFromListChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, ScalarDeltaChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, NumericDeltaChange):
                change_data_item = change_data_item_data.to_dict()
            else:
                change_data_item = change_data_item_data.to_dict()

            change_data.append(change_data_item)

        sources = self.sources

        methodology = self.methodology

        observed_at = self.observed_at.isoformat()

        centi_credits_charged = self.centi_credits_charged

        is_dummy = self.is_dummy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entityId": entity_id,
                "entityType": entity_type,
                "linkedinIdentifier": linkedin_identifier,
                "linkedinSlug": linkedin_slug,
                "linkedinUrl": linkedin_url,
                "type": type_,
                "summary": summary,
                "changeData": change_data,
                "sources": sources,
                "methodology": methodology,
                "observedAt": observed_at,
                "centiCreditsCharged": centi_credits_charged,
                "isDummy": is_dummy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acquisition_change import AcquisitionChange  # noqa: PLC0415
        from ..models.certification_change import CertificationChange  # noqa: PLC0415
        from ..models.company_location_change import CompanyLocationChange  # noqa: PLC0415
        from ..models.departed_from_list_change import DepartedFromListChange  # noqa: PLC0415
        from ..models.department_size_change import DepartmentSizeChange  # noqa: PLC0415
        from ..models.funding_round_change import FundingRoundChange  # noqa: PLC0415
        from ..models.funding_stage_change import FundingStageChange  # noqa: PLC0415
        from ..models.investor_change import InvestorChange  # noqa: PLC0415
        from ..models.job_posting_change import JobPostingChange  # noqa: PLC0415
        from ..models.layoff_event_change import LayoffEventChange  # noqa: PLC0415
        from ..models.linked_in_post_change import LinkedInPostChange  # noqa: PLC0415
        from ..models.location_delta_change import LocationDeltaChange  # noqa: PLC0415
        from ..models.named_item_change import NamedItemChange  # noqa: PLC0415
        from ..models.news_article_change import NewsArticleChange  # noqa: PLC0415
        from ..models.numeric_delta_change import NumericDeltaChange  # noqa: PLC0415
        from ..models.person_comment_change import PersonCommentChange  # noqa: PLC0415
        from ..models.person_experience_change import PersonExperienceChange  # noqa: PLC0415
        from ..models.person_reaction_change import PersonReactionChange  # noqa: PLC0415
        from ..models.scalar_delta_change import ScalarDeltaChange  # noqa: PLC0415
        from ..models.tenure_change import TenureChange  # noqa: PLC0415
        from ..models.tracked_employee_change import TrackedEmployeeChange  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        entity_id = d.pop("entityId")

        entity_type = TrackerSignalOutputEntityType(d.pop("entityType"))

        linkedin_identifier = d.pop("linkedinIdentifier")

        def _parse_linkedin_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        type_ = d.pop("type")

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        change_data = []
        _change_data = d.pop("changeData")
        for change_data_item_data in _change_data:

            def _parse_change_data_item(
                data: object,
            ) -> (
                AcquisitionChange
                | CertificationChange
                | CompanyLocationChange
                | DepartedFromListChange
                | DepartmentSizeChange
                | FundingRoundChange
                | FundingStageChange
                | InvestorChange
                | JobPostingChange
                | LayoffEventChange
                | LinkedInPostChange
                | LocationDeltaChange
                | NamedItemChange
                | NewsArticleChange
                | NumericDeltaChange
                | PersonCommentChange
                | PersonExperienceChange
                | PersonReactionChange
                | ScalarDeltaChange
                | TenureChange
                | TrackedEmployeeChange
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_0 = FundingStageChange.from_dict(data)

                    return change_data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_1 = LocationDeltaChange.from_dict(data)

                    return change_data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_2 = CompanyLocationChange.from_dict(data)

                    return change_data_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_3 = FundingRoundChange.from_dict(data)

                    return change_data_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_4 = JobPostingChange.from_dict(data)

                    return change_data_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_5 = NewsArticleChange.from_dict(data)

                    return change_data_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_6 = LinkedInPostChange.from_dict(data)

                    return change_data_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_7 = PersonExperienceChange.from_dict(data)

                    return change_data_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_9 = TenureChange.from_dict(data)

                    return change_data_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_11 = LayoffEventChange.from_dict(data)

                    return change_data_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_12 = TrackedEmployeeChange.from_dict(data)

                    return change_data_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_13 = InvestorChange.from_dict(data)

                    return change_data_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_14 = AcquisitionChange.from_dict(data)

                    return change_data_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_15 = CertificationChange.from_dict(data)

                    return change_data_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_16 = DepartmentSizeChange.from_dict(data)

                    return change_data_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_17 = PersonReactionChange.from_dict(data)

                    return change_data_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_18 = PersonCommentChange.from_dict(data)

                    return change_data_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_19 = DepartedFromListChange.from_dict(data)

                    return change_data_item_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_20 = ScalarDeltaChange.from_dict(data)

                    return change_data_item_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_23 = NumericDeltaChange.from_dict(data)

                    return change_data_item_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                change_data_item_type_24 = NamedItemChange.from_dict(data)

                return change_data_item_type_24

            change_data_item = _parse_change_data_item(change_data_item_data)

            change_data.append(change_data_item)

        sources = cast(list[str], d.pop("sources"))

        methodology = d.pop("methodology")

        observed_at = datetime.datetime.fromisoformat(d.pop("observedAt"))

        centi_credits_charged = d.pop("centiCreditsCharged")

        is_dummy = d.pop("isDummy")

        tracker_signal_output = cls(
            id=id,
            entity_id=entity_id,
            entity_type=entity_type,
            linkedin_identifier=linkedin_identifier,
            linkedin_slug=linkedin_slug,
            linkedin_url=linkedin_url,
            type_=type_,
            summary=summary,
            change_data=change_data,
            sources=sources,
            methodology=methodology,
            observed_at=observed_at,
            centi_credits_charged=centi_credits_charged,
            is_dummy=is_dummy,
        )

        tracker_signal_output.additional_properties = d
        return tracker_signal_output

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
