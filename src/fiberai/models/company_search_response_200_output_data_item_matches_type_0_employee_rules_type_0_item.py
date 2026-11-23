from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item import (
        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem,
    )
    from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0 import (
        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0,
    )


T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0Item:
    """The people behind one employees rule.

    Attributes:
        rule_index (int): Position of the rule in `searchParams.employees.rules` that these matches belong to, starting
            at 0.
        people (list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem]): A capped
            sample of the matching people, most recent start first.
        total_count (CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0 | None |
            Unset): How many people at this company satisfy the rule. Null when the rule has no countable people: it asks
            that all or none of the employees match, or the company was returned through an OR joiner without matching this
            rule.
    """

    rule_index: int
    people: list[CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem]
    total_count: (
        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0 import (
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0,  # noqa: PLC0415
        )

        rule_index = self.rule_index

        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        total_count: dict[str, Any] | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        elif isinstance(
            self.total_count, CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0
        ):
            total_count = self.total_count.to_dict()
        else:
            total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_index": rule_index,
                "people": people,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item import (
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem,  # noqa: PLC0415
        )
        from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_total_count_type_0 import (
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        rule_index = d.pop("rule_index")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem.from_dict(
                people_item_data
            )

            people.append(people_item)

        def _parse_total_count(
            data: object,
        ) -> CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_count_type_0 = (
                    CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0.from_dict(
                        data
                    )
                )

                return total_count_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemTotalCountType0 | None | Unset,
                data,
            )

        total_count = _parse_total_count(d.pop("total_count", UNSET))

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item = cls(
            rule_index=rule_index,
            people=people,
            total_count=total_count,
        )

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item

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
