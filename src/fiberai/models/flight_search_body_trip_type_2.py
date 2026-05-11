from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_search_body_trip_type_2_flight_type import FlightSearchBodyTripType2FlightType

if TYPE_CHECKING:
    from ..models.flight_search_body_trip_type_2_segments_item import FlightSearchBodyTripType2SegmentsItem


T = TypeVar("T", bound="FlightSearchBodyTripType2")


@_attrs_define
class FlightSearchBodyTripType2:
    """
    Attributes:
        flight_type (FlightSearchBodyTripType2FlightType):
        segments (list[FlightSearchBodyTripType2SegmentsItem]): Provide between 2 and 5 segments.
    """

    flight_type: FlightSearchBodyTripType2FlightType
    segments: list[FlightSearchBodyTripType2SegmentsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flight_type = self.flight_type.value

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flightType": flight_type,
                "segments": segments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_body_trip_type_2_segments_item import FlightSearchBodyTripType2SegmentsItem

        d = dict(src_dict)
        flight_type = FlightSearchBodyTripType2FlightType(d.pop("flightType"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = FlightSearchBodyTripType2SegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        flight_search_body_trip_type_2 = cls(
            flight_type=flight_type,
            segments=segments,
        )

        flight_search_body_trip_type_2.additional_properties = d
        return flight_search_body_trip_type_2

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
