from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_company_logos_body_companies_identifier_type_0_type import (
    BulkCompanyLogosBodyCompaniesIdentifierType0Type,
)

T = TypeVar("T", bound="BulkCompanyLogosBodyCompaniesIdentifierType0")


@_attrs_define
class BulkCompanyLogosBodyCompaniesIdentifierType0:
    """
    Attributes:
        type_ (BulkCompanyLogosBodyCompaniesIdentifierType0Type):
        domains (list[str]):
    """

    type_: BulkCompanyLogosBodyCompaniesIdentifierType0Type
    domains: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domains = self.domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "domains": domains,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = BulkCompanyLogosBodyCompaniesIdentifierType0Type(d.pop("type"))

        domains = cast(list[str], d.pop("domains"))

        bulk_company_logos_body_companies_identifier_type_0 = cls(
            type_=type_,
            domains=domains,
        )

        bulk_company_logos_body_companies_identifier_type_0.additional_properties = d
        return bulk_company_logos_body_companies_identifier_type_0

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
