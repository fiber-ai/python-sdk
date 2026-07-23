from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookEndpointResponse200Output")


@_attrs_define
class CreateWebhookEndpointResponse200Output:
    """
    Attributes:
        endpoint_id (str): The unique ID of this webhook endpoint.
        url (str): The HTTPS URL that receives event payloads.
        event_types (list[str]): The event types this endpoint is subscribed to. An empty array means the endpoint
            receives every event type; endpoints created through this API are always subscribed to one or more specific
            event types.
        disabled (bool): Whether delivery to this endpoint is currently paused.
        created_at (str): When the endpoint was created (ISO 8601).
        updated_at (str): When the endpoint was last updated (ISO 8601).
        signing_secret (str): The secret used to verify payload signatures. Store it securely — it is only returned when
            the endpoint is created or its secret is rotated.
        description (None | str | Unset): An optional human-readable label for this endpoint.
    """

    endpoint_id: str
    url: str
    event_types: list[str]
    disabled: bool
    created_at: str
    updated_at: str
    signing_secret: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = self.endpoint_id

        url = self.url

        event_types = self.event_types

        disabled = self.disabled

        created_at = self.created_at

        updated_at = self.updated_at

        signing_secret = self.signing_secret

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointId": endpoint_id,
                "url": url,
                "eventTypes": event_types,
                "disabled": disabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "signingSecret": signing_secret,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = d.pop("endpointId")

        url = d.pop("url")

        event_types = cast(list[str], d.pop("eventTypes"))

        disabled = d.pop("disabled")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        signing_secret = d.pop("signingSecret")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        create_webhook_endpoint_response_200_output = cls(
            endpoint_id=endpoint_id,
            url=url,
            event_types=event_types,
            disabled=disabled,
            created_at=created_at,
            updated_at=updated_at,
            signing_secret=signing_secret,
            description=description,
        )

        create_webhook_endpoint_response_200_output.additional_properties = d
        return create_webhook_endpoint_response_200_output

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
