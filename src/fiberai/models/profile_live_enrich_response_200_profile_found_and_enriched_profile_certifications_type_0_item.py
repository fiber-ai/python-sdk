from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileCertificationsType0Item")



@_attrs_define
class ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileCertificationsType0Item:
    """ 
        Attributes:
            title (Union[None, Unset, str]):
            credential_id (Union[None, Unset, str]):
            verify_url (Union[None, Unset, str]):
            summary (Union[None, Unset, str]):
            linkedin_company_id (Union[None, Unset, str]):
            company_name (Union[None, Unset, str]):
            date (Union[None, Unset, str]):
     """

    title: Union[None, Unset, str] = UNSET
    credential_id: Union[None, Unset, str] = UNSET
    verify_url: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    linkedin_company_id: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        credential_id: Union[None, Unset, str]
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        else:
            credential_id = self.credential_id

        verify_url: Union[None, Unset, str]
        if isinstance(self.verify_url, Unset):
            verify_url = UNSET
        else:
            verify_url = self.verify_url

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        linkedin_company_id: Union[None, Unset, str]
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if verify_url is not UNSET:
            field_dict["verify_url"] = verify_url
        if summary is not UNSET:
            field_dict["summary"] = summary
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_credential_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        credential_id = _parse_credential_id(d.pop("credential_id", UNSET))


        def _parse_verify_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        verify_url = _parse_verify_url(d.pop("verify_url", UNSET))


        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_linkedin_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))


        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))


        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))


        profile_live_enrich_response_200_profile_found_and_enriched_profile_certifications_type_0_item = cls(
            title=title,
            credential_id=credential_id,
            verify_url=verify_url,
            summary=summary,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            date=date,
        )


        profile_live_enrich_response_200_profile_found_and_enriched_profile_certifications_type_0_item.additional_properties = d
        return profile_live_enrich_response_200_profile_found_and_enriched_profile_certifications_type_0_item

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
