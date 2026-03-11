from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_regions_response_200_output_regions_item_countries_item import (
        GetRegionsResponse200OutputRegionsItemCountriesItem,
    )


T = TypeVar("T", bound="GetRegionsResponse200OutputRegionsItem")


@_attrs_define
class GetRegionsResponse200OutputRegionsItem:
    """A multi-country region, as defined by Fiber AI.

    Attributes:
        name (str): The common name of the region
        api_code (str): The code you need to use to filter by this region in our API
        countries (list[GetRegionsResponse200OutputRegionsItemCountriesItem]): List of countries that we say belong in
            the region
        acronym (None | str | Unset): Short form, if applicable
        flag (str | Unset): Unicode flag emoji for the region; mostly for cosmetic purposes
    """

    name: str
    api_code: str
    countries: list[GetRegionsResponse200OutputRegionsItemCountriesItem]
    acronym: None | str | Unset = UNSET
    flag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        api_code = self.api_code

        countries = []
        for countries_item_data in self.countries:
            countries_item = countries_item_data.to_dict()
            countries.append(countries_item)

        acronym: None | str | Unset
        if isinstance(self.acronym, Unset):
            acronym = UNSET
        else:
            acronym = self.acronym

        flag = self.flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "apiCode": api_code,
                "countries": countries,
            }
        )
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if flag is not UNSET:
            field_dict["flag"] = flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_regions_response_200_output_regions_item_countries_item import (
            GetRegionsResponse200OutputRegionsItemCountriesItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        api_code = d.pop("apiCode")

        countries = []
        _countries = d.pop("countries")
        for countries_item_data in _countries:
            countries_item = GetRegionsResponse200OutputRegionsItemCountriesItem.from_dict(countries_item_data)

            countries.append(countries_item)

        def _parse_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acronym = _parse_acronym(d.pop("acronym", UNSET))

        flag = d.pop("flag", UNSET)

        get_regions_response_200_output_regions_item = cls(
            name=name,
            api_code=api_code,
            countries=countries,
            acronym=acronym,
            flag=flag,
        )

        get_regions_response_200_output_regions_item.additional_properties = d
        return get_regions_response_200_output_regions_item

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
