from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_webhook_endpoint_body_event_types_type_0_item import UpdateWebhookEndpointBodyEventTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookEndpointBody")


@_attrs_define
class UpdateWebhookEndpointBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        url (None | str | Unset): A new HTTPS URL to receive event payloads.
        event_types (list[UpdateWebhookEndpointBodyEventTypesType0Item] | None | Unset): A new set of event types to
            subscribe this endpoint to.
        description (None | str | Unset): A new human-readable label for this endpoint.
        disabled (bool | None | Unset): Set to true to pause delivery, or false to resume it.
    """

    api_key: str
    url: None | str | Unset = UNSET
    event_types: list[UpdateWebhookEndpointBodyEventTypesType0Item] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    disabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = []
            for event_types_type_0_item_data in self.event_types:
                event_types_type_0_item = event_types_type_0_item_data.value
                event_types.append(event_types_type_0_item)

        else:
            event_types = self.event_types

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_event_types(data: object) -> list[UpdateWebhookEndpointBodyEventTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = []
                _event_types_type_0 = data
                for event_types_type_0_item_data in _event_types_type_0:
                    event_types_type_0_item = UpdateWebhookEndpointBodyEventTypesType0Item(event_types_type_0_item_data)

                    event_types_type_0.append(event_types_type_0_item)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateWebhookEndpointBodyEventTypesType0Item] | None | Unset, data)

        event_types = _parse_event_types(d.pop("eventTypes", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        update_webhook_endpoint_body = cls(
            api_key=api_key,
            url=url,
            event_types=event_types,
            description=description,
            disabled=disabled,
        )

        update_webhook_endpoint_body.additional_properties = d
        return update_webhook_endpoint_body

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
