from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_excluded_prospects_for_exclusion_list_response_200_output_prospects_item import (
        GetExcludedProspectsForExclusionListResponse200OutputProspectsItem,
    )


T = TypeVar("T", bound="GetExcludedProspectsForExclusionListResponse200Output")


@_attrs_define
class GetExcludedProspectsForExclusionListResponse200Output:
    """
    Attributes:
        prospects (list[GetExcludedProspectsForExclusionListResponse200OutputProspectsItem]): List of excluded prospects
        next_cursor (None | str): Cursor for the next page of results
        has_more (bool): Whether there are more results available
    """

    prospects: list[GetExcludedProspectsForExclusionListResponse200OutputProspectsItem]
    next_cursor: None | str
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prospects = []
        for prospects_item_data in self.prospects:
            prospects_item = prospects_item_data.to_dict()
            prospects.append(prospects_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prospects": prospects,
                "nextCursor": next_cursor,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_excluded_prospects_for_exclusion_list_response_200_output_prospects_item import (
            GetExcludedProspectsForExclusionListResponse200OutputProspectsItem,
        )

        d = dict(src_dict)
        prospects = []
        _prospects = d.pop("prospects")
        for prospects_item_data in _prospects:
            prospects_item = GetExcludedProspectsForExclusionListResponse200OutputProspectsItem.from_dict(
                prospects_item_data
            )

            prospects.append(prospects_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        has_more = d.pop("hasMore")

        get_excluded_prospects_for_exclusion_list_response_200_output = cls(
            prospects=prospects,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        get_excluded_prospects_for_exclusion_list_response_200_output.additional_properties = d
        return get_excluded_prospects_for_exclusion_list_response_200_output

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
