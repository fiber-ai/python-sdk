from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_source_search_response_200_output_data_type_1_type import (
    MultiSourceSearchResponse200OutputDataType1Type,
)

if TYPE_CHECKING:
    from ..models.multi_source_search_response_200_output_data_type_1_results_item import (
        MultiSourceSearchResponse200OutputDataType1ResultsItem,
    )


T = TypeVar("T", bound="MultiSourceSearchResponse200OutputDataType1")


@_attrs_define
class MultiSourceSearchResponse200OutputDataType1:
    """
    Attributes:
        type_ (MultiSourceSearchResponse200OutputDataType1Type):
        results (list[MultiSourceSearchResponse200OutputDataType1ResultsItem]): Matched prospects with company info
    """

    type_: MultiSourceSearchResponse200OutputDataType1Type
    results: list[MultiSourceSearchResponse200OutputDataType1ResultsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_source_search_response_200_output_data_type_1_results_item import (
            MultiSourceSearchResponse200OutputDataType1ResultsItem,
        )

        d = dict(src_dict)
        type_ = MultiSourceSearchResponse200OutputDataType1Type(d.pop("type"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = MultiSourceSearchResponse200OutputDataType1ResultsItem.from_dict(results_item_data)

            results.append(results_item)

        multi_source_search_response_200_output_data_type_1 = cls(
            type_=type_,
            results=results,
        )

        multi_source_search_response_200_output_data_type_1.additional_properties = d
        return multi_source_search_response_200_output_data_type_1

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
