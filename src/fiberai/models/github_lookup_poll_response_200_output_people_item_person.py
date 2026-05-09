from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupPollResponse200OutputPeopleItemPerson")


@_attrs_define
class GithubLookupPollResponse200OutputPeopleItemPerson:
    """The original input person.

    Attributes:
        full_name (str): The full name of the person.
        company (None | str | Unset): Company provided in the original input.
        job_title (None | str | Unset): Job title provided in the original input.
        work_email (None | str | Unset): Work email provided in the original input.
        linked_in_url (None | str | Unset): LinkedIn URL provided or resolved from the original input.
        linkedin_user_id (None | str | Unset): LinkedIn numeric user ID if provided in the original input.
        customer_provided_id (None | str | Unset): The external ID echoed back from the input for joining results to the
            original dataset.
    """

    full_name: str
    company: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    work_email: None | str | Unset = UNSET
    linked_in_url: None | str | Unset = UNSET
    linkedin_user_id: None | str | Unset = UNSET
    customer_provided_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

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

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        linked_in_url: None | str | Unset
        if isinstance(self.linked_in_url, Unset):
            linked_in_url = UNSET
        else:
            linked_in_url = self.linked_in_url

        linkedin_user_id: None | str | Unset
        if isinstance(self.linkedin_user_id, Unset):
            linkedin_user_id = UNSET
        else:
            linkedin_user_id = self.linkedin_user_id

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullName": full_name,
            }
        )
        if company is not UNSET:
            field_dict["company"] = company
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if work_email is not UNSET:
            field_dict["workEmail"] = work_email
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if linkedin_user_id is not UNSET:
            field_dict["linkedinUserId"] = linkedin_user_id
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName")

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

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("workEmail", UNSET))

        def _parse_linked_in_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl", UNSET))

        def _parse_linkedin_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_user_id = _parse_linkedin_user_id(d.pop("linkedinUserId", UNSET))

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        github_lookup_poll_response_200_output_people_item_person = cls(
            full_name=full_name,
            company=company,
            job_title=job_title,
            work_email=work_email,
            linked_in_url=linked_in_url,
            linkedin_user_id=linkedin_user_id,
            customer_provided_id=customer_provided_id,
        )

        github_lookup_poll_response_200_output_people_item_person.additional_properties = d
        return github_lookup_poll_response_200_output_people_item_person

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
