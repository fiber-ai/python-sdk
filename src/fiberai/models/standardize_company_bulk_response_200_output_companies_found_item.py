from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandardizeCompanyBulkResponse200OutputCompaniesFoundItem")


@_attrs_define
class StandardizeCompanyBulkResponse200OutputCompaniesFoundItem:
    """
    Attributes:
        linkedin_url (str): The standardized LinkedIn company URL (e.g., 'https://www.linkedin.com/company/microsoft')
        identifier (str): The input identifier this result was resolved from (slug, organization ID, or URL as provided
            in the request).
        name (None | str | Unset): The company name, if available
        website_url (None | str | Unset): The company's website URL, if available
    """

    linkedin_url: str
    identifier: str
    name: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        identifier = self.identifier

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "identifier": identifier,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        identifier = d.pop("identifier")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("websiteUrl", UNSET))

        standardize_company_bulk_response_200_output_companies_found_item = cls(
            linkedin_url=linkedin_url,
            identifier=identifier,
            name=name,
            website_url=website_url,
        )

        standardize_company_bulk_response_200_output_companies_found_item.additional_properties = d
        return standardize_company_bulk_response_200_output_companies_found_item

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
