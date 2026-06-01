from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_signal_delivery_status import TrackerSignalDeliveryStatus
from ..models.tracker_signal_entity_type import TrackerSignalEntityType

if TYPE_CHECKING:
    from ..models.tracker_signal_change_data_item import TrackerSignalChangeDataItem


T = TypeVar("T", bound="TrackerSignal")


@_attrs_define
class TrackerSignal:
    """
    Attributes:
        id (str): Signal ID
        entity_id (str): Tracked entity ID
        entity_type (TrackerSignalEntityType): Entity type
        linkedin_identifier (str): LinkedIn org ID or user ID
        type_ (str): Signal type (e.g. headcount_crossed_threshold)
        summary (None | str): Human-readable description of what changed
        change_data (list[TrackerSignalChangeDataItem]): Array of objects describing what changed. Shape varies by
            signal type.
        observed_at (datetime.datetime): When the signal was detected
        delivery_status (TrackerSignalDeliveryStatus): Webhook delivery status
        delivered_at (datetime.datetime | None): When the webhook was successfully delivered. Null when status is
            PENDING, FAILED, or SKIPPED.
        centi_credits_charged (int): Credits charged for the tracker check that produced this signal, in centi-credits
            (100 = 1 credit).
    """

    id: str
    entity_id: str
    entity_type: TrackerSignalEntityType
    linkedin_identifier: str
    type_: str
    summary: None | str
    change_data: list[TrackerSignalChangeDataItem]
    observed_at: datetime.datetime
    delivery_status: TrackerSignalDeliveryStatus
    delivered_at: datetime.datetime | None
    centi_credits_charged: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        entity_id = self.entity_id

        entity_type = self.entity_type.value

        linkedin_identifier = self.linkedin_identifier

        type_ = self.type_

        summary: None | str
        summary = self.summary

        change_data = []
        for change_data_item_data in self.change_data:
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
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_signal_change_data_item import TrackerSignalChangeDataItem

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
            change_data_item = TrackerSignalChangeDataItem.from_dict(change_data_item_data)

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
