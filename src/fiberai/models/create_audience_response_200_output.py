from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_audience_response_200_output_status import CreateAudienceResponse200OutputStatus

T = TypeVar("T", bound="CreateAudienceResponse200Output")


@_attrs_define
class CreateAudienceResponse200Output:
    """
    Attributes:
        audience_id (str): Unique ID of the created audience
        name (str): Name of the audience
        status (CreateAudienceResponse200OutputStatus): Current status of the audience
        created_at (str): When the audience was created
    """

    audience_id: str
    name: str
    status: CreateAudienceResponse200OutputStatus
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_id = self.audience_id

        name = self.name

        status = self.status.value

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceId": audience_id,
                "name": name,
                "status": status,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        name = d.pop("name")

        status = CreateAudienceResponse200OutputStatus(d.pop("status"))

        created_at = d.pop("createdAt")

        create_audience_response_200_output = cls(
            audience_id=audience_id,
            name=name,
            status=status,
            created_at=created_at,
        )

        create_audience_response_200_output.additional_properties = d
        return create_audience_response_200_output

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
