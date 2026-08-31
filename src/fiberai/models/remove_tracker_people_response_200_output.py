from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.remove_tracker_people_response_200_output_failed_identifiers_item import (
        RemoveTrackerPeopleResponse200OutputFailedIdentifiersItem,
    )


T = TypeVar("T", bound="RemoveTrackerPeopleResponse200Output")


@_attrs_define
class RemoveTrackerPeopleResponse200Output:
    """
    Attributes:
        removed (int): Number of people successfully deactivated.
        not_found (int): Number of identifiers not found or already inactive.
        failed_identifiers (list[RemoveTrackerPeopleResponse200OutputFailedIdentifiersItem]): Details on identifiers
            that could not be removed.
    """

    removed: int
    not_found: int
    failed_identifiers: list[RemoveTrackerPeopleResponse200OutputFailedIdentifiersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        removed = self.removed

        not_found = self.not_found

        failed_identifiers = []
        for failed_identifiers_item_data in self.failed_identifiers:
            failed_identifiers_item = failed_identifiers_item_data.to_dict()
            failed_identifiers.append(failed_identifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "removed": removed,
                "notFound": not_found,
                "failedIdentifiers": failed_identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_tracker_people_response_200_output_failed_identifiers_item import (
            RemoveTrackerPeopleResponse200OutputFailedIdentifiersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        removed = d.pop("removed")

        not_found = d.pop("notFound")

        failed_identifiers = []
        _failed_identifiers = d.pop("failedIdentifiers")
        for failed_identifiers_item_data in _failed_identifiers:
            failed_identifiers_item = RemoveTrackerPeopleResponse200OutputFailedIdentifiersItem.from_dict(
                failed_identifiers_item_data
            )

            failed_identifiers.append(failed_identifiers_item)

        remove_tracker_people_response_200_output = cls(
            removed=removed,
            not_found=not_found,
            failed_identifiers=failed_identifiers,
        )

        remove_tracker_people_response_200_output.additional_properties = d
        return remove_tracker_people_response_200_output

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
