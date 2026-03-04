from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0Center")



@_attrs_define
class CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0Center:
    """ 
        Attributes:
            latitude (float):
            longitude (float):
            name (Union[None, Unset, str]):
            address (Union[None, Unset, str]):
     """

    latitude: float
    longitude: float
    name: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "latitude": latitude,
            "longitude": longitude,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))


        combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_center = cls(
            latitude=latitude,
            longitude=longitude,
            name=name,
            address=address,
        )


        combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_center.additional_properties = d
        return combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_center

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
