from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0
  from ..models.kitchen_sink_bulk_company_body_companies_item_company_domain_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0
  from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1
  from ..models.kitchen_sink_bulk_company_body_companies_item_company_name_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0
  from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_2 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2





T = TypeVar("T", bound="KitchenSinkBulkCompanyBodyCompaniesItem")



@_attrs_define
class KitchenSinkBulkCompanyBodyCompaniesItem:
    """ 
        Attributes:
            company_identifier (Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0',
                'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1',
                'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2', None, Unset]):
            company_name (Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0', None, Unset]):
            company_domain (Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0', None, Unset]):
            num_companies (Union[Unset, int]):  Default: 1.
     """

    company_identifier: Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2', None, Unset] = UNSET
    company_name: Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0', None, Unset] = UNSET
    company_domain: Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0', None, Unset] = UNSET
    num_companies: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_domain_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_name_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_2 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2
        company_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_identifier, Unset):
            company_identifier = UNSET
        elif isinstance(self.company_identifier, KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2):
            company_identifier = self.company_identifier.to_dict()
        else:
            company_identifier = self.company_identifier

        company_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        elif isinstance(self.company_name, KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0):
            company_name = self.company_name.to_dict()
        else:
            company_name = self.company_name

        company_domain: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        elif isinstance(self.company_domain, KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0):
            company_domain = self.company_domain.to_dict()
        else:
            company_domain = self.company_domain

        num_companies = self.num_companies


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if num_companies is not UNSET:
            field_dict["numCompanies"] = num_companies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_domain_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_1 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_name_type_0 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0
        from ..models.kitchen_sink_bulk_company_body_companies_item_company_identifier_type_2 import KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2
        d = dict(src_dict)
        def _parse_company_identifier(data: object) -> Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_0 = KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0.from_dict(data)



                return company_identifier_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_1 = KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1.from_dict(data)



                return company_identifier_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_2 = KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2.from_dict(data)



                return company_identifier_type_2
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType0', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType1', 'KitchenSinkBulkCompanyBodyCompaniesItemCompanyIdentifierType2', None, Unset], data)

        company_identifier = _parse_company_identifier(d.pop("companyIdentifier", UNSET))


        def _parse_company_name(data: object) -> Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_name_type_0 = KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0.from_dict(data)



                return company_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyNameType0', None, Unset], data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_company_domain(data: object) -> Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_domain_type_0 = KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0.from_dict(data)



                return company_domain_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkCompanyBodyCompaniesItemCompanyDomainType0', None, Unset], data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))


        num_companies = d.pop("numCompanies", UNSET)

        kitchen_sink_bulk_company_body_companies_item = cls(
            company_identifier=company_identifier,
            company_name=company_name,
            company_domain=company_domain,
            num_companies=num_companies,
        )


        kitchen_sink_bulk_company_body_companies_item.additional_properties = d
        return kitchen_sink_bulk_company_body_companies_item

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
