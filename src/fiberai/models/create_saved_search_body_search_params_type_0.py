from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_0_type import CreateSavedSearchBodySearchParamsType0Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParams,
    )
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParams,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0:
    """A combined company and profile search.

    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType0Type): The search type: combined companies and profiles.
        company_search_params (CreateSavedSearchBodySearchParamsType0CompanySearchParams): The company search
            parameters. Uses the same schema as the company search endpoint.
        max_new_companies_per_run (int | Unset): Maximum number of new companies to charge for per run. Default: 1000.
        profile_search_params (CreateSavedSearchBodySearchParamsType0ProfileSearchParams | Unset): The profile search
            parameters. Uses the same schema as the profile search endpoint.
        max_new_profiles_per_run (int | Unset): Maximum number of new profiles to charge for per run. Default: 1000.
    """

    type_: CreateSavedSearchBodySearchParamsType0Type
    company_search_params: CreateSavedSearchBodySearchParamsType0CompanySearchParams
    max_new_companies_per_run: int | Unset = 1000
    profile_search_params: CreateSavedSearchBodySearchParamsType0ProfileSearchParams | Unset = UNSET
    max_new_profiles_per_run: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        company_search_params = self.company_search_params.to_dict()

        max_new_companies_per_run = self.max_new_companies_per_run

        profile_search_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_search_params, Unset):
            profile_search_params = self.profile_search_params.to_dict()

        max_new_profiles_per_run = self.max_new_profiles_per_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "companySearchParams": company_search_params,
            }
        )
        if max_new_companies_per_run is not UNSET:
            field_dict["maxNewCompaniesPerRun"] = max_new_companies_per_run
        if profile_search_params is not UNSET:
            field_dict["profileSearchParams"] = profile_search_params
        if max_new_profiles_per_run is not UNSET:
            field_dict["maxNewProfilesPerRun"] = max_new_profiles_per_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParams,
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParams,
        )

        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType0Type(d.pop("type"))

        company_search_params = CreateSavedSearchBodySearchParamsType0CompanySearchParams.from_dict(
            d.pop("companySearchParams")
        )

        max_new_companies_per_run = d.pop("maxNewCompaniesPerRun", UNSET)

        _profile_search_params = d.pop("profileSearchParams", UNSET)
        profile_search_params: CreateSavedSearchBodySearchParamsType0ProfileSearchParams | Unset
        if isinstance(_profile_search_params, Unset):
            profile_search_params = UNSET
        else:
            profile_search_params = CreateSavedSearchBodySearchParamsType0ProfileSearchParams.from_dict(
                _profile_search_params
            )

        max_new_profiles_per_run = d.pop("maxNewProfilesPerRun", UNSET)

        create_saved_search_body_search_params_type_0 = cls(
            type_=type_,
            company_search_params=company_search_params,
            max_new_companies_per_run=max_new_companies_per_run,
            profile_search_params=profile_search_params,
            max_new_profiles_per_run=max_new_profiles_per_run,
        )

        create_saved_search_body_search_params_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0

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
