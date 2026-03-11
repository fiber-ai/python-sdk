from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_company_logos_body_companies_identifier_type_1_type import (
    BulkCompanyLogosBodyCompaniesIdentifierType1Type,
)

T = TypeVar("T", bound="BulkCompanyLogosBodyCompaniesIdentifierType1")


@_attrs_define
class BulkCompanyLogosBodyCompaniesIdentifierType1:
    """
    Attributes:
        type_ (BulkCompanyLogosBodyCompaniesIdentifierType1Type):
        linkedin_urls (list[str]):
    """

    type_: BulkCompanyLogosBodyCompaniesIdentifierType1Type
    linkedin_urls: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        linkedin_urls = self.linkedin_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "linkedinUrls": linkedin_urls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = BulkCompanyLogosBodyCompaniesIdentifierType1Type(d.pop("type"))

        linkedin_urls = cast(list[str], d.pop("linkedinUrls"))

        bulk_company_logos_body_companies_identifier_type_1 = cls(
            type_=type_,
            linkedin_urls=linkedin_urls,
        )

        bulk_company_logos_body_companies_identifier_type_1.additional_properties = d
        return bulk_company_logos_body_companies_identifier_type_1

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
