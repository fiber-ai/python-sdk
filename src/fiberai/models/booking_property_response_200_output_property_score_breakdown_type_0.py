from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingPropertyResponse200OutputPropertyScoreBreakdownType0")


@_attrs_define
class BookingPropertyResponse200OutputPropertyScoreBreakdownType0:
    """Guest review scores by category, each from 0 to 10.

    Attributes:
        staff (float | None | Unset): Staff score from 0 to 10.
        facilities (float | None | Unset): Facilities score from 0 to 10.
        cleanliness (float | None | Unset): Cleanliness score from 0 to 10.
        comfort (float | None | Unset): Comfort score from 0 to 10.
        value (float | None | Unset): Value-for-money score from 0 to 10.
        location (float | None | Unset): Location score from 0 to 10.
        breakfast (float | None | Unset): Breakfast score from 0 to 10.
        wifi (float | None | Unset): Wi-Fi score from 0 to 10.
    """

    staff: float | None | Unset = UNSET
    facilities: float | None | Unset = UNSET
    cleanliness: float | None | Unset = UNSET
    comfort: float | None | Unset = UNSET
    value: float | None | Unset = UNSET
    location: float | None | Unset = UNSET
    breakfast: float | None | Unset = UNSET
    wifi: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        staff: float | None | Unset
        if isinstance(self.staff, Unset):
            staff = UNSET
        else:
            staff = self.staff

        facilities: float | None | Unset
        if isinstance(self.facilities, Unset):
            facilities = UNSET
        else:
            facilities = self.facilities

        cleanliness: float | None | Unset
        if isinstance(self.cleanliness, Unset):
            cleanliness = UNSET
        else:
            cleanliness = self.cleanliness

        comfort: float | None | Unset
        if isinstance(self.comfort, Unset):
            comfort = UNSET
        else:
            comfort = self.comfort

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        location: float | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        breakfast: float | None | Unset
        if isinstance(self.breakfast, Unset):
            breakfast = UNSET
        else:
            breakfast = self.breakfast

        wifi: float | None | Unset
        if isinstance(self.wifi, Unset):
            wifi = UNSET
        else:
            wifi = self.wifi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if staff is not UNSET:
            field_dict["staff"] = staff
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if cleanliness is not UNSET:
            field_dict["cleanliness"] = cleanliness
        if comfort is not UNSET:
            field_dict["comfort"] = comfort
        if value is not UNSET:
            field_dict["value"] = value
        if location is not UNSET:
            field_dict["location"] = location
        if breakfast is not UNSET:
            field_dict["breakfast"] = breakfast
        if wifi is not UNSET:
            field_dict["wifi"] = wifi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_staff(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        staff = _parse_staff(d.pop("staff", UNSET))

        def _parse_facilities(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        facilities = _parse_facilities(d.pop("facilities", UNSET))

        def _parse_cleanliness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cleanliness = _parse_cleanliness(d.pop("cleanliness", UNSET))

        def _parse_comfort(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        comfort = _parse_comfort(d.pop("comfort", UNSET))

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_location(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_breakfast(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        breakfast = _parse_breakfast(d.pop("breakfast", UNSET))

        def _parse_wifi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wifi = _parse_wifi(d.pop("wifi", UNSET))

        booking_property_response_200_output_property_score_breakdown_type_0 = cls(
            staff=staff,
            facilities=facilities,
            cleanliness=cleanliness,
            comfort=comfort,
            value=value,
            location=location,
            breakfast=breakfast,
            wifi=wifi,
        )

        booking_property_response_200_output_property_score_breakdown_type_0.additional_properties = d
        return booking_property_response_200_output_property_score_breakdown_type_0

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
