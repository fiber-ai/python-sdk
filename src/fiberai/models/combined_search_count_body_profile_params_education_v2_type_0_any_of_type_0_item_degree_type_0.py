from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0_method import (
    CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Method,
)

if TYPE_CHECKING:
    from ..models.combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0_criteria import (
        CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Criteria,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0")


@_attrs_define
class CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0:
    """
    Attributes:
        method (CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Method):
        criteria (CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Criteria):
    """

    method: CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Method
    criteria: CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Criteria
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
        from ..models.combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0_criteria import (
            CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Criteria,  # noqa: PLC0415
        )

        d = dict(src_dict)
        method = CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Method(d.pop("method"))

        criteria = CombinedSearchCountBodyProfileParamsEducationV2Type0AnyOfType0ItemDegreeType0Criteria.from_dict(
            d.pop("criteria")
        )

        combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0 = cls(
            method=method,
            criteria=criteria,
        )

        combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0.additional_properties = d
        return combined_search_count_body_profile_params_education_v2_type_0_any_of_type_0_item_degree_type_0

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
