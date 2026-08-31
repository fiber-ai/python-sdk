from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_response_200_output_data_item import PeopleSearchResponse200OutputDataItem


T = TypeVar("T", bound="PeopleSearchResponse200Output")


@_attrs_define
class PeopleSearchResponse200Output:
    """
    Attributes:
        data (list[PeopleSearchResponse200OutputDataItem]):
        estimated_count (float | None | Unset): The estimated total number of people who match your search parameters.
            Note that this does not account for exclusion lists.
        next_cursor (None | str | Unset): The pagination cursor for the next page. Provide this in the next request to
            continue paginating.
    """

    data: list[PeopleSearchResponse200OutputDataItem]
    estimated_count: float | None | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        estimated_count: float | None | Unset
        if isinstance(self.estimated_count, Unset):
            estimated_count = UNSET
        else:
            estimated_count = self.estimated_count

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if estimated_count is not UNSET:
            field_dict["estimatedCount"] = estimated_count
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_response_200_output_data_item import (
            PeopleSearchResponse200OutputDataItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PeopleSearchResponse200OutputDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_estimated_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_count = _parse_estimated_count(d.pop("estimatedCount", UNSET))

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        people_search_response_200_output = cls(
            data=data,
            estimated_count=estimated_count,
            next_cursor=next_cursor,
        )

        people_search_response_200_output.additional_properties = d
        return people_search_response_200_output

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
