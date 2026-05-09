from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchRealEstateListingsBodyFeaturesType0")


@_attrs_define
class FetchRealEstateListingsBodyFeaturesType0:
    """Optional property feature filters.

    Attributes:
        has_pool (bool | None | Unset):
        has_garage (bool | None | Unset):
        has_air_conditioning (bool | None | Unset):
        is_waterfront (bool | None | Unset):
        is_single_story (bool | None | Unset):
        has_open_house (bool | None | Unset):
        include_under_contract (bool | None | Unset):
    """

    has_pool: bool | None | Unset = UNSET
    has_garage: bool | None | Unset = UNSET
    has_air_conditioning: bool | None | Unset = UNSET
    is_waterfront: bool | None | Unset = UNSET
    is_single_story: bool | None | Unset = UNSET
    has_open_house: bool | None | Unset = UNSET
    include_under_contract: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_pool: bool | None | Unset
        if isinstance(self.has_pool, Unset):
            has_pool = UNSET
        else:
            has_pool = self.has_pool

        has_garage: bool | None | Unset
        if isinstance(self.has_garage, Unset):
            has_garage = UNSET
        else:
            has_garage = self.has_garage

        has_air_conditioning: bool | None | Unset
        if isinstance(self.has_air_conditioning, Unset):
            has_air_conditioning = UNSET
        else:
            has_air_conditioning = self.has_air_conditioning

        is_waterfront: bool | None | Unset
        if isinstance(self.is_waterfront, Unset):
            is_waterfront = UNSET
        else:
            is_waterfront = self.is_waterfront

        is_single_story: bool | None | Unset
        if isinstance(self.is_single_story, Unset):
            is_single_story = UNSET
        else:
            is_single_story = self.is_single_story

        has_open_house: bool | None | Unset
        if isinstance(self.has_open_house, Unset):
            has_open_house = UNSET
        else:
            has_open_house = self.has_open_house

        include_under_contract: bool | None | Unset
        if isinstance(self.include_under_contract, Unset):
            include_under_contract = UNSET
        else:
            include_under_contract = self.include_under_contract

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_pool is not UNSET:
            field_dict["hasPool"] = has_pool
        if has_garage is not UNSET:
            field_dict["hasGarage"] = has_garage
        if has_air_conditioning is not UNSET:
            field_dict["hasAirConditioning"] = has_air_conditioning
        if is_waterfront is not UNSET:
            field_dict["isWaterfront"] = is_waterfront
        if is_single_story is not UNSET:
            field_dict["isSingleStory"] = is_single_story
        if has_open_house is not UNSET:
            field_dict["hasOpenHouse"] = has_open_house
        if include_under_contract is not UNSET:
            field_dict["includeUnderContract"] = include_under_contract

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_has_pool(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_pool = _parse_has_pool(d.pop("hasPool", UNSET))

        def _parse_has_garage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_garage = _parse_has_garage(d.pop("hasGarage", UNSET))

        def _parse_has_air_conditioning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_air_conditioning = _parse_has_air_conditioning(d.pop("hasAirConditioning", UNSET))

        def _parse_is_waterfront(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_waterfront = _parse_is_waterfront(d.pop("isWaterfront", UNSET))

        def _parse_is_single_story(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_single_story = _parse_is_single_story(d.pop("isSingleStory", UNSET))

        def _parse_has_open_house(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_open_house = _parse_has_open_house(d.pop("hasOpenHouse", UNSET))

        def _parse_include_under_contract(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_under_contract = _parse_include_under_contract(d.pop("includeUnderContract", UNSET))

        fetch_real_estate_listings_body_features_type_0 = cls(
            has_pool=has_pool,
            has_garage=has_garage,
            has_air_conditioning=has_air_conditioning,
            is_waterfront=is_waterfront,
            is_single_story=is_single_story,
            has_open_house=has_open_house,
            include_under_contract=include_under_contract,
        )

        fetch_real_estate_listings_body_features_type_0.additional_properties = d
        return fetch_real_estate_listings_body_features_type_0

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
