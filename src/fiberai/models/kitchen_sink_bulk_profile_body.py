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
  from ..models.kitchen_sink_bulk_profile_body_profiles_item import KitchenSinkBulkProfileBodyProfilesItem





T = TypeVar("T", bound="KitchenSinkBulkProfileBody")



@_attrs_define
class KitchenSinkBulkProfileBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            profiles (list['KitchenSinkBulkProfileBodyProfilesItem']):
            live_fetch (Union[None, Unset, bool]):  Default: False.
            force_company_match (Union[None, Unset, bool]):  Default: False.
            fuzzy_search (Union[None, Unset, bool]):  Default: False.
            get_detailed_education (Union[None, Unset, bool]):  Default: False.
            get_detailed_work_experience (Union[None, Unset, bool]):  Default: False.
     """

    api_key: str
    profiles: list['KitchenSinkBulkProfileBodyProfilesItem']
    live_fetch: Union[None, Unset, bool] = False
    force_company_match: Union[None, Unset, bool] = False
    fuzzy_search: Union[None, Unset, bool] = False
    get_detailed_education: Union[None, Unset, bool] = False
    get_detailed_work_experience: Union[None, Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_bulk_profile_body_profiles_item import KitchenSinkBulkProfileBodyProfilesItem
        api_key = self.api_key

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)



        live_fetch: Union[None, Unset, bool]
        if isinstance(self.live_fetch, Unset):
            live_fetch = UNSET
        else:
            live_fetch = self.live_fetch

        force_company_match: Union[None, Unset, bool]
        if isinstance(self.force_company_match, Unset):
            force_company_match = UNSET
        else:
            force_company_match = self.force_company_match

        fuzzy_search: Union[None, Unset, bool]
        if isinstance(self.fuzzy_search, Unset):
            fuzzy_search = UNSET
        else:
            fuzzy_search = self.fuzzy_search

        get_detailed_education: Union[None, Unset, bool]
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: Union[None, Unset, bool]
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "profiles": profiles,
        })
        if live_fetch is not UNSET:
            field_dict["liveFetch"] = live_fetch
        if force_company_match is not UNSET:
            field_dict["forceCompanyMatch"] = force_company_match
        if fuzzy_search is not UNSET:
            field_dict["fuzzySearch"] = fuzzy_search
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_bulk_profile_body_profiles_item import KitchenSinkBulkProfileBodyProfilesItem
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in (_profiles):
            profiles_item = KitchenSinkBulkProfileBodyProfilesItem.from_dict(profiles_item_data)



            profiles.append(profiles_item)


        def _parse_live_fetch(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        live_fetch = _parse_live_fetch(d.pop("liveFetch", UNSET))


        def _parse_force_company_match(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        force_company_match = _parse_force_company_match(d.pop("forceCompanyMatch", UNSET))


        def _parse_fuzzy_search(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        fuzzy_search = _parse_fuzzy_search(d.pop("fuzzySearch", UNSET))


        def _parse_get_detailed_education(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))


        def _parse_get_detailed_work_experience(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))


        kitchen_sink_bulk_profile_body = cls(
            api_key=api_key,
            profiles=profiles,
            live_fetch=live_fetch,
            force_company_match=force_company_match,
            fuzzy_search=fuzzy_search,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )


        kitchen_sink_bulk_profile_body.additional_properties = d
        return kitchen_sink_bulk_profile_body

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
