from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_1_company_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1_identifier import CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1Identifier






T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1")



@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1:
    """ 
        Attributes:
            identifier
                (CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1Identifier):
            linkedin_url (str):
     """

    identifier: CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1Identifier
    linkedin_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        linkedin_url = self.linkedin_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "identifier": identifier,
            "linkedin_url": linkedin_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = CreateSavedSearchBodySearchParamsType1CompanySearchParamsExactCompanyV2Type0AnyOfType0ItemType1Identifier(d.pop("identifier"))




        linkedin_url = d.pop("linkedin_url")

        create_saved_search_body_search_params_type_1_company_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1 = cls(
            identifier=identifier,
            linkedin_url=linkedin_url,
        )


        create_saved_search_body_search_params_type_1_company_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1

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
