from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0_method import (
    PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Method,
)

if TYPE_CHECKING:
    from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0_criteria import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Criteria,
    )


T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0:
    """
    Attributes:
        method (PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Method):
        criteria (PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Criteria):
    """

    method: PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Method
    criteria: PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Criteria
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
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0_criteria import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Criteria,  # noqa: PLC0415
        )

        d = dict(src_dict)
        method = PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Method(d.pop("method"))

        criteria = PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0Criteria.from_dict(
            d.pop("criteria")
        )

        people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0 = cls(
            method=method,
            criteria=criteria,
        )

        people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0.additional_properties = d
        return people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0

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
