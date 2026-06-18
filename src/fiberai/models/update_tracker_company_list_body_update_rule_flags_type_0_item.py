from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item")


@_attrs_define
class UpdateTrackerCompanyListBodyUpdateRuleFlagsType0Item:
    """
    Attributes:
        rule_id (str): ID of the rule to update.
        is_dummy (bool): Set `isDummy` flag on this rule.
    """

    rule_id: str
    is_dummy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_id = self.rule_id

        is_dummy = self.is_dummy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ruleId": rule_id,
                "isDummy": is_dummy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_id = d.pop("ruleId")

        is_dummy = d.pop("isDummy")

        update_tracker_company_list_body_update_rule_flags_type_0_item = cls(
            rule_id=rule_id,
            is_dummy=is_dummy,
        )

        update_tracker_company_list_body_update_rule_flags_type_0_item.additional_properties = d
        return update_tracker_company_list_body_update_rule_flags_type_0_item

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
