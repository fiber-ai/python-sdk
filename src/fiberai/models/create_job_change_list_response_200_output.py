from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_job_change_list_response_200_output_status import CreateJobChangeListResponse200OutputStatus

T = TypeVar("T", bound="CreateJobChangeListResponse200Output")


@_attrs_define
class CreateJobChangeListResponse200Output:
    """
    Attributes:
        id (str): The ID of the job change list.
        name (str): The name of the job change list.
        status (CreateJobChangeListResponse200OutputStatus): Status of the Journeyman list. 'NORMAL' = list has profiles
            and is ready to use. 'DRAFT' = list is empty, no profiles added yet. 'BUILDING' = profiles are currently being
            added to the list. 'ERROR' = list is broken and unusable; contact support.
        is_active (bool): Is the list is active or not. By default, the list is in-active.
    """

    id: str
    name: str
    status: CreateJobChangeListResponse200OutputStatus
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
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

        status = CreateJobChangeListResponse200OutputStatus(d.pop("status"))

        is_active = d.pop("isActive")

        create_job_change_list_response_200_output = cls(
            id=id,
            name=name,
            status=status,
            is_active=is_active,
        )

        create_job_change_list_response_200_output.additional_properties = d
        return create_job_change_list_response_200_output

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
