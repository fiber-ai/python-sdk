from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_tracker_company_list_body_company_search_params_type_0_crunchbase_categories_type_0_none_of_type_0_item_type import (
    CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0ItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0Item")


@_attrs_define
class CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0Item:
    """
    Attributes:
        category (str):
        type_ (CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0ItemType):
        group (None | str | Unset):
    """

    category: str
    type_: CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0ItemType
    group: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        type_ = self.type_.value

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "type": type_,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        type_ = CreateTrackerCompanyListBodyCompanySearchParamsType0CrunchbaseCategoriesType0NoneOfType0ItemType(
            d.pop("type")
        )

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        create_tracker_company_list_body_company_search_params_type_0_crunchbase_categories_type_0_none_of_type_0_item = cls(
            category=category,
            type_=type_,
            group=group,
        )

        create_tracker_company_list_body_company_search_params_type_0_crunchbase_categories_type_0_none_of_type_0_item.additional_properties = d
        return create_tracker_company_list_body_company_search_params_type_0_crunchbase_categories_type_0_none_of_type_0_item

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
