from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_webhook_event_types_response_200_output_event_types_item import (
        ListWebhookEventTypesResponse200OutputEventTypesItem,
    )


T = TypeVar("T", bound="ListWebhookEventTypesResponse200Output")


@_attrs_define
class ListWebhookEventTypesResponse200Output:
    """
    Attributes:
        event_types (list[ListWebhookEventTypesResponse200OutputEventTypesItem]): All event types you can subscribe a
            webhook endpoint to.
    """

    event_types: list[ListWebhookEventTypesResponse200OutputEventTypesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.to_dict()
            event_types.append(event_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventTypes": event_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_webhook_event_types_response_200_output_event_types_item import (
            ListWebhookEventTypesResponse200OutputEventTypesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        event_types = []
        _event_types = d.pop("eventTypes")
        for event_types_item_data in _event_types:
            event_types_item = ListWebhookEventTypesResponse200OutputEventTypesItem.from_dict(event_types_item_data)

            event_types.append(event_types_item)

        list_webhook_event_types_response_200_output = cls(
            event_types=event_types,
        )

        list_webhook_event_types_response_200_output.additional_properties = d
        return list_webhook_event_types_response_200_output

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
