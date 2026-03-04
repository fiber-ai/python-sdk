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
  from ..models.get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item_date_range import GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange





T = TypeVar("T", bound="GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0Item")



@_attrs_define
class GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0Item:
    """ 
        Attributes:
            date_range (GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange):
            titles (list[str]):
            localities (list[str]):
            linkedin_company_id (Union[None, Unset, str]):
            company_name (Union[None, Unset, str]):
            range_length_days (Union[None, Unset, float]):
     """

    date_range: 'GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange'
    titles: list[str]
    localities: list[str]
    linkedin_company_id: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    range_length_days: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item_date_range import GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange
        date_range = self.date_range.to_dict()

        titles = self.titles



        localities = self.localities



        linkedin_company_id: Union[None, Unset, str]
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        range_length_days: Union[None, Unset, float]
        if isinstance(self.range_length_days, Unset):
            range_length_days = UNSET
        else:
            range_length_days = self.range_length_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date_range": date_range,
            "titles": titles,
            "localities": localities,
        })
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if range_length_days is not UNSET:
            field_dict["range_length_days"] = range_length_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item_date_range import GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange
        d = dict(src_dict)
        date_range = GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTenuresType0ItemDateRange.from_dict(d.pop("date_range"))




        titles = cast(list[str], d.pop("titles"))


        localities = cast(list[str], d.pop("localities"))


        def _parse_linkedin_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))


        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))


        def _parse_range_length_days(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        range_length_days = _parse_range_length_days(d.pop("range_length_days", UNSET))


        get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item = cls(
            date_range=date_range,
            titles=titles,
            localities=localities,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            range_length_days=range_length_days,
        )


        get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item.additional_properties = d
        return get_current_profiles_in_saved_search_response_200_output_profiles_item_tenures_type_0_item

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
