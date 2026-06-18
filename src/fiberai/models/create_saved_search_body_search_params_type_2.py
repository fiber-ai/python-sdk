from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_2_type import CreateSavedSearchBodySearchParamsType2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParams,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2:
    """A profile-only search.

    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType2Type): The search type: profiles only.
        profile_search_params (CreateSavedSearchBodySearchParamsType2ProfileSearchParams | Unset): The profile search
            parameters. Uses the same schema as the profile search endpoint.
        max_new_profiles_per_run (int | Unset): Maximum number of new profiles to charge for per run. Default: 1000.
    """

    type_: CreateSavedSearchBodySearchParamsType2Type
    profile_search_params: CreateSavedSearchBodySearchParamsType2ProfileSearchParams | Unset = UNSET
    max_new_profiles_per_run: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        profile_search_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_search_params, Unset):
            profile_search_params = self.profile_search_params.to_dict()

        max_new_profiles_per_run = self.max_new_profiles_per_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if profile_search_params is not UNSET:
            field_dict["profileSearchParams"] = profile_search_params
        if max_new_profiles_per_run is not UNSET:
            field_dict["maxNewProfilesPerRun"] = max_new_profiles_per_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParams,
        )

        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType2Type(d.pop("type"))

        _profile_search_params = d.pop("profileSearchParams", UNSET)
        profile_search_params: CreateSavedSearchBodySearchParamsType2ProfileSearchParams | Unset
        if isinstance(_profile_search_params, Unset):
            profile_search_params = UNSET
        else:
            profile_search_params = CreateSavedSearchBodySearchParamsType2ProfileSearchParams.from_dict(
                _profile_search_params
            )

        max_new_profiles_per_run = d.pop("maxNewProfilesPerRun", UNSET)

        create_saved_search_body_search_params_type_2 = cls(
            type_=type_,
            profile_search_params=profile_search_params,
            max_new_profiles_per_run=max_new_profiles_per_run,
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
