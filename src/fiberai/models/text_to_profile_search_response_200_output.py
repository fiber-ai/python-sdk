from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_profile_search_response_200_output_data_item import (
        TextToProfileSearchResponse200OutputDataItem,
    )
    from ..models.text_to_profile_search_response_200_output_search_params import (
        TextToProfileSearchResponse200OutputSearchParams,
    )


T = TypeVar("T", bound="TextToProfileSearchResponse200Output")


@_attrs_define
class TextToProfileSearchResponse200Output:
    """
    Attributes:
        data (list[TextToProfileSearchResponse200OutputDataItem]):
        search_params (TextToProfileSearchResponse200OutputSearchParams):
        next_cursor (None | str | Unset): The cursor for paginating to next page. Provide this in next search call and
            we will paginate from that point onward.
    """

    data: list[TextToProfileSearchResponse200OutputDataItem]
    search_params: TextToProfileSearchResponse200OutputSearchParams
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        search_params = self.search_params.to_dict()

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
                "searchParams": search_params,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_response_200_output_data_item import (
            TextToProfileSearchResponse200OutputDataItem,
        )
        from ..models.text_to_profile_search_response_200_output_search_params import (
            TextToProfileSearchResponse200OutputSearchParams,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TextToProfileSearchResponse200OutputDataItem.from_dict(data_item_data)

            data.append(data_item)

        search_params = TextToProfileSearchResponse200OutputSearchParams.from_dict(d.pop("searchParams"))

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        text_to_profile_search_response_200_output = cls(
            data=data,
            search_params=search_params,
            next_cursor=next_cursor,
        )

        text_to_profile_search_response_200_output.additional_properties = d
        return text_to_profile_search_response_200_output

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
