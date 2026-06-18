from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.company_location_change_coordinates_type_0 import CompanyLocationChangeCoordinatesType0


T = TypeVar("T", bound="CompanyLocationChange")


@_attrs_define
class CompanyLocationChange:
    """
    Attributes:
        city (None | str): City name
        state (None | str): State or province
        country (None | str): Country name
        country_code (None | str): ISO country code
        coordinates (CompanyLocationChangeCoordinatesType0 | None): Geocoded coordinates, when known
    """

    city: None | str
    state: None | str
    country: None | str
    country_code: None | str
    coordinates: CompanyLocationChangeCoordinatesType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_location_change_coordinates_type_0 import CompanyLocationChangeCoordinatesType0

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        country: None | str
        country = self.country

        country_code: None | str
        country_code = self.country_code

        coordinates: dict[str, Any] | None
        if isinstance(self.coordinates, CompanyLocationChangeCoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "state": state,
                "country": country,
                "countryCode": country_code,
                "coordinates": coordinates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_location_change_coordinates_type_0 import CompanyLocationChangeCoordinatesType0

        d = dict(src_dict)

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("countryCode"))

        def _parse_coordinates(data: object) -> CompanyLocationChangeCoordinatesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = CompanyLocationChangeCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLocationChangeCoordinatesType0 | None, data)

        coordinates = _parse_coordinates(d.pop("coordinates"))

        company_location_change = cls(
            city=city,
            state=state,
            country=country,
            country_code=country_code,
            coordinates=coordinates,
        )

        company_location_change.additional_properties = d
        return company_location_change

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
