from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_webhook_event_types_response_200_output_event_types_item_example_payload import (
        ListWebhookEventTypesResponse200OutputEventTypesItemExamplePayload,
    )


T = TypeVar("T", bound="ListWebhookEventTypesResponse200OutputEventTypesItem")


@_attrs_define
class ListWebhookEventTypesResponse200OutputEventTypesItem:
    """
    Attributes:
        event_type (str): The event type identifier you subscribe to.
        description (str): What this event represents and when it fires.
        group (str): The category this event belongs to.
        example_payload (ListWebhookEventTypesResponse200OutputEventTypesItemExamplePayload): An example payload
            delivered for this event type.
    """

    event_type: str
    description: str
    group: str
    example_payload: ListWebhookEventTypesResponse200OutputEventTypesItemExamplePayload
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        description = self.description

        group = self.group

        example_payload = self.example_payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "description": description,
                "group": group,
                "examplePayload": example_payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_webhook_event_types_response_200_output_event_types_item_example_payload import (
            ListWebhookEventTypesResponse200OutputEventTypesItemExamplePayload,
        )

        d = dict(src_dict)
        event_type = d.pop("eventType")

        description = d.pop("description")

        group = d.pop("group")

        example_payload = ListWebhookEventTypesResponse200OutputEventTypesItemExamplePayload.from_dict(
            d.pop("examplePayload")
        )

        list_webhook_event_types_response_200_output_event_types_item = cls(
            event_type=event_type,
            description=description,
            group=group,
            example_payload=example_payload,
        )

        list_webhook_event_types_response_200_output_event_types_item.additional_properties = d
        return list_webhook_event_types_response_200_output_event_types_item

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
