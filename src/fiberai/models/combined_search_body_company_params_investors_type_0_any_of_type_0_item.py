from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsInvestorsType0AnyOfType0Item")



@_attrs_define
class CombinedSearchBodyCompanyParamsInvestorsType0AnyOfType0Item:
    """ Requires at least one identifier: LinkedIn company ID, LinkedIn URL, or company domain to uniquely identify the
    investor organization.

        Attributes:
            linkedin_company_id (Union[None, Unset, str]):
            linkedin_url (Union[None, Unset, str]):
            company_domain (Union[None, Unset, str]):
     """

    linkedin_company_id: Union[None, Unset, str] = UNSET
    linkedin_url: Union[None, Unset, str] = UNSET
    company_domain: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        linkedin_company_id: Union[None, Unset, str]
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        linkedin_url: Union[None, Unset, str]
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        company_domain: Union[None, Unset, str]
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linkedin_company_id is not UNSET:
            field_dict["linkedinCompanyId"] = linkedin_company_id
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_linkedin_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedinCompanyId", UNSET))


        def _parse_linkedin_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))


        def _parse_company_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))


        combined_search_body_company_params_investors_type_0_any_of_type_0_item = cls(
            linkedin_company_id=linkedin_company_id,
            linkedin_url=linkedin_url,
            company_domain=company_domain,
        )


        combined_search_body_company_params_investors_type_0_any_of_type_0_item.additional_properties = d
        return combined_search_body_company_params_investors_type_0_any_of_type_0_item

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
