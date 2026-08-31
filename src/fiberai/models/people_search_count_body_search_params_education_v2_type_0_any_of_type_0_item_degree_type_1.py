from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1_method import (
    PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Method,
)

if TYPE_CHECKING:
    from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1_criteria import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Criteria,
    )


T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1")


@_attrs_define
class PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1:
    """
    Attributes:
        method (PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Method):
        criteria (PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Criteria):
    """

    method: PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Method
    criteria: PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Criteria
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        criteria = self.criteria.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "criteria": criteria,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1_criteria import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Criteria,  # noqa: PLC0415
        )

        d = dict(src_dict)
        method = PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Method(d.pop("method"))

        criteria = PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemDegreeType1Criteria.from_dict(
            d.pop("criteria")
        )

        people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 = cls(
            method=method,
            criteria=criteria,
        )

        people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1.additional_properties = d
        return people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1

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
