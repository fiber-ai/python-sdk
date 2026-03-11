from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_search_body_strategy_type_1_strategy import GoogleMapsSearchBodyStrategyType1Strategy

if TYPE_CHECKING:
    from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0 import (
        GoogleMapsSearchBodyStrategyType1UnionAllItemType0,
    )
    from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1 import (
        GoogleMapsSearchBodyStrategyType1UnionAllItemType1,
    )


T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType1")


@_attrs_define
class GoogleMapsSearchBodyStrategyType1:
    """
    Attributes:
        strategy (GoogleMapsSearchBodyStrategyType1Strategy): Use 'specific-areas' to search for places in specific
            areas
        union_all (list[GoogleMapsSearchBodyStrategyType1UnionAllItemType0 |
            GoogleMapsSearchBodyStrategyType1UnionAllItemType1]): An array of region definitions (rectangles and/or
            circles). All regions in this array will be unioned together to form the total search area.
    """

    strategy: GoogleMapsSearchBodyStrategyType1Strategy
    union_all: list[
        GoogleMapsSearchBodyStrategyType1UnionAllItemType0 | GoogleMapsSearchBodyStrategyType1UnionAllItemType1
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0 import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType0,
        )

        strategy = self.strategy.value

        union_all = []
        for union_all_item_data in self.union_all:
            union_all_item: dict[str, Any]
            if isinstance(union_all_item_data, GoogleMapsSearchBodyStrategyType1UnionAllItemType0):
                union_all_item = union_all_item_data.to_dict()
            else:
                union_all_item = union_all_item_data.to_dict()

            union_all.append(union_all_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "unionAll": union_all,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0 import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType0,
        )
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1 import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType1,
        )

        d = dict(src_dict)
        strategy = GoogleMapsSearchBodyStrategyType1Strategy(d.pop("strategy"))

        union_all = []
        _union_all = d.pop("unionAll")
        for union_all_item_data in _union_all:

            def _parse_union_all_item(
                data: object,
            ) -> (
                GoogleMapsSearchBodyStrategyType1UnionAllItemType0 | GoogleMapsSearchBodyStrategyType1UnionAllItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    union_all_item_type_0 = GoogleMapsSearchBodyStrategyType1UnionAllItemType0.from_dict(data)

                    return union_all_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                union_all_item_type_1 = GoogleMapsSearchBodyStrategyType1UnionAllItemType1.from_dict(data)

                return union_all_item_type_1

            union_all_item = _parse_union_all_item(union_all_item_data)

            union_all.append(union_all_item)

        google_maps_search_body_strategy_type_1 = cls(
            strategy=strategy,
            union_all=union_all,
        )

        google_maps_search_body_strategy_type_1.additional_properties = d
        return google_maps_search_body_strategy_type_1

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
