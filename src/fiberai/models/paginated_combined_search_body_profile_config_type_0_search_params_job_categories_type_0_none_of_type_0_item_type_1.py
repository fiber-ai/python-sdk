from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_categories_type_0_none_of_type_0_item_type_1_type import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Type,
)
from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_categories_type_0_none_of_type_0_item_type_1_value import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Value,
)

T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1"
)


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1:
    """
    Attributes:
        type_ (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Type):
        value (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Value):
    """

    type_: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Type
    value: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Value

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value.value

        field_dict: dict[str, Any] = {}

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
        type_ = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Type(
            d.pop("type")
        )

        value = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobCategoriesType0NoneOfType0ItemType1Value(
            d.pop("value")
        )

        paginated_combined_search_body_profile_config_type_0_search_params_job_categories_type_0_none_of_type_0_item_type_1 = cls(
            type_=type_,
            value=value,
        )

        return paginated_combined_search_body_profile_config_type_0_search_params_job_categories_type_0_none_of_type_0_item_type_1
