from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendTestWebhookEventResponse200Output")


@_attrs_define
class SendTestWebhookEventResponse200Output:
    """
    Attributes:
        endpoint_id (str): The ID of the endpoint the test event was sent to.
        event_type (str): The event type of the test event.
        message_id (str): The ID of the test message, useful for tracing the delivery.
    """

    endpoint_id: str
    event_type: str
    message_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = self.endpoint_id

        event_type = self.event_type

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointId": endpoint_id,
                "eventType": event_type,
                "messageId": message_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = d.pop("endpointId")

        event_type = d.pop("eventType")

        message_id = d.pop("messageId")

        send_test_webhook_event_response_200_output = cls(
            endpoint_id=endpoint_id,
            event_type=event_type,
            message_id=message_id,
        )

        send_test_webhook_event_response_200_output.additional_properties = d
        return send_test_webhook_event_response_200_output

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
