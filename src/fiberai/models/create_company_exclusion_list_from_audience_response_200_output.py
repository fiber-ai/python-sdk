from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCompanyExclusionListFromAudienceResponse200Output")


@_attrs_define
class CreateCompanyExclusionListFromAudienceResponse200Output:
    """
    Attributes:
        list_id (str): Id of the company exclusion list
        name (str): Name of the company exclusion list
        companies_added (float): Number of companies added to the exclusion list
    """

    list_id: str
    name: str
    companies_added: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        name = self.name

        companies_added = self.companies_added

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "name": name,
                "companiesAdded": companies_added,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("listId")

        name = d.pop("name")

        companies_added = d.pop("companiesAdded")

        create_company_exclusion_list_from_audience_response_200_output = cls(
            list_id=list_id,
            name=name,
            companies_added=companies_added,
        )

        create_company_exclusion_list_from_audience_response_200_output.additional_properties = d
        return create_company_exclusion_list_from_audience_response_200_output

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
