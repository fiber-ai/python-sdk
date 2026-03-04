from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.google_maps_search_body_strategy_type_2_largest_city_tier_id_type_1 import GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1
from ..models.google_maps_search_body_strategy_type_2_largest_city_tier_id_type_2_type_1 import GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1
from ..models.google_maps_search_body_strategy_type_2_largest_city_tier_id_type_3_type_1 import GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1
from ..models.google_maps_search_body_strategy_type_2_smallest_city_tier_id_type_1 import GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1
from ..models.google_maps_search_body_strategy_type_2_smallest_city_tier_id_type_2_type_1 import GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1
from ..models.google_maps_search_body_strategy_type_2_smallest_city_tier_id_type_3_type_1 import GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1
from ..models.google_maps_search_body_strategy_type_2_strategy import GoogleMapsSearchBodyStrategyType2Strategy
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.google_maps_search_body_strategy_type_2_countries_and_regions import GoogleMapsSearchBodyStrategyType2CountriesAndRegions





T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType2")



@_attrs_define
class GoogleMapsSearchBodyStrategyType2:
    """ 
        Attributes:
            strategy (GoogleMapsSearchBodyStrategyType2Strategy):
            countries_and_regions (GoogleMapsSearchBodyStrategyType2CountriesAndRegions):
            smallest_city_tier_id (Union[GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1,
                GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1,
                GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1, None, Unset]):
            largest_city_tier_id (Union[GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1,
                GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1,
                GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1, None, Unset]):
     """

    strategy: GoogleMapsSearchBodyStrategyType2Strategy
    countries_and_regions: 'GoogleMapsSearchBodyStrategyType2CountriesAndRegions'
    smallest_city_tier_id: Union[GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1, None, Unset] = UNSET
    largest_city_tier_id: Union[GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.google_maps_search_body_strategy_type_2_countries_and_regions import GoogleMapsSearchBodyStrategyType2CountriesAndRegions
        strategy = self.strategy.value

        countries_and_regions = self.countries_and_regions.to_dict()

        smallest_city_tier_id: Union[None, Unset, str]
        if isinstance(self.smallest_city_tier_id, Unset):
            smallest_city_tier_id = UNSET
        elif isinstance(self.smallest_city_tier_id, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1):
            smallest_city_tier_id = self.smallest_city_tier_id.value
        elif isinstance(self.smallest_city_tier_id, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1):
            smallest_city_tier_id = self.smallest_city_tier_id.value
        elif isinstance(self.smallest_city_tier_id, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1):
            smallest_city_tier_id = self.smallest_city_tier_id.value
        else:
            smallest_city_tier_id = self.smallest_city_tier_id

        largest_city_tier_id: Union[None, Unset, str]
        if isinstance(self.largest_city_tier_id, Unset):
            largest_city_tier_id = UNSET
        elif isinstance(self.largest_city_tier_id, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1):
            largest_city_tier_id = self.largest_city_tier_id.value
        elif isinstance(self.largest_city_tier_id, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1):
            largest_city_tier_id = self.largest_city_tier_id.value
        elif isinstance(self.largest_city_tier_id, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1):
            largest_city_tier_id = self.largest_city_tier_id.value
        else:
            largest_city_tier_id = self.largest_city_tier_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
            "countriesAndRegions": countries_and_regions,
        })
        if smallest_city_tier_id is not UNSET:
            field_dict["smallestCityTierID"] = smallest_city_tier_id
        if largest_city_tier_id is not UNSET:
            field_dict["largestCityTierID"] = largest_city_tier_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_2_countries_and_regions import GoogleMapsSearchBodyStrategyType2CountriesAndRegions
        d = dict(src_dict)
        strategy = GoogleMapsSearchBodyStrategyType2Strategy(d.pop("strategy"))




        countries_and_regions = GoogleMapsSearchBodyStrategyType2CountriesAndRegions.from_dict(d.pop("countriesAndRegions"))




        def _parse_smallest_city_tier_id(data: object) -> Union[GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smallest_city_tier_id_type_1 = GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1(data)



                return smallest_city_tier_id_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smallest_city_tier_id_type_2_type_1 = GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1(data)



                return smallest_city_tier_id_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smallest_city_tier_id_type_3_type_1 = GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1(data)



                return smallest_city_tier_id_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType3Type1, None, Unset], data)

        smallest_city_tier_id = _parse_smallest_city_tier_id(d.pop("smallestCityTierID", UNSET))


        def _parse_largest_city_tier_id(data: object) -> Union[GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                largest_city_tier_id_type_1 = GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1(data)



                return largest_city_tier_id_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                largest_city_tier_id_type_2_type_1 = GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1(data)



                return largest_city_tier_id_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                largest_city_tier_id_type_3_type_1 = GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1(data)



                return largest_city_tier_id_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[GoogleMapsSearchBodyStrategyType2LargestCityTierIDType1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1, GoogleMapsSearchBodyStrategyType2LargestCityTierIDType3Type1, None, Unset], data)

        largest_city_tier_id = _parse_largest_city_tier_id(d.pop("largestCityTierID", UNSET))


        google_maps_search_body_strategy_type_2 = cls(
            strategy=strategy,
            countries_and_regions=countries_and_regions,
            smallest_city_tier_id=smallest_city_tier_id,
            largest_city_tier_id=largest_city_tier_id,
        )


        google_maps_search_body_strategy_type_2.additional_properties = d
        return google_maps_search_body_strategy_type_2

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
