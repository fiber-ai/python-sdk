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
  from ..models.sync_combined_search_body_profile_params import SyncCombinedSearchBodyProfileParams
  from ..models.sync_combined_search_body_company_params import SyncCombinedSearchBodyCompanyParams





T = TypeVar("T", bound="SyncCombinedSearchBody")



@_attrs_define
class SyncCombinedSearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            company_params (SyncCombinedSearchBodyCompanyParams): Company search params. We would find prospects who are
                currently working in the companies that satisfy these search params. Make sure that the search scope of
                companies is small, else we truncate it to the top 1000 companies.
            profile_params (Union[Unset, SyncCombinedSearchBodyProfileParams]): The People search params. We would return
                the profiles that satisfy these params and work in the companies satisfying `companyParams`. The number of these
                profiles are truncated to top 1000.
            company_item_limit (Union[None, Unset, float]): The number of companies to return. Defaults to 20 if not
                provided. If you want to get 0 companies, you can pass `null`. However, profiles would still be found working in
                the companies that satisfy the `companyParams`. Default: 20.0.
            profile_item_limit (Union[Unset, float]): The number of profiles to return. Default: 20.0.
            company_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out companies which belong to the given
                company exclusion lists. You can create company exclusion lists via /v1/exclusions/companies/create-list
            prospect_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out people which belong to the given
                prospect exclusion lists. You can create prospect exclusion lists via /v1/exclusions/prospects/create-list
     """

    api_key: str
    company_params: 'SyncCombinedSearchBodyCompanyParams'
    profile_params: Union[Unset, 'SyncCombinedSearchBodyProfileParams'] = UNSET
    company_item_limit: Union[None, Unset, float] = 20.0
    profile_item_limit: Union[Unset, float] = 20.0
    company_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    prospect_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_profile_params import SyncCombinedSearchBodyProfileParams
        from ..models.sync_combined_search_body_company_params import SyncCombinedSearchBodyCompanyParams
        api_key = self.api_key

        company_params = self.company_params.to_dict()

        profile_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile_params, Unset):
            profile_params = self.profile_params.to_dict()

        company_item_limit: Union[None, Unset, float]
        if isinstance(self.company_item_limit, Unset):
            company_item_limit = UNSET
        else:
            company_item_limit = self.company_item_limit

        profile_item_limit = self.profile_item_limit

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
        if company_item_limit is not UNSET:
            field_dict["companyItemLimit"] = company_item_limit
        if profile_item_limit is not UNSET:
            field_dict["profileItemLimit"] = profile_item_limit
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds
        if prospect_exclusion_list_i_ds is not UNSET:
            field_dict["prospectExclusionListIDs"] = prospect_exclusion_list_i_ds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_profile_params import SyncCombinedSearchBodyProfileParams
        from ..models.sync_combined_search_body_company_params import SyncCombinedSearchBodyCompanyParams
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        company_params = SyncCombinedSearchBodyCompanyParams.from_dict(d.pop("companyParams"))




        _profile_params = d.pop("profileParams", UNSET)
        profile_params: Union[Unset, SyncCombinedSearchBodyProfileParams]
        if isinstance(_profile_params,  Unset):
            profile_params = UNSET
        else:
            profile_params = SyncCombinedSearchBodyProfileParams.from_dict(_profile_params)




        def _parse_company_item_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        company_item_limit = _parse_company_item_limit(d.pop("companyItemLimit", UNSET))


        profile_item_limit = d.pop("profileItemLimit", UNSET)

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


        sync_combined_search_body = cls(
            api_key=api_key,
            company_params=company_params,
            profile_params=profile_params,
            company_item_limit=company_item_limit,
            profile_item_limit=profile_item_limit,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
            prospect_exclusion_list_i_ds=prospect_exclusion_list_i_ds,
        )


        sync_combined_search_body.additional_properties = d
        return sync_combined_search_body

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
