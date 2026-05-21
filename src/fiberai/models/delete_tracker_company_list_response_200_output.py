from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteTrackerCompanyListResponse200Output")


@_attrs_define
class DeleteTrackerCompanyListResponse200Output:
    """
    Attributes:
        id (str): ID of the archived list
        name (str): Name of the archived list
        is_archived (bool): List has been archived
        is_active (bool): Monitoring has been stopped
    """

    id: str
    name: str
    is_archived: bool
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_archived = self.is_archived

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isArchived": is_archived,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_archived = d.pop("isArchived")

        is_active = d.pop("isActive")

        delete_tracker_company_list_response_200_output = cls(
            id=id,
            name=name,
            is_archived=is_archived,
            is_active=is_active,
        )

        delete_tracker_company_list_response_200_output.additional_properties = d
        return delete_tracker_company_list_response_200_output

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
