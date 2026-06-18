from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fire_tracker_dummy_response_200_output_signals_item_change_data_item import (
        FireTrackerDummyResponse200OutputSignalsItemChangeDataItem,
    )


T = TypeVar("T", bound="FireTrackerDummyResponse200OutputSignalsItem")


@_attrs_define
class FireTrackerDummyResponse200OutputSignalsItem:
    """
    Attributes:
        id (str): Unique identifier for the generated signal.
        rule_id (str): ID of the dummy rule that produced this signal.
        rule_type (str): Rule type slug (e.g. person_connections_milestone).
        summary (str): Human-readable description of what changed.
        change_data (list[FireTrackerDummyResponse200OutputSignalsItemChangeDataItem]): Structured payload describing
            what changed.
        is_dummy (bool):
        webhook_dispatched (bool): Whether a webhook was dispatched for this signal.
        entity_id (None | str | Unset): Tracked entity ID the signal is attached to. Null if the list has no entities.
    """

    id: str
    rule_id: str
    rule_type: str
    summary: str
    change_data: list[FireTrackerDummyResponse200OutputSignalsItemChangeDataItem]
    is_dummy: bool
    webhook_dispatched: bool
    entity_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rule_id = self.rule_id

        rule_type = self.rule_type

        summary = self.summary

        change_data = []
        for change_data_item_data in self.change_data:
            change_data_item = change_data_item_data.to_dict()
            change_data.append(change_data_item)

        is_dummy = self.is_dummy

        webhook_dispatched = self.webhook_dispatched

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ruleId": rule_id,
                "ruleType": rule_type,
                "summary": summary,
                "changeData": change_data,
                "isDummy": is_dummy,
                "webhookDispatched": webhook_dispatched,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fire_tracker_dummy_response_200_output_signals_item_change_data_item import (
            FireTrackerDummyResponse200OutputSignalsItemChangeDataItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        rule_id = d.pop("ruleId")

        rule_type = d.pop("ruleType")

        summary = d.pop("summary")

        change_data = []
        _change_data = d.pop("changeData")
        for change_data_item_data in _change_data:
            change_data_item = FireTrackerDummyResponse200OutputSignalsItemChangeDataItem.from_dict(
                change_data_item_data
            )

            change_data.append(change_data_item)

        is_dummy = d.pop("isDummy")

        webhook_dispatched = d.pop("webhookDispatched")

        def _parse_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        fire_tracker_dummy_response_200_output_signals_item = cls(
            id=id,
            rule_id=rule_id,
            rule_type=rule_type,
            summary=summary,
            change_data=change_data,
            is_dummy=is_dummy,
            webhook_dispatched=webhook_dispatched,
            entity_id=entity_id,
        )

        fire_tracker_dummy_response_200_output_signals_item.additional_properties = d
        return fire_tracker_dummy_response_200_output_signals_item

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
