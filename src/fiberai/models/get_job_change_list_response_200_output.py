from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_job_change_list_response_200_output_status import GetJobChangeListResponse200OutputStatus

T = TypeVar("T", bound="GetJobChangeListResponse200Output")


@_attrs_define
class GetJobChangeListResponse200Output:
    """
    Attributes:
        id (str): The ID of the job change list.
        name (str): The name of the job change list.
        created_at (str): When the list was created.
        status (GetJobChangeListResponse200OutputStatus): Status of the job changes list. 'NORMAL' = list has profiles
            and is ready to use. 'DRAFT' = list is empty, no profiles added yet. 'BUILDING' = profiles are currently being
            added to the list. 'ERROR' = an error occurred while processing the list; contact support.
        is_active (bool): Whether the list is currently active.
    """

    id: str
    name: str
    created_at: str
    status: GetJobChangeListResponse200OutputStatus
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at

        status = self.status.value

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "createdAt": created_at,
                "status": status,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("createdAt")

        status = GetJobChangeListResponse200OutputStatus(d.pop("status"))

        is_active = d.pop("isActive")

        get_job_change_list_response_200_output = cls(
            id=id,
            name=name,
            created_at=created_at,
            status=status,
            is_active=is_active,
        )

        get_job_change_list_response_200_output.additional_properties = d
        return get_job_change_list_response_200_output

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
