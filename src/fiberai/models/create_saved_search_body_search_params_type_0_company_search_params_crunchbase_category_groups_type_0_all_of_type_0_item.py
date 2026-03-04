from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_0_company_search_params_crunchbase_category_groups_type_0_all_of_type_0_item_type import CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0ItemType






T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0Item")



@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0Item:
    """ 
        Attributes:
            group (str):
            type_
                (CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0ItemType):
     """

    group: str
    type_: CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0ItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        group = self.group

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "group": group,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group = d.pop("group")

        type_ = CreateSavedSearchBodySearchParamsType0CompanySearchParamsCrunchbaseCategoryGroupsType0AllOfType0ItemType(d.pop("type"))




        create_saved_search_body_search_params_type_0_company_search_params_crunchbase_category_groups_type_0_all_of_type_0_item = cls(
            group=group,
            type_=type_,
        )


        create_saved_search_body_search_params_type_0_company_search_params_crunchbase_category_groups_type_0_all_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_crunchbase_category_groups_type_0_all_of_type_0_item

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
