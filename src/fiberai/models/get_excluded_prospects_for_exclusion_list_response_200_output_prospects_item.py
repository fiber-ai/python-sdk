from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetExcludedProspectsForExclusionListResponse200OutputProspectsItem")


@_attrs_define
class GetExcludedProspectsForExclusionListResponse200OutputProspectsItem:
    """
    Attributes:
        id (str): ID of the excluded prospect
        linked_in_url (None | str): LinkedIn URL of the excluded prospect
    """

    id: str
    linked_in_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        linked_in_url: None | str
        linked_in_url = self.linked_in_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "linkedInUrl": linked_in_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_linked_in_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl"))

        get_excluded_prospects_for_exclusion_list_response_200_output_prospects_item = cls(
            id=id,
            linked_in_url=linked_in_url,
        )

        get_excluded_prospects_for_exclusion_list_response_200_output_prospects_item.additional_properties = d
        return get_excluded_prospects_for_exclusion_list_response_200_output_prospects_item

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
