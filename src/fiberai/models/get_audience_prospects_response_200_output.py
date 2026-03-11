from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_audience_prospects_response_200_output_prospects_item import (
        GetAudienceProspectsResponse200OutputProspectsItem,
    )


T = TypeVar("T", bound="GetAudienceProspectsResponse200Output")


@_attrs_define
class GetAudienceProspectsResponse200Output:
    """
    Attributes:
        audience_id (str): ID of the audience
        prospects (list[GetAudienceProspectsResponse200OutputProspectsItem]): List of prospects
        total_count (float): Total number of prospects in the audience
        has_more (bool): Whether there are more results
        next_cursor (None | str | Unset): Cursor for pagination
    """

    audience_id: str
    prospects: list[GetAudienceProspectsResponse200OutputProspectsItem]
    total_count: float
    has_more: bool
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_id = self.audience_id

        prospects = []
        for prospects_item_data in self.prospects:
            prospects_item = prospects_item_data.to_dict()
            prospects.append(prospects_item)

        total_count = self.total_count

        has_more = self.has_more

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceId": audience_id,
                "prospects": prospects,
                "totalCount": total_count,
                "hasMore": has_more,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_audience_prospects_response_200_output_prospects_item import (
            GetAudienceProspectsResponse200OutputProspectsItem,
        )

        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        prospects = []
        _prospects = d.pop("prospects")
        for prospects_item_data in _prospects:
            prospects_item = GetAudienceProspectsResponse200OutputProspectsItem.from_dict(prospects_item_data)

            prospects.append(prospects_item)

        total_count = d.pop("totalCount")

        has_more = d.pop("hasMore")

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        get_audience_prospects_response_200_output = cls(
            audience_id=audience_id,
            prospects=prospects,
            total_count=total_count,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        get_audience_prospects_response_200_output.additional_properties = d
        return get_audience_prospects_response_200_output

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
