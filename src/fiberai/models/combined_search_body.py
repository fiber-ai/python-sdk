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
  from ..models.combined_search_body_profile_params import CombinedSearchBodyProfileParams
  from ..models.combined_search_body_company_params import CombinedSearchBodyCompanyParams





T = TypeVar("T", bound="CombinedSearchBody")



@_attrs_define
class CombinedSearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            company_params (CombinedSearchBodyCompanyParams): Search parameters for company search API.
            profile_params (Union[Unset, CombinedSearchBodyProfileParams]): Search parameters for people search.
            max_companies (Union[Unset, int]): The total number of companies from which you want to find the final profiles.
                Set this to adjust how many different companies' profiles you want. If this is set to 0,  no companies would be
                returned. However, profiles would still be found working in the companies that satisfy the `companyParams`.
                Default: 100.
            max_profiles (Union[Unset, int]): The total number of profiles to find from the companies that are saved.
                Default: 100.
            company_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out companies which belong to the given
                company exclusion lists. You can create company exclusion lists via our API
            prospect_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out people which belong to the given
                prospect exclusion lists. You can create prospect exclusion lists via our API
     """

    api_key: str
    company_params: 'CombinedSearchBodyCompanyParams'
    profile_params: Union[Unset, 'CombinedSearchBodyProfileParams'] = UNSET
    max_companies: Union[Unset, int] = 100
    max_profiles: Union[Unset, int] = 100
    company_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    prospect_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_profile_params import CombinedSearchBodyProfileParams
        from ..models.combined_search_body_company_params import CombinedSearchBodyCompanyParams
        api_key = self.api_key

        company_params = self.company_params.to_dict()

        profile_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile_params, Unset):
            profile_params = self.profile_params.to_dict()

        max_companies = self.max_companies

        max_profiles = self.max_profiles

        company_exclusion_list_i_ds: Union[None, Unset, list[str]]
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds


        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        prospect_exclusion_list_i_ds: Union[None, Unset, list[str]]
        if isinstance(self.prospect_exclusion_list_i_ds, Unset):
            prospect_exclusion_list_i_ds = UNSET
        elif isinstance(self.prospect_exclusion_list_i_ds, list):
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds


        else:
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "companyParams": company_params,
        })
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
        from ..models.combined_search_body_profile_params import CombinedSearchBodyProfileParams
        from ..models.combined_search_body_company_params import CombinedSearchBodyCompanyParams
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        company_params = CombinedSearchBodyCompanyParams.from_dict(d.pop("companyParams"))




        _profile_params = d.pop("profileParams", UNSET)
        profile_params: Union[Unset, CombinedSearchBodyProfileParams]
        if isinstance(_profile_params,  Unset):
            profile_params = UNSET
        else:
            profile_params = CombinedSearchBodyProfileParams.from_dict(_profile_params)




        max_companies = d.pop("maxCompanies", UNSET)

        max_profiles = d.pop("maxProfiles", UNSET)

        def _parse_company_exclusion_list_i_ds(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return company_exclusion_list_i_ds_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        company_exclusion_list_i_ds = _parse_company_exclusion_list_i_ds(d.pop("companyExclusionListIDs", UNSET))


        def _parse_prospect_exclusion_list_i_ds(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prospect_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return prospect_exclusion_list_i_ds_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

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
