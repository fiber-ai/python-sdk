from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_location_change import CompanyLocationChange


T = TypeVar("T", bound="LocationDeltaChange")


@_attrs_define
class LocationDeltaChange:
    """
    Attributes:
        kind (Literal['location']):
        previous (CompanyLocationChange | None):
        current (CompanyLocationChange | None):
        country_changed (bool):
        state_changed (bool):
        city_changed (bool):
        distance_miles (float | None | Unset): Distance moved in miles, when both locations are geocoded
    """

    kind: Literal["location"]
    previous: CompanyLocationChange | None
    current: CompanyLocationChange | None
    country_changed: bool
    state_changed: bool
    city_changed: bool
    distance_miles: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_location_change import CompanyLocationChange

        kind = self.kind

        previous: dict[str, Any] | None
        if isinstance(self.previous, CompanyLocationChange):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        current: dict[str, Any] | None
        if isinstance(self.current, CompanyLocationChange):
            current = self.current.to_dict()
        else:
            current = self.current

        country_changed = self.country_changed

        state_changed = self.state_changed

        city_changed = self.city_changed

        distance_miles: float | None | Unset
        if isinstance(self.distance_miles, Unset):
            distance_miles = UNSET
        else:
            distance_miles = self.distance_miles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "previous": previous,
                "current": current,
                "countryChanged": country_changed,
                "stateChanged": state_changed,
                "cityChanged": city_changed,
            }
        )
        if distance_miles is not UNSET:
            field_dict["distanceMiles"] = distance_miles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_location_change import CompanyLocationChange

        d = dict(src_dict)
        kind = cast(Literal["location"], d.pop("kind"))
        if kind != "location":
            raise ValueError(f"kind must match const 'location', got '{kind}'")

        def _parse_previous(data: object) -> CompanyLocationChange | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = CompanyLocationChange.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLocationChange | None, data)

        previous = _parse_previous(d.pop("previous"))

        def _parse_current(data: object) -> CompanyLocationChange | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = CompanyLocationChange.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLocationChange | None, data)

        current = _parse_current(d.pop("current"))

        country_changed = d.pop("countryChanged")

        state_changed = d.pop("stateChanged")

        city_changed = d.pop("cityChanged")

        def _parse_distance_miles(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_miles = _parse_distance_miles(d.pop("distanceMiles", UNSET))

        location_delta_change = cls(
            kind=kind,
            previous=previous,
            current=current,
            country_changed=country_changed,
            state_changed=state_changed,
            city_changed=city_changed,
            distance_miles=distance_miles,
        )

        location_delta_change.additional_properties = d
        return location_delta_change

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
