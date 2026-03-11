from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_prospects_to_exclusion_list_body_prospects_item import (
        AddProspectsToExclusionListBodyProspectsItem,
    )


T = TypeVar("T", bound="AddProspectsToExclusionListBody")


@_attrs_define
class AddProspectsToExclusionListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        list_id (str): Id of the prospect exclusion list to add prospects to
        prospects (list[AddProspectsToExclusionListBodyProspectsItem]): Prospects to add to the exclusion list. Max 5000
            prospects can be added at a time.
    """

    api_key: str
    list_id: str
    prospects: list[AddProspectsToExclusionListBodyProspectsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        list_id = self.list_id

        prospects = []
        for prospects_item_data in self.prospects:
            prospects_item = prospects_item_data.to_dict()
            prospects.append(prospects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "listId": list_id,
                "prospects": prospects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_prospects_to_exclusion_list_body_prospects_item import (
            AddProspectsToExclusionListBodyProspectsItem,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        list_id = d.pop("listId")

        prospects = []
        _prospects = d.pop("prospects")
        for prospects_item_data in _prospects:
            prospects_item = AddProspectsToExclusionListBodyProspectsItem.from_dict(prospects_item_data)

            prospects.append(prospects_item)

        add_prospects_to_exclusion_list_body = cls(
            api_key=api_key,
            list_id=list_id,
            prospects=prospects,
        )

        add_prospects_to_exclusion_list_body.additional_properties = d
        return add_prospects_to_exclusion_list_body

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
