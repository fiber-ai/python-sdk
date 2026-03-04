from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CreateProspectExclusionListBody")



@_attrs_define
class CreateProspectExclusionListBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            name (str): Name of the prospect exclusion list
            is_organization_wide (Union[Unset, bool]): Is the prospect exclusion list organization wide Default: False.
     """

    api_key: str
    name: str
    is_organization_wide: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        name = self.name

        is_organization_wide = self.is_organization_wide


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "name": name,
        })
        if is_organization_wide is not UNSET:
            field_dict["isOrganizationWide"] = is_organization_wide

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        name = d.pop("name")

        is_organization_wide = d.pop("isOrganizationWide", UNSET)

        create_prospect_exclusion_list_body = cls(
            api_key=api_key,
            name=name,
            is_organization_wide=is_organization_wide,
        )


        create_prospect_exclusion_list_body.additional_properties = d
        return create_prospect_exclusion_list_body

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
