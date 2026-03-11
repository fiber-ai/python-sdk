from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_combined_search_response_200_output_data_type_0 import (
        PollCombinedSearchResponse200OutputDataType0,
    )
    from ..models.poll_combined_search_response_200_output_data_type_1 import (
        PollCombinedSearchResponse200OutputDataType1,
    )


T = TypeVar("T", bound="PollCombinedSearchResponse200Output")


@_attrs_define
class PollCombinedSearchResponse200Output:
    """
    Attributes:
        data (PollCombinedSearchResponse200OutputDataType0 | PollCombinedSearchResponse200OutputDataType1):
        next_cursor (None | str | Unset): The cursor for paginating to next page. Provide this in next search call and
            we will paginate from that point onward.
    """

    data: PollCombinedSearchResponse200OutputDataType0 | PollCombinedSearchResponse200OutputDataType1
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_combined_search_response_200_output_data_type_0 import (
            PollCombinedSearchResponse200OutputDataType0,
        )

        data: dict[str, Any]
        if isinstance(self.data, PollCombinedSearchResponse200OutputDataType0):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

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
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_combined_search_response_200_output_data_type_0 import (
            PollCombinedSearchResponse200OutputDataType0,
        )
        from ..models.poll_combined_search_response_200_output_data_type_1 import (
            PollCombinedSearchResponse200OutputDataType1,
        )

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> PollCombinedSearchResponse200OutputDataType0 | PollCombinedSearchResponse200OutputDataType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = PollCombinedSearchResponse200OutputDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = PollCombinedSearchResponse200OutputDataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        poll_combined_search_response_200_output = cls(
            data=data,
            next_cursor=next_cursor,
        )

        poll_combined_search_response_200_output.additional_properties = d
        return poll_combined_search_response_200_output

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
