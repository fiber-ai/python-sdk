from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_available_tracker_rules_response_200_output_person_rules_item_config_example import (
        ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigExample,
    )
    from ..models.list_available_tracker_rules_response_200_output_person_rules_item_config_schema import (
        ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigSchema,
    )


T = TypeVar("T", bound="ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfig")


@_attrs_define
class ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfig:
    """Config schema and example for creating this rule type.

    Attributes:
        schema (ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigSchema): JSON Schema for the rule config
            object. Pass a config conforming to this schema when creating a tracker list rule.
        example (ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigExample): A valid example config you can
            pass directly to create a rule.
    """

    schema: ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigSchema
    example: ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigExample
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema.to_dict()

        example = self.example.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
                "example": example,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_available_tracker_rules_response_200_output_person_rules_item_config_example import (
            ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigExample,
        )
        from ..models.list_available_tracker_rules_response_200_output_person_rules_item_config_schema import (
            ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigSchema,
        )

        d = dict(src_dict)
        schema = ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigSchema.from_dict(d.pop("schema"))

        example = ListAvailableTrackerRulesResponse200OutputPersonRulesItemConfigExample.from_dict(d.pop("example"))

        list_available_tracker_rules_response_200_output_person_rules_item_config = cls(
            schema=schema,
            example=example,
        )

        list_available_tracker_rules_response_200_output_person_rules_item_config.additional_properties = d
        return list_available_tracker_rules_response_200_output_person_rules_item_config

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
