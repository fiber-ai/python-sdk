from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_audiences_response_200_output_audiences_item import ListAudiencesResponse200OutputAudiencesItem


T = TypeVar("T", bound="ListAudiencesResponse200Output")


@_attrs_define
class ListAudiencesResponse200Output:
    """
    Attributes:
        audiences (list[ListAudiencesResponse200OutputAudiencesItem]):
        total_count (float): Total number of audiences
    """

    audiences: list[ListAudiencesResponse200OutputAudiencesItem]
    total_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audiences = []
        for audiences_item_data in self.audiences:
            audiences_item = audiences_item_data.to_dict()
            audiences.append(audiences_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audiences": audiences,
                "totalCount": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_audiences_response_200_output_audiences_item import (
            ListAudiencesResponse200OutputAudiencesItem,
        )

        d = dict(src_dict)
        audiences = []
        _audiences = d.pop("audiences")
        for audiences_item_data in _audiences:
            audiences_item = ListAudiencesResponse200OutputAudiencesItem.from_dict(audiences_item_data)

            audiences.append(audiences_item)

        total_count = d.pop("totalCount")

        list_audiences_response_200_output = cls(
            audiences=audiences,
            total_count=total_count,
        )

        list_audiences_response_200_output.additional_properties = d
        return list_audiences_response_200_output

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
