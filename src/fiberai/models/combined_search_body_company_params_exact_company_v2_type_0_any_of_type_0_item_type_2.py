from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_body_company_params_exact_company_v2_type_0_any_of_type_0_item_type_2_identifier import (
    CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2Identifier,
)

T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2")


@_attrs_define
class CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2:
    """
    Attributes:
        identifier (CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2Identifier):
        org_id (str):
    """

    identifier: CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2Identifier
    org_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "org_id": org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = CombinedSearchBodyCompanyParamsExactCompanyV2Type0AnyOfType0ItemType2Identifier(
            d.pop("identifier")
        )

        org_id = d.pop("org_id")

        combined_search_body_company_params_exact_company_v2_type_0_any_of_type_0_item_type_2 = cls(
            identifier=identifier,
            org_id=org_id,
        )

        combined_search_body_company_params_exact_company_v2_type_0_any_of_type_0_item_type_2.additional_properties = d
        return combined_search_body_company_params_exact_company_v2_type_0_any_of_type_0_item_type_2

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
