from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_company_search_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3_type import (
    TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3Type,
)

T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3")


@_attrs_define
class TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3:
    """
    Attributes:
        type_ (TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3Type):
    """

    type_: TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = TextToCompanySearchResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3Type(
            d.pop("type")
        )

        text_to_company_search_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3 = cls(
            type_=type_,
        )

        text_to_company_search_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3.additional_properties = d
        return text_to_company_search_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3

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
