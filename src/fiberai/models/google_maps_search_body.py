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
        name (None | str | Unset): An optional name for the project for reference purposes.
        query (None | str | Unset): The search query to run on Google Maps. Do not include a location info here.
            Examples: 'dominos pizza', 'real estate agent'. Omit this when you pass a Google Maps URL instead.
        google_maps_url (None | str | Unset): A link to a Google Maps search, taken from the address bar after
            searching. The search term and the area to search are read from the link. The term is used exactly as it appears
            in the link, so it may name a location even though you should leave locations out of 'query' — the area to
            search comes from the link, not from the term. Omit this when you pass a query and strategy instead.
        max_results (int | Unset): The maximum number of Google Maps results to return. Default: 100.
        strategy (GoogleMapsSearchBodyStrategyType0 | GoogleMapsSearchBodyStrategyType1 |
            GoogleMapsSearchBodyStrategyType2 | None | Unset): The strategy for searching places. Omit this when you pass a
            Google Maps URL instead.
    """

    api_key: str
    name: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    google_maps_url: None | str | Unset = UNSET
    max_results: int | Unset = 100
    strategy: (
        GoogleMapsSearchBodyStrategyType0
        | GoogleMapsSearchBodyStrategyType1
        | GoogleMapsSearchBodyStrategyType2
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_maps_search_body_strategy_type_0 import GoogleMapsSearchBodyStrategyType0  # noqa: PLC0415
        from ..models.google_maps_search_body_strategy_type_1 import GoogleMapsSearchBodyStrategyType1  # noqa: PLC0415
        from ..models.google_maps_search_body_strategy_type_2 import GoogleMapsSearchBodyStrategyType2  # noqa: PLC0415

        api_key = self.api_key

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        google_maps_url: None | str | Unset
        if isinstance(self.google_maps_url, Unset):
            google_maps_url = UNSET
        else:
            google_maps_url = self.google_maps_url

        max_results = self.max_results

        strategy: dict[str, Any] | None | Unset
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        elif isinstance(self.strategy, GoogleMapsSearchBodyStrategyType0):
            strategy = self.strategy.to_dict()
        elif isinstance(self.strategy, GoogleMapsSearchBodyStrategyType1):
            strategy = self.strategy.to_dict()
        elif isinstance(self.strategy, GoogleMapsSearchBodyStrategyType2):
            strategy = self.strategy.to_dict()
        else:
            strategy = self.strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if query is not UNSET:
            field_dict["query"] = query
        if google_maps_url is not UNSET:
            field_dict["googleMapsUrl"] = google_maps_url
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_0 import GoogleMapsSearchBodyStrategyType0  # noqa: PLC0415
        from ..models.google_maps_search_body_strategy_type_1 import GoogleMapsSearchBodyStrategyType1  # noqa: PLC0415
        from ..models.google_maps_search_body_strategy_type_2 import GoogleMapsSearchBodyStrategyType2  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_google_maps_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_maps_url = _parse_google_maps_url(d.pop("googleMapsUrl", UNSET))

        max_results = d.pop("maxResults", UNSET)

        def _parse_strategy(
            data: object,
        ) -> (
            GoogleMapsSearchBodyStrategyType0
            | GoogleMapsSearchBodyStrategyType1
            | GoogleMapsSearchBodyStrategyType2
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                strategy_type_2 = GoogleMapsSearchBodyStrategyType2.from_dict(data)

                return strategy_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GoogleMapsSearchBodyStrategyType0
                | GoogleMapsSearchBodyStrategyType1
                | GoogleMapsSearchBodyStrategyType2
                | None
                | Unset,
                data,
            )

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        google_maps_search_body = cls(
            api_key=api_key,
            name=name,
            query=query,
            google_maps_url=google_maps_url,
            max_results=max_results,
            strategy=strategy,
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
