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
  from ..models.people_search_count_body_current_companies_type_0_item import PeopleSearchCountBodyCurrentCompaniesType0Item
  from ..models.people_search_count_body_search_params import PeopleSearchCountBodySearchParams





T = TypeVar("T", bound="PeopleSearchCountBody")



@_attrs_define
class PeopleSearchCountBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            search_params (Union[Unset, PeopleSearchCountBodySearchParams]): Search parameters for people search.
            current_companies (Union[None, Unset, list['PeopleSearchCountBodyCurrentCompaniesType0Item']]): Filter people by
                the companies they are currently working for. If you want to search over many companies, we suggest using the
                Combined Search API, which is optimized for this use case.
            prospect_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out people which belong to the given
                prospect exclusion lists
            company_exclusion_list_i_ds (Union[None, Unset, list[str]]): Filter out people who work at companies which
                belong to the given company exclusion lists
     """

    api_key: str
    search_params: Union[Unset, 'PeopleSearchCountBodySearchParams'] = UNSET
    current_companies: Union[None, Unset, list['PeopleSearchCountBodyCurrentCompaniesType0Item']] = UNSET
    prospect_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    company_exclusion_list_i_ds: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_current_companies_type_0_item import PeopleSearchCountBodyCurrentCompaniesType0Item
        from ..models.people_search_count_body_search_params import PeopleSearchCountBodySearchParams
        api_key = self.api_key

        search_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.search_params, Unset):
            search_params = self.search_params.to_dict()

        current_companies: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.current_companies, Unset):
            current_companies = UNSET
        elif isinstance(self.current_companies, list):
            current_companies = []
            for current_companies_type_0_item_data in self.current_companies:
                current_companies_type_0_item = current_companies_type_0_item_data.to_dict()
                current_companies.append(current_companies_type_0_item)


        else:
            current_companies = self.current_companies

        prospect_exclusion_list_i_ds: Union[None, Unset, list[str]]
        if isinstance(self.prospect_exclusion_list_i_ds, Unset):
            prospect_exclusion_list_i_ds = UNSET
        elif isinstance(self.prospect_exclusion_list_i_ds, list):
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds


        else:
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds

        company_exclusion_list_i_ds: Union[None, Unset, list[str]]
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds


        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
        })
        if search_params is not UNSET:
            field_dict["searchParams"] = search_params
        if current_companies is not UNSET:
            field_dict["currentCompanies"] = current_companies
        if prospect_exclusion_list_i_ds is not UNSET:
            field_dict["prospectExclusionListIDs"] = prospect_exclusion_list_i_ds
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_current_companies_type_0_item import PeopleSearchCountBodyCurrentCompaniesType0Item
        from ..models.people_search_count_body_search_params import PeopleSearchCountBodySearchParams
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        _search_params = d.pop("searchParams", UNSET)
        search_params: Union[Unset, PeopleSearchCountBodySearchParams]
        if isinstance(_search_params,  Unset):
            search_params = UNSET
        else:
            search_params = PeopleSearchCountBodySearchParams.from_dict(_search_params)




        def _parse_current_companies(data: object) -> Union[None, Unset, list['PeopleSearchCountBodyCurrentCompaniesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                current_companies_type_0 = []
                _current_companies_type_0 = data
                for current_companies_type_0_item_data in (_current_companies_type_0):
                    current_companies_type_0_item = PeopleSearchCountBodyCurrentCompaniesType0Item.from_dict(current_companies_type_0_item_data)



                    current_companies_type_0.append(current_companies_type_0_item)

                return current_companies_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['PeopleSearchCountBodyCurrentCompaniesType0Item']], data)

        current_companies = _parse_current_companies(d.pop("currentCompanies", UNSET))


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


        people_search_count_body = cls(
            api_key=api_key,
            search_params=search_params,
            current_companies=current_companies,
            prospect_exclusion_list_i_ds=prospect_exclusion_list_i_ds,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
        )


        people_search_count_body.additional_properties = d
        return people_search_count_body

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
