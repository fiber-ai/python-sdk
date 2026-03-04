from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_2_type import CreateSavedSearchBodySearchParamsType2Type
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_2_profile_search_params import CreateSavedSearchBodySearchParamsType2ProfileSearchParams





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2")



@_attrs_define
class CreateSavedSearchBodySearchParamsType2:
    """ profiles

        Attributes:
            type_ (CreateSavedSearchBodySearchParamsType2Type): profiles
            profile_search_params (Union[Unset, CreateSavedSearchBodySearchParamsType2ProfileSearchParams]): The profile
                search params. This is same as our normal profile search api.
            max_profiles (Union[None, Unset, int]): Max profiles to find. Defaults to 10000 if not provided. Default: 10000.
     """

    type_: CreateSavedSearchBodySearchParamsType2Type
    profile_search_params: Union[Unset, 'CreateSavedSearchBodySearchParamsType2ProfileSearchParams'] = UNSET
    max_profiles: Union[None, Unset, int] = 10000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params import CreateSavedSearchBodySearchParamsType2ProfileSearchParams
        type_ = self.type_.value

        profile_search_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile_search_params, Unset):
            profile_search_params = self.profile_search_params.to_dict()

        max_profiles: Union[None, Unset, int]
        if isinstance(self.max_profiles, Unset):
            max_profiles = UNSET
        else:
            max_profiles = self.max_profiles


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if profile_search_params is not UNSET:
            field_dict["profileSearchParams"] = profile_search_params
        if max_profiles is not UNSET:
            field_dict["maxProfiles"] = max_profiles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params import CreateSavedSearchBodySearchParamsType2ProfileSearchParams
        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType2Type(d.pop("type"))




        _profile_search_params = d.pop("profileSearchParams", UNSET)
        profile_search_params: Union[Unset, CreateSavedSearchBodySearchParamsType2ProfileSearchParams]
        if isinstance(_profile_search_params,  Unset):
            profile_search_params = UNSET
        else:
            profile_search_params = CreateSavedSearchBodySearchParamsType2ProfileSearchParams.from_dict(_profile_search_params)




        def _parse_max_profiles(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_profiles = _parse_max_profiles(d.pop("maxProfiles", UNSET))


        create_saved_search_body_search_params_type_2 = cls(
            type_=type_,
            profile_search_params=profile_search_params,
            max_profiles=max_profiles,
        )


        create_saved_search_body_search_params_type_2.additional_properties = d
        return create_saved_search_body_search_params_type_2

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
