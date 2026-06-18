from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_signal_delivery_status import TrackerSignalDeliveryStatus
from ..models.tracker_signal_entity_type import TrackerSignalEntityType

if TYPE_CHECKING:
    from ..models.acquisition_change import AcquisitionChange
    from ..models.certification_change import CertificationChange
    from ..models.company_location_change import CompanyLocationChange
    from ..models.department_size_change import DepartmentSizeChange
    from ..models.funding_round_change import FundingRoundChange
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


T = TypeVar("T", bound="TrackerSignal")


@_attrs_define
class TrackerSignal:
    """
    Attributes:
        id (str): Signal ID.
        entity_id (str): Tracked entity ID.
        entity_type (TrackerSignalEntityType): Entity type.
        linkedin_identifier (str): LinkedIn org ID or user ID.
        type_ (str): Signal type (e.g. headcount_crossed_threshold).
        summary (None | str): Human-readable description of what changed.
        change_data (list[AcquisitionChange | CertificationChange | CompanyLocationChange | DepartmentSizeChange |
            FundingRoundChange | InvestorChange | JobPostingChange | LayoffEventChange | LinkedInPostChange |
            LocationDeltaChange | NamedItemChange | NewsArticleChange | NumericDeltaChange | PersonCommentChange |
            PersonExperienceChange | PersonReactionChange | ScalarDeltaChange | TenureChange | TrackedEmployeeChange]):
            Array of objects describing what changed. Shape depends on signal type.
        observed_at (datetime.datetime): When the signal was detected.
        delivery_status (TrackerSignalDeliveryStatus): Webhook delivery status.
        delivered_at (datetime.datetime | None): When the webhook was successfully delivered. Null when status is
            PENDING, FAILED, or SKIPPED.
        centi_credits_charged (int): Credits charged for the tracker check that produced this signal, in centi-credits
            (100 = 1 credit).
        is_dummy (bool): When true, this signal was generated synthetically via the `fire-dummy` endpoint.
    """

    id: str
    entity_id: str
    entity_type: TrackerSignalEntityType
    linkedin_identifier: str
    type_: str
    summary: None | str
    change_data: list[
        AcquisitionChange
        | CertificationChange
        | CompanyLocationChange
        | DepartmentSizeChange
        | FundingRoundChange
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
    observed_at: datetime.datetime
    delivery_status: TrackerSignalDeliveryStatus
    delivered_at: datetime.datetime | None
    centi_credits_charged: int
    is_dummy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.acquisition_change import AcquisitionChange
        from ..models.certification_change import CertificationChange
        from ..models.company_location_change import CompanyLocationChange
        from ..models.department_size_change import DepartmentSizeChange
        from ..models.funding_round_change import FundingRoundChange
        from ..models.investor_change import InvestorChange
        from ..models.job_posting_change import JobPostingChange
        from ..models.layoff_event_change import LayoffEventChange
        from ..models.linked_in_post_change import LinkedInPostChange
        from ..models.location_delta_change import LocationDeltaChange
        from ..models.named_item_change import NamedItemChange
        from ..models.news_article_change import NewsArticleChange
        from ..models.numeric_delta_change import NumericDeltaChange
        from ..models.person_experience_change import PersonExperienceChange
        from ..models.person_reaction_change import PersonReactionChange
        from ..models.scalar_delta_change import ScalarDeltaChange
        from ..models.tenure_change import TenureChange
        from ..models.tracked_employee_change import TrackedEmployeeChange

        id = self.id

        entity_id = self.entity_id

        entity_type = self.entity_type.value

        linkedin_identifier = self.linkedin_identifier

        type_ = self.type_

        summary: None | str
        summary = self.summary

        change_data = []
        for change_data_item_data in self.change_data:
            change_data_item: dict[str, Any]
            if isinstance(change_data_item_data, NumericDeltaChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, ScalarDeltaChange):
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
            elif isinstance(change_data_item_data, NamedItemChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, AcquisitionChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, InvestorChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, CertificationChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, TrackedEmployeeChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, DepartmentSizeChange):
                change_data_item = change_data_item_data.to_dict()
            elif isinstance(change_data_item_data, PersonReactionChange):
                change_data_item = change_data_item_data.to_dict()
            else:
                change_data_item = change_data_item_data.to_dict()

            change_data.append(change_data_item)

        observed_at = self.observed_at.isoformat()

        delivery_status = self.delivery_status.value

        delivered_at: None | str
        if isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

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
                "type": type_,
                "summary": summary,
                "changeData": change_data,
                "observedAt": observed_at,
                "deliveryStatus": delivery_status,
                "deliveredAt": delivered_at,
                "centiCreditsCharged": centi_credits_charged,
                "isDummy": is_dummy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acquisition_change import AcquisitionChange
        from ..models.certification_change import CertificationChange
        from ..models.company_location_change import CompanyLocationChange
        from ..models.department_size_change import DepartmentSizeChange
        from ..models.funding_round_change import FundingRoundChange
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

        d = dict(src_dict)
        id = d.pop("id")

        entity_id = d.pop("entityId")

        entity_type = TrackerSignalEntityType(d.pop("entityType"))

        linkedin_identifier = d.pop("linkedinIdentifier")

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
                | DepartmentSizeChange
                | FundingRoundChange
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
                    change_data_item_type_0 = NumericDeltaChange.from_dict(data)

                    return change_data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_1 = ScalarDeltaChange.from_dict(data)

                    return change_data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_2 = LocationDeltaChange.from_dict(data)

                    return change_data_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_3 = CompanyLocationChange.from_dict(data)

                    return change_data_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_4 = FundingRoundChange.from_dict(data)

                    return change_data_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_5 = JobPostingChange.from_dict(data)

                    return change_data_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_6 = NewsArticleChange.from_dict(data)

                    return change_data_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_7 = LinkedInPostChange.from_dict(data)

                    return change_data_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_8 = PersonExperienceChange.from_dict(data)

                    return change_data_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_11 = TenureChange.from_dict(data)

                    return change_data_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_14 = LayoffEventChange.from_dict(data)

                    return change_data_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_15 = NamedItemChange.from_dict(data)

                    return change_data_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_16 = AcquisitionChange.from_dict(data)

                    return change_data_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_17 = InvestorChange.from_dict(data)

                    return change_data_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_18 = CertificationChange.from_dict(data)

                    return change_data_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_19 = TrackedEmployeeChange.from_dict(data)

                    return change_data_item_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_20 = DepartmentSizeChange.from_dict(data)

                    return change_data_item_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    change_data_item_type_21 = PersonReactionChange.from_dict(data)

                    return change_data_item_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                change_data_item_type_22 = PersonCommentChange.from_dict(data)

                return change_data_item_type_22

            change_data_item = _parse_change_data_item(change_data_item_data)

            change_data.append(change_data_item)

        observed_at = datetime.datetime.fromisoformat(d.pop("observedAt"))

        delivery_status = TrackerSignalDeliveryStatus(d.pop("deliveryStatus"))

        def _parse_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        delivered_at = _parse_delivered_at(d.pop("deliveredAt"))

        centi_credits_charged = d.pop("centiCreditsCharged")

        is_dummy = d.pop("isDummy")

        tracker_signal = cls(
            id=id,
            entity_id=entity_id,
            entity_type=entity_type,
            linkedin_identifier=linkedin_identifier,
            type_=type_,
            summary=summary,
            change_data=change_data,
            observed_at=observed_at,
            delivery_status=delivery_status,
            delivered_at=delivered_at,
            centi_credits_charged=centi_credits_charged,
            is_dummy=is_dummy,
        )

        tracker_signal.additional_properties = d
        return tracker_signal

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
