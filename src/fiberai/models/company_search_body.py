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
  from ..models.company_search_body_search_params import CompanySearchBodySearchParams





T = TypeVar("T", bound="CompanySearchBody")



@_attrs_define
class CompanySearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            search_params (CompanySearchBodySearchParams): Search parameters for company search API.
            page_size (Union[Unset, int]): The number of companies to return, if you need to get more results, you can
                paginate. Default: 25.
            cursor (Union[None, Unset, str]): A pagination cursor returned from a previous search response. Use this to
                fetch the next page of results.
            company_exclusion_list_i_ds (Union[Unset, list[str]]): Filter out companies which belong to the given company
                exclusion lists. You can create company exclusion lists via /v1/exclusions/companies/create-list
     """

    api_key: str
    search_params: 'CompanySearchBodySearchParams'
    page_size: Union[Unset, int] = 25
    cursor: Union[None, Unset, str] = UNSET
    company_exclusion_list_i_ds: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params import CompanySearchBodySearchParams
        api_key = self.api_key

        search_params = self.search_params.to_dict()

        page_size = self.page_size

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        company_exclusion_list_i_ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "searchParams": search_params,
        })
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params import CompanySearchBodySearchParams
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        search_params = CompanySearchBodySearchParams.from_dict(d.pop("searchParams"))




        page_size = d.pop("pageSize", UNSET)

        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        company_exclusion_list_i_ds = cast(list[str], d.pop("companyExclusionListIDs", UNSET))


        company_search_body = cls(
            api_key=api_key,
            search_params=search_params,
            page_size=page_size,
            cursor=cursor,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
        )


        company_search_body.additional_properties = d
        return company_search_body

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
