from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0_method import (
    JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Method,
)

if TYPE_CHECKING:
    from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0_criteria import (
        JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Criteria,
    )


T = TypeVar(
    "T", bound="JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0"
)


@_attrs_define
class JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0:
    """
    Attributes:
        method (JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Method):
        criteria
            (JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Criteria):
    """

    method: JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Method
    criteria: JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Criteria
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
        from ..models.jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0_criteria import (
            JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Criteria,
        )

        d = dict(src_dict)
        method = JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Method(
            d.pop("method")
        )

        criteria = JdToProfileSearchResponse200OutputUsedSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type0Criteria.from_dict(
            d.pop("criteria")
        )

        jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0 = cls(
            method=method,
            criteria=criteria,
        )

        jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0.additional_properties = d
        return jd_to_profile_search_response_200_output_used_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_0

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
