from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_tracker_company_lists_response_200_output_lists_item import (
        ListTrackerCompanyListsResponse200OutputListsItem,
    )


T = TypeVar("T", bound="ListTrackerCompanyListsResponse200Output")


@_attrs_define
class ListTrackerCompanyListsResponse200Output:
    """
    Attributes:
        lists (list[ListTrackerCompanyListsResponse200OutputListsItem]):
    """

    lists: list[ListTrackerCompanyListsResponse200OutputListsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lists = []
        for lists_item_data in self.lists:
            lists_item = lists_item_data.to_dict()
            lists.append(lists_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lists": lists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_tracker_company_lists_response_200_output_lists_item import (
            ListTrackerCompanyListsResponse200OutputListsItem,
        )

        d = dict(src_dict)
        lists = []
        _lists = d.pop("lists")
        for lists_item_data in _lists:
            lists_item = ListTrackerCompanyListsResponse200OutputListsItem.from_dict(lists_item_data)

            lists.append(lists_item)

        list_tracker_company_lists_response_200_output = cls(
            lists=lists,
        )

        list_tracker_company_lists_response_200_output.additional_properties = d
        return list_tracker_company_lists_response_200_output

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
