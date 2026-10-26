from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_all_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0_type import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type,
)
from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_all_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0_value import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value,
)

T = TypeVar(
    "T",
    bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0",
)


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0:
    """
    Attributes:
        type_ (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfTy
            pe0ItemType0Type):
        value (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfTy
            pe0ItemType0Value):
    """

    type_: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type
    value: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value

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
        type_ = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type(
            d.pop("type")
        )

        value = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value(
            d.pop("value")
        )

        paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_all_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0 = cls(
            type_=type_,
            value=value,
        )

        return paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_all_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0
