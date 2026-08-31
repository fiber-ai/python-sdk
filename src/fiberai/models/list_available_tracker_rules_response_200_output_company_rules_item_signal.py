from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal_example import (
        ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalExample,
    )
    from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal_schema import (
        ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalSchema,
    )


T = TypeVar("T", bound="ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal")


@_attrs_define
class ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal:
    """Signal output schema and example for this rule type.

    Attributes:
        schema (ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalSchema): JSON Schema for each item in
            the changeData array. When this rule fires, the signal contains one or more changeData items conforming to this
            schema.
        example (ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalExample): A concrete changeData item
            example matching the schema above.
    """

    schema: ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalSchema
    example: ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalExample
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
        from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal_example import (
            ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalExample,  # noqa: PLC0415
        )
        from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal_schema import (
            ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalSchema,  # noqa: PLC0415
        )

        d = dict(src_dict)
        schema = ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalSchema.from_dict(d.pop("schema"))

        example = ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignalExample.from_dict(d.pop("example"))

        list_available_tracker_rules_response_200_output_company_rules_item_signal = cls(
            schema=schema,
            example=example,
        )

        list_available_tracker_rules_response_200_output_company_rules_item_signal.additional_properties = d
        return list_available_tracker_rules_response_200_output_company_rules_item_signal

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
