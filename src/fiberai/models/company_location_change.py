from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_location_change_change_type_type_1 import CompanyLocationChangeChangeTypeType1
from ..models.company_location_change_change_type_type_2_type_1 import CompanyLocationChangeChangeTypeType2Type1
from ..models.company_location_change_change_type_type_3_type_1 import CompanyLocationChangeChangeTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_location_change_coordinates_type_0 import CompanyLocationChangeCoordinatesType0


T = TypeVar("T", bound="CompanyLocationChange")


@_attrs_define
class CompanyLocationChange:
    """
    Attributes:
        city (None | str | Unset): City name
        state (None | str | Unset): State or province
        country (None | str | Unset): Country name
        country_code (None | str | Unset): ISO country code
        coordinates (CompanyLocationChangeCoordinatesType0 | None | Unset): Geocoded coordinates, when known
        street_address (None | str | Unset): Street address of the office
        postal_code (None | str | Unset): Postal or ZIP code
        change_type (CompanyLocationChangeChangeTypeType1 | CompanyLocationChangeChangeTypeType2Type1 |
            CompanyLocationChangeChangeTypeType3Type1 | None | Unset): Marks a location as newly added. New office alerts
            report only net-new locations, so this is always 'added'; the field is unset in other location signals.
    """

    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    coordinates: CompanyLocationChangeCoordinatesType0 | None | Unset = UNSET
    street_address: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    change_type: (
        CompanyLocationChangeChangeTypeType1
        | CompanyLocationChangeChangeTypeType2Type1
        | CompanyLocationChangeChangeTypeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_location_change_coordinates_type_0 import (
            CompanyLocationChangeCoordinatesType0,  # noqa: PLC0415
        )

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, CompanyLocationChangeCoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        street_address: None | str | Unset
        if isinstance(self.street_address, Unset):
            street_address = UNSET
        else:
            street_address = self.street_address

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        change_type: None | str | Unset
        if isinstance(self.change_type, Unset):
            change_type = UNSET
        elif isinstance(self.change_type, CompanyLocationChangeChangeTypeType1):
            change_type = self.change_type.value
        elif isinstance(self.change_type, CompanyLocationChangeChangeTypeType2Type1):
            change_type = self.change_type.value
        elif isinstance(self.change_type, CompanyLocationChangeChangeTypeType3Type1):
            change_type = self.change_type.value
        else:
            change_type = self.change_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if change_type is not UNSET:
            field_dict["changeType"] = change_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_location_change_coordinates_type_0 import (
            CompanyLocationChangeCoordinatesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_coordinates(data: object) -> CompanyLocationChangeCoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = CompanyLocationChangeCoordinatesType0.from_dict(data)

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLocationChangeCoordinatesType0 | None | Unset, data)

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_street_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_address = _parse_street_address(d.pop("streetAddress", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))

        def _parse_change_type(
            data: object,
        ) -> (
            CompanyLocationChangeChangeTypeType1
            | CompanyLocationChangeChangeTypeType2Type1
            | CompanyLocationChangeChangeTypeType3Type1
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
                change_type_type_1 = CompanyLocationChangeChangeTypeType1(data)

                return change_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                change_type_type_2_type_1 = CompanyLocationChangeChangeTypeType2Type1(data)

                return change_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                change_type_type_3_type_1 = CompanyLocationChangeChangeTypeType3Type1(data)

                return change_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyLocationChangeChangeTypeType1
                | CompanyLocationChangeChangeTypeType2Type1
                | CompanyLocationChangeChangeTypeType3Type1
                | None
                | Unset,
                data,
            )

        change_type = _parse_change_type(d.pop("changeType", UNSET))

        company_location_change = cls(
            city=city,
            state=state,
            country=country,
            country_code=country_code,
            coordinates=coordinates,
            street_address=street_address,
            postal_code=postal_code,
            change_type=change_type,
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
