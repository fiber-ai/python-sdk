from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_search_response_200_output_price_insights_type_0_price_level_type_1 import (
    FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1,
)
from ..models.flight_search_response_200_output_price_insights_type_0_price_level_type_2_type_1 import (
    FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1,
)
from ..models.flight_search_response_200_output_price_insights_type_0_price_level_type_3_type_1 import (
    FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_response_200_output_price_insights_type_0_history_item import (
        FlightSearchResponse200OutputPriceInsightsType0HistoryItem,
    )
    from ..models.flight_search_response_200_output_price_insights_type_0_typical_price_range_type_0 import (
        FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0,
    )


T = TypeVar("T", bound="FlightSearchResponse200OutputPriceInsightsType0")


@_attrs_define
class FlightSearchResponse200OutputPriceInsightsType0:
    """Price-insight summary for this route query.

    Attributes:
        history (list[FlightSearchResponse200OutputPriceInsightsType0HistoryItem]): Historical prices for this route.
        lowest_price (int | None | Unset): Lowest observed price for this query.
        price_level (FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1 |
            FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1 |
            FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1 | None | Unset): How the current price
            compares to historical prices for this route.
        typical_price_range (FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0 | None | Unset):
            Typical price range for this route in whole currency units.
    """

    history: list[FlightSearchResponse200OutputPriceInsightsType0HistoryItem]
    lowest_price: int | None | Unset = UNSET
    price_level: (
        FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1
        | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1
        | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1
        | None
        | Unset
    ) = UNSET
    typical_price_range: FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_response_200_output_price_insights_type_0_typical_price_range_type_0 import (
            FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0,  # noqa: PLC0415
        )

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        lowest_price: int | None | Unset
        if isinstance(self.lowest_price, Unset):
            lowest_price = UNSET
        else:
            lowest_price = self.lowest_price

        price_level: None | str | Unset
        if isinstance(self.price_level, Unset):
            price_level = UNSET
        elif isinstance(self.price_level, FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1):
            price_level = self.price_level.value
        elif isinstance(self.price_level, FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1):
            price_level = self.price_level.value
        elif isinstance(self.price_level, FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1):
            price_level = self.price_level.value
        else:
            price_level = self.price_level

        typical_price_range: dict[str, Any] | None | Unset
        if isinstance(self.typical_price_range, Unset):
            typical_price_range = UNSET
        elif isinstance(
            self.typical_price_range, FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0
        ):
            typical_price_range = self.typical_price_range.to_dict()
        else:
            typical_price_range = self.typical_price_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history": history,
            }
        )
        if lowest_price is not UNSET:
            field_dict["lowestPrice"] = lowest_price
        if price_level is not UNSET:
            field_dict["priceLevel"] = price_level
        if typical_price_range is not UNSET:
            field_dict["typicalPriceRange"] = typical_price_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_response_200_output_price_insights_type_0_history_item import (
            FlightSearchResponse200OutputPriceInsightsType0HistoryItem,  # noqa: PLC0415
        )
        from ..models.flight_search_response_200_output_price_insights_type_0_typical_price_range_type_0 import (
            FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = FlightSearchResponse200OutputPriceInsightsType0HistoryItem.from_dict(history_item_data)

            history.append(history_item)

        def _parse_lowest_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lowest_price = _parse_lowest_price(d.pop("lowestPrice", UNSET))

        def _parse_price_level(
            data: object,
        ) -> (
            FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1
            | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1
            | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_level_type_1 = FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1(data)

                return price_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_level_type_2_type_1 = FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1(data)

                return price_level_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_level_type_3_type_1 = FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1(data)

                return price_level_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FlightSearchResponse200OutputPriceInsightsType0PriceLevelType1
                | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1
                | FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1
                | None
                | Unset,
                data,
            )

        price_level = _parse_price_level(d.pop("priceLevel", UNSET))

        def _parse_typical_price_range(
            data: object,
        ) -> FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                typical_price_range_type_0 = (
                    FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0.from_dict(data)
                )

                return typical_price_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchResponse200OutputPriceInsightsType0TypicalPriceRangeType0 | None | Unset, data)

        typical_price_range = _parse_typical_price_range(d.pop("typicalPriceRange", UNSET))

        flight_search_response_200_output_price_insights_type_0 = cls(
            history=history,
            lowest_price=lowest_price,
            price_level=price_level,
            typical_price_range=typical_price_range,
        )

        flight_search_response_200_output_price_insights_type_0.additional_properties = d
        return flight_search_response_200_output_price_insights_type_0

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
