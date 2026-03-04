from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.company_count_body_search_params import CompanyCountBodySearchParams





T = TypeVar("T", bound="CompanyCountBody")



@_attrs_define
class CompanyCountBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            search_params (CompanyCountBodySearchParams): Search parameters for company search API.
            company_exclusion_list_i_ds (Union[Unset, list[str]]): Filter out companies which belong to the given company
                exclusion lists. You can create company exclusion lists via /v1/exclusions/companies/create-list
     """

    api_key: str
    search_params: 'CompanyCountBodySearchParams'
    company_exclusion_list_i_ds: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_count_body_search_params import CompanyCountBodySearchParams
        api_key = self.api_key

        search_params = self.search_params.to_dict()

        company_exclusion_list_i_ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "searchParams": search_params,
        })
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_body_search_params import CompanyCountBodySearchParams
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        search_params = CompanyCountBodySearchParams.from_dict(d.pop("searchParams"))




        company_exclusion_list_i_ds = cast(list[str], d.pop("companyExclusionListIDs", UNSET))


        company_count_body = cls(
            api_key=api_key,
            search_params=search_params,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
        )


        company_count_body.additional_properties = d
        return company_count_body

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
