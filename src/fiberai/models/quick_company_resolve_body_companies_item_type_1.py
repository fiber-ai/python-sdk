from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quick_company_resolve_body_companies_item_type_1_identifier import (
    QuickCompanyResolveBodyCompaniesItemType1Identifier,
)

T = TypeVar("T", bound="QuickCompanyResolveBodyCompaniesItemType1")


@_attrs_define
class QuickCompanyResolveBodyCompaniesItemType1:
    """
    Attributes:
        identifier (QuickCompanyResolveBodyCompaniesItemType1Identifier):
        value (str): LinkedIn company slug (e.g. 'openai').
    """

    identifier: QuickCompanyResolveBodyCompaniesItemType1Identifier
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = QuickCompanyResolveBodyCompaniesItemType1Identifier(d.pop("identifier"))

        value = d.pop("value")

        quick_company_resolve_body_companies_item_type_1 = cls(
            identifier=identifier,
            value=value,
        )

        quick_company_resolve_body_companies_item_type_1.additional_properties = d
        return quick_company_resolve_body_companies_item_type_1

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
