from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_company_logos_body_companies_identifier_type_2_type import BulkCompanyLogosBodyCompaniesIdentifierType2Type
from typing import cast






T = TypeVar("T", bound="BulkCompanyLogosBodyCompaniesIdentifierType2")



@_attrs_define
class BulkCompanyLogosBodyCompaniesIdentifierType2:
    """ 
        Attributes:
            type_ (BulkCompanyLogosBodyCompaniesIdentifierType2Type):
            li_org_ids (list[str]):
     """

    type_: BulkCompanyLogosBodyCompaniesIdentifierType2Type
    li_org_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        li_org_ids = self.li_org_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "liOrgIds": li_org_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = BulkCompanyLogosBodyCompaniesIdentifierType2Type(d.pop("type"))




        li_org_ids = cast(list[str], d.pop("liOrgIds"))


        bulk_company_logos_body_companies_identifier_type_2 = cls(
            type_=type_,
            li_org_ids=li_org_ids,
        )


        bulk_company_logos_body_companies_identifier_type_2.additional_properties = d
        return bulk_company_logos_body_companies_identifier_type_2

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
