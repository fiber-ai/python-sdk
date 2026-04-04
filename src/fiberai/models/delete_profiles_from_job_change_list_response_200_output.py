from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteProfilesFromJobChangeListResponse200Output")


@_attrs_define
class DeleteProfilesFromJobChangeListResponse200Output:
    """
    Attributes:
        num_deleted (float): Number of profiles successfully deleted.
    """

    num_deleted: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_deleted = self.num_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numDeleted": num_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_deleted = d.pop("numDeleted")

        delete_profiles_from_job_change_list_response_200_output = cls(
            num_deleted=num_deleted,
        )

        delete_profiles_from_job_change_list_response_200_output.additional_properties = d
        return delete_profiles_from_job_change_list_response_200_output

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
