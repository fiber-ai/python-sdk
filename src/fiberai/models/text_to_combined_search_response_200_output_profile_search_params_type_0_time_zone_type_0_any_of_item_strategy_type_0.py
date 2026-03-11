from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0_any_of_item_strategy_type_0_mode import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0Mode,
)

T = TypeVar(
    "T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0"
)


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0:
    """
    Attributes:
        mode (TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0Mode):
        midpoint_time_zone_name (str):
        max_minutes_westward (int):
        max_minutes_eastward (float):
        include_partial_year_matches (bool):
    """

    mode: TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0Mode
    midpoint_time_zone_name: str
    max_minutes_westward: int
    max_minutes_eastward: float
    include_partial_year_matches: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        midpoint_time_zone_name = self.midpoint_time_zone_name

        max_minutes_westward = self.max_minutes_westward

        max_minutes_eastward = self.max_minutes_eastward

        include_partial_year_matches = self.include_partial_year_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "midpointTimeZoneName": midpoint_time_zone_name,
                "maxMinutesWestward": max_minutes_westward,
                "maxMinutesEastward": max_minutes_eastward,
                "includePartialYearMatches": include_partial_year_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = TextToCombinedSearchResponse200OutputProfileSearchParamsType0TimeZoneType0AnyOfItemStrategyType0Mode(
            d.pop("mode")
        )

        midpoint_time_zone_name = d.pop("midpointTimeZoneName")

        max_minutes_westward = d.pop("maxMinutesWestward")

        max_minutes_eastward = d.pop("maxMinutesEastward")

        include_partial_year_matches = d.pop("includePartialYearMatches")

        text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0_any_of_item_strategy_type_0 = cls(
            mode=mode,
            midpoint_time_zone_name=midpoint_time_zone_name,
            max_minutes_westward=max_minutes_westward,
            max_minutes_eastward=max_minutes_eastward,
            include_partial_year_matches=include_partial_year_matches,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0_any_of_item_strategy_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_time_zone_type_0_any_of_item_strategy_type_0

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
