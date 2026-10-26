from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.job_posting_search_count_body_search_params_job_categories_type_0_none_of_type_0_item_type_1_type import (
    JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Type,
)
from ..models.job_posting_search_count_body_search_params_job_categories_type_0_none_of_type_0_item_type_1_value import (
    JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Value,
)

T = TypeVar("T", bound="JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1")


@_attrs_define
class JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1:
    """
    Attributes:
        type_ (JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Type):
        value (JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Value):
    """

    type_: JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Type
    value: JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Value

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
        type_ = JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Type(d.pop("type"))

        value = JobPostingSearchCountBodySearchParamsJobCategoriesType0NoneOfType0ItemType1Value(d.pop("value"))

        job_posting_search_count_body_search_params_job_categories_type_0_none_of_type_0_item_type_1 = cls(
            type_=type_,
            value=value,
        )

        return job_posting_search_count_body_search_params_job_categories_type_0_none_of_type_0_item_type_1
