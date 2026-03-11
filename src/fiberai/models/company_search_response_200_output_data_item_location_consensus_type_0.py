from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_response_200_output_data_item_location_consensus_type_0_coordinates_type_0 import (
        CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0,
    )


T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemLocationConsensusType0")


@_attrs_define
class CompanySearchResponse200OutputDataItemLocationConsensusType0:
    """
    Attributes:
        street_address (None | str | Unset):
        neighborhood (None | str | Unset):
        city (None | str | Unset):
        state_name (None | str | Unset):
        state_code (None | str | Unset):
        county (None | str | Unset):
        postal_code (None | str | Unset):
        country_code (None | str | Unset):
        country_name (None | str | Unset):
        coordinates (CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0 | None | Unset):
        timezone (None | str | Unset):
        full_address (None | str | Unset):
        formatted_address (None | str | Unset):
    """

    street_address: None | str | Unset = UNSET
    neighborhood: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state_name: None | str | Unset = UNSET
    state_code: None | str | Unset = UNSET
    county: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    country_name: None | str | Unset = UNSET
    coordinates: CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0 | None | Unset = UNSET
    timezone: None | str | Unset = UNSET
    full_address: None | str | Unset = UNSET
    formatted_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_response_200_output_data_item_location_consensus_type_0_coordinates_type_0 import (
            CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0,
        )

        street_address: None | str | Unset
        if isinstance(self.street_address, Unset):
            street_address = UNSET
        else:
            street_address = self.street_address

        neighborhood: None | str | Unset
        if isinstance(self.neighborhood, Unset):
            neighborhood = UNSET
        else:
            neighborhood = self.neighborhood

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state_name: None | str | Unset
        if isinstance(self.state_name, Unset):
            state_name = UNSET
        else:
            state_name = self.state_name

        state_code: None | str | Unset
        if isinstance(self.state_code, Unset):
            state_code = UNSET
        else:
            state_code = self.state_code

        county: None | str | Unset
        if isinstance(self.county, Unset):
            county = UNSET
        else:
            county = self.county

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        coordinates: dict[str, Any] | None | Unset
        if isinstance(self.coordinates, Unset):
            coordinates = UNSET
        elif isinstance(self.coordinates, CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0):
            coordinates = self.coordinates.to_dict()
        else:
            coordinates = self.coordinates

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        full_address: None | str | Unset
        if isinstance(self.full_address, Unset):
            full_address = UNSET
        else:
            full_address = self.full_address

        formatted_address: None | str | Unset
        if isinstance(self.formatted_address, Unset):
            formatted_address = UNSET
        else:
            formatted_address = self.formatted_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street_address is not UNSET:
            field_dict["street_address"] = street_address
        if neighborhood is not UNSET:
            field_dict["neighborhood"] = neighborhood
        if city is not UNSET:
            field_dict["city"] = city
        if state_name is not UNSET:
            field_dict["state_name"] = state_name
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if county is not UNSET:
            field_dict["county"] = county
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if formatted_address is not UNSET:
            field_dict["formatted_address"] = formatted_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_location_consensus_type_0_coordinates_type_0 import (
            CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0,
        )

        d = dict(src_dict)

        def _parse_street_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_address = _parse_street_address(d.pop("street_address", UNSET))

        def _parse_neighborhood(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        neighborhood = _parse_neighborhood(d.pop("neighborhood", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_name = _parse_state_name(d.pop("state_name", UNSET))

        def _parse_state_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_code = _parse_state_code(d.pop("state_code", UNSET))

        def _parse_county(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        county = _parse_county(d.pop("county", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("country_name", UNSET))

        def _parse_coordinates(
            data: object,
        ) -> CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coordinates_type_0 = (
                    CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0.from_dict(data)
                )

                return coordinates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchResponse200OutputDataItemLocationConsensusType0CoordinatesType0 | None | Unset, data
            )

        coordinates = _parse_coordinates(d.pop("coordinates", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_full_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_address = _parse_full_address(d.pop("full_address", UNSET))

        def _parse_formatted_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_address = _parse_formatted_address(d.pop("formatted_address", UNSET))

        company_search_response_200_output_data_item_location_consensus_type_0 = cls(
            street_address=street_address,
            neighborhood=neighborhood,
            city=city,
            state_name=state_name,
            state_code=state_code,
            county=county,
            postal_code=postal_code,
            country_code=country_code,
            country_name=country_name,
            coordinates=coordinates,
            timezone=timezone,
            full_address=full_address,
            formatted_address=formatted_address,
        )

        company_search_response_200_output_data_item_location_consensus_type_0.additional_properties = d
        return company_search_response_200_output_data_item_location_consensus_type_0

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
