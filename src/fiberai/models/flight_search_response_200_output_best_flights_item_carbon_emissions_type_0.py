from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchResponse200OutputBestFlightsItemCarbonEmissionsType0")


@_attrs_define
class FlightSearchResponse200OutputBestFlightsItemCarbonEmissionsType0:
    """Carbon emissions summary for this itinerary.

    Attributes:
        this_flight_kg (int | None | Unset): Estimated emissions for this itinerary in kilograms.
        typical_for_route_kg (int | None | Unset): Typical route emissions in kilograms.
        difference_percent (float | None | Unset): Percent difference versus typical route emissions. Negative means
            lower than typical, positive means higher.
    """

    this_flight_kg: int | None | Unset = UNSET
    typical_for_route_kg: int | None | Unset = UNSET
    difference_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        this_flight_kg: int | None | Unset
        if isinstance(self.this_flight_kg, Unset):
            this_flight_kg = UNSET
        else:
            this_flight_kg = self.this_flight_kg

        typical_for_route_kg: int | None | Unset
        if isinstance(self.typical_for_route_kg, Unset):
            typical_for_route_kg = UNSET
        else:
            typical_for_route_kg = self.typical_for_route_kg

        difference_percent: float | None | Unset
        if isinstance(self.difference_percent, Unset):
            difference_percent = UNSET
        else:
            difference_percent = self.difference_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if this_flight_kg is not UNSET:
            field_dict["thisFlightKg"] = this_flight_kg
        if typical_for_route_kg is not UNSET:
            field_dict["typicalForRouteKg"] = typical_for_route_kg
        if difference_percent is not UNSET:
            field_dict["differencePercent"] = difference_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_this_flight_kg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        this_flight_kg = _parse_this_flight_kg(d.pop("thisFlightKg", UNSET))

        def _parse_typical_for_route_kg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        typical_for_route_kg = _parse_typical_for_route_kg(d.pop("typicalForRouteKg", UNSET))

        def _parse_difference_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        difference_percent = _parse_difference_percent(d.pop("differencePercent", UNSET))

        flight_search_response_200_output_best_flights_item_carbon_emissions_type_0 = cls(
            this_flight_kg=this_flight_kg,
            typical_for_route_kg=typical_for_route_kg,
            difference_percent=difference_percent,
        )

        flight_search_response_200_output_best_flights_item_carbon_emissions_type_0.additional_properties = d
        return flight_search_response_200_output_best_flights_item_carbon_emissions_type_0

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
