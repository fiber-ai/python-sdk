from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_body_company_params import CombinedSearchBodyCompanyParams
    from ..models.combined_search_body_profile_params import CombinedSearchBodyProfileParams


T = TypeVar("T", bound="CombinedSearchBody")


@_attrs_define
class CombinedSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company_params (CombinedSearchBodyCompanyParams): Search parameters for company search API.
        profile_params (CombinedSearchBodyProfileParams | Unset): Search parameters for people search.
        max_companies (int | Unset): The total number of companies from which you want to find the final profiles. Set
            this to adjust how many different companies' profiles you want. If this is set to 0,  no companies would be
            returned. However, profiles would still be found working in the companies that satisfy the `companyParams`.
            Default: 100.
        max_profiles (int | Unset): The total number of profiles to find from the companies that are saved. Default:
            100.
        company_exclusion_list_i_ds (list[str] | None | Unset): Filter out companies which belong to the given company
            exclusion lists. You can create company exclusion lists via our API
        prospect_exclusion_list_i_ds (list[str] | None | Unset): Filter out people which belong to the given prospect
            exclusion lists. You can create prospect exclusion lists via our API
    """

    api_key: str
    company_params: CombinedSearchBodyCompanyParams
    profile_params: CombinedSearchBodyProfileParams | Unset = UNSET
    max_companies: int | Unset = 100
    max_profiles: int | Unset = 100
    company_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    prospect_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        company_params = self.company_params.to_dict()

        profile_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_params, Unset):
            profile_params = self.profile_params.to_dict()

        max_companies = self.max_companies

        max_profiles = self.max_profiles

        company_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        prospect_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.prospect_exclusion_list_i_ds, Unset):
            prospect_exclusion_list_i_ds = UNSET
        elif isinstance(self.prospect_exclusion_list_i_ds, list):
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds

        else:
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companyParams": company_params,
            }
        )
        if profile_params is not UNSET:
            field_dict["profileParams"] = profile_params
        if max_companies is not UNSET:
            field_dict["maxCompanies"] = max_companies
        if max_profiles is not UNSET:
            field_dict["maxProfiles"] = max_profiles
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds
        if prospect_exclusion_list_i_ds is not UNSET:
            field_dict["prospectExclusionListIDs"] = prospect_exclusion_list_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_company_params import CombinedSearchBodyCompanyParams
        from ..models.combined_search_body_profile_params import CombinedSearchBodyProfileParams

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        company_params = CombinedSearchBodyCompanyParams.from_dict(d.pop("companyParams"))

        _profile_params = d.pop("profileParams", UNSET)
        profile_params: CombinedSearchBodyProfileParams | Unset
        if isinstance(_profile_params, Unset):
            profile_params = UNSET
        else:
            profile_params = CombinedSearchBodyProfileParams.from_dict(_profile_params)

        max_companies = d.pop("maxCompanies", UNSET)

        max_profiles = d.pop("maxProfiles", UNSET)

        def _parse_company_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return company_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_exclusion_list_i_ds = _parse_company_exclusion_list_i_ds(d.pop("companyExclusionListIDs", UNSET))

        def _parse_prospect_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prospect_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return prospect_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        prospect_exclusion_list_i_ds = _parse_prospect_exclusion_list_i_ds(d.pop("prospectExclusionListIDs", UNSET))

        combined_search_body = cls(
            api_key=api_key,
            company_params=company_params,
            profile_params=profile_params,
            max_companies=max_companies,
            max_profiles=max_profiles,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
            prospect_exclusion_list_i_ds=prospect_exclusion_list_i_ds,
        )

        combined_search_body.additional_properties = d
        return combined_search_body

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
