from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ReverseEmailLookupBody")



@_attrs_define
class ReverseEmailLookupBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            email (str): The person's email address for which you want to do a reverse lookup
            num_profiles (Union[None, Unset, float]): Number of profiles to return. Maximum 10 profiles can be returned for
                given query. The returned profiles will be sorted by best match first. Default: 1.0.
     """

    api_key: str
    email: str
    num_profiles: Union[None, Unset, float] = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        email = self.email

        num_profiles: Union[None, Unset, float]
        if isinstance(self.num_profiles, Unset):
            num_profiles = UNSET
        else:
            num_profiles = self.num_profiles


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "email": email,
        })
        if num_profiles is not UNSET:
            field_dict["num_profiles"] = num_profiles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        email = d.pop("email")

        def _parse_num_profiles(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_profiles = _parse_num_profiles(d.pop("num_profiles", UNSET))


        reverse_email_lookup_body = cls(
            api_key=api_key,
            email=email,
            num_profiles=num_profiles,
        )


        reverse_email_lookup_body.additional_properties = d
        return reverse_email_lookup_body

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
