from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.company_search_response_200_output_data_item_num_matching_locations_type_0_matched_offices_item import CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem





T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemNumMatchingLocationsType0")



@_attrs_define
class CompanySearchResponse200OutputDataItemNumMatchingLocationsType0:
    """ 
        Attributes:
            num_offices_matched (float):
            matched_offices (list['CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem']):
     """

    num_offices_matched: float
    matched_offices: list['CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_response_200_output_data_item_num_matching_locations_type_0_matched_offices_item import CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem
        num_offices_matched = self.num_offices_matched

        matched_offices = []
        for matched_offices_item_data in self.matched_offices:
            matched_offices_item = matched_offices_item_data.to_dict()
            matched_offices.append(matched_offices_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "num_offices_matched": num_offices_matched,
            "matched_offices": matched_offices,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_num_matching_locations_type_0_matched_offices_item import CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem
        d = dict(src_dict)
        num_offices_matched = d.pop("num_offices_matched")

        matched_offices = []
        _matched_offices = d.pop("matched_offices")
        for matched_offices_item_data in (_matched_offices):
            matched_offices_item = CompanySearchResponse200OutputDataItemNumMatchingLocationsType0MatchedOfficesItem.from_dict(matched_offices_item_data)



            matched_offices.append(matched_offices_item)


        company_search_response_200_output_data_item_num_matching_locations_type_0 = cls(
            num_offices_matched=num_offices_matched,
            matched_offices=matched_offices,
        )


        company_search_response_200_output_data_item_num_matching_locations_type_0.additional_properties = d
        return company_search_response_200_output_data_item_num_matching_locations_type_0

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
