from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteCompanyExclusionListBody")


@_attrs_define
class DeleteCompanyExclusionListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        list_i_ds (list[str]): Ids of the company exclusion lists to delete
    """

    api_key: str
    list_i_ds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        list_i_ds = self.list_i_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "listIDs": list_i_ds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        list_i_ds = cast(list[str], d.pop("listIDs"))

        delete_company_exclusion_list_body = cls(
            api_key=api_key,
            list_i_ds=list_i_ds,
        )

        delete_company_exclusion_list_body.additional_properties = d
        return delete_company_exclusion_list_body

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
