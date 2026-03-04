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
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_job_title_type_0 import KitchenSinkBulkProfileBodyProfilesItemJobTitleType0
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_domain_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_person_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemPersonNameType0
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0
  from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0





T = TypeVar("T", bound="KitchenSinkBulkProfileBodyProfilesItem")



@_attrs_define
class KitchenSinkBulkProfileBodyProfilesItem:
    """ 
        Attributes:
            company_domain (Union['KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0', None, Unset]):
            company_name (Union['KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0', None, Unset]):
            job_title (Union['KitchenSinkBulkProfileBodyProfilesItemJobTitleType0', None, Unset]):
            person_name (Union['KitchenSinkBulkProfileBodyProfilesItemPersonNameType0', None, Unset]):
            num_profiles (Union[Unset, int]):  Default: 1.
            profile_identifier (Union['KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0',
                'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1',
                'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2', None, Unset]):
            company_identifier (Union['KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0',
                'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1',
                'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2', None, Unset]):
            email_address (Union[None, Unset, str]):
     """

    company_domain: Union['KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0', None, Unset] = UNSET
    company_name: Union['KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0', None, Unset] = UNSET
    job_title: Union['KitchenSinkBulkProfileBodyProfilesItemJobTitleType0', None, Unset] = UNSET
    person_name: Union['KitchenSinkBulkProfileBodyProfilesItemPersonNameType0', None, Unset] = UNSET
    num_profiles: Union[Unset, int] = 1
    profile_identifier: Union['KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2', None, Unset] = UNSET
    company_identifier: Union['KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2', None, Unset] = UNSET
    email_address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_job_title_type_0 import KitchenSinkBulkProfileBodyProfilesItemJobTitleType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_domain_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_person_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemPersonNameType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0
        company_domain: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        elif isinstance(self.company_domain, KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0):
            company_domain = self.company_domain.to_dict()
        else:
            company_domain = self.company_domain

        company_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        elif isinstance(self.company_name, KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0):
            company_name = self.company_name.to_dict()
        else:
            company_name = self.company_name

        job_title: Union[None, Unset, dict[str, Any]]
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, KitchenSinkBulkProfileBodyProfilesItemJobTitleType0):
            job_title = self.job_title.to_dict()
        else:
            job_title = self.job_title

        person_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_name, Unset):
            person_name = UNSET
        elif isinstance(self.person_name, KitchenSinkBulkProfileBodyProfilesItemPersonNameType0):
            person_name = self.person_name.to_dict()
        else:
            person_name = self.person_name

        num_profiles = self.num_profiles

        profile_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.profile_identifier, Unset):
            profile_identifier = UNSET
        elif isinstance(self.profile_identifier, KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0):
            profile_identifier = self.profile_identifier.to_dict()
        elif isinstance(self.profile_identifier, KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1):
            profile_identifier = self.profile_identifier.to_dict()
        elif isinstance(self.profile_identifier, KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2):
            profile_identifier = self.profile_identifier.to_dict()
        else:
            profile_identifier = self.profile_identifier

        company_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.company_identifier, Unset):
            company_identifier = UNSET
        elif isinstance(self.company_identifier, KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2):
            company_identifier = self.company_identifier.to_dict()
        else:
            company_identifier = self.company_identifier

        email_address: Union[None, Unset, str]
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if num_profiles is not UNSET:
            field_dict["numProfiles"] = num_profiles
        if profile_identifier is not UNSET:
            field_dict["profileIdentifier"] = profile_identifier
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_2 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_job_title_type_0 import KitchenSinkBulkProfileBodyProfilesItemJobTitleType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_domain_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_person_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemPersonNameType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_1 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_company_name_type_0 import KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0
        from ..models.kitchen_sink_bulk_profile_body_profiles_item_profile_identifier_type_0 import KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0
        d = dict(src_dict)
        def _parse_company_domain(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_domain_type_0 = KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0.from_dict(data)



                return company_domain_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemCompanyDomainType0', None, Unset], data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))


        def _parse_company_name(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_name_type_0 = KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0.from_dict(data)



                return company_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemCompanyNameType0', None, Unset], data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_job_title(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemJobTitleType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_type_0 = KitchenSinkBulkProfileBodyProfilesItemJobTitleType0.from_dict(data)



                return job_title_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemJobTitleType0', None, Unset], data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        def _parse_person_name(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemPersonNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_name_type_0 = KitchenSinkBulkProfileBodyProfilesItemPersonNameType0.from_dict(data)



                return person_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemPersonNameType0', None, Unset], data)

        person_name = _parse_person_name(d.pop("personName", UNSET))


        num_profiles = d.pop("numProfiles", UNSET)

        def _parse_profile_identifier(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_0 = KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0.from_dict(data)



                return profile_identifier_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_1 = KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1.from_dict(data)



                return profile_identifier_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_2 = KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2.from_dict(data)



                return profile_identifier_type_2
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2', None, Unset], data)

        profile_identifier = _parse_profile_identifier(d.pop("profileIdentifier", UNSET))


        def _parse_company_identifier(data: object) -> Union['KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_0 = KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0.from_dict(data)



                return company_identifier_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_1 = KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1.from_dict(data)



                return company_identifier_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_2 = KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2.from_dict(data)



                return company_identifier_type_2
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType0', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1', 'KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2', None, Unset], data)

        company_identifier = _parse_company_identifier(d.pop("companyIdentifier", UNSET))


        def _parse_email_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))


        kitchen_sink_bulk_profile_body_profiles_item = cls(
            company_domain=company_domain,
            company_name=company_name,
            job_title=job_title,
            person_name=person_name,
            num_profiles=num_profiles,
            profile_identifier=profile_identifier,
            company_identifier=company_identifier,
            email_address=email_address,
        )


        kitchen_sink_bulk_profile_body_profiles_item.additional_properties = d
        return kitchen_sink_bulk_profile_body_profiles_item

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
