from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteCompanyExclusionListResponse200Output")


@_attrs_define
class DeleteCompanyExclusionListResponse200Output:
    """
    Attributes:
        list_i_ds (list[str]): Ids of the company exclusion lists deleted
    """

    list_i_ds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_i_ds = self.list_i_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listIDs": list_i_ds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_i_ds = cast(list[str], d.pop("listIDs"))

        delete_company_exclusion_list_response_200_output = cls(
            list_i_ds=list_i_ds,
        )

        delete_company_exclusion_list_response_200_output.additional_properties = d
        return delete_company_exclusion_list_response_200_output

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
