from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_test_webhook_event_body_event_type import SendTestWebhookEventBodyEventType

T = TypeVar("T", bound="SendTestWebhookEventBody")


@_attrs_define
class SendTestWebhookEventBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        event_type (SendTestWebhookEventBodyEventType): The event type to send an example payload for. Retrieve
            available event types from the webhook event types endpoint.
    """

    api_key: str
    event_type: SendTestWebhookEventBodyEventType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        event_type = self.event_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "eventType": event_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        event_type = SendTestWebhookEventBodyEventType(d.pop("eventType"))

        send_test_webhook_event_body = cls(
            api_key=api_key,
            event_type=event_type,
        )

        send_test_webhook_event_body.additional_properties = d
        return send_test_webhook_event_body

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
