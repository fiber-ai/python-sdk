from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_max_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_min_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0,
    )


T = TypeVar("T", bound="FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0")


@_attrs_define
class FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0:
    """Base-rent range in USD and local currency.

    Attributes:
        min_ (FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0 | None | Unset): Minimum base
            rent in USD and local currency.
        max_ (FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0 | None | Unset): Maximum base
            rent in USD and local currency.
    """

    min_: FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0 | None | Unset = UNSET
    max_: FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_max_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_min_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0,  # noqa: PLC0415
        )

        min_: dict[str, Any] | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        elif isinstance(self.min_, FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0):
            min_ = self.min_.to_dict()
        else:
            min_ = self.min_

        max_: dict[str, Any] | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        elif isinstance(self.max_, FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0):
            max_ = self.max_.to_dict()
        else:
            max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_max_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0_min_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_min_(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                min_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0.from_dict(data)

                return min_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MinType0 | None | Unset, data
            )

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0.from_dict(data)

                return max_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0MaxType0 | None | Unset, data
            )

        max_ = _parse_max_(d.pop("max", UNSET))

        fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0 = cls(
            min_=min_,
            max_=max_,
        )

        fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0.additional_properties = d
        return fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0

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
