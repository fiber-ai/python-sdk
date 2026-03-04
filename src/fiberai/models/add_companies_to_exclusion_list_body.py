from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.add_companies_to_exclusion_list_body_companies_item import AddCompaniesToExclusionListBodyCompaniesItem





T = TypeVar("T", bound="AddCompaniesToExclusionListBody")



@_attrs_define
class AddCompaniesToExclusionListBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            list_id (str): Id of the company exclusion list to add companies to
            companies (list['AddCompaniesToExclusionListBodyCompaniesItem']): Companies to add to the exclusion list. Max
                5000 companies can be added at a time.
     """

    api_key: str
    list_id: str
    companies: list['AddCompaniesToExclusionListBodyCompaniesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_companies_to_exclusion_list_body_companies_item import AddCompaniesToExclusionListBodyCompaniesItem
        api_key = self.api_key

        list_id = self.list_id

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "listId": list_id,
            "companies": companies,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_companies_to_exclusion_list_body_companies_item import AddCompaniesToExclusionListBodyCompaniesItem
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        list_id = d.pop("listId")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in (_companies):
            companies_item = AddCompaniesToExclusionListBodyCompaniesItem.from_dict(companies_item_data)



            companies.append(companies_item)


        add_companies_to_exclusion_list_body = cls(
            api_key=api_key,
            list_id=list_id,
            companies=companies,
        )


        add_companies_to_exclusion_list_body.additional_properties = d
        return add_companies_to_exclusion_list_body

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
