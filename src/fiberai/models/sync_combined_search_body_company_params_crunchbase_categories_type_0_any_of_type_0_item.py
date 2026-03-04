from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_crunchbase_categories_type_0_any_of_type_0_item_type import SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0ItemType






T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0Item")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0Item:
    """ 
        Attributes:
            group (str):
            category (str):
            type_ (SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0ItemType):
     """

    group: str
    category: str
    type_: SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0ItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        group = self.group

        category = self.category

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "group": group,
            "category": category,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group = d.pop("group")

        category = d.pop("category")

        type_ = SyncCombinedSearchBodyCompanyParamsCrunchbaseCategoriesType0AnyOfType0ItemType(d.pop("type"))




        sync_combined_search_body_company_params_crunchbase_categories_type_0_any_of_type_0_item = cls(
            group=group,
            category=category,
            type_=type_,
        )


        sync_combined_search_body_company_params_crunchbase_categories_type_0_any_of_type_0_item.additional_properties = d
        return sync_combined_search_body_company_params_crunchbase_categories_type_0_any_of_type_0_item

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
