from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.text_to_profile_search_params_response_200_output_search_params import (
        TextToProfileSearchParamsResponse200OutputSearchParams,
    )


T = TypeVar("T", bound="TextToProfileSearchParamsResponse200Output")


@_attrs_define
class TextToProfileSearchParamsResponse200Output:
    """
    Attributes:
        search_params (TextToProfileSearchParamsResponse200OutputSearchParams):
    """

    search_params: TextToProfileSearchParamsResponse200OutputSearchParams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_params = self.search_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "searchParams": search_params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_params_response_200_output_search_params import (
            TextToProfileSearchParamsResponse200OutputSearchParams,
        )

        d = dict(src_dict)
        search_params = TextToProfileSearchParamsResponse200OutputSearchParams.from_dict(d.pop("searchParams"))

        text_to_profile_search_params_response_200_output = cls(
            search_params=search_params,
        )

        text_to_profile_search_params_response_200_output.additional_properties = d
        return text_to_profile_search_params_response_200_output

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
