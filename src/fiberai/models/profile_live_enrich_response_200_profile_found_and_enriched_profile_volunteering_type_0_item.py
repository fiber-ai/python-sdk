from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVolunteeringType0Item")



@_attrs_define
class ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVolunteeringType0Item:
    """ 
        Attributes:
            role (Union[None, Unset, str]):
            is_current (Union[None, Unset, bool]):
            cause (Union[None, Unset, str]):
            summary (Union[None, Unset, str]):
            linkedin_company_id (Union[None, Unset, str]):
            company_name (Union[None, Unset, str]):
            start_date (Union[None, Unset, str]):
            end_date (Union[None, Unset, str]):
     """

    role: Union[None, Unset, str] = UNSET
    is_current: Union[None, Unset, bool] = UNSET
    cause: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    linkedin_company_id: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        is_current: Union[None, Unset, bool]
        if isinstance(self.is_current, Unset):
            is_current = UNSET
        else:
            is_current = self.is_current

        cause: Union[None, Unset, str]
        if isinstance(self.cause, Unset):
            cause = UNSET
        else:
            cause = self.cause

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

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if role is not UNSET:
            field_dict["role"] = role
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if cause is not UNSET:
            field_dict["cause"] = cause
        if summary is not UNSET:
            field_dict["summary"] = summary
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))


        def _parse_is_current(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_current = _parse_is_current(d.pop("is_current", UNSET))


        def _parse_cause(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cause = _parse_cause(d.pop("cause", UNSET))


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


        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))


        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        profile_live_enrich_response_200_profile_found_and_enriched_profile_volunteering_type_0_item = cls(
            role=role,
            is_current=is_current,
            cause=cause,
            summary=summary,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            start_date=start_date,
            end_date=end_date,
        )


        profile_live_enrich_response_200_profile_found_and_enriched_profile_volunteering_type_0_item.additional_properties = d
        return profile_live_enrich_response_200_profile_found_and_enriched_profile_volunteering_type_0_item

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
