from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompanyLogoBody")


@_attrs_define
class CompanyLogoBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        identifier (str): A company identifier: a LinkedIn company URL (e.g. 'https://www.linkedin.com/company/openai'),
            a LinkedIn company slug (e.g. 'openai'), a numeric LinkedIn organization ID (e.g. '11130470'), or a company
            domain (e.g. 'openai.com'). The format is auto-detected.
    """

    api_key: str
    identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        identifier = d.pop("identifier")

        company_logo_body = cls(
            api_key=api_key,
            identifier=identifier,
        )

        company_logo_body.additional_properties = d
        return company_logo_body

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
