from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_trigger_body_people_item_type_2_input_type import (
    GithubLookupTriggerBodyPeopleItemType2InputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupTriggerBodyPeopleItemType2")


@_attrs_define
class GithubLookupTriggerBodyPeopleItemType2:
    """
    Attributes:
        input_type (GithubLookupTriggerBodyPeopleItemType2InputType):
        full_name (str): The full name of the person whose GitHub profile you want to find.
        external_id (None | str | Unset): Your own ID to join results back
        company (None | str | Unset):
        job_title (None | str | Unset):
        school_name (None | str | Unset): School or university name
        work_email (None | str | Unset):
        linkedin_url (None | str | Unset):
    """

    input_type: GithubLookupTriggerBodyPeopleItemType2InputType
    full_name: str
    external_id: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    school_name: None | str | Unset = UNSET
    work_email: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type = self.input_type.value

        full_name = self.full_name

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        school_name: None | str | Unset
        if isinstance(self.school_name, Unset):
            school_name = UNSET
        else:
            school_name = self.school_name

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputType": input_type,
                "fullName": full_name,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if company is not UNSET:
            field_dict["company"] = company
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if school_name is not UNSET:
            field_dict["schoolName"] = school_name
        if work_email is not UNSET:
            field_dict["workEmail"] = work_email
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_type = GithubLookupTriggerBodyPeopleItemType2InputType(d.pop("inputType"))

        full_name = d.pop("fullName")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_school_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name = _parse_school_name(d.pop("schoolName", UNSET))

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("workEmail", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        github_lookup_trigger_body_people_item_type_2 = cls(
            input_type=input_type,
            full_name=full_name,
            external_id=external_id,
            company=company,
            job_title=job_title,
            school_name=school_name,
            work_email=work_email,
            linkedin_url=linkedin_url,
        )

        github_lookup_trigger_body_people_item_type_2.additional_properties = d
        return github_lookup_trigger_body_people_item_type_2

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
