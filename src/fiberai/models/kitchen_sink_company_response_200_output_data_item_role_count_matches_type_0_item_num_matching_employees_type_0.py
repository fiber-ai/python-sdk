from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0_type import (
    KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0Type,
)

T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0:
    """
    Attributes:
        type_ (KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0Type):
        value (float):
    """

    type_: KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0Type
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0Type(
            d.pop("type")
        )

        value = d.pop("value")

        kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0 = cls(
            type_=type_,
            value=value,
        )

        kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0

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
