from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_company_search_response_200_output_search_params_accelerators_v2_type_0_any_of_type_0_item_batch_selection_type_0_strategy import (
    TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0Strategy,
)

T = TypeVar(
    "T", bound="TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0"
)


@_attrs_define
class TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0:
    """
    Attributes:
        strategy
            (TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0Strategy):
    """

    strategy: (
        TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0Strategy
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0AnyOfType0ItemBatchSelectionType0Strategy(
            d.pop("strategy")
        )

        text_to_company_search_response_200_output_search_params_accelerators_v2_type_0_any_of_type_0_item_batch_selection_type_0 = cls(
            strategy=strategy,
        )

        text_to_company_search_response_200_output_search_params_accelerators_v2_type_0_any_of_type_0_item_batch_selection_type_0.additional_properties = d
        return text_to_company_search_response_200_output_search_params_accelerators_v2_type_0_any_of_type_0_item_batch_selection_type_0

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
