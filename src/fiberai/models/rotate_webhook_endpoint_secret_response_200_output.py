from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RotateWebhookEndpointSecretResponse200Output")


@_attrs_define
class RotateWebhookEndpointSecretResponse200Output:
    """
    Attributes:
        endpoint_id (str): The ID of the webhook endpoint whose secret was rotated.
        signing_secret (str): The new signing secret. Store it securely — it will not be shown again.
    """

    endpoint_id: str
    signing_secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = self.endpoint_id

        signing_secret = self.signing_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointId": endpoint_id,
                "signingSecret": signing_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = d.pop("endpointId")

        signing_secret = d.pop("signingSecret")

        rotate_webhook_endpoint_secret_response_200_output = cls(
            endpoint_id=endpoint_id,
            signing_secret=signing_secret,
        )

        rotate_webhook_endpoint_secret_response_200_output.additional_properties = d
        return rotate_webhook_endpoint_secret_response_200_output

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
