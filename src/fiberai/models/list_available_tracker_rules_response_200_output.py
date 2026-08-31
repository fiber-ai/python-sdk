from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_available_tracker_rules_response_200_output_company_rules_item import (
        ListAvailableTrackerRulesResponse200OutputCompanyRulesItem,
    )
    from ..models.list_available_tracker_rules_response_200_output_person_rules_item import (
        ListAvailableTrackerRulesResponse200OutputPersonRulesItem,
    )


T = TypeVar("T", bound="ListAvailableTrackerRulesResponse200Output")


@_attrs_define
class ListAvailableTrackerRulesResponse200Output:
    """
    Attributes:
        company_rules (list[ListAvailableTrackerRulesResponse200OutputCompanyRulesItem]): All available company tracking
            rule types.
        person_rules (list[ListAvailableTrackerRulesResponse200OutputPersonRulesItem]): All available person tracking
            rule types.
        total_rule_count (int): Total number of available rule types across both entity types.
    """

    company_rules: list[ListAvailableTrackerRulesResponse200OutputCompanyRulesItem]
    person_rules: list[ListAvailableTrackerRulesResponse200OutputPersonRulesItem]
    total_rule_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_rules = []
        for company_rules_item_data in self.company_rules:
            company_rules_item = company_rules_item_data.to_dict()
            company_rules.append(company_rules_item)

        person_rules = []
        for person_rules_item_data in self.person_rules:
            person_rules_item = person_rules_item_data.to_dict()
            person_rules.append(person_rules_item)

        total_rule_count = self.total_rule_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyRules": company_rules,
                "personRules": person_rules,
                "totalRuleCount": total_rule_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_available_tracker_rules_response_200_output_company_rules_item import (
            ListAvailableTrackerRulesResponse200OutputCompanyRulesItem,  # noqa: PLC0415
        )
        from ..models.list_available_tracker_rules_response_200_output_person_rules_item import (
            ListAvailableTrackerRulesResponse200OutputPersonRulesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        company_rules = []
        _company_rules = d.pop("companyRules")
        for company_rules_item_data in _company_rules:
            company_rules_item = ListAvailableTrackerRulesResponse200OutputCompanyRulesItem.from_dict(
                company_rules_item_data
            )

            company_rules.append(company_rules_item)

        person_rules = []
        _person_rules = d.pop("personRules")
        for person_rules_item_data in _person_rules:
            person_rules_item = ListAvailableTrackerRulesResponse200OutputPersonRulesItem.from_dict(
                person_rules_item_data
            )

            person_rules.append(person_rules_item)

        total_rule_count = d.pop("totalRuleCount")

        list_available_tracker_rules_response_200_output = cls(
            company_rules=company_rules,
            person_rules=person_rules,
            total_rule_count=total_rule_count,
        )

        list_available_tracker_rules_response_200_output.additional_properties = d
        return list_available_tracker_rules_response_200_output

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
