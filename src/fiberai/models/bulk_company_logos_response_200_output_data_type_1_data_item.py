from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkCompanyLogosResponse200OutputDataType1DataItem")


@_attrs_define
class BulkCompanyLogosResponse200OutputDataType1DataItem:
    """
    Attributes:
        linkedin_url (str): The linkedin URL of the company
        logo_url (str): The logo URL
    """

    linkedin_url: str
    logo_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "logoUrl": logo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        logo_url = d.pop("logoUrl")

        bulk_company_logos_response_200_output_data_type_1_data_item = cls(
            linkedin_url=linkedin_url,
            logo_url=logo_url,
        )

        bulk_company_logos_response_200_output_data_type_1_data_item.additional_properties = d
        return bulk_company_logos_response_200_output_data_type_1_data_item

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
