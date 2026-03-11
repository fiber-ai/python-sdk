from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddProspectsToExclusionListResponse200Output")


@_attrs_define
class AddProspectsToExclusionListResponse200Output:
    """
    Attributes:
        list_id (str): Id of the prospect exclusion list
        prospects_added (float): Number of prospects added to the exclusion list
    """

    list_id: str
    prospects_added: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        prospects_added = self.prospects_added

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "prospectsAdded": prospects_added,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("listId")

        prospects_added = d.pop("prospectsAdded")

        add_prospects_to_exclusion_list_response_200_output = cls(
            list_id=list_id,
            prospects_added=prospects_added,
        )

        add_prospects_to_exclusion_list_response_200_output.additional_properties = d
        return add_prospects_to_exclusion_list_response_200_output

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
