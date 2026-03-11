from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_maps_search_body_strategy_type_0 import GoogleMapsSearchBodyStrategyType0
    from ..models.google_maps_search_body_strategy_type_1 import GoogleMapsSearchBodyStrategyType1
    from ..models.google_maps_search_body_strategy_type_2 import GoogleMapsSearchBodyStrategyType2


T = TypeVar("T", bound="GoogleMapsSearchBody")


@_attrs_define
class GoogleMapsSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        query (str): The search query to run on Google Maps. Do not include a location info here. Examples: 'dominos
            pizza', 'real estate agent'.
        strategy (GoogleMapsSearchBodyStrategyType0 | GoogleMapsSearchBodyStrategyType1 |
            GoogleMapsSearchBodyStrategyType2): The strategy by which to search for places.
        name (None | str | Unset): An Optional name for the project for user reference. Not used for anything else.
        max_results (int | Unset): The maximum number of Google Maps results to return. Default: 100.
    """

    api_key: str
    query: str
    strategy: GoogleMapsSearchBodyStrategyType0 | GoogleMapsSearchBodyStrategyType1 | GoogleMapsSearchBodyStrategyType2
    name: None | str | Unset = UNSET
    max_results: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_maps_search_body_strategy_type_0 import GoogleMapsSearchBodyStrategyType0
        from ..models.google_maps_search_body_strategy_type_1 import GoogleMapsSearchBodyStrategyType1

        api_key = self.api_key

        query = self.query

        strategy: dict[str, Any]
        if isinstance(self.strategy, GoogleMapsSearchBodyStrategyType0):
            strategy = self.strategy.to_dict()
        elif isinstance(self.strategy, GoogleMapsSearchBodyStrategyType1):
            strategy = self.strategy.to_dict()
        else:
            strategy = self.strategy.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        max_results = self.max_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "query": query,
                "strategy": strategy,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_0 import GoogleMapsSearchBodyStrategyType0
        from ..models.google_maps_search_body_strategy_type_1 import GoogleMapsSearchBodyStrategyType1
        from ..models.google_maps_search_body_strategy_type_2 import GoogleMapsSearchBodyStrategyType2

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        def _parse_strategy(
            data: object,
        ) -> GoogleMapsSearchBodyStrategyType0 | GoogleMapsSearchBodyStrategyType1 | GoogleMapsSearchBodyStrategyType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                strategy_type_0 = GoogleMapsSearchBodyStrategyType0.from_dict(data)

                return strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                strategy_type_1 = GoogleMapsSearchBodyStrategyType1.from_dict(data)

                return strategy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            strategy_type_2 = GoogleMapsSearchBodyStrategyType2.from_dict(data)

            return strategy_type_2

        strategy = _parse_strategy(d.pop("strategy"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        max_results = d.pop("maxResults", UNSET)

        google_maps_search_body = cls(
            api_key=api_key,
            query=query,
            strategy=strategy,
            name=name,
            max_results=max_results,
        )

        google_maps_search_body.additional_properties = d
        return google_maps_search_body

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
