from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jd_to_profile_search_response_200_output_data_item import JdToProfileSearchResponse200OutputDataItem
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItem,
    )
    from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0 import (
        JdToProfileSearchResponse200OutputUsedSearchParamsType0,
    )


T = TypeVar("T", bound="JdToProfileSearchResponse200Output")


@_attrs_define
class JdToProfileSearchResponse200Output:
    """
    Attributes:
        data (list[JdToProfileSearchResponse200OutputDataItem]):
        generated_search_params (list[JdToProfileSearchResponse200OutputGeneratedSearchParamsItem]):
        next_cursor (None | str | Unset): The pagination cursor for the next page. Provide this in the next request to
            continue paginating.
        used_search_params (JdToProfileSearchResponse200OutputUsedSearchParamsType0 | None | Unset):
    """

    data: list[JdToProfileSearchResponse200OutputDataItem]
    generated_search_params: list[JdToProfileSearchResponse200OutputGeneratedSearchParamsItem]
    next_cursor: None | str | Unset = UNSET
    used_search_params: JdToProfileSearchResponse200OutputUsedSearchParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0 import (
            JdToProfileSearchResponse200OutputUsedSearchParamsType0,
        )

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        generated_search_params = []
        for generated_search_params_item_data in self.generated_search_params:
            generated_search_params_item = generated_search_params_item_data.to_dict()
            generated_search_params.append(generated_search_params_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        used_search_params: dict[str, Any] | None | Unset
        if isinstance(self.used_search_params, Unset):
            used_search_params = UNSET
        elif isinstance(self.used_search_params, JdToProfileSearchResponse200OutputUsedSearchParamsType0):
            used_search_params = self.used_search_params.to_dict()
        else:
            used_search_params = self.used_search_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "generatedSearchParams": generated_search_params,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if used_search_params is not UNSET:
            field_dict["usedSearchParams"] = used_search_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jd_to_profile_search_response_200_output_data_item import (
            JdToProfileSearchResponse200OutputDataItem,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItem,
        )
        from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0 import (
            JdToProfileSearchResponse200OutputUsedSearchParamsType0,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = JdToProfileSearchResponse200OutputDataItem.from_dict(data_item_data)

            data.append(data_item)

        generated_search_params = []
        _generated_search_params = d.pop("generatedSearchParams")
        for generated_search_params_item_data in _generated_search_params:
            generated_search_params_item = JdToProfileSearchResponse200OutputGeneratedSearchParamsItem.from_dict(
                generated_search_params_item_data
            )

            generated_search_params.append(generated_search_params_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        def _parse_used_search_params(
            data: object,
        ) -> JdToProfileSearchResponse200OutputUsedSearchParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                used_search_params_type_0 = JdToProfileSearchResponse200OutputUsedSearchParamsType0.from_dict(data)

                return used_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JdToProfileSearchResponse200OutputUsedSearchParamsType0 | None | Unset, data)

        used_search_params = _parse_used_search_params(d.pop("usedSearchParams", UNSET))

        jd_to_profile_search_response_200_output = cls(
            data=data,
            generated_search_params=generated_search_params,
            next_cursor=next_cursor,
            used_search_params=used_search_params,
        )

        jd_to_profile_search_response_200_output.additional_properties = d
        return jd_to_profile_search_response_200_output

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
