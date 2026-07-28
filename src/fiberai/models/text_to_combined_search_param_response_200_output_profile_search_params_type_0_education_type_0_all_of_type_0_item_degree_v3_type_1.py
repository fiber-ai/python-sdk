from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1_method import (
    TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Method,
)

if TYPE_CHECKING:
    from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1_criteria import (
        TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Criteria,
    )


T = TypeVar(
    "T",
    bound="TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1",
)


@_attrs_define
class TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1:
    """
    Attributes:
        method (TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Ty
            pe1Method):
        criteria (TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3
            Type1Criteria):
    """

    method: TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Method
    criteria: TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Criteria
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
        from ..models.text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1_criteria import (
            TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Criteria,
        )

        d = dict(src_dict)
        method = TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Method(
            d.pop("method")
        )

        criteria = TextToCombinedSearchParamResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemDegreeV3Type1Criteria.from_dict(
            d.pop("criteria")
        )

        text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1 = cls(
            method=method,
            criteria=criteria,
        )

        text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1.additional_properties = d
        return text_to_combined_search_param_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_degree_v3_type_1

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
