from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_saved_search_body_search_params_type_2_profile_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0_type import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type,
)
from ..models.create_saved_search_body_search_params_type_2_profile_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0_value import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value,
)

T = TypeVar(
    "T",
    bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0",
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0:
    """
    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfT
            ype0ItemType0Type):
        value (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfT
            ype0ItemType0Value):
    """

    type_: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type
    value: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value

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
        type_ = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Type(
            d.pop("type")
        )

        value = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobsType0NoneOfType0ItemJobCategoriesType0AnyOfType0ItemType0Value(
            d.pop("value")
        )

        create_saved_search_body_search_params_type_2_profile_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0 = cls(
            type_=type_,
            value=value,
        )

        return create_saved_search_body_search_params_type_2_profile_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0_any_of_type_0_item_type_0
