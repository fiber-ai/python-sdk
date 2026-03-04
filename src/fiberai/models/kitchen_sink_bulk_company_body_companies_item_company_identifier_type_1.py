from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1_identifier import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1Identifier






T = TypeVar("T", bound="KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1")



@_attrs_define
class KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1:
    """ 
        Attributes:
            identifier (KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1Identifier):
            value (str):
     """

    identifier: KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1Identifier
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "identifier": identifier,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1Identifier(d.pop("identifier"))




        value = d.pop("value")

        kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1 = cls(
            identifier=identifier,
            value=value,
        )


        kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1.additional_properties = d
        return kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1

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
