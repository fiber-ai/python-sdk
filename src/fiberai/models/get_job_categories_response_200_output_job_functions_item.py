from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_job_categories_response_200_output_job_functions_item_function import (
    GetJobCategoriesResponse200OutputJobFunctionsItemFunction,
)
from ..models.get_job_categories_response_200_output_job_functions_item_specialties_item import (
    GetJobCategoriesResponse200OutputJobFunctionsItemSpecialtiesItem,
)

T = TypeVar("T", bound="GetJobCategoriesResponse200OutputJobFunctionsItem")


@_attrs_define
class GetJobCategoriesResponse200OutputJobFunctionsItem:
    """
    Attributes:
        function (GetJobCategoriesResponse200OutputJobFunctionsItemFunction):
        specialties (list[GetJobCategoriesResponse200OutputJobFunctionsItemSpecialtiesItem]): Every specialty under this
            function, in taxonomy order. Use as `{ "type": "specialty", "value": "..." }` in the `jobCategories` filter.
    """

    function: GetJobCategoriesResponse200OutputJobFunctionsItemFunction
    specialties: list[GetJobCategoriesResponse200OutputJobFunctionsItemSpecialtiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function.value

        specialties = []
        for specialties_item_data in self.specialties:
            specialties_item = specialties_item_data.value
            specialties.append(specialties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "specialties": specialties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function = GetJobCategoriesResponse200OutputJobFunctionsItemFunction(d.pop("function"))

        specialties = []
        _specialties = d.pop("specialties")
        for specialties_item_data in _specialties:
            specialties_item = GetJobCategoriesResponse200OutputJobFunctionsItemSpecialtiesItem(specialties_item_data)

            specialties.append(specialties_item)

        get_job_categories_response_200_output_job_functions_item = cls(
            function=function,
            specialties=specialties,
        )

        get_job_categories_response_200_output_job_functions_item.additional_properties = d
        return get_job_categories_response_200_output_job_functions_item

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
