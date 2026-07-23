from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_available_tracker_rules_response_200_output_company_rules_item_entity_type import (
    ListAvailableTrackerRulesResponse200OutputCompanyRulesItemEntityType,
)

if TYPE_CHECKING:
    from ..models.list_available_tracker_rules_response_200_output_company_rules_item_config import (
        ListAvailableTrackerRulesResponse200OutputCompanyRulesItemConfig,
    )
    from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal import (
        ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal,
    )


T = TypeVar("T", bound="ListAvailableTrackerRulesResponse200OutputCompanyRulesItem")


@_attrs_define
class ListAvailableTrackerRulesResponse200OutputCompanyRulesItem:
    """
    Attributes:
        name (str): Rule type slug used in config objects (e.g. headcount_crossed_threshold).
        readable_name (str): Human-readable name for this rule type.
        entity_type (ListAvailableTrackerRulesResponse200OutputCompanyRulesItemEntityType): Whether this rule applies to
            company or person lists.
        description (str): What change this rule detects and when it fires.
        use_case (str): Sales-oriented example of why you would use this rule.
        supports_initial_signals (bool): Whether this rule supports immediate initial signals on entity addition.
        config (ListAvailableTrackerRulesResponse200OutputCompanyRulesItemConfig): Config schema and example for
            creating this rule type.
        signal (ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal): Signal output schema and example for
            this rule type.
    """

    name: str
    readable_name: str
    entity_type: ListAvailableTrackerRulesResponse200OutputCompanyRulesItemEntityType
    description: str
    use_case: str
    supports_initial_signals: bool
    config: ListAvailableTrackerRulesResponse200OutputCompanyRulesItemConfig
    signal: ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        readable_name = self.readable_name

        entity_type = self.entity_type.value

        description = self.description

        use_case = self.use_case

        supports_initial_signals = self.supports_initial_signals

        config = self.config.to_dict()

        signal = self.signal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "readableName": readable_name,
                "entityType": entity_type,
                "description": description,
                "useCase": use_case,
                "supportsInitialSignals": supports_initial_signals,
                "config": config,
                "signal": signal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_available_tracker_rules_response_200_output_company_rules_item_config import (
            ListAvailableTrackerRulesResponse200OutputCompanyRulesItemConfig,
        )
        from ..models.list_available_tracker_rules_response_200_output_company_rules_item_signal import (
            ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal,
        )

        d = dict(src_dict)
        name = d.pop("name")

        readable_name = d.pop("readableName")

        entity_type = ListAvailableTrackerRulesResponse200OutputCompanyRulesItemEntityType(d.pop("entityType"))

        description = d.pop("description")

        use_case = d.pop("useCase")

        supports_initial_signals = d.pop("supportsInitialSignals")

        config = ListAvailableTrackerRulesResponse200OutputCompanyRulesItemConfig.from_dict(d.pop("config"))

        signal = ListAvailableTrackerRulesResponse200OutputCompanyRulesItemSignal.from_dict(d.pop("signal"))

        list_available_tracker_rules_response_200_output_company_rules_item = cls(
            name=name,
            readable_name=readable_name,
            entity_type=entity_type,
            description=description,
            use_case=use_case,
            supports_initial_signals=supports_initial_signals,
            config=config,
            signal=signal,
        )

        list_available_tracker_rules_response_200_output_company_rules_item.additional_properties = d
        return list_available_tracker_rules_response_200_output_company_rules_item

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
