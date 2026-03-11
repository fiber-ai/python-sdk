from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TextToCompanySearchResponse200OutputSearchParamsNaicsCodesType0NoneOfType0Item")


@_attrs_define
class TextToCompanySearchResponse200OutputSearchParamsNaicsCodesType0NoneOfType0Item:
    """
    Attributes:
        code (str):
        title (str):
    """

    code: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        title = d.pop("title")

        text_to_company_search_response_200_output_search_params_naics_codes_type_0_none_of_type_0_item = cls(
            code=code,
            title=title,
        )

        text_to_company_search_response_200_output_search_params_naics_codes_type_0_none_of_type_0_item.additional_properties = d
        return text_to_company_search_response_200_output_search_params_naics_codes_type_0_none_of_type_0_item

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
