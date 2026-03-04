from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0





T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItem")



@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItem:
    """ 
        Attributes:
            address (Union[None, Unset, str]):
            is_primary (Union[None, Unset, bool]):
            location (Union['SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLoca
                tionType0', None, Unset]):
     """

    address: Union[None, Unset, str] = UNSET
    is_primary: Union[None, Unset, bool] = UNSET
    location: Union['SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0
        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        is_primary: Union[None, Unset, bool]
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0
        d = dict(src_dict)
        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_is_primary(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_primary = _parse_is_primary(d.pop("is_primary", UNSET))


        def _parse_location(data: object) -> Union['SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0.from_dict(data)



                return location_type_0
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchResponse200OutputCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0', None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))


        sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item = cls(
            address=address,
            is_primary=is_primary,
            location=location,
        )


        sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item.additional_properties = d
        return sync_combined_search_response_200_output_companies_item_num_matching_locations_type_0_matched_offices_item

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
