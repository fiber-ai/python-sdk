from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0:
    """How many people at this company satisfy the rule. Null when the rule has no countable people: it asks that all or
    none of the employees match, or the company was returned through an OR joiner without matching this rule.

        Attributes:
            count (int): Number of matches found.
            is_lower_bound (bool): True when more matches exist than were counted, so `count` is a minimum.
    """

    count: int
    is_lower_bound: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        is_lower_bound = self.is_lower_bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "is_lower_bound": is_lower_bound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        is_lower_bound = d.pop("is_lower_bound")

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0 = cls(
            count=count,
            is_lower_bound=is_lower_bound,
        )

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0

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
