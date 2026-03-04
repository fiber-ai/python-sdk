from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_regions_response_200_output_regions_item import GetRegionsResponse200OutputRegionsItem
  from ..models.get_regions_response_200_output_countries_item import GetRegionsResponse200OutputCountriesItem





T = TypeVar("T", bound="GetRegionsResponse200Output")



@_attrs_define
class GetRegionsResponse200Output:
    """ 
        Attributes:
            countries (list['GetRegionsResponse200OutputCountriesItem']):
            regions (list['GetRegionsResponse200OutputRegionsItem']):
     """

    countries: list['GetRegionsResponse200OutputCountriesItem']
    regions: list['GetRegionsResponse200OutputRegionsItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_regions_response_200_output_regions_item import GetRegionsResponse200OutputRegionsItem
        from ..models.get_regions_response_200_output_countries_item import GetRegionsResponse200OutputCountriesItem
        countries = []
        for countries_item_data in self.countries:
            countries_item = countries_item_data.to_dict()
            countries.append(countries_item)



        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "countries": countries,
            "regions": regions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_regions_response_200_output_regions_item import GetRegionsResponse200OutputRegionsItem
        from ..models.get_regions_response_200_output_countries_item import GetRegionsResponse200OutputCountriesItem
        d = dict(src_dict)
        countries = []
        _countries = d.pop("countries")
        for countries_item_data in (_countries):
            countries_item = GetRegionsResponse200OutputCountriesItem.from_dict(countries_item_data)



            countries.append(countries_item)


        regions = []
        _regions = d.pop("regions")
        for regions_item_data in (_regions):
            regions_item = GetRegionsResponse200OutputRegionsItem.from_dict(regions_item_data)



            regions.append(regions_item)


        get_regions_response_200_output = cls(
            countries=countries,
            regions=regions,
        )


        get_regions_response_200_output.additional_properties = d
        return get_regions_response_200_output

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
